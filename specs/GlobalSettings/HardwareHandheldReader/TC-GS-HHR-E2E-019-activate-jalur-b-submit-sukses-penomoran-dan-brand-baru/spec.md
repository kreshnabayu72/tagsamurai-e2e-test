---
id: TC-GS-HHR-E2E-019-activate-jalur-b-submit-sukses-penomoran-dan-brand-baru
title: "Aktivasi Jalur B Berhasil: Source Self-Purchased, Penomoran Device Name per ID, Brand Baru, Model/Type Kosong, Stay on Form, dan Counter yang Tidak Dipakai Ulang"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-70
  - TC-GS-HHR-72
  - TC-GS-HHR-73
  - TC-GS-HHR-486
  - TC-GS-HHR-487
coverage:
  web: automated
---

# Aktivasi Jalur B Berhasil: Source Self-Purchased, Penomoran Device Name per ID, Brand Baru, Model/Type Kosong, Stay on Form, dan Counter yang Tidak Dipakai Ulang

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec membuat dan menghapus reader di Client A, mengonsumsi kuota, mengubah counter `N` per Device Name, memakai simulator USB bersama, dan memulihkan state di tengah spec.
- Aktor: Total Control Sari Dewi (Client A, toggle `Allow Self-Purchased Device Activation` aktif) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_gs-handheld-reader` mengikuti hook suite (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji `tc-hardware-handheld-reader.md`):
  - Client A plan Growth, Seed Reader A DD-01 s.d. DD-10 (`Short Range` `5 of 8`, `Long Range` `5 of 6`); DD-05 `Chainway C72 - 1` dan DD-08 `Unitech EA520 - 1` sudah ada sehingga reader baru bernomor `- 2`; DN-05 `Handheld Terminal` belum punya unit (`N` mulai 1).
  - Serial Jalur B bebas (tidak ada di stok Principal): `SN-HHR-00302` dan `SN-HHR-00303`; reader `SN-HHR-00302` mengembalikan Current Power 20 dBm.
  - Katalog Device Name Admin Console, dibaca Client A read-only: DN-01 `Chainway C72`, DN-03 `Unitech EA520`, DN-05 `Handheld Terminal`. `SKU-HHR-01` (Zebra, RFD40) ada di pemilih `SKU`.
- Data Dinamis: Brand baru `Aurora Scan {runId}-019` (langkah 40 sampai 43); Brand `Chainway`, `Unitech`, dan `Zebra` adalah nilai katalog yang sudah ada.
- Pemulihan state di tengah spec: tiap blok sukses dimulai dari state awal. Langkah 15, 30, 54, dan 80 memulihkan Seed Reader A (menghapus reader hasil aktivasi), kuota `Short Range` `5 of 8` dan `Long Range` `5 of 6`, counter `N` Device Name (`Chainway C72` ke 1, `Unitech EA520` ke 1, `Handheld Terminal` ke 0), dan serial `SN-HHR-00302` serta `SN-HHR-00303` ke bebas lewat reset fixture backend dan hook reset counter (Catatan TC: "mutasi TC sebelumnya tidak dibawa ke TC berikutnya"); mekanisme disediakan tim FE/BE. Kuota `Long Range` hanya 5 dari 6 sehingga hanya satu aktivasi `Long Range` sukses per state awal.
- Kemampuan teknis: simulator reader USB dan driver lokal (disediakan tim FE; mekanisme tidak didefinisikan di TC, PRD, atau LLD) yang menyajikan reader `SN-HHR-00302` dan `SN-HHR-00303` bergantian; seluruh TC spec ini berlabel Manual Only (b) di TC sumber. Reset fixture backend dan counter `N` (di atas). Pembacaan daftar opsi combobox `Brand`.
- Cleanup (hook `after`, tidak berasumsi spec berjalan penuh): pulihkan state seperti di atas, pulihkan Column Visibility ke default (langkah 26 mengaktifkan kolom `Model/Type`), dan tutup popup yang masih terbuka.

## Test Steps

### TC-GS-HHR-70: Submit aktivasi Jalur B berhasil dengan Source Self-Purchased

1. Klik `[+ Activate Reader]`
2. Klik `Long Range` pada Overlay `Select Range Type`
3. Sambungkan reader dengan Serial Number `SN-HHR-00302` (Current Power 20 dBm) lewat simulator reader USB
4. Klik `[Sync]`
5. Pilih `Chainway C72` pada pemilih `Device Name`
6. Isi `Brand` dengan `Chainway`
7. Isi `Model/Type` dengan `C72`
8. Klik `[Submit]`
9. Verifikasi muncul toast sukses: "Success, Chainway C72 - 2 has been activated."
10. Verifikasi kartu `Long Range` menampilkan `6 of 6`
11. Verifikasi kartu `Long Range` menampilkan `0 remaining`
12. Ketik Search `Chainway C72 - 2`, tekan Enter
13. Verifikasi baris baru `Chainway C72 - 2` menampilkan `SKU` `—`, `Source` `Self-Purchased`, `Status` `Available`, dan `Reader Power` `20 dBm`
14. Klik `(←)` pada kotak Search
15. Pulihkan state awal lewat reset fixture backend dan counter `N` Device Name
16. Muat ulang halaman Handheld Reader (`F5`)

### TC-GS-HHR-72: Model/Type opsional, aktivasi tanpa Model/Type berhasil

17. Klik `[+ Activate Reader]`
18. Klik `Long Range` pada Overlay `Select Range Type`
19. Sambungkan reader dengan Serial Number `SN-HHR-00302` lewat simulator reader USB
20. Klik `[Sync]`
21. Pilih `Unitech EA520` pada `Device Name`
22. Isi `Brand` dengan `Unitech` dan biarkan `Model/Type` kosong
23. Verifikasi `[Submit]` enabled tanpa `Model/Type`
24. Klik `[Submit]`
25. Verifikasi muncul toast sukses: "Success, Unitech EA520 - 2 has been activated."
26. Aktifkan kolom `Model/Type` lewat Overlay Column Visibility
27. Ketik Search `Unitech EA520 - 2`, tekan Enter
28. Verifikasi baris baru `Unitech EA520 - 2` menampilkan `Model/Type` `—`
29. Klik `(←)` pada kotak Search
30. Pulihkan state awal lewat reset fixture backend dan counter `N` Device Name
31. Muat ulang halaman Handheld Reader (`F5`)

### TC-GS-HHR-73: Combobox Brand, opsi Add muncul bila teks tidak cocok dan nilai baru langsung dipakai

32. Klik `[+ Activate Reader]`
33. Klik `Long Range` pada Overlay `Select Range Type`
34. Sambungkan reader dengan Serial Number `SN-HHR-00302` lewat simulator reader USB
35. Klik `[Sync]`
36. Pilih `Handheld Terminal` pada `Device Name`
37. Ketik `Zebra` pada `Brand`
38. Verifikasi daftar opsi `Brand` menampilkan opsi `Zebra` dari daftar yang sudah ada
39. Hapus teks pada `Brand`
40. Ketik `Aurora Scan {runId}-019` pada `Brand`
41. Verifikasi daftar opsi menampilkan opsi `Add 'Aurora Scan {runId}-019'` di bagian bawah daftar
42. Pilih opsi `Add 'Aurora Scan {runId}-019'`
43. Verifikasi `Brand` terisi `Aurora Scan {runId}-019`
44. Isi `Model/Type` dengan `A1`
45. Klik `[Submit]`
46. Verifikasi muncul toast sukses: "Success, Handheld Terminal - 1 has been activated."
47. Klik `[+ Activate Reader]`
48. Klik `Short Range` pada Overlay `Select Range Type`
49. Sambungkan reader dengan Serial Number `SN-HHR-00303` lewat simulator reader USB
50. Klik `[Sync]`
51. Ketik `Aurora` pada `Brand`
52. Verifikasi daftar opsi `Brand` menampilkan opsi `Aurora Scan {runId}-019`
53. Klik `[✕]` di header popup, lalu klik `[Cancel Activation]` pada dialog
54. Pulihkan state awal lewat reset fixture backend dan counter `N` Device Name
55. Muat ulang halaman Handheld Reader (`F5`)

### TC-GS-HHR-486: Nama unit mengikuti Device Name katalog dan N dihitung per ID Device Name walau SKU berbeda

56. Klik `[+ Activate Reader]`
57. Klik `Short Range` pada Overlay `Select Range Type`
58. Centang `Stay on this form after submitting`
59. Sambungkan reader dengan Serial Number `SN-HHR-00302` lewat simulator reader USB
60. Klik `[Sync]`
61. Pilih `Handheld Terminal` pada `Device Name`
62. Isi `Brand` dengan `Zebra`
63. Klik `[Submit]`
64. Verifikasi muncul toast sukses: "Success, Handheld Terminal - 1 has been activated."
65. Verifikasi Popup `Activate Handheld Reader` tetap terbuka
66. Verifikasi popup pada state Menunggu Sync: `Serial Number`, label jalur, `Device Name`, `SKU`, `Brand`, `Model/Type`, slider `Reader Power`, dan `Alias Name` tidak tampil
67. Sambungkan reader dengan Serial Number `SN-HHR-00303` lewat simulator reader USB
68. Klik `[Sync]`
69. Pilih `Handheld Terminal` pada `Device Name`
70. Pilih `SKU-HHR-01` pada `SKU`
71. Klik `[Submit]`
72. Verifikasi muncul toast sukses: "Success, Handheld Terminal - 2 has been activated."
73. Klik `[✕]` di header popup
74. Ketik Search `Handheld Terminal`, tekan Enter
75. Verifikasi baris `Handheld Terminal - 1` menampilkan `SKU` `—`
76. Verifikasi baris `Handheld Terminal - 2` menampilkan `SKU` `SKU-HHR-01`
77. Klik `(←)` pada kotak Search
78. Verifikasi kartu `Short Range` menampilkan `7 of 8`
79. Verifikasi kartu `Short Range` menampilkan `1 remaining`
80. Pulihkan state awal lewat reset fixture backend dan counter `N` Device Name
81. Muat ulang halaman Handheld Reader (`F5`)

### TC-GS-HHR-487: Counter N per ID Device Name tidak dipakai ulang setelah reader dihapus (destruktif, terakhir)

82. Klik `[+ Activate Reader]`
83. Klik `Short Range` pada Overlay `Select Range Type`
84. Sambungkan reader dengan Serial Number `SN-HHR-00302` lewat simulator reader USB
85. Klik `[Sync]`
86. Pilih `Handheld Terminal` pada `Device Name`
87. Isi `Brand` dengan `Zebra`
88. Klik `[Submit]`
89. Verifikasi muncul toast sukses: "Success, Handheld Terminal - 1 has been activated."
90. Ketik Search `Handheld Terminal - 1`, tekan Enter
91. Klik `⋯` pada baris `Handheld Terminal - 1`
92. Pilih `Delete`
93. Klik `[Delete]` pada dialog
94. Verifikasi muncul toast sukses: "Success, Handheld Terminal - 1 has been deleted."
95. Klik `(←)` pada kotak Search
96. Klik `[+ Activate Reader]`
97. Klik `Short Range` pada Overlay `Select Range Type`
98. Sambungkan reader dengan Serial Number `SN-HHR-00303` lewat simulator reader USB
99. Klik `[Sync]`
100. Pilih `Handheld Terminal` pada `Device Name`
101. Isi `Brand` dengan `Zebra`
102. Klik `[Submit]`
103. Verifikasi muncul toast sukses: "Success, Handheld Terminal - 2 has been activated." (nomor `1` tidak dipakai ulang)
104. Ketik Search `Handheld Terminal`, tekan Enter
105. Verifikasi baris `Handheld Terminal - 2` tampil di daftar
106. Verifikasi tidak ada baris `Handheld Terminal - 1` di daftar
107. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Kelas harness: eksternal (d), simulator reader USB; seluruh TC berlabel Manual Only (b). Satu topik (submit sukses Jalur B), satu akun, satu harness. Aksi destruktif (Delete reader milik spec) berada di blok terakhir (TC-GS-HHR-487).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (107 langkah). Alasan: lima blok sukses yang masing-masing mengulang prefix `Klik [+ Activate Reader]` sampai `Klik [Sync]` dan Submit, ditambah pemulihan state; 25 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01). Tiap blok dimulai dari state hasil reset (langkah 15, 30, 54, 80) sehingga kegagalan satu blok tidak membuat blok berikutnya kehilangan makna; semua blok satu kelas harness dan satu akun. Kuota `Long Range` (5 dari 6) dan counter `N` Device Name membuat blok sukses tidak dapat digabung tanpa pemulihan.
- Langkah penghubung (tanpa `Verifikasi`): langkah 3, 19, 34, 49, 59, 67, 84, 98 (menyiapkan reader di simulator); langkah 12, 27, 74, 90, 104 (Search untuk menemukan baris target) dan langkah 14, 29, 77, 95, 107 (mengosongkan Search); langkah 15, 16, 30, 31, 54, 55, 80, 81 (pemulihan state dan muat ulang); langkah 26 (mengaktifkan kolom `Model/Type` sesuai langkah TC-GS-HHR-72); langkah 53 (menutup popup yang berisi hasil Sync); langkah 73 (menutup popup yang sudah kembali ke state Menunggu Sync).
- Brand baru TC-GS-HHR-73 ditulis `Aurora Scan {runId}-019` supaya opsi `Add '...'` muncul pada tiap run (S-12); asersi memakai nilai bersuffix yang sama.
- Asersi absence langkah 106 didahului toast sukses Delete (langkah 94) dan `Verifikasi` baris `Handheld Terminal - 2` tampil (langkah 105) sebagai anchor (butir 2 bagian 8b); asersi absence langkah 66 didahului `Verifikasi` popup tetap terbuka (langkah 65).
- Langkah 9, 25, 46, 64, 72, 89, 94, 103 (toast) diasersi tepat sesudah pemicu karena toast bersifat sementara.
- Temuan untuk QA:
  - Mekanisme simulasi reader USB, pembacaan Current Power, pemulihan serial `SN-HHR-00302` dan `SN-HHR-00303` ke bebas, reset fixture backend, dan reset counter `N` Device Name di tengah spec tidak didefinisikan di TC, PRD, atau LLD; spec mencatat kebutuhan di Prerequisites tanpa mengarang endpoint.
  - TC-GS-HHR-73 Expected e ("`Aurora Scan` tersedia sebagai opsi `Brand` pada aktivasi Jalur B berikutnya") tidak menyebut Range Type, reader, atau cara pembuktian; spec membuka aktivasi `Short Range` dengan `SN-HHR-00303` (kuota `Long Range` sudah habis sesudah Submit) dan mengasersi opsi muncul saat mengetik `Aurora` (langkah 47 sampai 52).
  - TC-GS-HHR-72 mengaktifkan kolom `Model/Type` lewat Column Visibility (langkah TC 7) sehingga kolom itu tersembunyi secara default; spec memulihkan kolom ke default di hook `after`.
  - TC-GS-HHR-487 langkah 6 ("Ulangi aktivasi Short Range dengan reader SN-HHR-00303") tidak menyebut `[Sync]` secara eksplisit; spec menyalin langkah aktivasi utuh termasuk `[Sync]` (langkah 96 sampai 102) sesuai S-04.
  - Brand `Aurora Scan {runId}-019` yang dibuat TC-GS-HHR-73 tidak punya cara pembersihan di TC; pembersihan Brand baru disediakan tim FE/BE bila diperlukan.
