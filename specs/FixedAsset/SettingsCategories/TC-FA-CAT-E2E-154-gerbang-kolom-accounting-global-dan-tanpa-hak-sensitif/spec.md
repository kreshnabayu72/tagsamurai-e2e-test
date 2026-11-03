---
id: TC-FA-CAT-E2E-154-gerbang-kolom-accounting-global-dan-tanpa-hak-sensitif
title: "Gerbang Kolom Popup Detail: Accounting Global Melihat Nilai Client-wide dan Aktor Tanpa Hak Nilai Sensitif Melihat Seluruh Sel No access"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-670
  - TC-FA-CAT-672
coverage:
  web: automated
---

# Gerbang Kolom Popup Detail: Accounting Global Melihat Nilai Client-wide dan Aktor Tanpa Hak Nilai Sensitif Melihat Seluruh Sel No access

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Accounting Global (Pre-setup #52) `accountingGlobal_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_ACCGL_PASSWORD` (Manage Asset Master Data: R; Global Role Manage accounting; tanpa Group Role View asset value dan Manage purchase; lisensi FA-7 aktif). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua: Tanpa Hak Nilai Sensitif (Pre-setup #54) `noSensitive_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_NOSENS_PASSWORD` (Manage Asset Master Data: R; tanpa View asset value, Manage purchase, dan Manage accounting). Login lewat langkah Ganti akun eksplisit (langkah 12). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_ACCGL_PASSWORD` dan `FA_NOSENS_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup yang hanya dibaca (tidak diubah): Pre-setup #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), #22 (aset `Laptop Dell - 1` sampai `- 8`, `Laptop HP - 1` sampai `- 4`), #55 (Asset Value `Laptop Dell - 1` 15000000.00 dan `Laptop HP - 3` 20000000.00 pada group `Region Jawa > Jakarta Selatan Distribution Center`), #56 (Custom Field General `Warna Casing` dengan `Laptop Dell - 1` `Silver`; Purchasing `Nilai Kontrak`, `Nomor Kontrak Dell`, `Nomor PO`; Accounting `Kode Anggaran` dengan `Laptop Dell - 1` `ANG-01`, `Laptop Dell - 2` dan `Laptop HP - 3` tanpa nilai, lisensi FA-7 aktif).
- Kemampuan teknis: pemulihan konfigurasi kolom Setup Column dengan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`), dipakai sebagai langkah penghubung dan di hook `after` suite; disediakan tim FE.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite (termasuk untuk akun kedua).
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-670: Accounting Global, nilai client-wide untuk Asset Value dan Kode Anggaran, Warranty dan Purchasing tidak

1. Pilih node `Electronics` pada sidebar
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
3. Klik header Actions (⋯) > `Setup Column...`
4. Verifikasi daftar kolom Custom Field memuat `Kode Anggaran` (Accounting)
5. Verifikasi daftar kolom Custom Field tidak memuat kolom Purchasing `Nilai Kontrak`, `Nomor Kontrak Dell`, dan `Nomor PO`
6. Centang `Asset Value`, `Warranty Expiry`, dan `Kode Anggaran`, lalu klik `[Save]`
7. Verifikasi sel Asset Value `Laptop Dell - 1` dan `Laptop HP - 3` menampilkan nilai walau group `Region Jawa` (Manage accounting berlaku client-wide)
8. Verifikasi sel Warranty Expiry menampilkan `No access` pada seluruh baris
9. Verifikasi sel `Kode Anggaran` `Laptop Dell - 1` menampilkan `ANG-01`
10. Verifikasi sel `Kode Anggaran` `Laptop Dell - 2` dan `Laptop HP - 3` menampilkan `—`
11. Tutup Popup Detail dan pulihkan konfigurasi kolom tabel Assets dengan menghapus preferensi kolom di browser

### TC-FA-CAT-672: Aktor tanpa hak nilai sensitif, kolom Asset Value dan Warranty ada tetapi seluruh sel No access

12. Ganti akun: logout, login sebagai Tanpa Hak Nilai Sensitif (Pre-setup #54) dengan `Spectra.env.FA_NOSENS_PASSWORD`, lalu buka Fixed Asset > Settings > Categories
13. Pilih node `Electronics` pada sidebar
14. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
15. Klik header Actions (⋯) > `Setup Column...`
16. Verifikasi kolom `Asset Value` dan `Warranty Expiry` tersedia di Setup Column
17. Verifikasi kolom Custom Field Purchasing (`Nilai Kontrak`, `Nomor Kontrak Dell`, `Nomor PO`) dan Accounting (`Kode Anggaran`) tidak tersedia di Setup Column
18. Centang `Asset Value`, `Warranty Expiry`, dan `Warna Casing`, lalu klik `[Save]`
19. Verifikasi seluruh sel Asset Value dan Warranty Expiry menampilkan `No access`
20. Verifikasi sel `Warna Casing` `Laptop Dell - 1` menampilkan `Silver`
21. Hover sel `No access` pada Asset Value
22. Verifikasi tooltip `Requires View asset value access in this group.`
23. Hover sel `No access` pada Warranty Expiry
24. Verifikasi tooltip `Requires Manage purchase access in this group.`
25. Tutup Popup Detail dan pulihkan konfigurasi kolom tabel Assets dengan menghapus preferensi kolom di browser

## Notes

- Langkah penghubung (S-03, S-09): langkah 1, 13 (memilih node sidebar), langkah 11 dan 25 (menutup popup dan memulihkan konfigurasi kolom).
- Langkah 12 adalah Ganti akun eksplisit (S-07); spec bergerak dari akun pertama ke akun kedua sehingga bukan satu loop role (bagian 3a, langkah dan akun berbeda).
- Post Condition TC-FA-CAT-670 dan TC-FA-CAT-672 ("dikembalikan lewat `[Reset to Default]` lalu `[Save]`") dipenuhi dengan menghapus preferensi kolom di browser sesuai konvensi bagian 4; kemampuan disediakan tim FE.
- Asersi absence pada langkah 5 dan 17 diawali anchor positif pada surface yang sama (langkah 4 dan 16: kolom lain di daftar Setup Column tampil).
- Spec dengan tier Group Manager ada di spec 197 dan tier Total Control, Default User, serta Read Only di spec 198.
- Temuan untuk QA:
  - Nama env var password akun aktor tidak tertulis di TC; `FA_ACCGL_PASSWORD` dan `FA_NOSENS_PASSWORD` adalah usulan.
  - TC-FA-CAT-670 Expected b menyebut "menampilkan nilai" pada `Laptop Dell - 1` dan `Laptop HP - 3` tanpa angka; spec memverifikasi bahwa nilai tampil (bukan `No access`) dan tidak menambah angka dari Pre-setup #55.
  - TC-FA-CAT-670 langkah 1 menyebut baris `Laptop` "setelah memilih node `Electronics`"; spec mengikuti dengan langkah memilih node.
  - TC-FA-CAT-670 Expected d menyebut "keadaan lisensi FA-7 lain diuji di TC-FA-CAT-687"; TC itu di luar spec ini.
