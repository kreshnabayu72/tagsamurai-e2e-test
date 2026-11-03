---
id: TC-FA-CAT-E2E-006-node-excess-sidebar-tabel-alert-blokir-d01
title: "Node Excess: Sidebar, Tabel, Alert Consolidation, Menu, dan Blokir D-01"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-22
  - TC-FA-CAT-23
  - TC-FA-CAT-24
  - TC-FA-CAT-316
  - TC-FA-CAT-317
  - TC-FA-CAT-320
coverage:
  web: automated
---

# Node Excess: Sidebar, Tabel, Alert Consolidation, Menu, dan Blokir D-01

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) pada client CatExcess (Pre-setup #31), `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = CatExcess, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: client CatExcess (Pre-setup #31, plan Starter setelah downgrade, cap kategori 5, T-0 sudah lewat, 9 kategori): usable `Electronics` (internal, anak `Laptop` dan `Monitor`), `Office`, `Spare Parts` (internal, anak `Old Parts` Excess); Excess `Heavy Equipment`, `Vehicle`, `Furniture` (Total Asset 5, ditunjuk Asset Name `Office Chair`), `Old Parts`. Spec hanya membaca; client disediakan ulang lewat seed API.
- Flag Guided Tooltip halaman Categories: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan client Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-categories.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-22: Node Excess di sidebar redup 50% dengan tooltip Read-only

1. Verifikasi nama node Excess `Heavy Equipment`, `Vehicle`, dan `Furniture` di sidebar ditampilkan dengan opacity 50%
2. Hover node `Heavy Equipment`
3. Verifikasi tooltip node Excess `Read-only — over your plan's category limit`
4. Verifikasi node usable `Office` tampil normal (tanpa opacity 50%)
5. Hover node `Office`
6. Verifikasi node `Office` tidak menampilkan tooltip Excess

### TC-FA-CAT-23: Baris Excess di tabel redup dengan row action Edit dan + Add Subcategory Hidden

7. Verifikasi teks Category baris `Furniture` pada tabel L1 di-dim dibanding baris usable
8. Klik elipsis (⋯) pada baris `Furniture`
9. Verifikasi menu baris Excess memuat Detail dan Delete
10. Verifikasi Edit dan + Add Subcategory Hidden (tidak dirender) pada menu baris `Furniture`
11. Tutup menu baris `Furniture`
12. Klik elipsis (⋯) pada baris `Office` (usable)
13. Verifikasi menu baris usable memuat Detail, + Add Subcategory, Edit, dan Delete
14. Tutup menu baris `Office`

### TC-FA-CAT-24: Alert Category Consolidation tampil untuk Total Control saat jumlah kategori melebihi cap

15. Verifikasi Alert varian Warning With Action tampil dengan title `Your plan allows 5 categories`, body `You have 9 categories. Choose which categories stay active.`, dan aksi `[Choose Categories]`
16. Verifikasi Alert tidak memiliki tombol close (✕)

### TC-FA-CAT-316: Menu elipsis node Excess di sidebar memuat Detail dan Delete saja

17. Klik elipsis (⋯) pada node `Furniture` di sidebar
18. Verifikasi menu memuat Detail dan Delete
19. Verifikasi Edit dan + Add Subcategory tidak dirender
20. Tutup menu node `Furniture`

### TC-FA-CAT-317: Saat jumlah kategori melebihi cap, pembuatan kategori baru diblok D-01 sedangkan Detail dan Delete tetap tersedia

21. Klik `[+] Category` di sidebar
22. Verifikasi dialog D-01 `Cannot Add Category` tampil karena jumlah (9) melebihi cap (5)
23. Klik `[OK]`
24. Klik elipsis (⋯) pada baris `Office`
25. Verifikasi menu `Office` (usable) memuat Detail, + Add Subcategory, Edit, dan Delete
26. Klik `+ Add Subcategory`
27. Verifikasi dialog D-01 tampil
28. Klik `[OK]`

### TC-FA-CAT-320: TreeSearchInput ikut mencocokkan node Excess

29. Ketik `Furn` pada TreeSearchInput sidebar lalu Enter
30. Verifikasi node `Furniture` (Excess) tetap tampil sebagai hasil dan redup
31. Hover node `Furniture` hasil pencarian
32. Verifikasi tooltip Excess tampil pada node `Furniture`
33. Verifikasi node yang tidak cocok (`Office`) disembunyikan
34. Kosongkan kotak TreeSearchInput lalu Enter

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 11, 14, 20 (menutup menu), 28 (menutup dialog D-01), 34 (mengosongkan TreeSearchInput). TC-FA-CAT-320 diletakkan terakhir karena menyaring pohon sidebar.
- Expected TC-FA-CAT-317 butir a menyebut dialog D-01 `Cannot Add Category` tanpa isi body; hanya judul dan penyebab (jumlah 9 melebihi cap 5) yang diasersi.
- Expected TC-FA-CAT-320 "redup dengan tooltip Excess" dipecah menjadi `Verifikasi` redup dan `Verifikasi` tooltip (setelah hover, langkah tambahan S-14).
- Temuan untuk QA:
  - TC-FA-CAT-317 tidak menyebut isi body dialog D-01; asersi dibatasi pada judul `Cannot Add Category`.
  - TC-FA-CAT-320 tidak menyebut cara melihat tooltip Excess; spec menambah hover pada node hasil pencarian.
- Ukuran spec 34 langkah, di bawah ambang sekitar 35.
