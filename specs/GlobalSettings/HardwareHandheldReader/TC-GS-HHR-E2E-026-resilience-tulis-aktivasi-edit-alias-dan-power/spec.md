---
id: TC-GS-HHR-E2E-026-resilience-tulis-aktivasi-edit-alias-dan-power
title: "Resilience Tulis: Aktivasi, Edit Alias Name, dan Edit Reader Power saat Kegagalan Server 5xx dan Timeout, Retry setelah Timeout"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-HHR-96
  - TC-GS-HHR-97
  - TC-GS-HHR-121
  - TC-GS-HHR-122
  - TC-GS-HHR-137
  - TC-GS-HHR-368
  - TC-GS-HHR-436
coverage:
  web: automated
---

# Resilience Tulis: Aktivasi, Edit Alias Name, dan Edit Reader Power saat Kegagalan Server 5xx dan Timeout, Retry setelah Timeout

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata). Respons yang dipaksa lewat `Spectra.intercept()` pada request yang dimaksud TC (endpoint tidak disebut di TC, PRD, atau LLD yang dirujuk spec ini, sehingga tidak dituliskan):
  - Request edit (Alias Name dan Reader Power): respons 500 (langkah 1 dan 14); ditunda hingga timeout (langkah 26).
  - Request aktivasi: respons 500 (langkah 44); ditunda hingga timeout tanpa diteruskan ke server (langkah 60); respons 500 satu kali lalu diteruskan (langkah 80); ditunda hingga timeout tetapi request tetap diteruskan ke server (langkah 102).
  - Intercept dilepas segera setelah pemicunya selesai (S-09).
- Suite serial (`parallel: false`). State global yang diubah spec ini: (a) `Alias Name` reader DD-01 menjadi `Reader Dock 01` dan satu entri Changelog `Alias Name` (langkah 35); (b) tiga aktivasi sukses unit `SN-HHR-00201` menjadi reader `Zebra RFID Reader - 2` (langkah 71, 87, 111) dan kartu `Long Range` menjadi `6 of 6` pada momen aktivasi. Dua reader pertama dihapus oleh spec lewat `Delete` agar kuota `Long Range` pulih (NC-06: Delete reader Jalur A mengembalikan unit ke `Available` di Hardware Stock). Hook `after` melepas semua intercept, menghapus reader sisa, dan memulihkan Seed Reader A lewat fixture backend (DD-01 memakai data Pre-setup bersama karena TC menetapkannya; efek yang tersisa hanya `Alias Name` dan Last Updated DD-01 dan entri Changelog, dipulihkan oleh fixture).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.
- Akun aktor (login di hook `before`, bukan di langkah): Total Control Sari Dewi, Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (Client A): Seed Reader A (DD-01 sampai DD-10), plan Growth, `Long Range` terpakai 5 dari 6, General Settings `dd/MM/yy` 24-hour Asia/Jakarta. DD-01 (Device Name `Zebra RFID Reader - 1`, Serial Number `SN-HHR-00101`, Alias Name `—`, Reader Power `30 dBm`, Available) ditemukan lewat Search Serial Number karena Device Name-nya sama dengan DD-06. HS-01 `SN-HHR-00201` (SKU-HHR-01, Long Range, Zebra RFD40, Current Power 22 dBm, nomor urut 2) tersedia di stok Principal. Total reader N = 10 (dari seeding). Fixture baru `Fixture.hardwareHandheldReader.resilienceTulis026`.
- Data Dinamis: tidak ada data bernama yang dibuat spec; nama baris hasil aktivasi `Zebra RFID Reader - 2` mengikuti nomor urut unit HS-01 (HHR-LOGIC-02g) dan dipakai apa adanya karena Expected TC menyebutnya.
- Baseline: jumlah entri Changelog dicatat sebelum aksi pemicu TC-GS-HHR-122 (langkah 25); jumlah entri Event Log dicatat sebelum aksi pemicu TC-GS-HHR-368 (langkah 79).
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 500, menunda respons hingga timeout dengan atau tanpa meneruskan request ke server, memicu 500 satu kali, dan membaca request yang dikirim ulang (untuk membandingkan kunci idempotensi permintaan pertama dan kedua tanpa menamai header karena TC tidak menyebutnya); simulator reader USB (sambung reader dengan Serial Number tertentu, dibaca oleh `[Sync]`; mekanisme tidak didefinisikan di TC, PRD, atau LLD sehingga disediakan tim FE); membaca toast beserta ketahanannya (toast error tidak hilang otomatis; `foundation/functions/toast-copy.md`) dan men-dismiss toast; membaca total reader pada daftar.

## Test Steps

### TC-GS-HHR-121: Save Edit Alias Name gagal 5xx mempertahankan dialog dan input

1. Pasang intercept pada request edit: respons 500
2. Ketik Search `SN-HHR-00101`, tekan Enter
3. Klik `⋯` pada baris DD-01, pilih `Edit Alias Name`
4. Isi `Alias Name` dengan `Reader Dock 01`
5. Klik `[Save]`
6. Verifikasi toast error "Error, failed to update device." tampil
7. Verifikasi dialog Edit Alias Name tetap terbuka
8. Verifikasi `Alias Name` dialog tetap `Reader Dock 01`
9. Verifikasi `[Save]` enabled
10. Dismiss toast error
11. Klik `✕` di header dialog, lalu klik `[Leave]` pada dialog `Unsaved Changes`
12. Verifikasi kolom `Alias Name` baris DD-01 tetap `—`
13. Lepas intercept pada request edit

### TC-GS-HHR-137: Save Edit Reader Power gagal 5xx mempertahankan dialog

14. Pasang intercept pada request edit: respons 500
15. Klik `⋯` pada baris DD-01, pilih `Edit Reader Power`
16. Geser slider `Reader Power` ke 25 dBm
17. Klik `[Save]`
18. Verifikasi toast error "Error, failed to update device." tampil
19. Verifikasi dialog Edit Reader Power tetap terbuka pada `25 dBm`
20. Verifikasi `[Save]` enabled
21. Dismiss toast error
22. Klik `✕` di header dialog, lalu klik `[Leave]` pada dialog `Unsaved Changes`
23. Verifikasi kolom `Reader Power` baris DD-01 tetap `30 dBm`
24. Lepas intercept pada request edit

### TC-GS-HHR-122: Timeout saat Save Edit Alias Name, retry diperlakukan sebagai kirim ulang

25. Klik ikon Changelog, catat jumlah entri Changelog sebagai baseline, lalu tutup Modal Changelog lewat `✕`
26. Pasang intercept pada request edit: ditunda hingga timeout
27. Klik `⋯` pada baris DD-01, pilih `Edit Alias Name`
28. Isi `Alias Name` dengan `Reader Dock 01`
29. Klik `[Save]`
30. Verifikasi toast error "Connection problem. Please try again." tampil tanpa tombol aksi
31. Verifikasi dialog Edit Alias Name tetap terbuka
32. Verifikasi `Alias Name` dialog tetap `Reader Dock 01`
33. Dismiss toast error
34. Lepas intercept pada request edit
35. Klik `[Save]`
36. Verifikasi permintaan yang dikirim ulang sama dengan permintaan pertama dan membawa kunci idempotensi yang sama
37. Verifikasi toast sukses "Success, Reader Dock 01 has been updated."
38. Verifikasi dialog Edit Alias Name tertutup
39. Verifikasi kolom `Alias Name` baris DD-01 menampilkan `Reader Dock 01`
40. Klik ikon Changelog
41. Verifikasi jumlah entri Changelog bertambah tepat satu dari baseline
42. Tutup Modal Changelog lewat `✕`
43. Klik `(←)` pada kotak Search

### TC-GS-HHR-96: Submit aktivasi gagal 5xx mempertahankan popup dan input

44. Pasang intercept pada request aktivasi: respons 500
45. Klik `[+ Activate Reader]`
46. Klik `Long Range` pada Overlay `Select Range Type`
47. Sambungkan reader USB dengan Serial Number `SN-HHR-00201` lewat simulator USB
48. Klik `[Sync]`
49. Isi `Alias Name` dengan `Reader Dock 01`
50. Klik `[Submit]`
51. Verifikasi toast error "Error, failed to activate device." tampil
52. Verifikasi Popup Activate tetap terbuka
53. Verifikasi `Serial Number` tetap `SN-HHR-00201`
54. Verifikasi `Alias Name` tetap `Reader Dock 01`
55. Verifikasi `[Submit]` enabled
56. Dismiss toast error
57. Lepas intercept pada request aktivasi
58. Klik `[✕]`, lalu klik `[Cancel Activation]`
59. Verifikasi total reader pada daftar tetap 10

### TC-GS-HHR-97: Timeout jaringan saat Submit mempertahankan nomor seri dan menampilkan toast koneksi

60. Pasang intercept pada request aktivasi: ditunda hingga timeout (tidak diteruskan ke server)
61. Klik `[+ Activate Reader]`
62. Klik `Long Range` pada Overlay `Select Range Type`
63. Sambungkan reader USB dengan Serial Number `SN-HHR-00201` lewat simulator USB
64. Klik `[Sync]`
65. Klik `[Submit]`
66. Verifikasi toast error "Connection problem. Please try again." tampil tanpa tombol aksi
67. Verifikasi `Serial Number` tetap `SN-HHR-00201`
68. Verifikasi tidak ada toast sukses maupun toast error aktivasi selain toast koneksi
69. Dismiss toast error
70. Lepas intercept pada request aktivasi
71. Klik `[Submit]`
72. Verifikasi permintaan yang dikirim ulang sama dengan permintaan pertama dan membawa kunci idempotensi yang sama
73. Verifikasi toast sukses "Success, Zebra RFID Reader - 2 has been activated."
74. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
75. Verifikasi hanya satu baris `Zebra RFID Reader - 2` pada hasil Search
76. Klik `⋯` pada baris `Zebra RFID Reader - 2`, pilih `Delete`
77. Klik `[Delete]` pada dialog
78. Klik `(←)` pada kotak Search

### TC-GS-HHR-368: Submit gagal 5xx lalu berhasil menghasilkan satu baris Failed dan satu baris Activated

79. Klik ikon Event Log, catat jumlah entri Event Log sebagai baseline, lalu tutup Popup Event Log lewat `✕`
80. Pasang intercept pada request aktivasi: respons 500 satu kali, permintaan berikutnya diteruskan
81. Klik `[+ Activate Reader]`
82. Klik `Long Range` pada Overlay `Select Range Type`
83. Sambungkan reader USB `SN-HHR-00201` (HS-01) lewat simulator USB
84. Klik `[Sync]`
85. Klik `[Submit]`
86. Dismiss toast error
87. Klik `[Submit]`
88. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
89. Verifikasi baris `Zebra RFID Reader - 2` tampil
90. Klik `(←)` pada kotak Search
91. Klik ikon Event Log
92. Verifikasi jumlah entri Event Log bertambah tepat dua dari baseline
93. Verifikasi satu baris baru ber-Result `Failed` dengan Range Type `Long Range`
94. Verifikasi satu baris baru ber-Result `Activated` dengan Range Type `Long Range`
95. Verifikasi baris `Failed` tidak dihapus atau diganti oleh baris `Activated`
96. Verifikasi baris `Activated` tampil di atas baris `Failed` pada urutan Date descending
97. Tutup Popup Event Log lewat `✕`
98. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
99. Klik `⋯` pada baris `Zebra RFID Reader - 2`, pilih `Delete`
100. Klik `[Delete]` pada dialog
101. Klik `(←)` pada kotak Search

### TC-GS-HHR-436: Retry setelah timeout tidak menggandakan reader

102. Pasang intercept pada request aktivasi: respons ditunda hingga timeout namun request tetap diteruskan ke server
103. Klik `[+ Activate Reader]`
104. Klik `Long Range` pada Overlay `Select Range Type`
105. Sambungkan reader USB `SN-HHR-00201` (HS-01) lewat simulator USB
106. Klik `[Sync]`
107. Klik `[Submit]`
108. Verifikasi toast error "Connection problem. Please try again." tampil
109. Dismiss toast error
110. Lepas intercept pada request aktivasi
111. Klik `[Submit]`
112. Verifikasi permintaan yang dikirim ulang sama dengan permintaan pertama dan membawa kunci idempotensi yang sama
113. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
114. Verifikasi hanya satu baris `Zebra RFID Reader - 2` pada hasil Search
115. Verifikasi kartu `Long Range` menjadi `6 of 6`
116. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (intercept parsial). Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan blok: edit (TC-GS-HHR-121, 137, lalu 122) dulu, kemudian aktivasi (TC-GS-HHR-96, 97, 368, 436). TC-GS-HHR-137 ditaruh sebelum TC-GS-HHR-122 karena TC-GS-HHR-122 mengubah `Alias Name` DD-01 dan TC-GS-HHR-121 mengharapkan `—`. Di blok aktivasi, TC-GS-HHR-96 (tidak membuat data) dulu, lalu TC-GS-HHR-97, 368, dan 436 yang masing-masing membuat reader. Dialog edit dibuka 3 kali dan ditutup 3 kali (2 lewat `✕` dan `[Leave]`, 1 lewat Save sukses); Popup Activate dibuka 4 kali dan ditutup 4 kali (satu lewat `[✕]` dan `[Cancel Activation]`, tiga lewat Submit sukses).
- Langkah penghubung (aksi tanpa `Verifikasi`): pemasangan dan pelepasan intercept; dismiss toast error (agar toast error berikutnya yang sama tidak lulus karena toast lama, S-09); Search untuk menemukan baris target dan `(←)` untuk mengosongkan Search; baseline Changelog dan Event Log (langkah 25 dan 79); penyambungan reader di simulator USB; `✕` dan `[Leave]` untuk menutup dialog edit yang dirty (S-08; dialog `Unsaved Changes` tidak perlu dicatat lagi); `Delete` reader hasil TC-GS-HHR-97 dan 368 sesudah diasersi, untuk memulihkan kuota `Long Range` ke `5 of 6` sehingga `Long Range` tidak diblok gate kuota pada popup berikutnya (reader hasil TC-GS-HHR-436 dipulihkan oleh hook `after`). Karena Delete adalah pemulihan, bukan objek uji, tidak ada `Verifikasi` atasnya.
- Pengecualian P-2: Sync reader USB pada TC-GS-HHR-96, 97, 368, dan 436 hanya membentuk state yang dibutuhkan agar `[Submit]` aktif (precondition TC); objek uji adalah perilaku FE atas kegagalan server, bukan pembacaan reader. Intercept yang dipakai sebagai pemicu dilepas segera setelah selesai.
- Spec melewati sekitar 35 langkah (116 langkah). Alasan: seluruhnya satu kelas harness (kelas b: fault injection 5xx dan timeout pada aksi tulis) dan satu akun aktor. Blok edit (TC-GS-HHR-121, 137, 122) dan blok aktivasi (TC-GS-HHR-96, 97, 368, 436) berdiri sendiri: tiap TC membuka dialog atau popup sendiri dan memulihkan state di akhirnya (tutup dialog, hapus reader), sehingga kegagalan keras satu blok tidak menghilangkan makna blok lain. Spec edit-saja dan spec aktivasi-saja sah dipecah bila diinginkan, tetapi plan menetapkan satu spec per kelas per modul (konvensi bagian 3, prinsip 13 "Cara menggabung antar-aksi").
- Pembagian TC lintas spec: TC-GS-HHR-147, 155, 160, 225, 226, dan 352 (kegagalan 5xx status, Delete, Cancel Request, bulk, dan log) ada di spec 027; TC-GS-HHR-184, 315, dan 339 (kegagalan unduh) ada di spec 028. Asersi absence log pada TC-GS-HHR-352 ada di spec 027.
- Temuan untuk QA:
  - TC-GS-HHR-96, 97, 368, dan 436 berlabel `Manual Only` (b) di TC sumber (reader USB fisik) dan TC-GS-HHR-121, 122, 137 `Automatable`; semuanya tetap ditulis (konvensi bagian 2). Mekanisme simulasi reader USB tidak didefinisikan di TC, PRD, atau LLD; spec tidak mengarang endpoint dan menyatakannya "disediakan tim FE".
  - Kontradiksi sumber: Expected TC-GS-HHR-97 d, 122 c, dan 436 a menyebut kunci idempotensi yang sama (NC-09 menyatakan pengiriman ulang manual memakai kunci idempotensi yang sama, merujuk PRD §7.2), sedangkan teks PRD §7.2 butir "Timeout atau gangguan jaringan pada aksi apa pun" menyebut kirim ulang manual "diproses sebagai permintaan baru ... (tidak ada replay berbasis kunci idempotensi)". Spec mengikuti TC dan NC-09; nama header kunci idempotensi dan cara membacanya tidak disebut di TC sehingga disediakan tim FE dan tidak dikarang.
  - Expected TC-GS-HHR-97 c ("hasil aktivasi tidak diasumsikan sukses maupun gagal") tidak punya indikator di UI; spec mengasersinya sebagai tidak adanya toast sukses atau toast error aktivasi selain toast koneksi.
  - TC-GS-HHR-121, 122, dan 137 menyebut target `baris DD-01`, sedangkan Device Name DD-01 dan DD-06 sama (`Zebra RFID Reader - 1`); spec menemukan DD-01 lewat Search Serial Number `SN-HHR-00101`. TC-GS-HHR-122 mengubah `Alias Name` DD-01 (data Pre-setup bersama), dipulihkan oleh fixture backend (S-06 terpaksa karena TC menetapkan DD-01).
  - TC-GS-HHR-121 dan 137 tidak menyebut cara menutup dialog sesudah kegagalan; spec memakai `✕` dan `[Leave]` (dialog `Unsaved Changes`) sesuai S-08.
  - TC-GS-HHR-368 b ("berurutan sesuai waktu permintaan pada urutan Date descending") tidak menyebut posisi baris yang diharapkan; spec mengasersi baris `Activated` di atas baris `Failed`.
  - TC-GS-HHR-368 langkah 2 menulis `[Submit]` (gagal) lalu `[Submit]` lagi tanpa menyebut dismiss toast error; spec men-dismiss toast error di antaranya sebagai langkah penghubung.
  - Pemulihan antar-TC (`Delete` reader hasil aktivasi) bergantung pada asumsi bahwa Delete reader Jalur A mengembalikan unit ke `Available` (NC-06) dan nama bawaan aktivasi ulang tetap `Zebra RFID Reader - 2` (nomor urut unit HS-01). TC tidak menyatakan ini.
  - TC-GS-HHR-122 menyebut entri Changelog `Alias Name` untuk DD-01 bertambah satu; spec mengasersi selisih jumlah entri Changelog terhadap baseline (S-12) dan tidak memfilter per reader.
