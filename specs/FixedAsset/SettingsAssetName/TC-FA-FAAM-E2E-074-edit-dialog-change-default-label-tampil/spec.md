---
id: TC-FA-FAAM-E2E-074-edit-dialog-change-default-label-tampil
title: "Edit Ber-Aset: Dialog Change Default Label (Jamak, Tunggal, Klausa 0 Dihilangkan)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-242
  - TC-FA-FAAM-243
  - TC-FA-FAAM-681
  - TC-FA-FAAM-682
coverage:
  web: automated
---

# Edit Ber-Aset: Dialog Change Default Label (Jamak, Tunggal, Klausa 0 Dihilangkan)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #10: Asset Name `Dell Latitude` (Code `DLAT`, Category `IT Equipment`, TAG Type `RFID`+`QR`, Brand `Dell` model `3310`, `5420`, `7420`, Default Addon `Audit`+`Maintenance`, Default Label `Finance`+`High Priority`, UoM `Unit`, Total Asset 42), dirujuk lewat fixture baru `Fixture.faAssetName.dellLatitude`; pada spec ini hanya dibuka dan dibatalkan, tidak disimpan sehingga Last Updated tidak berubah (S-06).
- Data Pre-setup #14h: `Single Asset Item` (Total Asset 1, Default Label `Interior`), hanya dibuka dan dibatalkan. Label `Finance`, `High Priority`, dan `Urgent` (Pre-setup #25).
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-242: Ubah Default Label pada Asset Name ber-aset memunculkan dialog Change Default Label

1. Ketik Search `Dell Latitude`, tekan Enter
2. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Lepas Default Label `High Priority` dan tambahkan `Urgent`
4. Klik `[Save]`
5. Verifikasi dialog `Change Default Label` dengan teks `42 assets will be assigned new labels.`, `42 assets will be unassigned.`, dan `Are you sure you want to save this change?`
6. Verifikasi tombol `[Cancel]` dan `[Save]` pada dialog
7. Klik `[Cancel]` pada dialog

### TC-FA-FAAM-681: Dialog Change Default Label hanya penambahan menghilangkan baris unassigned bernilai 0

8. Tambahkan kembali Default Label `High Priority` sehingga label menjadi `Finance`, `High Priority`, dan `Urgent`
9. Klik `[Save]`
10. Verifikasi dialog `Change Default Label` memuat `42 assets will be assigned new labels.` lalu `Are you sure you want to save this change?`
11. Verifikasi tidak ada baris `unassigned` pada dialog
12. Klik `[Cancel]` pada dialog

### TC-FA-FAAM-682: Dialog Change Default Label hanya pelepasan menghilangkan baris assigned bernilai 0

13. Lepas Default Label `Urgent` dan `High Priority` sehingga label menjadi `Finance`
14. Klik `[Save]`
15. Verifikasi dialog `Change Default Label` memuat `42 assets will be unassigned.` lalu `Are you sure you want to save this change?`
16. Verifikasi tidak ada baris `assigned new labels` pada dialog
17. Klik `[Cancel]` pada dialog
18. Klik `[✕]` pada modal Edit
19. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
20. Klik `[Leave]`

### TC-FA-FAAM-243: Dialog Change Default Label bentuk tunggal untuk 1 aset

21. Ganti isi kotak search dengan `Single Asset Item`, tekan Enter
22. Klik `⋯` baris `Single Asset Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
23. Lepas Default Label `Interior` dan tambahkan `Urgent`
24. Klik `[Save]`
25. Verifikasi dialog memuat `1 asset will be assigned new labels.` dan `1 asset will be unassigned.`
26. Klik `[Cancel]` pada dialog
27. Klik `[✕]` pada modal Edit
28. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
29. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1 dan 21 untuk menemukan baris target (R-16); `[Cancel]` dialog pada langkah 7, 12, 17, dan 26; penyesuaian label antar-TC pada langkah 8 dan 13 pada form yang sama; penutupan form dirty pada langkah 18 dan 27 (✕, dialog Unsaved Changes, `[Leave]`, S-08).
- Urutan TC: TC-FA-FAAM-242, 681, dan 682 berurutan pada satu pembukaan form `Dell Latitude` (label diatur ulang antar-dialog), lalu TC-FA-FAAM-243 pada `Single Asset Item`. Seluruh dialog dibatalkan sehingga fixture tidak berubah.
- Verifikasi isi dialog pada TC-FA-FAAM-681 dan 682 menjadi anchor bagi asersi ketiadaan baris `unassigned` dan `assigned new labels` (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAM-242 menyebut perubahan Default Label dari `Finance`, `High Priority` menjadi `Finance`, `Urgent`; spec menjalankan TC-FA-FAAM-681 dan 682 pada form yang sama dengan menyesuaikan label antar-dialog tanpa membuka ulang form.
