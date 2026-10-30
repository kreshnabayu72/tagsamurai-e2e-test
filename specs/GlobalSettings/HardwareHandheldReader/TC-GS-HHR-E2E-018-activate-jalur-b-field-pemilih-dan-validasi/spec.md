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
- Suite serial (`parallel: false`): spec membuat satu reader Self-Purchased di Client A (langkah 82), memakai simulator USB bersama, dan membaca katalog Device Name Admin Console.
- Aktor: Total Control Sari Dewi (Client A, toggle `Allow Self-Purchased Device Activation` aktif) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_gs-handheld-reader` mengikuti hook suite (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji `tc-hardware-handheld-reader.md`):
  - Client A plan Growth, Seed Reader A DD-01 s.d. DD-10 (`Short Range` `5 of 8`, `Long Range` `5 of 6`); DD-05 (`Chainway C72 - 1`) sudah ada sehingga reader baru `Chainway C72` bernomor `- 2`.
  - Serial Jalur B (tidak ada di stok Principal): `SN-HHR-00302` (Current Power 20 dBm via driver) dan `SN-HHR-00303` (reader tidak mengembalikan nilai daya).
  - Katalog Device Name Admin Console, dibaca Client A read-only: DN-01 `Chainway C72`, DN-02 `Honeywell CK65`, DN-03 `Unitech EA520`, DN-04 `International Handheld Terminals Ltd Ultra-Rugged Series 7000 Pro Max`, DN-05 `Handheld Terminal` (Category Hardware > Handheld Reader dan turunannya, termasuk UHF Handheld); DN-06 `Gate Antenna` (Hardware > Smart Fixed Reader > Antenna) dan DN-07 `Access Card Reader` (TAG > NFC) di luar konteks `Handheld Reader`.
  - Pemilih `SKU` Jalur B memuat `SKU-HHR-01` sampai `SKU-HHR-04`; `SKU-HHR-03` berisi Brand `Chainway` dan Model/Type `C66`.
  - State awal dipulihkan oleh fixture backend sebelum spec (Catatan TC; mekanisme disediakan tim FE/BE).
- Efek spec: langkah 82 membuat reader `Chainway C72 - 2` (Short Range, `SKU-HHR-03`, Self-Purchased) di Client A; kuota `Short Range` menjadi `6 of 8`. Hook `after` memulihkan Seed Reader A dan kuota Client A lewat reset fixture backend (disediakan tim FE/BE). Brand dan Model/Type yang diketik adalah nilai katalog yang sudah ada; tidak ada nilai baru yang dibuat.
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
20. Verifikasi daftar tidak menawarkan opsi `Add 'Perangkat Tidak Terdaftar'`
21. Isi `Brand` dengan `Chainway`
22. Verifikasi `Device Name` tetap belum terpilih
23. Verifikasi `[Submit]` tetap disabled
24. Kosongkan teks yang diketik pada field `Device Name`

### TC-GS-HHR-481: Submit disabled selama Device Name belum dipilih

25. Isi `Model/Type` dengan `C72` (`Brand` sudah `Chainway`, `Device Name` kosong)
26. Verifikasi `[Submit]` disabled
27. Verifikasi tidak ada tooltip pada `[Submit]`
28. Pilih `Chainway C72` pada `Device Name`
29. Verifikasi `[Submit]` enabled

### TC-GS-HHR-71: Submit disabled selama Brand kosong dan SKU belum dipilih

30. Kosongkan isi `Brand` (`SKU` tetap kosong; `Device Name` `Chainway C72` dan `Model/Type` `C72` terisi)
31. Verifikasi `[Submit]` disabled
32. Verifikasi tanda `*` pada `Brand` tampil selama `SKU` kosong
33. Verifikasi tidak ada tooltip pada `[Submit]`
34. Isi `Brand` dengan `Chainway`
35. Verifikasi `[Submit]` enabled

### TC-GS-HHR-74: Batas 120 karakter Brand dan Model/Type

36. Ganti isi `Brand` dengan 120 karakter `A`
37. Ganti isi `Model/Type` dengan 120 karakter `B`
38. Verifikasi tidak ada pesan inline pada `Brand` dan `Model/Type`
39. Verifikasi `[Submit]` enabled
40. Tambah satu karakter pada `Brand` (121 karakter)
41. Verifikasi pesan inline `Max. 120 characters` pada `Brand`
42. Verifikasi `[Submit]` disabled
43. Kembalikan `Brand` ke 120 karakter, lalu tambah satu karakter pada `Model/Type` (121 karakter)
44. Verifikasi pesan inline `Max. 120 characters` pada `Model/Type`
45. Verifikasi `[Submit]` disabled

### TC-GS-HHR-479 (lanjutan): Pencarian dan pemilihan Device Name

46. Ganti isi field `Device Name` dengan `Unitech`
47. Verifikasi daftar opsi dipersempit dibanding daftar penuh pada langkah 17
48. Verifikasi daftar opsi memuat `Unitech EA520`
49. Pilih opsi `Unitech EA520`
50. Verifikasi field `Device Name` menampilkan `Unitech EA520`
51. Klik `[✕]` di header popup, lalu klik `[Cancel Activation]` pada dialog

### Popup 2: Long Range, reader SN-HHR-00303

52. Klik `[+ Activate Reader]`
53. Klik `Long Range` pada Overlay `Select Range Type`
54. Sambungkan reader dengan Serial Number `SN-HHR-00303` (di luar stok Principal, tanpa nilai daya) lewat simulator reader USB
55. Klik `[Sync]`

### TC-GS-HHR-445: Reader Power tidak terbaca dari reader, slider memakai default 30 dBm

56. Verifikasi `Serial Number` read-only terisi `SN-HHR-00303`
57. Verifikasi label `Official` tidak tampil
58. Verifikasi slider `Reader Power` terisi nilai awal `30 dBm`
59. Verifikasi slider `Reader Power` dapat digeser
60. Klik `[✕]` di header popup, lalu klik `[Cancel Activation]` pada dialog

### Popup 3: Short Range, reader SN-HHR-00302

61. Klik `[+ Activate Reader]`
62. Klik `Short Range` pada Overlay `Select Range Type`
63. Sambungkan reader dengan Serial Number `SN-HHR-00302` lewat simulator reader USB
64. Klik `[Sync]`

### TC-GS-HHR-484: Memilih SKU opsional mengisi Brand dan Model/Type

65. Pilih `Chainway C72` pada `Device Name`
66. Pilih `SKU-HHR-03` pada `SKU`
67. Verifikasi `Device Name` terisi `Chainway C72`
68. Verifikasi `Brand` terisi `Chainway`
69. Verifikasi `Model/Type` terisi `C66`
70. Verifikasi tanda `*` pada `Brand` hilang
71. Verifikasi `Device Name`, `Brand`, dan `Model/Type` terkunci (tidak dapat diedit) selama `SKU` terisi
72. Verifikasi `[Submit]` enabled tanpa mengisi `Brand` secara manual

### TC-GS-HHR-485: Mengosongkan SKU membuat Brand wajib kembali

73. Kosongkan `SKU`
74. Verifikasi nilai `Device Name`, `Brand`, dan `Model/Type` hasil autofill dikosongkan
75. Verifikasi `Device Name`, `Brand`, dan `Model/Type` dapat diedit kembali
76. Verifikasi tanda `*` pada `Brand` tampil kembali
77. Verifikasi `[Submit]` disabled selama `Device Name` atau `Brand` kosong
78. Pilih `Chainway C72` pada `Device Name`
79. Isi `Brand` dengan `Chainway`
80. Verifikasi `[Submit]` enabled

### TC-GS-HHR-484 (lanjutan): Submit dengan SKU dan Popup Detail

81. Pilih `SKU-HHR-03` pada `SKU`
82. Klik `[Submit]`
83. Verifikasi muncul toast sukses: "Success, Chainway C72 - 2 has been activated."
84. Ketik Search `Chainway C72 - 2`, tekan Enter
85. Klik `Device Name` baris baru `Chainway C72 - 2` untuk membuka Popup Detail
86. Verifikasi Popup Detail baris baru menampilkan `SKU` `SKU-HHR-03`
87. Verifikasi Popup Detail baris baru menampilkan `Brand` `Chainway`
88. Verifikasi Popup Detail baris baru menampilkan `Model/Type` `C66`
89. Verifikasi Popup Detail baris baru menampilkan `Source` `Self-Purchased`

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Kelas harness: eksternal (d), simulator reader USB; seluruh TC berlabel Manual Only (b). Satu topik (field dan validasi popup Activate Jalur B), satu akun, satu harness. Submit sukses hanya satu (TC-GS-HHR-484) dan berada di akhir; submit sukses lain berada di spec 019.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan menyimpang dari urutan nomor TC untuk memakai satu popup per reader tanpa submit (prinsip 13, halaman yang sama dipakai berulang) dan menjaga state field: TC-GS-HHR-479 dipecah dua bagian (langkah 16 sampai 18 pada field `Device Name` kosong; langkah 46 sampai 50 sesudah state field dipakai TC-GS-HHR-74) karena pemilihan `Device Name` pada langkah 49 akan mengisi field yang dibutuhkan TC-GS-HHR-480 dalam keadaan kosong; TC-GS-HHR-480, TC-GS-HHR-481, TC-GS-HHR-71, dan TC-GS-HHR-74 berurutan menurut state field (tidak terpilih, `Brand`/`Model/Type` terisi, `Brand` dikosongkan, batas panjang). TC-GS-HHR-485 dikerjakan sebelum langkah Submit TC-GS-HHR-484 (langkah 81 sampai 82) agar asersi "`[Submit]` enabled tanpa mengisi `Brand` secara manual" (langkah 72) belum tercampur isian manual; langkah 81 memilih ulang `SKU-HHR-03` sehingga autofill menimpa isian manual langkah 78 dan 79.
- Verifikasi langkah 7 memenuhi Expected b TC-GS-HHR-69 dan Expected a pertama TC-GS-HHR-479 (klausa identik: tanda wajib, placeholder, kosong); langkah 17 dan 18 memenuhi Expected b dan c TC-GS-HHR-479.
- Spec melewati sekitar 35 langkah (89 langkah). Alasan: 52 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01); tiga popup memakai prefix `Klik [+ Activate Reader]` sampai `Klik [Sync]`; semua blok satu kelas harness (simulator USB), satu topik, dan hanya langkah 82 yang menyimpan data, di akhir spec, sehingga kegagalan lunak satu blok tidak menutup makna blok lain.
- Langkah penghubung (tanpa `Verifikasi`): langkah 3, 54, 63 (menyiapkan reader di simulator); langkah 24 (mengosongkan teks `Device Name` agar field benar-benar kosong untuk TC-GS-HHR-481); langkah 51 dan 60 (menutup popup yang berisi hasil Sync); langkah 84 (Search untuk menemukan baris target).
- Asersi absence: langkah 6, 18, 20, 57 didahului `Verifikasi` pada surface yang sama (langkah 5; langkah 17; daftar opsi yang tampil pada langkah 17; langkah 56) sebagai anchor positif.
- Temuan untuk QA:
  - Mekanisme simulasi reader USB, driver lokal, dan nilai Current Power yang dikembalikan reader tidak didefinisikan di TC, PRD, atau LLD; spec mencatat kebutuhan di Prerequisites tanpa mengarang endpoint atau perintah simulator.
  - TC-GS-HHR-480 Expected b ("`Device Name` tetap belum terpilih") dan langkah 24 mengasumsikan teks yang diketik tanpa memilih opsi tidak menjadi nilai terpilih dan dapat dikosongkan; TC tidak menyatakannya.
  - TC-GS-HHR-481 dan TC-GS-HHR-71 menguji state kebalikan satu sama lain (`Device Name` kosong vs `Brand` kosong); spec mengerjakannya berurutan pada satu popup dan mengosongkan `Brand` pada langkah 30 sebagai pengganti prasyarat TC-GS-HHR-71 ("`Brand` dan `SKU` kosong"). Bila mengosongkan `Brand` tidak mengembalikan state awal, QA perlu menyatakan caranya.
  - TC-GS-HHR-74 menyebut pesan `Max. 120 characters` pada 121 karakter, padahal combobox dapat saja menolak karakter ke-121 pada input; spec mengikuti TC (langkah 41 dan 44) dan membutuhkan input yang menerima 121 karakter.
  - Judul dan isi dialog yang memuat `[Cancel Activation]` (langkah 51, 60) tidak tertulis di TC sumber slice ini; langkah dibuat tanpa `Verifikasi` dialog.
  - TC-GS-HHR-484 Expected a menyebut `Device Name` terisi `Chainway C72` padahal langkah 4 TC memilihnya manual sebelum memilih `SKU`; spec mengasersinya apa adanya (langkah 67).
  - Brand `Chainway` pada langkah 21, 34, dan 79 adalah nilai katalog yang sudah ada; TC tidak menyatakan apakah mengetik `Chainway` tanpa memilih opsi `Chainway` membuat Brand baru. Cleanup Brand tidak dibutuhkan bila tidak membuat nilai baru.
