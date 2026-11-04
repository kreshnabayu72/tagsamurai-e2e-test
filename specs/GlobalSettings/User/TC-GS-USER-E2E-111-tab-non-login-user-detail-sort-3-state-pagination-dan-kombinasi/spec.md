---
id: TC-GS-USER-E2E-111-tab-non-login-user-detail-sort-3-state-pagination-dan-kombinasi
title: "Tab Non-Login User Detail: Sort 3-state, Pagination, dan kombinasi Search+Filter+Sort+Pagination"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-692
  - TC-GS-USER-693
  - TC-GS-USER-694
  - TC-GS-USER-695
  - TC-GS-USER-696
  - TC-GS-USER-714
  - TC-GS-USER-715
coverage:
  web: automated
---

# Tab Non-Login User Detail: Sort 3-state, Pagination, dan kombinasi Search+Filter+Sort+Pagination

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup; state yang diubah adalah page size tabel, sort, dan visibilitas kolom curated (dipulihkan).
- Akun: Total Control, `Siti Nurhaliza`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Master Data Position (`Finance Manager`, `Staff`, `Supervisor`, `Internal Auditor`) dan Division (`Finance`, `General Affairs`, `Legal`) Pre-setup No. 22 dan 23 sebagai nilai seed.
- Data Dinamis, holder: Login User milik spec `Ahmad Fauzi {runId}-111` (email `ahmadfauzi+{runId}-111@qwertysystem.net`, status Activated, Access Global Settings) sebagai Represented By seluruh Non-Login User di bawah. Holder milik spec dipakai, bukan `Ahmad Fauzi` Pre-setup (Tabel Data Uji Pre-setup No. 13) beserta `Agus Prasetyo` dan `Lina Marlina` Pre-setup (No. 21), karena S-06 melarang mengubah data Pre-setup bersama dan S-11 menuntut data dengan lebih dari satu halaman serta sedikitnya dua nilai distinct pada kolom yang diuji.
- Data Dinamis, 21 Non-Login User milik spec (Represented By = `Ahmad Fauzi {runId}-111`), di-seed di hook `before` (TC-GS-USER-714 mensyaratkan 21 baris atau lebih). Tabel memuat 21 baris: halaman 1 dan 2 berisi 10 baris, halaman 3 berisi 1 baris. `{L1}` = tanggal 7 hari sebelum hari uji dan `{L2}` = tanggal hari uji pada kolom Last Update; Temporary Until = hari uji + N hari; semua tanggal ditampilkan dalam Date Format General Settings.
  | Name | Email | Employee ID | Position | Division | Active | Temporary User | Temporary Until | Last Update |
  |---|---|---|---|---|---|---|---|---|
  | `Agus Prasetyo {runId}-111` | `nlu07+{runId}-111@qwertysystem.net` | `EMP-05-{runId}-111` | Finance Manager | Finance | Active | No | kosong | `{L2}` |
  | `Bagas Santoso {runId}-111` | `nlu14+{runId}-111@qwertysystem.net` | `EMP-10-{runId}-111` | Internal Auditor | General Affairs | Active | Yes | hari uji + 50 hari | `{L1}` |
  | `Citra Dewanti {runId}-111` | `nlu21+{runId}-111@qwertysystem.net` | `EMP-15-{runId}-111` | Staff | Legal | Active | No | kosong | `{L2}` |
  | `Dimas Pranoto {runId}-111` | `nlu06+{runId}-111@qwertysystem.net` | `EMP-20-{runId}-111` | Supervisor | Finance | Active | No | kosong | `{L1}` |
  | `Eka Wulandari {runId}-111` | `nlu13+{runId}-111@qwertysystem.net` | `EMP-03-{runId}-111` | Finance Manager | General Affairs | Inactive | No | kosong | `{L2}` |
  | `Fitri Handayani {runId}-111` | `nlu20+{runId}-111@qwertysystem.net` | `EMP-08-{runId}-111` | Internal Auditor | Legal | Active | No | kosong | `{L1}` |
  | `Galih Permadi {runId}-111` | `nlu05+{runId}-111@qwertysystem.net` | `EMP-13-{runId}-111` | Staff | Finance | Active | Yes | hari uji + 20 hari | `{L2}` |
  | `Hana Kusuma {runId}-111` | `nlu12+{runId}-111@qwertysystem.net` | `EMP-18-{runId}-111` | Supervisor | General Affairs | Active | No | kosong | `{L1}` |
  | `Indra Gunawan {runId}-111` | `nlu19+{runId}-111@qwertysystem.net` | `EMP-01-{runId}-111` | Finance Manager | Legal | Active | No | kosong | `{L2}` |
  | `Joko Pramono {runId}-111` | `nlu04+{runId}-111@qwertysystem.net` | `EMP-06-{runId}-111` | Internal Auditor | Finance | Active | No | kosong | `{L1}` |
  | `Kartika Sari {runId}-111` | `nlu11+{runId}-111@qwertysystem.net` | `EMP-11-{runId}-111` | Staff | General Affairs | Active | Yes | hari uji + 40 hari | `{L2}` |
  | `Lina Marlina {runId}-111` | `nlu18+{runId}-111@qwertysystem.net` | kosong | kosong | Legal | Inactive | No | kosong | `{L1}` |
  | `Maya Putri {runId}-111` | `nlu03+{runId}-111@qwertysystem.net` | `EMP-21-{runId}-111` | Finance Manager | Finance | Active | No | kosong | `{L2}` |
  | `Nadia Rahma {runId}-111` | `nlu10+{runId}-111@qwertysystem.net` | `EMP-04-{runId}-111` | Internal Auditor | General Affairs | Active | No | kosong | `{L1}` |
  | `Oka Saputra {runId}-111` | `nlu17+{runId}-111@qwertysystem.net` | kosong | kosong | Legal | Active | No | kosong | `{L2}` |
  | `Putri Ayu {runId}-111` | `nlu02+{runId}-111@qwertysystem.net` | `EMP-14-{runId}-111` | Supervisor | Finance | Active | Yes | hari uji + 10 hari | `{L1}` |
  | `Rizky Fadillah {runId}-111` | `nlu09+{runId}-111@qwertysystem.net` | `EMP-19-{runId}-111` | Finance Manager | General Affairs | Inactive | No | kosong | `{L2}` |
  | `Sinta Dewi {runId}-111` | `nlu16+{runId}-111@qwertysystem.net` | `EMP-02-{runId}-111` | Internal Auditor | Legal | Active | No | kosong | `{L1}` |
  | `Tegar Wibowo {runId}-111` | `nlu01+{runId}-111@qwertysystem.net` | `EMP-07-{runId}-111` | Staff | Finance | Active | Yes | hari uji + 30 hari | `{L2}` |
  | `Umar Hakim {runId}-111` | `nlu08+{runId}-111@qwertysystem.net` | `EMP-12-{runId}-111` | Supervisor | General Affairs | Active | No | kosong | `{L1}` |
  | `Wahyu Hidayat {runId}-111` | `nlu15+{runId}-111@qwertysystem.net` | `EMP-17-{runId}-111` | Finance Manager | Legal | Inactive | No | kosong | `{L2}` |

  Komposisi nilai (dua nilai distinct atau lebih pada tiap kolom yang di-sort, S-11): Email dan Employee ID berurutan acak terhadap Name sehingga A-Z dan Z-A keduanya berbeda dari default Name A-Z; Position 4 nilai (Finance Manager 6, Internal Auditor 5, Staff 4, Supervisor 4 baris) dan 2 baris kosong (`Lina Marlina`, `Oka Saputra`); Employee ID 19 nilai dan 2 baris kosong (baris yang sama); Division 3 nilai (7 baris tiap nilai); Active 17 baris dan Inactive 4 baris; Temporary User `Yes` 5 baris dengan 5 tanggal Temporary Until berbeda; Last Update 2 tanggal (10 baris `{L1}`, 11 baris `{L2}`).
- Kemampuan teknis (disediakan tim FE/BE; endpoint ditentukan tim FE di tahap script): seeding Login User holder dan Non-Login User dengan Represented By = holder lewat API di hook `before`; cleanup di hook `after` menghapus Non-Login User lalu holder lewat API tanpa berasumsi seeding berhasil penuh. Seeding menambah 22 user pada hitungan Master Data Count Limit gabungan Login + Non-Login User; nilai limit environment cukup besar untuk itu.
- Kemampuan teknis tambahan (disediakan tim FE/BE; TC tidak memberi cara): mengatur Last Update Non-Login User seed menjadi `{L1}` untuk baris bernomor genap dan `{L2}` untuk baris bernomor ganjil pada tabel di atas. Last Update diturunkan dari waktu entri Changelog terbaru user itu (PRD user.md §4.1.4), sehingga nilainya tidak dapat diatur lewat edit biasa.
- Data uji per TC: TC-GS-USER-714 page size 25 dan 10, nomor halaman 2; TC-GS-USER-715 keyword `EMP`, Filter Status `Active`, sort Name Z-A, page size 25. Sort memakai kolom Name, Email, Division, Employee ID, Position, Active, Last Update, Temporary Until, dan Temporary User.
- Date Format General Settings default environment (`DD/MM/YY`); spec tidak mengubahnya.
- Kolom `Temporary User` dan `Temporary Until` adalah Curated (default unchecked, PRD user.md §4.1.4) dan ditampilkan lewat Overlay Column Visibility sebelum sort kedua kolom itu, lalu disembunyikan kembali (langkah 77 sampai 80). Preferensi kolom tersimpan di browser (PRD prd-conventions.md §9.3); hook `after` mengembalikan preferensi kolom Tab Non-Login User ke default.
- State yang diubah dan dipulihkan: page size dikembalikan ke 10 (langkah 81) dan di akhir spec, sort Name dikembalikan ke default, Search ditutup dengan icon ←, Filter dikosongkan; hook `after` sebagai cadangan.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`). Spec tidak mengubah data Pre-setup bersama (S-06).
- Kemampuan teknis: membaca teks sel tabel dan urutan baris; memilih page size dan mengetik nomor halaman di footer pagination; menekan Esc untuk menutup Overlay Column Visibility.

## Test Steps

1. Klik icon Search, ketik `Ahmad Fauzi {runId}-111`, tekan Enter
2. Klik Name `Ahmad Fauzi {runId}-111` di User List
3. Klik Tab `Non-Login User`

### TC-GS-USER-714: Pagination ubah page size dan input nomor halaman

4. Verifikasi tabel menampilkan 10 baris pada halaman 1 (page size default 10, total 3 halaman untuk 21 baris)
5. Ubah page size ke 25
6. Verifikasi tabel menampilkan 21 baris dalam satu halaman (tidak lebih dari 25 baris)
7. Ubah page size ke 10
8. Ketik nomor halaman `2` di input nomor halaman, tekan Enter
9. Verifikasi tabel langsung berada di halaman 2: 10 baris dari `Kartika Sari {runId}-111` sampai `Umar Hakim {runId}-111`
10. Klik next
11. Verifikasi tabel berpindah ke halaman 3: 1 baris `Wahyu Hidayat {runId}-111`
12. Klik prev
13. Verifikasi tabel berpindah ke halaman 2: 10 baris dari `Kartika Sari {runId}-111` sampai `Umar Hakim {runId}-111`
14. Ubah page size ke 25

### TC-GS-USER-692: Sort 3-state kolom kelas teks A-Z

15. Klik header kolom Name
16. Verifikasi Name klik 1 A-Z: 3 baris pertama `Agus Prasetyo {runId}-111`, `Bagas Santoso {runId}-111`, `Citra Dewanti {runId}-111`
17. Klik header kolom Name
18. Verifikasi Name klik 2 Z-A: 3 baris pertama `Wahyu Hidayat {runId}-111`, `Umar Hakim {runId}-111`, `Tegar Wibowo {runId}-111`
19. Klik header kolom Name
20. Verifikasi Name klik 3 kembali ke default sort tabel Name A-Z: 3 baris pertama `Agus Prasetyo {runId}-111`, `Bagas Santoso {runId}-111`, `Citra Dewanti {runId}-111`
21. Klik header kolom Email
22. Verifikasi Email klik 1 A-Z: 3 baris pertama memuat Email `nlu01+{runId}-111@qwertysystem.net`, `nlu02+{runId}-111@qwertysystem.net`, `nlu03+{runId}-111@qwertysystem.net`
23. Klik header kolom Email
24. Verifikasi Email klik 2 Z-A: 3 baris pertama memuat Email `nlu21+{runId}-111@qwertysystem.net`, `nlu20+{runId}-111@qwertysystem.net`, `nlu19+{runId}-111@qwertysystem.net`
25. Klik header kolom Email
26. Verifikasi Email klik 3 kembali ke default sort tabel Name A-Z: 3 baris pertama `Agus Prasetyo {runId}-111`, `Bagas Santoso {runId}-111`, `Citra Dewanti {runId}-111`
27. Klik header kolom Division
28. Verifikasi Division klik 1 A-Z: 7 baris pertama memuat Division `Finance`
29. Klik header kolom Division
30. Verifikasi Division klik 2 Z-A: 7 baris pertama memuat Division `Legal`
31. Klik header kolom Division
32. Verifikasi Division klik 3 kembali ke default sort tabel Name A-Z: 3 baris pertama `Agus Prasetyo {runId}-111`, `Bagas Santoso {runId}-111`, `Citra Dewanti {runId}-111`

### TC-GS-USER-693: Sort 3-state kolom kelas teks dengan kosong di akhir

33. Klik header kolom Employee ID
34. Verifikasi Employee ID klik 1 A-Z: 3 baris pertama memuat Employee ID `EMP-01-{runId}-111`, `EMP-02-{runId}-111`, `EMP-03-{runId}-111`
35. Verifikasi Employee ID klik 1: 2 baris terakhir (`Lina Marlina {runId}-111` dan `Oka Saputra {runId}-111`) menampilkan `—` di akhir
36. Klik header kolom Employee ID
37. Verifikasi Employee ID klik 2 Z-A: 3 baris pertama memuat Employee ID `EMP-21-{runId}-111`, `EMP-20-{runId}-111`, `EMP-19-{runId}-111`
38. Verifikasi Employee ID klik 2: 2 baris terakhir (`Lina Marlina {runId}-111` dan `Oka Saputra {runId}-111`) tetap menampilkan `—` di akhir
39. Klik header kolom Employee ID
40. Verifikasi Employee ID klik 3 kembali ke default sort tabel Name A-Z: 3 baris pertama `Agus Prasetyo {runId}-111`, `Bagas Santoso {runId}-111`, `Citra Dewanti {runId}-111`
41. Klik header kolom Position
42. Verifikasi Position klik 1 A-Z: 6 baris pertama memuat Position `Finance Manager`
43. Verifikasi Position klik 1: 2 baris terakhir (`Lina Marlina {runId}-111` dan `Oka Saputra {runId}-111`) menampilkan `—` di akhir
44. Klik header kolom Position
45. Verifikasi Position klik 2 Z-A: 4 baris pertama memuat Position `Supervisor`
46. Verifikasi Position klik 2: 2 baris terakhir (`Lina Marlina {runId}-111` dan `Oka Saputra {runId}-111`) tetap menampilkan `—` di akhir
47. Klik header kolom Position
48. Verifikasi Position klik 3 kembali ke default sort tabel Name A-Z: 3 baris pertama `Agus Prasetyo {runId}-111`, `Bagas Santoso {runId}-111`, `Citra Dewanti {runId}-111`

### TC-GS-USER-694: Sort 3-state kolom kelas status

49. Klik header kolom Active
50. Verifikasi Active klik 1 Active First: 17 baris pertama berbadge `Active` dan 4 baris terakhir berbadge `Inactive` (`Eka Wulandari {runId}-111`, `Lina Marlina {runId}-111`, `Rizky Fadillah {runId}-111`, `Wahyu Hidayat {runId}-111`)
51. Klik header kolom Active
52. Verifikasi Active klik 2 Inactive First: 4 baris pertama berbadge `Inactive` (`Eka Wulandari {runId}-111`, `Lina Marlina {runId}-111`, `Rizky Fadillah {runId}-111`, `Wahyu Hidayat {runId}-111`) dan 17 baris sesudahnya berbadge `Active`
53. Klik header kolom Active
54. Verifikasi Active klik 3 kembali ke default sort tabel Name A-Z: 5 baris pertama `Agus Prasetyo {runId}-111`, `Bagas Santoso {runId}-111`, `Citra Dewanti {runId}-111`, `Dimas Pranoto {runId}-111`, `Eka Wulandari {runId}-111` dengan `Eka Wulandari {runId}-111` berbadge `Inactive`

### TC-GS-USER-695: Sort 3-state kolom kelas tanggal

55. Klik header kolom Last Update
56. Verifikasi Last Update klik 1 Oldest First: 10 baris pertama memuat Last Update `{L1}` dan 11 baris sesudahnya memuat `{L2}`
57. Klik header kolom Last Update
58. Verifikasi Last Update klik 2 Newest First: 11 baris pertama memuat Last Update `{L2}` dan 10 baris sesudahnya memuat `{L1}`
59. Klik header kolom Last Update
60. Verifikasi Last Update klik 3 kembali ke default sort tabel Name A-Z: 3 baris pertama `Agus Prasetyo {runId}-111`, `Bagas Santoso {runId}-111`, `Citra Dewanti {runId}-111`
61. Klik header kolom Column Visibility (⋯)
62. Centang kolom `Temporary User`
63. Centang kolom `Temporary Until`
64. Tutup Overlay Column Visibility dengan menekan Esc
65. Klik header kolom Temporary Until
66. Verifikasi Temporary Until klik 1 Oldest First: 5 baris pertama berurutan `Putri Ayu {runId}-111`, `Galih Permadi {runId}-111`, `Tegar Wibowo {runId}-111`, `Kartika Sari {runId}-111`, `Bagas Santoso {runId}-111`
67. Klik header kolom Temporary Until
68. Verifikasi Temporary Until klik 2 Newest First: 5 baris pertama berurutan `Bagas Santoso {runId}-111`, `Kartika Sari {runId}-111`, `Tegar Wibowo {runId}-111`, `Galih Permadi {runId}-111`, `Putri Ayu {runId}-111`
69. Klik header kolom Temporary Until
70. Verifikasi Temporary Until klik 3 kembali ke default sort tabel Name A-Z: 3 baris pertama `Agus Prasetyo {runId}-111`, `Bagas Santoso {runId}-111`, `Citra Dewanti {runId}-111`

### TC-GS-USER-696: Sort 3-state kolom kelas Yes/No

71. Klik header kolom Temporary User
72. Verifikasi Temporary User klik 1 Yes First: 5 baris pertama berstatus `Yes` (`Bagas Santoso {runId}-111`, `Galih Permadi {runId}-111`, `Kartika Sari {runId}-111`, `Putri Ayu {runId}-111`, `Tegar Wibowo {runId}-111`) dan 16 baris sesudahnya `No`
73. Klik header kolom Temporary User
74. Verifikasi Temporary User klik 2 No First: 16 baris pertama berstatus `No` dan 5 baris terakhir `Yes` (`Bagas Santoso {runId}-111`, `Galih Permadi {runId}-111`, `Kartika Sari {runId}-111`, `Putri Ayu {runId}-111`, `Tegar Wibowo {runId}-111`)
75. Klik header kolom Temporary User
76. Verifikasi Temporary User klik 3 kembali ke default sort tabel Name A-Z: 3 baris pertama `Agus Prasetyo {runId}-111`, `Bagas Santoso {runId}-111`, `Citra Dewanti {runId}-111`
77. Klik header kolom Column Visibility (⋯)
78. Hilangkan centang kolom `Temporary User`
79. Hilangkan centang kolom `Temporary Until`
80. Tutup Overlay Column Visibility dengan menekan Esc
81. Ubah page size ke 10

### TC-GS-USER-715: Kombinasi Search + Filter + Sort + Pagination berjalan bersamaan

82. Klik icon Search, ketik `EMP`, tekan Enter
83. Verifikasi tabel menampilkan 19 baris dengan Employee ID terisi: halaman 1 berisi 10 baris dan total 2 halaman (`Lina Marlina {runId}-111` dan `Oka Saputra {runId}-111` dengan Employee ID kosong tidak tampil)
84. Klik icon Filter
85. Pilih opsi `Active` pada dropdown Status
86. Klik `[Apply]`
87. Verifikasi hasil = Search ∩ Filter: tabel menampilkan 16 baris berstatus `Active`: halaman 1 berisi 10 baris dan total 2 halaman
88. Klik header kolom Name
89. Klik header kolom Name
90. Verifikasi sort Name Z-A berlaku: 3 baris pertama `Umar Hakim {runId}-111`, `Tegar Wibowo {runId}-111`, `Sinta Dewi {runId}-111`
91. Ubah page size ke 25
92. Verifikasi page size 25 berlaku: tabel menampilkan 16 baris dalam satu halaman
93. Verifikasi Search tidak ter-reset: kotak Search tetap berisi `EMP`
94. Verifikasi Filter tidak ter-reset: jumlah baris tetap 16 (tanpa baris berstatus `Inactive`)
95. Verifikasi Sort tidak ter-reset: 3 baris pertama tetap `Umar Hakim {runId}-111`, `Tegar Wibowo {runId}-111`, `Sinta Dewi {runId}-111`
96. Klik icon ←
97. Klik icon Filter
98. Klik `[Clear Field]`
99. Klik `[Apply]`
100. Klik header kolom Name
101. Ubah page size ke 10

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Holder dan 21 Non-Login User dipenuhi spec ini lewat seeding di hook `before`; spec tidak menumpang spec lain.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 714 (Pagination), 692 sampai 696 (Sort), lalu 715 (kombinasi). TC-GS-USER-714 mulai pada page size default 10; sort 692 sampai 696 memakai page size 25 supaya seluruh 21 baris teramati pada satu halaman (kosong di akhir, kelompok Active/Inactive, kelompok tanggal); TC-GS-USER-715 kembali ke page size 10 karena langkah terakhirnya mengubah page size ke 25. Urutan di `tc-user.md`: 692 sampai 696, 714, 715.
- Langkah penghubung (aksi tanpa `Verifikasi`): pembukaan Tab (langkah 1 sampai 3); `Ubah page size ke 25` pada langkah 14 (mengatur ukuran halaman untuk blok Sort) dan `Ubah page size ke 10` pada langkah 81 serta di akhir spec; langkah 61 sampai 64 dan 77 sampai 80 (menampilkan dan menyembunyikan kolom curated, penutupan Overlay Column Visibility dengan Esc); dan langkah pembersihan di akhir TC-GS-USER-715 (icon ←, `Klik icon Filter`, `[Clear Field]`, `[Apply]`, klik header Name ketiga, page size 10).
- Sort default tabel adalah Name A-Z (PRD user.md §4.1.4), sehingga Name klik 1 menghasilkan urutan yang sama dengan default dan keduanya dibedakan lewat langkah klik yang bernomor. Pada kolom lain klik 3 dibedakan dari klik 1 lewat 3 baris pertama default (`Agus Prasetyo`, `Bagas Santoso`, `Citra Dewanti`).
- Asersi tambahan (S-03): TC-GS-USER-693 dan 694 memverifikasi baris kosong atau baris Inactive pada posisi ujung tabel; TC-GS-USER-695 memverifikasi nilai tanggal per kelompok baris; kolom Temporary Until memverifikasi urutan 5 baris yang memuat tanggal. Tanggal Temporary Until baris `Yes`: hari uji + 10 (`Putri Ayu`), + 20 (`Galih Permadi`), + 30 (`Tegar Wibowo`), + 40 (`Kartika Sari`), + 50 (`Bagas Santoso`).
- Pembagian TC lintas spec: TC-GS-USER-400 sampai 403 (screening Tab, navigasi) dan 671 sampai 677 (Search) ada di spec 108; TC-GS-USER-678 sampai 686 (Filter Panel) ada di spec 109; TC-GS-USER-687 sampai 691 (kombinasi Search dan Filter, Clear) ada di spec 110; TC-GS-USER-697 sampai 708 (Setup Column) ada di spec 112; TC-GS-USER-404 dan 709 sampai 713 (Download) ada di spec 113.
- Spec melewati sekitar 35 langkah (101 langkah) karena tujuh TC berbagi satu layar (Tab Non-Login User), satu dataset (21 Non-Login User milik spec), dan satu kelas harness (fungsional). TC-GS-USER-692 sampai 696 menguji sembilan kolom dengan pola identik (tiga klik header, tiga `Verifikasi`), tiap blok berdiri sendiri (kegagalan satu kolom tidak menghapus makna kolom lain), dan memakai Tab serta page size 25 yang sama; memisahkannya mengulang login, seeding 22 user, dan pembukaan Tab.
- Temuan untuk QA:
  - TC-GS-USER-692 sampai 696, 714, 715 menyebut tabel dan Name tanpa suffix; spec memakai holder dan Non-Login User milik spec bersuffix (S-06, S-11).
  - TC-GS-USER-693 Expected: `—` tetap di akhir pada Z-A, sedangkan prd-conventions.md §9.7 menyebut nilai kosong "di awal (descending)". PRD user.md §4.1.4 menyatakan "kosong → akhir" untuk kolom Employee ID dan Position; spec mengikuti TC dan PRD modul.
  - TC-GS-USER-695: Expected tidak menyebut posisi baris Temporary Until kosong; spec hanya mengasersi urutan 5 baris yang berisi tanggal. PRD user.md §4.1.4 menyatakan kosong di akhir.
  - TC-GS-USER-695: Last Update diturunkan dari waktu entri Changelog terbaru, sehingga mengatur dua tanggal berbeda pada seed tidak punya cara yang disebut TC, PRD, atau LLD; disediakan tim FE/BE.
  - TC-GS-USER-714: Data Uji "≥21 baris" dipenuhi 21 baris; pada page size 25 seluruh 21 baris tampil sehingga batas "maksimal 25 baris" teramati sebagai 21 baris pada satu halaman, bukan sebagai pemotongan di baris ke-25.
  - TC-GS-USER-715: langkah "Terapkan filter bila tersedia" dipenuhi Filter Status `Active` (Filter tersedia di tab ini); langkah "Sort kolom" memakai kolom Name Z-A; Search memakai `EMP` supaya hasil melebihi satu halaman pada page size 10.
  - TC-GS-USER-692 sampai 696: TC tidak menyatakan ukuran halaman untuk pengamatan; spec memakai page size 25 sebagai langkah penghubung.
  - Cara menutup Overlay Column Visibility tidak didefinisikan di TC maupun PRD; spec memakai Esc.
  - Mekanisme seeding Login User dan Non-Login User (Represented By, Employee ID, Position, Division, Temporary Until) dan penghapusan sisa tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
