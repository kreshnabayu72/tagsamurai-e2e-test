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

- Mode: FE+BE (intercept parsial di atas backend nyata). Respons yang dipaksa lewat `Spectra.intercept()` pada request yang dimaksud TC (kontrak: `API/openapi.yaml` modul Handheld Reader):
  - Request edit Alias Name: `PATCH /v2/hardware-tagging/handheld-readers/{readerId}/alias-name`; request edit Reader Power: `PATCH /v2/hardware-tagging/handheld-readers/{readerId}/reader-power`. Respons 500 (langkah 1 dan 16); ditunda hingga timeout lalu request dibuang tanpa diteruskan ke server (langkah 30).
  - Request aktivasi: `POST /v2/hardware-tagging/handheld-readers`. Respons 500 (langkah 47); ditunda hingga timeout lalu request dibuang tanpa diteruskan ke server (langkah 65); respons 500 satu kali lalu diteruskan (langkah 86); ditunda hingga timeout tetapi request tetap diteruskan ke server (langkah 109).
  - Intercept dilepas segera setelah pemicunya selesai (S-09).
- Suite serial (`parallel: false`). State global yang diubah spec ini: (a) `Alias Name` reader DD-01 menjadi `Reader Dock 01-{runId}-026` dan satu entri Changelog `Alias Name` (langkah 39); (b) tiga aktivasi unit `SN-HHR-00201` menjadi reader `Zebra RFID Reader - 2` (langkah 77, 93, dan 114: Submit pertama TC-GS-HHR-436 yang tetap diteruskan ke server) dan kartu `Long Range` menjadi `6 of 6` pada momen aktivasi. Dua reader pertama dihapus oleh spec lewat `Delete` agar kuota `Long Range` pulih (NC-06: Delete reader Jalur A mengembalikan unit ke `Available` di Hardware Stock). Hook `after` melepas semua intercept, menghapus reader sisa, dan memulihkan Seed Reader A lewat fixture backend (DD-01 memakai data Pre-setup bersama karena TC menetapkannya; efek yang tersisa hanya `Alias Name` dan Last Updated DD-01 dan entri Changelog, dipulihkan oleh fixture).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.
- Akun aktor (login di hook `before`, bukan di langkah): Total Control Sari Dewi, Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (Client A): Seed Reader A (DD-01 sampai DD-10), plan Growth, `Long Range` terpakai 5 dari 6, General Settings `dd/MM/yy` 24-hour Asia/Jakarta. DD-01 (Device Name `Zebra RFID Reader - 1`, Serial Number `SN-HHR-00101`, Alias Name `—`, Reader Power `30 dBm`, Available) ditemukan lewat Search Serial Number karena Device Name-nya sama dengan DD-06. HS-01 `SN-HHR-00201` (SKU-HHR-01, Long Range, Zebra RFD40, Current Power 22 dBm, nomor urut 2) tersedia di stok Principal. Total reader N = 10 (dari seeding). Fixture baru `Fixture.hardwareHandheldReader.resilienceTulis026`.
- Data Dinamis: Alias Name `Reader Dock 01-{runId}-026` (TC-GS-HHR-121, 122, 96); tidak ada data bernama lain yang dibuat spec; nama baris hasil aktivasi `Zebra RFID Reader - 2` mengikuti nomor urut unit HS-01 (HHR-LOGIC-02g) dan dipakai apa adanya karena Expected TC menyebutnya.
- Baseline: jumlah entri Changelog dicatat sebelum aksi pemicu TC-GS-HHR-122 (langkah 29); jumlah entri Event Log dicatat sebelum aksi pemicu TC-GS-HHR-368 (langkah 85).
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 500, menunda respons hingga timeout dengan atau tanpa meneruskan request ke server, memicu 500 satu kali, dan membuang request tanpa meneruskannya ke server; simulator reader USB (sambung reader dengan Serial Number tertentu, dibaca oleh `[Sync]`; mekanisme tidak didefinisikan di TC, PRD, atau LLD sehingga disediakan tim FE); membaca toast beserta ketahanannya (toast error tidak hilang otomatis; `foundation/functions/toast-copy.md`) dan men-dismiss toast; membaca total reader pada daftar; pembacaan jumlah entri Modal Changelog dan Popup Event Log Activate (baseline, S-12), disediakan tim FE/BE.

## Test Steps

### TC-GS-HHR-121: Save Edit Alias Name gagal 5xx mempertahankan dialog dan input

1. Pasang intercept pada request edit: respons 500
2. Ketik Search `SN-HHR-00101`, tekan Enter
3. Klik `⋯` pada baris DD-01, pilih `Edit Alias Name`
4. Isi `Alias Name` dengan `Reader Dock 01-{runId}-026`
5. Klik `[Save]`
6. Verifikasi toast error "Error, failed to update device." tampil
7. Verifikasi dialog Edit Alias Name tetap terbuka
8. Verifikasi `Alias Name` dialog tetap `Reader Dock 01-{runId}-026`
9. Verifikasi `[Save]` enabled
10. Dismiss toast error
11. Klik `✕` di header dialog
12. Verifikasi dialog `Unsaved Changes` tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` `[Leave]`
13. Klik `[Leave]`
14. Verifikasi kolom `Alias Name` baris DD-01 tetap `—`
15. Lepas intercept pada request edit

### TC-GS-HHR-137: Save Edit Reader Power gagal 5xx mempertahankan dialog

16. Pasang intercept pada request edit: respons 500
17. Klik `⋯` pada baris DD-01, pilih `Edit Reader Power`
18. Geser slider `Reader Power` ke 25 dBm
19. Klik `[Save]`
20. Verifikasi toast error "Error, failed to update device." tampil
21. Verifikasi dialog Edit Reader Power tetap terbuka pada `25 dBm`
22. Verifikasi `[Save]` enabled
23. Dismiss toast error
24. Klik `✕` di header dialog
25. Verifikasi dialog `Unsaved Changes` tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` `[Leave]`
26. Klik `[Leave]`
27. Verifikasi kolom `Reader Power` baris DD-01 tetap `30 dBm`
28. Lepas intercept pada request edit

### TC-GS-HHR-122: Timeout saat Save Edit Alias Name, retry diperlakukan sebagai kirim ulang

29. Klik ikon Changelog, catat jumlah entri Changelog sebagai baseline, lalu tutup Modal Changelog lewat `✕`
30. Pasang intercept pada request edit: ditunda hingga timeout, lalu request dibuang tanpa diteruskan ke server
31. Klik `⋯` pada baris DD-01, pilih `Edit Alias Name`
32. Isi `Alias Name` dengan `Reader Dock 01-{runId}-026`
33. Klik `[Save]`
34. Verifikasi toast error "Connection problem. Please try again." tampil tanpa tombol aksi
35. Verifikasi dialog Edit Alias Name tetap terbuka
36. Verifikasi `Alias Name` dialog tetap `Reader Dock 01-{runId}-026`
37. Dismiss toast error
38. Lepas intercept pada request edit
39. Klik `[Save]`
40. Verifikasi toast sukses "Success, Reader Dock 01-{runId}-026 has been updated."
41. Verifikasi dialog Edit Alias Name tertutup
42. Verifikasi kolom `Alias Name` baris DD-01 menampilkan `Reader Dock 01-{runId}-026`
43. Klik ikon Changelog
44. Verifikasi jumlah entri Changelog bertambah tepat satu dari baseline
45. Tutup Modal Changelog lewat `✕`
46. Klik `(←)` pada kotak Search

### TC-GS-HHR-96: Submit aktivasi gagal 5xx mempertahankan popup dan input

47. Pasang intercept pada request aktivasi: respons 500
48. Klik `[+ Activate Reader]`
49. Klik `Long Range` pada Overlay `Select Range Type`
50. Sambungkan reader USB dengan Serial Number `SN-HHR-00201` lewat simulator USB
51. Klik `[Sync]`
52. Isi `Alias Name` dengan `Reader Dock 01-{runId}-026`
53. Klik `[Submit]`
54. Verifikasi toast error "Error, failed to activate device." tampil
55. Verifikasi Popup Activate tetap terbuka
56. Verifikasi `Serial Number` tetap `SN-HHR-00201`
57. Verifikasi `Alias Name` tetap `Reader Dock 01-{runId}-026`
58. Verifikasi `[Submit]` enabled
59. Dismiss toast error
60. Lepas intercept pada request aktivasi
61. Klik `[✕]`
62. Verifikasi dialog `Cancel Activation` tampil dengan body "Are you sure you want to cancel this activation? The Sync progress you've made will be lost." dan tombol `[Go Back]` `[Cancel Activation]`
63. Klik `[Cancel Activation]`
64. Verifikasi total reader pada daftar tetap 10

### TC-GS-HHR-97: Timeout jaringan saat Submit mempertahankan nomor seri dan menampilkan toast koneksi

65. Pasang intercept pada request aktivasi: ditunda hingga timeout, lalu request dibuang tanpa diteruskan ke server
66. Klik `[+ Activate Reader]`
67. Klik `Long Range` pada Overlay `Select Range Type`
68. Sambungkan reader USB dengan Serial Number `SN-HHR-00201` lewat simulator USB
69. Klik `[Sync]`
70. Klik `[Submit]`
71. Verifikasi toast error "Connection problem. Please try again." tampil tanpa tombol aksi
72. Verifikasi `Serial Number` tetap `SN-HHR-00201`
73. Verifikasi tidak ada toast sukses maupun toast error aktivasi selain toast koneksi
74. Verifikasi Popup Activate tetap terbuka dengan input dipertahankan
75. Dismiss toast error
76. Lepas intercept pada request aktivasi
77. Klik `[Submit]`
78. Verifikasi toast sukses "Success, Zebra RFID Reader - 2 has been activated."
79. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
80. Verifikasi hanya satu baris `Zebra RFID Reader - 2` pada hasil Search
81. Klik `⋯` pada baris `Zebra RFID Reader - 2`, pilih `Delete`
82. Klik `[Delete]` pada dialog
83. Tunggu aksi selesai
84. Klik `(←)` pada kotak Search

### TC-GS-HHR-368: Submit gagal 5xx lalu berhasil menghasilkan satu baris Failed dan satu baris Activated

85. Klik ikon Event Log, catat jumlah entri Event Log sebagai baseline, lalu tutup Popup Event Log lewat `✕`
86. Pasang intercept pada request aktivasi: respons 500 satu kali, permintaan berikutnya diteruskan
87. Klik `[+ Activate Reader]`
88. Klik `Long Range` pada Overlay `Select Range Type`
89. Sambungkan reader USB `SN-HHR-00201` (HS-01) lewat simulator USB
90. Klik `[Sync]`
91. Klik `[Submit]`
92. Dismiss toast error
93. Klik `[Submit]`
94. Tunggu aksi selesai
95. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
96. Verifikasi baris `Zebra RFID Reader - 2` tampil
97. Klik `(←)` pada kotak Search
98. Klik ikon Event Log
99. Verifikasi jumlah entri Event Log bertambah tepat dua dari baseline
100. Verifikasi satu baris baru ber-Result `Failed` dengan Range Type `Long Range`
101. Verifikasi satu baris baru ber-Result `Activated` dengan Range Type `Long Range`
102. Verifikasi baris `Failed` tidak dihapus atau diganti oleh baris `Activated`
103. Tutup Popup Event Log lewat `✕`
104. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
105. Klik `⋯` pada baris `Zebra RFID Reader - 2`, pilih `Delete`
106. Klik `[Delete]` pada dialog
107. Tunggu aksi selesai
108. Klik `(←)` pada kotak Search

### TC-GS-HHR-436: Retry setelah timeout tidak menggandakan reader

109. Pasang intercept pada request aktivasi: respons ditunda hingga timeout namun request tetap diteruskan ke server
110. Klik `[+ Activate Reader]`
111. Klik `Long Range` pada Overlay `Select Range Type`
112. Sambungkan reader USB `SN-HHR-00201` (HS-01) lewat simulator USB
113. Klik `[Sync]`
114. Klik `[Submit]`
115. Verifikasi toast error "Connection problem. Please try again." tampil
116. Dismiss toast error
117. Lepas intercept pada request aktivasi
118. Klik `[Submit]` kembali
119. Verifikasi pesan inline `Serial number already exists` tampil di Popup Activate
120. Klik `[✕]`
121. Verifikasi dialog `Cancel Activation` tampil dengan body "Are you sure you want to cancel this activation? The Sync progress you've made will be lost." dan tombol `[Go Back]` `[Cancel Activation]`
122. Klik `[Cancel Activation]`
123. Muat ulang halaman Handheld Reader (`F5`)
124. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
125. Verifikasi hanya satu baris `Zebra RFID Reader - 2` pada hasil Search
126. Verifikasi baris `Zebra RFID Reader - 2` tetap menampilkan `Status` `Available` dan `Reader Power` `22 dBm`
127. Verifikasi kartu `Long Range` menjadi `6 of 6`
128. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (intercept parsial). Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan blok: edit (TC-GS-HHR-121, 137, lalu 122) dulu, kemudian aktivasi (TC-GS-HHR-96, 97, 368, 436). TC-GS-HHR-137 ditaruh sebelum TC-GS-HHR-122 karena TC-GS-HHR-122 mengubah `Alias Name` DD-01 dan TC-GS-HHR-121 mengharapkan `—`. Di blok aktivasi, TC-GS-HHR-96 (tidak membuat data) dulu, lalu TC-GS-HHR-97, 368, dan 436 yang masing-masing membuat reader (pada TC-GS-HHR-436 reader dibuat oleh Submit pertama; Submit ulang ditolak). Dialog edit dibuka 3 kali dan ditutup 3 kali (2 lewat `✕`, verifikasi dialog `Unsaved Changes`, dan `[Leave]`, 1 lewat Save sukses); Popup Activate dibuka 4 kali dan ditutup 4 kali (dua lewat `[✕]`, dialog `Cancel Activation`, dan `[Cancel Activation]` pada TC-GS-HHR-96 dan 436; dua lewat Submit sukses).
- Langkah penghubung (aksi tanpa `Verifikasi`): pemasangan dan pelepasan intercept; dismiss toast error (agar toast error berikutnya yang sama tidak lulus karena toast lama, S-09); Search untuk menemukan baris target dan `(←)` untuk mengosongkan Search; baseline Changelog dan Event Log (langkah 29 dan 85); "Tunggu aksi selesai" (langkah 83, 94, dan 107: hasil `Delete` atau `[Submit]` tidak diasersi dan langkah berikutnya bergantung pada kuota atau Search, bagian 8b butir 8); penyambungan reader di simulator USB; `✕` dan `[Leave]` untuk menutup dialog edit yang dirty (S-08; dialog `Unsaved Changes` diverifikasi pada langkah 12 dan 25); dialog `Cancel Activation` pada TC-GS-HHR-96 dan 436 diverifikasi menurut S-08 (teks dari Expected TC-GS-HHR-89), dan `Delete` reader hasil TC-GS-HHR-97 dan 368 sesudah diasersi, untuk memulihkan kuota `Long Range` ke `5 of 6` sehingga `Long Range` tidak diblok gate kuota pada popup berikutnya (reader hasil TC-GS-HHR-436 dipulihkan oleh hook `after`). Karena Delete adalah pemulihan, bukan objek uji, tidak ada `Verifikasi` atasnya.
- Kelas harness: kelas b (fault injection 5xx dan timeout pada aksi tulis) dengan simulator reader USB (kelas d) sebagai pembentuk precondition. `P-8`: TC-GS-HHR-96, 97, 368, dan 436 membutuhkan `[Sync]` lewat simulator reader USB hanya untuk membentuk precondition (`[Sync]` harus menghasilkan data agar `[Submit]` aktif); objek ujinya perilaku FE atas kegagalan server, bukan reader USB atau pembacaannya. Syarat P-8 terpenuhi: blok non-USB (TC-GS-HHR-121, 137, dan 122; langkah 1 sampai 46) lebih dulu dan blok USB di akhir spec (TC-GS-HHR-96, 97, 368, dan 436; langkah 47 sampai 128), sehingga kegagalan keras simulator tidak menutupi blok edit; state antar blok dipulihkan lewat langkah penghubung (intercept dilepas, dialog ditutup, `(←)` pada Search, `Delete` reader hasil aktivasi). Intercept yang dipakai sebagai pemicu dilepas segera setelah selesai. Alasan spec tetap satu dan tidak dipecah ada pada butir ukuran di bawah.
- Spec melewati sekitar 35 langkah (128 langkah nominal, 42 di antaranya `Verifikasi` yang dipecah per klausa Expected, S-01). Alasan: seluruh blok satu topik (resilience aksi tulis) dan satu akun aktor; empat blok aktivasi memakai simulator USB hanya sebagai precondition. Blok edit (TC-GS-HHR-121, 137, 122) dan blok aktivasi (TC-GS-HHR-96, 97, 368, 436) berdiri sendiri: tiap TC membuka dialog atau popup sendiri dan memulihkan state di akhirnya (tutup dialog, hapus reader), sehingga kegagalan keras satu blok tidak menghilangkan makna blok lain. Spec edit-saja dan spec aktivasi-saja sah dipecah bila diinginkan, tetapi konvensi menetapkan satu spec per kelas per modul (bagian 3, prinsip 13 "Cara menggabung antar-aksi").
- Pembagian TC lintas spec: TC-GS-HHR-147, 155, 160, 225, 226, dan 352 (kegagalan 5xx status, Delete, Cancel Request, bulk, dan log) ada di spec 027; TC-GS-HHR-184, 315, dan 339 (kegagalan unduh) ada di spec 028. Asersi absence log pada TC-GS-HHR-352 ada di spec 027.
- Alias Name `Reader Dock 01` pada TC-GS-HHR-121, 122, dan 96 ditulis bersuffix per run (`Reader Dock 01-{runId}-026`) mengikuti S-12.
- Temuan untuk QA:
  - TC-GS-HHR-96, 97, 368, dan 436 berlabel `Manual Only` (b) di TC sumber (reader USB fisik) dan TC-GS-HHR-121, 122, 137 `Automatable`; semuanya tetap ditulis (konvensi bagian 2). Mekanisme simulasi reader USB tidak didefinisikan di TC, PRD, atau LLD; spec tidak mengarang endpoint dan menyatakannya "disediakan tim FE".
  - TC-GS-HHR-121, 122, dan 137 menyebut target `baris DD-01`, sedangkan Device Name DD-01 dan DD-06 sama (`Zebra RFID Reader - 1`); spec menemukan DD-01 lewat Search Serial Number `SN-HHR-00101`. TC-GS-HHR-122 mengubah `Alias Name` DD-01 (data Pre-setup bersama), dipulihkan oleh fixture backend (S-06 terpaksa karena TC menetapkan DD-01).
  - TC-GS-HHR-368 langkah 2 menulis `[Submit]` (gagal) lalu `[Submit]` lagi tanpa menyebut dismiss toast error; spec men-dismiss toast error di antaranya sebagai langkah penghubung.
  - Pemulihan antar-TC (`Delete` reader hasil aktivasi) bergantung pada asumsi bahwa Delete reader Jalur A mengembalikan unit ke `Available` (NC-06) dan nama bawaan aktivasi ulang tetap `Zebra RFID Reader - 2` (nomor urut unit HS-01). TC tidak menyatakan ini.
  - TC-GS-HHR-122 menyebut entri Changelog `Alias Name` untuk DD-01 bertambah satu; spec mengasersi selisih jumlah entri Changelog terhadap baseline (S-12) dan tidak memfilter per reader.
  - TC-GS-HHR-436 Expected a menyebut pengiriman ulang "tidak mengubah reader yang sudah ada" tanpa nilai pembanding; spec mengasersinya lewat `Status` `Available` dan `Reader Power` `22 dBm` (nilai hasil aktivasi Jalur A HS-01 menurut TC-GS-HHR-64) setelah muat ulang.
  - TC-GS-HHR-121 dan 137 tidak menyebut cara menutup dialog edit sesudah kegagalan; spec memakai `✕`, `Verifikasi` dialog `Unsaved Changes`, dan `[Leave]` (S-08). Teks dialog (body "You have unsaved changes. Are you sure you want to leave?", tombol `[Cancel]` `[Leave]`) diambil dari Expected a TC-GS-HHR-115 (Edit Alias Name) dan TC-GS-HHR-134 (Edit Reader Power).
