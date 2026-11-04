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
- Data Pre-setup #26 (fixture tabel sesi, dipulihkan fixture BE di hook `before`): tepat lima sesi cuplikan Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso pada client Paid Pre-setup #1; Online Users 5/25. Identitas dan nilai data dirujuk lewat `Fixture.fixedAssetLicense.sesiTabel` (berkas fixture belum ada, disiapkan tim FE).
- Data Pre-setup #17 (hanya dibaca, tidak diubah): delapan Custom Field aktif pada client, termasuk `Cost Center` (Dropdown) dan `Joining Date` (Date); 13 kolom data bawaan ditambah 8 Custom Field menjadi 21 kolom pada Tab Concurrent User (TC-FA-LIC-293). Identitas dan nilai data dirujuk lewat `Fixture.fixedAssetLicense.customField` (berkas fixture belum ada, disiapkan tim FE); Custom Field Pre-setup #17 tidak dinonaktifkan atau dihapus oleh spec ini.
- Data Dinamis (S-06, S-12): dua Custom Field milik spec, `Cost Center+{runId}-139` (Dropdown) dan `Joining Date+{runId}-139` (Date), dibuat lewat fixture BE pada langkah 8 (disediakan tim FE/BE; TC tidak menyebut mekanisme pembuatan) dan dihapus lewat fixture BE di hook `after` bila masih ada (idempotent; tidak berasumsi setup berhasil penuh). TC-FA-LIC-541 menonaktifkan `Cost Center+{runId}-139` dan menghapus `Joining Date+{runId}-139` sebagai pengganti Custom Field Pre-setup #17 bernama `Cost Center` dan `Joining Date`. Kedua Custom Field itu baru ada sesudah langkah 8, sehingga TC-FA-LIC-293 (langkah 1 sampai 7) tetap mengukur 21 kolom.
- Konfigurasi kolom: spec ini menyimpan Setup Column di browser (langkah 11); hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (dinyatakan di `suite.md`; kemampuan disediakan tim FE).
- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih Pre-setup #26; pemulihan konfigurasi kolom. Kemampuan teknis: membaca tooltip checkbox disabled; membuka Global Settings > User > Custom Field dengan akun yang sama; membuat dan menghapus Custom Field milik spec lewat fixture BE (disediakan tim FE/BE).

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

8. Buat Custom Field milik spec `Cost Center+{runId}-139` (Dropdown) dan `Joining Date+{runId}-139` (Date) lewat fixture BE hingga tersimpan
9. Muat ulang halaman License, lalu klik tab Concurrent User
10. Buka Popup Setup Column, lalu centang kolom `Cost Center+{runId}-139` dan `Joining Date+{runId}-139`
11. Klik `[Save]`
12. Verifikasi kolom `Cost Center+{runId}-139` tampil pada tabel
13. Verifikasi kolom `Joining Date+{runId}-139` tampil pada tabel
14. Buka Global Settings > User > Custom Field
15. Ketik Search `Cost Center+{runId}-139`, tekan Enter
16. Deactivate `Cost Center+{runId}-139`, lalu konfirmasi dialog
17. Ganti isi kotak search dengan `Joining Date+{runId}-139`, tekan Enter
18. Delete `Joining Date+{runId}-139`, lalu konfirmasi dialog
19. Tunggu aksi selesai
20. Buka kembali Fixed Asset > License > tab Concurrent User
21. Verifikasi kolom `User Name` tampil pada tabel (tabel selesai dimuat)
22. Verifikasi kolom `Cost Center+{runId}-139` tidak ada pada tabel
23. Verifikasi kolom `Joining Date+{runId}-139` tidak ada pada tabel
24. Buka Popup Setup Column
25. Verifikasi daftar Setup Column memuat kolom `User Name` dan tidak memuat `Cost Center+{runId}-139`
26. Verifikasi daftar Setup Column tidak memuat `Joining Date+{runId}-139`
27. Klik `(×)` untuk menutup popup tanpa menyimpan

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 9 (memuat ulang halaman License setelah fixture BE membuat Custom Field), menutup popup dengan `(×)` (S-09), membuka Global Settings > User > Custom Field, dan membuka kembali tab Concurrent User. Aksi yang menghapus data (Deactivate dan Delete Custom Field) berada di akhir spec (S-10).
- Verifikasi kolom `User Name` tampil pada langkah sebelum asersi absence adalah anchor positif (butir 2 bagian 8b) dan bukan asersi dari TC.
- Langkah 15 dan 17 mencari baris Custom Field target lewat Search (R-16, bagian 8b butir 13) karena daftar Custom Field dapat memuat lebih dari satu halaman; langkah 19 menunggu aksi Deactivate dan Delete selesai sebelum berpindah surface (bagian 8b butir 8). Asersi absence kolom memakai nama bersuffix persis (`Cost Center+{runId}-139`, `Joining Date+{runId}-139`); kolom Pre-setup `Cost Center` dan `Joining Date` tidak diubah.
- Pemulihan Setup Column (bagian 8b butir 14, S-03): kolom yang dicentang dan disimpan pada langkah 10 dan 11 adalah kolom Custom Field milik spec yang dinonaktifkan pada langkah 16 dan dihapus pada langkah 18, sehingga tidak ada kolom yang dapat dipulihkan dengan langkah eksplisit tanpa membuat asersi absence langkah 22 dan 23 lulus semu; konfigurasi kolom dibersihkan hook `after`.
- Temuan untuk QA: TC-FA-LIC-541 tidak menyebut teks dialog konfirmasi Deactivate dan Delete di Global Settings > User > Custom Field; spec hanya menulis "konfirmasi dialog" tanpa asersi teks. TC-FA-LIC-293 menyebut "Delapan Custom Field aktif dibuat" tanpa mekanisme pembuatan; kondisi itu dinyatakan sebagai Pre-setup #17 yang disediakan tim FE/BE. TC-FA-LIC-541 menyebut Custom Field Pre-setup #17 (`Cost Center`, `Joining Date`) sebagai objek Deactivate dan Delete; spec memakai Custom Field milik spec bernama bersuffix karena S-06 melarang mengubah Pre-setup bersama, dan mekanisme pembuatannya tidak disebut TC. Search di halaman Custom Field Global Settings (langkah 15 dan 17) belum terbukti di UI; spec mengasumsikannya, konfirmasi tim FE.
