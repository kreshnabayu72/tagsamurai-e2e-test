---
id: TC-FA-FAAM-E2E-086-edit-blok-hapus-model-dan-brand-in-use
title: "Edit: Blok Hapus Model dan Brand In-Use (Tooltip, Dialog Tunggal dan Jamak) serta Brand Bebas Dilepas"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-254
  - TC-FA-FAAM-255
  - TC-FA-FAAM-256
  - TC-FA-FAAM-257
  - TC-FA-FAAM-258
  - TC-FA-FAAM-259
coverage:
  web: automated
---

# Edit: Blok Hapus Model dan Brand In-Use (Tooltip, Dialog Tunggal dan Jamak) serta Brand Bebas Dilepas

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #10: Asset Name `Dell Latitude` (Code `DLAT`, Category `IT Equipment`, TAG Type `RFID`+`QR`, Brand `Dell` model `3310`, `5420`, `7420`, Default Addon `Audit`+`Maintenance`, Default Label `Finance`+`High Priority`, UoM `Unit`, Total Asset 42), dirujuk lewat fixture baru `Fixture.faAssetName.dellLatitude`. Fixture ini tidak dapat digandakan dan diubah spec ini. Pemulihan ke keadaan Pre-setup #10 (dengan varian #10h, #10i, dan #10k) dijamin fixture seed reset (disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar-blok. Efek yang tersisa: Last Updated dan entri audit trail bertambah. Suite berjalan serial (S-06, pengecualian 2026-10-30).
- Varian Pre-setup #10 per blok: #10h (model `3310` dipakai 1 aset Active, `5420` dipakai 15 aset Active; TC-254, 255, 258), #10i (model `7420` hanya dirujuk aset Deleted dan Disposed; TC-256), dan #10k (Brand `Lenovo` tanpa model in-use; TC-259). Pre-setup #10j `Single Model Item` (Brand `Dell` dengan tepat 1 model `5420` dipakai aset Active, Total Asset 1; TC-257) hanya dibuka dan ditolak, tidak disimpan. Brand `Lenovo` (Pre-setup #23).
- Tidak ada state global yang diubah selain data fixture yang dipulihkan seed reset.

## Test Steps

### TC-FA-FAAM-254: Hapus badge model yang dipakai 1 aset diblokir dengan tooltip tunggal

1. Ketik Search `Dell Latitude`, tekan Enter
2. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Klik `×` pada badge `3310` baris Dell
4. Verifikasi badge `3310` tidak terhapus
5. Verifikasi tooltip `This model is used by 1 asset and cannot be removed.`

### TC-FA-FAAM-255: Hapus badge model yang dipakai banyak aset diblokir dengan tooltip jamak

6. Klik `×` pada badge `5420` baris Dell
7. Verifikasi badge `5420` tidak terhapus
8. Verifikasi tooltip `This model is used by 15 assets and cannot be removed.`

### TC-FA-FAAM-258: Dialog blok hapus Brand bentuk jamak untuk lebih dari satu model in-use

9. Klik icon 🗑 pada baris Brand `Dell`
10. Verifikasi dialog `Cannot Delete Brand` dengan teks `Dell has models in use by existing assets. Remove or reassign those assets first.`
11. Klik `[OK]` pada dialog
12. Klik `[✕]` pada modal Edit (form sama dengan nilai tersimpan, tanpa dialog)

### TC-FA-FAAM-257: Deselect chip Brand yang modelnya dipakai 1 aset memunculkan dialog blok tunggal dan chip tetap

13. Ganti isi kotak search dengan `Single Model Item`, tekan Enter
14. Klik `⋯` baris `Single Model Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
15. Klik `(✕)` chip Brand `Dell`
16. Verifikasi dialog `Cannot Delete Brand` dengan teks `Dell has a model in use by existing assets. Remove or reassign those assets first.` dan tombol `[OK]`
17. Verifikasi chip `Dell` tetap terpilih
18. Klik `[OK]` pada dialog
19. Klik `[✕]` pada modal Edit (form sama dengan nilai tersimpan, tanpa dialog)

### TC-FA-FAAM-256: Model dipakai hanya oleh aset Deleted atau Disposed dapat dihapus

20. Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
21. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
22. Klik `×` pada badge `7420`
23. Verifikasi badge `7420` terhapus
24. Klik `[Save]`
25. Verifikasi toast `Success, asset name has been updated.` tampil
26. Pulihkan `Dell Latitude` ke keadaan Pre-setup #10 (varian #10k) lewat seed reset, lalu Ganti isi kotak search dengan `Dell Latitude`, tekan Enter

### TC-FA-FAAM-259: Brand tanpa model in-use dapat dilepas

27. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
28. Pilih Brand `Lenovo`
29. Klik `[Save]`
30. Tunggu aksi selesai (modal Edit tertutup)
31. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
32. Lepas chip `Lenovo`
33. Verifikasi baris `Lenovo` hilang
34. Klik `[Save]`
35. Verifikasi toast `Success, asset name has been updated.` tampil
36. Pulihkan `Dell Latitude` ke keadaan Pre-setup #10 lewat seed reset

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1, 13, 20, dan 26 untuk menemukan baris target (R-16); `[OK]` dialog pada langkah 11 dan 18; penutupan modal bersih pada langkah 12 dan 19 (tanpa dialog karena form sama dengan nilai tersimpan); tunggu aksi selesai pada langkah 30 (bagian 8b butir 8); pemulihan fixture pada langkah 26 (antar-blok, S-09) dan 36 (akhir spec).
- Urutan TC: blok yang diblokir (TC-FA-FAAM-254, 255, 258, 257) lebih dulu, lalu aksi yang menyimpan (TC-FA-FAAM-256, 259) (S-10). TC-FA-FAAM-254, 255, dan 258 diamati pada satu pembukaan form `Dell Latitude`.
- Temuan untuk QA:
  - TC-FA-FAAM-254 sampai 259 mengasumsikan varian #10h, #10i, dan #10k berlaku pada fixture yang sama; spec memulihkan fixture lewat seed reset sebelum TC yang menyimpan.
  - TC-FA-FAAM-256 dan 259 menyimpan perubahan pada fixture Pre-setup #10 langsung; fixture dipulihkan seed reset (S-06, pengecualian 2026-10-30).
  - TC-FA-FAAM-254 dan 255 tidak menyebut pemicu tooltip (hover atau klik); spec memakai klik `×` yang diikuti pengamatan tooltip (bagian 8b butir 5).
- Alasan melewati sekitar 35 langkah: enam blok satu topik (model dan Brand in-use pada Edit) pada satu fixture; blok yang diblokir berbagi satu pembukaan form dan blok yang menyimpan dipulihkan seed reset, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
