---
id: TC-AC-ACTS-E2E-159-detail-sku-aria-label-sort-tag-code-mutasi-terfilter-siklus-toast-dan-ikon-combined
title: "Detail SKU Tab Available: Aria-Label Tabel, Sort TAG Code Tanpa Nilai Kosong dan Ikon Combined, Mutasi saat Terfilter, dan Siklus Toast"
priority: Low
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-29
  - TC-AC-ACTS-98
  - TC-AC-ACTS-101
  - TC-AC-ACTS-804
  - TC-AC-ACTS-901
coverage:
  web: automated
---

# Detail SKU Tab Available: Aria-Label Tabel, Sort TAG Code Tanpa Nilai Kosong dan Ikon Combined, Mutasi saat Terfilter, dan Siklus Toast

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Data Dinamis (Tabel Data Uji Dinamis #5) pada SKU `RFID-ASSET-CORE-R5` (Pre-setup #12): unit uji hapus milik spec, di-seed di hook `before` (idempoten) dan dipulihkan fixture BE di hook `after`: Available U1 (`TAG-4F7K2XQ9`), U2, U3; Damaged/Missing U4; Combined C1; Existing Record Subject Register Duplicate pending P1; Waiting for Approval W1 (tidak tampil di Tab Available, Subject ada di Approvals); In Use I1; pada SKU `NFC-CARD-BETA-N2` (Pre-setup #13): Available X1. Identifier unit tetap (tidak bersuffix `{runId}`; S-12): seeding idempoten, pemulihan lewat fixture BE sebelum spec ini, suite serial.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Data per blok TC: Tab Available memuat unit Available dan Damaged/Missing (TC-AC-ACTS-29, 98, 101); unit Combined dan standalone dengan TAG Code berselang-seling (TC-AC-ACTS-901); TC-AC-ACTS-804 memakai minimal 3 unit Available tanpa guard Delete (U1 sampai U3 dari Data Dinamis #5).
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata untuk respons `5xx` pada request Delete (TC-AC-ACTS-804), dilepas segera setelah blok TC itu. Jeda nyata pendek yang disebut eksplisit (TC-AC-ACTS-804): 10 detik untuk memastikan toast Error persisten dan 5 detik untuk mengamati toast sukses hilang setelah 4 detik.

## Test Steps

### TC-AC-ACTS-29: Aksesibilitas tabel Detail SKU > Tab Available memiliki aria-label

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Periksa atribut aria-label tabel unit
3. Verifikasi tabel memiliki aria-label `TAG Stock for RFID-ASSET-CORE-R5 (RFID)`

### TC-AC-ACTS-101: Sort TAG Code Tab Available, tanpa nilai kosong, urutan A-Z lalu kebalikannya

4. Klik header TAG Code Ascending
5. Verifikasi tabel memuat sedikitnya satu baris tampil
6. Verifikasi TAG Code urut A-Z (case-insensitive)
7. Verifikasi tidak ada baris dengan TAG Code `—`
8. Klik lagi header TAG Code (Descending)
9. Verifikasi urutan terbalik dari Ascending

### TC-AC-ACTS-901: Sort TAG Code Tab Available, ikon Combined tidak memengaruhi urutan

10. Klik menu sidebar TAG > Stock, lalu buka lagi Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
11. Verifikasi tabel memuat sedikitnya satu baris tampil
12. Klik header kolom `TAG Code` sekali
13. Verifikasi Ascending: urutan hanya mengikuti nilai TAG Code A-Z tanpa memperhatikan ada atau tidaknya ikon Combined
14. Klik header kolom `TAG Code` kedua kali
15. Verifikasi Descending: urutan terbalik dengan aturan yang sama

### TC-AC-ACTS-98: Mutasi saat Tab Available terfilter, unit baru yang tidak cocok tidak muncul

16. Klik menu sidebar TAG > Stock, lalu buka lagi Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
17. Terapkan Filter Status = Damaged/Missing
18. Verifikasi hasil terfilter memuat sedikitnya satu baris Damaged/Missing tampil
19. Klik `[Add Stock]`, scan satu TAG baru, klik `[Stop]`, lalu klik `[Submit]`
20. Tunggu aksi selesai
21. Kembali ke Tab Available
22. Verifikasi unit baru (Available) tidak muncul pada hasil terfilter Damaged/Missing
23. Kosongkan Filter Status

### TC-AC-ACTS-804: Siklus toast, posisi kanan bawah, Error bertahan, toast baru menggantikan, Success hilang setelah 4 detik

24. Klik menu sidebar TAG > Stock, lalu buka lagi Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
25. Intercept request Delete dengan respons `5xx`
26. Klik (⋯) pada unit pertama, klik `Delete`, lalu klik `[Delete]`
27. Verifikasi toast Error tampil di kanan bawah layar
28. Tunggu 10 detik
29. Verifikasi toast Error `Error, failed to delete unit.` masih tampil setelah 10 detik
30. Tanpa menutup toast, klik (⋯) pada unit kedua, klik `Delete`, lalu klik `[Delete]`
31. Verifikasi toast Error kedua menggantikan toast pertama (hanya satu toast aktif)
32. Lepas intercept, lalu tutup toast manual
33. Verifikasi toast Error hanya hilang lewat dismiss manual
34. Klik (⋯) pada unit ketiga, klik `Delete`, lalu klik `[Delete]`
35. Verifikasi toast sukses `Success, unit has been deleted.` tampil di kanan bawah layar
36. Tunggu 5 detik
37. Verifikasi toast sukses hilang otomatis setelah 4 detik

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu topik (Detail SKU, satu SKU dan satu dataset); tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah pembukaan Detail SKU dan pemulihan state diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), navigasi sidebar yang mereset sort dan filter, "Kosongkan Filter Status", pelepasan intercept, dan penutupan toast manual. Urutan TC: 29, 101, 901, 98, 804; aksi menghapus data (TC-AC-ACTS-804) di akhir.
- P-5 butir b: TC-AC-ACTS-804 menginjeksi dua respons 5xx pada Delete sebagai bagian dari siklus toast (objek uji ringan kelas b tanpa harness eksternal) di spec fungsional Detail SKU Tab Available; satu-satunya TC kelas b di spec ini.
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun perlu dikonfirmasi tim FE.
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - Langkah Uji TC-AC-ACTS-804 nomor 3 menyebut "tanpa menutup toast, hapus unit kedua"; Expected butir b-c (Error bertahan dan hanya hilang lewat dismiss manual) diasersi sebelum toast ditutup dan sesudah dismiss; asersi "hanya hilang lewat dismiss manual" diamati sebagai toast hilang setelah ditutup.
  - Langkah Uji TC-AC-ACTS-98 nomor 1 "Add Stock satu unit OK" tidak menyebut TAG Type dan cara scan; spec memakai Add Stock scan satu TAG baru (simulator RFID).
  - TC-AC-ACTS-101 dan 901 memakai Tab Available yang sama; kebutuhan dua nilai distinct pada TAG Code terpenuhi oleh seeding unit Available, Damaged/Missing, dan Combined (S-11).
