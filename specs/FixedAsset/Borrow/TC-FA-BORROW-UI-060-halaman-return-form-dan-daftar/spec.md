---
id: TC-FA-BORROW-UI-060-halaman-return-form-dan-daftar
title: "Halaman Return: daftar aset, kolom Verification dan Return Photo, error Submit, dan aksi baris"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: [FI-BRW-100, FI-BRW-101, FI-BRW-102, FI-BRW-103, FI-BRW-104, FI-BRW-105, FI-BRW-106, FI-BRW-107, FI-BRW-108, FI-BRW-110, FI-BRW-111, FI-BRW-112, FI-BRW-113, FI-BRW-114, FI-BRW-133, FI-BRW-134, FI-BRW-135, FI-BRW-136, FI-BRW-87, FI-BRW-88, FI-BRW-89, FI-BRW-90, FI-BRW-91, FLD-BRW-22, FLD-BRW-23, FLD-BRW-24, FLD-BRW-25, EB-ERR-1@return]
smoke: []
dependsOn: []
trace:
  FI-BRW-100: 60
  FI-BRW-101: [2, 3]
  FI-BRW-102: [4, 5]
  FI-BRW-103: [5, 8]
  FI-BRW-104: 11
  FI-BRW-105: 20
  FI-BRW-106: 10
  FI-BRW-107: [14, 15, 18]
  FI-BRW-108: 16
  FI-BRW-110: [30, 40, 41, 44, 45]
  FI-BRW-111: 29
  FI-BRW-112: 73
  FI-BRW-113: 63
  FI-BRW-114: 65
  FI-BRW-133: [6, 7, 21, 22, 23, 24, 25]
  FI-BRW-134: 76
  FI-BRW-135: [67, 69]
  FI-BRW-136: [67, 69]
  FI-BRW-87: [48, 49, 56]
  FI-BRW-88: 50
  FI-BRW-89: 52
  FI-BRW-90: 57
  FI-BRW-91: [27, 37]
  FLD-BRW-22: [29, 33, 34]
  FLD-BRW-23: [30, 63]
  FLD-BRW-24: [40, 44]
  FLD-BRW-25: [41, 45]
  EB-ERR-1@return: [71, 72, 73, 74, 76, 79, 80, 81, 82, 84]
anchor: []
coverage:
  web: automated
---

# Halaman Return: daftar aset, kolom Verification dan Return Photo, error Submit, dan aksi baris

## Prerequisites
- Aktor: Aktor Borrow dengan cakupan Group `Finance`.
- Layar awal: Halaman Return
- Komponen: Halaman Return
- Data:
  - DU-060-1: Borrower `Budi Santoso`.
  - DU-060-2: aset di daftar Return, Name `Printer Epson L3110`, Asset ID `AST-0001`, Brand `Epson`, Model/Type `L3110`, TAG `TAG-0001`, Status `Borrowed`, Transaction ID `BRW-0001`, Group `Finance`, Due Return Date `20/12/2026`, Verification `Unverified`, Return Photo `tanpa foto`.
  - DU-060-3: aset di daftar Return, Name `Laptop Dell Latitude 5420`, Asset ID `AST-0002`, Brand `Dell`, Model/Type `Latitude 5420`, TAG `TAG-0002`, Status `Overdue`, Transaction ID `BRW-0002`, Group `Finance`, Due Return Date `05/11/2026`, Verification `Unverified`, Return Photo `tanpa foto`.
  - DU-060-4: aset di daftar Return tanpa TAG, Name `Meja Kerja Kayu`, Asset ID `AST-0003`, Brand `Olympic`, Model/Type `Meja Kerja 120`, TAG `—`, Status `Borrowed`, Transaction ID `BRW-0001`, Group `Finance`, Due Return Date `20/12/2026`, Verification `Non TAG`, Return Photo `tanpa foto`.
  - DU-060-5: aset ber-TAG, Name `Kamera Canon EOS 200D`, Asset ID `AST-0004`, Brand `Canon`, Model/Type `EOS 200D`, TAG `TAG-0004`, Status `Borrowed`, Transaction ID `BRW-0003`, Group `Finance`, Due Return Date `20/12/2026`, Verification `Unverified`, Return Photo `tanpa foto`.
  - DU-060-6: aset ber-TAG, Name `Proyektor BenQ MX550`, Asset ID `AST-0005`, Brand `BenQ`, Model/Type `MX550`, TAG `TAG-0005`, Status `Borrowed`, Transaction ID `BRW-0003`, Group `Finance`, Due Return Date `20/12/2026`, Verification `Unverified`, Return Photo `tanpa foto`.
  - DU-060-7: Borrower `Sari Wulandari`.
  - DU-060-8: 10 aset tambahan di dialog Select Asset, Name `Kursi Lipat Cabang {n}`, Asset ID `AST-02{n}`, Transaction ID `BRW-0004`, Group `Finance`, Due Return Date `20/12/2026`.
  - DU-060-9: aset milik Borrower `Budi Santoso`, Name `Proyektor Epson EB-X06`, Asset ID `AST-0007`, Brand `Epson`, Model/Type `EB-X06`, TAG `TAG-0007`, Status `Borrowed`, Transaction ID `BRW-0005`, Group `Regional Jakarta`, Due Return Date `20/12/2026`.
  - DU-060-10: aset tambahan di daftar sehingga jumlah aset melebihi Bulk Transaction Row Limit, Name `Kursi Lipat Gudang {n}`, Asset ID `AST-03{n}`, TAG `—`, Status `Borrowed`, Transaction ID `BRW-0006`, Group `Finance`, Due Return Date `20/12/2026`.
  - DU-060-11: berkas foto Return Photo `printer-epson-kembali.jpg`.
  - DU-060-12: aset di daftar Return tanpa TAG, Name `Scanner Fujitsu fi-7160`, Asset ID `AST-0008`, Brand `Fujitsu`, Model/Type `fi-7160`, TAG `—`, Status `Extension Request`, Transaction ID `BRW-0007`, Group `Finance`, Due Return Date `20/12/2026`, Verification `Non TAG`, Return Photo `—`.
  - DU-060-13: aset di daftar Return tanpa TAG, Name `Monitor LG 24MK430`, Asset ID `AST-0009`, Brand `LG`, Model/Type `24MK430`, TAG `—`, Status `Overdue` dan `Extension Approval`, Transaction ID `BRW-0008`, Group `Finance`, Due Return Date `01/11/2026`, Verification `Non TAG`, Return Photo `—`.
  - DU-060-14: aset di daftar Return tanpa TAG, Name `Tablet Samsung Galaxy Tab A8`, Asset ID `AST-0010`, Brand `Samsung`, Model/Type `Galaxy Tab A8`, TAG `—`, Status `Borrowed` dan `Reported Damaged`, Transaction ID `BRW-0009`, Group `Finance`, Due Return Date `20/12/2026`, Verification `Non TAG`, Return Photo `—`.
  - DU-060-15: aset di daftar Return tanpa TAG, Name `Kamera Sony A6000`, Asset ID `AST-0011`, Brand `Sony`, Model/Type `A6000`, TAG `—`, Status `Borrowed` dan `Damaged`, Transaction ID `BRW-0010`, Group `Finance`, Due Return Date `20/12/2026`, Verification `Non TAG`, Return Photo `—`.
  - DU-060-16: aset di daftar Return tanpa TAG, Name `Drone DJI Mini 3`, Asset ID `AST-0012`, Brand `DJI`, Model/Type `Mini 3`, TAG `—`, Status `Borrowed` dan `Reported Missing`, Transaction ID `BRW-0011`, Group `Finance`, Due Return Date `20/12/2026`, Verification `Non TAG`, Return Photo `—`.
  - DU-060-17: aset di daftar Return tanpa TAG, Name `Speaker JBL PartyBox`, Asset ID `AST-0013`, Brand `JBL`, Model/Type `PartyBox`, TAG `—`, Status `Extension Request`, Transaction ID `BRW-0012`, Group `Finance`, Due Return Date `20/12/2026`, Verification `Non TAG`, Return Photo `—`.
- Kondisi:
  - K1: Photo at end bernilai ON, Date Format bernilai `DD/MM/YYYY`, Borrower DU-060-1 sudah terpilih, daftar berisi DU-060-2, DU-060-3, dan DU-060-4.
  - K2: Photo at end bernilai OFF, Borrower DU-060-1 sudah terpilih, daftar berisi DU-060-12, DU-060-13, DU-060-14, DU-060-15, dan DU-060-16.
  - K3: Photo at end bernilai ON, Borrower DU-060-1 sudah terpilih, daftar berisi DU-060-2.
  - K4: Photo at end bernilai ON, Borrower DU-060-1 sudah terpilih, daftar berisi DU-060-4, DU-060-5, dan DU-060-6.
  - K5: Borrower belum dipilih, daftar kosong, opsi Borrower adalah DU-060-1 dan DU-060-7.
  - K6: Borrower DU-060-1 sudah terpilih, daftar kosong, dialog Select Asset memuat DU-060-5, DU-060-6, lalu DU-060-8, sehingga lebih dari satu halaman.
  - K7: Borrower DU-060-1 sudah terpilih, daftar kosong, hasil scan TAG `TAG-0007` adalah DU-060-9.
  - K8: Borrower DU-060-1 sudah terpilih, daftar berisi DU-060-2 dan DU-060-10, dan jumlah aset di daftar melebihi Bulk Transaction Row Limit.
  - K9: Photo at end bernilai OFF, Borrower DU-060-1 sudah terpilih, daftar berisi DU-060-12 dan DU-060-17.
  - K10: Photo at end bernilai OFF, Borrower DU-060-1 sudah terpilih dan masih memegang DU-060-3 yang tidak dimasukkan ke daftar, daftar berisi DU-060-12, DU-060-14, dan DU-060-16, Submit pertama dijawab error server, Submit berikutnya berhasil.
  - K11: Photo at end bernilai OFF, Borrower DU-060-1 sudah terpilih, daftar berisi DU-060-14 dan DU-060-16, Submit pertama tidak mendapat respons karena koneksi putus, Submit berikutnya berhasil.

## Test Steps

### Kolom Verification, Due Return Date, dan Status baris daftar
1. Tampilkan Halaman Return dengan kondisi K1
2. Verifikasi kolom Verification baris `Printer Epson L3110` menampilkan badge `Unverified`
3. Verifikasi kolom Verification baris `Meja Kerja Kayu` tidak menampilkan badge `Unverified`
4. Verifikasi kolom Due Return Date baris `Printer Epson L3110` menampilkan `20/12/2026`
5. Verifikasi kolom Due Return Date baris `Laptop Dell Latitude 5420` menampilkan `05/11/2026` sebagai teks `danger`
6. Verifikasi kolom Status baris `Printer Epson L3110` menampilkan badge `Borrowed`
7. Verifikasi kolom Status baris `Laptop Dell Latitude 5420` menampilkan badge `Overdue`
8. Verifikasi kolom Name baris `Laptop Dell Latitude 5420` tidak menampilkan badge `Overdue`

### Field Return Photo per aset saat Photo at end ON
9. Tampilkan Halaman Return dengan kondisi K1
10. Verifikasi kolom Return Photo baris `Printer Epson L3110` menampilkan tombol ambil foto
11. Verifikasi baris `Laptop Dell Latitude 5420` memiliki field Return Photo sendiri dengan tombol ambil foto
12. Pilih berkas `printer-epson-kembali.jpg` pada field Return Photo baris `Printer Epson L3110`
13. Klik `[Apply]` pada dialog `Adjust photo`
14. Verifikasi thumbnail foto tampil pada kolom Return Photo baris `Printer Epson L3110`
15. Verifikasi ikon Edit dan ikon Delete tampil di samping thumbnail baris `Printer Epson L3110`
16. Verifikasi kolom Return Photo baris `Printer Epson L3110` tidak menampilkan badge centang
17. Klik thumbnail foto baris `Printer Epson L3110`
18. Verifikasi pratinjau foto ukuran penuh tampil

### Return Photo `—` dan badge Status saat Photo at end OFF
19. Tampilkan Halaman Return dengan kondisi K2
20. Verifikasi kolom Return Photo baris `Scanner Fujitsu fi-7160` menampilkan `—`
21. Verifikasi kolom Status baris `Scanner Fujitsu fi-7160` menampilkan badge `Extension Request`
22. Verifikasi kolom Status baris `Monitor LG 24MK430` menampilkan dua badge, `Overdue` dan `Extension Approval`
23. Verifikasi kolom Status baris `Tablet Samsung Galaxy Tab A8` menampilkan badge `Reported Damaged`
24. Verifikasi kolom Status baris `Kamera Sony A6000` menampilkan badge `Damaged`
25. Verifikasi kolom Status baris `Drone DJI Mini 3` menampilkan badge `Reported Missing`

### Borrower dan daftar kosong ditolak saat Submit
26. Tampilkan Halaman Return dengan kondisi K5
27. Verifikasi tombol `[+ Asset]` disabled
28. Klik `[Submit]`
29. Verifikasi pesan `You must pick a borrower` tampil di bawah field Borrower
30. Verifikasi ringkasan error di atas tombol `[Submit]` menampilkan `Add at least one asset to return.`
31. Klik field Borrower
32. Isi kotak Search field Borrower dengan `Sari Wulandari`
33. Verifikasi opsi `Sari Wulandari` tampil di daftar opsi Borrower
34. Verifikasi opsi `Budi Santoso` tidak tampil di daftar opsi Borrower
35. Ganti isi kotak Search field Borrower dengan `Budi Santoso`
36. Pilih opsi `Budi Santoso`
37. Verifikasi tombol `[+ Asset]` aktif

### Ringkasan error untuk satu aset
38. Tampilkan Halaman Return dengan kondisi K3
39. Klik `[Submit]`
40. Verifikasi ringkasan error di atas tombol `[Submit]` menampilkan `1 asset is not verified. Scan it with Verify Asset.`
41. Verifikasi ringkasan error di atas tombol `[Submit]` menampilkan `1 asset needs a return photo.`

### Ringkasan error untuk beberapa aset
42. Tampilkan Halaman Return dengan kondisi K4
43. Klik `[Submit]`
44. Verifikasi ringkasan error di atas tombol `[Submit]` menampilkan `2 assets are not verified. Scan them with Verify Asset.`
45. Verifikasi ringkasan error di atas tombol `[Submit]` menampilkan `3 assets need a return photo.`

### Dialog Select Asset dari tombol `[+ Asset]`
46. Tampilkan Halaman Return dengan kondisi K6
47. Klik `[+ Asset]`
48. Verifikasi dialog Select Asset menampilkan kolom `Photo`, `Name`, `Asset ID`, `Transaction ID`, `Group`, dan `Due Return Date`
49. Verifikasi dialog Select Asset menampilkan kotak Search, Filter `Asset Name`, `Transaction ID`, dan `Group`, serta paginasi
50. Verifikasi tombol `[Select]` aktif sebelum ada aset yang dipilih
51. Klik `[Select]`
52. Verifikasi caption error `You must pick an asset` tampil di footer dialog Select Asset
53. Centang baris `Kamera Canon EOS 200D`
54. Centang baris `Proyektor BenQ MX550`
55. Klik `[Select]`
56. Verifikasi baris `Kamera Canon EOS 200D` dan `Proyektor BenQ MX550` masuk ke daftar aset
57. Verifikasi kolom Verification baris `Kamera Canon EOS 200D` dan `Proyektor BenQ MX550` menampilkan badge `Unverified`

### Hasil scan aset dengan Group asal di luar cakupan Aktor
58. Tampilkan Halaman Return dengan kondisi K7
59. Pindai TAG `TAG-0007` lewat `[Verify Asset]`
60. Verifikasi toast `Error, return this asset to Regional Jakarta.` tampil

### Jumlah aset melebihi Bulk Transaction Row Limit
61. Tampilkan Halaman Return dengan kondisi K8
62. Klik `[Submit]`
63. Verifikasi dialog blok Bulk Transaction Row Limit tampil dengan tombol `[OK]`
64. Klik `[OK]`
65. Verifikasi baris `Printer Epson L3110` tetap tampil di daftar aset dan Borrower `Budi Santoso` tetap terpilih

### Catatan pengajuan Extend yang dibatalkan untuk beberapa baris
66. Tampilkan Halaman Return dengan kondisi K9
67. Verifikasi catatan di atas tombol `[Submit]` menampilkan `2 extension requests will be canceled.`

### Submit gagal karena error server lalu diulang
68. Tampilkan Halaman Return dengan kondisi K10
69. Verifikasi catatan di atas tombol `[Submit]` menampilkan `1 extension request will be canceled.`
70. Klik `[Submit]`
71. Verifikasi toast `Error, failed to return assets.` tampil
72. Verifikasi toast error Return tidak menampilkan tombol aksi `[Try Again]`
73. Verifikasi Borrower `Budi Santoso` tetap terpilih, daftar tetap memuat `Scanner Fujitsu fi-7160`, `Tablet Samsung Galaxy Tab A8`, dan `Drone DJI Mini 3`, dan baris `Laptop Dell Latitude 5420` tidak ada di daftar
74. Verifikasi tombol `[Submit]` aktif lagi
75. Klik `[Submit]`
76. Verifikasi toast `Success, 3 assets have been returned.` tampil

### Submit gagal karena koneksi putus lalu diulang
77. Tampilkan Halaman Return dengan kondisi K11
78. Klik `[Submit]`
79. Verifikasi toast `Connection problem. Please try again.` tampil
80. Verifikasi toast gangguan koneksi pada Return tidak menampilkan tombol aksi `[Try Again]`
81. Verifikasi daftar tetap memuat `Tablet Samsung Galaxy Tab A8` dan `Drone DJI Mini 3` setelah gangguan koneksi
82. Verifikasi tombol `[Submit]` aktif lagi setelah gangguan koneksi
83. Klik `[Submit]`
84. Verifikasi toast `Success, 2 assets have been returned.` tampil
