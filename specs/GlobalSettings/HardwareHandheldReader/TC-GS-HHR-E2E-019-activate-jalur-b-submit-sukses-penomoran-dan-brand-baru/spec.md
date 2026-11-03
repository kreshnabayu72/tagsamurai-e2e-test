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
  - Katalog Device Name Admin Console, dibaca Client A read-only: DN-01 `Chainway C72`, DN-03 `Unitech EA520`, DN-05 `Handheld Terminal`. SKU-486: satu SKU katalog yang Device Name-nya `Handheld Terminal` (DN-05) dan ada di pemilih `SKU`; kode SKU disediakan pemilik TC (TC-GS-HHR-486 tidak menyebut kodenya; lihat Temuan untuk QA).
- Data Dinamis: Brand baru `Aurora Scan {runId}-019` (langkah 43 sampai 46); Brand `Chainway`, `Unitech`, dan `Zebra` adalah nilai katalog yang sudah ada.
- Pemulihan state di tengah spec: tiap blok sukses dimulai dari state awal. Langkah 18, 33, 59, dan 84 memulihkan Seed Reader A (menghapus reader hasil aktivasi), kuota `Short Range` `5 of 8` dan `Long Range` `5 of 6`, counter `N` Device Name (`Chainway C72` ke 1, `Unitech EA520` ke 1, `Handheld Terminal` ke 0), dan serial `SN-HHR-00302` serta `SN-HHR-00303` ke bebas lewat reset fixture backend dan hook reset counter (Catatan TC: "mutasi TC sebelumnya tidak dibawa ke TC berikutnya"); mekanisme disediakan tim FE/BE. Kuota `Long Range` hanya 5 dari 6 sehingga hanya satu aktivasi `Long Range` sukses per state awal.
- Kemampuan teknis: simulator reader USB dan driver lokal (disediakan tim FE; mekanisme tidak didefinisikan di TC, PRD, atau LLD) yang menyajikan reader `SN-HHR-00302` dan `SN-HHR-00303` bergantian; seluruh TC spec ini berlabel Manual Only (b) di TC sumber. Reset fixture backend dan counter `N` (di atas). Pembacaan daftar opsi combobox `Brand`.
- Cleanup (hook `after`, tidak berasumsi spec berjalan penuh): pulihkan state seperti di atas, pulihkan Column Visibility ke default (langkah 29 mengaktifkan kolom `Model/Type`), dan tutup popup yang masih terbuka.

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
13. Verifikasi baris baru `Chainway C72 - 2` menampilkan `SKU` `—`
14. Verifikasi baris `Chainway C72 - 2` menampilkan `Source` `Self-Purchased`
15. Verifikasi baris `Chainway C72 - 2` menampilkan `Status` `Available`
16. Verifikasi baris `Chainway C72 - 2` menampilkan `Reader Power` `20 dBm`
17. Klik `(←)` pada kotak Search
18. Pulihkan state awal lewat reset fixture backend dan counter `N` Device Name
19. Muat ulang halaman Handheld Reader (`F5`)

### TC-GS-HHR-72: Model/Type opsional, aktivasi tanpa Model/Type berhasil

20. Klik `[+ Activate Reader]`
21. Klik `Long Range` pada Overlay `Select Range Type`
22. Sambungkan reader dengan Serial Number `SN-HHR-00302` lewat simulator reader USB
23. Klik `[Sync]`
24. Pilih `Unitech EA520` pada `Device Name`
25. Isi `Brand` dengan `Unitech` dan biarkan `Model/Type` kosong
26. Verifikasi `[Submit]` enabled tanpa `Model/Type`
27. Klik `[Submit]`
28. Verifikasi muncul toast sukses: "Success, Unitech EA520 - 2 has been activated."
29. Aktifkan kolom `Model/Type` lewat Overlay Column Visibility
30. Ketik Search `Unitech EA520 - 2`, tekan Enter
31. Verifikasi baris baru `Unitech EA520 - 2` menampilkan `Model/Type` `—`
32. Klik `(←)` pada kotak Search
33. Pulihkan state awal lewat reset fixture backend dan counter `N` Device Name
34. Muat ulang halaman Handheld Reader (`F5`)

### TC-GS-HHR-73: Combobox Brand, opsi Add muncul bila teks tidak cocok dan nilai baru langsung dipakai

35. Klik `[+ Activate Reader]`
36. Klik `Long Range` pada Overlay `Select Range Type`
37. Sambungkan reader dengan Serial Number `SN-HHR-00302` lewat simulator reader USB
38. Klik `[Sync]`
39. Pilih `Handheld Terminal` pada `Device Name`
40. Ketik `Zebra` pada `Brand`
41. Verifikasi daftar opsi `Brand` menampilkan opsi `Zebra` dari daftar yang sudah ada
42. Hapus teks pada `Brand`
43. Ketik `Aurora Scan {runId}-019` pada `Brand`
44. Verifikasi daftar opsi menampilkan opsi `Add 'Aurora Scan {runId}-019'` di bagian bawah daftar
45. Pilih opsi `Add 'Aurora Scan {runId}-019'`
46. Verifikasi `Brand` terisi `Aurora Scan {runId}-019`
47. Isi `Model/Type` dengan `A1`
48. Klik `[Submit]`
49. Verifikasi muncul toast sukses: "Success, Handheld Terminal - 1 has been activated."
50. Klik `[+ Activate Reader]`
51. Klik `Short Range` pada Overlay `Select Range Type`
52. Sambungkan reader dengan Serial Number `SN-HHR-00303` lewat simulator reader USB
53. Klik `[Sync]`
54. Ketik `Aurora` pada `Brand`
55. Verifikasi daftar opsi `Brand` menampilkan opsi `Aurora Scan {runId}-019`
56. Klik `[✕]` di header popup
57. Verifikasi dialog `Cancel Activation` tampil dengan body "Are you sure you want to cancel this activation? The Sync progress you've made will be lost." dan tombol `[Go Back]` `[Cancel Activation]`
58. Klik `[Cancel Activation]`
59. Pulihkan state awal lewat reset fixture backend dan counter `N` Device Name
60. Muat ulang halaman Handheld Reader (`F5`)

### TC-GS-HHR-486: Nama unit mengikuti Device Name katalog dan N dihitung per ID Device Name walau SKU berbeda

61. Klik `[+ Activate Reader]`
62. Klik `Short Range` pada Overlay `Select Range Type`
63. Centang `Stay on this form after submitting`
64. Sambungkan reader dengan Serial Number `SN-HHR-00302` lewat simulator reader USB
65. Klik `[Sync]`
66. Pilih `Handheld Terminal` pada `Device Name`
67. Isi `Brand` dengan `Zebra`
68. Klik `[Submit]`
69. Verifikasi muncul toast sukses: "Success, Handheld Terminal - 1 has been activated."
70. Verifikasi Popup `Activate Handheld Reader` tetap terbuka
71. Verifikasi popup pada state Menunggu Sync: `Serial Number`, label jalur, `Device Name`, `SKU`, `Brand`, `Model/Type`, slider `Reader Power`, dan `Alias Name` tidak tampil
72. Sambungkan reader dengan Serial Number `SN-HHR-00303` lewat simulator reader USB
73. Klik `[Sync]`
74. Pilih pada `SKU` satu SKU katalog ber-Device Name `Handheld Terminal` (SKU-486)
75. Klik `[Submit]`
76. Verifikasi muncul toast sukses: "Success, Handheld Terminal - 2 has been activated."
77. Klik `[✕]` di header popup
78. Ketik Search `Handheld Terminal`, tekan Enter
79. Verifikasi baris `Handheld Terminal - 1` menampilkan `SKU` `—`
80. Verifikasi baris `Handheld Terminal - 2` menampilkan `SKU` berisi SKU-486 yang dipilih pada langkah 74
81. Klik `(←)` pada kotak Search
82. Verifikasi kartu `Short Range` menampilkan `7 of 8`
83. Verifikasi kartu `Short Range` menampilkan `1 remaining`
84. Pulihkan state awal lewat reset fixture backend dan counter `N` Device Name
85. Muat ulang halaman Handheld Reader (`F5`)

### TC-GS-HHR-487: Counter N per ID Device Name tidak dipakai ulang setelah reader dihapus (destruktif, terakhir)

86. Klik `[+ Activate Reader]`
87. Klik `Short Range` pada Overlay `Select Range Type`
88. Sambungkan reader dengan Serial Number `SN-HHR-00302` lewat simulator reader USB
89. Klik `[Sync]`
90. Pilih `Handheld Terminal` pada `Device Name`
91. Isi `Brand` dengan `Zebra`
92. Klik `[Submit]`
93. Verifikasi muncul toast sukses: "Success, Handheld Terminal - 1 has been activated."
94. Ketik Search `Handheld Terminal - 1`, tekan Enter
95. Klik `⋯` pada baris `Handheld Terminal - 1`
96. Pilih `Delete`
97. Klik `[Delete]` pada dialog
98. Verifikasi muncul toast sukses: "Success, Handheld Terminal - 1 has been deleted."
99. Klik `(←)` pada kotak Search
100. Klik `[+ Activate Reader]`
101. Klik `Short Range` pada Overlay `Select Range Type`
102. Sambungkan reader dengan Serial Number `SN-HHR-00303` lewat simulator reader USB
103. Klik `[Sync]`
104. Pilih `Handheld Terminal` pada `Device Name`
105. Isi `Brand` dengan `Zebra`
106. Klik `[Submit]`
107. Verifikasi muncul toast sukses: "Success, Handheld Terminal - 2 has been activated." (nomor `1` tidak dipakai ulang)
108. Ketik Search `Handheld Terminal`, tekan Enter
109. Verifikasi baris `Handheld Terminal - 2` tampil di daftar
110. Verifikasi tidak ada baris `Handheld Terminal - 1` di daftar
111. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Kelas harness: eksternal (d), simulator reader USB; seluruh TC berlabel Manual Only (b). Satu topik (submit sukses Jalur B), satu akun, satu harness. Aksi destruktif (Delete reader milik spec) berada di blok terakhir (TC-GS-HHR-487).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (111 langkah). Alasan: lima blok sukses yang masing-masing mengulang prefix `Klik [+ Activate Reader]` sampai `Klik [Sync]` dan Submit, ditambah pemulihan state; 29 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01). Tiap blok dimulai dari state hasil reset (langkah 18, 33, 59, 84) sehingga kegagalan satu blok tidak membuat blok berikutnya kehilangan makna; semua blok satu kelas harness dan satu akun. Kuota `Long Range` (5 dari 6) dan counter `N` Device Name membuat blok sukses tidak dapat digabung tanpa pemulihan.
- Langkah penghubung (tanpa `Verifikasi`): langkah 3, 22, 37, 52, 64, 72, 88, 102 (menyiapkan reader di simulator); langkah 12, 30, 78, 94, 108 (Search untuk menemukan baris target) dan langkah 17, 32, 81, 99, 111 (mengosongkan Search); langkah 18, 19, 33, 34, 59, 60, 84, 85 (pemulihan state dan muat ulang); langkah 29 (mengaktifkan kolom `Model/Type` sesuai langkah TC-GS-HHR-72); langkah 56 sampai 58 (menutup popup yang berisi hasil Sync lewat dialog `Cancel Activation`, S-08; teks dialog mengikuti Expected TC-GS-HHR-89); langkah 77 (menutup popup yang sudah kembali ke state Menunggu Sync).
- Brand baru TC-GS-HHR-73 ditulis `Aurora Scan {runId}-019` supaya opsi `Add '...'` muncul pada tiap run (S-12); asersi memakai nilai bersuffix yang sama.
- Asersi absence langkah 110 didahului toast sukses Delete (langkah 98) dan `Verifikasi` baris `Handheld Terminal - 2` tampil (langkah 109) sebagai anchor (butir 2 bagian 8b); asersi absence langkah 71 didahului `Verifikasi` popup tetap terbuka (langkah 70).
- Langkah 9, 28, 49, 69, 76, 93, 98, 107 (toast) diasersi tepat sesudah pemicu karena toast bersifat sementara.
- Temuan untuk QA:
  - Mekanisme simulasi reader USB, pembacaan Current Power, pemulihan serial `SN-HHR-00302` dan `SN-HHR-00303` ke bebas, reset fixture backend, dan reset counter `N` Device Name di tengah spec tidak didefinisikan di TC, PRD, atau LLD; spec mencatat kebutuhan di Prerequisites tanpa mengarang endpoint.
  - TC-GS-HHR-73 Expected e ("`Aurora Scan` tersedia sebagai opsi `Brand` pada aktivasi Jalur B berikutnya") tidak menyebut Range Type, reader, atau cara pembuktian; spec membuka aktivasi `Short Range` dengan `SN-HHR-00303` (kuota `Long Range` sudah habis sesudah Submit) dan mengasersi opsi muncul saat mengetik `Aurora` (langkah 50 sampai 55).
  - TC-GS-HHR-72 mengaktifkan kolom `Model/Type` lewat Column Visibility (langkah TC 7) sehingga kolom itu tersembunyi secara default; spec memulihkan kolom ke default di hook `after`.
  - TC-GS-HHR-487 langkah 6 ("Ulangi aktivasi Short Range dengan reader SN-HHR-00303") tidak menyebut `[Sync]` secara eksplisit; spec menyalin langkah aktivasi utuh termasuk `[Sync]` (langkah 100 sampai 106) sesuai S-04.
  - TC-GS-HHR-486 langkah 7 memilih "satu SKU yang katalognya memuat Device Name `Handheld Terminal`" tanpa menyebut kode SKU (data uji "ditetapkan pemilik TC dari Tabel Data Uji"); spec menamainya SKU-486 dan menyerahkan kodenya ke pemilik TC. Pemilihan SKU mengisi dan mengunci Device Name, Brand, dan Model/Type dari katalog (all-tags.md FI-01, dirujuk TC); TC tidak mengasersinya sehingga spec tidak menambah asersi. Asersi `SKU` baris `Handheld Terminal - 2` memakai SKU-486 itu, bukan literal `SKU-HHR-01`.
  - Brand `Aurora Scan {runId}-019` yang dibuat TC-GS-HHR-73 tidak punya cara pembersihan di TC; pembersihan Brand baru disediakan tim FE/BE bila diperlukan.
