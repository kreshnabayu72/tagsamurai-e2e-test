---
id: TC-AC-DC-E2E-076-changelog-pagination
title: "Modal Changelog Category: Pagination, Navigasi Halaman, dan Page Size"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-206
  - TC-AC-DC-207
  - TC-AC-DC-208
coverage:
  web: automated
---

# Modal Changelog Category: Pagination, Navigasi Halaman, dan Page Size

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-206: Pagination default 10 per halaman dengan opsi 10, 25, 50, dan 100

1. Klik ikon Changelog pada header Sidebar Category
2. Verifikasi halaman 1 menampilkan 10 baris
3. Klik halaman 2 pada pagination
4. Verifikasi halaman 2 menampilkan 2 baris
5. Klik halaman 1 pada pagination
6. Buka selector page size
7. Verifikasi opsi page size tepat 10, 25, 50, 100
8. Verifikasi selector page size tidak memuat opsi "All"
9. Pilih 25
10. Verifikasi seluruh 12 baris tampil dalam satu halaman
11. Verifikasi tabel berada di halaman 1

### TC-AC-DC-207: Navigasi halaman: Next, Prev, input nomor halaman, dan input tidak valid diabaikan

12. Tutup modal lewat icon `[×]`, lalu klik ikon Changelog pada header Sidebar Category
13. Klik Next
14. Verifikasi halaman 2 tampil berisi `Gateway Kit` dan `Scanner`
15. Klik Prev
16. Verifikasi halaman 1 tampil
17. Ketik 2 pada input nomor halaman, tekan Enter
18. Verifikasi halaman 2 tampil berisi `Gateway Kit` dan `Scanner`
19. Ketik 0 pada input nomor halaman, tekan Enter
20. Verifikasi input 0 diabaikan; tabel tetap pada halaman 2
21. Ketik 99 pada input nomor halaman, tekan Enter
22. Verifikasi input 99 diabaikan; tabel tetap pada halaman 2
23. Ketik "abc" pada input nomor halaman, tekan Enter
24. Verifikasi input "abc" diabaikan; tabel tetap pada halaman 2

### TC-AC-DC-208: Mengganti page size kembali ke halaman 1

25. Ubah page size menjadi 25
26. Verifikasi tabel kembali ke halaman 1
27. Verifikasi tabel menampilkan seluruh 12 baris

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-206, 207, 208). Tidak ada TC hanya-BE di spec ini.
- TC-AC-DC-208 melanjutkan halaman 2 dari TC-AC-DC-207 (langkah 'Klik halaman 2' sudah terpenuhi); tidak ada langkah tambahan.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah dari TC): langkah 5, 12.
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - TC-AC-DC-207 butir b tidak menyebut halaman mana yang aktif saat input tidak valid; spec mengasumsikan halaman 2 (hasil input 2 sebelumnya).
