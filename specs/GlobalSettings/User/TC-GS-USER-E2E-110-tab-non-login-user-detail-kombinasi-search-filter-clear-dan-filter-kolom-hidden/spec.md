---
id: TC-GS-USER-E2E-110-tab-non-login-user-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden
title: "Tab Non-Login User Detail: kombinasi Search dan Filter, Clear, filter kolom hidden, nol baris"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-687
  - TC-GS-USER-688
  - TC-GS-USER-689
  - TC-GS-USER-690
  - TC-GS-USER-691
coverage:
  web: automated
---

# Tab Non-Login User Detail: kombinasi Search dan Filter, Clear, filter kolom hidden, nol baris

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup; satu-satunya state yang diubah adalah visibilitas kolom `Division` (dipulihkan).
- Akun: Total Control, `Siti Nurhaliza`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Master Data Position (`Finance Manager`, `Staff`, `Supervisor`, `Internal Auditor`) dan Division (`Finance`, `General Affairs`, `Legal`) Pre-setup No. 22 dan 23 sebagai nilai seed.
- Data Dinamis, holder: Login User milik spec `Ahmad Fauzi {runId}-110` (email `ahmadfauzi+{runId}-110@qwertysystem.net`, status Activated, Access Global Settings) sebagai Represented By seluruh Non-Login User di bawah. Holder milik spec dipakai, bukan `Ahmad Fauzi` Pre-setup (Tabel Data Uji Pre-setup No. 13) beserta `Agus Prasetyo` dan `Lina Marlina` Pre-setup (No. 21), karena S-06 melarang mengubah data Pre-setup bersama dan S-11 menuntut data dengan lebih dari satu halaman serta sedikitnya dua nilai distinct pada kolom yang diuji.
- Data Dinamis, 12 Non-Login User milik spec (Represented By = `Ahmad Fauzi {runId}-110`), di-seed di hook `before`. Tabel memuat 12 baris: halaman 1 berisi 10 baris dan total 2 halaman. Nilai Name, Email, dan Employee ID bersuffix `{runId}-110`. `{U1}` dan `{U2}` pada kolom Temporary Until adalah tanggal hari uji + 30 hari dan hari uji + 60 hari, ditampilkan dalam Date Format General Settings.
  | Name | Email | Employee ID | Position | Division | Active | Temporary User | Temporary Until |
  |---|---|---|---|---|---|---|---|
  | `Agus Prasetyo {runId}-110` | `nlu01+{runId}-110@qwertysystem.net` | `EMP-AGS-{runId}-110` | Finance Manager | Finance | Active | No | kosong |
  | `Bagas Santoso {runId}-110` | `nlu02+{runId}-110@qwertysystem.net` | `EMP-BGS-{runId}-110` | Staff | General Affairs | Active | No | kosong |
  | `Citra Dewanti {runId}-110` | `nlu03+{runId}-110@qwertysystem.net` | `EMP-CTR-{runId}-110` | Supervisor | Finance | Active | Yes | `{U1}` (hari uji + 30 hari) |
  | `Dimas Pranoto {runId}-110` | `nlu04+{runId}-110@qwertysystem.net` | `EMP-DMS-{runId}-110` | Staff | General Affairs | Active | No | kosong |
  | `Eka Wulandari {runId}-110` | `nlu05+{runId}-110@qwertysystem.net` | `EMP-EKA-{runId}-110` | Finance Manager | Legal | Active | No | kosong |
  | `Fitri Handayani {runId}-110` | `nlu06+{runId}-110@qwertysystem.net` | `EMP-FTR-{runId}-110` | Internal Auditor | Finance | Active | Yes | `{U2}` (hari uji + 60 hari) |
  | `Galih Permadi {runId}-110` | `nlu07+{runId}-110@qwertysystem.net` | `EMP-GLH-{runId}-110` | Staff | Legal | Active | No | kosong |
  | `Hana Kusuma {runId}-110` | `nlu08+{runId}-110@qwertysystem.net` | `EMP-HNA-{runId}-110` | Supervisor | General Affairs | Active | No | kosong |
  | `Lina Marlina {runId}-110` | `nlu09+{runId}-110@qwertysystem.net` | kosong | kosong | Legal | Inactive | No | kosong |
  | `Nadia Rahma {runId}-110` | `nlu10+{runId}-110@qwertysystem.net` | `EMP-NDR-{runId}-110` | Staff | Finance | Active | No | kosong |
  | `Rizky Fadillah {runId}-110` | `nlu11+{runId}-110@qwertysystem.net` | `EMP-RZK-{runId}-110` | Finance Manager | General Affairs | Inactive | No | kosong |
  | `Wahyu Hidayat {runId}-110` | `nlu12+{runId}-110@qwertysystem.net` | `EMP-WHY-{runId}-110` | Supervisor | Legal | Active | No | kosong |

  Position dan Division di atas memberi dua nilai atau lebih pada kolom yang dipakai Search dan Filter (Position: 4 nilai; Division: 3 nilai).
- Kemampuan teknis (disediakan tim FE/BE; endpoint ditentukan tim FE di tahap script): seeding Login User holder dan Non-Login User dengan Represented By = holder lewat API di hook `before`; cleanup di hook `after` menghapus Non-Login User lalu holder lewat API tanpa berasumsi seeding berhasil penuh. Seeding menambah 13 user pada hitungan Master Data Count Limit gabungan Login + Non-Login User; nilai limit environment cukup besar untuk itu.
- Data uji per TC: TC-GS-USER-687 Search `Supervisor` + Filter Division `General Affairs`; TC-GS-USER-688 Filter Division `Legal` + Search `Supervisor`; TC-GS-USER-689 Search `Staff`, sort Name, Filter Division `Legal`; TC-GS-USER-690 Filter Division `Finance` lalu hide kolom `Division`; TC-GS-USER-691 Search `Auditor` + Filter Division `Legal` (irisan kosong).
- Date Format General Settings default environment (`DD/MM/YY`); spec tidak mengubahnya.
- Preferensi kolom tersimpan di browser (PRD prd-conventions.md §9.3); hook `after` mengembalikan preferensi kolom Tab Non-Login User ke default.
- State yang diubah dan dipulihkan: Filter Panel dikosongkan dengan `[Clear Field]` dan `[Apply]`, Search ditutup dengan icon ←, sort Name dikembalikan ke default, kolom `Division` dicentang kembali (langkah 56 sampai 58); hook `after` sebagai cadangan.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`). Spec tidak mengubah data Pre-setup bersama (S-06).
- Kemampuan teknis: membaca warna icon Filter (gelap saat filter aktif); menekan Esc untuk menutup Overlay Column Visibility.

## Test Steps

1. Klik icon Search, ketik `Ahmad Fauzi {runId}-110`, tekan Enter
2. Klik Name `Ahmad Fauzi {runId}-110` di User List
3. Klik Tab `Non-Login User`

### TC-GS-USER-687: Search lalu Filter menghasilkan irisan

4. Klik icon Search, ketik `Supervisor`, tekan Enter
5. Verifikasi tabel hanya menampilkan 3 baris dengan Position `Supervisor`: `Citra Dewanti {runId}-110`, `Hana Kusuma {runId}-110`, `Wahyu Hidayat {runId}-110`
6. Klik icon Filter
7. Pilih opsi `General Affairs` pada dropdown Division
8. Klik `[Apply]`
9. Verifikasi hasil = Search ∩ Filter: tabel hanya menampilkan baris `Hana Kusuma {runId}-110`
10. Verifikasi keyword tidak ter-reset: kotak Search tetap berisi `Supervisor`
11. Klik icon Filter
12. Klik `[Clear Field]`
13. Klik `[Apply]`
14. Klik icon ←

### TC-GS-USER-688: Filter lalu Search menghasilkan irisan

15. Klik icon Filter
16. Pilih opsi `Legal` pada dropdown Division
17. Klik `[Apply]`
18. Verifikasi tabel hanya menampilkan 4 baris dengan Division `Legal`: `Eka Wulandari {runId}-110`, `Galih Permadi {runId}-110`, `Lina Marlina {runId}-110`, `Wahyu Hidayat {runId}-110`
19. Klik icon Search, ketik `Supervisor`, tekan Enter
20. Verifikasi hasil = Filter ∩ Search: tabel hanya menampilkan baris `Wahyu Hidayat {runId}-110`
21. Verifikasi filter tetap aktif: icon Filter berwarna gelap
22. Klik icon Filter
23. Klik `[Clear Field]`
24. Klik `[Apply]`
25. Klik icon ←

### TC-GS-USER-689: Clear filter saat Search dan Sort aktif

26. Klik icon Search, ketik `Staff`, tekan Enter
27. Verifikasi tabel hanya menampilkan 4 baris dengan Position `Staff`: `Bagas Santoso {runId}-110`, `Dimas Pranoto {runId}-110`, `Galih Permadi {runId}-110`, `Nadia Rahma {runId}-110`
28. Klik header kolom Name
29. Klik header kolom Name
30. Verifikasi sort Name Z-A: urutan baris `Nadia Rahma {runId}-110`, `Galih Permadi {runId}-110`, `Dimas Pranoto {runId}-110`, `Bagas Santoso {runId}-110`
31. Klik icon Filter
32. Pilih opsi `Legal` pada dropdown Division
33. Klik `[Apply]`
34. Verifikasi hasil = Search ∩ Filter: tabel hanya menampilkan baris `Galih Permadi {runId}-110`
35. Klik icon Filter
36. Klik `[Clear Field]`
37. Klik `[Apply]`
38. Verifikasi keyword tetap aktif: kotak Search tetap berisi `Staff`
39. Verifikasi arah sort tetap aktif: urutan baris Z-A `Nadia Rahma {runId}-110`, `Galih Permadi {runId}-110`, `Dimas Pranoto {runId}-110`, `Bagas Santoso {runId}-110`
40. Verifikasi filter terlepas: icon Filter tidak berwarna gelap
41. Klik icon ←
42. Klik header kolom Name

### TC-GS-USER-690: Filter tetap tersedia untuk kolom yang di-hide

43. Klik icon Filter
44. Pilih opsi `Finance` pada dropdown Division
45. Klik `[Apply]`
46. Verifikasi tabel hanya menampilkan 4 baris dengan Division `Finance`: `Agus Prasetyo {runId}-110`, `Citra Dewanti {runId}-110`, `Fitri Handayani {runId}-110`, `Nadia Rahma {runId}-110`
47. Klik header kolom Column Visibility (⋯)
48. Hilangkan centang kolom `Division`
49. Tutup Overlay Column Visibility dengan menekan Esc
50. Verifikasi kolom `Division` tidak tampil di tabel
51. Verifikasi filter tetap aktif menyaring: tabel tetap hanya menampilkan `Agus Prasetyo {runId}-110`, `Citra Dewanti {runId}-110`, `Fitri Handayani {runId}-110`, `Nadia Rahma {runId}-110`
52. Klik icon Filter
53. Verifikasi field `Division` tetap ada di Filter Panel
54. Klik `[Clear Field]`
55. Klik `[Apply]`
56. Klik header kolom Column Visibility (⋯)
57. Centang kolom `Division`
58. Tutup Overlay Column Visibility dengan menekan Esc

### TC-GS-USER-691: Kombinasi Search + Filter menghasilkan 0 baris lalu pulih saat salah satu dilepas

59. Klik icon Search, ketik `Auditor`, tekan Enter
60. Verifikasi tabel hanya menampilkan baris `Fitri Handayani {runId}-110` (Position `Internal Auditor`, Division `Finance`)
61. Klik icon Filter
62. Pilih opsi `Legal` pada dropdown Division
63. Klik `[Apply]`
64. Verifikasi ilustrasi empty filtered state tampil
65. Verifikasi judul empty filtered state `No results found`
66. Verifikasi deskripsi empty filtered state `Try adjusting your search or filter.`
67. Klik icon Filter
68. Klik `[Clear Field]`
69. Klik `[Apply]`
70. Verifikasi setelah filter dilepas, baris hasil search tampil kembali: `Fitri Handayani {runId}-110`
71. Klik icon ←

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Holder dan 12 Non-Login User dipenuhi spec ini lewat seeding di hook `before`; spec tidak menumpang spec lain.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (687 sampai 691) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): pembukaan Tab (langkah 1 sampai 3); `Klik icon Filter`, `[Clear Field]`, dan `[Apply]` sesudah tiap `Verifikasi` hasil filter, serta `Klik icon ←` (menutup Search dan mereset tabel), supaya TC berikutnya mulai tanpa Search dan Filter aktif; klik header Name ketiga sesudah TC-GS-USER-689 (mengembalikan sort ke default); langkah 56 sampai 58 (membuka Overlay Column Visibility, mencentang kolom `Division`, menutup overlay). Penutupan Overlay Column Visibility memakai Esc.
- Langkah `Klik icon Filter` dituliskan sebelum `[Clear Field]` sesudah tiap `[Apply]`: panel Filter ditutup oleh `[Apply]` dan icon Filter dipakai untuk membukanya kembali.
- Urutan klik pada TC-GS-USER-689: sort Name diklik dua kali (Z-A) sebelum Filter diterapkan supaya arah sort teramati pada empat baris hasil Search dan tetap teramati setelah Filter dilepas. Sort default tabel adalah Name A-Z (PRD user.md §4.1.4), sehingga klik pertama (A-Z) tidak mengubah urutan dan tidak diasersi.
- Anchor positif (S-03, bagian 8b butir 2): `Verifikasi` hasil Search (TC-GS-USER-687, 689, 691) dan hasil Filter (TC-GS-USER-688, 690) mendahului asersi irisan; `Verifikasi` baris hasil search sebelum Filter pada TC-GS-USER-691 mendahului asersi empty filtered state.
- Pembagian TC lintas spec: TC-GS-USER-400 sampai 403 (screening Tab, navigasi) dan 671 sampai 677 (Search) ada di spec 108; TC-GS-USER-678 sampai 686 (Filter Panel) ada di spec 109; TC-GS-USER-692 sampai 696, 714, dan 715 (Sort, Pagination, kombinasi empat kontrol) ada di spec 111; TC-GS-USER-697 sampai 708 (Setup Column) ada di spec 112; TC-GS-USER-404 dan 709 sampai 713 (Download) ada di spec 113.
- Spec melewati sekitar 35 langkah (71 langkah) karena lima TC kombinasi berbagi satu layar (Tab Non-Login User), satu dataset (12 Non-Login User milik spec), dan satu kelas harness (fungsional). Tiap blok memakai Search dan Filter pada Tab yang sama dan berdiri sendiri (kegagalan satu blok tidak menghapus makna blok lain); memisahkannya mengulang login, seeding 13 user, dan pembukaan Tab. Langkah `Klik icon Filter`, `[Clear Field]`, `[Apply]` yang berulang adalah prefix pembersihan.
- Temuan untuk QA:
  - TC-GS-USER-687 sampai 691 menyebut tabel dan Name tanpa suffix; spec memakai holder dan Non-Login User milik spec bersuffix (S-06, S-11).
  - TC-GS-USER-687 sampai 691: TC menyebut "keyword" dan "filter" tanpa nilai; spec memakai keyword dan opsi pada bagian Data uji per TC di Prerequisites.
  - TC-GS-USER-688 Expected b: "Filter tetap aktif" tidak menyebut cara mengamati; spec mengasersi icon Filter berwarna gelap (sama dengan TC-GS-USER-680 di spec 109).
  - TC-GS-USER-689: TC tidak menyebut kolom Sort; spec memakai kolom Name (sort default A-Z, dua klik menghasilkan Z-A).
  - TC-GS-USER-690: TC tidak menyatakan apakah Filter Panel menutup sesudah `[Apply]`; spec membuka kembali lewat icon Filter.
  - Cara menutup Overlay Column Visibility tidak didefinisikan di TC maupun PRD; spec memakai Esc.
  - Mekanisme seeding Login User dan Non-Login User (Represented By, Employee ID, Position, Division, Temporary Until) dan penghapusan sisa tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
