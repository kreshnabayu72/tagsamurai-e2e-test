---
id: TC-FA-GRP-E2E-170-tab-users-filter-temporary-user-temporary-until-dan-custom-field-dropdown
title: "Tab Users Filter Temporary User (Yes/No), Temporary Until (Rentang), dan Custom Field Dropdown"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1013
  - TC-FA-GRP-1014
  - TC-FA-GRP-1015
coverage:
  web: automated
---

# Tab Users Filter Temporary User (Yes/No), Temporary Until (Rentang), dan Custom Field Dropdown

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role. Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Custom Field spec ini di-seed sendiri (S-11): di hook `before` lewat sesi API aktor dibuat Custom Field User aktif `Phone {runId}` (teks) dan `Lokasi Kerja {runId}` (dropdown; opsi `Fixture.groupsTabUsers.lokasi1`, `Fixture.groupsTabUsers.lokasi2`, dan satu opsi lain), lalu nilainya diisi pada user Warehouse A: sedikitnya satu user bernilai lokasi1, satu bernilai lokasi2, satu bernilai opsi lain, dan satu tanpa nilai. Hook `after` menghapus kedua Custom Field itu dan preferensi kolom.
- Warehouse A memuat Temporary User dan non-Temporary User; Temporary User dengan Temporary Until bervariasi (sedikitnya dua tanggal distinct; rentang uji `Fixture.groupsTabUsers.untilFrom` sampai `Fixture.groupsTabUsers.untilTo` mencakup sebagian saja) dan user tanpa Temporary Until. Dua opsi berbeda dari Custom Field `Lokasi Kerja {runId}`: `Fixture.groupsTabUsers.lokasi1` dan `Fixture.groupsTabUsers.lokasi2`.
- Format tanggal mengikuti Date Format General Settings (nilai default dd/MM/yy; tidak diubah oleh spec).

## Test Steps

1. Ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A
2. Klik icon Filter

### TC-1013: Filter Temporary User Yes/No

3. Tampilkan kolom Temporary User via Column Visibility
4. Klik icon Filter
5. Buka dropdown Temporary User
6. Verifikasi placeholder `All options`
7. Verifikasi opsi `Yes` dan `No`
8. Pilih `Yes`, klik [Apply]
9. Verifikasi sedikitnya satu baris tampil pada tabel
10. Verifikasi hanya Temporary User yang tampil
11. Buka Filter, ganti ke `No`, klik [Apply]
12. Verifikasi sedikitnya satu baris tampil pada tabel
13. Verifikasi hanya user non-Temporary yang tampil
14. Sembunyikan kolom Temporary User via Column Visibility
15. Buka Filter, pilih `Yes`, klik [Apply]
16. Verifikasi sedikitnya satu baris tampil pada tabel
17. Verifikasi filter bekerja walau kolom Temporary User sedang tidak tampil (Hidden)
18. Buka Filter, klik [Clear Field], klik [Apply]

### TC-1014: Filter Temporary Until rentang

19. Klik icon Filter
20. Verifikasi placeholder date range picker `Select date`
21. Buka date range picker Temporary Until, pilih tanggal awal dan akhir dari `Fixture.groupsTabUsers.untilFrom` dan `Fixture.groupsTabUsers.untilTo`
22. Klik [Apply]
23. Tampilkan kolom Temporary Until via Column Visibility
24. Verifikasi sedikitnya satu baris tampil pada tabel
25. Verifikasi hanya baris dengan Temporary Until di rentang (inklusif) tampil
26. Verifikasi tanggal pada kolom Temporary Until berformat Date Format General Settings
27. Verifikasi user tanpa Temporary Until tidak tampil
28. Klik icon Filter
29. Verifikasi tanggal pada field Temporary Until di Filter Panel berformat Date Format General Settings
30. Tutup Filter Panel
31. Buka Filter, klik [Clear Field], klik [Apply]

### TC-1015: Filter Custom Field Dropdown

32. Tampilkan kolom Custom Field `Lokasi Kerja {runId}` via Column Visibility
33. Klik icon Filter
34. Verifikasi field filter `Lokasi Kerja {runId}` tampil dengan placeholder `All [plural noun]`
35. Verifikasi `Phone {runId}` (teks) tidak punya field filter
36. Pilih dua opsi berbeda pada field `Lokasi Kerja {runId}`, klik [Apply]
37. Verifikasi sedikitnya satu baris tampil pada tabel
38. Verifikasi baris yang bernilai salah satu dari kedua opsi `Lokasi Kerja {runId}` tampil (OR di dalam field)
39. Verifikasi baris bernilai lain tidak tampil
40. Sembunyikan kolom Custom Field `Lokasi Kerja {runId}` via Column Visibility
41. Buka Filter, klik [Clear Field], pilih dua opsi berbeda pada field `Lokasi Kerja {runId}`, klik [Apply]
42. Verifikasi sedikitnya satu baris tampil pada tabel
43. Verifikasi filter bekerja walau kolom Custom Field sedang tidak tampil (Hidden)
44. Buka Filter, klik [Clear Field], klik [Apply]

## Notes

- Spec 44 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): `Buka Filter, klik [Clear Field], klik [Apply]` antar TC (S-09); menyembunyikan kolom Temporary User dan Custom Field `Lokasi Kerja {runId}` serta menampilkan kolom Temporary Until lewat Column Visibility agar Expected d (TC-1013), Expected c (TC-1015), dan Expected c (TC-1014, format tanggal kolom) dapat diamati; kolom dipulihkan lewat hook `after` (hapus preferensi kolom).
- Asersi tambahan (S-03, 8b.2): `Verifikasi sedikitnya satu baris tampil pada tabel` ditambahkan sebelum asersi hasil Search atau Filter yang bersifat universal ("hanya baris ...", "nilai lain tidak tampil") agar asersi tidak vacuous; bukan klausa Expected TC.
- Baris `Warehouse A` dicari lewat Search sebelum klik angka Total User (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan; Refresh F5 membuang Search sehingga Search diketik ulang). Langkah Search digabung ke langkah klik angka dan dihitung langkah penghubung (S-03, S-14, R-16).
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - Custom Field User beserta nilainya pada user Warehouse A tidak tertulis di Tabel Pre-setup TC (TC-1013 sampai 1015); spec men-seed sendiri di hook `before` (bersuffix `{runId}`) dan menghapusnya di hook `after` (S-11).
  - TC-1013 sampai 1015 tidak menyebut langkah menyembunyikan kolom padahal Expected memeriksa "filter bekerja saat kolom Hidden"; spec menambah langkah itu dan mengikuti Expected TC. TC-1014 Expected c (format tanggal) dibaca pada filter dan kolom Temporary Until, sehingga kolom ditampilkan lebih dulu.
