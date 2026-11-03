---
id: TC-FA-FAAM-E2E-082-edit-dialog-change-tag-type-tampil-dan-tanpa-perubahan
title: "Edit Ber-Aset: Dialog Change TAG Type Konfirmasi Saja, Tanpa Input Tanggal, dan Field Lain"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-647
  - TC-FA-FAAM-648
  - TC-FA-FAAM-652
  - TC-FA-FAAM-653
coverage:
  web: automated
---

# Edit Ber-Aset: Dialog Change TAG Type Konfirmasi Saja, Tanpa Input Tanggal, dan Field Lain

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #10: Asset Name `Dell Latitude` (Code `DLAT`, Category `IT Equipment`, TAG Type `RFID`+`QR`, Brand `Dell` model `3310`, `5420`, `7420`, Default Addon `Audit`+`Maintenance`, Default Label `Finance`+`High Priority`, UoM `Unit`, Total Asset 42), dirujuk lewat fixture baru `Fixture.faAssetName.dellLatitude`. Fixture ini tidak dapat digandakan dan diubah spec ini. Pemulihan ke keadaan Pre-setup #10 dijamin fixture seed reset (disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar-blok. Efek yang tersisa: Last Updated dan entri audit trail Changelog, System Log, dan Activity Log bertambah. Suite berjalan serial (S-06, pengecualian 2026-10-30).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah Tag Non-standard pada aset Dell Latitude di `tag/` (mode baca) sebagai baseline sebelum aksi.
- Tidak ada state global yang diubah selain data fixture yang dipulihkan seed reset.

## Test Steps

### TC-FA-FAAM-647 dan TC-FA-FAAM-648: dialog Change TAG Type konfirmasi saja tanpa input tanggal

1. Ketik Search `Dell Latitude`, tekan Enter
2. Catat jumlah Tag Non-standard pada aset `Dell Latitude` sebagai baseline
3. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
4. Lepas `RFID` dan pilih `NFC` pada TAG Type
5. Klik `[Save]`
6. Verifikasi dialog `Change TAG Type` dengan teks `Changing the TAG Type selection will apply to all existing assets of this asset name. TAGs of removed types will be counted as non-standard until they are replaced. Are you sure you want to save this change?`
7. Verifikasi tombol `[Cancel]` dan `[Save]` (primary) pada dialog
8. Verifikasi tidak ada field input apa pun di dialog
9. Verifikasi dialog tidak memuat field tanggal, date picker, label `Start Date`, maupun label `Target Date`
10. Verifikasi `[Save]` pada dialog langsung dapat diklik tanpa mengisi apa pun
11. Klik `[Cancel]` pada dialog

### TC-FA-FAAM-652: Menambah tipe TAG tanpa melepas tipe lama tetap memunculkan dialog Change TAG Type

12. Pilih kembali `RFID` sehingga TAG Type menjadi `RFID`, `QR`, dan `NFC`
13. Klik `[Save]`
14. Verifikasi dialog `Change TAG Type` tampil
15. Klik `[Cancel]` pada dialog

### TC-FA-FAAM-653: Edit field lain tanpa mengubah TAG Type tidak memunculkan dialog Change TAG Type

16. Lepas `NFC` sehingga TAG Type kembali `RFID`, `QR` (sama dengan nilai tersimpan)
17. Ubah hanya Code menjadi `DLAT2`
18. Klik `[Save]`
19. Verifikasi toast `Success, asset name has been updated.` tampil
20. Verifikasi tidak ada dialog `Change TAG Type`
21. Verifikasi jumlah Tag Non-standard pada aset `Dell Latitude` sama dengan baseline
22. Pulihkan `Dell Latitude` ke keadaan Pre-setup #10 lewat seed reset

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1 untuk menemukan baris target (R-16); `[Cancel]` dialog pada langkah 11 dan 15; penyesuaian TAG Type antar-TC pada langkah 12 dan 16 pada form yang sama; pemulihan fixture pada langkah 22.
- Urutan TC: TC-FA-FAAM-647 dan 648 diamati pada satu dialog yang sama (Langkah Uji TC-FA-FAAM-648 mengulang langkah TC-FA-FAAM-647 lalu memeriksa seluruh isi dialog), kemudian TC-FA-FAAM-652 dan TC-FA-FAAM-653 pada form yang sama; TC-FA-FAAM-653 menyimpan sehingga ditaruh terakhir (S-10).
- Ketiadaan dialog pada TC-FA-FAAM-653 diasersi sesudah toast sukses yang menjadi anchor (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAM-653 Expected c (tidak ada Tag Non-standard di `tag/`) tidak punya langkah observasi di TC; spec mengamatinya lewat kemampuan membaca jumlah Tag Non-standard (disediakan tim FE/BE) dengan baseline.
  - TC-FA-FAAM-653 menyimpan Code `DLAT2` pada fixture Pre-setup #10 langsung; fixture dipulihkan seed reset (S-06, pengecualian 2026-10-30).
