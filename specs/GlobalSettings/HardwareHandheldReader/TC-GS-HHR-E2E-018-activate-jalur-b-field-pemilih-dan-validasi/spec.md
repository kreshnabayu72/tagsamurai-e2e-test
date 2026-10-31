---
id: TC-GS-HHR-E2E-018-activate-jalur-b-field-pemilih-dan-validasi
title: "Aktivasi Jalur B (Self-Purchased): Field, Pemilih Device Name dan SKU, Validasi Submit, Batas 120 Karakter, dan Default Reader Power 30 dBm"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-69
  - TC-GS-HHR-71
  - TC-GS-HHR-74
  - TC-GS-HHR-445
  - TC-GS-HHR-479
  - TC-GS-HHR-480
  - TC-GS-HHR-481
  - TC-GS-HHR-484
  - TC-GS-HHR-485
coverage:
  web: automated
---

# Aktivasi Jalur B (Self-Purchased): Field, Pemilih Device Name dan SKU, Validasi Submit, Batas 120 Karakter, dan Default Reader Power 30 dBm

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec membuat satu reader Self-Purchased di Client A (langkah 88), memakai simulator USB bersama, dan membaca katalog Device Name Admin Console.
- Aktor: Total Control Sari Dewi (Client A, toggle `Allow Self-Purchased Device Activation` aktif) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_gs-handheld-reader` mengikuti hook suite (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji `tc-hardware-handheld-reader.md`):
  - Client A plan Growth, Seed Reader A DD-01 s.d. DD-10 (`Short Range` `5 of 8`, `Long Range` `5 of 6`); DD-05 (`Chainway C72 - 1`) sudah ada sehingga reader baru `Chainway C72` bernomor `- 2`.
  - Serial Jalur B (tidak ada di stok Principal): `SN-HHR-00302` (Current Power 20 dBm via driver) dan `SN-HHR-00303` (reader tidak mengembalikan nilai daya).
  - Katalog Device Name Admin Console, dibaca Client A read-only: DN-01 `Chainway C72`, DN-02 `Honeywell CK65`, DN-03 `Unitech EA520`, DN-04 `International Handheld Terminals Ltd Ultra-Rugged Series 7000 Pro Max`, DN-05 `Handheld Terminal` (Category Hardware > Handheld Reader dan turunannya, termasuk UHF Handheld); DN-06 `Gate Antenna` (Hardware > Smart Fixed Reader > Antenna) dan DN-07 `Access Card Reader` (TAG > NFC) di luar konteks `Handheld Reader`.
  - Pemilih `SKU` Jalur B memuat `SKU-HHR-01` sampai `SKU-HHR-04`; `SKU-HHR-03` berisi Brand `Chainway` dan Model/Type `C66`.
  - State awal dipulihkan oleh fixture backend sebelum spec (Catatan TC; mekanisme disediakan tim FE/BE).
- Efek spec: langkah 88 membuat reader `Chainway C72 - 2` (Short Range, `SKU-HHR-03`, Self-Purchased) di Client A; kuota `Short Range` menjadi `6 of 8`. Hook `after` memulihkan Seed Reader A dan kuota Client A lewat reset fixture backend (disediakan tim FE/BE). Brand dan Model/Type yang diketik adalah nilai katalog yang sudah ada; tidak ada nilai baru yang dibuat.
- Kemampuan teknis: simulator reader USB dan driver lokal (disediakan tim FE; mekanisme tidak didefinisikan di TC, PRD, atau LLD) yang menyajikan reader `SN-HHR-00302` (Current Power 20 dBm) dan `SN-HHR-00303` (tanpa nilai daya) bergantian; seluruh TC spec ini berlabel Manual Only (b) di TC sumber. Pembacaan atribut placeholder, tanda wajib `*`, batas panjang, state terkunci field, dan keberadaan tooltip.
- Cleanup (hook `after`, tidak berasumsi spec berjalan penuh): tutup popup yang masih terbuka dan pulihkan state seperti di atas.

## Test Steps

### Popup 1: Long Range, reader SN-HHR-00302

1. Klik `[+ Activate Reader]`
2. Klik `Long Range` pada Overlay `Select Range Type`
3. Sambungkan reader dengan Serial Number `SN-HHR-00302` (di luar stok Principal, Current Power 20 dBm) lewat simulator reader USB
4. Klik `[Sync]`

### TC-GS-HHR-69: Empat field Jalur B tampil setelah Sync

5. Verifikasi `Serial Number` read-only terisi `SN-HHR-00302`
6. Verifikasi label `Official` tidak tampil
7. Verifikasi pemilih katalog `Device Name` bertanda wajib `*`, placeholder `Search and select device name...`, dan kosong
8. Verifikasi pemilih katalog `SKU` (opsional) memiliki placeholder `Search and select SKU (optional)...` dan kosong
9. Verifikasi combobox search-or-create `Brand` memiliki placeholder `Search or add a brand...` dan kosong
10. Verifikasi `Brand` bertanda wajib `*` selama `SKU` kosong
11. Verifikasi `Brand` membatasi maksimum 120 karakter
12. Verifikasi combobox search-or-create `Model/Type` (opsional) memiliki placeholder `Search or add a model/type...` dan kosong
13. Verifikasi `Model/Type` membatasi maksimum 120 karakter
14. Verifikasi slider `Reader Power` terisi `20 dBm`
15. Verifikasi `[Submit]` disabled

### TC-GS-HHR-479: Pemilih Device Name (daftar opsi terfilter Category Handheld Reader)

16. Klik field `Device Name`
17. Verifikasi daftar opsi memuat `Chainway C72`, `Honeywell CK65`, `Unitech EA520`, `International Handheld Terminals Ltd Ultra-Rugged Series 7000 Pro Max`, dan `Handheld Terminal`
18. Verifikasi daftar opsi tidak memuat `Gate Antenna` maupun `Access Card Reader`

### TC-GS-HHR-480: Nilai Device Name di luar katalog tidak dapat dibuat

19. Ketik `Perangkat Tidak Terdaftar` pada field `Device Name`
20. Verifikasi daftar opsi `Device Name` tampil
21. Verifikasi daftar tidak menawarkan opsi `Add 'Perangkat Tidak Terdaftar'`
22. Isi `Brand` dengan `Chainway`
23. Verifikasi teks `Perangkat Tidak Terdaftar` yang diketik tanpa memilih opsi bukan nilai terpilih: `Device Name` tetap belum terpilih (tidak ada nilai katalog yang dipilih)
24. Verifikasi `[Submit]` tetap disabled walau `Brand` terisi
25. Kosongkan teks yang diketik pada field `Device Name`

### TC-GS-HHR-481: Submit disabled selama Device Name belum dipilih

26. Isi `Model/Type` dengan `C72` (`Brand` sudah `Chainway`, `Device Name` kosong)
27. Verifikasi `[Submit]` disabled
28. Verifikasi tidak ada tooltip pada `[Submit]`
29. Pilih `Chainway C72` pada `Device Name`
30. Verifikasi `[Submit]` enabled

### TC-GS-HHR-71: Submit disabled selama Brand kosong dan SKU belum dipilih

31. Kosongkan isi `Brand` (`SKU` tetap kosong; `Device Name` `Chainway C72` dan `Model/Type` `C72` terisi)
32. Verifikasi `[Submit]` disabled
33. Verifikasi tanda `*` pada `Brand` tampil selama `SKU` kosong
34. Verifikasi tidak ada tooltip pada `[Submit]`
35. Isi `Brand` dengan `Chainway`
36. Verifikasi `[Submit]` enabled

### TC-GS-HHR-74: Batas 120 karakter Brand dan Model/Type

37. Ganti isi `Brand` dengan 120 karakter `A`
38. Ganti isi `Model/Type` dengan 120 karakter `B`
39. Verifikasi tidak ada pesan inline pada `Brand` dan `Model/Type`
40. Verifikasi `[Submit]` enabled
41. Tambah satu karakter pada `Brand` (121 karakter)
42. Verifikasi pesan inline `Max. 120 characters` pada `Brand`
43. Verifikasi `[Submit]` disabled
44. Kembalikan `Brand` ke 120 karakter, lalu tambah satu karakter pada `Model/Type` (121 karakter)
45. Verifikasi pesan inline `Max. 120 characters` pada `Model/Type`
46. Verifikasi `[Submit]` disabled

### TC-GS-HHR-479 (lanjutan): Pencarian dan pemilihan Device Name

47. Ganti isi field `Device Name` dengan `Unitech`
48. Verifikasi daftar opsi dipersempit dibanding daftar penuh pada langkah 17
49. Verifikasi daftar opsi memuat `Unitech EA520`
50. Pilih opsi `Unitech EA520`
51. Verifikasi field `Device Name` menampilkan `Unitech EA520`
52. Klik `[✕]` di header popup
53. Verifikasi dialog `Cancel Activation` tampil dengan body "Are you sure you want to cancel this activation? The Sync progress you've made will be lost." dan tombol `[Go Back]` `[Cancel Activation]`
54. Klik `[Cancel Activation]`

### Popup 2: Long Range, reader SN-HHR-00303

55. Klik `[+ Activate Reader]`
56. Klik `Long Range` pada Overlay `Select Range Type`
57. Sambungkan reader dengan Serial Number `SN-HHR-00303` (di luar stok Principal, tanpa nilai daya) lewat simulator reader USB
58. Klik `[Sync]`

### TC-GS-HHR-445: Reader Power tidak terbaca dari reader, slider memakai default 30 dBm

59. Verifikasi `Serial Number` read-only terisi `SN-HHR-00303`
60. Verifikasi label `Official` tidak tampil
61. Verifikasi slider `Reader Power` terisi nilai awal `30 dBm`
62. Verifikasi slider `Reader Power` dapat digeser
63. Klik `[✕]` di header popup
64. Verifikasi dialog `Cancel Activation` tampil dengan body "Are you sure you want to cancel this activation? The Sync progress you've made will be lost." dan tombol `[Go Back]` `[Cancel Activation]`
65. Klik `[Cancel Activation]`

### Popup 3: Short Range, reader SN-HHR-00302

66. Klik `[+ Activate Reader]`
67. Klik `Short Range` pada Overlay `Select Range Type`
68. Sambungkan reader dengan Serial Number `SN-HHR-00302` lewat simulator reader USB
69. Klik `[Sync]`

### TC-GS-HHR-484: Memilih SKU opsional mengisi Brand dan Model/Type

70. Pilih `Chainway C72` pada `Device Name`
71. Klik `[Clear Field]` sehingga `Device Name` kembali kosong
72. Pilih `SKU-HHR-03` pada `SKU`
73. Verifikasi `Device Name` terisi `Chainway C72`
74. Verifikasi `Brand` terisi `Chainway`
75. Verifikasi `Model/Type` terisi `C66`
76. Verifikasi tanda `*` pada `Brand` hilang
77. Verifikasi `Device Name`, `Brand`, dan `Model/Type` terkunci (tidak dapat diedit) selama `SKU` terisi
78. Verifikasi `[Submit]` enabled tanpa mengisi `Brand` secara manual

### TC-GS-HHR-485: Mengosongkan SKU membuat Brand wajib kembali

79. Kosongkan `SKU`
80. Verifikasi nilai `Device Name`, `Brand`, dan `Model/Type` hasil autofill dikosongkan
81. Verifikasi `Device Name`, `Brand`, dan `Model/Type` dapat diedit kembali
82. Verifikasi tanda `*` pada `Brand` tampil kembali
83. Verifikasi `[Submit]` disabled selama `Device Name` atau `Brand` kosong
84. Pilih `Chainway C72` pada `Device Name`
85. Isi `Brand` dengan `Chainway`
86. Verifikasi `[Submit]` enabled

### TC-GS-HHR-484 (lanjutan): Submit dengan SKU dan Popup Detail

87. Pilih `SKU-HHR-03` pada `SKU`
88. Klik `[Submit]`
89. Verifikasi muncul toast sukses: "Success, Chainway C72 - 2 has been activated."
90. Ketik Search `Chainway C72 - 2`, tekan Enter
91. Klik `Device Name` baris baru `Chainway C72 - 2` untuk membuka Popup Detail
92. Verifikasi Popup Detail baris baru menampilkan `SKU` `SKU-HHR-03`
93. Verifikasi Popup Detail baris baru menampilkan `Brand` `Chainway`
94. Verifikasi Popup Detail baris baru menampilkan `Model/Type` `C66`
95. Verifikasi Popup Detail baris baru menampilkan `Source` `Self-Purchased`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Kelas harness: eksternal (d), simulator reader USB; seluruh TC berlabel Manual Only (b). Satu topik (field dan validasi popup Activate Jalur B), satu akun, satu harness. Submit sukses hanya satu (TC-GS-HHR-484) dan berada di akhir; submit sukses lain berada di spec 019.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan menyimpang dari urutan nomor TC untuk memakai satu popup per reader tanpa submit (prinsip 13, halaman yang sama dipakai berulang) dan menjaga state field: TC-GS-HHR-479 dipecah dua bagian (langkah 16 sampai 18 pada field `Device Name` kosong; langkah 47 sampai 51 sesudah state field dipakai TC-GS-HHR-74) karena pemilihan `Device Name` pada langkah 50 akan mengisi field yang dibutuhkan TC-GS-HHR-480 dalam keadaan kosong; TC-GS-HHR-480, TC-GS-HHR-481, TC-GS-HHR-71, dan TC-GS-HHR-74 berurutan menurut state field (tidak terpilih, `Brand`/`Model/Type` terisi, `Brand` dikosongkan, batas panjang). TC-GS-HHR-485 dikerjakan sebelum langkah Submit TC-GS-HHR-484 (langkah 87 sampai 88) agar asersi "`[Submit]` enabled tanpa mengisi `Brand` secara manual" (langkah 78) belum tercampur isian manual; langkah 87 memilih ulang `SKU-HHR-03` sehingga autofill menimpa isian manual langkah 84 dan 85.
- Verifikasi langkah 7 memenuhi Expected b TC-GS-HHR-69 dan Expected a pertama TC-GS-HHR-479 (klausa identik: tanda wajib, placeholder, kosong); langkah 17 dan 18 memenuhi Expected b dan c TC-GS-HHR-479.
- Spec melewati sekitar 35 langkah (95 langkah). Alasan: 55 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01); tiga popup memakai prefix `Klik [+ Activate Reader]` sampai `Klik [Sync]`; semua blok satu kelas harness (simulator USB), satu topik, dan hanya langkah 88 yang menyimpan data, di akhir spec, sehingga kegagalan lunak satu blok tidak menutup makna blok lain.
- Langkah penghubung (tanpa `Verifikasi`): langkah 3, 57, 68 (menyiapkan reader di simulator); langkah 25 (mengosongkan teks `Device Name` agar field benar-benar kosong untuk TC-GS-HHR-481); langkah 52 sampai 54 dan 63 sampai 65 (menutup popup yang berisi hasil Sync lewat dialog `Cancel Activation`, S-08; teks dialog dari Expected TC-GS-HHR-89); langkah 90 (Search untuk menemukan baris target).
- Asersi absence: langkah 6, 18, 21, 60 didahului `Verifikasi` pada surface yang sama (langkah 5; langkah 17; langkah 20; langkah 59) sebagai anchor positif. Anchor langkah 20 (daftar opsi `Device Name` tampil) ditulis spec untuk butir 2 bagian 8b; TC-GS-HHR-480 tidak menyebut isi daftar untuk teks yang tidak cocok.
- Temuan untuk QA:
  - Mekanisme simulasi reader USB, driver lokal, dan nilai Current Power yang dikembalikan reader tidak didefinisikan di TC, PRD, atau LLD; spec mencatat kebutuhan di Prerequisites tanpa mengarang endpoint atau perintah simulator.
  - TC-GS-HHR-480 tidak menyebut isi daftar opsi `Device Name` untuk teks yang tidak cocok (daftar kosong, pesan, atau panel tertutup); `Verifikasi` langkah 20 hanya memastikan daftar tampil. Langkah 25 (mengosongkan teks yang diketik) bukan langkah TC dan mengasumsikan teks yang diketik tanpa memilih opsi dapat dikosongkan.
  - TC-GS-HHR-481 dan TC-GS-HHR-71 menguji state kebalikan satu sama lain (`Device Name` kosong vs `Brand` kosong); spec mengerjakannya berurutan pada satu popup dan mengosongkan `Brand` pada langkah 31 sebagai pengganti prasyarat TC-GS-HHR-71 ("`Brand` dan `SKU` kosong"). Bila mengosongkan `Brand` tidak mengembalikan state awal, QA perlu menyatakan caranya.
  - TC-GS-HHR-74 menyebut pesan `Max. 120 characters` pada 121 karakter, padahal combobox dapat saja menolak karakter ke-121 pada input; spec mengikuti TC (langkah 42 dan 45) dan membutuhkan input yang menerima 121 karakter.
  - Brand `Chainway` pada langkah 22, 35, dan 85 adalah nilai katalog yang sudah ada; TC tidak menyatakan apakah mengetik `Chainway` tanpa memilih opsi `Chainway` membuat Brand baru. Cleanup Brand tidak dibutuhkan bila tidak membuat nilai baru.
