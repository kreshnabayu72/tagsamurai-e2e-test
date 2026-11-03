---
id: TC-FA-CAT-E2E-073-delete-sukses-leaf-family-cascade-pakai-ulang-code
title: "Delete Sukses: Dialog D-08 Tunggal dan Jamak, Delete Leaf, Delete Family Tiga Level, dan Pakai Ulang Code"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-216
  - TC-FA-CAT-217
  - TC-FA-CAT-218
  - TC-FA-CAT-213
  - TC-FA-CAT-229
coverage:
  web: automated
---

# Delete Sukses: Dialog D-08 Tunggal dan Jamak, Delete Leaf, Delete Family Tiga Level, dan Pakai Ulang Code

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data milik spec (di-seed hook `before` lewat API, kemampuan seed disediakan tim FE/BE; dibersihkan hook `after` bila masih tersisa), semua L1 kecuali disebut lain, nama berakhiran `{runId}-073`:
  - `Accessory {runId}-073` (Code `AC73`) berisi satu anak `Cable {runId}-073`.
  - `Peripheral {runId}-073` (Code `PE73`) berisi dua anak `Keyboard {runId}-073` dan `Mouse {runId}-073`.
  - `Spare Part {runId}-073` (Code `SP73`) > `Bolt {runId}-073` > `Bolt M8 {runId}-073`.
  - `Vehicle {runId}-073` (Code `V73A`) leaf untuk Delete leaf; `Vehicle Code {runId}-073` (Code `V073`) leaf untuk pakai ulang Code. Code literal ini dibersihkan di hook `before` bila tersisa.
  - Data Dinamis: `Vehicle New {runId}-073` (Code `V073`), dibuat spec, dibersihkan di `after`.
- Data Pre-setup #20 hanya dibaca (tidak diubah).
- Kemampuan teknis: tidak ada selain seed.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search `{runId}-073`, tekan Enter

### TC-FA-CAT-216: Dialog D-08 bentuk tunggal untuk node dengan satu subcategory

2. Klik elipsis (⋯) pada baris `Accessory {runId}-073` > `Delete`
3. Verifikasi dialog D-08 dengan title `Delete Category`, bullet `Accessory {runId}-073`, dan body `This category has 1 subcategory — deleting it will also delete its subcategory. This action cannot be undone. Are you sure you want to delete it?`
4. Verifikasi tombol `[Cancel]` dan `[Delete]` tampil
5. Klik `[Cancel]`

### TC-FA-CAT-217: Dialog D-08 bentuk jamak untuk node dengan dua subcategory

6. Klik elipsis (⋯) pada baris `Peripheral {runId}-073` > `Delete`
7. Verifikasi body dialog `This category has 2 subcategories — deleting it will also delete all its subcategories. This action cannot be undone. Are you sure you want to delete it?`
8. Klik `[Cancel]`

### TC-FA-CAT-213: Delete leaf bersih

9. Klik elipsis (⋯) pada baris `Vehicle {runId}-073` > `Delete`
10. Klik `[Delete]` pada dialog D-09
11. Verifikasi toast sukses `Success, category has been deleted.`
12. Verifikasi baris `Vehicle {runId}-073` hilang dari tabel
13. Verifikasi `Vehicle {runId}-073` hilang dari sidebar
14. Verifikasi seleksi sidebar tetap `All Categories`
15. Buka Modal Changelog
16. Verifikasi Changelog memuat satu baris Delete dengan Field `Category Name`, Old `Vehicle {runId}-073`, New `—`, dan Category Name path sebelum dihapus
17. Tutup Modal Changelog

### TC-FA-CAT-218: Delete family tiga level menghapus seluruh descendant dalam satu transaksi dengan log per node

18. Klik elipsis (⋯) pada baris `Spare Part {runId}-073` > `Delete`
19. Verifikasi dialog D-08 menyebut `2 subcategories`
20. Klik `[Delete]`
21. Verifikasi toast `Success, category has been deleted.`
22. Verifikasi `Spare Part {runId}-073` hilang dari tabel
23. Verifikasi `Spare Part {runId}-073`, `Bolt {runId}-073`, dan `Bolt M8 {runId}-073` hilang dari sidebar
24. Buka Modal Changelog
25. Verifikasi Changelog memuat tiga baris Delete dengan Category Name path `Spare Part {runId}-073`, `Spare Part {runId}-073 › Bolt {runId}-073`, dan `Spare Part {runId}-073 › Bolt {runId}-073 › Bolt M8 {runId}-073`
26. Tutup Modal Changelog

### TC-FA-CAT-229: Code kategori yang sudah dihapus dapat dipakai ulang

27. Klik elipsis (⋯) pada baris `Vehicle Code {runId}-073` > `Delete`
28. Klik `[Delete]`
29. Klik `[+] Category`, isi Category Name `Vehicle New {runId}-073` dan Code `V073`, lalu klik `[Submit]`
30. Verifikasi tidak ada error `Code already exists`
31. Verifikasi kategori `Vehicle New {runId}-073` tersimpan dengan Code `V073`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Langkah penghubung (tanpa `Verifikasi`, S-03/R-16): Search `{runId}-073` di awal untuk menemukan baris target milik spec; `[Cancel]` menutup dialog; membuka dan menutup Modal Changelog.
- Urutan dialog (TC-FA-CAT-216, TC-FA-CAT-217) mendahului aksi sukses, pakai ulang Code di akhir (S-10).
- Data milik spec (bersuffix) menggantikan `Accessory`, `Peripheral`, `Spare Part`, `Vehicle` Pre-setup #20 agar Pre-setup tidak berubah (S-06). Code `VEH` pada TC-FA-CAT-229 diganti Code milik spec `V073`.
- Temuan untuk QA:
  - TC-FA-CAT-213 Post Condition b (System Log aktor dan Activity Log mencatat baris yang sama) tidak punya langkah observasi di TC, sehingga tidak diasersi.
  - TC-FA-CAT-229 tidak menyebut field lain pada form Create; spec hanya mengisi Category Name dan Code.
