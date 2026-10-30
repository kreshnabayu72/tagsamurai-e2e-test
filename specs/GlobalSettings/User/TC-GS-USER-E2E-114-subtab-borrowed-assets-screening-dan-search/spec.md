---
id: TC-GS-USER-E2E-114-subtab-borrowed-assets-screening-dan-search
title: "Sub-tab Borrowed Assets: screening, state kosong, dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-387
  - TC-GS-USER-388
  - TC-GS-USER-716
  - TC-GS-USER-717
  - TC-GS-USER-718
  - TC-GS-USER-719
  - TC-GS-USER-720
  - TC-GS-USER-721
coverage:
  web: automated
---

# Sub-tab Borrowed Assets: screening, state kosong, dan Search

## Prerequisites

- Mode: FE+BE. Spec hanya membaca data user; tidak ada data user yang diubah.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun: Total Control, Siti Nurhaliza, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > User List dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): `Joko Susilo` (No. 19; Access Fixed Asset + Supply Asset) sebagai pemilik tabel Borrowed Assets; `Dewi Lestari` (No. 12; Access Fixed Asset + Global Settings) untuk empty state TC-GS-USER-388; `Andi Wijaya` dan `Doni Pratama` (No. 10 dan 11) sebagai PIC seed. Client FAMS aktif. `Joko Susilo` (Tabel Pre-setup No. 19) sudah punya borrowed asset Pre-setup (`B0` baris, nilainya tidak disebut TC). Baris itu tidak diubah dan ikut tampil di tabel. Asersi memakai nilai bersuffix `{runId}-114` (Name, Brand, Model / Type) sehingga tidak bentrok dengan `B0`; jumlah baris tabel = `B0` + baris seed.
- Prasyarat TC-GS-USER-388 (disediakan tim FE/BE bila belum ada): `Dewi Lestari` tanpa borrowed asset, tetapi sedikitnya satu sub-tab Responsibilities lain berisi data, supaya switcher sub-tab tampil dan tidak digantikan empty state global (NC-12). Spec tidak men-seed data untuk `Dewi Lestari`.
- Data Dinamis (seeding FAMS atas `Joko Susilo`, 26 baris aset pinjaman; seluruhnya tanpa foto sehingga kolom Photo menampilkan `—`):
  - Grup L (8 baris): Name `Laptop 1 {runId}-114` sampai `Laptop 8 {runId}-114`; Brand `Lenovo {runId}-114`; Model / Type `ThinkPad {runId}-114`; PIC `Andi Wijaya` (tampil `Andi W`); Due Return Date = hari uji + 10 hari (`{tglL}`).
  - Grup P (10 baris): Name `Proyektor 1 {runId}-114` sampai `Proyektor 10 {runId}-114`; Brand `Epson {runId}-114`; Model / Type `EB-X06 {runId}-114`; PIC `Doni Pratama` (tampil `Doni P`); Due Return Date = hari uji + 20 hari (`{tglP}`).
  - Grup K (8 baris): Name `Kamera 1 {runId}-114` sampai `Kamera 8 {runId}-114`; Brand `Canon {runId}-114`; Model / Type `EOS-R10 {runId}-114`; PIC `Andi Wijaya` (tampil `Andi W`); Due Return Date = hari uji + 30 hari (`{tglK}`).
  - Seluruh nilai Name, Brand, dan Model / Type unik per spec dan per run; setiap kolom yang diuji punya sedikitnya dua nilai distinct (Brand dan Model / Type tiga nilai, PIC dua nilai, Due Return Date tiga nilai) (S-11). `{tglL}`, `{tglP}`, `{tglK}` adalah tanggal Due Return Date grup tersebut dalam Date Format General Settings client, dihitung di hook `before` dari hasil seeding. PIC memakai user Pre-setup `Andi Wijaya` dan `Doni Pratama` yang hanya dibaca.
- Data uji per TC: TC-GS-USER-716 keyword `Proyektor`; TC-GS-USER-717 keyword `  LAPTOP  `; TC-GS-USER-718 keyword `{trxL1}` (Transaction ID penuh baris `Laptop 1`, dibaca dari tabel), `Kamera 3`, `{aidL1}` (Asset ID penuh baris `Laptop 1`), `Canon`, `EB-X06`, `Wijaya`; TC-GS-USER-719 keyword `—` (nilai kolom Photo tanpa foto) dan `{tglL}`; TC-GS-USER-720 kolom `PIC` di-hide lalu di-unhide dengan keyword `Wijaya`; TC-GS-USER-721 keyword `zzzqqq`.
- Kemampuan teknis (HK8, disediakan tim FE/BE; endpoint tidak disebut di TC, PRD, atau LLD): seeding FAMS yang membuat aset beserta transaksi peminjaman atas `Joko Susilo` dengan Name, Brand, Model / Type, PIC, dan Due Return Date yang ditentukan; membaca Transaction ID dan Asset ID hasil seeding; membaca jumlah borrowed asset Pre-setup `Joko Susilo` sebelum seeding (disebut `B0` di bawah); menghapus atau mengembalikan aset dan transaksi seed di hook `after`.
- Kemampuan teknis tambahan: menyetel page size Pagination sub-tab; mengetik dan mengosongkan Search; mengamati fokus kursor pada input Search.
- State yang diubah dan dipulihkan: Search dikosongkan dan ditutup, kolom `PIC` ditampilkan kembali, page size dikembalikan ke 10 di akhir spec; preferensi kolom tabel Borrowed Assets dikembalikan ke default (semua kolom tampil, urutan default) di hook `after` sebagai cadangan. Aset dan transaksi seed dibersihkan di hook `after` tanpa mengandalkan seeding berhasil penuh.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-387: Screening sub-tab Borrowed Assets

1. Klik icon Search di User List, ketik `Joko Susilo`, tekan Enter
2. Klik Name `Joko Susilo` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Borrowed Assets`
5. Verifikasi toolbar menampilkan `Search`, `Filter`, dan `Download`
6. Verifikasi header kolom berurutan `Photo`, `Transaction ID`, `Name`, `Asset ID`, `Brand`, `Model / Type`, `Due Return Date`, `PIC`, dan Column Visibility (⋯)
7. Verifikasi header `Photo` tanpa ikon sort (unsortable)
8. Verifikasi header `Transaction ID`, `Name`, `Asset ID`, `Brand`, `Model / Type`, `Due Return Date`, dan `PIC` memiliki ikon sort (sortable)
9. Verifikasi tabel terurut menurut `Due Return Date` ascending sebagai default (nilai Due Return Date baris tidak menurun)
10. Verifikasi baris tabel tidak memiliki row action
11. Verifikasi kolom Actions hanya berisi pemicu Column Visibility (⋯)
12. Verifikasi kontrol pagination tampil karena tabel memuat lebih dari 10 baris
13. Klik icon Search, ketik `Laptop 1 {runId}-114`, tekan Enter
14. Verifikasi tabel hanya menampilkan satu baris dengan Name `Laptop 1 {runId}-114`
15. Verifikasi Transaction ID baris tersebut berformat `BRW-YYYYMMDD-XXXX`
16. Verifikasi Asset ID baris tersebut terisi dengan Asset ID aset seed `Laptop 1 {runId}-114`
17. Verifikasi kontrol pagination tidak tampil (satu baris, tidak lebih dari 10 baris)
18. Klik icon panah `(←)` untuk menutup Search dan mereset tabel
19. Pilih 100 baris per halaman pada Pagination

### TC-GS-USER-716: Siklus Search: reveal, Enter, clear (✕), dan collapse (←)

20. Klik icon Search
21. Verifikasi Search bar melebar
22. Verifikasi kursor auto-focus di input Search
23. Ketik `Proyektor` pada kotak Search
24. Verifikasi icon `(✕)` muncul di dalam input
25. Verifikasi tabel belum tersaring: baris `Kamera 1 {runId}-114` tetap tampil
26. Tekan Enter
27. Verifikasi baris `Proyektor 1 {runId}-114` tampil (tabel tersaring)
28. Verifikasi baris `Kamera 1 {runId}-114` tidak tampil
29. Klik icon `(✕)`
30. Verifikasi input Search kosong
31. Verifikasi tabel tetap menampilkan hasil search terakhir: baris `Proyektor 1 {runId}-114` tampil
32. Verifikasi tabel tetap menampilkan hasil search terakhir: baris `Kamera 1 {runId}-114` tidak tampil
33. Tekan Enter pada input kosong
34. Verifikasi tabel kembali menampilkan semua data: baris `Kamera 1 {runId}-114` tampil kembali
35. Isi Search dengan `Proyektor`, tekan Enter
36. Klik icon panah `(←)`
37. Verifikasi Search collapse menjadi icon Search biasa
38. Verifikasi tabel langsung reset tanpa menekan Enter: baris `Kamera 1 {runId}-114` tampil
39. Klik icon Search
40. Verifikasi input Search kosong (keyword dikosongkan)

### TC-GS-USER-717: Query Search di-trim dan tidak case-sensitive

41. Isi Search dengan `  LAPTOP  ` (dua spasi di awal dan di akhir), tekan Enter
42. Verifikasi baris `Laptop 1 {runId}-114` tampil (spasi diabaikan, huruf besar kecil tidak dibedakan)
43. Verifikasi isi kotak Search tetap menampilkan `  LAPTOP  ` apa adanya

### TC-GS-USER-718: Search menemukan substring pada kolom kelas teks

44. Baca Transaction ID (`{trxL1}`) dan Asset ID (`{aidL1}`) baris `Laptop 1 {runId}-114`
45. Ganti isi kotak search dengan `{trxL1}`, tekan Enter
46. Verifikasi baris `Laptop 1 {runId}-114` dengan Transaction ID `{trxL1}` tampil (kolom Transaction ID)
47. Ganti isi kotak search dengan `Kamera 3`, tekan Enter
48. Verifikasi baris `Kamera 3 {runId}-114` tampil (kolom Name)
49. Ganti isi kotak search dengan `{aidL1}`, tekan Enter
50. Verifikasi baris `Laptop 1 {runId}-114` dengan Asset ID `{aidL1}` tampil (kolom Asset ID)
51. Ganti isi kotak search dengan `Canon`, tekan Enter
52. Verifikasi baris `Kamera 1 {runId}-114` dengan Brand `Canon {runId}-114` tampil (kolom Brand)
53. Ganti isi kotak search dengan `EB-X06`, tekan Enter
54. Verifikasi baris `Proyektor 1 {runId}-114` dengan Model / Type `EB-X06 {runId}-114` tampil (kolom Model / Type)
55. Ganti isi kotak search dengan `Wijaya`, tekan Enter
56. Verifikasi baris `Laptop 1 {runId}-114` dengan PIC `Andi W` tampil (kolom PIC, dicocokkan dengan nama lengkap `Andi Wijaya`)
57. Klik icon `(✕)`, tekan Enter pada input kosong

### TC-GS-USER-719: Kolom non-searchable tidak tercakup Search

58. Verifikasi sel Photo baris `Laptop 1 {runId}-114` menampilkan `—`
59. Baca teks Due Return Date baris `Laptop 1 {runId}-114` (`{tglL}`)
60. Isi Search dengan `—`, tekan Enter
61. Verifikasi tabel menampilkan no result state `No results found` (kolom Photo tidak tercakup Search)
62. Ganti isi kotak search dengan `{tglL}`, tekan Enter
63. Verifikasi tabel menampilkan no result state `No results found` (kolom Due Return Date tidak tercakup Search)

### TC-GS-USER-720: Search tidak mencocokkan kolom yang di-hide dan kembali cocok setelah unhide

64. Klik icon `(✕)`, tekan Enter pada input kosong
65. Verifikasi baris `Laptop 1 {runId}-114` tampil sebelum kolom PIC di-hide
66. Klik header kolom Column Visibility (⋯)
67. Hilangkan centang kolom `PIC` pada Overlay Column Visibility
68. Isi Search dengan `Wijaya`, tekan Enter
69. Verifikasi tabel menampilkan no result state `No results found` saat kolom PIC hidden
70. Klik header kolom Column Visibility (⋯)
71. Centang kembali kolom `PIC` pada Overlay Column Visibility
72. Tekan Enter pada input Search
73. Verifikasi baris `Laptop 1 {runId}-114` kembali cocok dan tampil setelah kolom PIC di-unhide

### TC-GS-USER-721: Empty filtered state

74. Ganti isi kotak search dengan `zzzqqq`, tekan Enter
75. Verifikasi ilustrasi empty filtered state tampil
76. Verifikasi teks `No results found` tampil
77. Verifikasi teks `Try adjusting your search or filter.` tampil
78. Klik icon panah `(←)` untuk menutup Search dan mereset tabel
79. Pilih 10 baris per halaman pada Pagination

### TC-GS-USER-388: Empty state sub-tab Borrowed Assets

80. Klik menu `User` pada Global Settings untuk kembali ke User List
81. Klik icon Search di User List, ketik `Dewi Lestari`, tekan Enter
82. Klik Name `Dewi Lestari` di User List
83. Klik Tab `Responsibilities`
84. Klik sub-tab `Borrowed Assets`
85. Verifikasi ilustrasi empty state tampil
86. Verifikasi teks `No borrowed assets` tampil
87. Verifikasi teks `This user has no borrowed assets currently.` tampil

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Data target: TC sumber memakai `Ahmad Fauzi` (TC-GS-USER-387 dan 716 sampai 721); spec memakai `Joko Susilo` (Tabel Pre-setup No. 19) dengan populasi aset pinjaman milik spec (lebih dari satu halaman), sehingga asersi memakai nilai seed bersuffix. TC-GS-USER-388 memakai `Dewi Lestari` seperti di TC.
- Urutan TC: 387, 716, 717, 718, 719, 720, 721, lalu 388 di akhir. TC-GS-USER-388 memakai user lain, sehingga ditaruh terakhir agar blok Search tidak terputus perpindahan user. Urutan di `tc-user.md` adalah 387, 388, 716 sampai 721. Expected c dan e TC-GS-USER-387 (baris contoh dan pagination tidak tampil untuk 10 baris atau kurang) diasersi pada tabel yang dipersempit Search menjadi satu baris (langkah 13), setelah langkah 12 membuktikan kontrol pagination tampil pada tabel penuh.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 81 (mencari user target di User List); langkah 13 (mempersempit tabel menjadi satu baris untuk Expected c dan e); langkah 18, 78 (menutup Search); langkah 19 (100 baris per halaman supaya seluruh baris seed berada di satu halaman); langkah 44 (membaca nilai untuk keyword Transaction ID dan Asset ID); langkah 57 (mengosongkan Search seusai tiap kasus kolom); langkah 59 (membaca nilai Due Return Date untuk keyword); langkah 64 (mengosongkan Search); langkah 79 (memulihkan page size 10); langkah 80 (kembali ke User List).
- Asersi tambahan (S-03): langkah 12 (kontrol pagination tampil pada tabel penuh) dan langkah 58 (nilai kolom Photo `—` pada baris seed) adalah anchor positif bagi asersi absence di langkah sesudahnya (bagian 8b butir 2, S-14). Langkah pertama TC-GS-USER-720 memverifikasi baris `Laptop 1 {runId}-114` tampil sebelum kolom PIC di-hide, sebagai anchor bagi asersi no result.
- Search memakai "Klik icon Search, ketik ..." saat kotak belum terbuka, "Isi Search dengan" saat kotak terbuka dan kosong, dan "ganti isi kotak search dengan" saat kotak berisi (bagian 8b butir 9). Hasil Search pada TC-GS-USER-718 diasersi lewat baris seed yang nilainya unik; PIC dicari lewat `Wijaya` karena Search mencocokkan nama lengkap PIC, bukan teks tampil `Andi W` (PRD user.md §4.1.3).
- Spec melewati sekitar 35 langkah (87 langkah) karena tujuh TC Search dan screening berbagi satu layar (sub-tab Borrowed Assets `Joko Susilo`), satu dataset seed, dan satu kelas harness (fungsional, baca saja). Blok saling melanjutkan state Search bar yang terbuka dan tabel penuh; memisahkannya mengulang login, seeding, dan pembukaan sub-tab yang sama. TC-GS-USER-388 berdiri sendiri di akhir.
- Pembagian TC lintas spec: TC-GS-USER-722 sampai 730 (Filter Panel) ada di spec 115; TC-GS-USER-731 sampai 735 (kombinasi Search dan Filter) ada di spec 116; TC-GS-USER-736, 737, 738, 753, 754 (Sort, Pagination, kombinasi) ada di spec 117; TC-GS-USER-739 sampai 747 (Setup Column) ada di spec 118; TC-GS-USER-389 dan 748 sampai 752 (Download) ada di spec 119.
- Temuan untuk QA:
  - TC-GS-USER-387 Expected b: urutan kolom `Photo | Transaction ID | Name | Asset ID | ...` berbeda dari TC-GS-USER-739 dan PRD user.md §4.1.3 (`Photo | Name | Asset ID | Transaction ID | ...`). Spec ini mengikuti TC-GS-USER-387; spec 118 mengikuti TC-GS-USER-739.
  - TC-GS-USER-387 Expected c: nilai contoh (`BRW-20260610-0001`, `"Laptop - 1"`, `AST-00123`) berasal dari data contoh `Ahmad Fauzi` di PRD; spec mengasersi Name seed unik (tanpa suffix urutan senama), pola Transaction ID `BRW-YYYYMMDD-XXXX` (PRD §4.1.3), dan Asset ID terisi.
  - TC-GS-USER-387 Expected e: "≤10 baris" tidak terpenuhi oleh populasi seed lebih dari satu halaman; diasersi pada tabel hasil Search satu baris.
  - TC-GS-USER-388: precondition tidak menyebut data sub-tab lain; bila semua sub-tab Responsibilities `Dewi Lestari` kosong, empty state global menggantikan switcher (NC-12) dan sub-tab Borrowed Assets tidak dapat dibuka.
  - TC-GS-USER-718: "potongan nilai kolom" Transaction ID dan Asset ID dipenuhi dengan nilai penuh karena potongan pendek (`BRW-`) mencocokkan semua baris; Transaction ID dan Asset ID dibaca dari tabel.
  - TC-GS-USER-719: Photo berisi thumbnail atau `—`, TC tidak menyebut nilai yang diketik; spec memakai `—` dari baris tanpa foto (PRD §4.1.3, Nilai Kosong). TC juga tidak menyebut format teks tanggal Due Return Date; spec memakai teks sel sesuai Date Format General Settings.
  - TC-GS-USER-716 Expected b: "tabel belum tersaring" tidak menyebut baris yang diamati; spec mengamati baris grup Kamera tetap tampil saat keyword `Proyektor` baru diketik.
  - Mekanisme menandai Guided Tooltip sebagai sudah dilihat dan seeding FAMS tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
