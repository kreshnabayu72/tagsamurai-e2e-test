---
id: TC-AC-ACHA-E2E-001-list-screening-dan-format-sel
title: "Screening List Device Allocation, Format Sel, dan State Loading"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-1
  - TC-AC-ACHA-2
  - TC-AC-ACHA-3
  - TC-AC-ACHA-4
  - TC-AC-ACHA-5
  - TC-AC-ACHA-10
  - TC-AC-ACHA-11
  - TC-AC-ACHA-12
  - TC-AC-ACHA-13
  - TC-AC-ACHA-14
  - TC-AC-ACHA-15
  - TC-AC-ACHA-16
  - TC-AC-ACHA-17
  - TC-AC-ACHA-18
  - TC-AC-ACHA-19
  - TC-AC-ACHA-20
coverage:
  web: automated
---

# Screening List Device Allocation, Format Sel, dan State Loading

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal PT ABC (Pre-setup #21, nama pengguna Admin Pratama) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (TC-1 sampai TC-5, TC-10 sampai TC-15, TC-17 sampai TC-19). Akun kedua: Total Control Distributor PT Global Distribusi (Pre-setup #27, alias TC_DIST) `totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_TC_DIST_PASSWORD` (TC-16). Akun ketiga: Group Member Distributor toggle ON (Pre-setup #32, alias MB_ON, nama pengguna Budi Santoso) `memberOnDistributor_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_MB_ON_PASSWORD` (TC-20).
- Login akun aktor pertama di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal PT ABC, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah logout dan login eksplisit.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor, flag Guided Tooltip `guided_tooltip_seen_ac-device-allocation` true untuk akun aktor, fixture API Pre-setup #20 (disediakan tim FE/BE; endpoint tidak dikarang di spec ini), dan pemulihan preferensi kolom Setup Column. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (hanya dibaca, tidak diubah): Seed 30 alokasi (Pre-setup #48) dengan nilai literal dan Rincian Seed List (Allocation ID, Category, Type, Quantity, From, Allocated By, Status, Notes, Payment, Paid From, Cost, Last Updated) sebagai acuan asersi; transaksi Waiting for Approval milik MB_ON (Pre-setup #49, TC-20); transaksi Completed ber-Notes 300 karakter milik TC_DIST (Pre-setup #61, TC-16). Allocation ID Pre-setup #49 dan #61 dibaca lewat fixture seed (disediakan tim FE/BE), tidak di-hardcode. Fixture baseline memulihkan seed ke keadaan awal sebelum spec dijalankan.
- General Settings Pre-setup #1: Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta (tidak diubah). Format Last Updated tampil `dd/MM/yy HH:mm`.
- Kemampuan teknis: intercept penundaan respons permintaan data tabel selama 3 detik (TC-5, dilepas segera sesudah asersi Loading); hover dan keyboard focus; Setup Column untuk menampilkan kolom Notes, Payment, Paid From, dan Cost (disimpan di browser, dipulihkan hook `after` suite dengan menghapus preferensi kolom).
- State global: tidak ada yang diubah selain preferensi Setup Column; suite berjalan serial.
- Tabel parameter langkah berulang:

Tooltip Table Tools (langkah 34 sampai 36):

| Elemen | Tooltip |
|---|---|
| ikon Search | `Search` |
| ikon Filter | `Filter` |
| ikon Download | `Download` |
| ikon `⋯` pada header kolom terakhir | `Column Visibility` |
| tombol `[?]` | `Show guide` |

Baris uji badge Category, TC-10 (langkah 63 sampai 68):

| Allocation ID | Category tampil | Hierarki tooltip |
|---|---|---|
| `HALC-20260901-00001` | `RFID` | `TAG > RFID` |
| `HALC-20260902-00003` | `Handheld Reader` | `Hardware > Handheld Reader` |
| `HALC-20260904-00001` | `NFC` | `TAG > NFC` |

Baris uji kolom Type, TC-11 (langkah 70 sampai 72):

| Allocation ID | Category | Type tampil |
|---|---|---|
| `HALC-20260901-00001` | RFID | `Object TAG` |
| `HALC-20260901-00002` | RFID | `User TAG` |
| `HALC-20260902-00003` | Handheld Reader | `Long Range` |
| `HALC-20260903-00001` | Handheld Reader | `Short Range` |
| `HALC-20260904-00001` | NFC | `—` |

Baris uji Quantity, TC-12 (langkah 74 sampai 76):

| Allocation ID | Quantity seed | Quantity tampil |
|---|---|---|
| `HALC-20260903-00004` | 5000 | `5,000` |
| `HALC-20260906-00002` | 1 | `1` |

Baris uji badge Status, TC-13 (langkah 78 sampai 80):

| Allocation ID | Status | Severity badge |
|---|---|---|
| `HALC-20260901-00001` | `Completed` | success (hijau) |
| `HALC-20260901-00002` | `Waiting for Approval` | warning (kuning) |
| `HALC-20260902-00002` | `Rejected` | danger (merah) |
| `HALC-20260901-00003` | `Canceled` | danger (merah) |

Baris uji Allocated By, TC-18 (langkah 82 sampai 88):

| Allocation ID | Nama lengkap | Tampil di sel | Tooltip |
|---|---|---|---|
| `HALC-20260901-00001` | Budi Santoso | `Budi S` | `Budi Santoso` |
| `HALC-20260902-00003` | Admin Pratama | `Admin P` | `Admin Pratama` |

- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_DA_TC_DIST_PASSWORD` dan `AC_DA_MB_ON_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` dan `.env.example` pada tahap script. Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-ACHA-1: Screening List

1. Amati halaman List dari atas ke bawah (halaman dibuka hook `beforeEach`)
2. Verifikasi Breadcrumb `Allocation > Device Allocation` terdiri atas dua segmen
3. Verifikasi tidak ada segmen Breadcrumb yang dapat diklik
4. Verifikasi tidak ada Page Title Header di bawah Breadcrumb
5. Verifikasi tombol replay Guided Tooltip `[?]` tepat di sebelah kanan Breadcrumb
6. Verifikasi SectionCard `Allocated quota` (Stock Balance Summary Panel) berisi tujuh baris Category berurutan: RFID | NFC | BLE | GPS | Handheld Reader | Smart Fixed Reader | BLE Gateway
7. Verifikasi Table Tools menampilkan Search | Filter | Download | `[+ Allocation]`
8. Verifikasi tidak ada ikon Changelog pada Table Tools
9. Verifikasi kolom default: `Allocation ID (sortable) | Category (sortable) | Type (sortable) | Quantity (sortable) | From (sortable) | Client (sortable) | Allocated By (sortable) | Status (sortable) | Last Updated (sortable) | Column Visibility (⋯)`
10. Verifikasi header kolom `Column Visibility (⋯)` unsortable
11. Klik header kolom `Column Visibility (⋯)`
12. Verifikasi overlay Column Visibility terbuka dengan CTA `[Setup Column]`
13. Tekan Esc untuk menutup overlay
14. Klik `[⋯]` pada baris pertama tabel
15. Verifikasi row action menu terbuka
16. Tekan Esc untuk menutup row action menu
17. Verifikasi sepuluh baris pertama urut Last Updated terbaru, tiga baris teratas `HALC-20260909-00003`, `HALC-20260909-00002`, `HALC-20260909-00001`
18. Verifikasi tidak ada kolom checkbox seleksi baris
19. Verifikasi tidak ada Bulk Action Bar
20. Verifikasi pagination default 10 data per halaman
21. Verifikasi pagination menampilkan tiga halaman untuk 30 baris

### TC-AC-ACHA-2: Hover dan tooltip Table Tools, header Actions, dan tombol replay Guided Tooltip

22. Arahkan kursor ke ikon Search
23. Verifikasi tooltip ikon Search `Search`
24. Arahkan kursor ke ikon Filter
25. Verifikasi tooltip ikon Filter `Filter`
26. Arahkan kursor ke ikon Download
27. Verifikasi tooltip ikon Download `Download`
28. Arahkan kursor ke ikon `⋯` pada header kolom terakhir tabel
29. Verifikasi tooltip header kolom Actions `Column Visibility`
30. Arahkan kursor ke tombol `[?]` di sebelah kanan Breadcrumb
31. Verifikasi tooltip tombol `[?]` `Show guide`
32. Pindahkan kursor ke area kosong halaman
33. Untuk setiap baris tabel "Tooltip Table Tools" lakukan langkah 34 sampai 36
34. Pindahkan fokus keyboard ke elemen pada baris tabel
35. Verifikasi tooltip pada baris tabel tampil sesuai kolom "Tooltip" saat elemen menerima keyboard focus
36. Tekan Esc untuk melepas fokus

### TC-AC-ACHA-3: Default sort Last Updated Newest First dan konsistensi urutan antar halaman

37. Amati urutan baris dan indikator sort pada header kolom
38. Verifikasi tiga baris pertama `HALC-20260909-00003` (09/09/26 19:00), `HALC-20260909-00002` (09/09/26 12:00), `HALC-20260909-00001` (09/09/26 05:00)
39. Verifikasi indikator sort aktif berada pada kolom Last Updated
40. Klik nomor halaman 2
41. Verifikasi halaman 2 memuat baris ke-11 sampai ke-20 (urutan Allocation ID sesuai Rincian Seed List No 20 `HALC-20260906-00004` sampai No 11 `HALC-20260904-00001`)
42. Klik nomor halaman 3
43. Verifikasi halaman 3 memuat 10 baris terakhir (No 10 sampai No 1), baris terakhir `HALC-20260901-00001`
44. Verifikasi tidak ada baris ganda atau terlewat di antara halaman 1, 2, dan 3 (30 Allocation ID berbeda)
45. Klik nomor halaman 1

### TC-AC-ACHA-4: Tidak ada Bulk Action dan tidak ada Changelog

46. Verifikasi tabel menampilkan sepuluh baris
47. Cari kolom checkbox di header dan di baris tabel
48. Verifikasi tidak ada kolom checkbox seleksi baris
49. Verifikasi tidak ada Bulk Action Bar, tombol `Bulk Action`, maupun `Select All`
50. Klik area baris tabel di luar kolom Allocation ID dan di luar row action
51. Verifikasi Table Tools `Search`, `Filter`, `Download` tetap tampil
52. Verifikasi klik area baris tidak membuka modal, drawer, atau halaman apa pun
53. Verifikasi tidak ada ikon Changelog di Table Tools
54. Verifikasi tidak ada modal Changelog (riwayat per transaksi hanya lewat modal Allocation Log)

### TC-AC-ACHA-5: State Loading pada tabel List

55. Tahan respons permintaan data tabel selama 3 detik (intercept), lalu muat ulang halaman (F5)
56. Verifikasi tabel menampilkan komponen skeleton atau spinner loading
57. Verifikasi tabel tidak menampilkan empty state
58. Verifikasi tabel tidak menampilkan state error
59. Lepas tahanan respons (hapus intercept) dan tunggu respons diterima
60. Verifikasi skeleton hilang
61. Verifikasi sepuluh baris tampil

### TC-AC-ACHA-10: Badge Category dan hover hierarki dari root

62. Untuk setiap baris tabel "Baris uji badge Category" lakukan langkah 63 sampai 68
63. Ketik Search `Allocation ID` pada baris tabel, tekan Enter
64. Arahkan kursor ke badge Category pada baris hasil
65. Verifikasi badge Category berwarna primary menampilkan nama first-level sesuai kolom "Category tampil"
66. Verifikasi tooltip hover badge menampilkan hierarki lengkap dari root sesuai kolom "Hierarki tooltip"
67. Verifikasi nama Category (kurang dari 25 karakter) tampil penuh tanpa potongan
68. Klik `(←)` pada kotak Search

### TC-AC-ACHA-11: Kolom Type

69. Untuk setiap baris tabel "Baris uji kolom Type" lakukan langkah 70 sampai 72
70. Ketik Search `Allocation ID` pada baris tabel, tekan Enter
71. Verifikasi kolom Type pada baris hasil menampilkan nilai kolom "Type tampil" (`—` em dash untuk Category tanpa Type, bukan sel kosong)
72. Klik `(←)` pada kotak Search

### TC-AC-ACHA-12: Format kolom Quantity

73. Untuk setiap baris tabel "Baris uji Quantity" lakukan langkah 74 sampai 76
74. Ketik Search `Allocation ID` pada baris tabel, tekan Enter
75. Verifikasi kolom Quantity pada baris hasil menampilkan bilangan bulat sesuai kolom "Quantity tampil" (pemisah ribuan)
76. Klik `(←)` pada kotak Search

### TC-AC-ACHA-13: Badge kolom Status per nilai

77. Untuk setiap baris tabel "Baris uji badge Status" lakukan langkah 78 sampai 80
78. Ketik Search `Allocation ID` pada baris tabel, tekan Enter
79. Verifikasi badge pada kolom Status baris hasil bertuliskan nilai kolom "Status" dengan severity sesuai kolom "Severity badge"
80. Klik `(←)` pada kotak Search

### TC-AC-ACHA-18: Kolom Allocated By

81. Untuk setiap baris tabel "Baris uji Allocated By" lakukan langkah 82 sampai 88
82. Ketik Search `Allocation ID` pada baris tabel, tekan Enter
83. Verifikasi kolom Allocated By pada baris hasil berupa plain text (bukan badge) bernilai kolom "Tampil di sel"
84. Arahkan kursor ke sel Allocated By
85. Verifikasi tooltip menampilkan nama lengkap sesuai kolom "Tooltip"
86. Pindahkan fokus keyboard ke sel Allocated By
87. Verifikasi tooltip nama lengkap yang sama tampil saat keyboard focus
88. Klik `(←)` pada kotak Search

### TC-AC-ACHA-19: Allocation ID sebagai primary identifier

89. Amati teks Allocation ID pada baris `HALC-20260909-00003` dalam keadaan normal
90. Verifikasi Allocation ID berformat `HALC-YYYYMMDD-XXXXX` (`HALC-20260909-00003`) berupa text link dengan warna teks netral
91. Arahkan kursor ke Allocation ID `HALC-20260909-00003`
92. Verifikasi warna teks berubah menjadi warna primary Admin Console (merah) tanpa garis bawah
93. Klik Allocation ID `HALC-20260909-00003`
94. Verifikasi modal Allocation Log transaksi itu terbuka (bukan halaman baru)
95. Klik `[×]` pada modal Allocation Log

### Tampilkan kolom tambahan

96. Klik header kolom `Column Visibility (⋯)`, klik `[Setup Column]`, tampilkan kolom Notes, Payment, Paid From, dan Cost, lalu klik `[Save]`

### TC-AC-ACHA-14: Baris pengirim Principal

97. Ketik Search `HALC-20260902-00003`, tekan Enter
98. Verifikasi kolom From baris hasil `PT ABC`
99. Verifikasi kolom Payment `Free`
100. Verifikasi kolom Paid From `—`
101. Verifikasi kolom Cost `—`
102. Verifikasi tidak ada nominal biaya dan tidak ada sumber kantong pada baris pengirim Principal

### TC-AC-ACHA-15: Baris pengirim Distributor

103. Ganti isi kotak search dengan `HALC-20260901-00001`, tekan Enter
104. Verifikasi kolom From `PT Global Distribusi`
105. Verifikasi kolom Payment `Wallet`
106. Verifikasi kolom Paid From `PT ABC (Principal)`
107. Verifikasi kolom Cost `$1,250.00`
108. Verifikasi kolom Notes `Batch awal Q3`

### TC-AC-ACHA-17: Nilai kosong sebagai strip

109. Ganti isi kotak search dengan `HALC-20260902-00001`, tekan Enter
110. Verifikasi sel Type `—`
111. Verifikasi sel Notes `—`
112. Verifikasi sel Type dan Notes tidak kosong
113. Klik `(←)` pada kotak Search

### Ganti akun ke Total Control Distributor

114. Logout dari akun Total Control Principal
115. Login sebagai Total Control Distributor (`totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_TC_DIST_PASSWORD`)
116. Buka Allocation > Device Allocation lewat sidebar
117. Klik header kolom `Column Visibility (⋯)`, klik `[Setup Column]`, tampilkan kolom Notes, lalu klik `[Save]`

### TC-AC-ACHA-16: Kolom Notes teks panjang

118. Ketik Search `Allocation ID` transaksi Pre-setup #61 (Notes 300 karakter), tekan Enter
119. Amati sel Notes baris hasil
120. Verifikasi sel Notes memotong teks panjang dengan ellipsis pada satu baris
121. Verifikasi baris tidak melebar melebihi batas kolom
122. Arahkan kursor ke sel Notes
123. Verifikasi hover menampilkan teks Notes lengkap 300 karakter (`Pengiriman batch awal untuk gudang pusat. ` diulang hingga 300 karakter)
124. Klik `(←)` pada kotak Search

### Ganti akun ke Group Member Distributor

125. Logout dari akun Total Control Distributor
126. Login sebagai MB_ON (`memberOnDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_MB_ON_PASSWORD`)
127. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-20: Last Updated Waiting for Approval sama dengan waktu Created

128. Ketik Search `Allocation ID` transaksi Pre-setup #49, tekan Enter
129. Catat nilai kolom Last Updated baris hasil
130. Klik Allocation ID transaksi itu untuk membuka modal Allocation Log
131. Catat waktu entri `Allocation created by Budi S`
132. Verifikasi kolom Last Updated tabel sama dengan waktu entri `Allocation created by Budi S` (belum ada kejadian lanjutan)
133. Klik `[×]` pada modal Allocation Log dan klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Spec screening dan format sel List, hanya baca; tidak ada aksi tulis.
- Pengecualian S-12 nama literal: Population seed Pre-setup #48 (30 baris) memakai Allocation ID, nilai kolom, dan Last Updated literal karena asersi bergantung pada ID, urutan, dan jumlah. Seed idempotent, tidak diubah spec ini, suite serial. Dasarnya Lampiran A butir A-6 (seed idempotent Pre-setup #48).
- Subjudul `###` memetakan langkah ke id TC granular.
- Anchor dan adaptasi (S-02, S-03, S-15): langkah 33 sampai 36 mengulang tooltip pada keyboard focus untuk lima elemen Table Tools (adaptasi dari TC-2 Expected f); jangkar pembuktian elemen sudah dimuat adalah verifikasi tooltip hover langkah 23 sampai 31 pada elemen yang sama, sehingga langkah 35 tidak dapat lolos kosong.
- Langkah penghubung (S-03): langkah 13 dan 16 (tutup overlay dan menu), langkah 32 dan 36 (lepas kursor dan fokus), langkah 45 (kembali ke halaman 1), langkah 62 sampai 68, 69 sampai 72, 73 sampai 76, 77 sampai 80, dan 81 sampai 88 (Search untuk menemukan baris target, `(←)` untuk mereset Search), langkah 95 (tutup modal), langkah 96 dan 117 (Setup Column menampilkan kolom TC-14 sampai TC-17 dan TC-16), langkah 114 sampai 116 dan 125 sampai 127 (ganti akun), langkah 133 (tutup modal dan reset Search). Langkah 59 melepas intercept.
- Langkah berulang (bagian 8b butir 7): langkah 34 sampai 36 diulang lima kali (tabel Tooltip Table Tools), langkah 63 sampai 68 tiga kali, langkah 70 sampai 72 lima kali, langkah 74 sampai 76 dua kali, langkah 78 sampai 80 empat kali, langkah 82 sampai 88 dua kali. Jumlah langkah nominal 133; ekspansi sekitar 185.
- Ukuran spec (di atas sekitar 35 langkah): spec hanya membaca, memakai satu dataset (seed #48) tanpa mengubah state, dan tiap Expected menjadi `Verifikasi` sendiri (S-01). Blok TC berdiri sendiri (pencarian baris tersendiri per TC) sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal; TC-16 dan TC-20 memakai ganti akun eksplisit dan tidak bergantung pada blok sebelumnya (bagian 3, batas ukuran). Spec tidak dipecah.
- Pembagian TC lintas spec: TC-6 (empty state) ada di spec 002; TC-7 dan TC-9 (empty state Filtered) di spec 037; TC-8 (error load) di spec 058.
- Temuan untuk QA:
  - TC-2 Expected f menyatakan tooltip yang sama muncul saat keyboard focus, tetapi Langkah Uji hanya hover. Spec menambah langkah fokus keyboard (langkah 33 sampai 36) karena Expected memuatnya.
  - TC-3 Expected c menyatakan "baris ke-11 sampai ke-20" tanpa menyebut Allocation ID; spec menurunkan urutan dari Rincian Seed List Pre-setup #48 (Last Updated naik 7 jam per nomor).
  - TC-1 Expected b.i menyebut header klik membuka overlay Column Visibility dan body per baris membuka row action menu; Langkah Uji TC-1 hanya "amati halaman". Spec menambah langkah klik (langkah 11 sampai 16) agar klausa itu teramati.
  - TC-14, TC-15, TC-16, TC-17 mensyaratkan kolom Notes, Payment, Paid From, Cost ditampilkan lewat Setup Column tetapi tidak menyatakan apakah preferensi Setup Column berlaku lintas akun; spec menampilkan kolom lagi setelah ganti akun (langkah 117).
  - TC-16 dan TC-20 memakai Pre-setup #61 dan #49 tanpa Allocation ID; spec membacanya lewat fixture seed (disediakan tim FE/BE).
  - TC-20 tidak menyebut format waktu entri Allocation Log; spec membandingkan nilai Last Updated tabel dengan waktu entri sebagaimana tampil (menit yang sama).
  - TC-18 Expected a ("bukan badge") tidak punya padanan selector; diasersi sebagai plain text.
  - Post Condition kolom TC-1 sampai TC-20 bernilai `-`; tidak ada yang perlu diasersi.
