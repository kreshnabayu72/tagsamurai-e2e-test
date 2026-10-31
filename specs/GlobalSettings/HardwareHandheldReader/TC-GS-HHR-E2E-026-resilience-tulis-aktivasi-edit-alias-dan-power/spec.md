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
  - Request edit Alias Name: `PATCH /v2/hardware-tagging/handheld-readers/{readerId}/alias-name`; request edit Reader Power: `PATCH /v2/hardware-tagging/handheld-readers/{readerId}/reader-power`. Respons 500 (langkah 1 dan 14); ditunda hingga timeout lalu request dibuang tanpa diteruskan ke server (langkah 26).
  - Request aktivasi: `POST /v2/hardware-tagging/handheld-readers`. Respons 500 (langkah 43); ditunda hingga timeout lalu request dibuang tanpa diteruskan ke server (langkah 61); respons 500 satu kali lalu diteruskan (langkah 81); ditunda hingga timeout tetapi request tetap diteruskan ke server (langkah 103).
  - Intercept dilepas segera setelah pemicunya selesai (S-09).
- Suite serial (`parallel: false`). State global yang diubah spec ini: (a) `Alias Name` reader DD-01 menjadi `Reader Dock 01-{runId}-026` dan satu entri Changelog `Alias Name` (langkah 35); (b) tiga aktivasi unit `SN-HHR-00201` menjadi reader `Zebra RFID Reader - 2` (langkah 73, 88, dan 108: Submit pertama TC-GS-HHR-436 yang tetap diteruskan ke server) dan kartu `Long Range` menjadi `6 of 6` pada momen aktivasi. Dua reader pertama dihapus oleh spec lewat `Delete` agar kuota `Long Range` pulih (NC-06: Delete reader Jalur A mengembalikan unit ke `Available` di Hardware Stock). Hook `after` melepas semua intercept, menghapus reader sisa, dan memulihkan Seed Reader A lewat fixture backend (DD-01 memakai data Pre-setup bersama karena TC menetapkannya; efek yang tersisa hanya `Alias Name` dan Last Updated DD-01 dan entri Changelog, dipulihkan oleh fixture).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.
- Akun aktor (login di hook `before`, bukan di langkah): Total Control Sari Dewi, Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (Client A): Seed Reader A (DD-01 sampai DD-10), plan Growth, `Long Range` terpakai 5 dari 6, General Settings `dd/MM/yy` 24-hour Asia/Jakarta. DD-01 (Device Name `Zebra RFID Reader - 1`, Serial Number `SN-HHR-00101`, Alias Name `—`, Reader Power `30 dBm`, Available) ditemukan lewat Search Serial Number karena Device Name-nya sama dengan DD-06. HS-01 `SN-HHR-00201` (SKU-HHR-01, Long Range, Zebra RFD40, Current Power 22 dBm, nomor urut 2) tersedia di stok Principal. Total reader N = 10 (dari seeding). Fixture baru `Fixture.hardwareHandheldReader.resilienceTulis026`.
- Data Dinamis: Alias Name `Reader Dock 01-{runId}-026` (TC-GS-HHR-121, 122, 96); tidak ada data bernama lain yang dibuat spec; nama baris hasil aktivasi `Zebra RFID Reader - 2` mengikuti nomor urut unit HS-01 (HHR-LOGIC-02g) dan dipakai apa adanya karena Expected TC menyebutnya.
- Baseline: jumlah entri Changelog dicatat sebelum aksi pemicu TC-GS-HHR-122 (langkah 25); jumlah entri Event Log dicatat sebelum aksi pemicu TC-GS-HHR-368 (langkah 80).
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 500, menunda respons hingga timeout dengan atau tanpa meneruskan request ke server, memicu 500 satu kali, dan membuang request tanpa meneruskannya ke server; simulator reader USB (sambung reader dengan Serial Number tertentu, dibaca oleh `[Sync]`; mekanisme tidak didefinisikan di TC, PRD, atau LLD sehingga disediakan tim FE); membaca toast beserta ketahanannya (toast error tidak hilang otomatis; `foundation/functions/toast-copy.md`) dan men-dismiss toast; membaca total reader pada daftar.

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
26. Pasang intercept pada request edit: ditunda hingga timeout, lalu request dibuang tanpa diteruskan ke server
27. Klik `⋯` pada baris DD-01, pilih `Edit Alias Name`
28. Isi `Alias Name` dengan `Reader Dock 01-{runId}-026`
29. Klik `[Save]`
30. Verifikasi toast error "Connection problem. Please try again." tampil tanpa tombol aksi
31. Verifikasi dialog Edit Alias Name tetap terbuka
32. Verifikasi `Alias Name` dialog tetap `Reader Dock 01-{runId}-026`
33. Dismiss toast error
34. Lepas intercept pada request edit
35. Klik `[Save]`
36. Verifikasi toast sukses "Success, Reader Dock 01-{runId}-026 has been updated."
37. Verifikasi dialog Edit Alias Name tertutup
38. Verifikasi kolom `Alias Name` baris DD-01 menampilkan `Reader Dock 01-{runId}-026`
39. Klik ikon Changelog
40. Verifikasi jumlah entri Changelog bertambah tepat satu dari baseline
41. Tutup Modal Changelog lewat `✕`
42. Klik `(←)` pada kotak Search

### TC-GS-HHR-96: Submit aktivasi gagal 5xx mempertahankan popup dan input

43. Pasang intercept pada request aktivasi: respons 500
44. Klik `[+ Activate Reader]`
45. Klik `Long Range` pada Overlay `Select Range Type`
46. Sambungkan reader USB dengan Serial Number `SN-HHR-00201` lewat simulator USB
47. Klik `[Sync]`
48. Isi `Alias Name` dengan `Reader Dock 01-{runId}-026`
49. Klik `[Submit]`
50. Verifikasi toast error "Error, failed to activate device." tampil
51. Verifikasi Popup Activate tetap terbuka
52. Verifikasi `Serial Number` tetap `SN-HHR-00201`
53. Verifikasi `Alias Name` tetap `Reader Dock 01-{runId}-026`
54. Verifikasi `[Submit]` enabled
55. Dismiss toast error
56. Lepas intercept pada request aktivasi
57. Klik `[✕]`
58. Verifikasi dialog `Cancel Activation` tampil dengan body "Are you sure you want to cancel this activation? The Sync progress you've made will be lost." dan tombol `[Go Back]` `[Cancel Activation]`
59. Klik `[Cancel Activation]`
60. Verifikasi total reader pada daftar tetap 10

### TC-GS-HHR-97: Timeout jaringan saat Submit mempertahankan nomor seri dan menampilkan toast koneksi

61. Pasang intercept pada request aktivasi: ditunda hingga timeout, lalu request dibuang tanpa diteruskan ke server
62. Klik `[+ Activate Reader]`
63. Klik `Long Range` pada Overlay `Select Range Type`
64. Sambungkan reader USB dengan Serial Number `SN-HHR-00201` lewat simulator USB
65. Klik `[Sync]`
66. Klik `[Submit]`
67. Verifikasi toast error "Connection problem. Please try again." tampil tanpa tombol aksi
68. Verifikasi `Serial Number` tetap `SN-HHR-00201`
69. Verifikasi tidak ada toast sukses maupun toast error aktivasi selain toast koneksi
70. Verifikasi Popup Activate tetap terbuka dengan input dipertahankan
71. Dismiss toast error
72. Lepas intercept pada request aktivasi
73. Klik `[Submit]`
74. Verifikasi toast sukses "Success, Zebra RFID Reader - 2 has been activated."
75. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
76. Verifikasi hanya satu baris `Zebra RFID Reader - 2` pada hasil Search
77. Klik `⋯` pada baris `Zebra RFID Reader - 2`, pilih `Delete`
78. Klik `[Delete]` pada dialog
79. Klik `(←)` pada kotak Search

### TC-GS-HHR-368: Submit gagal 5xx lalu berhasil menghasilkan satu baris Failed dan satu baris Activated

80. Klik ikon Event Log, catat jumlah entri Event Log sebagai baseline, lalu tutup Popup Event Log lewat `✕`
81. Pasang intercept pada request aktivasi: respons 500 satu kali, permintaan berikutnya diteruskan
82. Klik `[+ Activate Reader]`
83. Klik `Long Range` pada Overlay `Select Range Type`
84. Sambungkan reader USB `SN-HHR-00201` (HS-01) lewat simulator USB
85. Klik `[Sync]`
86. Klik `[Submit]`
87. Dismiss toast error
88. Klik `[Submit]`
89. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
90. Verifikasi baris `Zebra RFID Reader - 2` tampil
91. Klik `(←)` pada kotak Search
92. Klik ikon Event Log
93. Verifikasi jumlah entri Event Log bertambah tepat dua dari baseline
94. Verifikasi satu baris baru ber-Result `Failed` dengan Range Type `Long Range`
95. Verifikasi satu baris baru ber-Result `Activated` dengan Range Type `Long Range`
96. Verifikasi baris `Failed` tidak dihapus atau diganti oleh baris `Activated`
97. Verifikasi baris `Activated` tampil di atas baris `Failed` pada urutan Date descending
98. Tutup Popup Event Log lewat `✕`
99. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
100. Klik `⋯` pada baris `Zebra RFID Reader - 2`, pilih `Delete`
101. Klik `[Delete]` pada dialog
102. Klik `(←)` pada kotak Search

### TC-GS-HHR-436: Retry setelah timeout tidak menggandakan reader

103. Pasang intercept pada request aktivasi: respons ditunda hingga timeout namun request tetap diteruskan ke server
104. Klik `[+ Activate Reader]`
105. Klik `Long Range` pada Overlay `Select Range Type`
106. Sambungkan reader USB `SN-HHR-00201` (HS-01) lewat simulator USB
107. Klik `[Sync]`
108. Klik `[Submit]`
109. Verifikasi toast error "Connection problem. Please try again." tampil
110. Dismiss toast error
111. Lepas intercept pada request aktivasi
112. Klik `[Submit]` kembali
113. Verifikasi pesan inline `Serial number already exists` tampil di Popup Activate
114. Klik `[✕]`
115. Verifikasi dialog `Cancel Activation` tampil dengan body "Are you sure you want to cancel this activation? The Sync progress you've made will be lost." dan tombol `[Go Back]` `[Cancel Activation]`
116. Klik `[Cancel Activation]`
117. Muat ulang halaman Handheld Reader (`F5`)
118. Ketik Search `Zebra RFID Reader - 2`, tekan Enter
119. Verifikasi hanya satu baris `Zebra RFID Reader - 2` pada hasil Search
120. Verifikasi baris `Zebra RFID Reader - 2` tetap menampilkan `Status` `Available` dan `Reader Power` `22 dBm`
121. Verifikasi kartu `Long Range` menjadi `6 of 6`
122. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (intercept parsial). Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan blok: edit (TC-GS-HHR-121, 137, lalu 122) dulu, kemudian aktivasi (TC-GS-HHR-96, 97, 368, 436). TC-GS-HHR-137 ditaruh sebelum TC-GS-HHR-122 karena TC-GS-HHR-122 mengubah `Alias Name` DD-01 dan TC-GS-HHR-121 mengharapkan `—`. Di blok aktivasi, TC-GS-HHR-96 (tidak membuat data) dulu, lalu TC-GS-HHR-97, 368, dan 436 yang masing-masing membuat reader (pada TC-GS-HHR-436 reader dibuat oleh Submit pertama; Submit ulang ditolak). Dialog edit dibuka 3 kali dan ditutup 3 kali (2 lewat `✕` dan `[Leave]`, 1 lewat Save sukses); Popup Activate dibuka 4 kali dan ditutup 4 kali (dua lewat `[✕]`, dialog `Cancel Activation`, dan `[Cancel Activation]` pada TC-GS-HHR-96 dan 436; dua lewat Submit sukses).
- Langkah penghubung (aksi tanpa `Verifikasi`): pemasangan dan pelepasan intercept; dismiss toast error (agar toast error berikutnya yang sama tidak lulus karena toast lama, S-09); Search untuk menemukan baris target dan `(←)` untuk mengosongkan Search; baseline Changelog dan Event Log (langkah 25 dan 80); penyambungan reader di simulator USB; `✕` dan `[Leave]` untuk menutup dialog edit yang dirty (S-08; dialog `Unsaved Changes` tidak perlu dicatat lagi); dialog `Cancel Activation` pada TC-GS-HHR-96 dan 436 diverifikasi menurut S-08 (teks dari Expected TC-GS-HHR-89), dan `Delete` reader hasil TC-GS-HHR-97 dan 368 sesudah diasersi, untuk memulihkan kuota `Long Range` ke `5 of 6` sehingga `Long Range` tidak diblok gate kuota pada popup berikutnya (reader hasil TC-GS-HHR-436 dipulihkan oleh hook `after`). Karena Delete adalah pemulihan, bukan objek uji, tidak ada `Verifikasi` atasnya.
- Kelas harness: kelas b (fault injection 5xx dan timeout pada aksi tulis) dengan simulator reader USB (kelas d) sebagai pembentuk precondition TC-GS-HHR-96, 97, 368, dan 436 (`[Sync]` harus menghasilkan data agar `[Submit]` aktif); objek uji tetap perilaku FE atas kegagalan server, bukan pembacaan reader. Tidak ada pengecualian `P-1` sampai `P-7` yang mencakup kombinasi ini, sehingga spec tidak menyebut id pengecualian; alasan spec tetap satu dan tidak dipecah ada pada butir ukuran di bawah. Intercept yang dipakai sebagai pemicu dilepas segera setelah selesai.
- Spec melewati sekitar 35 langkah (122 langkah nominal, 41 di antaranya `Verifikasi` yang dipecah per klausa Expected, S-01). Alasan: seluruh blok satu topik (resilience aksi tulis) dan satu akun aktor; empat blok aktivasi memakai simulator USB hanya sebagai precondition. Blok edit (TC-GS-HHR-121, 137, 122) dan blok aktivasi (TC-GS-HHR-96, 97, 368, 436) berdiri sendiri: tiap TC membuka dialog atau popup sendiri dan memulihkan state di akhirnya (tutup dialog, hapus reader), sehingga kegagalan keras satu blok tidak menghilangkan makna blok lain. Spec edit-saja dan spec aktivasi-saja sah dipecah bila diinginkan, tetapi konvensi menetapkan satu spec per kelas per modul (bagian 3, prinsip 13 "Cara menggabung antar-aksi").
- Pembagian TC lintas spec: TC-GS-HHR-147, 155, 160, 225, 226, dan 352 (kegagalan 5xx status, Delete, Cancel Request, bulk, dan log) ada di spec 027; TC-GS-HHR-184, 315, dan 339 (kegagalan unduh) ada di spec 028. Asersi absence log pada TC-GS-HHR-352 ada di spec 027.
- Alias Name `Reader Dock 01` pada TC-GS-HHR-121, 122, dan 96 ditulis bersuffix per run (`Reader Dock 01-{runId}-026`) mengikuti S-12.
- Temuan untuk QA:
  - TC-GS-HHR-96, 97, 368, dan 436 berlabel `Manual Only` (b) di TC sumber (reader USB fisik) dan TC-GS-HHR-121, 122, 137 `Automatable`; semuanya tetap ditulis (konvensi bagian 2). Mekanisme simulasi reader USB tidak didefinisikan di TC, PRD, atau LLD; spec tidak mengarang endpoint dan menyatakannya "disediakan tim FE".
  - TC-GS-HHR-121, 122, dan 137 menyebut target `baris DD-01`, sedangkan Device Name DD-01 dan DD-06 sama (`Zebra RFID Reader - 1`); spec menemukan DD-01 lewat Search Serial Number `SN-HHR-00101`. TC-GS-HHR-122 mengubah `Alias Name` DD-01 (data Pre-setup bersama), dipulihkan oleh fixture backend (S-06 terpaksa karena TC menetapkan DD-01).
  - TC-GS-HHR-121 dan 137 tidak menyebut cara menutup dialog sesudah kegagalan; spec memakai `✕` dan `[Leave]` (dialog `Unsaved Changes`) sesuai S-08.
  - TC-GS-HHR-368 langkah 2 menulis `[Submit]` (gagal) lalu `[Submit]` lagi tanpa menyebut dismiss toast error; spec men-dismiss toast error di antaranya sebagai langkah penghubung.
  - Pemulihan antar-TC (`Delete` reader hasil aktivasi) bergantung pada asumsi bahwa Delete reader Jalur A mengembalikan unit ke `Available` (NC-06) dan nama bawaan aktivasi ulang tetap `Zebra RFID Reader - 2` (nomor urut unit HS-01). TC tidak menyatakan ini.
  - TC-GS-HHR-122 menyebut entri Changelog `Alias Name` untuk DD-01 bertambah satu; spec mengasersi selisih jumlah entri Changelog terhadap baseline (S-12) dan tidak memfilter per reader.
  - Spec ini mencampur dua kelas harness (b: fault injection; d: simulator USB sebagai precondition pada TC-GS-HHR-96, 97, 368, 436) tanpa pengecualian `P-` yang berlaku; spec tidak dipecah (D2). QA/pemilik suite diminta memutuskan apakah blok aktivasi dipisah ke spec sendiri.
  - TC-GS-HHR-436 Expected a menyebut pengiriman ulang "tidak mengubah reader yang sudah ada" tanpa nilai pembanding; spec mengasersinya lewat `Status` `Available` dan `Reader Power` `22 dBm` (nilai hasil aktivasi Jalur A HS-01 menurut TC-GS-HHR-64) setelah muat ulang.
  - TC-GS-HHR-121 dan 137 menutup dialog edit dengan `✕` dan `[Leave]` (dialog `Unsaved Changes`), tetapi TC tidak memuat teks dialog; spec tidak memverifikasi isi dialog itu.
