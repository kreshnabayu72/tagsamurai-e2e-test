---
id: TC-GS-USER-E2E-121-subtab-assigned-assets-filter-panel-opsi-multi-select-or-chip-dan-and
title: "Sub-tab Assigned Assets: Filter Panel (Opsi, Multi-Select, OR, Pencarian Dropdown, Chip, dan AND)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-761
  - TC-GS-USER-762
  - TC-GS-USER-763
  - TC-GS-USER-764
  - TC-GS-USER-765
  - TC-GS-USER-766
  - TC-GS-USER-767
  - TC-GS-USER-768
coverage:
  web: automated
---

# Sub-tab Assigned Assets: Filter Panel (Opsi, Multi-Select, OR, Pencarian Dropdown, Chip, dan AND)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup user; hanya dataset Assigned Assets milik spec yang ditambahkan lalu dibersihkan.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`.
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22, hanya dibaca): Ahmad Fauzi (No. 13; Assigned Assets berisi K1) dan Doni Pratama (No. 11, hanya sebagai pemegang aset pengecoh).
- Data Dinamis, dataset Assigned Assets milik Ahmad Fauzi (27 baris; dengan page size 10 menjadi tiga halaman: 10, 10, 7 baris). K1 adalah data Pre-setup (hanya dibaca, tidak dihapus); K2 sampai K27 di-seed milik spec lewat kemampuan seeding data Responsibilities/FAMS (HK8) di hook `before` (disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Saat spec mulai, Assigned Assets Ahmad Fauzi hanya berisi K1 sampai K27. Transaction ID `ASG-{runId}-121-kk` dan Asset ID `AST-{runId}-121-kk` dengan kk = nomor K dua digit:
  - K1 (Pre-setup, literal dari TC-GS-USER-390): Transaction ID `ASG-20260505-0001`, Name `Company Vehicle B1234XY`, Asset ID `AST-0001`, Brand `Toyota`, Model / Type `Hilux`, PIC `Citra Wulandari`.
  - K2 sampai K4: Name `Company Vehicle V1 {runId}-121` sampai `Company Vehicle V3 {runId}-121`, Brand `Toyota`, Model / Type `Hilux`, PIC `Rudi Hartanto {runId}-121`.
  - K5 sampai K7: Name `Company Vehicle V4 {runId}-121` sampai `Company Vehicle V6 {runId}-121`, Brand `Honda`, Model / Type `Civic`, PIC `Sinta Dewi {runId}-121`.
  - K8 sampai K12: Name `Laptop L1 {runId}-121` sampai `Laptop L5 {runId}-121`, Brand `Dell`, Model / Type `Latitude 5440`, PIC `Bambang Susanto {runId}-121`.
  - K13 sampai K17: Name `Laptop L6 {runId}-121` sampai `Laptop L10 {runId}-121`, Brand `Lenovo`, Model / Type `ThinkPad T14`, PIC `Rudi Hartanto {runId}-121`.
  - K18 sampai K22: Name `Printer P1 {runId}-121` sampai `Printer P5 {runId}-121`, Brand `Canon`, Model / Type `PIXMA G3010`, PIC `Sinta Dewi {runId}-121`.
  - K23 sampai K27: Name `Printer P6 {runId}-121` sampai `Printer P10 {runId}-121`, Brand `Epson`, Model / Type `EcoTank L3250`, PIC `Bambang Susanto {runId}-121`.
  - Ringkasan: Name 27 nilai distinct; Brand 6 nilai (Toyota 4 baris, Honda 3, Dell 5, Lenovo 5, Canon 5, Epson 5); PIC 4 nilai (Citra Wulandari 1 baris, Rudi Hartanto 8, Sinta Dewi 8, Bambang Susanto 10); baris ber-Name memuat `Vehicle`: 7 (K1 sampai K7). Nilai distinct pada kolom yang di-sort, di-search, dan di-filter dipenuhi (S-11).
  - Nama literal tanpa suffix hanya K1 (Pre-setup); seluruh nilai Name, Transaction ID, Asset ID, dan PIC milik spec bersuffix `{runId}-121`. Nama Brand dan Model / Type adalah nilai master tanpa suffix.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus aset seed K2 sampai K27 lewat kemampuan seeding yang sama; data Pre-setup (K1 dan record user) tidak diubah. Seeding aset tidak mengubah record user Ahmad Fauzi.
- Aset pengecoh (untuk asersi opsi dropdown tidak memuat nilai tanpa baris di tabel, TC-GS-USER-762): satu aset FAMS yang ditugaskan ke Doni Pratama dengan Name `Decoy Asset {runId}-121`, Brand `Brother`, PIC `Dedi Kurnia {runId}-121`; di-seed di hook `before` lewat kemampuan seeding yang sama dengan dataset dan dihapus di hook `after`. Aset ini tidak tampil di Assigned Assets Ahmad Fauzi.
- Data uji per TC: TC-GS-USER-763 opsi Name `Printer P3 {runId}-121`, Brand `Lenovo`, PIC `Sinta Dewi {runId}-121`; TC-GS-USER-764 dan 766 dan 767 opsi Name `Printer P3 {runId}-121` dan `Laptop L2 {runId}-121`; TC-GS-USER-765 keyword dropdown `LAPTOP L1` dan `zzz`; TC-GS-USER-768 Brand `Toyota` dan PIC `Rudi Hartanto {runId}-121`.
- Kemampuan teknis: seeding Assigned Assets (HK8) untuk dua user (disediakan tim FE/BE); membaca opsi, chip, dan status centang dropdown multi-select; membaca status gelap dan badge titik pada icon Filter.
- State yang diubah dan dipulihkan: Filter dikosongkan lewat `[Clear Field]` dan `[Apply]` di akhir tiap blok yang menerapkannya; hook `after` sebagai cadangan. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik icon Search, ketik `Ahmad Fauzi`, tekan Enter
2. Klik Name `Ahmad Fauzi` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Assigned Assets`

### TC-GS-USER-761: Screening Filter Panel

5. Klik icon Filter
6. Verifikasi Filter Panel memuat empat field berurutan: `Name` (multi-select searchable, placeholder `All assets`), `Brand` (multi-select searchable, placeholder `All brands`), `Model / Type` (multi-select searchable, placeholder `All models/types`), dan `PIC` (multi-select searchable, placeholder `All PICs`)
7. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-GS-USER-762: Opsi dropdown filter diambil dari nilai yang ada di tabel

8. Buka dropdown Name
9. Verifikasi opsi Name berjumlah 27: `Company Vehicle B1234XY`, `Company Vehicle V1 {runId}-121` sampai `Company Vehicle V6 {runId}-121`, `Laptop L1 {runId}-121` sampai `Laptop L10 {runId}-121`, dan `Printer P1 {runId}-121` sampai `Printer P10 {runId}-121`
10. Verifikasi opsi `Decoy Asset {runId}-121` tidak ada di dropdown Name
11. Buka dropdown Brand
12. Verifikasi opsi Brand berjumlah 6: `Toyota`, `Honda`, `Dell`, `Lenovo`, `Canon`, dan `Epson`
13. Verifikasi opsi `Brother` tidak ada di dropdown Brand
14. Buka dropdown PIC
15. Verifikasi opsi PIC berjumlah 4: `Citra Wulandari`, `Rudi Hartanto {runId}-121`, `Sinta Dewi {runId}-121`, dan `Bambang Susanto {runId}-121`
16. Verifikasi opsi `Dedi Kurnia {runId}-121` tidak ada di dropdown PIC

### TC-GS-USER-763: Filter multi-select per field menyaring baris

17. Pilih opsi `Printer P3 {runId}-121` pada dropdown Name
18. Klik `[Apply]`
19. Verifikasi tabel hanya menampilkan 1 baris dengan Name `Printer P3 {runId}-121`
20. Verifikasi badge titik tampil pada icon Filter
21. Klik icon Filter
22. Verifikasi icon Filter gelap (panel terbuka)
23. Klik `[Clear Field]`
24. Klik `[Apply]`
25. Klik icon Filter
26. Pilih opsi `Lenovo` pada dropdown Brand
27. Klik `[Apply]`
28. Verifikasi tabel hanya menampilkan 5 baris dengan Brand `Lenovo` (`Laptop L6 {runId}-121` sampai `Laptop L10 {runId}-121`)
29. Verifikasi badge titik tampil pada icon Filter
30. Klik icon Filter
31. Verifikasi icon Filter gelap (panel terbuka)
32. Klik `[Clear Field]`
33. Klik `[Apply]`
34. Klik icon Filter
35. Pilih opsi `Sinta Dewi {runId}-121` pada dropdown PIC
36. Klik `[Apply]`
37. Verifikasi tabel hanya menampilkan 8 baris dengan PIC `Sinta D`
38. Verifikasi badge titik tampil pada icon Filter
39. Klik icon Filter
40. Verifikasi icon Filter gelap (panel terbuka)
41. Klik `[Clear Field]`
42. Klik `[Apply]`

### TC-GS-USER-764: Dua opsi dalam satu field filter digabung OR

43. Klik icon Filter
44. Pilih opsi `Printer P3 {runId}-121` pada dropdown Name
45. Pilih opsi `Laptop L2 {runId}-121` pada dropdown Name
46. Klik `[Apply]`
47. Verifikasi tabel menampilkan tepat 2 baris: Name `Printer P3 {runId}-121` dan Name `Laptop L2 {runId}-121`
48. Klik icon Filter
49. Klik `[Clear Field]`
50. Klik `[Apply]`

### TC-GS-USER-765: Search di dalam dropdown filter mempersempit opsi

51. Klik icon Filter
52. Buka dropdown Name
53. Ketik `LAPTOP L1` pada pencarian di dalam dropdown Name
54. Verifikasi opsi tersaring substring tanpa membedakan huruf besar kecil: hanya `Laptop L1 {runId}-121` dan `Laptop L10 {runId}-121`
55. Ganti isi pencarian dropdown dengan `zzz`
56. Verifikasi tidak ada opsi yang cocok di dropdown Name
57. Kosongkan isi pencarian dropdown Name

### TC-GS-USER-766: Hapus chip filter via (X) meng-uncheck opsi

58. Pilih opsi `Printer P3 {runId}-121` pada dropdown Name
59. Pilih opsi `Laptop L2 {runId}-121` pada dropdown Name
60. Verifikasi dua chip tampil berurutan: `Printer P3 {runId}-121` lalu `Laptop L2 {runId}-121`
61. Klik (X) pada chip pertama `Printer P3 {runId}-121`
62. Verifikasi chip `Printer P3 {runId}-121` hilang
63. Verifikasi chip `Laptop L2 {runId}-121` tetap tampil
64. Buka dropdown Name
65. Verifikasi checkbox opsi `Printer P3 {runId}-121` ter-uncheck

### TC-GS-USER-767: Uncheck opsi di dropdown menghapus chip

66. Klik `[Clear Field]`
67. Pilih opsi `Printer P3 {runId}-121` pada dropdown Name
68. Pilih opsi `Laptop L2 {runId}-121` pada dropdown Name
69. Verifikasi dua chip tampil: `Printer P3 {runId}-121` dan `Laptop L2 {runId}-121`
70. Buka dropdown Name, hilangkan centang opsi kedua `Laptop L2 {runId}-121`
71. Verifikasi chip `Laptop L2 {runId}-121` hilang
72. Verifikasi chip `Printer P3 {runId}-121` tetap tampil

### TC-GS-USER-768: Kombinasi dua field filter digabung AND

73. Klik `[Clear Field]`
74. Pilih opsi `Toyota` pada dropdown Brand
75. Pilih opsi `Rudi Hartanto {runId}-121` pada dropdown PIC
76. Klik `[Apply]`
77. Verifikasi tabel hanya menampilkan 3 baris yang memenuhi Brand `Toyota` dan PIC `Rudi H`: `Company Vehicle V1 {runId}-121` sampai `Company Vehicle V3 {runId}-121`
78. Klik icon Filter
79. Klik `[Clear Field]`
80. Klik `[Apply]`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Dataset 27 baris (lebih dari satu halaman) dipenuhi spec lewat seeding di hook `before`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (761 sampai 768) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 4 (pembukaan layar bersama untuk Ahmad Fauzi), tiga langkah pembersih filter (`Klik icon Filter`, `[Clear Field]`, `[Apply]`) di akhir TC-GS-USER-763, 764, dan 768 serta di antara kasus Name, Brand, dan PIC pada TC-GS-USER-763, `[Clear Field]` pembuka TC-GS-USER-767 dan 768, serta langkah pengosongan pencarian dropdown di akhir TC-GS-USER-765. Langkah `Klik icon Filter` yang berulang merupakan prefix berulang.
- Format PIC: kolom PIC di tabel menampilkan `[First Name] [Last Initial]` (contoh `Sinta D`), bukan nama lengkap (PRD user.md §4.1.3). Format teks opsi pada dropdown filter PIC ditetapkan PRD §4.1.3; spec tidak memutuskannya.
- Anchor positif (bagian 8b butir 2): verifikasi daftar opsi Name, Brand, dan PIC mendahului asersi ketiadaan `Decoy Asset {runId}-121`, `Brother`, dan `Dedi Kurnia {runId}-121` pada dropdown yang sama.
- Dropdown yang masih terbuka dipindah dengan membuka dropdown berikutnya; Filter Panel yang masih terbuka dari kasus sebelumnya dipakai ulang (TC-GS-USER-762 memakai panel dari TC-GS-USER-761, TC-GS-USER-766 dan 767 memakai panel dan dropdown dari TC-GS-USER-765). Langkah Uji 4 sampai 5 TC-GS-USER-762 dipenuhi `Klik icon Filter` TC-GS-USER-761.
- Langkah Uji 6 TC-GS-USER-766 (`Klik (X) pada chip pertama`) mengikuti urutan pemilihan: chip pertama adalah opsi yang dipilih lebih dulu (`Printer P3 {runId}-121`).
- Spec melewati sekitar 35 langkah (80 langkah) karena delapan TC berbagi satu layar (Filter Panel sub-tab Assigned Assets), satu dataset 27 baris, dan satu kelas harness (fungsional). TC-GS-USER-763 menguji tiga field dengan blok identik (pilih, Apply, cek, bersihkan) dan tiap blok berdiri sendiri; TC-GS-USER-765 sampai 767 memakai Filter Panel dan dropdown Name yang sama sehingga memisahkannya mengulang login, seeding, dan pembukaan layar yang sama.
- Pembagian TC lintas spec: TC-GS-USER-390, 391, dan 755 sampai 760 (screening, empty state, Search) ada di spec 120; TC-GS-USER-769 sampai 773 (kombinasi Search dan Filter) ada di spec 122; TC-GS-USER-774, 775, 790, 791 ada di spec 123; TC-GS-USER-776 sampai 784 ada di spec 124; TC-GS-USER-392 dan 785 sampai 789 ada di spec 125.
- Temuan untuk QA:
  - TC-GS-USER-762: Expected `nilai tanpa baris tidak tampil` tidak menyebut contoh nilai tanpa baris; spec menetapkan aset pengecoh milik user lain (Doni Pratama) sebagai nilai tanpa baris di tabel Ahmad Fauzi. Apakah opsi dropdown berasal dari aset user ini atau dari seluruh aset client tidak dinyatakan jelas di TC maupun PRD.
  - TC-GS-USER-764: Data Uji hanya `2 opsi`; spec memakai `Printer P3 {runId}-121` dan `Laptop L2 {runId}-121`. TC-GS-USER-768 hanya `2 field`; spec memakai Brand dan PIC.
  - TC-GS-USER-765: Expected b (`zzz: tidak ada opsi cocok`) tidak menyebut teks atau tampilan kosong dropdown; spec hanya mengasersi tidak ada opsi.
  - Mekanisme menandai Guided Tooltip sebagai sudah dilihat dan menyiapkan data FAMS tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
