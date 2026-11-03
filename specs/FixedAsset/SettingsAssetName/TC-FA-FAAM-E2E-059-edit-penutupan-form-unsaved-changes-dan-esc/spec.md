---
id: TC-FA-FAAM-E2E-059-edit-penutupan-form-unsaved-changes-dan-esc
title: "Edit: Tutup Tanpa Perubahan, Unsaved Changes, Leave, Cancel, dan Esc pada Dialog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-174
  - TC-FA-FAAM-175
  - TC-FA-FAAM-176
  - TC-FA-FAAM-670
  - TC-FA-FAAM-671
coverage:
  web: automated
---

# Edit: Tutup Tanpa Perubahan, Unsaved Changes, Leave, Cancel, dan Esc pada Dialog

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #13d: Asset Name `Edit Target Item` (Code `ETI`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell` model `5420`, UoM `Unit`, Total Asset 0), dirujuk lewat fixture baru `Fixture.faAssetName.editTargetItem`. Pada spec ini baris itu hanya dibuka, divalidasi, dan dibatalkan atau ditolak validasi; tidak ada yang disimpan sehingga Last Updated tidak berubah (S-06, pengecualian aksi dibatalkan atau ditolak).
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-174: Menutup Popup Edit tanpa perubahan tidak memunculkan Unsaved Changes

1. Ketik Search `Edit Target Item`, tekan Enter
2. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Klik `[✕]` pada modal Edit
4. Verifikasi modal Edit tertutup
5. Verifikasi baris `Edit Target Item` tampil di tabel
6. Verifikasi tidak ada dialog Unsaved Changes

### TC-FA-FAAM-175: Menutup Popup Edit yang berubah memunculkan Unsaved Changes

7. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
8. Ubah Code menjadi `ETI9`
9. Klik `[✕]` pada modal Edit
10. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`

### TC-FA-FAAM-670: Cancel pada Unsaved Changes Edit mempertahankan form dan input

11. Klik `[Cancel]` pada dialog
12. Verifikasi dialog tertutup
13. Verifikasi modal Edit tetap terbuka
14. Verifikasi Code masih `ETI9`

### TC-FA-FAAM-176: Leave pada Unsaved Changes Edit menutup form tanpa menyimpan

15. Klik `[✕]` pada modal Edit
16. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
17. Klik `[Leave]`
18. Verifikasi modal Edit tertutup
19. Verifikasi Code baris `Edit Target Item` tetap `ETI`

### TC-FA-FAAM-671: Esc pada dialog Unsaved Changes Edit setara Cancel

20. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
21. Ubah Code menjadi `ETI9`
22. Tekan Esc
23. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil pada Esc pertama
24. Tekan Esc sekali lagi
25. Verifikasi dialog tertutup
26. Verifikasi modal Edit tetap terbuka
27. Verifikasi Code masih `ETI9`
28. Klik `[✕]` pada modal Edit
29. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
30. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search `Edit Target Item` pada langkah 1 untuk menemukan baris target (R-16) dan penutupan modal pada langkah 28 sampai 30 (✕, dialog Unsaved Changes, `[Leave]`, S-08).
- Urutan TC: TC-FA-FAAM-174 (tanpa perubahan) lebih dulu, lalu TC-FA-FAAM-175, TC-FA-FAAM-670, dan TC-FA-FAAM-176 berurutan pada satu pembukaan form dirty (dialog dari TC-FA-FAAM-175 dibatalkan oleh TC-FA-FAAM-670, lalu form ditutup dengan `[Leave]` oleh TC-FA-FAAM-176), kemudian TC-FA-FAAM-671 (Esc dua kali) pada pembukaan baru. Penggabungan pembukaan mengikuti prinsip 6 bagian 3; Langkah Uji TC-FA-FAAM-670 (✕ lalu `[Cancel]`) dan TC-FA-FAAM-176 (✕ lalu `[Leave]`) dijalankan seluruhnya.
- Temuan untuk QA:
  - TC-FA-FAAM-174 Expected tidak menyebut apa yang dibandingkan untuk "tanpa dialog"; spec mengasersi baris `Edit Target Item` tampil sebagai anchor lalu ketiadaan dialog (bagian 8b butir 2).
