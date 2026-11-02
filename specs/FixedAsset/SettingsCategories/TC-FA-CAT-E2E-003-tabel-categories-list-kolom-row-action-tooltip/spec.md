---
id: TC-FA-CAT-E2E-003-tabel-categories-list-kolom-row-action-tooltip
title: "Tabel Categories List: Kolom, Row Action, Bulk Action Bar, Total Asset, dan Tooltip Table Tools"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-14
  - TC-FA-CAT-15
  - TC-FA-CAT-16
  - TC-FA-CAT-17
  - TC-FA-CAT-11
coverage:
  web: automated
---

# Tabel Categories List: Kolom, Row Action, Bulk Action Bar, Total Asset, dan Tooltip Table Tools

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: client CatMain (Pre-setup #20, plan Enterprise): 15 kategori; L1 `Accessory`, `Default Category`, `Electronics` (anak `Laptop`, `Monitor`), `Furniture`, `Peripheral` (anak `Keyboard`, `Mouse`), `Spare Part`, `Tools`, `Vehicle`. Spec hanya membaca; tidak membuat atau mengubah data.
- Data tambahan: aset Pre-setup #22 pada node `Laptop` (12 aset terhitung: 10 Active, 1 Draft, 1 Waiting for Approval; 3 aset tidak terhitung: 2 Disposed, 1 Deleted), disediakan tim FE/BE lewat seed API. Dipakai untuk TC-FA-CAT-11.
- Pembanding sort dan format: baris L1 `Accessory` dan `Default Category` (urutan Category A-Z), Modified By `Jane Smith` pada baris `Electronics`.
- Flag Guided Tooltip halaman Categories: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan client Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-categories.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-14: Kolom default, default sort Category A-Z, dan format tampilan sel

1. Verifikasi kolom berurutan: Category (text link), Code, Total Asset, Modified By, Last Updated
2. Verifikasi kelima kolom sortable dan default Visible
3. Verifikasi urutan baris default Category A-Z case-insensitive (`Accessory` sebelum `Default Category`)
4. Verifikasi Code pada baris `Electronics` tampil huruf kapital `ELEC`
5. Verifikasi Total Asset tampil angka bulat dan `0` tampil `0` bukan `—`
6. Verifikasi Modified By pada baris `Electronics` tampil `Jane S`
7. Hover nilai Modified By pada baris `Electronics`
8. Verifikasi tooltip `Jane Smith` tampil
9. Verifikasi Category pada baris `Electronics` tampil sebagai teks biasa netral
10. Hover Category pada baris `Electronics`
11. Verifikasi Category berubah ke warna primary FAMS (biru) tanpa garis bawah saat di-hover

### TC-FA-CAT-15: Isi dan urutan menu row action beserta icon dan severity

12. Klik elipsis (⋯) pada baris `Furniture`
13. Verifikasi menu memuat aksi berurutan: Detail, + Add Subcategory, Edit, Delete
14. Verifikasi icon dan severity tiap aksi: Detail `FileInfoLine` (dark), + Add Subcategory `AddLine` (dark), Edit `Edit2Line` (dark), Delete `DeleteBin6Line` (danger)
15. Tutup menu row action
16. Klik elipsis (⋯) pada node `Furniture` di sidebar
17. Verifikasi menu pada elipsis node sidebar memuat aksi yang sama dengan menu baris tabel
18. Tutup menu elipsis node sidebar

### TC-FA-CAT-16: Bulk Action Bar tidak tampil tanpa seleksi dan checkbox berada di kolom pertama

19. Verifikasi sisi kiri baris bar kosong dan hanya Table Tools yang tampil (tanpa seleksi)
20. Centang checkbox baris `Tools`
21. Verifikasi Bulk Action Bar muncul
22. Hapus centang checkbox baris `Tools`
23. Verifikasi Bulk Action Bar hilang
24. Verifikasi kolom Checkbox pinned kiri sebagai kolom pertama
25. Verifikasi kolom Actions (⋯) pinned kanan

### TC-FA-CAT-17: Tooltip icon Table Tools dan header Column Visibility

26. Hover icon Search
27. Verifikasi tooltip `Search` tampil
28. Hover icon Filter
29. Verifikasi tooltip `Filter` tampil
30. Hover icon Download
31. Verifikasi tooltip `Download` tampil
32. Hover icon Changelog
33. Verifikasi tooltip `Changelog` tampil
34. Hover ikon (⋯) di header kolom Actions
35. Verifikasi tooltip `Column Visibility` tampil
36. Pindahkan fokus keyboard (Tab) ke icon Search, Filter, Download, Changelog, dan ikon (⋯) header kolom Actions satu per satu
37. Verifikasi tooltip yang sama dengan hover muncul saat tiap elemen mendapat fokus keyboard

### TC-FA-CAT-11: Total Asset exact-match node dengan himpunan lifecycle Draft, Waiting for Approval, dan Active

38. Klik node `Electronics` di sidebar
39. Catat Total Asset baris `Laptop`
40. Verifikasi baris `Laptop` menampilkan Total Asset `12` (10 Active + 1 Draft + 1 Waiting for Approval; 2 aset Disposed dan 1 aset Deleted tidak dihitung)
41. Klik angka Total Asset baris `Laptop`
42. Verifikasi tabel Assets pada Popup Detail `Laptop` memuat 12 aset (sama dengan Total Asset yang dicatat)
43. Tutup Popup Detail
44. Klik node `Laptop` di sidebar
45. Verifikasi Category Context Header node `Laptop` menampilkan Total Asset `12` (sama dengan angka yang dicatat)
46. Klik root `All Categories`
47. Verifikasi baris `Electronics` pada tabel L1 menampilkan Total Asset `0` (exact-match node itu sendiri, bukan agregat descendant)

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 15, 18 (menutup menu), 43 (menutup Popup Detail). Langkah klik elipsis node sidebar `Furniture` (langkah 16), pindah fokus keyboard (langkah 36), serta klik node `Laptop` dan root `All Categories` (langkah 44 dan 46) ditambahkan agar Expected TC punya langkah menuju keadaannya (S-14).
- TC-FA-CAT-14 dan TC-FA-CAT-16 membaca tabel L1 pada keadaan awal halaman; tidak ada sort, Search, atau Filter yang diubah. TC-FA-CAT-11 diletakkan terakhir karena berpindah node dan membuka Popup Detail.
- Temuan untuk QA:
  - TC-FA-CAT-15 butir b menyebut menu elipsis node sidebar tanpa langkah uji; spec menambah klik elipsis node `Furniture` di sidebar.
  - TC-FA-CAT-17 butir b (tooltip muncul saat fokus keyboard) tidak menyebut elemen mana saja; spec memindahkan fokus ke kelima elemen pada butir a dengan satu `Verifikasi`.
  - TC-FA-CAT-11 butir a menyebut 2 aset Disposed dan 1 aset Deleted tidak dihitung tanpa observasi terpisah; hal itu dimasukkan sebagai bagian nilai `12` yang diasersi.
  - TC-FA-CAT-11 butir c: jumlah baris tabel Assets dibaca dari seeding (12, bagian 8b butir 10), bukan dari halaman tunggal.
- Ukuran spec 47 langkah, melewati sekitar 35 karena Expected dipecah per klausa (S-01) dan tooltip lima elemen dipisah per elemen. Seluruh blok satu kelas harness (fungsional, baca saja), satu dataset (CatMain), tanpa aksi tulis, dan tiap blok berdiri sendiri; spec tidak dipecah (konvensi bagian 3, batas ukuran).
- Spec melewati 35 langkah (47 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri; nomor cadangan slice habis sehingga tidak dipecah lebih jauh.
