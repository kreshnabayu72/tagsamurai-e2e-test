---
id: TC-FA-FAAM-E2E-067-edit-validasi-model-dan-kapitalisasi
title: "Edit: Validasi Nama Model (Duplikat, Batas 120, Emoji, Kapitalisasi Beda)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-215
  - TC-FA-FAAM-216
  - TC-FA-FAAM-217
  - TC-FA-FAAM-733
coverage:
  web: automated
---

# Edit: Validasi Nama Model (Duplikat, Batas 120, Emoji, Kapitalisasi Beda)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #13d: Asset Name `Edit Target Item` (Code `ETI`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell` model `5420`, UoM `Unit`, Total Asset 0), dirujuk lewat fixture baru `Fixture.faAssetName.editTargetItem`; pada spec ini hanya dibuka dan ditolak validasi atau dibatalkan, tidak disimpan sehingga Last Updated tidak berubah (S-06).
- Data Pre-setup #13j: Asset Name `Case Model Item` (Code `CSM`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell` model `X1`, UoM `Unit`, Total Asset 0), dirujuk lewat fixture baru `Fixture.faAssetName.caseModelItem`; hanya dibuka dan ditolak validasi (TC-733), tidak disimpan (S-06).
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-215: Model duplikat dalam Brand yang sama ditolak saat Edit

1. Ketik Search `Edit Target Item`, tekan Enter
2. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Ketik model `5420` pada baris Dell lalu tekan Enter
4. Verifikasi error inline `Model name already exists` pada input model

### TC-FA-FAAM-217: Emoji pada nama model diblok saat Edit

5. Kosongkan input model
6. Ketik dan paste emoji `😊` di input model
7. Verifikasi emoji tidak masuk ke input model

### TC-FA-FAAM-216: Model 121 karakter ditolak dan 120 karakter diterima saat Edit

8. Ganti isi input model dengan model 121 karakter `A`
9. Verifikasi error inline `Max. 120 characters`
10. Ganti isi input model dengan model 120 karakter `B` lalu tekan Enter
11. Verifikasi model 120 karakter menjadi badge pada baris Dell
12. Klik `[✕]` pada modal Edit
13. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
14. Klik `[Leave]`

### TC-FA-FAAM-733: Nama model dengan kapitalisasi berbeda dalam Brand yang sama ditolak saat Edit

15. Ganti isi kotak search dengan `Case Model Item`, tekan Enter
16. Klik `⋯` baris `Case Model Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
17. Ketik model `x1` pada baris Dell lalu tekan Enter
18. Verifikasi error inline `Model name already exists` pada input model baris Dell
19. Verifikasi badge `X1` tampil pada baris Dell
20. Verifikasi badge `x1` tidak dibuat
21. Kosongkan input model
22. Klik `[✕]` pada modal Edit

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1 dan 15 untuk menemukan baris target (R-16); langkah 5 dan 21 mengosongkan input model yang belum menjadi badge agar error inline tidak terbawa; penutupan form dirty pada langkah 12 (✕, dialog Unsaved Changes, `[Leave]`, S-08) dan penutupan langkah 22 tanpa dialog karena tidak ada badge baru.
- Urutan TC: validasi diblokir (TC-FA-FAAM-215, 217, 216 bagian 121 karakter) lebih dulu; bagian 120 karakter TC-FA-FAAM-216 membuat badge sehingga ditaruh terakhir pada pembukaan itu; TC-FA-FAAM-733 memakai baris lain. Seluruh blok tanpa simpan.
- Verifikasi badge `X1` tampil pada TC-FA-FAAM-733 adalah anchor untuk asersi ketiadaan badge `x1` (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAM-215, 217, dan 733 tidak menyebut apakah input model yang belum menjadi badge membuat form dianggap dirty; spec mengosongkan input lalu menutup dengan ✕ tanpa verifikasi dialog.
