---
id: TC-FA-BORROW-E2E-040-titik-masuk-borrow-dep-asset-list
title: "Titik masuk Borrow dan Add to Borrow Draft dari Asset List dan Quick Action membuka form dengan aset terisi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#p1", "§4.2.13#b1", "§4.2.13#b2"]
smoke: []
dependsOn: ["Asset List: aksi Borrow dan Add to Borrow Draft"]
trace:
  "§4.1#p1": [6, 16, 25, 41, 46]
  "§4.2.13#b1": [6, 7, 16, 17, 25, 26, 34, 37, 52, 56, 57, 61, 64]
  "§4.2.13#b2": [43, 46]
anchor: []
coverage:
  web: automated
---

# Titik masuk Borrow dan Add to Borrow Draft dari Asset List dan Quick Action membuka form dengan aset terisi

## Prerequisites
- Aktor: `Agus Pratama {runId}`, Asset Admin (Aktor Borrow) pada Group `Head Office`.
- Layar awal: halaman Asset List (Assets > All).
- Data:
  - DU-040-1: aset `Laptop Lenovo ThinkPad {runId}`, Group `Head Office`, Custody `Available`, Allow Borrow `Allow`.
  - DU-040-2: aset `Proyektor BenQ MW550 {runId}`, Group `Head Office`, Custody `Available`, Allow Borrow `Allow`.
  - DU-040-3: aset `Printer Epson L3250 {runId}`, Group `Head Office`, Custody `Available`, Allow Borrow `Allow`; sudah berada di Draft DU-040-7.
  - DU-040-4: aset `Tablet Samsung Tab S9 {runId}`, Group `Head Office`, Custody `Available`, Allow Borrow `Allow`.
  - DU-040-5: karyawan `Rina Wulandari {runId}`, Status `Active`, Eligibility `Can borrow`, tanpa Draft yang bisa diedit Aktor.
  - DU-040-6: karyawan `Dewi Lestari {runId}`, Status `Active`, Eligibility `Can borrow`, punya satu Draft yang bisa diedit Aktor (DU-040-7).
  - DU-040-7: Draft Borrower `Dewi Lestari {runId}`, Group `Head Office`, Total Asset `1`, berisi aset DU-040-3, Modified By `Agus Pratama {runId}`.
  - DU-040-8: Category `Peralatan Berat {runId}` dengan Max assets per borrower `2`; Max assets per borrower Company default bernilai `5`, dan nilai Category menggantikan Company default untuk aset di Category itu.
  - DU-040-9: aset `Excavator Mini Kubota {runId}`, Group `Head Office`, Category `Peralatan Berat {runId}`, Custody `Available`, Allow Borrow `Allow`.
  - DU-040-10: karyawan `Teguh Santoso {runId}`, Home Group `Head Office`, Status `Active`, Active Borrows `2 assets` (DU-040-11), alasan Blocked untuk aset di Category berbatas `Teguh Santoso {runId} can borrow up to 2 assets at a time.`
  - DU-040-11: BRW `Borrowed` Group `Head Office`, Borrower `Teguh Santoso {runId}`, berisi aset `Genset Silent Perkins {runId}` dan `Kompresor Angin Ingersoll {runId}`, keduanya Category `Peralatan Berat {runId}`.
  - DU-040-12: aset `Kursi Rapat Ergotec {runId}`, Group `Head Office`, Custody `Available`, Allow Borrow `Allow`, Allowed borrower `Same Group only`.
  - DU-040-13: karyawan `Bagas Prakoso {runId}`, Home Group `Branch Surabaya`, Status `Active`, Eligibility `Can borrow`.

## Test Steps

### Borrow dari baris aset membuka form Borrow Request dengan Borrower dan aset terisi
1. Ketik Search `{runId}`, tekan Enter
2. Klik menu ⋯ pada baris aset DU-040-1
3. Klik `Borrow`
4. Pilih Borrower `Rina Wulandari {runId}` pada dialog Select Borrower
5. Klik `[Select]`
6. Verifikasi form `Borrow Request` tampil sebagai halaman penuh, bukan dialog, dengan Borrower `Rina Wulandari {runId}`
7. Verifikasi aset `Laptop Lenovo ThinkPad {runId}` terisi pada tabel aset form `Borrow Request`
8. Klik `[Cancel]` pada form `Borrow Request` yang belum diubah pengguna

### Borrow bulk membuka form Borrow Request dengan semua aset terpilih
9. Buka halaman Asset List lewat sidebar `Assets` > `All`
10. Ketik Search `{runId}`, tekan Enter
11. Centang baris `Laptop Lenovo ThinkPad {runId}`
12. Centang baris `Proyektor BenQ MW550 {runId}`
13. Klik aksi bulk `Borrow`
14. Pilih Borrower `Rina Wulandari {runId}` pada dialog Select Borrower
15. Klik `[Select]`
16. Verifikasi form `Borrow Request` tampil dengan Borrower `Rina Wulandari {runId}`
17. Verifikasi aset `Laptop Lenovo ThinkPad {runId}` dan aset `Proyektor BenQ MW550 {runId}` terisi pada tabel aset
18. Klik `[Cancel]` pada form `Borrow Request` yang belum diubah pengguna

### Add to Borrow Draft dari baris aset untuk Borrower tanpa Draft membuat Draft baru
19. Buka halaman Asset List lewat sidebar `Assets` > `All`
20. Ketik Search `{runId}`, tekan Enter
21. Klik menu ⋯ pada baris aset DU-040-4
22. Klik `Add to Borrow Draft`
23. Pilih Borrower `Rina Wulandari {runId}` pada dialog Select Borrower
24. Klik `[Select]`
25. Verifikasi toast `Success, 1 asset has been added to the draft.` tampil langsung karena Borrower belum punya Draft yang bisa diedit
26. Verifikasi aset `Tablet Samsung Tab S9 {runId}` tetap berstatus `Available` di Asset List karena Draft tidak mengunci aset

### Add to Borrow Draft bulk untuk Borrower yang punya Draft membuka dialog pilihan Draft
27. Buka halaman Asset List lewat sidebar `Assets` > `All`
28. Ketik Search `{runId}`, tekan Enter
29. Centang baris `Laptop Lenovo ThinkPad {runId}`
30. Centang baris `Proyektor BenQ MW550 {runId}`
31. Klik aksi bulk `Add to Borrow Draft`
32. Pilih Borrower `Dewi Lestari {runId}` pada dialog Select Borrower
33. Klik `[Select]`
34. Verifikasi dialog `Add to Borrow Draft` tampil dengan subjudul `[Borrower] has 1 draft you can edit.` dengan [Borrower] berisi `Dewi Lestari {runId}`
35. Pilih Draft DU-040-7 pada dialog `Add to Borrow Draft`
36. Klik `[Add to Borrow Draft]`
37. Verifikasi toast `Success, 2 assets have been added to the draft.` tampil

### Tombol + Borrow di halaman Borrow membuka form Borrow Request
38. Klik `Transactions` pada sidebar
39. Klik `Borrow`
40. Klik `[+ Borrow]`
41. Verifikasi form `Borrow Request` tampil dengan tombol `[Select Borrower]` dan keterangan `No assets added` pada tabel aset
42. Klik `[Cancel]` pada form `Borrow Request` yang belum diubah pengguna

### Item Borrow di Quick Action navbar membuka form Borrow Request tanpa aset
43. Verifikasi `Quick Action` tampil pada navbar
44. Klik `Quick Action` pada navbar
45. Klik `Borrow`
46. Verifikasi form `Borrow Request` tampil dengan tombol `[Select Borrower]` dan keterangan `No assets added` pada tabel aset
47. Klik `[Cancel]` pada form `Borrow Request` yang belum diubah pengguna

### Max assets dinilai terhadap aset terpilih pada dialog Select Borrower
48. Buka halaman Asset List lewat sidebar `Assets` > `All`
49. Ketik Search `{runId}`, tekan Enter
50. Klik menu ⋯ pada baris aset DU-040-1
51. Klik `Borrow`
52. Verifikasi Borrower `Teguh Santoso {runId}` pada dialog Select Borrower berstatus `Can borrow` karena aset terpilih tidak berada di Category berbatas
53. Tutup dialog Select Borrower
54. Klik menu ⋯ pada baris aset DU-040-9
55. Klik `Borrow`
56. Verifikasi Borrower `Teguh Santoso {runId}` pada dialog Select Borrower berstatus `Blocked` dan tidak dapat dipilih karena 2 aset aktifnya ditambah aset terpilih melebihi Max assets per borrower Category `Peralatan Berat {runId}` yaitu `2`
57. Verifikasi alasan `Teguh Santoso {runId} can borrow up to 2 assets at a time.` tersampaikan pada Borrower `Teguh Santoso {runId}`
58. Tutup dialog Select Borrower

### Allowed borrower dinilai pada aset di form, bukan di dialog Select Borrower
59. Klik menu ⋯ pada baris aset DU-040-12
60. Klik `Borrow`
61. Verifikasi Borrower `Bagas Prakoso {runId}` pada dialog Select Borrower berstatus `Can borrow` walau Allowed borrower aset `Same Group only` tidak terpenuhi, karena Allowed borrower tidak dinilai di dialog
62. Pilih Borrower `Bagas Prakoso {runId}` pada dialog Select Borrower
63. Klik `[Select]`
64. Verifikasi baris aset `Kursi Rapat Ergotec {runId}` pada form `Borrow Request` ditandai tidak layak dengan caption `This asset can no longer be borrowed.` karena Borrower `Bagas Prakoso {runId}` bukan dari Group aset
65. Klik `[Cancel]` pada form `Borrow Request` yang belum diubah pengguna
