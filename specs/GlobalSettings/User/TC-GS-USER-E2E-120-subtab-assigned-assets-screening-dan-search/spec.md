---
id: TC-GS-USER-E2E-120-subtab-assigned-assets-screening-dan-search
title: "Sub-tab Assigned Assets: Screening, Empty State, dan Search (Reveal, Clear, Trim, Kolom Searchable, dan Kolom Hidden)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-390
  - TC-GS-USER-391
  - TC-GS-USER-755
  - TC-GS-USER-756
  - TC-GS-USER-757
  - TC-GS-USER-758
  - TC-GS-USER-759
  - TC-GS-USER-760
coverage:
  web: automated
---

# Sub-tab Assigned Assets: Screening, Empty State, dan Search (Reveal, Clear, Trim, Kolom Searchable, dan Kolom Hidden)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup user; hanya dataset Assigned Assets milik spec yang ditambahkan lalu dibersihkan.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`.
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22 dan No. 30, hanya dibaca): Ahmad Fauzi (No. 13; Assigned Assets berisi K1) dan Rina Kartika (No. 30; data hanya di sub-tab Responsibilities Borrowed Assets, sedangkan Assigned Assets, Pending Approvals, dan Pending Tasks kosong). Rina Kartika tanpa data Assigned Assets dan Client FAMS aktif (precondition TC-GS-USER-391); spec tidak membuat atau mengubah aset Rina Kartika.
- Data Dinamis, dataset Assigned Assets milik Ahmad Fauzi (27 baris; dengan page size 10 menjadi tiga halaman: 10, 10, 7 baris). K1 adalah data Pre-setup (hanya dibaca, tidak dihapus); K2 sampai K27 di-seed milik spec lewat kemampuan seeding data Responsibilities/FAMS (HK8) di hook `before` (disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Saat spec mulai, Assigned Assets Ahmad Fauzi hanya berisi K1 sampai K27. Transaction ID `ASG-{runId}-120-kk` dan Asset ID `AST-{runId}-120-kk` dengan kk = nomor K dua digit:
  - K1 (Pre-setup, literal dari TC-GS-USER-390): Transaction ID `ASG-20260505-0001`, Name `Company Vehicle B1234XY`, Asset ID `AST-0001`, Brand `Toyota`, Model / Type `Hilux`, PIC `Citra Wulandari`.
  - K2 sampai K4: Name `Company Vehicle V1 {runId}-120` sampai `Company Vehicle V3 {runId}-120`, Brand `Toyota`, Model / Type `Hilux`, PIC `Rudi Hartanto {runId}-120`.
  - K5 sampai K7: Name `Company Vehicle V4 {runId}-120` sampai `Company Vehicle V6 {runId}-120`, Brand `Honda`, Model / Type `Civic`, PIC `Sinta Dewi {runId}-120`.
  - K8 sampai K12: Name `Laptop L1 {runId}-120` sampai `Laptop L5 {runId}-120`, Brand `Dell`, Model / Type `Latitude 5440`, PIC `Bambang Susanto {runId}-120`.
  - K13 sampai K17: Name `Laptop L6 {runId}-120` sampai `Laptop L10 {runId}-120`, Brand `Lenovo`, Model / Type `ThinkPad T14`, PIC `Rudi Hartanto {runId}-120`.
  - K18 sampai K22: Name `Printer P1 {runId}-120` sampai `Printer P5 {runId}-120`, Brand `Canon`, Model / Type `PIXMA G3010`, PIC `Sinta Dewi {runId}-120`.
  - K23 sampai K27: Name `Printer P6 {runId}-120` sampai `Printer P10 {runId}-120`, Brand `Epson`, Model / Type `EcoTank L3250`, PIC `Bambang Susanto {runId}-120`.
  - Ringkasan: Name 27 nilai distinct; Brand 6 nilai (Toyota 4 baris, Honda 3, Dell 5, Lenovo 5, Canon 5, Epson 5); PIC 4 nilai (Citra Wulandari 1 baris, Rudi Hartanto 8, Sinta Dewi 8, Bambang Susanto 10); baris ber-Name memuat `Vehicle`: 7 (K1 sampai K7). Nilai distinct pada kolom yang di-sort, di-search, dan di-filter dipenuhi (S-11).
  - Nama literal tanpa suffix hanya K1 (Pre-setup); seluruh nilai Name, Transaction ID, Asset ID, dan PIC milik spec bersuffix `{runId}-120`. Nama Brand dan Model / Type adalah nilai master tanpa suffix.
  - Tiap baris K2 sampai K27 memiliki foto aset; berkas foto K7 bernama `foto-{runId}-120-07`.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus aset seed K2 sampai K27 lewat kemampuan seeding yang sama; data Pre-setup (K1 dan record user) tidak diubah. Seeding aset tidak mengubah record user Ahmad Fauzi.
- Data uji per TC: TC-GS-USER-755 keyword `Vehicle`; TC-GS-USER-756 keyword `  VEHICLE  `; TC-GS-USER-757 keyword per kolom `G-{runId}-120-07` (Transaction ID), `Printer P3` (Name), `T-{runId}-120-12` (Asset ID), `Lenov` (Brand), `PIXMA` (Model / Type), `Sinta` (PIC); TC-GS-USER-758 keyword `foto-{runId}-120-07` (nama berkas foto K7, tidak ada di kolom searchable mana pun); TC-GS-USER-759 keyword `Sinta` (nilai yang hanya ada di kolom PIC); TC-GS-USER-760 keyword `zzzqqq`.
- Kemampuan teknis: seeding Assigned Assets (HK8) dan pembacaan data Pre-setup Rina Kartika tanpa aset; mengunggah foto aset seed; membaca nilai kolom dan jumlah baris tabel; membaca isi kotak Search apa adanya (spasi awal dan akhir).
- State yang diubah dan dipulihkan: visibilitas kolom `PIC` (dipulihkan pada langkah 67; hook `after` mengembalikan visibilitas kolom sub-tab Assigned Assets ke default sebagai cadangan), Search (ditutup lewat `(←)` di akhir blok). Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik icon Search, ketik `Ahmad Fauzi`, tekan Enter
2. Klik Name `Ahmad Fauzi` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Assigned Assets`

### TC-GS-USER-390: Screening sub-tab Assigned Assets

5. Verifikasi Toolbar: `Search | Filter | Download`
6. Klik icon Search
7. Verifikasi input Search kosong dengan placeholder `Search name, asset ID, or transaction ID...`
8. Klik icon panah `(←)` di kiri toolbar
9. Verifikasi kolom tabel: `Photo (unsortable) | Transaction ID | Name (default A-Z) | Asset ID | Brand | Model / Type | PIC | Column Visibility (⋯)`
10. Verifikasi baris contoh: baris pertama memuat Transaction ID `ASG-20260505-0001` dan Name `Company Vehicle B1234XY`
11. Verifikasi baris tabel tidak memiliki row action
12. Verifikasi kolom Actions hanya memuat pemicu Column Visibility (⋯)
13. Verifikasi kontrol pagination tampil (27 baris, tiga halaman)

### TC-GS-USER-755: Siklus Search: reveal, Enter, clear (✕), collapse ←

14. Klik icon Search
15. Verifikasi input Search melebar
16. Verifikasi kursor auto-focus di input Search
17. Ketik `Vehicle` pada kotak Search
18. Verifikasi icon `(✕)` muncul di dalam input
19. Verifikasi tabel belum tersaring (27 baris, tiga halaman)
20. Tekan Enter
21. Verifikasi tabel tersaring: 7 baris dan Name setiap baris memuat `Vehicle`
22. Klik icon `(✕)`
23. Verifikasi input Search kosong
24. Verifikasi tabel tetap menampilkan hasil search terakhir (7 baris)
25. Tekan Enter pada input kosong
26. Verifikasi tabel kembali menampilkan semua data (27 baris, tiga halaman)
27. Isi Search dengan `Vehicle`, tekan Enter
28. Klik icon panah `(←)` di kiri toolbar
29. Verifikasi kotak search collapse menjadi icon Search biasa
30. Verifikasi tabel langsung kembali menampilkan semua data (27 baris) tanpa menekan Enter
31. Klik icon Search
32. Verifikasi input Search kosong (keyword dikosongkan)

### TC-GS-USER-756: Query Search di-trim dan tidak case-sensitive

33. Isi Search dengan `  VEHICLE  ` (dua spasi di depan dan di belakang), tekan Enter
34. Verifikasi tabel menampilkan 7 baris yang Name-nya memuat `Vehicle` (spasi diabaikan, huruf besar kecil tidak dibedakan)
35. Verifikasi isi search box tetap menampilkan `  VEHICLE  ` apa adanya
36. Verifikasi kontrol pagination tidak tampil (7 baris, tidak lebih dari 10)

### TC-GS-USER-757: Search menemukan substring pada kolom kelas teks

37. Ganti isi kotak search dengan `G-{runId}-120-07`, tekan Enter
38. Verifikasi kolom Transaction ID: hanya 1 baris tampil dengan Transaction ID `ASG-{runId}-120-07` (Name `Company Vehicle V6 {runId}-120`)
39. Klik icon ×
40. Isi Search dengan `Printer P3`, tekan Enter
41. Verifikasi kolom Name: hanya 1 baris tampil dengan Name `Printer P3 {runId}-120`
42. Klik icon ×
43. Isi Search dengan `T-{runId}-120-12`, tekan Enter
44. Verifikasi kolom Asset ID: hanya 1 baris tampil dengan Asset ID `AST-{runId}-120-12` (Name `Laptop L5 {runId}-120`)
45. Klik icon ×
46. Isi Search dengan `Lenov`, tekan Enter
47. Verifikasi kolom Brand: 5 baris tampil dengan Brand `Lenovo` (`Laptop L6 {runId}-120` sampai `Laptop L10 {runId}-120`)
48. Klik icon ×
49. Isi Search dengan `PIXMA`, tekan Enter
50. Verifikasi kolom Model / Type: 5 baris tampil dengan Model / Type `PIXMA G3010` (`Printer P1 {runId}-120` sampai `Printer P5 {runId}-120`)
51. Klik icon ×
52. Isi Search dengan `Sinta`, tekan Enter
53. Verifikasi kolom PIC: 8 baris tampil dengan PIC `Sinta D` (`Company Vehicle V4 {runId}-120` sampai `V6 {runId}-120`, `Printer P1 {runId}-120` sampai `P5 {runId}-120`)
54. Klik icon ×

### TC-GS-USER-758: Kolom non-searchable (Photo) tidak tercakup Search

55. Verifikasi tabel tetap menampilkan 8 baris hasil search terakhir (pembanding sebelum Search kolom Photo)
56. Isi Search dengan `foto-{runId}-120-07`, tekan Enter
57. Verifikasi kolom Photo: keyword tidak mencocokkan baris mana pun (no result state `No results found`)

### TC-GS-USER-759: Search tidak mencocokkan kolom yang di-hide, kembali cocok setelah unhide

58. Klik icon panah `(←)` di kiri toolbar
59. Klik header kolom Actions (⋯)
60. Hilangkan centang kolom `PIC` pada Overlay Column Visibility
61. Tutup Overlay Column Visibility dengan menekan Esc
62. Verifikasi kolom `PIC` tidak tampil di tabel
63. Verifikasi tabel menampilkan 10 baris pada halaman 1 (pembanding sebelum Search)
64. Klik icon Search, ketik `Sinta`, tekan Enter
65. Verifikasi saat kolom PIC hidden: no result state `No results found`
66. Klik header kolom Actions (⋯)
67. Centang kembali kolom `PIC` pada Overlay Column Visibility
68. Tutup Overlay Column Visibility dengan menekan Esc
69. Tekan Enter pada kotak Search (isi tetap `Sinta`)
70. Verifikasi setelah unhide: 8 baris tampil kembali dengan PIC `Sinta D`

### TC-GS-USER-760: Empty filtered state

71. Ganti isi kotak search dengan `zzzqqq`, tekan Enter
72. Verifikasi empty filtered state: ilustrasi, `No results found`, dan `Try adjusting your search or filter.`
73. Klik icon panah `(←)` di kiri toolbar

### TC-GS-USER-391: Empty state sub-tab Assigned Assets pada user tanpa aset

74. Klik menu User di sidebar Global Settings
75. Klik icon Search, ketik `Rina Kartika`, tekan Enter
76. Klik Name `Rina Kartika` di User List
77. Klik Tab `Responsibilities`
78. Klik sub-tab `Assigned Assets`
79. Verifikasi empty state: ilustrasi, `No assigned assets`, dan `This user has no assigned assets currently.`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Dataset 27 baris (lebih dari satu halaman) dipenuhi spec lewat seeding di hook `before`; spec tidak menumpang spec lain.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 390, 755, 756, 757, 758, 759, 760, lalu 391 di akhir. TC-GS-USER-391 membuka user lain (Rina Kartika), sehingga ditaruh paling akhir supaya hanya ada satu kali pembukaan Ahmad Fauzi dan satu kali pindah user (S-10); urutan di `tc-user.md`: 390, 391, 755 sampai 760.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 4 (pembukaan layar bersama untuk Ahmad Fauzi; langkah 1 sampai 3 TC sumber dipenuhi sekali), klik icon × setelah tiap kasus TC-GS-USER-757, langkah 6 dan 8 (membuka dan menutup Search untuk mengamati placeholder, penghubung TC-GS-USER-390), langkah 58 (menutup Search dan mereset tabel sebelum kolom PIC di-hide), langkah 61 dan 68 (menutup overlay), serta langkah 73 (menutup Search di akhir blok Ahmad Fauzi). Langkah Uji 1 sampai 3 TC-GS-USER-391 membuka Dewi Lestari dari User List.
- Format PIC: kolom PIC di tabel menampilkan `[First Name] [Last Initial]` (contoh `Sinta D`), bukan nama lengkap (PRD user.md §4.1.3). Format teks opsi pada dropdown filter PIC ditetapkan PRD §4.1.3; spec tidak memutuskannya.
- Anchor positif (bagian 8b butir 2): langkah 13 (pagination tampil pada 27 baris) mendahului asersi ketiadaan pagination pada langkah 36; verifikasi tabel 8 baris sebelum Search kolom Photo, dan verifikasi tabel 10 baris sebelum Search saat PIC hidden, mendahului asersi no result.
- Asersi tambahan dengan alasan (S-03): langkah 13 dan 36 memenuhi Expected e TC-GS-USER-390 (`≤10 baris: kontrol pagination tidak tampil`), yang bersyarat jumlah baris. Dataset spec 27 baris (lebih dari satu halaman), sehingga kondisi `≤10 baris` diamati pada hasil Search 7 baris di TC-GS-USER-756; tampilan awal dengan 27 baris diasersi menampilkan pagination sebagai pembandingnya.
- Langkah Uji 5 TC-GS-USER-755 (`Ketik keyword, amati tabel`) dipecah menjadi satu `Verifikasi` per klausa Expected b (tabel belum tersaring, icon `(✕)` muncul). Langkah Uji 9 TC-GS-USER-755 (`Ketik keyword lagi, Enter, lalu klik icon ←`) dipenuhi langkah `Isi Search dengan` sampai klik `(←)`; keyword dikosongkan diamati dengan membuka kembali Search.
- Spec melewati sekitar 35 langkah (79 langkah) karena delapan TC berbagi satu layar (sub-tab Assigned Assets milik Ahmad Fauzi), satu dataset 27 baris, dan satu kelas harness (fungsional). Blok Search saling melanjutkan state (kotak Search yang masih terbuka dari kasus sebelumnya dipakai kasus berikutnya) sehingga memisahkannya mengulang login, seeding, dan pembukaan layar yang sama. TC-GS-USER-757 menguji enam kolom dengan blok identik (isi keyword, Enter, cek, clear) dan tiap blok berdiri sendiri.
- Pembagian TC lintas spec: TC-GS-USER-761 sampai 768 (Filter Panel) ada di spec 121; TC-GS-USER-769 sampai 773 (kombinasi Search dan Filter) ada di spec 122; TC-GS-USER-774, 775, 790, 791 (Sort, Pagination, kombinasi) ada di spec 123; TC-GS-USER-776 sampai 784 (Setup Column) ada di spec 124; TC-GS-USER-392 dan 785 sampai 789 (Download) ada di spec 125.
- Temuan untuk QA:
  - TC-GS-USER-390: Expected e (`≤10 baris: kontrol pagination tidak tampil`) bersyarat jumlah baris, sedangkan dataset yang dipakai spec ini lebih dari satu halaman; spec mengamatinya pada hasil Search 7 baris (TC-GS-USER-756). TC juga tidak menyebut Asset ID, Brand, Model / Type, dan PIC baris `ASG-20260505-0001` serta jumlah baris Pre-setup Assigned Assets Ahmad Fauzi; nilai tersebut ditetapkan dataset spec dan disediakan tim FE/BE.
  - TC-GS-USER-758: Data Uji (`Nilai tanggal/status sesuai data`) tidak sesuai kolom Photo yang menampilkan gambar. Spec memakai nama berkas foto K7 (`foto-{runId}-120-07`) sebagai `nilai yang tampil di kolom Photo`; TC tidak mendefinisikan nilai teks kolom Photo.
  - TC-GS-USER-755: Data Uji hanya `Keyword sesuai data`; spec memakai `Vehicle`. TC-GS-USER-757 hanya memberi contoh `Vehicle`; keyword per kolom ditetapkan spec.
  - TC-GS-USER-391: precondition `Client FAMS aktif` tidak memberi cara menyiapkannya; disediakan tim FE/BE. User `Rina Kartika` (No. 30) berasal dari Tabel Data Uji Pre-setup di TC.
  - TC-GS-USER-758 dan 759: Expected `no result state` tidak menyebut teksnya; spec memakai teks empty filtered state TC-GS-USER-760 (`No results found`).
  - Mekanisme menandai Guided Tooltip sebagai sudah dilihat dan menyiapkan data FAMS tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
