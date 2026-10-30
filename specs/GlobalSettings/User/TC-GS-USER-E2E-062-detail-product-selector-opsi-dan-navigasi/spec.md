---
id: TC-GS-USER-E2E-062-detail-product-selector-opsi-dan-navigasi
title: "User Detail: Product Selector (Default Global Settings, Opsi Fixed Asset dan Supply Asset, Produk yang Pernah Dicabut, Hidden bagi Aktor tanpa Hak Read, dan Navigasi Penuh ke Fixed Asset)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-367
  - TC-GS-USER-368
  - TC-GS-USER-369
  - TC-GS-USER-370
coverage:
  web: automated
---

# User Detail: Product Selector (Default Global Settings, Opsi Fixed Asset dan Supply Asset, Produk yang Pernah Dicabut, Hidden bagi Aktor tanpa Hak Read, dan Navigasi Penuh ke Fixed Asset)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor (ganti akun eksplisit di Test Steps):
  - Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`): aktor pertama, login di hook `before` (akun default suite).
  - Manage user and role (Full CRUD) (Fajar Nugroho) `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (No. 4; kredensial `Spectra.env.GS_FULLCRUD_PASSWORD`): dipakai TC-GS-USER-369.
  - Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (dibaca, tidak diubah): Joko Susilo (No. 19; Access Fixed Asset + Supply Asset) untuk TC-GS-USER-367, 369, dan 370.
- Data Dinamis, di-seed lewat API di hook `before` dan dihapus di hook `after`: `Jane Smith {runId}-062`, email `janesmith+{runId}-062@qwertysystem.net`, Activated; Access `Fixed Asset` di-grant lalu dicabut (tercatat di Changelog App Access) untuk TC-GS-USER-368. Tabel Pre-setup mencatat Jane Smith (No. 17) hanya dengan Access Supply Asset, sehingga TC-GS-USER-368 memakai user seed milik spec.
- Kemampuan teknis (disediakan tim FE/BE): seeding user dengan grant lalu pencabutan Access `Fixed Asset` lewat API (nama endpoint ditentukan tim FE di tahap script); Fixed Asset memiliki modul Settings > User sedangkan Supply Asset belum (TC-GS-USER-367); akun Fajar Nugroho tidak punya izin Read Settings > User di Fixed Asset (TC-GS-USER-369 precondition c; Tabel Pre-setup tidak menyebut izin Fixed Asset akun ini).
- State global yang diubah: tidak ada. Hook `after` menghapus user seed dan mengembalikan sesi ke akun default suite (tetap berjalan walau spec gagal di tengah).

## Test Steps

### TC-GS-USER-367: Product Selector default Global Settings dan opsi produk Access

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Klik icon Search, ketik `Joko Susilo`, tekan Enter
3. Klik Name `Joko Susilo` di User List
4. Verifikasi Product Selector `Viewing:` menampilkan nilai default `Global Settings`
5. Klik `Viewing: [Global Settings ▾]`
6. Verifikasi opsi `Fixed Asset` tampil (Access aktif dan modul Settings > User tersedia)
7. Verifikasi opsi `Supply Asset` tidak tampil (modul Settings > User belum ada)
8. Tekan Esc untuk menutup Product Selector

### TC-GS-USER-368: Product Selector memuat produk yang pernah di-grant lalu dicabut

9. Klik menu User di sidebar Global Settings
10. Klik icon Search, ketik `Jane Smith {runId}-062`, tekan Enter
11. Klik Name `Jane Smith {runId}-062` di User List
12. Klik Product Selector
13. Verifikasi opsi `Fixed Asset` tetap tampil
14. Tekan Esc untuk menutup Product Selector

### TC-GS-USER-370: Klik opsi Product Selector navigasi penuh ke Detail User produk tujuan

15. Klik menu User di sidebar Global Settings
16. Klik icon Search, ketik `Joko Susilo`, tekan Enter
17. Klik Name `Joko Susilo` di User List
18. Klik Product Selector
19. Klik opsi `Fixed Asset`
20. Verifikasi navigasi penuh terjadi tanpa dialog konfirmasi
21. Verifikasi halaman tujuan adalah Fixed Asset > Settings > User > Detail milik Joko Susilo

### TC-GS-USER-369: Product Selector menyembunyikan produk yang aktor tidak boleh Read

22. Logout, lalu login sebagai Manage user and role (Full CRUD)
23. Buka Global Settings > User > User List (sub-tab Login User)
24. Klik icon Search, ketik `Joko Susilo`, tekan Enter
25. Klik Name `Joko Susilo` di User List
26. Klik Product Selector
27. Verifikasi opsi `Global Settings` tampil di Product Selector
28. Verifikasi opsi `Fixed Asset` Hidden (tidak ditampilkan, bukan tampil disabled)

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Urutan TC sumber diubah: TC-GS-USER-370 mendahului TC-GS-USER-369 karena TC-GS-USER-370 meninggalkan Global Settings (menuju Fixed Asset) dan TC-GS-USER-369 memerlukan ganti akun; ganti akun dilakukan sekali di akhir.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8 dan 14 (menutup Product Selector), 9 sampai 10, 15 sampai 16 (kembali ke User List dan mencari user target), 22 sampai 23 (ganti akun dan membuka User List), 24 (Search nama target).
- Anchor absence (bagian 8b butir 2): langkah 6 (opsi `Fixed Asset` tampil di Product Selector yang sama) mendahului langkah 7; langkah 27 (opsi `Global Settings` tampil di Product Selector akun Fajar Nugroho) mendahului langkah 28. Langkah 4 (nilai default sebelum Product Selector dibuka) mengikuti Expected TC-GS-USER-367 a. Langkah 27 tidak ada di TC dan ditambahkan hanya sebagai anchor; kehadiran opsi `Global Settings` di daftar tidak disebut TC.
- Langkah 20 (tanpa dialog konfirmasi) dan 21 (halaman tujuan) mengikuti Expected TC-GS-USER-370. Tampilan halaman tujuan diuji di TC fixed-asset/settings-user (Post Condition TC-GS-USER-370, tanpa langkah observasi di TC ini).
- Temuan untuk QA:
  - TC-GS-USER-368 precondition c ("Access Fixed Asset Jane Smith pernah ada lalu dicabut") tidak sesuai Tabel Pre-setup No. 17 (Jane Smith hanya Access Supply Asset); spec memakai user seed milik spec dengan nama bersuffix.
  - TC-GS-USER-369 precondition c ("Aktor tidak punya izin Read Settings > User di Fixed Asset") tidak ada di Tabel Pre-setup untuk Fajar Nugroho; disediakan tim FE/BE.
  - TC-GS-USER-370 Expected tidak menyebut cara memverifikasi halaman tujuan (URL atau judul halaman); spec mengasersi halaman Fixed Asset > Settings > User > Detail Joko Susilo terbuka.
