---
id: TC-AC-DC-E2E-067-changelog-filter-clear-apply-dan-search
title: "Modal Changelog Category: Clear Field, Apply, Indikator Filter, dan Kombinasi dengan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-179
  - TC-AC-DC-180
  - TC-AC-DC-181
  - TC-AC-DC-182
  - TC-AC-DC-183
coverage:
  web: automated
---

# Modal Changelog Category: Clear Field, Apply, Indikator Filter, dan Kombinasi dengan Search

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-179: Clear Field pada Filter Panel melepas filter tanpa mereset Search dan Sort

1. Klik ikon Changelog pada header Sidebar Category
2. Ketik Search `kit`, tekan Enter
3. Klik header Category sekali
4. Klik ikon Filter, buka dropdown Action, centang "Create", klik `[Apply]`
5. Verifikasi tabel menampilkan 3 baris Create dengan "kit" (`Gateway Kit`, `Kit Lama`, `Kit Lama Anak`)
6. Verifikasi ketiga baris berurutan Category A-Z
7. Klik ikon Filter, klik `[Clear Field]`, klik `[Apply]`
8. Verifikasi tabel menampilkan 6 baris yang mengandung "kit"
9. Verifikasi kata kunci "kit" tetap aktif di kotak pencarian
10. Verifikasi urutan Category ascending tetap aktif

### TC-AC-DC-180: Menutup Filter Panel tanpa Apply membuang perubahan yang belum di-Apply

11. Tutup modal lewat icon `[×]`, lalu klik ikon Changelog pada header Sidebar Category
12. Klik ikon Filter, buka dropdown Action, centang "Edit" tanpa klik `[Apply]`
13. Klik ikon Filter lagi untuk menutup panel
14. Klik ikon Filter lagi untuk membuka panel
15. Verifikasi tabel menampilkan 10 baris pada halaman 1 dari 12 entri
16. Verifikasi panel menampilkan nilai filter yang terakhir di-Apply (kosong), bukan pilihan "Edit" yang belum di-Apply

### TC-AC-DC-181: Ikon Filter menampilkan indikator titik selama ada filter ter-Apply

17. Buka dropdown Action, centang "Edit", klik `[Apply]`
18. Klik ikon Filter untuk menutup panel
19. Verifikasi ikon Filter menampilkan badge titik saat panel tertutup
20. Klik ikon Filter untuk membuka panel
21. Verifikasi ikon Filter menampilkan badge titik saat panel terbuka
22. Klik `[Clear Field]`, klik `[Apply]`
23. Verifikasi badge titik pada ikon Filter hilang

### TC-AC-DC-182: Alur Search lalu Filter menghasilkan irisan

24. Ketik Search `kit`, tekan Enter
25. Klik ikon Filter, buka dropdown Action, centang "Create", klik `[Apply]`
26. Verifikasi tabel menampilkan 3 baris Create (`Gateway Kit`, `Kit Lama`, `Kit Lama Anak`)
27. Verifikasi kata kunci "kit" di kotak pencarian tidak ter-reset oleh penerapan filter

### TC-AC-DC-183: Alur Filter lalu Search menghasilkan irisan yang identik

28. Klik icon panah `(←)` di kiri toolbar untuk mereset pencarian
29. Klik ikon Filter, klik `[Clear Field]`, klik `[Apply]`
30. Klik ikon Filter, buka dropdown Action, centang "Create", klik `[Apply]`
31. Ketik Search `kit`, tekan Enter
32. Verifikasi tabel menampilkan 3 baris yang sama dengan alur Search lalu Filter (`Gateway Kit`, `Kit Lama`, `Kit Lama Anak`)
33. Verifikasi filter Action "Create" tetap aktif

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-179, 180, 181, 182, 183). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah dari TC): langkah 11, 28, 29.
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - TC-AC-DC-180 dan 181 menulis 'klik ikon Filter lagi untuk menutup panel' tanpa menyebut apakah `[Apply]` sudah menutup panel; spec mengikuti kalimat TC (ikon Filter bersifat toggle).
  - TC-AC-DC-179 sampai 183 melanjutkan state akhir TC sebelumnya tanpa mengosongkannya; spec menambah langkah pembersih (S-09).
