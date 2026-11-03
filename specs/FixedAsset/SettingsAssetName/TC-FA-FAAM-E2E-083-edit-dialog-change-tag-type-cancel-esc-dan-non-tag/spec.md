---
id: TC-FA-FAAM-E2E-083-edit-dialog-change-tag-type-cancel-esc-dan-non-tag
title: "Edit Ber-Aset: Cancel, Esc, dan Backdrop Dialog Change TAG Type serta Non-TAG Tanpa Addon"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-650
  - TC-FA-FAAM-651
  - TC-FA-FAAM-655
coverage:
  web: automated
---

# Edit Ber-Aset: Cancel, Esc, dan Backdrop Dialog Change TAG Type serta Non-TAG Tanpa Addon

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #10: Asset Name `Dell Latitude` (Code `DLAT`, Category `IT Equipment`, TAG Type `RFID`+`QR`, Brand `Dell` model `3310`, `5420`, `7420`, Default Addon `Audit`+`Maintenance`, Default Label `Finance`+`High Priority`, UoM `Unit`, Total Asset 42), dirujuk lewat fixture baru `Fixture.faAssetName.dellLatitude`; pada spec ini hanya dibuka dan dibatalkan, tidak disimpan sehingga Last Updated tidak berubah (S-06).
- Data Dinamis (salinan seed fixture #14h, Dinamis #96): `Single Asset Item 655 {runId}-083` (Total Asset 1, TAG Type `QR`, tanpa Default Addon, Default Label `Interior`), disimpan oleh TC-655.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah Tag Non-standard pada aset Dell Latitude di `tag/` (mode baca) sebagai baseline sebelum aksi.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Changelog sebelum aksi sebagai baseline; asersi memakai selisih terhadap baseline (S-12).
- Kemampuan teknis (disediakan tim FE/BE): seed API per TC untuk salinan fixture bernama bersuffix `{runId}-083` (Code salinan mengikuti pola TC dan tetap di bawah batas 15 karakter) dan sesi API aktor; salinan dihapus lewat id hasil seed di hook `after`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-650: Cancel pada dialog Change TAG Type membatalkan seluruh penyimpanan

1. Ketik Search `Dell Latitude`, tekan Enter
2. Catat jumlah entri Changelog dan jumlah Tag Non-standard pada aset `Dell Latitude` sebagai baseline
3. Klik `⋯` baris `Dell Latitude` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
4. Lepas `RFID` dan pilih `NFC` pada TAG Type
5. Klik `[Save]`
6. Klik `[Cancel]` pada dialog `Change TAG Type`
7. Verifikasi dialog tertutup
8. Verifikasi modal Edit tetap terbuka dengan perubahan TAG Type dipertahankan

### TC-FA-FAAM-651: Esc pada dialog Change TAG Type setara Cancel dan klik backdrop diabaikan

9. Klik `[Save]`
10. Klik area gelap di luar dialog
11. Verifikasi klik backdrop tidak menutup dialog
12. Tekan Esc
13. Verifikasi Esc menutup dialog seperti Cancel
14. Verifikasi modal Edit tetap terbuka dengan input dipertahankan
15. Klik `[✕]` pada modal Edit
16. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
17. Klik `[Leave]`
18. Verifikasi TAG Type baris `Dell Latitude` tetap `RFID` dan `QR` (tanpa mutasi)
19. Buka Changelog (icon Changelog)
20. Verifikasi jumlah entri Changelog sama dengan baseline (tanpa entri log)
21. Tutup Modal Changelog
22. Verifikasi jumlah Tag Non-standard pada aset `Dell Latitude` sama dengan baseline

### TC-FA-FAAM-655: Memilih Non-TAG saat Default Addon kosong hanya memunculkan dialog Change TAG Type

23. Ganti isi kotak search dengan `Single Asset Item 655 {runId}-083`, tekan Enter
24. Klik `⋯` baris `Single Asset Item 655 {runId}-083` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
25. Pilih TAG Type `Non-TAG`
26. Klik `[Save]`
27. Verifikasi dialog `Change TAG Type` tampil
28. Klik `[Save]` pada dialog
29. Verifikasi toast `Success, asset name has been updated.` tampil
30. Verifikasi dialog `Change Default Addon` tidak muncul

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1 dan 23 untuk menemukan baris target (R-16); penutupan form dirty pada langkah 15 (✕, dialog Unsaved Changes, `[Leave]`, S-08); penutupan Modal Changelog pada langkah 21.
- Urutan TC: TC-FA-FAAM-650 dan 651 pada satu pembukaan form `Dell Latitude` (dialog Change TAG Type dibatalkan, lalu dibuka lagi untuk Esc dan backdrop), diikuti TC-FA-FAAM-655 yang menyimpan pada salinan (S-10). Hasil "tanpa mutasi" dan "tanpa entri log" TC-FA-FAAM-650 dan 651 diamati sesudah form ditutup; aksi dibatalkan sehingga asersinya selisih nol terhadap baseline, bukan asersi absence kelas g.
- Ketiadaan dialog `Change Default Addon` pada TC-FA-FAAM-655 diasersi sesudah toast sukses yang menjadi anchor (bagian 8b butir 2).
- Keunikan nilai Code yang diketik (batas 15 karakter tidak menyisakan ruang untuk suffix `{runId}-<NNN>`): nilai Code mengikuti TC, nomor TC membuatnya berbeda antar spec, seed salinan idempotent, cleanup hanya menghapus yang dibuat spec ini, dan suite berjalan serial (S-12).
- Temuan untuk QA:
  - TC-FA-FAAM-650 Expected c ("tanpa Tag yang menjadi Non-standard di tag/") tidak punya langkah observasi di TC; spec mengamatinya lewat kemampuan membaca jumlah Tag Non-standard dengan baseline.
