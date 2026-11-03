---
id: TC-FA-FAAM-E2E-004-sel-multi-nilai-badge-strip-dan-lima-icon-tag-type
title: "Sel Multi-Nilai: Strip, Satu Badge, Dua Badge, +N more, dan Lima Icon TAG Type"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-18
  - TC-FA-FAAM-19
  - TC-FA-FAAM-20
  - TC-FA-FAAM-21
  - TC-FA-FAAM-22
coverage:
  web: automated
---

# Sel Multi-Nilai: Strip, Satu Badge, Dua Badge, +N more, dan Lima Icon TAG Type

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; spec ini tidak memakai seed API per TC dan tidak memakai sesi API aktor.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.catalog`):
  - `Warehouse Pallet` (#13): Default Addon kosong, Brand `Krisbow` model `Standard Heavy`.
  - `Plain Unit` (#14b): tanpa Default Addon dan Default Label.
  - `Ergonomic Chair` (#11): Default Addon `Tracking`, Default Label `Interior`.
  - `Service Vehicle` (#14): Brand `Isuzu` model `D-Max`, `Toyota` model `Hilux`; Default Addon `Maintenance`+`Tracking`+`Maps`.
  - `Dell Latitude` (#10): model `3310`, `5420`, `7420`; Default Addon `Audit`+`Maintenance`; Default Label `Finance`+`High Priority`.
  - Asset Name dengan kelima tipe TAG (#14c): namanya tidak tertulis di TC; dirujuk lewat fixture baru `Fixture.faAssetName.fiveTagTypes`.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### Baris `Warehouse Pallet`

1. Ketik Search `Warehouse Pallet`, tekan Enter
2. Verifikasi sel Default Addon baris `Warehouse Pallet` menampilkan `—` (TC-FA-FAAM-18)
3. Verifikasi sel Brand baris `Warehouse Pallet` menampilkan `Krisbow` sebagai 1 badge Dark (TC-FA-FAAM-19)
4. Verifikasi sel Model/Type baris `Warehouse Pallet` menampilkan `Standard Heavy` sebagai 1 badge Dark (TC-FA-FAAM-19)

### Baris `Plain Unit`

5. Ganti isi kotak search dengan `Plain Unit`, tekan Enter
6. Verifikasi sel Default Label baris `Plain Unit` menampilkan `—` (TC-FA-FAAM-18)
7. Verifikasi kolom Brand baris `Plain Unit` tidak kosong (minimal 1 Brand) (TC-FA-FAAM-18)
8. Verifikasi kolom Model/Type baris `Plain Unit` tidak kosong (minimal badge `No Model`) (TC-FA-FAAM-18)

### Baris `Ergonomic Chair`

9. Ganti isi kotak search dengan `Ergonomic Chair`, tekan Enter
10. Verifikasi sel Default Addon baris `Ergonomic Chair` menampilkan `Tracking` sebagai 1 badge (TC-FA-FAAM-19)
11. Verifikasi sel Default Label baris `Ergonomic Chair` menampilkan `Interior` sebagai 1 badge berwarna hex label (TC-FA-FAAM-19)

### Baris `Service Vehicle`

12. Ganti isi kotak search dengan `Service Vehicle`, tekan Enter
13. Verifikasi sel Brand baris `Service Vehicle` menampilkan `Isuzu`, `Toyota` (2 badge) (TC-FA-FAAM-20)
14. Verifikasi sel Model/Type baris `Service Vehicle` menampilkan `D-Max`, `Hilux` (2 badge) (TC-FA-FAAM-20)
15. Verifikasi sel Default Addon baris `Service Vehicle` menampilkan `Maintenance`, `Tracking` dan chip `+1 more` (TC-FA-FAAM-21)
16. Verifikasi badge Default Addon pada sel tersebut urut enum tetap (TC-FA-FAAM-21)

### Baris `Dell Latitude`

17. Ganti isi kotak search dengan `Dell Latitude`, tekan Enter
18. Verifikasi sel Default Addon baris `Dell Latitude` menampilkan `Audit`, `Maintenance` (2 badge, urutan enum) (TC-FA-FAAM-20)
19. Verifikasi sel Default Label baris `Dell Latitude` menampilkan `Finance`, `High Priority` (2 badge) (TC-FA-FAAM-20)
20. Verifikasi sel Model/Type baris `Dell Latitude` menampilkan `3310`, `5420` dan chip `+1 more` (TC-FA-FAAM-21)
21. Verifikasi badge Model/Type pada sel tersebut urut A→Z (TC-FA-FAAM-21)

### Baris dengan lima tipe TAG

22. Ganti isi kotak search dengan nama Asset Name lima tipe TAG (`Fixture.faAssetName.fiveTagTypes`), tekan Enter
23. Verifikasi sel TAG Type baris tersebut menampilkan icon RFID, NFC, QR, BLE, GPS berurutan (TC-FA-FAAM-22)
24. Verifikasi sel TAG Type baris tersebut tidak memuat chip `+N more` (TC-FA-FAAM-22)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke baris target; id TC ditulis di akhir tiap langkah `Verifikasi`.
- Urutan TC di spec: dikelompokkan per baris target agar tiap baris dicari satu kali; urutan Expected per TC (18, 19, 20, 21, 22) tidak dipertahankan (8b butir 5: urutan langkah mengikuti state).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 5, 9, 12, 17, 22 (Search untuk menemukan baris target, R-16). Langkah "Perhatikan sel ..." Langkah uji TC-18 sampai TC-22 dilebur ke langkah `Verifikasi` karena tidak mengubah state.
- Langkah 7 dan 8 membaca Expected TC-18 c pada baris `Plain Unit` (baris yang disebut TC-18 untuk sel kosong).
- Temuan untuk QA:
  - TC-22 mengacu ke "Asset Name dengan kelima tipe TAG (Pre-setup #14c)" tanpa nama; spec memakai kunci fixture `Fixture.faAssetName.fiveTagTypes` yang disediakan tim FE/BE.
  - TC-18 c ("Kolom Brand dan Model/Type tidak pernah kosong") tidak menyebut baris yang diamati; spec mengasersinya pada `Plain Unit` yang disebut pada Langkah uji TC-18.
  - TC-19 a dan b menyebut badge "Dark" untuk Brand dan Model/Type tanpa definisi varian "Dark" di Data Uji atau Legend; spec mengasersinya sesuai kata Expected.
