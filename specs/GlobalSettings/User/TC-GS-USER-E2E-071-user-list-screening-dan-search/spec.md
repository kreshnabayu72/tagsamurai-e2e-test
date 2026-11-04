---
id: TC-GS-USER-E2E-071-user-list-screening-dan-search
title: "User List: State Kosong dan Search (Reveal, Clear, Trim, Substring per Kolom, Kolom Tanggal, Active Exact, Kolom Hidden)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-10
  - TC-GS-USER-413
  - TC-GS-USER-414
  - TC-GS-USER-415
  - TC-GS-USER-416
  - TC-GS-USER-417
  - TC-GS-USER-418
  - TC-GS-USER-1034
  - TC-GS-USER-419
  - TC-GS-USER-420
coverage:
  web: automated
---

# User List: State Kosong dan Search (Reveal, Clear, Trim, Substring per Kolom, Kolom Tanggal, Active Exact, Kolom Hidden)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `GS_TC2_PASSWORD` (admin kedua; hanya sesi API untuk membuat U-2 agar Modified By berbeda dari U-1). Keduanya didaftarkan di `executionConfig.environmentVariables`.
- Admin kedua: akun Total Control kedua yang disediakan tim FE (tidak ada di Tabel Pre-setup TC). Nama tampil admin kedua tidak memuat `Siti N`. Sesi UI kedua tidak dipakai.
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22 dan Custom Field aktif No. 24, hanya dibaca): `Dewi Lestari` (Active), `Jane Smith` dan `Budi Hartono` (Inactive), `John Doe` (Activated, TAG `TAG-4F7K2XQ9`), serta user Pre-setup lain di tabel Login User. Kondisi yang dibaca dan disediakan tim FE pada entitas uji: minimal satu baris dengan Modified By `System` (TC-GS-USER-419; Default User seed yang belum diedit, TC-GS-USER-1043).
- Data Dinamis, di-seed lewat API di hook `before`. Kemampuan seeding user lewat API disediakan tim FE/BE (endpoint tidak disebut di TC dan PRD). Field wajib yang bukan objek uji: Access sesuai tabel, Division sesuai tabel, dan Custom Field `Emergency Phone` (Required, Tabel Pre-setup No. 24) dengan Country Code `🇮🇩 +62` dan Number `81234567890`.
  - U-1 (dibuat lewat sesi API Total Control, sehingga Modified By `Siti N`): Name `Gandhi Pranoto {runId}-071`, Email `gandhipranoto+{runId}-071@qwertysystem.net`, Position `Supervisor`, Division `Logistics`, Access `Fixed Asset`, Employee ID `EMPA-{runId}-071`, Temporary User dengan Temporary Until hari uji + 30 hari. Status awal `Pending Activation`.
  - U-2 (dibuat lewat sesi API admin kedua, sehingga Modified By berbeda dari U-1): Name `Hesti Maharani {runId}-071`, Email `hestimaharani+{runId}-071@qwertysystem.net`, Position `Internal Auditor`, Division `Legal`, Access `Supply Asset`, Employee ID `EMPB-{runId}-071`, bukan Temporary User.
  - Seeding minimal (S-11): dua user dengan nilai berbeda pada setiap kolom yang di-search; baris Pre-setup dipakai sebagai pembanding hanya untuk kolom Active, Activation Status, dan TAG.
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus U-1 dan U-2 lewat API.
- Data uji: keyword `zzzqqq`, `Gandhi`, `  DEWI  `, `Gandhi Pra`, `ndhipranoto`, `Superv`, `Logis`, `EMPA`, `Siti N`, `Fixed`, `Inactive`, `Active`, `active`, `Pending`, `Yes`, `4F7K2`, `System`.
- State yang diubah dan dipulihkan: ukuran halaman 100 (langkah 1) dikembalikan ke 10 (langkah 120); kolom `Activation Status`, `Temporary User`, `Temporary Until`, `TAG` ditampilkan (langkah 71 sampai 75) dan disembunyikan lagi (langkah 114 sampai 118); kolom `Modified By` di-hide dan di-unhide di TC-GS-USER-419; Search ditutup di langkah 113. Hook `after` sebagai cadangan mengembalikan konfigurasi kolom ke default (Setup Column > `[Reset to Default]`, `[Save]`, atau penghapusan preferensi kolom User List di browser; mekanisme disediakan tim FE/BE).
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: memeriksa fokus kursor pada input Search; membaca teks sel tabel; mengirim Enter pada input Search yang sudah berisi.

## Test Steps

### Pembukaan layar

1. Pilih 100 baris per halaman pada Pagination

### TC-GS-USER-10: No result state User List saat Search tidak cocok

2. Klik icon Search, ketik `zzzqqq`, tekan Enter
3. Verifikasi tabel menampilkan ilustrasi no result
4. Verifikasi tabel menampilkan teks `No results found`
5. Verifikasi tabel menampilkan teks `Try adjusting your search or filter.`
6. Verifikasi Pagination tidak menampilkan baris
7. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-413: Siklus Search: reveal, Enter, clear (✕), collapse ←

8. Klik icon Search
9. Verifikasi input Search melebar
10. Verifikasi kursor auto-focus di input Search
11. Ketik `Gandhi` pada kotak Search
12. Verifikasi icon `(✕)` muncul di dalam input
13. Verifikasi tabel belum tersaring: baris `Gandhi Pranoto {runId}-071` dan baris `Hesti Maharani {runId}-071` sama-sama tampil
14. Tekan Enter
15. Verifikasi tabel tersaring: baris `Gandhi Pranoto {runId}-071` tampil
16. Verifikasi baris `Hesti Maharani {runId}-071` tidak tampil
17. Klik icon `(✕)`
18. Verifikasi input Search kosong
19. Verifikasi tabel tetap menampilkan hasil search terakhir: baris `Gandhi Pranoto {runId}-071` tampil dan baris `Hesti Maharani {runId}-071` tidak tampil
20. Tekan Enter pada input kosong
21. Verifikasi tabel kembali menampilkan semua data: baris `Hesti Maharani {runId}-071` tampil kembali
22. Isi Search dengan `Gandhi`, tekan Enter
23. Klik icon panah `(←)` di kiri toolbar
24. Verifikasi Search collapse menjadi icon Search biasa
25. Verifikasi tabel langsung reset tanpa menekan Enter: baris `Hesti Maharani {runId}-071` tampil
26. Klik icon Search
27. Verifikasi keyword Search kosong

### TC-GS-USER-414: Query Search di-trim dan tidak case-sensitive

28. Isi Search dengan `  DEWI  `, tekan Enter
29. Verifikasi baris `Dewi Lestari` tampil (spasi tepi diabaikan dan huruf besar/kecil tidak dibedakan)
30. Verifikasi isi kotak Search tetap menampilkan teks yang diketik apa adanya: `  DEWI  `

### TC-GS-USER-415: Search menemukan substring pada kolom kelas teks

31. Ganti isi kotak search dengan `Gandhi Pra`, tekan Enter
32. Verifikasi kolom Name: baris `Gandhi Pranoto {runId}-071` tampil (nilai Name memuat `Gandhi Pra`)
33. Verifikasi kolom Name: baris `Hesti Maharani {runId}-071` tidak tampil
34. Klik icon `(✕)`
35. Isi Search dengan `ndhipranoto`, tekan Enter
36. Verifikasi kolom Email: baris `Gandhi Pranoto {runId}-071` tampil (nilai Email memuat `ndhipranoto`)
37. Verifikasi kolom Email: baris `Hesti Maharani {runId}-071` tidak tampil
38. Klik icon `(✕)`
39. Isi Search dengan `Superv`, tekan Enter
40. Verifikasi kolom Position: baris `Gandhi Pranoto {runId}-071` tampil (nilai Position memuat `Superv`)
41. Verifikasi kolom Position: baris `Hesti Maharani {runId}-071` tidak tampil
42. Klik icon `(✕)`
43. Isi Search dengan `Logis`, tekan Enter
44. Verifikasi kolom Division: baris `Gandhi Pranoto {runId}-071` tampil (nilai Division memuat `Logis`)
45. Verifikasi kolom Division: baris `Hesti Maharani {runId}-071` tidak tampil
46. Klik icon `(✕)`
47. Isi Search dengan `EMPA`, tekan Enter
48. Verifikasi kolom Employee ID: baris `Gandhi Pranoto {runId}-071` tampil (nilai Employee ID memuat `EMPA`)
49. Verifikasi kolom Employee ID: baris `Hesti Maharani {runId}-071` tidak tampil
50. Klik icon `(✕)`
51. Isi Search dengan `Siti N`, tekan Enter
52. Verifikasi kolom Modified By: baris `Gandhi Pranoto {runId}-071` tampil (nilai Modified By memuat `Siti N`)
53. Verifikasi kolom Modified By: baris `Hesti Maharani {runId}-071` tidak tampil
54. Klik icon `(✕)`

### TC-GS-USER-416: Search menemukan substring pada kolom kelas chip produk

55. Isi Search dengan `Fixed`, tekan Enter
56. Verifikasi kolom Access: baris `Gandhi Pranoto {runId}-071` tampil (nilai Access memuat `Fixed`)
57. Verifikasi kolom Access: baris `Hesti Maharani {runId}-071` tidak tampil
58. Klik icon `(✕)`

### TC-GS-USER-1034: Search pada kolom Active exact match terhadap teks Active/Inactive

59. Isi Search dengan `Inactive`, tekan Enter
60. Verifikasi keyword `Inactive`: baris `Jane Smith` dan baris `Budi Hartono` (Inactive) tampil
61. Verifikasi keyword `Inactive`: baris `Dewi Lestari` (Active) tidak tampil
62. Klik icon `(✕)`
63. Isi Search dengan `Active`, tekan Enter
64. Verifikasi keyword `Active`: baris `Dewi Lestari` (Active) tampil
65. Verifikasi keyword `Active`: baris `Jane Smith` dan baris `Budi Hartono` (Inactive) tidak tampil (exact match, bukan substring dari `Inactive`)
66. Klik icon `(✕)`
67. Isi Search dengan `active`, tekan Enter
68. Verifikasi keyword `active` (huruf kecil): baris `Dewi Lestari` tampil
69. Verifikasi keyword `active` (huruf kecil): baris `Jane Smith` dan baris `Budi Hartono` tidak tampil (hasil sama dengan keyword `Active`)
70. Klik icon `(✕)`

### TC-GS-USER-417: Search menemukan substring pada kolom kelas curated (setelah ditampilkan)

71. Klik header kolom Column Visibility (⋯)
72. Centang `Activation Status`
73. Centang `Temporary User`
74. Centang `Temporary Until`
75. Centang `TAG`
76. Tekan Esc untuk menutup Overlay Column Visibility
77. Klik kotak Search
78. Isi Search dengan `Pending`, tekan Enter
79. Verifikasi kolom Activation Status: baris `Gandhi Pranoto {runId}-071` tampil (nilai Activation Status memuat `Pending`)
80. Verifikasi kolom Activation Status: baris `John Doe` (Activated) tidak tampil
81. Klik icon `(✕)`
82. Isi Search dengan `Yes`, tekan Enter
83. Verifikasi kolom Temporary User: baris `Gandhi Pranoto {runId}-071` tampil (nilai Temporary User memuat `Yes`)
84. Verifikasi kolom Temporary User: baris `Hesti Maharani {runId}-071` tidak tampil
85. Klik icon `(✕)`
86. Isi Search dengan `4F7K2`, tekan Enter
87. Verifikasi kolom TAG: baris `John Doe` tampil (nilai TAG memuat `4F7K2`)
88. Verifikasi kolom TAG: baris `Gandhi Pranoto {runId}-071` tidak tampil
89. Klik icon `(✕)`

### TC-GS-USER-418: Kolom bertipe tanggal tidak tercakup Search

90. Isi Search dengan `Gandhi Pra`, tekan Enter
91. Verifikasi baris `Gandhi Pranoto {runId}-071` tampil
92. Baca teks sel Last Update dan sel Temporary Until baris `Gandhi Pranoto {runId}-071` sebagai `{teks Last Update}` dan `{teks Temporary Until}`
93. Ganti isi kotak search dengan `{teks Last Update}`, tekan Enter
94. Verifikasi kolom Last Update: keyword tidak mencocokkan baris, tabel menampilkan teks `No results found`
95. Ganti isi kotak search dengan `{teks Temporary Until}`, tekan Enter
96. Verifikasi kolom Temporary Until: keyword tidak mencocokkan baris, tabel menampilkan teks `No results found`

### TC-GS-USER-419: Search tidak mencocokkan kolom yang sedang di-hide, kembali cocok setelah unhide

97. Ganti isi kotak search dengan `System`, tekan Enter
98. Verifikasi tabel menampilkan sedikitnya satu baris dengan Modified By `System` (pembanding sebelum kolom di-hide)
99. Klik header kolom Column Visibility (⋯)
100. Hilangkan centang `Modified By`
101. Tekan Esc untuk menutup Overlay Column Visibility
102. Klik kotak Search, tekan Enter
103. Verifikasi saat kolom Modified By hidden: tabel menampilkan teks `No results found`
104. Klik header kolom Column Visibility (⋯)
105. Centang `Modified By`
106. Tekan Esc untuk menutup Overlay Column Visibility
107. Klik kotak Search, tekan Enter
108. Verifikasi setelah kolom Modified By di-unhide: baris dengan Modified By `System` tampil kembali

### TC-GS-USER-420: Empty filtered state

109. Ganti isi kotak search dengan `zzzqqq`, tekan Enter
110. Verifikasi tabel menampilkan ilustrasi no result
111. Verifikasi tabel menampilkan teks `No results found`
112. Verifikasi tabel menampilkan teks `Try adjusting your search or filter.`

### Pemulihan state

113. Klik icon panah `(←)` untuk menutup Search dan mereset tabel
114. Klik header kolom Column Visibility (⋯)
115. Hilangkan centang `Activation Status`
116. Hilangkan centang `Temporary User`
117. Hilangkan centang `Temporary Until`
118. Hilangkan centang `TAG`
119. Tekan Esc untuk menutup Overlay Column Visibility
120. Pilih 10 baris per halaman pada Pagination

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 10, 413, 414, 415, 416, 1034, 417, 418, 419, 420. TC-GS-USER-1034 ditaruh sebelum TC-GS-USER-417 karena Search `Active` pada kolom Active harus dijalankan selagi kolom Activation Status masih hidden (nilai Activation Status memuat `Activated`; bila kolomnya sudah tampil, keyword `Active` ikut mencocokkan baris itu). Urutan di `tc-user.md`: 10, 413 sampai 418, 1034, 419, 420.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 agar baris seed dan baris Pre-setup berada di halaman yang sama), langkah 7 dan 113 (menutup Search dan mereset tabel), langkah 26 (membuka kembali Search untuk TC-GS-USER-414; sekaligus dipakai mengamati keyword kosong, Expected f TC-GS-USER-413), tiap `Klik icon (✕)` sesudah blok kolom (TC-GS-USER-415 sampai 417 meminta clear), langkah 71 sampai 76 (menampilkan kolom curated lewat Overlay Column Visibility sebelum TC-GS-USER-417), langkah 92 (membaca teks tanggal untuk TC-GS-USER-418), serta langkah 114 sampai 120 (memulihkan konfigurasi kolom dan ukuran halaman). Langkah `Klik kotak Search` sesudah Overlay ditutup mengembalikan fokus ke input Search.
- Asersi pembanding (S-03, bagian 8b butir 2): tiap `Verifikasi` ketiadaan baris didahului `Verifikasi` baris pembanding yang tampil pada tabel yang sama; langkah yang menyatakan "tidak tampil" untuk U-2 memakai U-1 yang tampil sebagai anchor. TC-GS-USER-419: langkah pembanding sebelum kolom di-hide (baris dengan Modified By `System` tampil) membuktikan keyword mencocokkan kolom itu; hasil kosong sesudah hide berasal dari kolom hidden, bukan dari keyword yang salah.
- Spec melewati sekitar 35 langkah karena sepuluh TC Search berbagi satu layar, satu dataset (U-1, U-2, dan Pre-setup), dan satu kelas harness (fungsional, baca saja). Tiap blok kolom berdiri sendiri dan memakai Search yang sama; memisahkannya mengulang login, seeding, dan pembukaan layar yang sama. Tiap `Verifikasi` dipecah per klausa (S-01) dan tiap kolom memuat dua `Verifikasi` (baris cocok tampil dan baris pembanding tidak tampil).
- Pembagian TC lintas spec: TC-GS-USER-6 (retensi Search dan Sort saat pindah tab) dan TC-GS-USER-1043 (Modified By Default User seed) diverifikasi di spec 001; TC-GS-USER-421 sampai 429 (Filter Panel) di spec 072; TC-GS-USER-430 sampai 434, 463, 464 (kombinasi Search dan Filter) di spec 073; Sort, Pagination, dan kombinasi di spec 074; Setup Column di spec 075; Download di spec 076 dan 077.
- Temuan untuk QA:
  - TC-GS-USER-415 dan 417: TC memberi contoh keyword (`Dewi`, `Fixed`, `Pending`) tetapi tidak menyebut baris pembanding yang tidak boleh cocok. Spec memakai dua user seed (U-1, U-2) dengan nilai berbeda pada tiap kolom dan satu baris Pre-setup (`John Doe`) untuk Activation Status dan TAG.
  - TC-GS-USER-415 (Modified By): sel Modified By menampilkan nama singkat (`Siti N`); TC tidak menyebut apakah Search mencocokkan nama lengkap atau teks sel. Spec memakai `Siti N`, yang ada di keduanya.
  - TC-GS-USER-419: TC tidak menyebut nilai yang "hanya ada di kolom Modified By". Spec memakai `System` (Modified By Default User seed menurut TC-GS-USER-1043), karena nama akun pembuat seed juga muncul sebagai Name user lain. Kondisi disediakan tim FE.
  - TC-GS-USER-1034: contoh hasil TC menyebut `Dewi Lestari` Active; TC tidak menyebut apakah user baru berstatus `Pending Activation` ikut Active. Spec hanya mengasersi baris Pre-setup (`Dewi Lestari`, `Jane Smith`, `Budi Hartono`).
  - TC-GS-USER-418: TC tidak menyebut format teks tanggal yang diketik; spec memakai teks sel apa adanya.
  - TC-GS-USER-413 dan 420: TC-GS-USER-420 mengulang kasus TC-GS-USER-10 (`zzzqqq`); keduanya diasersi di blok masing-masing.
  - TC-GS-USER-417 dan 418: label kolom curated mengikuti TC (`Activation Status`, `Temporary User`, `Temporary Until`, `TAG`); label Overlay untuk menampilkannya (centang di Overlay Column Visibility) mengikuti TC-GS-USER-419 ("Hide kolom via Column Visibility").
