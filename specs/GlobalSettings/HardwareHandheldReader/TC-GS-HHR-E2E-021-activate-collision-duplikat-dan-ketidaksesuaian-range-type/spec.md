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
- Suite serial (`parallel: false`). State global yang diubah spec ini: (a) dua permintaan aktivasi Waiting for Approval di Client A (langkah 33 dan 48) yang langsung dibatalkan lewat `Cancel Request`, dan (b) unit `SN-HHR-00302` yang didaftarkan lalu dihapus Principal di Hardware Stock Admin Console (langkah 66 dan 89). Hook `after` memulihkan seluruhnya (batalkan permintaan yang tersisa, hapus unit `SN-HHR-00302` dari stok, pulihkan Seed Reader A lewat fixture backend).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.
- Akun aktor (login di hook `before`, bukan di langkah): Total Control Sari Dewi, Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Pelaku kedua: Principal Bambang Hartono, `principal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`, hanya lewat sesi API untuk mendaftarkan dan menghapus unit `SN-HHR-00302` di Admin Console > Hardware Stock (langkah 66, 79, 89, 100). Sesi UI kedua tidak dipakai karena hasil di sesi itu tidak diasersi. Mekanisme API ini disediakan tim FE (tidak ada endpoint di TC, PRD, atau LLD yang dirujuk spec).
- Data Pre-setup (Client A): Seed Reader A (DD-01 sampai DD-10, Tabel Data Uji Dinamis TC), plan Growth, toggle `Allow Self-Purchased Device Activation` aktif, alokasi `Short Range` 8 (terpakai 5) dan `Long Range` 6 (terpakai 5), General Settings `dd/MM/yy` 24-hour Asia/Jakarta. Total reader awal N = 10 (dari seeding, bukan dibaca dari satu halaman tabel). Katalog Device Name DN-01 sampai DN-07 (Admin Console, dibaca read-only oleh Client A); `Chainway C72` (DN-01) sudah dipakai DD-05 dengan `N` terpakai 1.
- Data Pre-setup (stok dan tenant lain): HS-03 `SN-HHR-00203` (SKU-HHR-02, Long Range) dan HS-04 `SN-HHR-00204` (SKU-HHR-01, Long Range, aktif di Client C, nomor urut 4); `SN-HHR-00301` aktif sebagai Self-Purchased di Client C; `SN-HHR-00302` tidak ada di stok Principal pada awal spec. Client C tidak diubah. Fixture baru `Fixture.hardwareHandheldReader.activateCollision021`.
- Data Dinamis: tidak ada data bernama yang dibuat spec; nama baris hasil aktivasi (`Zebra RFID Reader - 4`, `Chainway C72 - 2`) ditentukan penomoran PRD HHR-LOGIC-02g dan dipakai apa adanya karena Expected TC menyebutnya.
- Baseline: jumlah entri Event Log dicatat sebelum aksi pemicu yang diasersi (langkah 13 dan 57); kartu `Long Range` awal `5 of 6`.
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
9. Klik `[✕]`, lalu klik `[Cancel Activation]`
10. Verifikasi total reader pada daftar tetap 10
11. Verifikasi kartu `Long Range` tetap `5 of 6`

### TC-GS-HHR-80: Range Type terpilih berbeda dari jenis SKU resmi unit ditolak

12. Klik ikon Event Log
13. Catat jumlah entri Event Log sebagai baseline
14. Tutup Popup Event Log lewat `✕`
15. Klik `[+ Activate Reader]`
16. Klik `Short Range` pada Overlay `Select Range Type`
17. Sambungkan reader USB dengan Serial Number `SN-HHR-00203` (HS-03, unit resmi berjenis Long Range) lewat simulator USB
18. Klik `[Sync]`
19. Klik `[Submit]`
20. Verifikasi pesan inline `Selected range type does not match this device.` tampil di Popup Activate
21. Verifikasi Popup Activate tetap terbuka
22. Verifikasi input dipertahankan: `Serial Number` tetap `SN-HHR-00203`
23. Klik `[✕]`, lalu klik `[Cancel Activation]`
24. Verifikasi total reader pada daftar tetap 10
25. Klik ikon Event Log
26. Verifikasi jumlah entri Event Log bertambah tepat satu dari baseline
27. Verifikasi satu baris baru ber-Result `Failed` dengan Range Type `Short Range`, Device Name `Zebra Mobile Reader (SKU-HHR-02)`, dan PIC `Sari D`
28. Tutup Popup Event Log lewat `✕`

### TC-GS-HHR-77: Serial Jalur A yang sudah aktif di tenant lain masuk Waiting for Approval

29. Klik `[+ Activate Reader]`
30. Klik `Long Range` pada Overlay `Select Range Type`
31. Sambungkan reader USB dengan Serial Number `SN-HHR-00204` (HS-04, unit stok Principal yang aktif di Client C) lewat simulator USB
32. Klik `[Sync]`
33. Klik `[Submit]`
34. Verifikasi toast sukses "Success, Zebra RFID Reader - 4 has been submitted for approval."
35. Ketik Search `Zebra RFID Reader - 4`, tekan Enter
36. Verifikasi baris baru `Zebra RFID Reader - 4` dengan `Status` `Waiting for Approval` (badge `severity="warning"`)
37. Verifikasi kartu `Long Range` menjadi `6 of 6` dengan `0 remaining`
38. Klik `⋯` pada baris `Zebra RFID Reader - 4`, pilih `Cancel Request`
39. Klik `[Cancel Request]` pada dialog
40. Klik `(←)` pada kotak Search

### TC-GS-HHR-78: Serial Jalur B yang sudah dipakai tenant lain masuk Waiting for Approval

41. Klik `[+ Activate Reader]`
42. Klik `Long Range` pada Overlay `Select Range Type`
43. Sambungkan reader USB dengan Serial Number `SN-HHR-00301` (aktif sebagai Self-Purchased di Client C, tidak ada di stok Principal) lewat simulator USB
44. Klik `[Sync]`
45. Pilih `Chainway C72` pada `Device Name`
46. Isi `Brand` dengan `Chainway`
47. Isi `Model/Type` dengan `C72`
48. Klik `[Submit]`
49. Verifikasi toast sukses "Success, Chainway C72 - 2 has been submitted for approval."
50. Ketik Search `Chainway C72 - 2`, tekan Enter
51. Verifikasi baris baru `Chainway C72 - 2` dengan `Status` `Waiting for Approval`
52. Verifikasi baris `Chainway C72 - 2` ber-`Source` `Self-Purchased`
53. Klik `⋯` pada baris `Chainway C72 - 2`, pilih `Cancel Request`
54. Klik `[Cancel Request]` pada dialog
55. Klik `(←)` pada kotak Search

### TC-GS-HHR-477: Jalur aktivasi berubah antara Sync dan Submit ditolak 409 dengan dialog Device Changed

56. Klik ikon Event Log
57. Catat jumlah entri Event Log sebagai baseline
58. Tutup Popup Event Log lewat `✕`
59. Klik `[+ Activate Reader]`
60. Klik `Long Range` pada Overlay `Select Range Type`
61. Sambungkan reader USB dengan Serial Number `SN-HHR-00302` (tidak ada di stok Principal) lewat simulator USB
62. Klik `[Sync]`
63. Pilih `Chainway C72` pada `Device Name`
64. Isi `Brand` dengan `Chainway`
65. Isi `Model/Type` dengan `C72`
66. Principal (sesi API) mendaftarkan `SN-HHR-00302` sebagai unit Long Range di Admin Console > Hardware Stock hingga tersimpan
67. Tunggu aksi selesai
68. Klik `[Submit]`
69. Verifikasi dialog `Device Changed` tampil dengan body "This device was changed by someone else. Please review." dan tombol `[OK]`
70. Klik `[OK]` pada dialog
71. Verifikasi Popup Activate kembali ke state Menunggu Sync: `Serial Number`, label jalur, `Device Name`, `SKU`, `Brand`, `Model/Type`, slider `Reader Power`, dan `Alias Name` tidak tampil
72. Verifikasi `[Submit]` disabled
73. Klik `[✕]`
74. Verifikasi total reader pada daftar tetap 10
75. Verifikasi kartu `Long Range` tetap `5 of 6`
76. Klik ikon Event Log
77. Verifikasi jumlah entri Event Log sama dengan baseline
78. Tutup Popup Event Log lewat `✕`
79. Principal (sesi API) menghapus `SN-HHR-00302` dari Admin Console > Hardware Stock hingga tersimpan, agar serial kembali di luar stok untuk TC berikutnya
80. Tunggu aksi selesai

### TC-GS-HHR-478: Sync ulang serial sama dengan jalur berubah mereset seluruh input

81. Klik `[+ Activate Reader]`
82. Klik `Long Range` pada Overlay `Select Range Type`
83. Sambungkan reader USB dengan Serial Number `SN-HHR-00302` (tidak ada di stok Principal) lewat simulator USB
84. Klik `[Sync]`
85. Pilih `Chainway C72` pada `Device Name`
86. Isi `Brand` dengan `Chainway`
87. Isi `Model/Type` dengan `C72`
88. Isi `Alias Name` dengan `Reader Dock 01`
89. Principal (sesi API) mendaftarkan `SN-HHR-00302` sebagai unit Long Range di Admin Console > Hardware Stock hingga tersimpan
90. Tunggu aksi selesai
91. Klik `[Sync]` lagi pada reader yang sama
92. Verifikasi label `Official` tampil
93. Verifikasi `Brand` terisi dari stok dan terkunci
94. Verifikasi `Model/Type` terisi dari stok dan terkunci
95. Verifikasi `Device Name` dan `SKU` Jalur B tidak tampil
96. Verifikasi `Alias Name` kosong
97. Verifikasi slider `Reader Power` terisi Current Power unit `SN-HHR-00302` di stok
98. Verifikasi `Serial Number` tetap `SN-HHR-00302`
99. Klik `[✕]`, lalu klik `[Cancel Activation]`
100. Principal (sesi API) menghapus `SN-HHR-00302` dari Admin Console > Hardware Stock hingga tersimpan
101. Tunggu aksi selesai

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan blok: TC-GS-HHR-79 dan 80 dulu (penolakan yang tidak membuat data), lalu TC-GS-HHR-77 dan 78 (aksi yang membuat permintaan Waiting for Approval), lalu TC-GS-HHR-477 dan 478 (butuh sesi API Principal). Urutan ini menyimpang dari urutan nomor TC karena validasi yang diblokir ditaruh sebelum aksi yang menghasilkan data (konvensi bagian 3). Popup Activate dibuka satu kali per TC (enam kali) dan setiap kali ditutup lewat `[✕]` dan `[Cancel Activation]`, `[✕]` atau submit.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 13 dan 57 (baseline Event Log, termasuk membuka dan menutup popup Event Log); pembatalan permintaan di akhir TC-GS-HHR-77 dan 78 (`Cancel Request`) yang mengembalikan kuota `Long Range` ke `5 of 6` agar popup berikutnya tidak diblok gate kuota; pendaftaran dan penghapusan unit stok oleh Principal (langkah 66, 79, 89, 100) beserta "Tunggu aksi selesai"; menutup popup lewat `[✕]` dan `[Cancel Activation]`.
- Search pada TC-GS-HHR-77 dan 78 ditulis untuk menemukan baris target (langkah penghubung); asersi kartu kuota dilakukan saat Search aktif. Search dikosongkan lewat `(←)` sebelum blok berikutnya (S-09).
- Pengecualian P-2: Principal (pelaku kedua) hanya memicu perubahan state stok lewat sesi API pada TC-GS-HHR-477 dan 478 dan tidak ada hasil di sesi itu yang diasersi.
- Spec melewati sekitar 35 langkah (101 langkah). Seluruhnya satu kelas harness (kelas d: simulator USB) dan satu akun aktor; Principal hanya pemicu sesi API. Tiap blok TC membuka Popup Activate sendiri dan memulihkan state di akhir (batalkan permintaan, hapus unit stok), sehingga kegagalan satu blok tidak menghilangkan makna blok lain. Penggabungan dilakukan karena enam TC berbagi topik (penolakan dan collision pada aksi Submit Activate), dataset, dan harness yang sama (konvensi bagian 3, prinsip 1 dan 13).
- Pembagian TC lintas spec: TC-GS-HHR-81 (kuota habis antara pemilihan Range Type dan Submit) ada di spec 075.
- Temuan untuk QA:
  - Seluruh TC spec ini berlabel `Manual Only` di TC sumber (reader USB fisik, dan dua sesi untuk TC-GS-HHR-477 dan 478) tetapi tetap ditulis (konvensi bagian 2). Mekanisme simulasi reader USB tidak didefinisikan di TC, PRD, atau LLD; spec tidak mengarang endpoint dan menyatakannya "disediakan tim FE".
  - TC-GS-HHR-79, 80, dan 477 mengharapkan "tidak ada baris baru" tanpa menyebut cara membacanya; spec memakai total reader dari seeding (N = 10) pada daftar. Cara membaca total (mis. footer pagination) tidak diuraikan di TC.
  - TC-GS-HHR-79 tidak menyebut apakah penolakan V-04 menambah baris Event Log; spec tidak mengasersi Event Log pada TC itu dan mengambil baseline TC-GS-HHR-80 sesudahnya.
  - TC-GS-HHR-477 dan 478 menyebut Principal "mendaftarkan SN-HHR-00302 sebagai unit Long Range" tanpa SKU, Brand, Model/Type, dan Current Power unit. Expected TC-GS-HHR-478 b menulis "Brand dan Model/Type terisi dari stok" dan "slider Reader Power terisi Current Power unit di stok" tanpa nilai konkret; asersi spec merujuk nilai dari seeding sesi API yang disediakan tim FE.
  - TC-GS-HHR-477 dan 478 sama-sama mensyaratkan `SN-HHR-00302` di luar stok pada awalnya; spec menghapus unit itu dari stok sesudah masing-masing TC. TC tidak menyatakan cara pemulihannya.
  - TC-GS-HHR-77 dan 78 menaikkan kartu `Long Range` ke `6 of 6`; TC berikutnya mengandalkan fixture backend yang dipulihkan antar TC (Catatan TC). Dalam satu spec, pemulihan dilakukan lewat `Cancel Request` (langkah penghubung), yang tidak diasersi.
  - TC-GS-HHR-478 tidak menyebut apakah sesi pertama harus mengulang `[Sync]` dengan reader yang sama atau setelah mencabut dan menyambung ulang; spec mengikuti Langkah TC (klik `[Sync]` lagi pada reader yang sama).
