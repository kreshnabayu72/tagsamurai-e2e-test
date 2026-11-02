---
id: TC-FA-GRP-E2E-271-tab-assets-custom-field-filter-dropdown-multi-dropdown-date-dan-numeric-range
title: "Tab Assets Custom Field Filter: Dropdown, Multi-Dropdown (OR), Date dan DateTime Range Picker, serta Numeric/Currency/Percentage Min-Max"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1270
  - TC-FA-GRP-1271
  - TC-FA-GRP-1273
  - TC-FA-GRP-1272
coverage:
  web: automated
---

# Tab Assets Custom Field Filter: Dropdown, Multi-Dropdown (OR), Date dan DateTime Range Picker, serta Numeric/Currency/Percentage Min-Max

## Prerequisites

- Mode: FE+BE.
- Hook suite: rujuk `suite.md` (login API aktor, sesi API, fixture BE, flag Guided Tooltip `fa-settings-groups` bernilai `seen`).
- Akun aktor pertama: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit, untuk TC-1272): allValueAccess (Pre-setup No 17) `allValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_ALLVALUEACCESS_PASSWORD`.
- Data Pre-setup tambahan (hanya dibaca): Value Gate Node A (Tabel Dinamis No 10, G1-G6) dan fixture tipe Custom Field (No 18); node di-seed idempotent di hook `before` dengan nama bersuffix `{runId}-271` (mekanisme seeding disediakan tim FE/BE). Langkah dan asersi memakai nama bersuffix itu.
- Nilai uji (diacu dari fixture spec): Condition Grade (Dropdown A/B/C) G1 A, G2 B, G4 C, G5 A, G6 B, G3 belum diisi; Features (Multi-Dropdown) G1 Wifi+Bluetooth, G2 Wifi, G4 NFC, G6 Bluetooth; Purchase Date G2 dan G6 01/03/2026; Inspection Time G1 01/10/2026 09:00, G2 05/10/2026 10:00, G4 10/10/2026 11:00; Usage Hours G1 100, G2 250, G4 40, G6 100; Budget (Currency) G1 5000, G2 0, G4 12000, G6 700; Utilization (Percentage) G1 80, G2 20, G4 95, G6 50. Setiap filter memakai sedikitnya dua nilai distinct (S-11).
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (kondisi awal client uji; spec tidak mengubahnya).
- Setup Column: filter tidak memerlukan kolom dicentang; tidak ada preferensi kolom yang disimpan spec.
- State global: tidak ada yang diubah.

## Test Steps

### TC-1270: Filter Custom Field Dropdown (Condition Grade): multi-select searchable, satu opsi dan dua opsi (OR)
1. Buka Detail Value Gate Node A (Tab Assets)
2. Klik icon Filter; buka dropdown field Condition Grade
3. Verifikasi field berlabel `Condition Grade`, dropdown multi-select searchable
4. Verifikasi opsi A, B, C
5. Pilih A, klik [Apply]
6. Verifikasi G1 dan G5 tampil
7. Klik [Clear Field]; pilih A dan C, klik [Apply]
8. Verifikasi G1, G5, dan G4 tampil (OR di dalam field)
9. Verifikasi baris belum diisi (G3) tidak tampil
### TC-1271: Filter Custom Field Multi-Dropdown (Features): cocok bila salah satu nilai terpilih ada (OR)
10. Klik [Clear Field]; buka dropdown field Features
11. Verifikasi opsi Wifi, Bluetooth, NFC
12. Pilih Wifi, klik [Apply]
13. Verifikasi G1 dan G2 tampil
14. Klik [Clear Field]; pilih NFC dan Bluetooth, klik [Apply]
15. Verifikasi G1, G4, G6 tampil (OR)
### TC-1273: Filter Custom Field Numeric, Currency, dan Percentage: range Min-Max
16. Klik [Clear Field]; pada field Usage Hours isi Min 90, Max 300, klik [Apply]
17. Verifikasi G1, G2, G6 tampil (100, 250, 100)
18. Verifikasi G4 (40) dan baris belum diisi tidak tampil
19. Klik [Clear Field]; pada field Budget (Currency) isi Min 1000, klik [Apply]
20. Verifikasi G1 (5000) dan G4 (12000) tampil
21. Klik [Clear Field]; pada field Utilization (Percentage) isi Min 60, klik [Apply]
22. Verifikasi G1 (80) dan G4 (95) tampil
23. Klik [Clear Field]
### TC-1272: Filter Custom Field Date (Purchase Date) dan DateTime (Inspection Time): date range picker
24. Ganti akun: Logout, login sebagai allValueAccess (`allValueAccess_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_GRP_ALLVALUEACCESS_PASSWORD`), buka Fixed Asset > Settings > Groups
25. Buka Detail Value Gate Node A (Tab Assets)
26. Klik icon Filter; pada field Purchase Date pilih rentang 01/03/2026-31/03/2026, klik [Apply]
27. Verifikasi G2 dan G6 tampil (01/03/2026)
28. Klik [Clear Field]; pada field Inspection Time pilih rentang 01/10/2026-07/10/2026, klik [Apply]
29. Verifikasi G1 dan G2 tampil
30. Verifikasi G4 (10/10/2026) dan baris belum diisi tidak tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: TC-1270, TC-1271, TC-1273, lalu TC-1272 terakhir supaya hanya ada satu Ganti akun (TC-1272 memakai aktor allValueAccess; tiga TC lain Total Control).
- Langkah penghubung (S-03): [Clear Field] di awal tiap TC mengosongkan filter TC sebelumnya (S-09); [Clear Field] terakhir pada TC-1273 menutup state filter sebelum Ganti akun; satu langkah Ganti akun sebelum TC-1272.
- Temuan untuk QA:
  - TC-1273 diberi label HINT e padahal hanya ambang nilai Min-Max, bukan volume data; spec tetap satu kelas fungsional.
  - TC-1270/1271/1273 menyebut tipe Dropdown dan Numeric untuk kolom yang pada Setup Column default tersembunyi, tetapi langkah TC tidak mencentang kolom; spec mengikuti TC (filter tidak mensyaratkan kolom tampil).
  - TC-1272 langkah 3 menyebut placeholder `Select date` pada field Purchase Date; tidak ada Expected padanan, sehingga tidak diasersi.
