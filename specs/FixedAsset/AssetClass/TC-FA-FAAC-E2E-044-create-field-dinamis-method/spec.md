---
id: TC-FA-FAAC-E2E-044-create-field-dinamis-method
title: "Create Asset Class: Field Dinamis Depreciation Menurut Method"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-121
  - TC-FA-FAAC-645
  - TC-FA-FAAC-122
  - TC-FA-FAAC-123
  - TC-FA-FAAC-124
coverage:
  web: automated
---

# Create Asset Class: Field Dinamis Depreciation Menurut Method

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup: tidak ada yang dipakai selain akun aktor. Berkas `fixtures/fixed-asset-asset-class.json` belum ada; disediakan tim FE.
- Data Dinamis: tidak ada. Spec hanya memilih Method dan mengisi field di form Create tanpa Submit sehingga tidak ada Asset Class yang dibuat dan tidak ada cleanup.
- Kemampuan teknis: tidak ada selain browser.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di `suite.md`.
- State global: tidak ada yang diubah. Form Create ditutup lewat klik breadcrumb `Asset Class` pada akhir spec.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Persiapan

1. Klik tombol `+ Asset Class` di toolbar tabel
2. Klik tab `Depreciation`

### TC-FA-FAAC-121: Pilih Method Straight Line menampilkan field yang berlaku

3. Pilih Method `Straight Line`
4. Verifikasi tampil: Useful Life, Residual Value, Depreciation Start Convention
5. Verifikasi tidak tampil: Declining Rate, Total Estimated Units, Unit Type

### TC-FA-FAAC-645: Field Useful Life setelah Method Straight Line dipilih

6. Verifikasi field Useful Life (months) tampil dengan placeholder `Enter useful life`
7. Verifikasi helper text berbunyi `1 to 600 months`

### TC-FA-FAAC-122: Pilih Method Declining Balance menampilkan Declining Rate

8. Pilih Method `Declining Balance`
9. Verifikasi tampil: Useful Life dan Declining Rate (placeholder `Enter declining rate`)
10. Verifikasi tidak tampil: Total Estimated Units dan Unit Type

### TC-FA-FAAC-123: Pilih Method Units of Production menampilkan Total Estimated Units dan Unit Type

11. Pilih Method `Units of Production`
12. Verifikasi tampil: Useful Life, Total Estimated Units (placeholder `Enter total estimated units`), Unit Type (placeholder `Select unit type`)
13. Verifikasi Declining Rate tidak tampil
14. Buka select Unit Type
15. Verifikasi opsi Unit Type: `Hour meter`, `Kilometer`, `Production unit`

### TC-FA-FAAC-124: Pilih Method Not Depreciated menyembunyikan field penyusutan

16. Pilih Method `Straight Line`, isi Useful Life `60` dan Residual Value `10`
17. Ganti Method menjadi `Not Depreciated`
18. Verifikasi Depreciation Start Convention dan blok Fiscal tetap tampil
19. Verifikasi Useful Life, Declining Rate, Total Estimated Units, Unit Type, dan Residual Value tidak tampil dan tidak wajib

### Penutup

20. Klik breadcrumb `Asset Class`
21. Verifikasi dialog `Unsaved Changes` tampil
22. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-121, 645, 122, 123, 124). Tidak ada TC hanya-BE di spec ini. TC-FA-FAAC-125 (nilai field tersembunyi tidak tersimpan, membuat Asset Class) ada di spec 047.
- Urutan TC di dalam spec: TC-121, TC-645, TC-122, TC-123, TC-124. TC-645 diletakkan sesudah TC-121 karena Expected TC-645 diamati pada state Method `Straight Line` yang sama; Method tidak perlu dipilih ulang.
- Halaman yang sama dipakai berulang (prinsip 13 bagian 3): form Create dibuka sekali pada langkah 1 dan tab Depreciation pada langkah 2.
- Urutan `Verifikasi` TC-124: langkah 18 (elemen yang tetap tampil) diletakkan sebelum langkah 19 (elemen yang tidak tampil) supaya asersi absence punya anchor positif pada surface yang sama (bagian 8b butir 2). Langkah 5, 10, 13 juga didahului `Verifikasi` elemen lain yang tampil pada surface yang sama (langkah 4, 9, 12).
- Langkah penghubung (S-03): langkah 16 mengisi Useful Life dan Residual Value sesuai langkah TC-124, dan langkah 20 sampai 22 menutup form dirty (S-08).
- Temuan untuk QA:
  - TC-124 butir a memuat klausa "tidak wajib" untuk field yang tersembunyi tanpa langkah observasi (tidak ada Submit di TC); ditulis satu `Verifikasi` bersama klausa "tidak tampil" (S-03, kesimpulan yang tidak teramati terpisah).
  - TC-123 mengharapkan placeholder Unit Type `Select unit type` dan opsi di dalam select yang sama; placeholder diasersi sebelum select dibuka (bagian 8b butir 5).
