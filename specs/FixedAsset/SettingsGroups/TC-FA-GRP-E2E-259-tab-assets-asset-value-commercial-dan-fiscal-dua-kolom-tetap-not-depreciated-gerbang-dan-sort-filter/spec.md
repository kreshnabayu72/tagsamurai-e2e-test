---
id: TC-FA-GRP-E2E-259-tab-assets-asset-value-commercial-dan-fiscal-dua-kolom-tetap-not-depreciated-gerbang-dan-sort-filter
title: "Tab Assets Asset Value Commercial dan Fiscal: Dua Kolom Tetap dengan Tooltip, Not Depreciated Menampilkan Harga Perolehan, Gerbang AST-LOGIC-10 di Kedua Kolom, dan Sort/Filter/Search per Buku"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1284
  - TC-FA-GRP-1286
  - TC-FA-GRP-1287
  - TC-FA-GRP-1288
coverage:
  web: automated
---

# Tab Assets Asset Value Commercial dan Fiscal: Dua Kolom Tetap dengan Tooltip, Not Depreciated Menampilkan Harga Perolehan, Gerbang AST-LOGIC-10 di Kedua Kolom, dan Sort/Filter/Search per Buku

## Prerequisites

- Mode: FE+BE.
- Akun viewAssetValueGroups (Pre-setup No 12; Group Role View asset value pada Value Gate Node A): `viewAssetValueGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_VIEWASSETVALUE_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun noValueAccess (Pre-setup No 16; tanpa View asset value, Manage purchase, maupun Manage accounting): `noValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_NOVALUEACCESS_PASSWORD`. Dipakai lewat langkah ganti akun eksplisit.
- Hook suite (`suite.md`) berlaku: sesi API aktor, fixture BE, flag Guided Tooltip `seen`, dan pemulihan state global; tidak ditulis ulang di sini.
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (dibaca; tidak diubah).
- Data Value Gate Node A (Tabel Dinamis No 10, hanya dibaca, tidak diubah): G1 `Laptop Dell - 1`, G2 `Printer HP - 1`, G3 `Monitor LG - 1`, G4 `Forklift Toyota - 1`, G5 `Kabel Roll - 1`, G6 `Laptop Dell - 2`. Asset Value (Commercial): G1 1500, G2 0, G3 belum ada, G4 8000, G5 120, G6 2300. Asset Value (Fiscal): G1 1200, G2 500, G3 belum ada, G4 7000, G5 150, G6 2000. Warranty Expiry: G1 15/03/2027, G2 20/01/2027, G3 dan G5 belum ada, G4 20/05/2028, G6 01/01/2026. PO Number: G1 `PO-001`, G2 `PO-002`, G3 belum diisi, G4 dan G5 di luar Scope, G6 `PO-006`. Cost Account: G1 `CA-100`, G2 `CA-150`, G3 belum diisi, G4 dan G5 di luar Scope, G6 `CA-200`.
- Data Value Gate Node B (Tabel Dinamis No 11, hanya dibaca): B1, B2, B3; aktor VAV tidak memegang View asset value pada Value Gate Node B. Buku Commercial dan Fiscal (Tabel Dinamis No 20); G2 dan G5 ber-Asset Class Not Depreciated/Tax Method kosong pada buku Fiscal (harga perolehan G2 500, G5 150).
- Kemampuan teknis: menghapus preferensi kolom Setup Column di browser (disediakan tim FE).
- Preferensi kolom Setup Column yang disimpan spec ini dihapus dari browser di hook `after` (kemampuan disediakan tim FE).
- State global: tidak ada yang diubah. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1284: Dua kolom tetap Asset Value dengan tooltip

1. Buka Detail Value Gate Node A (Tab Assets)
2. Buka Popup Setup Column
3. Verifikasi Popup Setup Column memuat tepat dua kolom curated `Asset Value (Commercial)` lalu `Asset Value (Fiscal)` (unchecked, enabled), berurutan setelah Last Scanned dan sebelum Warranty Expiry, tanpa kolom `Asset Value` tunggal dan tanpa kolom buku lain
4. Centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)` di Popup Setup Column, klik [Save]
5. Verifikasi Commercial: G1 1500, G2 currency nol, G3 `—`, G4 8000, G5 120, G6 2300
6. Verifikasi Fiscal: G1 1200, G2 500 dan G5 150 (harga perolehan), G3 `—`, G4 7000, G6 2000
7. Verifikasi format currency 2 desimal rata kanan mengikuti `prd-conventions.md` §32
8. Hover sel G1 pada kolom `Asset Value (Commercial)`
9. Verifikasi tooltip memuat metode dan masa manfaat buku Commercial (mis. `Straight Line · 60 months`)
10. Hover sel G1 pada kolom `Asset Value (Fiscal)`
11. Verifikasi tooltip memuat metode dan masa manfaat buku Fiscal (mis. `Straight Line · 60 months`)
12. Verifikasi metode tidak menjadi kolom tersendiri pada header tabel

### TC-FA-GRP-1286: Not Depreciated menampilkan harga perolehan

13. Amati G2, G3, dan G5 pada kedua kolom (kedua kolom tercentang dari blok TC-FA-GRP-1284)
14. Verifikasi kolom Fiscal: G2 menampilkan 500 dan G5 menampilkan 150 (harga perolehan; bukan `—`, bukan `No access`, bukan nol)
15. Verifikasi kolom Commercial: G2 currency nol dan G5 120
16. Verifikasi G3 (nilai belum ada) menampilkan `—` pada kedua kolom

### TC-FA-GRP-1288: Sort, Filter, dan Search per kolom buku

17. Klik header `Asset Value (Fiscal)` (Ascending)
18. Verifikasi urutan Fiscal Ascending: G5 (150), G2 (500), G1 (1200), G6 (2000), G4 (7000), lalu baris `—` (G3) di akhir
19. Klik header `Asset Value (Fiscal)` (Descending)
20. Verifikasi urutan Fiscal Descending: baris `—` (G3) di awal, lalu G4, G6, G1, G2, G5
21. Verifikasi kolom `Asset Value (Commercial)` tidak menampilkan indikator sort
22. Klik icon Filter
23. Verifikasi Filter Panel memuat satu field per kolom buku (`Asset Value (Commercial)`, `Asset Value (Fiscal)`)
24. Isi field `Asset Value (Fiscal)` Min 1000 dan Max 3000, klik [Apply]
25. Verifikasi hanya G1 dan G6 tampil
26. Klik [Clear Field], klik [Apply]
27. Ketik Search teks nilai Fiscal G4 persis seperti tampil di sel, tekan Enter
28. Verifikasi hanya G4 tampil
29. Klik `(←)` pada kotak Search
30. Buka Popup Setup Column, hilangkan centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, klik [Save]

### TC-FA-GRP-1287: Gerbang AST-LOGIC-10 di kedua kolom

31. Buka Detail Value Gate Node B (Tab Assets)
32. Centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)` di Popup Setup Column, klik [Save]
33. Verifikasi B1, B2, dan B3 menampilkan `No access` pada kedua kolom
34. Hover sel `No access`
35. Verifikasi tooltip "Requires View asset value access in this group."
36. Buka Popup Setup Column, hilangkan centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, klik [Save]
37. Logout
38. Login sebagai akun noValueAccess
39. Buka Detail Value Gate Node A (Tab Assets)
40. Centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)` di Popup Setup Column, klik [Save]
41. Verifikasi G1 sampai G6 menampilkan `No access` pada kedua kolom
42. Verifikasi tidak ada nilai atau harga perolehan yang tampil, termasuk pada G2 dan G5 (Not Depreciated)

## Notes

- Urutan TC: TC-1284 (screening), TC-1286, TC-1288, lalu TC-1287 dengan ganti akun ke NVA di akhir (S-10).
- Langkah penghubung (S-03): kedua kolom tetap tercentang dari TC-1284 sehingga langkah centang TC-1286 dan TC-1288 tidak diulang; menghilangkan centang antar blok; `[Clear Field]` dan `[Apply]` untuk membersihkan filter; klik `(←)` pada kotak Search untuk membersihkan Search.
- Alasan di atas ~35 langkah: satu dataset (Value Gate Node A, dua kolom buku) dengan empat blok yang berdiri sendiri; blok sesudah ganti akun tetap bermakna walau blok sebelumnya gagal.
- Temuan untuk QA:
  - TC-1284 butir d tidak memberi teks tooltip persis (hanya contoh `Straight Line · 60 months`); spec mengasersi isi metode dan masa manfaat.
  - TC-1288 butir a 'urutan acuan kolom Commercial tidak ikut berubah' ambigu; spec mengasersi kolom Commercial tidak menampilkan indikator sort.
  - TC-1288 mengosongkan field Filter dengan `[Clear Field]` tanpa menyebut `[Apply]`; spec menambah `[Apply]` sebagai langkah penghubung.
