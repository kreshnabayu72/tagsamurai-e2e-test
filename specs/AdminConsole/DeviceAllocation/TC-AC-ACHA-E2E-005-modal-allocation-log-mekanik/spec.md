---
id: TC-AC-ACHA-E2E-005-modal-allocation-log-mekanik
title: "Modal Allocation Log: Screening, Jalur Pembuka, Penutupan, Copy, Loading, dan Scroll"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-29
  - TC-AC-ACHA-30
  - TC-AC-ACHA-31
  - TC-AC-ACHA-32
  - TC-AC-ACHA-33
  - TC-AC-ACHA-35
  - TC-AC-ACHA-36
coverage:
  web: automated
---

# Modal Allocation Log: Screening, Jalur Pembuka, Penutupan, Copy, Loading, dan Scroll

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal PT ABC (Pre-setup #21, nama pengguna Admin Pratama) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (TC-29 sampai TC-33, TC-35). Akun kedua: Total Control Distributor PT Global Distribusi (Pre-setup #27) `totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_TC_DIST_PASSWORD` (TC-36).
- Login akun aktor pertama di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal PT ABC, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah logout dan login eksplisit.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor, flag Guided Tooltip `guided_tooltip_seen_ac-device-allocation` true untuk akun aktor, fixture API Pre-setup #20 (disediakan tim FE/BE; endpoint tidak dikarang di spec ini), dan pemulihan preferensi kolom Setup Column. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (hanya dibaca, tidak diubah): Seed 30 alokasi (Pre-setup #48) dengan nilai literal; transaksi Waiting for Approval dengan 12 entri Allocation edited milik MB_ON (Pre-setup #58, 13 entri log; Allocation ID dibaca lewat fixture seed, disediakan tim FE/BE). Fixture baseline memulihkan seed ke keadaan awal sebelum spec dijalankan.
- Tabel baris uji per Status (TC-30 langkah 27 sampai 31, TC-35 langkah 85 sampai 90):

| Allocation ID | Status | Allocated By (PIC) |
|---|---|---|
| `HALC-20260901-00001` | `Completed` | Budi S |
| `HALC-20260901-00002` | `Waiting for Approval` | Siti R |
| `HALC-20260902-00002` | `Rejected` | Hendra W |
| `HALC-20260901-00003` | `Canceled` | Andi W |

- Kemampuan teknis: intercept penundaan respons permintaan log selama 3 detik (TC-33), dilepas segera sesudah asersi Loading; izin clipboard diberikan pada browser uji (TC-32); kemampuan membaca jumlah baris Activity Log dan System Log (Detail User Admin Pratama) sebagai baseline sebelum dan sesudah aksi (TC-32; audit trail permanen sehingga jumlah dibaca, tidak diturunkan dari seeding); jeda nyata 2 detik pada TC-32 (tooltip inline Copied to clipboard tampil selama 2 detik).
- General Settings Pre-setup #1 tidak diubah. State global: tidak ada yang diubah; suite berjalan serial.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_DA_TC_DIST_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` dan `.env.example` pada tahap script. Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-ACHA-29: Screening modal Allocation Log

1. Klik Allocation ID `HALC-20260901-00001`
2. Amati modal dari atas ke bawah
3. Verifikasi header modal berjudul `Allocation Log`
4. Verifikasi header menampilkan Allocation ID `HALC-20260901-00001`
5. Verifikasi header menampilkan ikon Copy di samping Allocation ID
6. Verifikasi header menampilkan status badge `Completed`
7. Verifikasi header menampilkan Client `PT Sejahtera Logistik`
8. Verifikasi header menampilkan Paid From `PT ABC (Principal)`
9. Verifikasi header menampilkan ikon close `[×]`
10. Verifikasi body berupa daftar log berbentuk timeline vertikal (satu titik penanda per entri)
11. Verifikasi body bukan tabel
12. Verifikasi entri terbaru berada di atas
13. Verifikasi body tanpa Search, Filter, Sort, Setup Column, Download, kolom, maupun paginasi
14. Verifikasi tidak ada footer
15. Verifikasi tidak ada tombol aksi (`Edit`, `Cancel Allocation`, `Resubmit`, `Review`, `Approve`, `Reject` tidak tampil)
16. Verifikasi Breadcrumb tidak ada di modal
17. Klik ikon close `[×]`

### TC-AC-ACHA-30: Dua jalur pembuka modal Allocation Log

18. Klik Allocation ID `HALC-20260901-00001`
19. Verifikasi modal Allocation Log untuk Allocation ID `HALC-20260901-00001` terbuka
20. Klik ikon close `[×]`
21. Klik `[⋯]` pada baris `HALC-20260901-00001`
22. Verifikasi row action `Allocation Log` berikon `FileInfoLine` severity dark
23. Klik `Allocation Log`
24. Verifikasi modal Allocation Log yang sama untuk Allocation ID `HALC-20260901-00001` terbuka
25. Klik ikon close `[×]`
26. Untuk setiap baris tabel "Baris uji per Status" lakukan langkah 27 sampai 31
27. Ketik Search `Allocation ID` pada baris tabel, tekan Enter
28. Klik `[⋯]` pada baris hasil
29. Verifikasi row action `Allocation Log` tampil pada baris berstatus sesuai kolom "Status"
30. Tekan Esc untuk menutup menu
31. Klik `(←)` pada kotak Search

### TC-AC-ACHA-31: Menutup modal lewat Esc dan ikon close; backdrop tidak menutup

32. Klik nomor halaman 2
33. Klik Allocation ID pada baris pertama halaman 2
34. Klik area backdrop di luar modal
35. Verifikasi modal tetap terbuka
36. Tekan Esc
37. Verifikasi modal tertutup
38. Klik Allocation ID pada baris pertama halaman 2
39. Klik ikon close `[×]`
40. Verifikasi modal tertutup
41. Verifikasi halaman List di belakangnya tidak berubah: halaman 2 tetap aktif
42. Verifikasi halaman List di belakangnya tidak berubah: indikator sort tetap pada Last Updated
43. Klik nomor halaman 1

### TC-AC-ACHA-32: Ikon Copy menyalin Allocation ID dan tidak dicatat sebagai kejadian

44. Buka Activity Log di Admin Console lewat sidebar
45. Verifikasi tabel Activity Log menampilkan sedikitnya satu baris
46. Ketik Search `HALC-20260901-00001`, tekan Enter
47. Catat jumlah baris hasil Activity Log (baseline Activity Log)
48. Buka Detail User Admin Pratama dan tab System Log
49. Verifikasi tabel System Log menampilkan sedikitnya satu baris
50. Ketik Search `HALC-20260901-00001`, tekan Enter
51. Catat jumlah baris hasil System Log (baseline System Log)
52. Buka Allocation > Device Allocation lewat sidebar
53. Klik Allocation ID `HALC-20260901-00001`
54. Catat jumlah entri pada daftar log modal (baseline modal)
55. Arahkan kursor ke ikon Copy di samping Allocation ID
56. Verifikasi tooltip ikon Copy `Copy to clipboard`
57. Klik ikon Copy
58. Verifikasi tooltip inline `Copied to clipboard` tampil
59. Verifikasi tidak ada toast
60. Tunggu 2 detik
61. Verifikasi tooltip inline `Copied to clipboard` hilang
62. Verifikasi jumlah entri pada daftar log modal sama dengan baseline modal (penyalinan tidak menambah entri)
63. Klik ikon close `[×]`
64. Tempel isi clipboard ke kotak Search, tekan Enter
65. Verifikasi kotak Search berisi persis `HALC-20260901-00001` (isi clipboard)
66. Verifikasi pencarian menampilkan baris `HALC-20260901-00001`
67. Klik `(←)` pada kotak Search
68. Buka Activity Log di Admin Console lewat sidebar
69. Verifikasi tabel Activity Log menampilkan sedikitnya satu baris
70. Ketik Search `HALC-20260901-00001`, tekan Enter
71. Verifikasi jumlah baris hasil Activity Log sama dengan baseline Activity Log (tidak ada dokumen baru akibat pembukaan modal maupun penyalinan)
72. Buka Detail User Admin Pratama dan tab System Log
73. Verifikasi tabel System Log menampilkan sedikitnya satu baris
74. Ketik Search `HALC-20260901-00001`, tekan Enter
75. Verifikasi jumlah baris hasil System Log sama dengan baseline System Log (tidak ada dokumen baru akibat pembukaan modal maupun penyalinan)
76. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-33: State Loading pada modal Allocation Log

77. Tahan respons permintaan log selama 3 detik (intercept)
78. Klik Allocation ID `HALC-20260901-00001`
79. Verifikasi modal terbuka
80. Verifikasi daftar log menampilkan komponen Loading
81. Lepas tahanan respons (hapus intercept) dan tunggu respons diterima
82. Verifikasi entri log tampil
83. Klik ikon close `[×]`

### TC-AC-ACHA-35: Daftar log tidak pernah kosong

84. Untuk setiap baris tabel "Baris uji per Status" lakukan langkah 85 sampai 90
85. Ketik Search `Allocation ID` pada baris tabel, tekan Enter
86. Klik Allocation ID pada baris hasil
87. Verifikasi modal memuat minimal satu entri `Allocation created by [PIC]` dengan PIC sesuai kolom "Allocated By (PIC)"
88. Verifikasi tidak ada empty state pada daftar log
89. Klik ikon close `[×]`
90. Klik `(←)` pada kotak Search

### Ganti akun ke Total Control Distributor

91. Logout dari akun Total Control Principal
92. Login sebagai Total Control Distributor (`totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_TC_DIST_PASSWORD`)
93. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-36: Scroll internal daftar log dengan header tetap

94. Ketik Search `Allocation ID` transaksi Pre-setup #58, tekan Enter
95. Klik Allocation ID pada baris hasil
96. Amati posisi header modal (Allocation ID, Status, Client, Paid From) sebelum scroll
97. Verifikasi entri terbaru berada di atas
98. Scroll daftar log sampai entri terbawah
99. Verifikasi daftar log scroll di dalam modal
100. Verifikasi header (Allocation ID, Status, Client, Paid From) tetap di tempat dan tidak ikut scroll
101. Verifikasi tidak ada kontrol sort pada daftar log
102. Klik ikon close `[×]` dan klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Spec mekanik modal Allocation Log; hanya membaca (tidak ada aksi tulis).
- Pengecualian S-12 nama literal: seed Pre-setup #48 bernilai literal (lihat spec 001 Notes). Isi entri log per kejadian diuji di spec 047; pencatatan log aksi di spec 046.
- Langkah penghubung (S-03): langkah ganti akun (tiga langkah di subjudul "Ganti akun ke Total Control Distributor"), penutupan modal (`[×]`), reset Search (`(←)`), pencarian untuk menemukan baris target (langkah 27, 85, dan pencarian pada TC-36), langkah 32 dan 43 (pindah halaman 2 dan kembali ke halaman 1 agar "halaman List tidak berubah" pada TC-31 teramati), dan langkah penghubung navigasi antar surface pada TC-32. Langkah pencatatan baseline (Catat jumlah ...) adalah baseline S-12.
- Perlakuan klausa absence TC-32 d (S-05, kelas g): klausa "Activity Log dan System Log tidak memuat dokumen baru" diterima di spec fungsional ini, ditulis dengan baseline jumlah baris dan anchor positif (tabel log menampilkan sedikitnya satu baris), karena spec 049 tidak memuat aksi buka modal dan Copy sehingga merujuknya bukan pemenuhan Expected; butir `P-1` tidak diklaim karena aksinya bukan state berat (lihat Temuan untuk QA).
- Ukuran spec (di atas sekitar 35 langkah): semua blok membaca satu permukaan (modal Allocation Log) dari dataset seed yang sama tanpa mengubah state; tiap blok berdiri sendiri karena memuat dan menutup modal sendiri, dan TC-36 memakai ganti akun eksplisit dengan data sendiri. Sebagian besar langkah TC-32 berasal dari baseline Activity Log dan System Log (anchor, pencarian, dan pembacaan sebelum dan sesudah aksi).
- Pembagian TC lintas spec: TC-34 (error load modal) ada di spec 058; klausa absence log aksi ditolak ada di spec 049 dan 054/055.
- Temuan untuk QA:
  - TC-32 Expected d ("Activity Log dan System Log tidak memuat dokumen baru") adalah asersi absence (kelas g); klausa absence ini tetap di spec asal dengan baseline dan anchor positif (S-05) karena aksinya bukan permintaan langsung yang ditolak.
  - TC-32 Langkah Uji 4 tidak menyebut jalur menu untuk membuka Activity Log dan System Log (Detail User Admin Pratama); spec memakai nama halaman saja, jalur menu menjadi tanggung jawab Page Object.
  - TC-31 Expected c menyebut "Search, Filter, Sort, halaman tetap" tetapi Langkah Uji tidak mengatur state Search atau Filter; spec hanya mengatur halaman 2 (sort default tetap) untuk mengamati klausa itu.
  - TC-30 Expected b menyatakan row action `Allocation Log` "selalu tampil pada baris apa pun status transaksinya" sedangkan Langkah Uji hanya satu baris; spec mengulang pada empat baris Status (langkah 27 sampai 31).
  - TC-36 Data Uji menulis "12 entri Edit" sedangkan Pre-setup #58 menyebut 13 entri log (termasuk Allocation created); spec tidak mengasersi jumlah entri.
