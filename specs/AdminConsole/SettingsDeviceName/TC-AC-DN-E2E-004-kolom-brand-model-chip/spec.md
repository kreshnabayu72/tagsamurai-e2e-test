---
id: TC-AC-DN-E2E-004-kolom-brand-model-chip
title: "Kolom Brand dan Model/Type: Chip, +N more, Em Dash, Tooltip Fokus Keyboard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-13
  - TC-AC-DN-14
  - TC-AC-DN-15
  - TC-AC-DN-16
  - TC-AC-DN-642
coverage:
  web: automated
---

# Kolom Brand dan Model/Type: Chip, +N more, Em Dash, Tooltip Fokus Keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Master Brand (#15) dan Device Name inti (#16) `Gate Antenna` (Brand A/Model G1 dan Brand B/Model G2), `RFID Reader` (tiga SKU), `NFC Tag` (Brand A/Model N1), `Legacy Scanner` (Brand D/Model L1), `Cable Tester` dan `Door Antenna` (tanpa SKU), `Barcode Station` (Brand `International Scanner Solutions`, Model `Industrial Barcode Station Series Alpha`); seluruhnya baca-saja. Tidak ada data Dinamis.

## Test Steps

### TC-AC-DN-13: Brand dan Model/Type dengan dua nilai tampil sebagai dua chip tanpa +N more

1. Verifikasi baris `Gate Antenna`: kolom Brand chip dark `Brand A` dan `Brand B`
2. Verifikasi baris `Gate Antenna`: kolom Brand tanpa chip `+N more`
3. Verifikasi baris `Gate Antenna`: kolom Model/Type chip dark `Model G1` dan `Model G2`
4. Verifikasi baris `Gate Antenna`: kolom Model/Type tanpa chip `+N more`

### TC-AC-DN-14: Brand dan Model/Type dengan tiga nilai tampil dua chip lalu +1 more

5. Verifikasi baris `RFID Reader`: kolom Brand chip `Brand A`, `Brand B`, lalu chip `+1 more`
6. Verifikasi baris `RFID Reader`: kolom Model/Type chip `Model R1`, `Model R2`, lalu chip `+1 more`
7. Verifikasi urutan chip dalam sel Brand dan Model/Type baris `RFID Reader` alfabetis A-Z

### TC-AC-DN-15: Brand dan Model/Type dengan satu nilai tampil satu chip

8. Verifikasi baris `NFC Tag`: kolom Brand satu chip `Brand A`
9. Verifikasi baris `NFC Tag`: kolom Model/Type satu chip `Model N1`
10. Verifikasi baris `Legacy Scanner` (satu SKU): kolom Brand satu chip `Brand D` dan kolom Model/Type satu chip `Model L1`
11. Verifikasi baris `NFC Tag` dan `Legacy Scanner` tidak menampilkan chip `+N more`

### TC-AC-DN-16: Device Name tanpa SKU menampilkan em dash pada Brand dan Model/Type

12. Verifikasi baris `Cable Tester`: sel Brand `—` dan sel Model/Type `—`
13. Verifikasi baris `Door Antenna`: sel Brand `—` dan sel Model/Type `—`
14. Verifikasi sel Brand dan Model/Type baris `Cable Tester` dan `Door Antenna` tidak kosong
15. Verifikasi sel itu tidak menampilkan hyphen `-`
16. Verifikasi sel itu tidak menampilkan `null`

### TC-AC-DN-642: Tooltip chip Brand dan Model/Type terpotong dapat diakses lewat fokus keyboard

17. Tekan Tab sampai fokus berada pada chip Brand baris `Barcode Station`
18. Verifikasi chip Brand menampilkan `Internationa..er Solutions`
19. Verifikasi tooltip `International Scanner Solutions` tampil saat fokus keyboard pada chip Brand
20. Tekan Tab sampai fokus berada pada chip Model/Type baris `Barcode Station`
21. Verifikasi chip Model/Type menampilkan `Industrial B..Series Alpha`
22. Verifikasi tooltip `Industrial Barcode Station Series Alpha` tampil saat fokus keyboard pada chip Model/Type

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Semua TC tanpa aksi tulis.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan: TC-AC-DN-642 (fokus keyboard) di akhir karena mengubah fokus; tiga TC pertama hanya mengamati sel pada halaman 1 tanpa interaksi.
- Langkah Tab (TC-AC-DN-642) dimulai dari fokus awal halaman yang dimuat hook `beforeEach` suite.
- Temuan untuk QA: tidak ada temuan sumber untuk TC dalam spec ini (precondition, Expected, dan data konsisten).
