---
id: TC-FA-FAAM-E2E-084-edit-dialog-dampak-hanya-field-berubah-dan-cancel-berantai
title: "Edit Ber-Aset: Dialog Hanya Field Berubah dan Cancel Setelah Category"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-657
  - TC-FA-FAAM-658
coverage:
  web: automated
---

# Edit Ber-Aset: Dialog Hanya Field Berubah dan Cancel Setelah Category

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #10: Asset Name `Dell Latitude` (Code `DLAT`, Category `IT Equipment`, TAG Type `RFID`+`QR`, Brand `Dell` model `3310`, `5420`, `7420`, Default Addon `Audit`+`Maintenance`, Default Label `Finance`+`High Priority`, UoM `Unit`, Total Asset 42), dirujuk lewat fixture baru `Fixture.faAssetName.dellLatitude`; pada spec ini hanya dibuka dan dibatalkan, tidak disimpan sehingga Last Updated tidak berubah (S-06).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Changelog sebelum aksi sebagai baseline; asersi memakai selisih terhadap baseline (S-12).
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-657: Dialog dampak hanya untuk field yang berubah: TAG Type dan Default Label saja

1. Ketik Search `Dell Latitude`, tekan Enter
2. Catat jumlah entri Changelog sebagai baseline
3. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
4. Ubah TAG Type menjadi `NFC`+`QR` dan ganti Default Label ke `Urgent`
5. Klik `[Save]`
6. Verifikasi dialog pertama `Change TAG Type` tampil
7. Klik `[Save]` pada dialog pertama
8. Verifikasi dialog kedua `Change Default Label` tampil
9. Verifikasi dialog `Change Category` tidak muncul
10. Verifikasi dialog `Change Default Addon` tidak muncul
11. Klik `[Cancel]` pada dialog kedua
12. Klik `[✕]` pada modal Edit
13. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
14. Klik `[Leave]`

### TC-FA-FAAM-658: Cancel pada dialog Change TAG Type setelah dialog Category dikonfirmasi membatalkan seluruh penyimpanan

15. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
16. Ubah Category ke `Office Equipment` dan TAG Type menjadi `NFC`+`QR`
17. Klik `[Save]`
18. Klik `[Save]` pada dialog `Change Category`
19. Klik `[Cancel]` pada dialog `Change TAG Type`
20. Verifikasi modal Edit tetap terbuka dengan input dipertahankan
21. Klik `[✕]` pada modal Edit
22. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
23. Klik `[Leave]`
24. Verifikasi Category dan TAG Type baris `Dell Latitude` tetap `IT Equipment` serta `RFID` dan `QR` (tidak ada perubahan tersimpan)
25. Buka Changelog (icon Changelog)
26. Verifikasi jumlah entri Changelog sama dengan baseline (tidak ada log)
27. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1 untuk menemukan baris target (R-16); `[Cancel]` dialog pada langkah 11; penutupan form dirty pada langkah 12 dan 21 (✕, dialog Unsaved Changes, `[Leave]`, S-08); penutupan Modal Changelog pada langkah 27.
- Kedua blok dibatalkan sehingga fixture `Dell Latitude` tidak berubah. Ketiadaan dialog `Change Category` dan `Change Default Addon` pada TC-FA-FAAM-657 didahului `Verifikasi` dialog pertama dan kedua yang tampil sebagai anchor (bagian 8b butir 2). "Tidak ada log" pada TC-FA-FAAM-658 diasersi sebagai selisih nol terhadap baseline atas aksi yang dibatalkan, bukan asersi absence kelas g.
- TC-FA-FAAM-654 dan 656 (empat dialog berurutan dan Non-TAG ber-aset) ada di spec 090.
