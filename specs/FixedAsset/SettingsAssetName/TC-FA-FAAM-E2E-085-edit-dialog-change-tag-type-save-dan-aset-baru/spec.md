---
id: TC-FA-FAAM-E2E-085-edit-dialog-change-tag-type-save-dan-aset-baru
title: "Edit Ber-Aset: Save Change TAG Type Satu Baris Log dan Aset Baru Terdaftar Antar Dialog"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-649
  - TC-FA-FAAM-659
coverage:
  web: automated
---

# Edit Ber-Aset: Save Change TAG Type Satu Baris Log dan Aset Baru Terdaftar Antar Dialog

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #10: Asset Name `Dell Latitude` (Code `DLAT`, Category `IT Equipment`, TAG Type `RFID`+`QR`, Brand `Dell` model `3310`, `5420`, `7420`, Default Addon `Audit`+`Maintenance`, Default Label `Finance`+`High Priority`, UoM `Unit`, Total Asset 42), dirujuk lewat fixture baru `Fixture.faAssetName.dellLatitude`. Fixture ini tidak dapat digandakan dan diubah spec ini. Pemulihan ke keadaan Pre-setup #10 dijamin fixture seed reset (disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar-blok. Efek yang tersisa: Last Updated dan entri audit trail Changelog, System Log, dan Activity Log bertambah. Suite berjalan serial (S-06, pengecualian 2026-10-30).
- Tidak ada state global yang diubah selain data fixture yang dipulihkan seed reset.

## Test Steps

### TC-FA-FAAM-649: Save pada dialog Change TAG Type menyimpan perubahan dan mencatat satu baris Edit TAG Type

1. Ketik Search `Dell Latitude`, tekan Enter
2. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Lepas `RFID` dan pilih `NFC` pada TAG Type
4. Klik `[Save]`
5. Klik `[Save]` pada dialog `Change TAG Type`
6. Verifikasi toast `Success, asset name has been updated.` tampil
7. Verifikasi modal Edit tertutup
8. Buka Changelog (icon Changelog) dan ketik Search `Dell Latitude`, tekan Enter
9. Verifikasi entri teratas Changelog: Field `TAG Type`, Old `RFID, QR`, New `NFC, QR`
10. Tutup Modal Changelog
11. Klik `⋯` baris `Dell Latitude` lalu `Detail`
12. Verifikasi Popup Detail: Identitas Utama TAG Type menampilkan icon `NFC` dan `QR`
13. Tutup Popup Detail
14. Pulihkan `Dell Latitude` ke keadaan Pre-setup #10 lewat seed reset, buka kembali Fixed Asset > Settings > Asset Master > Asset Name, lalu Ketik Search `Dell Latitude`, tekan Enter

### TC-FA-FAAM-659: Aset baru terdaftar antara dialog Change TAG Type tampil dan konfirmasi: Save tetap sukses dan Total Asset memuat aset baru itu

15. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
16. Lepas `RFID` dan pilih `NFC`, klik `[Save]`
17. Daftarkan satu aset baru ke `Dell Latitude` lewat sesi API aktor hingga aset tersimpan
18. Klik `[Save]` pada dialog `Change TAG Type`
19. Verifikasi toast `Success, asset name has been updated.` tampil
20. Verifikasi modal Edit tertutup
21. Verifikasi kolom Total Asset baris `Dell Latitude` menampilkan `43` (42 aset awal ditambah aset baru yang didaftarkan sebelum Save)
22. Verifikasi kolom TAG Type baris `Dell Latitude` menampilkan icon `NFC` dan `QR`
23. Pulihkan `Dell Latitude` ke keadaan Pre-setup #10 lewat seed reset

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1 dan 14 untuk menemukan baris target (R-16); penutupan Modal Changelog pada langkah 10 dan Popup Detail pada langkah 13; pemulihan fixture pada langkah 14 (antar-blok, S-09) dan 23 (akhir spec).
- "Entri teratas" Changelog dibaca lewat Search nama fixture (urutan Date menurun, suite serial). Langkah Uji TC-FA-FAAM-659 "Di sesi lain daftarkan satu aset baru" ditulis sebagai langkah pemicu pelaku kedua lewat sesi API aktor (R-20).
- Temuan untuk QA:
  - TC-FA-FAAM-649 Post Condition (Tag `Paired` bertipe `RFID` terhitung Non-standard di `tag/`) tidak punya langkah observasi di TC; tidak diasersi (rujukan ke TC-FA-FAAM-828).
  - TC-FA-FAAM-649 dan 659 menyimpan perubahan pada fixture Pre-setup #10 langsung; fixture dipulihkan seed reset (S-06, pengecualian 2026-10-30).
