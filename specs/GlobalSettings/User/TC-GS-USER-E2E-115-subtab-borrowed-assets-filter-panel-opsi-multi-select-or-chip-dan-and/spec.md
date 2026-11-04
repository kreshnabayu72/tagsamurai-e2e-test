---
id: TC-GS-USER-E2E-115-subtab-borrowed-assets-filter-panel-opsi-multi-select-or-chip-dan-and
title: "Sub-tab Borrowed Assets: Filter Panel (opsi, multi-select, OR, dropdown search, chip, rentang, AND)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-722
  - TC-GS-USER-723
  - TC-GS-USER-724
  - TC-GS-USER-725
  - TC-GS-USER-726
  - TC-GS-USER-727
  - TC-GS-USER-728
  - TC-GS-USER-729
  - TC-GS-USER-730
coverage:
  web: automated
---

# Sub-tab Borrowed Assets: Filter Panel (opsi, multi-select, OR, dropdown search, chip, rentang, AND)

## Prerequisites

- Mode: FE+BE. Spec hanya membaca data user; tidak ada data user yang diubah.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun: Total Control, Siti Nurhaliza, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > User List dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): `Joko Susilo` (No. 19; Access Fixed Asset + Supply Asset) sebagai pemilik tabel Borrowed Assets; `Andi Wijaya`, `Doni Pratama` (No. 10 dan 11) sebagai PIC seed; `Eko Prasetyo` (Tabel Pre-setup No. 8) sebagai user yang tidak menjadi PIC baris mana pun (dipakai asersi opsi PIC). Client FAMS aktif. `Joko Susilo` (Tabel Pre-setup No. 19) sudah punya borrowed asset Pre-setup (`B0` baris, nilainya tidak disebut TC). Baris itu tidak diubah dan ikut tampil di tabel. Asersi memakai nilai bersuffix `{runId}-115` (Name, Brand, Model / Type) sehingga tidak bentrok dengan `B0`; jumlah baris tabel = `B0` + baris seed.
- Data Dinamis (seeding FAMS atas `Joko Susilo`, 26 baris aset pinjaman; seluruhnya tanpa foto sehingga kolom Photo menampilkan `—`):
  - Grup L (8 baris): Name `Laptop 1 {runId}-115` sampai `Laptop 8 {runId}-115`; Brand `Lenovo {runId}-115`; Model / Type `ThinkPad {runId}-115`; PIC `Andi Wijaya` (tampil `Andi W`); Due Return Date = hari uji + 10 hari (`{tglL}`).
  - Grup P (10 baris): Name `Proyektor 1 {runId}-115` sampai `Proyektor 10 {runId}-115`; Brand `Epson {runId}-115`; Model / Type `EB-X06 {runId}-115`; PIC `Doni Pratama` (tampil `Doni P`); Due Return Date = hari uji + 20 hari (`{tglP}`).
  - Grup K (8 baris): Name `Kamera 1 {runId}-115` sampai `Kamera 8 {runId}-115`; Brand `Canon {runId}-115`; Model / Type `EOS-R10 {runId}-115`; PIC `Andi Wijaya` (tampil `Andi W`); Due Return Date = hari uji + 30 hari (`{tglK}`).
  - Seluruh nilai Name, Brand, dan Model / Type unik per spec dan per run; setiap kolom yang diuji punya sedikitnya dua nilai distinct (Brand dan Model / Type tiga nilai, PIC dua nilai, Due Return Date tiga nilai) (S-11). `{tglL}`, `{tglP}`, `{tglK}` adalah tanggal Due Return Date grup tersebut dalam Date Format General Settings client, dihitung di hook `before` dari hasil seeding. PIC memakai user Pre-setup `Andi Wijaya` dan `Doni Pratama` yang hanya dibaca.
  - Aset pembanding opsi dropdown (TC-GS-USER-723): satu aset `Monitor Cadangan {runId}-115` dengan Brand `Samsung {runId}-115` yang terdaftar di FAMS tetapi tidak dipinjam `Joko Susilo` (tanpa transaksi peminjaman), sehingga nilainya tidak punya baris di tabel.
- Data uji per TC: TC-GS-USER-724 opsi `Kamera 1 {runId}-115` (Name), `Canon {runId}-115` (Brand), `Andi Wijaya` (PIC); TC-GS-USER-725 opsi `Laptop 1` dan `Proyektor 1`; TC-GS-USER-726 kata `kamera` dan `zzz`; TC-GS-USER-727 dan 728 opsi `Laptop 1` dan `Proyektor 1` (urutan pilih menentukan chip pertama dan kedua); TC-GS-USER-729 rentang `{tglL}` sampai `{tglL}`; TC-GS-USER-730 PIC `Andi Wijaya` dan Brand `Canon {runId}-115`.
- Kemampuan teknis (HK8, disediakan tim FE/BE; endpoint tidak disebut di TC, PRD, atau LLD): seeding FAMS yang membuat aset beserta transaksi peminjaman atas `Joko Susilo` dengan Name, Brand, Model / Type, PIC, dan Due Return Date yang ditentukan; membaca Transaction ID dan Asset ID hasil seeding; membaca jumlah borrowed asset Pre-setup `Joko Susilo` sebelum seeding (disebut `B0` di bawah); menghapus atau mengembalikan aset dan transaksi seed di hook `after`.
- Kemampuan teknis tambahan: memilih rentang tanggal pada date range picker Filter Panel; membaca warna icon Filter (terang atau gelap) dan badge titik pada icon Filter; membaca chip dan state checkbox di dropdown multi-select.
- State yang diubah dan dipulihkan: Filter dikosongkan (`[Clear Field]` lalu `[Apply]`) dan page size dikembalikan ke 10 di akhir spec; hook `after` sebagai cadangan. Aset dan transaksi seed dibersihkan di hook `after` tanpa mengandalkan seeding berhasil penuh.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-722: Screening Filter Panel

1. Klik icon Search di User List, ketik `Joko Susilo`, tekan Enter
2. Klik Name `Joko Susilo` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Borrowed Assets`
5. Pilih 100 baris per halaman pada Pagination
6. Klik icon Filter
7. Verifikasi field `Name` bertipe multi-select searchable dengan placeholder `All assets`
8. Verifikasi field `Brand` bertipe multi-select searchable dengan placeholder `All brands`
9. Verifikasi field `Model / Type` bertipe multi-select searchable dengan placeholder `All models/types`
10. Verifikasi field `PIC` bertipe multi-select searchable dengan placeholder `All PICs`
11. Verifikasi field `Due Return Date` bertipe date range picker dengan placeholder `Select date`
12. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-GS-USER-723: Opsi dropdown filter diambil dari nilai yang ada di tabel

13. Buka dropdown Name
14. Verifikasi dropdown Name memuat 26 Name seed (`Laptop 1 {runId}-115` sampai `Laptop 8`, `Proyektor 1` sampai `Proyektor 10`, dan `Kamera 1` sampai `Kamera 8`)
15. Verifikasi dropdown Name tidak memuat `Monitor Cadangan {runId}-115` (aset tanpa baris di tabel)
16. Tutup dropdown Name dengan mengklik area kosong pada Filter Panel
17. Buka dropdown Brand
18. Verifikasi dropdown Brand memuat `Lenovo {runId}-115`, `Epson {runId}-115`, dan `Canon {runId}-115`
19. Verifikasi dropdown Brand tidak memuat `Samsung {runId}-115` (brand aset tanpa baris di tabel)
20. Tutup dropdown Brand dengan mengklik area kosong pada Filter Panel
21. Buka dropdown PIC
22. Verifikasi dropdown PIC memuat `Andi Wijaya` dan `Doni Pratama`
23. Verifikasi dropdown PIC tidak memuat `Eko Prasetyo` (user tanpa baris sebagai PIC di tabel)
24. Tutup dropdown PIC dengan mengklik area kosong pada Filter Panel

### TC-GS-USER-724: Filter multi-select per field menyaring baris

25. Buka dropdown Name, pilih opsi `Kamera 1 {runId}-115`
26. Klik `[Apply]`
27. Verifikasi tabel hanya menampilkan satu baris, yaitu baris dengan Name `Kamera 1 {runId}-115`
28. Verifikasi badge titik tampil pada icon Filter
29. Klik icon Filter
30. Verifikasi icon Filter gelap (panel terbuka)
31. Klik `[Clear Field]`
32. Klik `[Apply]`
33. Klik icon Filter
34. Buka dropdown Brand, pilih opsi `Canon {runId}-115`
35. Klik `[Apply]`
36. Verifikasi tabel hanya menampilkan 8 baris dengan Brand `Canon {runId}-115` (`Kamera 1` sampai `Kamera 8`)
37. Verifikasi badge titik tampil pada icon Filter
38. Klik icon Filter
39. Verifikasi icon Filter gelap (panel terbuka)
40. Klik `[Clear Field]`
41. Klik `[Apply]`
42. Klik icon Filter
43. Buka dropdown PIC, pilih opsi `Andi Wijaya`
44. Klik `[Apply]`
45. Verifikasi baris `Laptop 1 {runId}-115` dan `Kamera 1 {runId}-115` tampil
46. Verifikasi seluruh baris tabel bernilai PIC `Andi W`
47. Verifikasi badge titik tampil pada icon Filter
48. Klik icon Filter
49. Verifikasi icon Filter gelap (panel terbuka)
50. Klik `[Clear Field]`
51. Klik `[Apply]`

### TC-GS-USER-725: Dua opsi dalam satu field filter digabung OR

52. Klik icon Filter
53. Buka dropdown Name, pilih opsi `Laptop 1 {runId}-115` dan `Proyektor 1 {runId}-115`
54. Klik `[Apply]`
55. Verifikasi baris `Laptop 1 {runId}-115` tampil (Name = opsi 1)
56. Verifikasi baris `Proyektor 1 {runId}-115` tampil (Name = opsi 2)
57. Verifikasi tabel hanya menampilkan kedua baris tersebut
58. Klik icon Filter
59. Klik `[Clear Field]`
60. Klik `[Apply]`

### TC-GS-USER-726: Search di dalam dropdown filter mempersempit opsi

61. Klik icon Filter
62. Buka dropdown Name
63. Ketik `kamera` pada pencarian di dalam dropdown Name
64. Verifikasi opsi `Kamera 1 {runId}-115` tampil (tersaring substring tanpa membedakan huruf besar kecil)
65. Verifikasi opsi `Laptop 1 {runId}-115` tidak tampil
66. Ganti isi pencarian di dalam dropdown dengan `zzz`
67. Verifikasi tidak ada opsi yang cocok

### TC-GS-USER-727: Hapus chip filter lewat (X) meng-uncheck opsi

68. Kosongkan pencarian di dalam dropdown Name
69. Pilih opsi `Laptop 1 {runId}-115` lalu `Proyektor 1 {runId}-115` pada dropdown Name
70. Verifikasi chip `Laptop 1 {runId}-115` dan chip `Proyektor 1 {runId}-115` tampil
71. Klik (X) pada chip pertama, `Laptop 1 {runId}-115`
72. Verifikasi chip `Laptop 1 {runId}-115` hilang
73. Verifikasi chip `Proyektor 1 {runId}-115` tetap tampil
74. Buka dropdown Name
75. Verifikasi checkbox opsi `Laptop 1 {runId}-115` ter-uncheck

### TC-GS-USER-728: Uncheck opsi di dropdown menghapus chip

76. Klik `[Clear Field]`
77. Pilih opsi `Laptop 1 {runId}-115` lalu `Proyektor 1 {runId}-115` pada dropdown Name
78. Verifikasi chip `Laptop 1 {runId}-115` dan chip `Proyektor 1 {runId}-115` tampil
79. Buka dropdown Name, uncheck opsi kedua, `Proyektor 1 {runId}-115`
80. Verifikasi chip `Proyektor 1 {runId}-115` hilang
81. Verifikasi chip `Laptop 1 {runId}-115` tetap tampil

### TC-GS-USER-729: Filter date range per field

82. Klik `[Clear Field]`
83. Pilih rentang tanggal `{tglL}` sampai `{tglL}` pada field Due Return Date
84. Verifikasi input Due Return Date menampilkan rentang `{tglL}` sampai `{tglL}` dalam Date Format General Settings
85. Klik `[Apply]`
86. Verifikasi baris `Laptop 1 {runId}-115` tampil (Due Return Date dalam rentang)
87. Verifikasi seluruh baris tabel bernilai Due Return Date `{tglL}`
88. Klik icon Filter
89. Klik `[Clear Field]`
90. Klik `[Apply]`

### TC-GS-USER-730: Kombinasi dua field filter digabung AND

91. Klik icon Filter
92. Buka dropdown PIC, pilih opsi `Andi Wijaya`
93. Buka dropdown Brand, pilih opsi `Canon {runId}-115`
94. Klik `[Apply]`
95. Verifikasi baris `Kamera 1 {runId}-115` tampil (PIC `Andi W` dan Brand `Canon {runId}-115`)
96. Verifikasi tabel hanya menampilkan 8 baris (`Kamera 1` sampai `Kamera 8`) yang memenuhi kedua kriteria
97. Verifikasi baris `Laptop 1 {runId}-115` (PIC `Andi W`, Brand `Lenovo {runId}-115`) tidak tampil
98. Klik icon Filter
99. Klik `[Clear Field]`
100. Klik `[Apply]`
101. Pilih 10 baris per halaman pada Pagination

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (722 sampai 730) dipertahankan.
- Data target: TC sumber memakai `Ahmad Fauzi`; spec memakai `Joko Susilo` (Tabel Pre-setup No. 19) dengan populasi aset pinjaman milik spec (lebih dari satu halaman), sehingga asersi memakai nilai seed bersuffix.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (mencari user target di User List); langkah 5 (100 baris per halaman supaya seluruh baris seed berada di satu halaman); langkah 16, 20, 24 (menutup dropdown filter); langkah 29, 31, 32, 38, 40, 41, 48, 50, 51, 58, 59, 60, 88, 89, 90, 98, 99, 100 (membuka dan mengosongkan Filter); langkah 68 (mengosongkan pencarian dropdown); langkah 76, 82 (mengosongkan pilihan Filter Panel sebelum TC berikutnya); langkah 101 (memulihkan page size 10). Pilihan dropdown yang belum di-Apply dibuang saat panel ditutup (prd-conventions §9.8), sehingga kasus tanpa Apply (TC-GS-USER-726, 727, 728) berurutan di panel yang sama dan dibersihkan lewat `[Clear Field]` sebelum TC berikutnya.
- Asersi tambahan (S-03): chip kedua yang tampil sebelum (X) dan uncheck di TC-GS-USER-727 dan 728 (langkah dengan `Verifikasi` chip tampil) adalah anchor positif bagi asersi chip hilang; pada TC-GS-USER-723 asersi ketiadaan opsi didahului `Verifikasi` opsi lain tampil pada dropdown yang sama (bagian 8b butir 2).
- Spec melewati sekitar 35 langkah (101 langkah) karena sembilan TC Filter Panel berbagi satu layar, satu dataset seed, dan satu kelas harness (fungsional, baca saja). Blok TC-GS-USER-724 mengulang pola pilih, Apply, amati, dan Clear untuk tiga field; blok lain berdiri sendiri dan memakai Filter Panel yang sama, sehingga memisahkannya mengulang login, seeding, dan pembukaan sub-tab.
- Pembagian TC lintas spec: TC-GS-USER-387, 388, 716 sampai 721 (screening dan Search) ada di spec 114; TC-GS-USER-731 sampai 735 (kombinasi Search dan Filter, filter kolom hidden) ada di spec 116; TC-GS-USER-736, 737, 738, 753, 754 ada di spec 117; TC-GS-USER-739 sampai 747 ada di spec 118; TC-GS-USER-389 dan 748 sampai 752 ada di spec 119.
- Temuan untuk QA:
  - TC-GS-USER-723: format teks opsi PIC (nama lengkap atau `[First Name] [Last Initial]`) tidak disebut TC; spec mengasersi opsi menurut nama lengkap `Andi Wijaya` dan `Doni Pratama`. Nilai yang "tanpa baris" untuk PIC dipenuhi user Pre-setup `Eko Prasetyo` dengan asumsi ia bukan PIC di baris `B0`; untuk Name dan Brand dipenuhi aset tidak dipinjam yang di-seed.
  - TC-GS-USER-724 sampai 727: TC tidak menyebut opsi yang dipilih; spec memakai nilai seed yang menghasilkan jumlah baris tertentu (satu baris untuk Name, delapan baris untuk Brand).
  - TC-GS-USER-729: TC tidak menyebut rentang tanggal dan format teksnya; spec memakai tanggal Due Return Date grup Laptop dalam Date Format General Settings client.
  - TC-GS-USER-730: "2 field berbeda" tidak menyebut kolomnya; spec memakai PIC dan Brand.
  - Mekanisme menandai Guided Tooltip sebagai sudah dilihat dan seeding FAMS tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
