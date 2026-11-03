---
id: TC-FA-FAAM-E2E-065-edit-tag-type-tanpa-aset
title: "Edit TAG Type Tanpa Aset: Kosong, Non-TAG, Mutual Exclusion, dan Penggantian Tipe"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-201
  - TC-FA-FAAM-202
  - TC-FA-FAAM-203
  - TC-FA-FAAM-204
coverage:
  web: automated
---

# Edit TAG Type Tanpa Aset: Kosong, Non-TAG, Mutual Exclusion, dan Penggantian Tipe

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #13d: Asset Name `Edit Target Item` (Code `ETI`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell` model `5420`, UoM `Unit`, Total Asset 0), dirujuk lewat fixture baru `Fixture.faAssetName.editTargetItem`; dipakai TC-201 dan 203 hanya untuk dibuka dan ditolak validasi, tidak disimpan sehingga Last Updated tidak berubah (S-06). Opsi TAG Type `RFID` tersedia (client Automation memiliki subscription Paid).
- Data Dinamis (salinan seed fixture #13d, Dinamis #23 dan #24): `Edit Target Item 202 {runId}-065` (Code `ETI202`) untuk TC-202 dan `Edit Target Item 204 {runId}-065` (Code `ETI204`) untuk TC-204. Default Addon `Audit` tersedia untuk dipilih.
- Kemampuan teknis (disediakan tim FE/BE): seed API per TC untuk salinan fixture bernama bersuffix `{runId}-065` (Code salinan mengikuti pola TC dan tetap di bawah batas 15 karakter) dan sesi API aktor; salinan dihapus lewat id hasil seed di hook `after`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-201: TAG Type dikosongkan saat Edit menampilkan error

1. Ketik Search `Edit Target Item`, tekan Enter
2. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Lepas chip TAG Type `QR`
4. Klik `[Save]`
5. Verifikasi error inline `Select at least one TAG type or Non-TAG`

### TC-FA-FAAM-203: Memilih tipe TAG dan Non-TAG tidak dapat bersamaan saat Edit

6. Pilih TAG Type `Non-TAG`
7. Pilih TAG Type `RFID`
8. Verifikasi chip `Non-TAG` hilang
9. Verifikasi chip `RFID` tampil
10. Klik `[✕]` pada modal Edit
11. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
12. Klik `[Leave]`

### TC-FA-FAAM-202: Edit TAG Type ke Non-TAG pada Asset Name tanpa aset mengosongkan Default Addon tanpa dialog

13. Ganti isi kotak search dengan `Edit Target Item 202 {runId}-065`, tekan Enter
14. Klik `⋯` baris `Edit Target Item 202 {runId}-065` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
15. Pilih Default Addon `Audit`
16. Pilih TAG Type `Non-TAG`
17. Verifikasi chip Default Addon hilang
18. Verifikasi field Default Addon Disabled
19. Klik `[Save]`
20. Verifikasi toast `Success, asset name has been updated.` tampil
21. Verifikasi tidak ada dialog dampak

### TC-FA-FAAM-204: Ubah TAG Type pada Asset Name tanpa aset langsung disimpan tanpa dialog

22. Ganti isi kotak search dengan `Edit Target Item 204 {runId}-065`, tekan Enter
23. Klik `⋯` baris `Edit Target Item 204 {runId}-065` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
24. Lepas `QR` dan pilih `RFID`
25. Klik `[Save]`
26. Verifikasi toast `Success, asset name has been updated.` tampil
27. Verifikasi kolom TAG Type baris `Edit Target Item 204 {runId}-065` menampilkan icon RFID

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1, 13, dan 22 untuk menemukan baris target (R-16); penutupan form dirty pada langkah 10 (✕, dialog Unsaved Changes, `[Leave]`, S-08).
- Urutan TC: validasi yang diblokir (TC-FA-FAAM-201, 203) lebih dulu pada satu pembukaan popup, lalu aksi sukses pada salinan (TC-FA-FAAM-202, 204) (S-10). TC-FA-FAAM-205 dan 206 (client Starter pasca-downgrade, akun berbeda) ada di spec 091.
- Pada TC-FA-FAAM-202 ketiadaan dialog dampak diasersi sesudah toast sukses yang menjadi anchor (bagian 8b butir 2).
- Keunikan nilai Code yang diketik (batas 15 karakter tidak menyisakan ruang untuk suffix `{runId}-<NNN>`): nilai Code mengikuti TC, nomor TC membuatnya berbeda antar spec, seed salinan idempotent, cleanup hanya menghapus yang dibuat spec ini, dan suite berjalan serial (S-12).
