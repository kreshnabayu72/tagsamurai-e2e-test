---
id: TC-FA-TDC-E2E-041-create-class-sukses-non-building-building-dan-land
title: "Create Class Sukses - Non-building, Building, dan Land"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-105
  - TC-FA-TDC-106
  - TC-FA-TDC-107
sourceRules: ["F-FATDC-01.k12", "T-01", "FI-09", "ST-02", "§4.1.1#r1", "§4.1.1#r2", "§4.1.1#r3", "§4.1.1#r4", "§4.1.1#r5", "§4.1.1#r6", "§4.1.1#r7", "§4.1.1#r8", "§4.1.1#r9", "§4.1.1#r10", "FATDC-LOGIC-03f.1", "FATDC-LOGIC-03f.2", "FATDC-LOGIC-03f.3", "FATDC-LOGIC-03c", "FATDC-LOGIC-03b"]
smoke: []
dependsOn: []
trace:
  "F-FATDC-01.k12": 9
  "T-01": [10, 23, 32]
  "FI-09": 11
  "ST-02": 12
  "§4.1.1#r1": 13
  "§4.1.1#r2": 13
  "§4.1.1#r3": 13
  "§4.1.1#r4": [13, 24, 33]
  "§4.1.1#r5": [13, 24, 33]
  "§4.1.1#r6": [13, 24, 33]
  "§4.1.1#r7": [13, 24, 33]
  "§4.1.1#r8": [13, 24, 33]
  "§4.1.1#r9": 13
  "§4.1.1#r10": 13
  "FATDC-LOGIC-03f.1": [13, 24]
  "FATDC-LOGIC-03f.2": 13
  "FATDC-LOGIC-03f.3": 24
  "FATDC-LOGIC-03c": 24
  "FATDC-LOGIC-03b": 33
coverage:
  web: automated
---

# Create Class Sukses - Non-building, Building, dan Land

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE): tujuh class seed bawaan NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND. Master Data Count Limit belum tercapai. Ukuran halaman tabel bawaan 10 baris; setelah tiga Create tabel berisi 10 baris sehingga baris target tampil tanpa Search.
- Data Dinamis (milik spec, nilai dari TC): Class Code `KHS-01`, `BGN-01`, dan `LHN-01` belum ada. Regulation Reference `UU HPP 7/2021; PMK 72/2023` (`Fixture.fixedAssetTaxDepreciationClass.regulationReference`); Class Name `Kelompok khusus uji 1`, `Bangunan uji 1`, `Tanah uji 1`. Kode class memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat (S-12); seeding idempotent (dilewati bila kode sudah ada), cleanup hanya menghapus yang dibuat spec ini, suite serial, dan kode berbeda antar spec.
- Pemulihan: hook `after` menghapus `KHS-01`, `BGN-01`, dan `LHN-01` lewat API (kemampuan disediakan tim FE/BE).

## Test Steps

### TC-FA-TDC-105: Submit Create class Non-building dengan Straight Line dan Declining Balance (Stay tidak dicentang)

1. Klik `+ Class` di toolbar
2. Isi Regulation Reference `UU HPP 7/2021; PMK 72/2023`
3. Isi Class Code `KHS-01`
4. Isi Class Name `Kelompok khusus uji 1`
5. Pilih Asset Type `Non-building`
6. Isi Useful Life `8`
7. Pilih Allowed Methods `Straight Line` dan `Declining Balance`
8. Klik `[Submit]`
9. Verifikasi Drawer menutup
10. Verifikasi muncul toast sukses: "Success, tax depreciation class has been created."
11. Verifikasi tabel dimuat ulang dan baris `KHS-01` tampil
12. Verifikasi baris `KHS-01` di-highlight sesaat
13. Verifikasi baris `KHS-01` berisi: Active = On, Class Name "Kelompok khusus uji 1", Asset Type "Non-building", Useful Life (years) "8", Straight Line Rate "12.5%", Declining Balance Rate "25%", Allowed Methods "Straight Line · Declining Balance", Used By "0", Effective From "—"

### TC-FA-TDC-106: Submit Create class Building dengan Straight Line saja

14. Tunggu toast lama hilang otomatis
15. Klik `+ Class` di toolbar
16. Isi Regulation Reference `UU HPP 7/2021; PMK 72/2023`
17. Isi Class Code `BGN-01`
18. Isi Class Name `Bangunan uji 1`
19. Pilih Asset Type `Building`
20. Isi Useful Life `20`
21. Pilih Allowed Methods `Straight Line`
22. Klik `[Submit]`
23. Verifikasi muncul toast sukses: "Success, tax depreciation class has been created."
24. Verifikasi baris `BGN-01` tampil di tabel: Asset Type "Building", Useful Life (years) "20", Straight Line Rate "5%", Declining Balance Rate "—", Allowed Methods "Straight Line"

### TC-FA-TDC-107: Submit Create class Land tanpa Useful Life dan Allowed Methods

25. Tunggu toast lama hilang otomatis
26. Klik `+ Class` di toolbar
27. Isi Regulation Reference `UU HPP 7/2021; PMK 72/2023`
28. Isi Class Code `LHN-01`
29. Isi Class Name `Tanah uji 1`
30. Pilih Asset Type `Land`
31. Klik `[Submit]`
32. Verifikasi muncul toast sukses: "Success, tax depreciation class has been created."
33. Verifikasi baris `LHN-01` tampil: Asset Type "Land", Useful Life (years) "—", Straight Line Rate "—", Declining Balance Rate "—", Allowed Methods "—"

## Notes

- Langkah penghubung (S-03): langkah 14 dan 25 (menunggu toast sukses sebelumnya hilang otomatis supaya toast berikutnya tidak lulus semu).
- Urutan Expected TC-FA-TDC-105 diasersi mengikuti urutan state (8b.5): highlight baris (langkah 12) langsung sesudah baris tampil (langkah 11) dan sebelum asersi isi baris.
- Setelah tiga Create tabel berisi tepat 10 baris (7 seed ditambah tiga class milik spec), sehingga langkah 11, 24, dan 33 tidak didahului Search (8b.13, R-23).
- Pembagian TC lintas spec: tidak ada; seluruh TC sumber ada di spec ini.
- Temuan untuk QA:
  - Post Condition TC-FA-TDC-105 a sampai e, TC-FA-TDC-106 a dan b, serta TC-FA-TDC-107 a dan b tidak punya langkah observasi di TC (status Active, Last Posted Tax Year kosong, satu versi Current, entri L-01 pada tiga surface log, opsi di Asset Class); spec tidak mengasersinya (S-01). Entri log L-01 dan opsi di Asset Class diuji di TC modul lain.
  - TC-FA-TDC-105 Expected d menulis rate dengan simbol `%` di tabel ("12.5%", "25%"); spec mengikuti TC.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
