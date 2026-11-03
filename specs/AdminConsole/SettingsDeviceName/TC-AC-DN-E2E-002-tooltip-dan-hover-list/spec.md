---
id: TC-AC-DN-E2E-002-tooltip-dan-hover-list
title: "Tooltip Toolbar, Header Actions, Hover Device Name, dan Klik Area Baris pada List"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-5
  - TC-AC-DN-6
  - TC-AC-DN-7
coverage:
  web: automated
---

# Tooltip Toolbar, Header Actions, Hover Device Name, dan Klik Area Baris pada List

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Device Name inti (#16) baris `Barcode Station`; hanya dibaca. Tidak ada data Dinamis.

## Test Steps

### TC-AC-DN-5: Tooltip ikon toolbar dan header kolom Actions muncul saat hover

1. Hover ikon Search
2. Verifikasi tooltip `Search`
3. Hover ikon Filter
4. Verifikasi tooltip `Filter`
5. Hover ikon Download
6. Verifikasi tooltip `Download`
7. Hover ikon Changelog
8. Verifikasi tooltip `Changelog`
9. Hover ikon `⋯` pada header kolom Actions
10. Verifikasi tooltip `Column Visibility`

### TC-AC-DN-6: Hover pada Device Name memakai warna primary Admin Console tanpa underline

11. Verifikasi warna teks Device Name `Barcode Station` saat idle netral sama dengan teks body tabel, tanpa warna tautan standar peramban
12. Hover Device Name `Barcode Station`
13. Verifikasi saat hover warna teks berubah ke warna primary Admin Console (merah)
14. Verifikasi saat hover teks Device Name `Barcode Station` tanpa garis bawah (underline)

### TC-AC-DN-7: Klik area baris di luar Device Name, checkbox, dan row action tidak melakukan aksi

15. Verifikasi baris `Barcode Station` tampil pada List
16. Klik sel Measurement pada baris `Barcode Station`
17. Verifikasi tidak ada dialog Detail, form Edit, atau popup yang terbuka
18. Klik sel Last Modified pada baris `Barcode Station`
19. Verifikasi tidak ada dialog Detail, form Edit, atau popup yang terbuka
20. Verifikasi baris `Barcode Station` tidak berstatus tercentang
21. Verifikasi halaman tetap `Settings > Device > Device Name`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Semua TC tanpa aksi tulis.
- Subjudul `###` memetakan langkah ke id TC granular.
- TC-AC-DN-7: langkah 15 (baris `Barcode Station` tampil) menjadi anchor positif untuk asersi absence dialog dan popup (bagian 8b butir 2); tidak ada di Expected TC dan dicatat sebagai asersi tambahan (S-03). Asersi "tidak ada dialog, form Edit, atau popup" diulang sesudah tiap klik karena TC menyebut "tidak ada perubahan" pada kedua langkah klik.
- Temuan untuk QA: tidak ada temuan sumber untuk TC dalam spec ini (precondition, Expected, dan data konsisten).
