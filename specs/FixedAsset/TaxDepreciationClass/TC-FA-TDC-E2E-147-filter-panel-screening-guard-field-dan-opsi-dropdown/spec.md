---
id: TC-FA-TDC-E2E-147-filter-panel-screening-guard-field-dan-opsi-dropdown
title: "Filter Panel: Screening, Guard Field, dan Opsi Dropdown"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-507
  - TC-FA-TDC-508
  - TC-FA-TDC-509
  - TC-FA-TDC-510
coverage:
  web: automated
---

# Filter Panel: Screening, Guard Field, dan Opsi Dropdown

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (`Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE), dua isi tabel berurutan:
  - Isi tabel A (TC-FA-TDC-507, 508, 509; dibaca, tidak diubah): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. NB-SL terakhir diubah oleh `Rina P`, class lain `System`; user `Budi Santoso` ada tetapi belum pernah memodifikasi class (user penyunting disediakan tim FE). Asset Type yang ada: `Building`, `Land`, `Non-building`; Allowed Methods hanya `Straight Line` dan `Declining Balance` (LAND bernilai `—`).
  - Isi tabel B (TC-FA-TDC-510, kunci `nonBuildingActiveOnly`): hanya class Non-building berstatus Active, yaitu NB-1, NB-2, NB-3, dan NB-4. Isi tabel diganti lewat seeding API sebagai langkah penghubung (langkah 31) dan dikembalikan ke isi tabel A pada langkah 38; efek pada Last Updated class Pre-setup dicatat di Notes. Pemulihan dijamin fixture BE yang disediakan tim FE/BE dan dijalankan juga di hook `after`.
- Data Dinamis: tidak ada.
- Kemampuan teknis: seeding dan penggantian isi tabel lewat API (`suite.md`); membuka dropdown multi-select dan membaca daftar opsinya.
- State global yang diubah: isi tabel (isi tabel B), dipulihkan pada langkah 38 dan di hook `after`; suite berjalan serial (`parallel: false`).

## Test Steps

### Screening Filter Panel (TC-FA-TDC-507)

1. Klik icon Filter
2. Verifikasi Filter Panel tampil di bawah toolbar
3. Verifikasi icon Filter berubah gelap
4. Verifikasi field berurutan (maks 4 per baris): `Active`, `Asset Type`, `Useful Life (years)`, `Straight Line Rate`, `Declining Balance Rate`, `Allowed Methods`, `Used By`, `Effective From`, `Modified By`, `Last Updated`
5. Verifikasi field `Active` bertipe multi-select searchable dengan placeholder `All statuses`
6. Verifikasi field `Asset Type` bertipe multi-select searchable dengan placeholder `All asset types`
7. Verifikasi field `Useful Life (years)` bertipe range dengan placeholder `Min` dan `Max`
8. Verifikasi field `Straight Line Rate` bertipe range dengan placeholder `Min` dan `Max`
9. Verifikasi field `Declining Balance Rate` bertipe range dengan placeholder `Min` dan `Max`
10. Verifikasi field `Allowed Methods` bertipe multi-select searchable dengan placeholder `All methods`
11. Verifikasi field `Used By` bertipe range dengan placeholder `Min` dan `Max`
12. Verifikasi field `Effective From` bertipe date range dengan placeholder `Select date`
13. Verifikasi field `Modified By` bertipe multi-select searchable dengan placeholder `All users`
14. Verifikasi field `Last Updated` bertipe date range dengan placeholder `Select date`
15. Verifikasi tombol `[Clear Field]` di kiri dan `[Apply]` di kanan

### Guard: Class Code, Class Name, dan Regulation Reference tanpa field filter (TC-FA-TDC-508)

16. Verifikasi tidak ada field untuk Class Code, Class Name, dan Regulation Reference pada Filter Panel

### Opsi dropdown filter di-populate dari data tabel tanpa opsi kosong (TC-FA-TDC-509)

17. Buka dropdown Active
18. Verifikasi opsi dropdown Active: `Active` dan `Inactive`
19. Verifikasi tidak ada opsi `None` pada dropdown Active
20. Buka dropdown Asset Type
21. Verifikasi opsi dropdown Asset Type: `Building`, `Land`, `Non-building`
22. Verifikasi tidak ada opsi `None` pada dropdown Asset Type
23. Buka dropdown Modified By
24. Verifikasi opsi dropdown Modified By: `Rina P` dan `System`
25. Verifikasi opsi `Budi S` tidak ada pada dropdown Modified By
26. Verifikasi tidak ada opsi `None` pada dropdown Modified By
27. Buka dropdown Allowed Methods
28. Verifikasi dropdown Allowed Methods memuat tepat dua opsi metode tunggal `Straight Line` dan `Declining Balance` (bukan kombinasi teks sel seperti `Straight Line · Declining Balance`)
29. Verifikasi class Land bernilai `—` tidak menghasilkan opsi `None` pada dropdown Allowed Methods
30. Tutup Filter Panel

### Opsi dropdown filter hanya memuat nilai yang ada di tabel (TC-FA-TDC-510)

31. Ganti isi tabel menjadi isi tabel B (hanya NB-1, NB-2, NB-3, dan NB-4 berstatus Active) lewat seeding API, lalu muat ulang halaman
32. Klik icon Filter
33. Buka dropdown Asset Type
34. Verifikasi dropdown Asset Type hanya memuat `Non-building`; `Building` dan `Land` tidak ada
35. Buka dropdown Active
36. Verifikasi dropdown Active hanya memuat `Active`; `Inactive` tidak ada
37. Tutup Filter Panel
38. Kembalikan isi tabel menjadi isi tabel A (sembilan class Example Data) lewat seeding API

## Notes

- Urutan TC dalam spec: TC-FA-TDC-507, 508, 509, 510. Filter Panel dibiarkan terbuka dari langkah 1 sampai 29 karena TC-FA-TDC-508 dan 509 memulai dengan membuka Filter Panel yang sudah terbuka pada TC-FA-TDC-507 (langkah "Klik icon Filter" TC-508 dan TC-509 tidak diulang agar panel tidak tertutup).
- Langkah penghubung (S-03): langkah 30 dan 37 (menutup Filter Panel), langkah 31 dan 38 (mengganti dan mengembalikan isi tabel lewat seeding API untuk TC-FA-TDC-510 yang mensyaratkan hanya class Non-building Active). Efek: Last Updated class Example Data dapat berubah karena penggantian isi tabel dan pemulihan (S-06); spec ini tidak mengasersi kolom Last Updated.
- Asersi absence langkah 16, 19, 22, 25, 26, 29, 34, dan 36 punya anchor positif pada `Verifikasi` elemen lain pada surface yang sama (field lain pada langkah 5 sampai 14; opsi lain pada dropdown yang sama pada langkah 18, 21, 24, 28, 34, dan 36; 8b.2).
- Spec ini 38 langkah, di atas ~35 langkah. Alasan: satu topik (Filter Panel tabel utama) pada dataset Example Data yang sama untuk tiga TC pertama, dan S-01 mengharuskan satu `Verifikasi` per field pada TC-FA-TDC-507 (10 field berbeda tipe dan placeholder).
- Temuan untuk QA:
  - TC-FA-TDC-510 mensyaratkan tabel hanya berisi NB-1 sampai NB-4 Active (NB-3 bukan class Example Data); spec mengganti isi tabel lewat seeding API dan memulihkannya. Mekanisme penggantian isi tabel disediakan tim FE/BE.
  - TC-FA-TDC-509 Expected d memuat dua klausa (tepat dua opsi metode tunggal; class Land tidak menghasilkan opsi `None`); keduanya diasersi terpisah.
  - TC-FA-TDC-507 Expected b tidak menyebut urutan placeholder `Min`/`Max` sebagai dua input terpisah; spec mengasersi keduanya pada satu `Verifikasi` per field.
  - Email akun Total Control dan nama user penyunting selain `Rina P` tidak tertulis di TC.
