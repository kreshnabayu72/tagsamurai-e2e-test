---
id: TC-AC-DN-E2E-005-chip-panjang-dan-popup-more-bagian-1
title: "Chip Panjang, Brand/Model Turunan SKU, dan Popup +N more (Brand, Model/Type)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-17
  - TC-AC-DN-23
  - TC-AC-DN-267
  - TC-AC-DN-268
coverage:
  web: automated
---

# Chip Panjang, Brand/Model Turunan SKU, dan Popup +N more (Brand, Model/Type)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Master Brand (#15) dan Device Name inti (#16) `Barcode Station` (Brand `International Scanner Solutions`, Model `Industrial Barcode Station Series Alpha`) dan `RFID Reader` (Brand A/B/C dan Model R1/R2/R3); daftar default tanpa Search, Filter, atau Sidebar. Seluruhnya baca-saja; tidak ada data Dinamis. Form Edit dibuka tanpa mengubah nilai dan ditutup tanpa disimpan.
- Kemampuan teknis: membuka popup chip lewat klik dan Esc, serta mengklik area di luar popup.

## Test Steps

### TC-AC-DN-17: Chip Brand dan Model/Type panjang dipotong dan hover menampilkan nama penuh

1. Verifikasi chip Brand baris `Barcode Station` menampilkan `Internationa..er Solutions`
2. Hover chip Brand pada baris `Barcode Station`
3. Verifikasi tooltip chip Brand `International Scanner Solutions`
4. Verifikasi chip Model/Type baris `Barcode Station` menampilkan `Industrial B..Series Alpha`
5. Hover chip Model/Type pada baris `Barcode Station`
6. Verifikasi tooltip chip Model/Type `Industrial Barcode Station Series Alpha`

### TC-AC-DN-23: Brand dan Model/Type hanya turunan SKU dan tidak ada di form Edit

7. Klik ikon `⋯` pada baris `RFID Reader`
8. Klik `Edit` pada Overlay Row Action
9. Verifikasi popup form Edit hanya memuat field `Device Name`, `Measurement`, dan `Category`
10. Verifikasi tidak ada field untuk mengisi atau mengubah Brand maupun Model/Type pada popup form Edit
11. Klik ikon silang `[✕]` pada header popup
12. Verifikasi List Device Name tampil
13. Verifikasi penutupan lewat `[✕]` pada form tanpa perubahan nilai tidak memunculkan dialog Unsaved Changes

### TC-AC-DN-267: Klik chip +N more pada kolom Brand membuka popup daftar Brand

14. Verifikasi sel Brand baris `RFID Reader` menampilkan `Brand A`, `Brand B`, lalu chip `+1 more`
15. Klik chip `+1 more` pada sel Brand baris `RFID Reader`
16. Verifikasi popup berjudul `Brand` dan berbentuk plain list
17. Verifikasi popup memuat seluruh nilai `Brand A`, `Brand B`, dan `Brand C` terurut alfabetis A-Z
18. Verifikasi popup tidak menampilkan tooltip
19. Klik ikon `[X]` pada popup
20. Verifikasi popup tertutup
21. Verifikasi List tampil tanpa perubahan

### TC-AC-DN-268: Klik chip +N more pada kolom Model/Type membuka popup daftar Model/Type

22. Verifikasi sel Model/Type baris `RFID Reader` menampilkan `Model R1`, `Model R2`, lalu chip `+1 more`
23. Klik chip `+1 more` pada sel Model/Type baris `RFID Reader`
24. Verifikasi popup berjudul `Model/Type` dan berbentuk plain list
25. Verifikasi popup memuat seluruh nilai `Model R1`, `Model R2`, dan `Model R3` terurut alfabetis A-Z
26. Verifikasi popup tidak menampilkan tooltip
27. Tekan tombol Esc
28. Verifikasi popup tertutup
29. Verifikasi List tampil tanpa perubahan

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Semua TC tanpa aksi tulis.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan: chip panjang (TC-AC-DN-17), form Edit tanpa perubahan (TC-AC-DN-23), lalu dua popup `+N more` (TC-AC-DN-267 dan TC-AC-DN-268); popup ditutup tiap TC sehingga tiap TC mulai dari List bersih.
- Langkah 12 (List tampil) menjadi anchor positif untuk asersi absence dialog `Unsaved Changes` (bagian 8b butir 2, S-03); anchor ini tidak ada di Expected TC-AC-DN-23.
- TC-AC-DN-23: form Edit dibuka dari Pre-setup `RFID Reader` hanya untuk dibaca dan ditutup tanpa perubahan; tidak ada data yang diubah (S-06).
- Temuan untuk QA: tidak ada temuan sumber untuk TC dalam spec ini (precondition, Expected, dan data konsisten).
