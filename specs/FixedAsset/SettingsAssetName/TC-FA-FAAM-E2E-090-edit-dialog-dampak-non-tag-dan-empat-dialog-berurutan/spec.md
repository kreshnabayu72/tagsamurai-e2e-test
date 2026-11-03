---
id: TC-FA-FAAM-E2E-090-edit-dialog-dampak-non-tag-dan-empat-dialog-berurutan
title: "Edit Ber-Aset: Non-TAG Memicu Dialog TAG Type lalu Default Addon dan Empat Dialog Berurutan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-654
  - TC-FA-FAAM-656
coverage:
  web: automated
---

# Edit Ber-Aset: Non-TAG Memicu Dialog TAG Type lalu Default Addon dan Empat Dialog Berurutan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #10: Asset Name `Dell Latitude` (Code `DLAT`, Category `IT Equipment`, TAG Type `RFID`+`QR`, Brand `Dell` model `3310`, `5420`, `7420`, Default Addon `Audit`+`Maintenance`, Default Label `Finance`+`High Priority`, UoM `Unit`, Total Asset 42), dirujuk lewat fixture baru `Fixture.faAssetName.dellLatitude`. Fixture ini tidak dapat digandakan dan diubah spec ini. Pemulihan ke keadaan Pre-setup #10 dijamin fixture seed reset (disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar-blok. Efek yang tersisa: Last Updated dan entri audit trail Changelog, System Log, dan Activity Log bertambah. Suite berjalan serial (S-06, pengecualian 2026-10-30).
- Varian Pre-setup #10r: Audit `enrolled_via_default` pada 7 aset Active tanpa transaksi aktif dan Maintenance `enrolled_via_default` pada 10 aset Active dengan 2 transaksi aktif (TC-654); varian #10d: lisensi Tracking tersedia (TC-656). Label `Urgent` (Pre-setup #25), leaf `Office Equipment` (Pre-setup #22).
- Tidak ada state global yang diubah selain data fixture yang dipulihkan seed reset.

## Test Steps

### TC-FA-FAAM-654: Memilih Non-TAG pada Asset Name ber-aset: dialog Change TAG Type lalu Change Default Addon

1. Ketik Search `Dell Latitude`, tekan Enter
2. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Pilih TAG Type `Non-TAG`
4. Verifikasi chip Default Addon `Audit` dan `Maintenance` hilang
5. Verifikasi field Default Addon Disabled
6. Klik `[Save]`
7. Verifikasi dialog pertama `Change TAG Type` tampil
8. Klik `[Save]` pada dialog pertama
9. Verifikasi dialog kedua `Change Default Addon` memuat `Removing Audit:` dengan klausa `7 assets will be unenrolled.` serta `Removing Maintenance:` dengan klausa `8 assets will be unenrolled.` dan klausa `2 assets have an active transaction — they will stay enrolled and be unenrolled once that transaction completes.`
10. Klik `[Save]` pada dialog kedua `Change Default Addon`
11. Verifikasi toast `Success, asset name has been updated.` tampil
12. Pulihkan `Dell Latitude` ke keadaan Pre-setup #10d lewat seed reset, lalu Ganti isi kotak search dengan `Dell Latitude`, tekan Enter

### TC-FA-FAAM-656: Empat dialog dampak tampil berurutan Category, TAG Type, Default Addon, Default Label

13. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
14. Ubah Category ke `Office Equipment`, TAG Type menjadi `NFC`+`QR`, tambahkan Default Addon `Tracking`, dan ganti Default Label ke `Urgent`
15. Klik `[Save]`
16. Verifikasi dialog pertama `Change Category` tampil
17. Klik `[Save]` pada dialog pertama
18. Verifikasi dialog kedua `Change TAG Type` tampil
19. Klik `[Save]` pada dialog kedua
20. Verifikasi dialog ketiga `Change Default Addon` tampil
21. Klik `[Save]` pada dialog ketiga
22. Verifikasi dialog keempat `Change Default Label` tampil
23. Klik `[Save]` pada dialog keempat
24. Verifikasi toast `Success, asset name has been updated.` tampil
25. Verifikasi keempat perubahan tersimpan: Category `Office Equipment`, TAG Type `NFC`+`QR`, Default Addon `Tracking`, dan Default Label `Urgent` pada baris `Dell Latitude`
26. Buka Changelog (icon Changelog) dan ketik Search `Dell Latitude`, tekan Enter
27. Verifikasi Changelog memuat satu baris Edit per field: `Category`, `TAG Type`, `Default Addon`, dan `Default Label`
28. Tutup Modal Changelog
29. Pulihkan `Dell Latitude` ke keadaan Pre-setup #10 lewat seed reset

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1 dan 12 untuk menemukan baris target (R-16); penutupan Modal Changelog pada langkah 28; pemulihan fixture pada langkah 12 (antar-blok, S-09) dan 29 (akhir spec).
- Spec ini memuat TC-FA-FAAM-654 dan 656 yang menyimpan pada fixture `Dell Latitude`; TC-FA-FAAM-657 dan 658 (dibatalkan) ada di spec 084.
- Temuan untuk QA:
  - TC-FA-FAAM-654 dan 656 menyimpan perubahan pada fixture Pre-setup #10 langsung; fixture tidak dapat digandakan sehingga dipulihkan seed reset (S-06, pengecualian 2026-10-30).
