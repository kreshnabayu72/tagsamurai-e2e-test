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
- Kemampuan teknis tambahan: memilih rentang tanggal pada date range picker Filter Panel; membaca warna icon Filter (terang atau gelap); membaca chip dan state checkbox di dropdown multi-select.
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
9. Verifikasi field `PIC` bertipe multi-select searchable dengan placeholder `All PICs`
10. Verifikasi field `Due Return Date` bertipe date range picker dengan placeholder `Select date`
11. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-GS-USER-723: Opsi dropdown filter diambil dari nilai yang ada di tabel

12. Buka dropdown Name
13. Verifikasi dropdown Name memuat 26 Name seed (`Laptop 1 {runId}-115` sampai `Laptop 8`, `Proyektor 1` sampai `Proyektor 10`, dan `Kamera 1` sampai `Kamera 8`)
14. Verifikasi dropdown Name tidak memuat `Monitor Cadangan {runId}-115` (aset tanpa baris di tabel)
15. Tutup dropdown Name dengan mengklik area kosong pada Filter Panel
16. Buka dropdown Brand
17. Verifikasi dropdown Brand memuat `Lenovo {runId}-115`, `Epson {runId}-115`, dan `Canon {runId}-115`
18. Verifikasi dropdown Brand tidak memuat `Samsung {runId}-115` (brand aset tanpa baris di tabel)
19. Tutup dropdown Brand dengan mengklik area kosong pada Filter Panel
20. Buka dropdown PIC
21. Verifikasi dropdown PIC memuat `Andi Wijaya` dan `Doni Pratama`
22. Verifikasi dropdown PIC tidak memuat `Eko Prasetyo` (user tanpa baris sebagai PIC di tabel)
23. Tutup dropdown PIC dengan mengklik area kosong pada Filter Panel

### TC-GS-USER-724: Filter multi-select per field menyaring baris

24. Buka dropdown Name, pilih opsi `Kamera 1 {runId}-115`
25. Klik `[Apply]`
26. Verifikasi tabel hanya menampilkan satu baris, yaitu baris dengan Name `Kamera 1 {runId}-115`
27. Verifikasi icon Filter berubah gelap saat filter Name aktif
28. Klik icon Filter
29. Klik `[Clear Field]`
30. Klik `[Apply]`
31. Klik icon Filter
32. Buka dropdown Brand, pilih opsi `Canon {runId}-115`
33. Klik `[Apply]`
34. Verifikasi tabel hanya menampilkan 8 baris dengan Brand `Canon {runId}-115` (`Kamera 1` sampai `Kamera 8`)
35. Verifikasi icon Filter berubah gelap saat filter Brand aktif
36. Klik icon Filter
37. Klik `[Clear Field]`
38. Klik `[Apply]`
39. Klik icon Filter
40. Buka dropdown PIC, pilih opsi `Andi Wijaya`
41. Klik `[Apply]`
42. Verifikasi baris `Laptop 1 {runId}-115` dan `Kamera 1 {runId}-115` tampil
43. Verifikasi seluruh baris tabel bernilai PIC `Andi W`
44. Verifikasi icon Filter berubah gelap saat filter PIC aktif
45. Klik icon Filter
46. Klik `[Clear Field]`
47. Klik `[Apply]`

### TC-GS-USER-725: Dua opsi dalam satu field filter digabung OR

48. Klik icon Filter
49. Buka dropdown Name, pilih opsi `Laptop 1 {runId}-115` dan `Proyektor 1 {runId}-115`
50. Klik `[Apply]`
51. Verifikasi baris `Laptop 1 {runId}-115` tampil (Name = opsi 1)
52. Verifikasi baris `Proyektor 1 {runId}-115` tampil (Name = opsi 2)
53. Verifikasi tabel hanya menampilkan kedua baris tersebut
54. Klik icon Filter
55. Klik `[Clear Field]`
56. Klik `[Apply]`

### TC-GS-USER-726: Search di dalam dropdown filter mempersempit opsi

57. Klik icon Filter
58. Buka dropdown Name
59. Ketik `kamera` pada pencarian di dalam dropdown Name
60. Verifikasi opsi `Kamera 1 {runId}-115` tampil (tersaring substring tanpa membedakan huruf besar kecil)
61. Verifikasi opsi `Laptop 1 {runId}-115` tidak tampil
62. Ganti isi pencarian di dalam dropdown dengan `zzz`
63. Verifikasi tidak ada opsi yang cocok

### TC-GS-USER-727: Hapus chip filter lewat (X) meng-uncheck opsi

64. Kosongkan pencarian di dalam dropdown Name
65. Pilih opsi `Laptop 1 {runId}-115` lalu `Proyektor 1 {runId}-115` pada dropdown Name
66. Verifikasi chip `Laptop 1 {runId}-115` dan chip `Proyektor 1 {runId}-115` tampil
67. Klik (X) pada chip pertama, `Laptop 1 {runId}-115`
68. Verifikasi chip `Laptop 1 {runId}-115` hilang
69. Verifikasi chip `Proyektor 1 {runId}-115` tetap tampil
70. Buka dropdown Name
71. Verifikasi checkbox opsi `Laptop 1 {runId}-115` ter-uncheck

### TC-GS-USER-728: Uncheck opsi di dropdown menghapus chip

72. Klik `[Clear Field]`
73. Pilih opsi `Laptop 1 {runId}-115` lalu `Proyektor 1 {runId}-115` pada dropdown Name
74. Verifikasi chip `Laptop 1 {runId}-115` dan chip `Proyektor 1 {runId}-115` tampil
75. Buka dropdown Name, uncheck opsi kedua, `Proyektor 1 {runId}-115`
76. Verifikasi chip `Proyektor 1 {runId}-115` hilang
77. Verifikasi chip `Laptop 1 {runId}-115` tetap tampil

### TC-GS-USER-729: Filter date range per field

78. Klik `[Clear Field]`
79. Pilih rentang tanggal `{tglL}` sampai `{tglL}` pada field Due Return Date
80. Verifikasi input Due Return Date menampilkan rentang `{tglL}` sampai `{tglL}` dalam Date Format General Settings
81. Klik `[Apply]`
82. Verifikasi baris `Laptop 1 {runId}-115` tampil (Due Return Date dalam rentang)
83. Verifikasi seluruh baris tabel bernilai Due Return Date `{tglL}`
84. Klik icon Filter
85. Klik `[Clear Field]`
86. Klik `[Apply]`

### TC-GS-USER-730: Kombinasi dua field filter digabung AND

87. Klik icon Filter
88. Buka dropdown PIC, pilih opsi `Andi Wijaya`
89. Buka dropdown Brand, pilih opsi `Canon {runId}-115`
90. Klik `[Apply]`
91. Verifikasi baris `Kamera 1 {runId}-115` tampil (PIC `Andi W` dan Brand `Canon {runId}-115`)
92. Verifikasi tabel hanya menampilkan 8 baris (`Kamera 1` sampai `Kamera 8`) yang memenuhi kedua kriteria
93. Verifikasi baris `Laptop 1 {runId}-115` (PIC `Andi W`, Brand `Lenovo {runId}-115`) tidak tampil
94. Klik icon Filter
95. Klik `[Clear Field]`
96. Klik `[Apply]`
97. Pilih 10 baris per halaman pada Pagination

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (722 sampai 730) dipertahankan.
- Data target: TC sumber memakai `Ahmad Fauzi`; spec memakai `Joko Susilo` (Tabel Pre-setup No. 19) dengan populasi aset pinjaman milik spec (lebih dari satu halaman), sehingga asersi memakai nilai seed bersuffix.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (mencari user target di User List); langkah 5 (100 baris per halaman supaya seluruh baris seed berada di satu halaman); langkah 15, 19, 23 (menutup dropdown filter); langkah 28, 29, 30, 36, 37, 38, 45, 46, 47, 54, 55, 56, 84, 85, 86, 94, 95, 96 (mengosongkan Filter); langkah 64 (mengosongkan pencarian dropdown); langkah 72, 78 (mengosongkan pilihan Filter Panel sebelum TC berikutnya); langkah 97 (memulihkan page size 10). Pilihan dropdown yang belum di-Apply dibuang saat panel ditutup (prd-conventions §9.8), sehingga kasus tanpa Apply (TC-GS-USER-726, 727, 728) berurutan di panel yang sama dan dibersihkan lewat `[Clear Field]` sebelum TC berikutnya.
- Asersi tambahan (S-03): chip kedua yang tampil sebelum (X) dan uncheck di TC-GS-USER-727 dan 728 (langkah dengan `Verifikasi` chip tampil) adalah anchor positif bagi asersi chip hilang; pada TC-GS-USER-723 asersi ketiadaan opsi didahului `Verifikasi` opsi lain tampil pada dropdown yang sama (bagian 8b butir 2).
- Spec melewati sekitar 35 langkah (97 langkah) karena sembilan TC Filter Panel berbagi satu layar, satu dataset seed, dan satu kelas harness (fungsional, baca saja). Blok TC-GS-USER-724 mengulang pola pilih, Apply, amati, dan Clear untuk tiga field; blok lain berdiri sendiri dan memakai Filter Panel yang sama, sehingga memisahkannya mengulang login, seeding, dan pembukaan sub-tab.
- Pembagian TC lintas spec: TC-GS-USER-387, 388, 716 sampai 721 (screening dan Search) ada di spec 114; TC-GS-USER-731 sampai 735 (kombinasi Search dan Filter, filter kolom hidden) ada di spec 116; TC-GS-USER-736, 737, 738, 753, 754 ada di spec 117; TC-GS-USER-739 sampai 747 ada di spec 118; TC-GS-USER-389 dan 748 sampai 752 ada di spec 119.
- Temuan untuk QA:
  - TC-GS-USER-723: format teks opsi PIC (nama lengkap atau `[First Name] [Last Initial]`) tidak disebut TC; spec mengasersi opsi menurut nama lengkap `Andi Wijaya` dan `Doni Pratama`. Nilai yang "tanpa baris" untuk PIC dipenuhi user Pre-setup `Eko Prasetyo` dengan asumsi ia bukan PIC di baris `B0`; untuk Name dan Brand dipenuhi aset tidak dipinjam yang di-seed.
  - TC-GS-USER-724: "icon Filter berubah gelap saat aktif" bertentangan dengan prd-conventions §9.8 (gelap saat panel aktif atau terbuka); spec mengasersi icon gelap sesudah `[Apply]` mengikuti TC.
  - TC-GS-USER-724 sampai 727: TC tidak menyebut opsi yang dipilih; spec memakai nilai seed yang menghasilkan jumlah baris tertentu (satu baris untuk Name, delapan baris untuk Brand).
  - TC-GS-USER-729: TC tidak menyebut rentang tanggal dan format teksnya; spec memakai tanggal Due Return Date grup Laptop dalam Date Format General Settings client.
  - TC-GS-USER-730: "2 field berbeda" tidak menyebut kolomnya; spec memakai PIC dan Brand.
  - Mekanisme menandai Guided Tooltip sebagai sudah dilihat dan seeding FAMS tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
