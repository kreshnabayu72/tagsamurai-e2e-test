---
id: TC-GS-HHR-E2E-021-activate-collision-duplikat-dan-ketidaksesuaian-range-type
title: "Activate Reader: Collision Lintas Tenant, Serial Duplikat, Ketidaksesuaian Range Type, dan Jalur Berubah antara Sync dan Submit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-HHR-77
  - TC-GS-HHR-78
  - TC-GS-HHR-79
  - TC-GS-HHR-80
  - TC-GS-HHR-477
  - TC-GS-HHR-478
coverage:
  web: automated
---

# Activate Reader: Collision Lintas Tenant, Serial Duplikat, Ketidaksesuaian Range Type, dan Jalur Berubah antara Sync dan Submit

## Prerequisites

- Mode: FE+BE. Backend nyata dengan fixture backend; permintaan Waiting for Approval dan unit stok yang dibuat spec dipulihkan oleh spec sendiri dan hook `after`.
- Suite serial (`parallel: false`). State global yang diubah spec ini: (a) dua permintaan aktivasi Waiting for Approval di Client A (langkah 37 dan 53) yang langsung dibatalkan lewat `Cancel Request`, dan (b) unit `SN-HHR-00302` yang didaftarkan lalu dihapus Principal di Hardware Stock Admin Console (langkah 72 dan 95). Hook `after` memulihkan seluruhnya (batalkan permintaan yang tersisa, hapus unit `SN-HHR-00302` dari stok, pulihkan Seed Reader A lewat fixture backend).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.
- Akun aktor (login di hook `before`, bukan di langkah): Total Control Sari Dewi, Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Pelaku kedua: Principal Bambang Hartono, `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`, hanya lewat sesi API untuk mendaftarkan dan menghapus unit `SN-HHR-00302` di Admin Console > Hardware Stock (langkah 72, 85, 95, 108). Sesi UI kedua tidak dipakai karena hasil di sesi itu tidak diasersi. Mekanisme API ini disediakan tim FE (tidak ada endpoint di TC, PRD, atau LLD yang dirujuk spec).
- Data Pre-setup (Client A): Seed Reader A (DD-01 sampai DD-10, Tabel Data Uji Dinamis TC), plan Growth, toggle `Allow Self-Purchased Device Activation` aktif, alokasi `Short Range` 8 (terpakai 5) dan `Long Range` 6 (terpakai 5), General Settings `dd/MM/yy` 24-hour Asia/Jakarta. Total reader awal N = 10 (dari seeding, bukan dibaca dari satu halaman tabel). Katalog Device Name DN-01 sampai DN-07 (Admin Console, dibaca read-only oleh Client A); `Chainway C72` (DN-01) sudah dipakai DD-05 dengan `N` terpakai 1.
- Data Pre-setup (stok dan tenant lain): HS-03 `SN-HHR-00203` (SKU-HHR-02, Long Range) dan HS-04 `SN-HHR-00204` (SKU-HHR-01, Long Range, aktif di Client C, nomor urut 4); `SN-HHR-00301` aktif sebagai Self-Purchased di Client C; `SN-HHR-00302` tidak ada di stok Principal pada awal spec. Client C tidak diubah. Fixture baru `Fixture.hardwareHandheldReader.activateCollision021`.
- Data Dinamis: Alias Name `Reader Dock 01-{runId}-021` (TC-GS-HHR-478, hanya diisi dan tidak disimpan); nama baris hasil aktivasi (`Zebra RFID Reader - 4`, `Chainway C72 - 2`) ditentukan penomoran PRD HHR-LOGIC-02g dan dipakai apa adanya karena Expected TC menyebutnya.
- Baseline: jumlah entri Event Log dicatat sebelum aksi pemicu yang diasersi (langkah 15 dan 63); kartu `Long Range` awal `5 of 6`.
- Kemampuan teknis: simulator reader USB (sambung dan cabut reader dengan Serial Number tertentu, dibaca oleh `[Sync]`; mekanisme tidak didefinisikan di TC, PRD, atau LLD sehingga disediakan tim FE); sesi API Principal untuk mendaftarkan dan menghapus unit stok; pemulihan fixture backend Seed Reader A; membaca total reader pada daftar.

## Test Steps

### TC-GS-HHR-79: Serial yang sudah terdaftar pada Range Type yang sama di tenant yang sama ditolak

1. Klik `[+ Activate Reader]`
2. Klik `Long Range` pada Overlay `Select Range Type`
3. Sambungkan reader USB dengan Serial Number `SN-HHR-00101` (DD-01, sudah aktif di Client A, Long Range) lewat simulator USB
4. Klik `[Sync]`
5. Klik `[Submit]`
6. Verifikasi pesan inline `Serial number already exists` tampil di Popup Activate
7. Verifikasi Popup Activate tetap terbuka
8. Verifikasi input dipertahankan: `Serial Number` tetap `SN-HHR-00101`
9. Klik `[✕]`
10. Verifikasi dialog `Cancel Activation` tampil dengan body "Are you sure you want to cancel this activation? The Sync progress you've made will be lost." dan tombol `[Go Back]` `[Cancel Activation]`
11. Klik `[Cancel Activation]`
12. Verifikasi total reader pada daftar tetap 10
13. Verifikasi kartu `Long Range` tetap `5 of 6`

### TC-GS-HHR-80: Range Type terpilih berbeda dari jenis SKU resmi unit ditolak

14. Klik ikon Event Log
15. Catat jumlah entri Event Log sebagai baseline
16. Tutup Popup Event Log lewat `✕`
17. Klik `[+ Activate Reader]`
18. Klik `Short Range` pada Overlay `Select Range Type`
19. Sambungkan reader USB dengan Serial Number `SN-HHR-00203` (HS-03, unit resmi berjenis Long Range) lewat simulator USB
20. Klik `[Sync]`
21. Klik `[Submit]`
22. Verifikasi pesan inline `Selected range type does not match this device.` tampil di Popup Activate
23. Verifikasi Popup Activate tetap terbuka
24. Verifikasi input dipertahankan: `Serial Number` tetap `SN-HHR-00203`
25. Klik `[✕]`
26. Verifikasi dialog `Cancel Activation` tampil dengan body "Are you sure you want to cancel this activation? The Sync progress you've made will be lost." dan tombol `[Go Back]` `[Cancel Activation]`
27. Klik `[Cancel Activation]`
28. Verifikasi total reader pada daftar tetap 10
29. Klik ikon Event Log
30. Verifikasi jumlah entri Event Log bertambah tepat satu dari baseline
31. Verifikasi satu baris baru ber-Result `Failed` dengan Range Type `Short Range`, Device Name `Zebra Mobile Reader (SKU-HHR-02)`, dan PIC `Sari D`
32. Tutup Popup Event Log lewat `✕`

### TC-GS-HHR-77: Serial Jalur A yang sudah aktif di tenant lain masuk Waiting for Approval

33. Klik `[+ Activate Reader]`
34. Klik `Long Range` pada Overlay `Select Range Type`
35. Sambungkan reader USB dengan Serial Number `SN-HHR-00204` (HS-04, unit stok Principal yang aktif di Client C) lewat simulator USB
36. Klik `[Sync]`
37. Klik `[Submit]`
38. Verifikasi toast sukses "Success, Zebra RFID Reader - 4 has been submitted for approval."
39. Ketik Search `Zebra RFID Reader - 4`, tekan Enter
40. Verifikasi baris baru `Zebra RFID Reader - 4` dengan `Status` `Waiting for Approval` (badge `severity="warning"`)
41. Verifikasi kartu `Long Range` menjadi `6 of 6` dengan `0 remaining`
42. Klik `⋯` pada baris `Zebra RFID Reader - 4`, pilih `Cancel Request`
43. Klik `[Cancel Request]` pada dialog
44. Tunggu aksi selesai
45. Klik `(←)` pada kotak Search

### TC-GS-HHR-78: Serial Jalur B yang sudah dipakai tenant lain masuk Waiting for Approval

46. Klik `[+ Activate Reader]`
47. Klik `Long Range` pada Overlay `Select Range Type`
48. Sambungkan reader USB dengan Serial Number `SN-HHR-00301` (aktif sebagai Self-Purchased di Client C, tidak ada di stok Principal) lewat simulator USB
49. Klik `[Sync]`
50. Pilih `Chainway C72` pada `Device Name`
51. Isi `Brand` dengan `Chainway`
52. Isi `Model/Type` dengan `C72`
53. Klik `[Submit]`
54. Verifikasi toast sukses "Success, Chainway C72 - 2 has been submitted for approval."
55. Ketik Search `Chainway C72 - 2`, tekan Enter
56. Verifikasi baris baru `Chainway C72 - 2` dengan `Status` `Waiting for Approval`
57. Verifikasi baris `Chainway C72 - 2` ber-`Source` `Self-Purchased`
58. Klik `⋯` pada baris `Chainway C72 - 2`, pilih `Cancel Request`
59. Klik `[Cancel Request]` pada dialog
60. Tunggu aksi selesai
61. Klik `(←)` pada kotak Search

### TC-GS-HHR-477: Jalur aktivasi berubah antara Sync dan Submit ditolak 409 dengan dialog Device Changed

62. Klik ikon Event Log
63. Catat jumlah entri Event Log sebagai baseline
64. Tutup Popup Event Log lewat `✕`
65. Klik `[+ Activate Reader]`
66. Klik `Long Range` pada Overlay `Select Range Type`
67. Sambungkan reader USB dengan Serial Number `SN-HHR-00302` (tidak ada di stok Principal) lewat simulator USB
68. Klik `[Sync]`
69. Pilih `Chainway C72` pada `Device Name`
70. Isi `Brand` dengan `Chainway`
71. Isi `Model/Type` dengan `C72`
72. Principal (sesi API) mendaftarkan `SN-HHR-00302` sebagai unit Long Range di Admin Console > Hardware Stock hingga tersimpan
73. Tunggu aksi selesai
74. Klik `[Submit]`
75. Verifikasi dialog `Device Changed` tampil dengan body "This device was changed by someone else. Please review." dan tombol `[OK]`
76. Klik `[OK]` pada dialog
77. Verifikasi Popup Activate kembali ke state Menunggu Sync: `Serial Number`, label jalur, `Device Name`, `SKU`, `Brand`, `Model/Type`, slider `Reader Power`, dan `Alias Name` tidak tampil
78. Verifikasi `[Submit]` disabled
79. Klik `[✕]`
80. Verifikasi total reader pada daftar tetap 10
81. Verifikasi kartu `Long Range` tetap `5 of 6`
82. Klik ikon Event Log
83. Verifikasi jumlah entri Event Log sama dengan baseline
84. Tutup Popup Event Log lewat `✕`
85. Principal (sesi API) menghapus `SN-HHR-00302` dari Admin Console > Hardware Stock hingga tersimpan, agar serial kembali di luar stok untuk TC berikutnya
86. Tunggu aksi selesai

### TC-GS-HHR-478: Sync ulang serial sama dengan jalur berubah mereset seluruh input

87. Klik `[+ Activate Reader]`
88. Klik `Long Range` pada Overlay `Select Range Type`
89. Sambungkan reader USB dengan Serial Number `SN-HHR-00302` (tidak ada di stok Principal) lewat simulator USB
90. Klik `[Sync]`
91. Pilih `Chainway C72` pada `Device Name`
92. Isi `Brand` dengan `Chainway`
93. Isi `Model/Type` dengan `C72`
94. Isi `Alias Name` dengan `Reader Dock 01-{runId}-021`
95. Principal (sesi API) mendaftarkan `SN-HHR-00302` sebagai unit Long Range di Admin Console > Hardware Stock hingga tersimpan
96. Tunggu aksi selesai
97. Klik `[Sync]` lagi pada reader yang sama
98. Verifikasi label `Official` tampil
99. Verifikasi `Brand` terisi dari stok dan terkunci
100. Verifikasi `Model/Type` terisi dari stok dan terkunci
101. Verifikasi `Device Name` dan `SKU` Jalur B tidak tampil
102. Verifikasi `Alias Name` kosong
103. Verifikasi slider `Reader Power` terisi Current Power unit `SN-HHR-00302` di stok
104. Verifikasi `Serial Number` tetap `SN-HHR-00302`
105. Klik `[✕]`
106. Verifikasi dialog `Cancel Activation` tampil dengan body "Are you sure you want to cancel this activation? The Sync progress you've made will be lost." dan tombol `[Go Back]` `[Cancel Activation]`
107. Klik `[Cancel Activation]`
108. Principal (sesi API) menghapus `SN-HHR-00302` dari Admin Console > Hardware Stock hingga tersimpan
109. Tunggu aksi selesai

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan blok: TC-GS-HHR-79 dan 80 dulu (penolakan yang tidak membuat data), lalu TC-GS-HHR-77 dan 78 (aksi yang membuat permintaan Waiting for Approval), lalu TC-GS-HHR-477 dan 478 (butuh sesi API Principal). Urutan ini menyimpang dari urutan nomor TC karena validasi yang diblokir ditaruh sebelum aksi yang menghasilkan data (konvensi bagian 3). Popup Activate dibuka satu kali per TC (enam kali) dan setiap kali ditutup lewat `[✕]` dan `[Cancel Activation]`, `[✕]` atau submit.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 15 dan 63 (baseline Event Log, termasuk membuka dan menutup popup Event Log); pembatalan permintaan di akhir TC-GS-HHR-77 dan 78 (`Cancel Request`, beserta "Tunggu aksi selesai" pada langkah 44 dan 60 karena langkah berikutnya bergantung pada kuota itu, bagian 8b butir 8) yang mengembalikan kuota `Long Range` ke `5 of 6` agar popup berikutnya tidak diblok gate kuota; pendaftaran dan penghapusan unit stok oleh Principal (langkah 72, 85, 95, 108) beserta "Tunggu aksi selesai"; menutup popup yang sudah berisi hasil Sync lewat `[✕]`, dialog `Cancel Activation`, dan `[Cancel Activation]` (langkah 9 sampai 11, 25 sampai 27, 105 sampai 107; S-08, teks dialog dari Expected TC-GS-HHR-89). Popup pada langkah 79 (sudah kembali ke state Menunggu Sync) ditutup langsung lewat `[✕]` tanpa dialog.
- Search pada TC-GS-HHR-77 dan 78 ditulis untuk menemukan baris target (langkah penghubung); asersi kartu kuota dilakukan saat Search aktif. Search dikosongkan lewat `(←)` sebelum blok berikutnya (S-09).
- P-1 (state berat): `Verifikasi` jumlah entri Event Log sama dengan baseline (TC-GS-HHR-477 Expected d, langkah 83) tetap di spec ini karena state yang dibutuhkan dibangun langkah sebelumnya dalam spec yang sama (Sync USB, pengisian field Jalur B, dan perubahan jalur oleh Principal pada langkah 72); memakai baseline langkah 63 (S-12). TC-GS-HHR-477 hanya ada di spec ini.
- Spec melewati sekitar 35 langkah (109 langkah). Seluruhnya satu kelas harness (kelas d: simulator USB) dan satu akun aktor; Principal hanya pemicu sesi API. Tiap blok TC membuka Popup Activate sendiri dan memulihkan state di akhir (batalkan permintaan, hapus unit stok), sehingga kegagalan satu blok tidak menghilangkan makna blok lain. Penggabungan dilakukan karena enam TC berbagi topik (penolakan dan collision pada aksi Submit Activate), dataset, dan harness yang sama (konvensi bagian 3, prinsip 1 dan 13).
- Pembagian TC lintas spec: TC-GS-HHR-81 (kuota habis antara pemilihan Range Type dan Submit) ada di spec 075.
- Temuan untuk QA:
  - Seluruh TC spec ini berlabel `Manual Only` di TC sumber (reader USB fisik, dan dua sesi untuk TC-GS-HHR-477 dan 478) tetapi tetap ditulis (konvensi bagian 2). Mekanisme simulasi reader USB tidak didefinisikan di TC, PRD, atau LLD; spec tidak mengarang endpoint dan menyatakannya "disediakan tim FE".
  - TC-GS-HHR-79, 80, dan 477 mengharapkan "tidak ada baris baru" tanpa menyebut cara membacanya; spec memakai total reader dari seeding (N = 10) pada daftar. Cara membaca total (mis. footer pagination) tidak diuraikan di TC.
  - TC-GS-HHR-79 tidak menyebut apakah penolakan V-04 menambah baris Event Log; spec tidak mengasersi Event Log pada TC itu dan mengambil baseline TC-GS-HHR-80 sesudahnya.
  - TC-GS-HHR-477 dan 478 menyebut Principal "mendaftarkan SN-HHR-00302 sebagai unit Long Range" tanpa SKU, Brand, Model/Type, dan Current Power unit. Expected TC-GS-HHR-478 b menulis "Brand dan Model/Type terisi dari stok" dan "slider Reader Power terisi Current Power unit di stok" tanpa nilai konkret; asersi spec merujuk nilai dari seeding sesi API yang disediakan tim FE.
  - TC-GS-HHR-477 dan 478 sama-sama mensyaratkan `SN-HHR-00302` di luar stok pada awalnya; spec menghapus unit itu dari stok sesudah masing-masing TC. TC tidak menyatakan cara pemulihannya.
  - TC-GS-HHR-77 dan 78 menaikkan kartu `Long Range` ke `6 of 6`; TC berikutnya mengandalkan fixture backend yang dipulihkan antar TC (Catatan TC). Dalam satu spec, pemulihan dilakukan lewat `Cancel Request` (langkah penghubung), yang tidak diasersi.
  - TC-GS-HHR-478 tidak menyebut apakah sesi pertama harus mengulang `[Sync]` dengan reader yang sama atau setelah mencabut dan menyambung ulang; spec mengikuti Langkah TC (klik `[Sync]` lagi pada reader yang sama).
