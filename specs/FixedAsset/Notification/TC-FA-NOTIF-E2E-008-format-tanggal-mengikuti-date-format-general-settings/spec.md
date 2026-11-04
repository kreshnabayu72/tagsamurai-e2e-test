---
id: TC-FA-NOTIF-E2E-008-format-tanggal-mengikuti-date-format-general-settings
title: "Format Tanggal Mengikuti Date Format General Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-41
  - TC-FA-NOTIF-42
  - TC-FA-NOTIF-43
  - TC-FA-NOTIF-44
coverage:
  web: automated
---

# Format Tanggal Mengikuti Date Format General Settings

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard, Dropdown Panel, dan Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- State General Settings: Date Format `dd/MM/yy`, `HH:mm`, zona `Asia/Jakarta` (nilai Pre-setup #1). Spec tidak mengubah General Settings; fixture BE memastikan nilai itu di hook `before`.
- Jam: tanggal acuan hari ini 18/06/26 (zona Asia/Jakarta) dari jam fixture. Tahun berjalan mengikuti jam fixture, bukan tahun nyata. Jam server dan jam browser dibekukan pada jam fixture selama spec; kemampuan jam disediakan tim FE/BE (dinyatakan di `suite.md`) dan dipulihkan di hook `after`. Suite berjalan serial (`parallel: false`).
- Data (seed notifikasi akun aktor; ditukar fixture BE penukar varian seed lewat langkah penghubung):
  - TC-41: satu notifikasi uji berumur tepat 7 hari pada tahun berjalan, dibuat 11/06/26 (Pre-setup #18, seed waktu);
  - TC-42: satu notifikasi uji berumur lebih dari 7 hari pada tahun sebelumnya, dibuat 03/08/25 (Pre-setup #18, seed waktu);
  - TC-43 dan TC-44: N-01 sampai N-07 (Pre-setup #17); N-05 `Your Total Control access was removed` dibuat 18/06/26 dengan Body `Admin A removed your Total Control access on 18/06/26.`.
- Fixture BE pemulih seed dijalankan di hook `before` dan `after`. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true), fixture BE pemulih dan penukar seed notifikasi, serta kemampuan jam server dan jam fixture.

## Test Steps

### TC-FA-NOTIF-41: Timestamp absolut item berumur tepat 7 hari pada tahun yang sama

1. Seed notifikasi uji berumur tepat 7 hari (dibuat 11/06/26) lewat fixture BE penukar, bekukan jam, lalu muat ulang halaman
2. Klik Bell icon
3. Verifikasi timestamp item uji pada Dropdown Panel menampilkan tanggal `11/06/26` mengikuti Date Format General Settings, bukan `Jun 11`
4. Klik `[Show All]` untuk membuka Notification Center
5. Verifikasi timestamp item yang sama pada Notification Center menampilkan tanggal `11/06/26`, bukan `Jun 11`

### TC-FA-NOTIF-42: Timestamp absolut item berumur lebih dari 7 hari pada tahun berbeda

6. Seed notifikasi uji berumur lebih dari 7 hari pada tahun sebelumnya (dibuat 03/08/25) lewat fixture BE penukar, bekukan jam, lalu muat ulang halaman
7. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
8. Scroll sampai item uji
9. Verifikasi timestamp item uji menampilkan `03/08/25` mengikuti Date Format General Settings, bukan `Aug 3, 2025`

### TC-FA-NOTIF-43: Format tanggal Filter Date pada input tanggal

10. Pulihkan seed N-01 sampai N-07 lewat fixture BE pemulih, muat ulang halaman, lalu klik Bell icon dan `[Show All]` untuk membuka Notification Center
11. Klik icon Filter
12. Pilih tanggal 18 Juni 2026 pada field Date
13. Verifikasi teks nilai pada input Date tampil `18/06/26` sesuai Date Format General Settings
14. Klik `[Clear Field]` pada Filter Panel, lalu klik icon Filter untuk menutup panel

### TC-FA-NOTIF-44: Format tanggal Body access change

15. Klik Bell icon
16. Verifikasi Body item N-05 (`Your Total Control access was removed`) `Admin A removed your Total Control access on 18/06/26.` dengan [Date] mengikuti Date Format General Settings
17. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 6, 10 (seed, jam, muat ulang halaman), langkah 7 dan 10 (buka Notification Center), langkah 14 (pulihkan Filter Panel: nilai Date yang dipilih pada langkah 12 dikosongkan dan panel ditutup tanpa `[Apply]`), langkah 17 (pulihkan jam server dan jam browser ke waktu nyata setelah blok terakhir; jam yang dibekukan pada langkah 1 dan 6 tidak terbawa ke spec berikutnya, S-03 dan R-08).
- Panel Dropdown yang terbuka pada langkah 2 tidak ditutup eksplisit karena langkah 4 membuka Notification Center lewat `[Show All]`.
- Dua negasi pada langkah 3, 5, dan 9 ("bukan `Jun 11`", "bukan `Aug 3, 2025`") adalah kontras format pada nilai timestamp yang sama; format yang diharapkan tampil pada `Verifikasi` yang sama sehingga tidak ada absence tanpa anchor.
- Temuan untuk QA:
  - TC-41 sampai TC-44 menyebut "Pre-setup #1" untuk Date Format tetapi tidak menyebut cara memastikannya; spec memastikan nilai itu lewat fixture BE di hook `before` tanpa mengubahnya.
  - TC-43 tidak menyebut tindak lanjut sesudah memilih tanggal (tanpa `[Apply]`); spec mengosongkan Date lewat `[Clear Field]` sebagai langkah penghubung.
