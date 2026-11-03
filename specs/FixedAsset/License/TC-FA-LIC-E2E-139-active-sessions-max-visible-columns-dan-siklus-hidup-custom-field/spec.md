---
id: TC-FA-LIC-E2E-139-active-sessions-max-visible-columns-dan-siklus-hidup-custom-field
title: "Active Sessions: Max Visible Columns Setup Column dan Kolom Custom Field Hilang Saat Deactivate atau Delete"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-293
  - TC-FA-LIC-541
coverage:
  web: automated
---

# Active Sessions: Max Visible Columns Setup Column dan Kolom Custom Field Hilang Saat Deactivate atau Delete

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #26 (fixture tabel sesi, dipulihkan fixture BE di hook `before`): tepat lima sesi cuplikan Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso pada client Paid Pre-setup #1; Online Users 5/25.
- Data Pre-setup #17: delapan Custom Field aktif pada client, termasuk `Cost Center` (Dropdown) dan `Joining Date` (Date); 13 kolom data bawaan ditambah 8 Custom Field menjadi 21 kolom pada Tab Concurrent User. Identitas dan nilai data dirujuk lewat fixture `fixtures/fixed-asset-license.json` (belum ada, disiapkan tim FE).
- Fixture BE pemulih Pre-setup #17 (delapan Custom Field aktif): dijalankan di hook `before` dan `after` spec ini; disediakan tim FE/BE (idempotent). TC-FA-LIC-541 menonaktifkan `Cost Center` dan menghapus `Joining Date`; hook `after` memulihkan keduanya. Efek pada Global Settings: Last Updated Custom Field berubah dan Custom Field `Joining Date` dibuat ulang oleh fixture.
- Data Dinamis: tidak ada.
- Konfigurasi kolom: spec ini menyimpan Setup Column di browser; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (dinyatakan di `suite.md`; kemampuan disediakan tim FE).
- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #26; pemulihan konfigurasi kolom. Kemampuan teknis: membaca tooltip checkbox disabled; membuka Global Settings > User > Custom Field dengan akun yang sama.

## Test Steps

### TC-FA-LIC-293: Max Visible Columns pada Setup Column Tab Concurrent User

1. Klik tab Concurrent User
2. Buka Popup Setup Column lewat header kolom Actions `⋯` lalu `Setup Column...`
3. Centang semua kolom sampai 20 kolom tercentang
4. Arahkan kursor ke checkbox kolom ke-21
5. Verifikasi checkbox kolom yang belum tercentang disabled saat 20 kolom tercentang
6. Verifikasi tooltip `Maximum 20 columns can be shown at once. Uncheck another column first.`
7. Klik `(×)` untuk menutup popup tanpa menyimpan

### TC-FA-LIC-541: Deactivate atau Delete Custom Field membuat kolom Custom Field aktif hilang dari tabel Active Sessions dan Setup Column

8. Buka Popup Setup Column, lalu centang kolom `Cost Center` dan `Joining Date`
9. Klik `[Save]`
10. Verifikasi kolom `Cost Center` tampil pada tabel
11. Verifikasi kolom `Joining Date` tampil pada tabel
12. Buka Global Settings > User > Custom Field
13. Deactivate `Cost Center`, lalu konfirmasi dialog
14. Delete `Joining Date`, lalu konfirmasi dialog
15. Buka kembali Fixed Asset > License > tab Concurrent User
16. Verifikasi kolom `User Name` tampil pada tabel (tabel selesai dimuat)
17. Verifikasi kolom `Cost Center` tidak ada pada tabel
18. Verifikasi kolom `Joining Date` tidak ada pada tabel
19. Buka Popup Setup Column
20. Verifikasi daftar Setup Column memuat kolom `User Name` dan tidak memuat `Cost Center`
21. Verifikasi daftar Setup Column tidak memuat `Joining Date`
22. Klik `(×)` untuk menutup popup tanpa menyimpan

## Notes

- Langkah penghubung tanpa `Verifikasi`: menutup popup dengan `(×)` (S-09), membuka Global Settings > User > Custom Field, dan membuka kembali tab Concurrent User. Aksi yang menghapus data (Deactivate dan Delete Custom Field) berada di akhir spec (S-10).
- Verifikasi kolom `User Name` tampil pada langkah sebelum asersi absence adalah anchor positif (butir 2 bagian 8b) dan bukan asersi dari TC.
- Temuan untuk QA: TC-FA-LIC-541 tidak menyebut teks dialog konfirmasi Deactivate dan Delete di Global Settings > User > Custom Field; spec hanya menulis "konfirmasi dialog" tanpa asersi teks. TC-FA-LIC-293 menyebut "Delapan Custom Field aktif dibuat" tanpa mekanisme pembuatan; dinyatakan sebagai fixture pemulih Pre-setup #17 yang disediakan tim FE/BE.
