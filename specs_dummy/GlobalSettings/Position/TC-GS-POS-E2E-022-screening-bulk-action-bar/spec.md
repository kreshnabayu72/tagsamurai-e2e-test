---
id: TC-GS-POS-E2E-022-screening-bulk-action-bar
title: Screening struktur Bulk Action Bar, seleksi lintas halaman, dan batas 1000 baris
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-26
  - TC-GS-POS-199
  - TC-GS-POS-236
  - TC-GS-POS-239
  - TC-GS-POS-240
coverage:
  web: automated
---

# Screening struktur Bulk Action Bar, seleksi lintas halaman, dan batas 1000 baris

## Prerequisites

- Aktor adalah `Fixture.globalSettingsPosition.actors.totalControl`, yaitu Role Total Control yang
  memegang capability Manage user and role dengan huruf C, U, dan D. Kolom checkbox dan Bulk Action Bar
  hanya tampil bagi role yang memegang capability Delete.
- `Fixture.globalSettingsPosition.bulkActionBar.screened.targets` adalah beberapa Position bebas relasi
perubahan seleksi, dan status
- `Fixture.globalSettingsPosition.pagination.defaultPageSize` adalah ukuran halaman default, yaitu `10`.
- `Fixture.globalSettingsPosition.pagination.crossPage.totalFiltered` adalah total Position pada tenant
  uji paging, yaitu lebih dari sepuluh sehingga mencakup beberapa halaman.
- `Fixture.globalSettingsPosition.pagination.crossPage.totalFirstPage` adalah jumlah baris pada halaman
  aktif pertama, yaitu sepuluh.
- `Fixture.globalSettingsPosition.limits.selectionLimit` adalah batas seleksi platform, yaitu `1000`.
- `Fixture.globalSettingsPosition.positions.selectionLimit.oversizedCount` adalah jumlah Position pada
  tenant uji batas seleksi, yaitu lebih dari seribu.
- `Fixture.globalSettingsPosition.positions.selectionLimit.oversizedFilteredCount` adalah jumlah baris
  yang akan ter-filter saat uji auto-cap, yaitu `1500`.
- `Fixture.globalSettingsPosition.captions.bulkActionBar.counter.one` adalah counter untuk satu baris,
  yaitu `1 position selected`.
- `Fixture.globalSettingsPosition.captions.bulkActionBar.counter.many` adalah counter untuk lebih dari satu
  baris, yaitu `{N} positions selected`.
- `Fixture.globalSettingsPosition.captions.bulkActionBar.selectAll` adalah tombol Server Select All, yaitu
  `Select All ({N} records)`.
- `Fixture.globalSettingsPosition.captions.bulkActionBar.unselectAll` adalah bentuk toggle saat seluruh
  data terpilih, yaitu `Unselect All`.
- `Fixture.globalSettingsPosition.captions.bulkActionBar.selectionLimitTooltip` adalah tooltip live-block,
  yaitu `You have reached the maximum selection of 1000 rows.`
- `Fixture.globalSettingsPosition.captions.toast.selectionAutoCap` adalah toast auto-cap, yaitu
  `Error, only the first 1000 of 1500 rows were selected. Narrow your filter to include the rest.`
- PRD §4.2 merender Bulk Action Bar dengan urutan ringkas `counter | [Delete] | [✕]`. Konvensi platform
  `prd-conventions.md` menetapkan urutan baku dari kiri ke kanan, yaitu Bulk Action, counter,
  `Select All ({N} records)`, lalu ikon `✕`. Spec ini memakai urutan baku dari konvensi, dan perbedaan
  dengan wireframe PRD dicatat di dokumen coverage.
- Konvensi platform membedakan dua mekanisme yang sering tertukar. Checkbox header hanya menyentuh baris
  pada halaman aktif, sedangkan tombol `Select All ({N} records)` melakukan query ke server dan menyentuh
  seluruh baris yang cocok dengan filter aktif lintas halaman.
- Konvensi platform juga menetapkan bahwa seleksi bertahan melewati pagination, search, filter, dan sort,
  serta bulk action bekerja pada total seleksi dan bukan hanya baris yang sedang terlihat.
- Dua subbagian terakhir butuh tenant dengan lebih dari seribu Position. Jumlah itu disiapkan tim FE di
  environment otomasi, dan FE sudah mencatat keterbatasan resource untuk menjalankan dua tenant
  besar itu sekaligus.
- Subbagian dipisah karena batas seleksi memakai tenant dengan data berbeda dari subbagian paging, dan
  mencampurnya akan membuat pengukuran become tidak terisolasi.

## Test Steps

### Struktur bar, siklus counter, select all, dan clear selection

1. Verifikasi tidak ada Bulk Action Bar yang tampil pada kondisi awal
2. Verifikasi kolom checkbox pada tabel tampil, karena role ini memegang capability Delete
3. Verifikasi tabel memuat `Fixture.globalSettingsPosition.bulkActionBar.screened.targets` pada halaman
   aktif
4. Verifikasi checkbox header tampil dalam keadaan unchecked
5. Centang checkbox pada baris pertama dari
   `Fixture.globalSettingsPosition.bulkActionBar.screened.targets`
6. Verifikasi Bulk Action Bar muncul
7. Verifikasi urutan elemen pada bar dari kiri ke kanan adalah Bulk Action, counter, tombol
   `Select All ({N} records)`, lalu ikon `✕`
8. Verifikasi counter menampilkan
   `Fixture.globalSettingsPosition.captions.bulkActionBar.counter.one`
9. Verifikasi counter memakai bentuk singular untuk satu baris terpilih
10. Verifikasi ikon `✕` berada di ujung kanan bar
11. Centang checkbox pada baris kedua dari
    `Fixture.globalSettingsPosition.bulkActionBar.screened.targets`
12. Verifikasi counter berubah menjadi bentuk jamak dari
    `Fixture.globalSettingsPosition.captions.bulkActionBar.counter.many`
13. Verifikasi angka pada counter sama dengan jumlah baris yang tercentang
14. Kosongkan checkbox pada baris pertama
15. Verifikasi counter berkurang kembali menjadi
    `Fixture.globalSettingsPosition.captions.bulkActionBar.counter.one`
16. Verifikasi baris kedua tetap tercentang
17. Verifikasi checkbox pada baris pertama tidak ikut tercentang kembali
18. Verifikasi tombol `Select All` pada bar menampilkan angka yang sama dengan total baris yang cocok
    dengan filter aktif
19. Klik tombol `Select All ({N} records)` pada bar
20. Verifikasi seluruh baris pada halaman aktif tercentang
21. Verifikasi counter menampilkan seluruh total data, bukan hanya baris di halaman aktif
22. Verifikasi tombol `Select All` berubah menjadi
    `Fixture.globalSettingsPosition.captions.bulkActionBar.unselectAll`
23. Verifikasi tombol yang muncul adalah pengubah state, bukan tombol yang hilang total
24. Klik ikon `✕` pada ujung kanan bar
25. Verifikasi Bulk Action Bar langsung hilang
26. Verifikasi seluruh checkbox baris kembali unchecked
27. Verifikasi checkbox header kembali unchecked
28. Verifikasi tidak ada seleksi yang tersisa di halaman lain, sehingga `✕` benar-benar membersihkan
    seluruh seleksi

### Checkbox header hanya menyentuh halaman aktif

29. Verifikasi tabel memuat `Fixture.globalSettingsPosition.pagination.crossPage.totalFirstPage` baris
    pada halaman aktif
30. Verifikasi ada halaman berikutnya pada kontrol paginasi
31. Centang checkbox pada header kolom
32. Verifikasi seluruh baris pada halaman aktif tercentang
33. Verifikasi checkbox header berstatus checked
34. Verifikasi Bulk Action Bar muncul dengan counter sebesar
    `Fixture.globalSettingsPosition.pagination.crossPage.totalFirstPage`
35. Verifikasi counter tidak sama dengan total seluruh data, karena checkbox header hanya
    menyentuh halaman aktif
36. Verifikasi checkbox header tidak berstatus Indeterminate pada kondisi seluruh halaman aktif tercentang
37. Kosongkan checkbox pada header kolom
38. Verifikasi seluruh checkbox baris pada halaman aktif kembali unchecked
39. Verifikasi checkbox header kembali unchecked
40. Verifikasi Bulk Action Bar langsung hilang
41. Verifikasi seleksi pada halaman lain tidak tersentuh, karena halaman lain memang tidak diseleksi
42. Centang hanya satu checkbox pada baris data
43. Verifikasi checkbox header berstatus Indeterminate dengan ikon strip minus `[-]`, bukan checked dan
    bukan unchecked
44. Verifikasi Bulk Action Bar menampilkan counter
    `Fixture.globalSettingsPosition.captions.bulkActionBar.counter.one`
45. Verifikasi baris lain tetap unchecked

### Server Select All lintas halaman

46. Verifikasi jumlah total yang cocok dengan filter aktif adalah
    `Fixture.globalSettingsPosition.pagination.crossPage.totalFiltered`
47. Verifikasi jumlah total itu lebih besar dari
    `Fixture.globalSettingsPosition.pagination.crossPage.totalFirstPage`
48. Centang satu checkbox pada baris untuk memunculkan bar
49. Verifikasi tombol pada bar menampilkan
    `Fixture.globalSettingsPosition.captions.bulkActionBar.selectAll` dengan angka yang sama dengan
    `Fixture.globalSettingsPosition.pagination.crossPage.totalFiltered`
50. Klik tombol `Select All ({N} records)`
51. Verifikasi seluruh baris pada halaman aktif tercentang
52. Verifikasi baris pada halaman berikutnya juga tercentang setelah pindah halaman
53. Verifikasi checkbox header pada halaman berikutnya berstatus checked
54. Verifikasi counter pada bar tetap menampilkan total seluruh data
55. Verifikasi tombol pada bar berubah menjadi
    `Fixture.globalSettingsPosition.captions.bulkActionBar.unselectAll`
56. Klik tombol tersebut
57. Verifikasi seluruh seleksi lintas halaman dibatalkan
58. Verifikasi Bulk Action Bar langsung hilang
59. Verifikasi checkbox pada halaman berikutnya kembali unchecked
60. Centang satu checkbox pada baris lagi
61. Klik tombol `Select All ({N} records)`
62. Verifikasi tombol berubah menjadi `Unselect All`
63. Kosongkan checkbox pada satu baris di halaman aktif
64. Verifikasi tombol kembali menjadi
    `Fixture.globalSettingsPosition.captions.bulkActionBar.selectAll`
65. Verifikasi counter turun satu, sesuai jumlah baris yang tersisa tercentang
66. Verifikasi baris yang di-uncheck tetap tidak tercentang

melewati paginasi, pencarian, filter, dan pengurutan

67. Verifikasi ada minimal dua baris tercentang pada halaman aktif
68. Verifikasi counter menampilkan jumlah seleksi saat ini
69. Pindah ke halaman berikutnya
70. Verifikasi baris yang tercentang di halaman sebelumnya tetap tercatat pada counter
71. Pindah kembali ke halaman sebelumnya
72. Verifikasi baris yang tercentang masih tercentang setelah pindah halaman
73. Verifikasi checkbox header pada halaman sebelumnya masih sesuai dengan kondisi seleksi di halaman itu
74. Pindah kembali ke tab Position lewat navigasi biasa
75. Verifikasi seleksi tetap bertahan setelah keluar dari tab dan masuk lagi
76. Verifikasi Bulk Action Bar tidak tiba-tiba hilang tanpa ada aksi dari user

### Live-block seleksi manual pada baris ke-1001

77. Verifikasi tenant aktif memuat
    `Fixture.globalSettingsPosition.positions.selectionLimit.oversizedCount`
78. Verifikasi jumlah itu lebih besar dari `Fixture.globalSettingsPosition.limits.selectionLimit`
79. Verifikasi tidak ada filter aktif, supaya yang diuji adalah limit absolut dan bukan limit dari
    hasil filter
80. Centang checkbox satu per satu sampai jumlah seleksi mencapai
    `Fixture.globalSettingsPosition.limits.selectionLimit`
81. Verifikasi seluruh checkbox yang dicentang sampai batas tetap checked
82. Verifikasi Bulk Action Bar tetap tampil dan counter menunjukkan
    `Fixture.globalSettingsPosition.limits.selectionLimit`
83. Verifikasi tombol aksi massal pada bar masih aktif dan bisa diklik
84. Verifikasi checkbox pada baris berikutnya berstatus disabled
85. Verifikasi tooltip
    `Fixture.globalSettingsPosition.captions.bulkActionBar.selectionLimitTooltip` muncul saat mencoba
    mencentang baris disabled itu
86. Verifikasi tooltip memakai kata `rows` dan bukan `items`
87. Verifikasi mencoba mencentang baris disabled tidak menambah jumlah seleksi
88. Verifikasi checkbox pada baris setelahnya juga disabled
89. Verifikasi baris yang sudah tercentang tidak ikut ter-uncheck karena penambahan limit
90. Verifikasi jumlah seleksi tetap pada
    `Fixture.globalSettingsPosition.limits.selectionLimit`

### Auto-cap saat Server Select All melebihi batas

91. Verifikasi filter aktif menyisakan
    `Fixture.globalSettingsPosition.positions.selectionLimit.oversizedFilteredCount` baris
92. Verifikasi jumlah itu lebih besar dari `Fixture.globalSettingsPosition.limits.selectionLimit`
93. Verifikasi angka pada tombol `Select All` menunjukkan
    `Fixture.globalSettingsPosition.positions.selectionLimit.oversizedFilteredCount`
94. Klik tombol `Select All ({N} records)`
95. Verifikasi seleksi ter-cap otomatis pada
    `Fixture.globalSettingsPosition.limits.selectionLimit` baris pertama
96. Verifikasi jumlah seleksi tidak sama dengan
    `Fixture.globalSettingsPosition.positions.selectionLimit.oversizedFilteredCount`, jadi capping
    benar-benar terjadi
97. Verifikasi jumlah seleksi tidak nol, jadi limit tidak memblokir seluruh aksi
98. Verifikasi toast
    `Fixture.globalSettingsPosition.captions.toast.selectionAutoCap` muncul
99. Verifikasi toast tersebut adalah toast error, bukan dialog blokir
100. Verifikasi toast bertahan sampai ditutup sendiri, tidak hilang otomatis
101. Verifikasi Bulk Action Bar tetap tampil
102. Verifikasi tombol aksi massal pada bar masih aktif dan bisa diklik
103. Verifikasi baris yang terpilih berada di bagian teratas hasil filter
104. Tutup toast
105. Verifikasi jumlah seleksi tidak berubah setelah toast ditutup
106. Verifikasi baris yang tidak terpilih tetap tidak tercentang

## Notes

- Yang diuji di sini adalah perilaku bar dan protokol seleksi, bukan Delete. Tidak ada satu pun langkah
  di spec ini yang menghapus Position, supaya kegagalan bulk action tidak mengaburkan kegagalan
  screening bar.
- Urutan elemen pada langkah 7 memakai urutan baku `prd-conventions.md`, yaitu Bulk Action, counter,
  `Select All ({N} records)`, lalu ikon `✕`. Wireframe PRD §4.2 masih memakai urutan ringkas
  `counter | [Delete] | [✕}` dan tidak menyebut elemen Select All sama sekali. Perbedaan itu dicatat
  di dokumen coverage sebagai gap yang perlu ditutup di PRD, bukan diselesaikan dengan mengarang
  urutan ketiga di spec ini.
- Elemen pertama pada urutan baku adalah tombol dropdown `Bulk Action` yang memuat daftar aksi, bukan
  tombol `Delete` langsung. Position hanya punya satu aksi massal sehingga isinya tetap satu. Spec ini
  memeriksa posisinya, bukan bentuk ketersusunnya, supaya spec tidak terkunci pada satu interpretasi
  komponen yang belum final di PRD modul ini.
- Subbagian kedua sengaja memisahkan checkbox header dari tombol Server Select All. Dua mekanisme itu
  punya cakupan berbeda, yaitu halaman aktif versus seluruh hasil filter, dan menggabungkannya
  membuat salah satunya akan selalu gagal.
- Langkah 35 memakai tanda tidak sama dengan karena itu yang diuji. Counter pada checkbox header harus
  sebesar baris halaman aktif, bukan sebesar total data.
- Status Indeterminate pada langkah 43 diuji pada kondisi parsial saja. Pada kondisi seluruh halaman
  aktif tercentang, header harus checked dan tidak Indeterminate.
- Subbagian ketiga memverifikasi seleksi lintas halaman secara nyata dengan pindah halaman, bukan
  hanya dengan membaca angka counter. Seleksi server bisa terlihat benar di counter tapi tidak benar
  di flag checkbox halaman lain.
- Subbagian keempat memakai navigasi keluar-masuk tab untuk memastikan seleksi bertahan. Seleksi
  hilang saat pindah tab akan membuat user kehilangan ratusan baris terpilih tanpa jejak apa pun.
- Dua subbagian terakhir memakai batas `Fixture.globalSettingsPosition.limits.selectionLimit` yang
  nilainya diambil dari System Limits, bukan ditulis di spec ini. Kalau nilainya diubah di
  Admin Console, spec ini mengikuti tanpa perlu ditulis ulang.
- Live-block dan auto-cap dibedakan karena keduanya memang dua mekanisme berbeda pada
  `prd-conventions.md`. Seleksi manual diblokir saat populer mencapai limit, sedangkan Select All
  dipotong ke limit sekaligus memberi toast error. Menggabungkan keduanya dalam satu skenario akan
  menghilangkan perbedaan itu.
- Toast auto-cap pada langkah 100 diperiksa bertahan sampai ditutup sendiri, karena toast itu
  membawa informasi bahwa baris sisanya belum terseleksi. Kalau hilang sendiri, user akan
  menjalankan Delete pada sebagian data tanpa tahu bagian mana yang tertinggal.
- Subbagian live-block dan auto-cap memakai tenant dengan lebih dari seribu Position. Itu disiapkan
  oleh tim FE, dan catatan keterbatasan resource sudah dicatat di dokumen coverage.
