---
id: TC-AC-DC-E2E-068-changelog-filter-kombinasi-penuh-dan-reset-halaman
title: "Modal Changelog Category: Kombinasi Search, Filter, Sort, Pagination, dan Reset Halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-184
  - TC-AC-DC-185
  - TC-AC-DC-186
  - TC-AC-DC-276
coverage:
  web: automated
---

# Modal Changelog Category: Kombinasi Search, Filter, Sort, Pagination, dan Reset Halaman

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- State global yang diubah dan dipulihkan: preferensi kolom modal Changelog di browser aktor; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE, bukan `[Reset to Default]`) dan Changelog dipulihkan ke No 17.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-184: Kombinasi penuh Search, Filter, Sort, dan Pagination berlaku bersamaan

1. Klik ikon Changelog pada header Sidebar Category
2. Ketik Search `kit`, tekan Enter
3. Klik ikon Filter, buka dropdown Action, centang "Create", klik `[Apply]`
4. Klik header Category sekali
5. Ubah page size menjadi 25
6. Verifikasi tabel menampilkan 3 baris: `Gateway Kit`, `Kit Lama`, `Kit Lama Anak`
7. Verifikasi ketiga baris berurutan Category A-Z
8. Verifikasi page size 25 aktif
9. Verifikasi kata kunci "kit" tetap aktif
10. Verifikasi filter Action "Create" tetap aktif
11. Verifikasi sort Category ascending tetap aktif

### TC-AC-DC-185: Pemulihan dari hasil kosong setelah salah satu kontrol dilepas

12. Tutup modal lewat icon `[×]`, lalu klik ikon Changelog pada header Sidebar Category
13. Ketik Search `scan`, tekan Enter
14. Verifikasi tabel menampilkan 3 baris yang mengandung "scan"
15. Klik ikon Filter, buka dropdown Action, centang "Delete", klik `[Apply]`
16. Verifikasi kombinasi menghasilkan 0 baris (tidak ada Delete yang mengandung "scan")
17. Klik ikon Filter, klik `[Clear Field]`, klik `[Apply]`
18. Verifikasi tabel pulih menampilkan 3 baris yang mengandung "scan"

### TC-AC-DC-186: Kriteria Search atau Filter berubah mereset paginasi ke halaman 1

19. Tutup modal lewat icon `[×]`, lalu klik ikon Changelog pada header Sidebar Category
20. Klik halaman 2 pada pagination
21. Verifikasi halaman 2 menampilkan 2 baris
22. Ketik Search `kit`, tekan Enter
23. Verifikasi tabel kembali ke halaman 1
24. Verifikasi tabel menampilkan 6 hasil
25. Kosongkan isi kotak search, tekan Enter
26. Klik halaman 2 pada pagination
27. Klik ikon Filter, buka dropdown Action, centang "Delete", klik `[Apply]`
28. Verifikasi tabel kembali ke halaman 1
29. Verifikasi tabel menampilkan 3 hasil Delete

### TC-AC-DC-276: Filter Changelog tetap tersedia dan tetap berlaku setelah kolomnya disembunyikan

30. Tutup modal lewat icon `[×]`, lalu klik ikon Changelog pada header Sidebar Category
31. Klik ikon Filter, buka dropdown Modified By, centang "Maya P", klik `[Apply]`
32. Klik ikon `⋯` pada header kolom Actions, uncheck kolom Modified By
33. Buka kembali Filter Panel
34. Verifikasi tabel tetap menampilkan 6 baris yang dilakukan Maya P setelah kolom Modified By disembunyikan
35. Verifikasi field Modified By tetap ada di Filter Panel
36. Verifikasi pilihan "Maya P" pada field Modified By tercentang
37. Klik ikon `⋯` pada header kolom Actions, check kembali kolom Modified By

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-184, 185, 186, 276). Tidak ada TC hanya-BE di spec ini.
- Penutupan dan pembukaan ulang modal dipakai sebagai langkah pembersih state Search, Filter, Sort, dan Pagination (NC-11).
- Alasan melewati sekitar 35 langkah: seluruh blok satu kelas harness (fungsional, satu permukaan Search, Filter, Sort, dan Pagination modal Changelog) dan tiap TC dimulai dari state yang direset lewat tutup-buka modal, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah dari TC): langkah 12, 19, 25, 30, 37.
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - TC-AC-DC-186 langkah 5 'Kosongkan pencarian dengan Enter pada input kosong' ditulis 'Kosongkan isi kotak search, tekan Enter' (8b.9); TC-AC-DC-186 tidak menyebut indikator 'halaman 1' selain pagination, spec membaca penanda halaman aktif pada pagination.
  - TC-AC-DC-276 menyembunyikan kolom Modified By lewat Column Visibility; preferensi kolom dipulihkan pada langkah terakhir dan di hook `after`.
