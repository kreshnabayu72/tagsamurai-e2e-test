---
id: TC-GS-POS-E2E-001-screening-tabel-layout-urutan-default-dan-tooltip
title: "Screening Tab Position: Layout 3 Zona, Breadcrumb, Tooltip Ikon, Urutan Name A-Z, Nama 120 Karakter, Last Updated Seed, dan State Visual"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-1
  - TC-GS-POS-2
  - TC-GS-POS-3
  - TC-GS-POS-4
  - TC-GS-POS-5
  - TC-GS-POS-9
  - TC-GS-POS-291
  - TC-GS-POS-293
coverage:
  web: automated
---

# Screening Tab Position: Layout 3 Zona, Breadcrumb, Tooltip Ikon, Urutan Name A-Z, Nama 120 Karakter, Last Updated Seed, dan State Visual

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor:
  - Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1) untuk TC-GS-POS-1, 2, 3, 4, 5, 9, dan 293. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
  - Total Control Client Seed (Pre-setup 21) untuk TC-GS-POS-291: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_CLIENTSEED_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Email akun ini tidak tertulis di tabel Pre-setup TC (lihat Temuan untuk QA). Hook `after` mengembalikan sesi ke akun Total Control default suite.
- Layar awal: hook `beforeEach` suite membuka Global Settings > User > Position untuk akun Total Control (bagian 4 konvensi); spec ini tidak menguji navigasi sidebar sehingga tidak mengulang langkah buka kecuali sesudah ganti akun.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, tanpa suffix): Position 10 `IT Manager`, 11 `Finance Analyst`, 12 `Warehouse Supervisor`, 13 `Customer Success Manager`, 14 `Procurement Officer`, 15 `Field Technician`, 16 `Sales Coordinator`. Pre-setup 21 (Client Seed) memuat record seed `Head of Operations` dan record hasil Import Type "Position" `Field Technician` (precondition TC-GS-POS-291).
- Data Dinamis (di-seed lewat API di hook `before` pada entitas Total Control; nama bersuffix per run; fixture baru `Fixture.position.hrBusinessPartner001`, `Fixture.position.iosDeveloper001`, `Fixture.position.legalCounsel001`, `Fixture.position.name120Char001`):
  - D-01: `HR Business Partner {runId}-001`.
  - D-02: `iOS Developer {runId}-001`.
  - D-03: `Legal Counsel {runId}-001`; dipakai sebagai precondition TC (TC-GS-POS-1 c: tabel berisi minimal 11 record: 7 Pre-setup + 4 Data Dinamis), tidak diasersi.
  - D-04: nama 120 karakter yang diawali teks Data Uji TC-GS-POS-9 (`Senior Manager of Regional Supply Chain Planning, Procurement Strategy, ...`) dan dipotong dari belakang sehingga panjang total termasuk suffix ` {runId}-001` tepat 120 karakter.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position D-01 sampai D-04 yang masih ada.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true, lihat `suite.md`.
- Kemampuan teknis: hover; fokus keyboard (Tab); pembacaan teks sel termasuk panjang karakter; pembacaan gaya terhitung (background, border, ring fokus) untuk TC-GS-POS-293; ganti akun (logout lalu login).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`) dan sesi akun (dipulihkan hook `after` seperti di atas).

## Test Steps

### TC-GS-POS-1: Screening halaman Position, 3 zona tabel utama

1. Amati area header, body tabel, dan footer dari atas ke bawah tanpa mengisi atau mengklik apa pun
2. Verifikasi Header: Breadcrumb `User > Position`
3. Verifikasi Header: tombol `[?]` Guided Tooltip tampil di sebelah breadcrumb
4. Verifikasi Header: sub-tab `User List | Position (aktif) | Division | Custom Field`
5. Verifikasi Header: Table Tools rata kanan `Search | Filter | Download | Changelog | [+ Position]`
6. Verifikasi `[+ Position]` bergaya filled primary
7. Verifikasi `[+ Position]` memiliki icon AddLine
8. Verifikasi Body: header kolom `Checkbox | Name (sortable) | Last Updated (sortable) | Actions (⋯) (unsortable)`
9. Klik header kolom Actions (⋯)
10. Verifikasi Overlay Column Visibility terbuka
11. Tutup Overlay Column Visibility dengan menekan Esc
12. Verifikasi Body: sedikitnya satu baris data tampil di tabel
13. Verifikasi Body: setiap baris memiliki menu row action pada kolom Actions (⋯)
14. Verifikasi Body: baris tampil terurut Name A-Z
15. Verifikasi Body: tidak ada Page Title terpisah di bawah breadcrumb
16. Verifikasi Body: Filter Panel tidak tampil
17. Verifikasi Footer: pagination default menampilkan 10 baris pada halaman 1
18. Verifikasi Footer: pilihan ukuran halaman tampil
19. Verifikasi Footer: navigasi prev dan next tampil
20. Verifikasi Footer: nomor halaman tampil
21. Verifikasi Footer: input nomor halaman tampil

### TC-GS-POS-2: Breadcrumb halaman Position, teks dan segmen terminal

22. Arahkan kursor ke segmen `Position` pada breadcrumb
23. Verifikasi breadcrumb tampil persis `User > Position`
24. Verifikasi breadcrumb tidak diawali nama produk `Global Settings`
25. Verifikasi segmen terakhir `Position` hanya label (bukan link)
26. Klik segmen `Position`
27. Verifikasi klik segmen `Position` tidak mengubah halaman
28. Verifikasi tombol `[?]` tampil di sebelah breadcrumb

### TC-GS-POS-3: Breadcrumb halaman Position, segmen User tidak bisa diklik

29. Verifikasi segmen `User` tampil sebagai label statis (bukan link)
30. Klik segmen `User` pada breadcrumb
31. Verifikasi klik segmen `User` tidak berpindah halaman
32. Verifikasi tab Position tetap aktif

### TC-GS-POS-4: Tooltip ikon Table Tools dan header Column Visibility tabel utama

33. Arahkan kursor ke ikon Search
34. Verifikasi tooltip "Search"
35. Arahkan kursor ke ikon Filter
36. Verifikasi tooltip "Filter"
37. Arahkan kursor ke ikon Download
38. Verifikasi tooltip "Download"
39. Arahkan kursor ke ikon Changelog
40. Verifikasi tooltip "Changelog"
41. Arahkan kursor ke ikon `⋯` pada header kolom Actions
42. Verifikasi tooltip "Column Visibility"
43. Pindahkan kursor keluar dari Table Tools dan header tabel
44. Tekan Tab hingga fokus keyboard berada pada ikon Search
45. Verifikasi tooltip "Search"
46. Tekan Tab hingga fokus keyboard berada pada ikon Filter
47. Verifikasi tooltip "Filter"
48. Tekan Tab hingga fokus keyboard berada pada ikon Download
49. Verifikasi tooltip "Download"
50. Tekan Tab hingga fokus keyboard berada pada ikon Changelog
51. Verifikasi tooltip "Changelog"
52. Tekan Tab hingga fokus keyboard berada pada ikon `⋯` pada header kolom Actions
53. Verifikasi tooltip "Column Visibility"

### TC-GS-POS-5: Urutan default tabel Position, Name A-Z case-insensitive

54. Klik area kosong halaman untuk melepas fokus keyboard
55. Amati urutan baris kolom Name halaman 1 tanpa menyentuh header sort
56. Verifikasi baris terurut Name ascending case-insensitive (collation en-US): `HR Business Partner {runId}-001`, lalu `iOS Developer {runId}-001`, lalu `IT Manager`
57. Verifikasi tidak ada indikator panah sort aktif pada header Name
58. Verifikasi tidak ada indikator panah sort aktif pada header Last Updated

### TC-GS-POS-9: Nama Position 120 karakter tampil utuh di tabel

59. Ketik Search nama Position D-04 (120 karakter), tekan Enter
60. Verifikasi sel Name baris D-04 menampilkan nama utuh 120 karakter
61. Verifikasi nama tidak dipotong
62. Verifikasi nama tidak memakai `..`/ellipsis
63. Verifikasi nama wrap natural
64. Arahkan kursor ke sel Name baris D-04
65. Verifikasi hover tidak memunculkan tooltip
66. Klik `(←)` pada kotak Search (menutup input dan mereset tabel)

### TC-GS-POS-293: State visual komponen tabel dan form Position

67. Arahkan kursor ke baris pertama tabel
68. Verifikasi baris menampilkan background hover
69. Centang checkbox baris pertama
70. Verifikasi baris menampilkan background selected
71. Hapus centang checkbox baris pertama
72. Arahkan kursor ke `[+ Position]`
73. Verifikasi `[+ Position]` menampilkan background primary hover
74. Pindahkan kursor keluar dari `[+ Position]`
75. Tekan Tab hingga fokus keyboard berada pada `[+ Position]`
76. Verifikasi `[+ Position]` menampilkan focus ring
77. Klik `[+ Position]`
78. Arahkan kursor ke input Position Name
79. Verifikasi input Position Name menampilkan border primary
80. Klik input Position Name
81. Verifikasi input Position Name menampilkan ring focus primary
82. Tutup modal dengan klik `✕` di header

### TC-GS-POS-291: Last Updated terisi untuk record seed dan hasil Import

83. Ganti akun: logout dari akun Total Control
84. Login sebagai Total Control Client Seed (Pre-setup 21) dengan `Spectra.env.GS_CLIENTSEED_TC_PASSWORD`
85. Buka Global Settings > User > Position
86. Amati sel Last Updated baris `Head of Operations` dan baris `Field Technician`
87. Verifikasi Last Updated baris `Head of Operations` berupa tanggal-waktu record dibuat (bukan `—` atau kosong)
88. Verifikasi Last Updated baris `Field Technician` berupa tanggal-waktu record dibuat (bukan `—` atau kosong)
89. Klik header Last Updated
90. Klik header Last Updated sekali lagi
91. Verifikasi header Last Updated menunjukkan sort Newest First
92. Verifikasi urutan baris `Head of Operations` dan `Field Technician` sesuai Last Updated masing-masing dengan yang terbaru di atas

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 1, 2, 3, 4, 5, 9, 293, 291. TC-GS-POS-5 (tanpa menyentuh header sort) ditaruh sebelum langkah apa pun yang mengubah sort; TC-GS-POS-293 membuka form kosong dan menutupnya sebagai kejadian terakhir pada akun Total Control; TC-GS-POS-291 ditaruh terakhir karena butuh ganti akun ke Client Seed. Urutan ini menyimpang dari urutan TC sumber demi satu sesi akun sebelum ganti akun. Form Create dibuka sekali dan ditutup sekali.
- Pembukaan Global Settings > User > Position untuk akun Total Control dilakukan hook `beforeEach` dan dipakai bersama oleh TC-GS-POS-1 sampai 5, 9, dan 293; tidak ada pembukaan ulang sebelum ganti akun.
- TC-GS-POS-1 pada langkah 9 sampai 11 menambah pengecekan klik header Actions (⋯) karena Expected Result TC mendeskripsikan perilaku klik header itu (membuka Overlay Column Visibility). Perilaku isi Overlay diuji di spec Column Visibility tabel utama.
- TC-GS-POS-1 langkah 12 (baris pembanding: sedikitnya satu baris data tampil di tabel) adalah asersi tambahan sebagai anchor positif agar langkah 13 ("setiap baris memiliki menu row action") tidak lulus pada tabel kosong; langkah ini tidak ada di Expected TC-GS-POS-1 (S-03).
- Kolom `⋯` tabel utama bernama "Actions (⋯)" di TC-GS-POS-1 dan TC-GS-POS-4 (langkah 8, 9, dan 13 memakai "Actions (⋯)"; langkah 41 dan 52 memakai "header kolom Actions"); tooltip header kolom itu "Column Visibility" dan overlay yang terbuka saat header diklik bernama Overlay Column Visibility.
- TC-GS-POS-5: nama `HR Business Partner` dan `iOS Developer` bersuffix `{runId}-001` (Data Dinamis bersuffix); urutan relatif terhadap `IT Manager` (Pre-setup 10) tidak berubah oleh suffix.
- TC-GS-POS-9: panjang 120 karakter sudah termasuk suffix ` {runId}-001`; suffix tidak mengubah batas yang diuji.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 11 (tutup Overlay Column Visibility dengan Esc), langkah 59 (Ketik Search agar baris D-04 tampil di halaman aktif) dan langkah 66 (klik `(←)` pada kotak Search untuk menutup input dan mereset tabel), langkah penghubung pelepasan fokus dan kursor pada TC-GS-POS-4 serta 5, penghapusan centang checkbox, dan penutupan modal pada TC-GS-POS-293.
- Spec melewati sekitar 35 langkah (92 langkah, sebagian besar pasangan aksi hover atau fokus dan `Verifikasi` pada TC-GS-POS-4 dan 293). Seluruhnya satu kelas (screening baca tabel Position, tidak ada aksi yang mengubah data), tiap blok TC berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain; satu-satunya blok pada akun lain (TC-GS-POS-291) berada di akhir dengan langkah ganti akun eksplisit.
- Temuan untuk QA:
  - TC-GS-POS-5 tidak menyebut halaman tempat ketiga baris berada; spec mengasumsikan ketiganya di halaman 1 (jumlah record yang namanya mendahului `IT Manager` kecil).
  - TC-GS-POS-293 tidak menyebut nilai warna; spec mengasersi keberadaan state (hover, selected, focus ring, border primary) tanpa nilai warna.
  - TC-GS-POS-291 tidak menyebut halaman tempat `Head of Operations` dan `Field Technician` berada; spec mengasumsikan keduanya di halaman 1 (jumlah record Client Seed tidak diketahui spec).
  - TC-GS-POS-291 berstatus Manual Only di TC tetapi tetap ditulis (konvensi bagian 2). Precondition menyebut `Field Technician` (Pre-setup 15) berada di entitas Client Seed, sedangkan Pre-setup 15 tidak dikaitkan dengan Client Seed; email akun Total Control Client Seed tidak tertulis di Pre-setup 21 dan env var `GS_CLIENTSEED_TC_PASSWORD` baru.
