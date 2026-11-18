---
id: TC-FA-ASSIGN-UI-109-dialog-select-user-pic
title: "Dialog Select User untuk PIC"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [D-ASG-18, FLD-ASG-09, T-ASG-09, "§4.1#r15", S-ASG-24, EC-ASG-32, "EB-TBL-9@select-user-pic"]
smoke: []
dependsOn: []
trace:
  D-ASG-18: [2, 3, 4, 8, 22, 24, 25, 35, 38]
  FLD-ASG-09: [19, 27, 31]
  T-ASG-09: [6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 37, 56, 58, 60, 62, 64, 66, 68, 71, 72, 73, 74, 77, 79, 82, 85, 88, 91, 93]
  "§4.1#r15": [5, 39]
  S-ASG-24: [45, 46, 49, 50]
  EC-ASG-32: 43
  "EB-TBL-9@select-user-pic": [29, 31, 32, 53, 54]
anchor: [52, 87]
coverage:
  web: automated
---
# Dialog Select User untuk PIC

## Prerequisites
- Aktor: Asset Admin pada Group `Head Office`.
- Layar awal: form Assignment Request dengan Assignee Division `Finance` untuk K1, K3, K4, dan K6; halaman Assignment untuk aksi `Change PIC` pada K2 dan K5.
- Komponen: Dialog Select User
- Data:
  - DU-109-1: Karyawan `Nadia Putri`, Email `nadia.putri@example.com`, Position `Analyst`, Division `Finance`, Home Group `Head Office`, Status `Active`, Active Assignments `0 assets`.
  - DU-109-2: Karyawan `Nadia Pratama`, Email `nadia.pratama@example.com`, Position `Accountant`, Division `Finance`, Home Group `Branch Surabaya`, Status `Active`, Active Assignments `2 assets`; hierarki lengkap Home Group `Head Office > Branch Surabaya`, dari Home Group `Branch Surabaya`; aset yang sedang ditugaskan `Laptop Dell Latitude 5420 - 10` dan `Toyota Avanza - 6`, dari Active Assignments `2 assets`.
  - DU-109-3: Karyawan `Dewi Anggraini`, Email `dewi.anggraini@example.com`, Position `Staff`, Division `Finance`, Home Group `—`, Status `Active`, Active Assignments `1 asset`.
  - DU-109-4: Karyawan `Sari D`, Email `sari.d@example.com`, Position `Analyst`, Division `Finance`, Home Group `Head Office`, Status `Active`, Active Assignments `4 assets`; PIC saat ini pada K2 dan K5.
  - DU-109-5: Division Assignee `Finance`. Keterangan yang diharapkan `Active members of Finance who can sign in.`, dari Division `Finance`.
  - DU-109-6: Kata kunci Search `Tanpa Hasil` yang tidak cocok dengan baris mana pun.
  - DU-109-7: Karyawan `Rahmat Hidayat`, Email `rahmat.hidayat@example.com`, Position `Staff`, Division `Finance`, Home Group `Head Office`, Status `Inactive`, Active Assignments `0 assets`.
  - DU-109-8: Karyawan `Lina Marlina`, Email `lina.marlina@example.com`, Position `Supervisor`, Division `Logistics`, Home Group `Head Office`, Status `Active`, Active Assignments `0 assets`.
  - DU-109-9: Rentang saringan Active Assignments Min `1` dan Max `2`.
- Kondisi:
  - K1: dialog dibuka dari field PIC form Assignment Request untuk Division DU-109-5; daftar berisi DU-109-1 sampai DU-109-3; belum ada baris terpilih.
  - K2: dialog dibuka dari aksi `Change PIC` untuk Division DU-109-5 dengan PIC saat ini DU-109-4; daftar berisi DU-109-1 sampai DU-109-3.
  - K3: dialog dibuka dari field PIC; Division DU-109-5 tidak punya anggota aktif ber-akun login lain; daftar kosong.
  - K4: seperti K1; Search DU-109-6 tidak menemukan baris mana pun.
  - K5: seperti K2; keanggotaan `Nadia Putri` di Division DU-109-5 berubah oleh sesi lain sesudah daftar dimuat sehingga ia bukan lagi anggota aktif Finance; simpan PIC baru ditolak karena anggota yang dipilih bukan anggota aktif Division DU-109-5; pesan yang diharapkan `Nadia Putri isn't an active member of Finance.`, dari Name `Nadia Putri` dan Division `Finance`.
  - K6: seperti K1; karyawan DU-109-7 (Status `Inactive`) dan DU-109-8 (Division `Logistics`) ada di sistem tetapi bukan anggota aktif Division DU-109-5, sehingga daftar tetap berisi DU-109-1 sampai DU-109-3.

## Test Steps

### Dialog Select User dari field PIC: keterangan, toolbar, kolom, dan isi baris
1. Tampilkan Dialog Select User dengan kondisi K1
2. Verifikasi judul dialog `Select User`
3. Verifikasi keterangan `Active members of Finance who can sign in.` tampil
4. Verifikasi dialog Select User memuat tombol `[Cancel]` dan `[Select]`
5. Verifikasi toolbar dialog Select User memuat Search dan Filter
6. Verifikasi kotak Search dialog Select User memuat placeholder `Search name or email...`
7. Verifikasi kolom `Name`, `Email`, `Position`, `Division`, `Home Group`, `Status`, dan `Active Assignments` tampil
8. Verifikasi kolom `Eligibility` tidak tampil
9. Verifikasi baris `Nadia Putri` menampilkan Email `nadia.putri@example.com`
10. Verifikasi baris `Nadia Putri` menampilkan Position `Analyst`
11. Verifikasi baris `Nadia Putri` menampilkan kolom `Division` bernilai `Finance`
12. Verifikasi baris `Nadia Putri` menampilkan Home Group `Head Office`
13. Verifikasi baris `Nadia Putri` menampilkan Status `Active`
14. Verifikasi baris `Nadia Putri` menampilkan Active Assignments `0 assets`
15. Verifikasi baris `Nadia Pratama` menampilkan Email `nadia.pratama@example.com`
16. Verifikasi baris `Nadia Pratama` menampilkan Active Assignments `2 assets`
17. Verifikasi baris `Dewi Anggraini` menampilkan Home Group `—`
18. Verifikasi baris `Dewi Anggraini` menampilkan Active Assignments `1 asset`
19. Verifikasi tidak ada baris yang terpilih saat dialog dibuka

### Single-select: memilih baris baru melepas baris sebelumnya
20. Tampilkan Dialog Select User dengan kondisi K1
21. Pilih baris `Nadia Putri`
22. Verifikasi baris `Nadia Putri` terpilih
23. Pilih baris `Nadia Pratama`
24. Verifikasi baris `Nadia Pratama` terpilih
25. Verifikasi baris `Nadia Putri` tidak lagi terpilih
26. Klik `[Select]`
27. Verifikasi dialog Select User tertutup

### Select tanpa pilihan menampilkan error inline
28. Tampilkan Dialog Select User dengan kondisi K1
29. Verifikasi `[Select]` pada dialog Select User enabled
30. Klik `[Select]`
31. Verifikasi pesan error inline `You must pick a user` tampil di atas tombol footer
32. Verifikasi dialog Select User tetap terbuka karena pilihan tidak dikirim

### Cancel menutup dialog
33. Tampilkan Dialog Select User dengan kondisi K1
34. Klik `[Cancel]`
35. Verifikasi dialog Select User tertutup

### Change PIC: PIC saat ini tidak tampil
36. Tampilkan Dialog Select User dengan kondisi K2
37. Verifikasi baris `Nadia Putri`, `Nadia Pratama`, dan `Dewi Anggraini` tampil
38. Verifikasi baris `Sari D` tidak tampil karena PIC saat ini tidak masuk daftar
39. Verifikasi dialog Select User tampil untuk memilih PIC baru pada Change PIC

### Change PIC ditolak karena PIC baru bukan anggota Division
40. Tampilkan Dialog Select User dengan kondisi K5
41. Pilih baris `Nadia Putri`
42. Klik `[Select]`
43. Verifikasi pesan `Nadia Putri isn't an active member of Finance.` tampil

### Empty state tanpa anggota eligible
44. Tampilkan Dialog Select User dengan kondisi K3
45. Verifikasi empty state memuat judul `No eligible members`
46. Verifikasi empty state memuat teks `This division has no other active member who can sign in.`

### Empty state akibat Search tanpa hasil
47. Tampilkan Dialog Select User dengan kondisi K4
48. Ketik Search `Tanpa Hasil`, tekan Enter
49. Verifikasi empty state memuat judul `No results found`
50. Verifikasi empty state memuat teks `Try adjusting your search or filter.`

### Karyawan nonaktif dan di luar Division tidak muncul
51. Tampilkan Dialog Select User dengan kondisi K6
52. Verifikasi baris `Nadia Putri`, `Nadia Pratama`, dan `Dewi Anggraini` tampil sebagai anggota aktif Finance
53. Verifikasi baris `Rahmat Hidayat` tidak tampil karena Status `Inactive`
54. Verifikasi baris `Lina Marlina` tidak tampil karena kolom `Division` bernilai `Logistics`, bukan `Finance`

### Urutan default dan sort kolom
55. Tampilkan Dialog Select User dengan kondisi K1
56. Verifikasi tabel memuat tiga baris yang tampil berurutan `Dewi Anggraini`, `Nadia Pratama`, `Nadia Putri` menurut Name A–Z secara default
57. Klik header kolom `Active Assignments`
58. Verifikasi baris tampil berurutan `Nadia Putri`, `Dewi Anggraini`, `Nadia Pratama` menurut Active Assignments naik
59. Klik header kolom `Active Assignments`
60. Verifikasi baris tampil berurutan `Nadia Pratama`, `Dewi Anggraini`, `Nadia Putri` menurut Active Assignments turun
61. Klik header kolom `Position`
62. Verifikasi baris tampil berurutan `Nadia Pratama`, `Nadia Putri`, `Dewi Anggraini` menurut Position A–Z

### Avatar pada kolom Name dan hover Home Group serta Active Assignments
63. Tampilkan Dialog Select User dengan kondisi K1
64. Verifikasi baris `Nadia Putri` menampilkan avatar bersama nama `Nadia Putri` pada kolom `Name`
65. Arahkan kursor ke Home Group `Branch Surabaya` pada baris `Nadia Pratama`
66. Verifikasi hierarki lengkap Home Group `Head Office > Branch Surabaya` tersampaikan
67. Arahkan kursor ke Active Assignments `2 assets` pada baris `Nadia Pratama`
68. Verifikasi daftar aset yang sedang ditugaskan `Laptop Dell Latitude 5420 - 10` dan `Toyota Avanza - 6` tersampaikan

### Filter Panel: field per kolom Filterable dan penerapan rentang
69. Tampilkan Dialog Select User dengan kondisi K1
70. Klik tombol Filter pada toolbar dialog Select User
71. Verifikasi Filter Panel memuat field `Position` dengan placeholder `All positions`
72. Verifikasi Filter Panel memuat field `Home Group` dengan placeholder `All home groups`
73. Verifikasi Filter Panel memuat rentang `Active Assignments` dengan placeholder `Min` dan `Max`
74. Verifikasi Filter Panel tidak memuat field `Division` maupun `Status`
75. Isi Min pada `Active Assignments` dengan `1`
76. Isi Max pada `Active Assignments` dengan `2`
77. Verifikasi tombol Filter belum menandai ada saringan aktif karena nilai belum diterapkan
78. Klik `[Apply]`
79. Verifikasi tombol Filter menandai ada saringan aktif
80. Klik `[Clear Field]`
81. Klik `[Apply]`
82. Verifikasi tombol Filter tidak lagi menandai ada saringan aktif

### Setup Column: kolom dapat disembunyikan
83. Tampilkan Dialog Select User dengan kondisi K1
84. Buka Setup Column
85. Verifikasi kolom `Name`, `Email`, `Position`, `Division`, `Home Group`, `Status`, dan `Active Assignments` tercentang dan enabled pada Setup Column
86. Hilangkan centang `Email` pada Setup Column
87. Verifikasi kolom `Name` tetap tampil
88. Verifikasi kolom `Email` tidak tampil

### Search baru diterapkan saat Enter
89. Tampilkan Dialog Select User dengan kondisi K1
90. Ketik Search `nadia.pratama@example.com` tanpa menekan Enter
91. Verifikasi tabel masih memuat baris `Nadia Putri`, `Nadia Pratama`, dan `Dewi Anggraini` karena Search belum diterapkan
92. Tekan Enter pada kotak Search
93. Verifikasi kotak Search memuat `nadia.pratama@example.com`


