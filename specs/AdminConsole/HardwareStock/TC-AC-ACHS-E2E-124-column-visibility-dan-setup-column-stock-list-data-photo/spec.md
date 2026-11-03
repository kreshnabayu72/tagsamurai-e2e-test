---
id: TC-AC-ACHS-E2E-124-column-visibility-dan-setup-column-stock-list-data-photo
title: "Column Visibility dan Setup Column Stock List: Screening Overlay dan Popup, Kelas Data dan Photo (Uncheck, Drag, Pin)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-234
  - TC-AC-ACHS-235
  - TC-AC-ACHS-236
  - TC-AC-ACHS-237
  - TC-AC-ACHS-238
  - TC-AC-ACHS-239
  - TC-AC-ACHS-240
  - TC-AC-ACHS-241
coverage:
  web: automated
---

# Column Visibility dan Setup Column Stock List: Screening Overlay dan Popup, Kelas Data dan Photo (Uncheck, Drag, Pin)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Stock List (lihat `suite.md`).
- Data Pre-setup (read-only, tidak diubah spec): #16 Katalog SKU 30 baris Stock List (Tabel A: 8 SKU nama dan 22 SKU `Fixture.hardwareStock.p16.a[9].sku` sampai `Fixture.hardwareStock.p16.a[30].sku`) dan #15 General Settings (Date Format `DD MMM YYYY`, Time Format 24-hour `HH:mm`). Tidak ada Data Dinamis.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | SKU baris padding 01 (Tabel A baris 9) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 01 (#16) | `Fixture.hardwareStock.p16.a[9].sku` |
  | SKU baris padding 22 (Tabel A baris 30) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 22 (#16) | `Fixture.hardwareStock.p16.a[30].sku` |
- Setup Column: preferensi kolom disimpan di browser; hook suite `after` menghapusnya (bukan `[Reset to Default]`; kemampuan disediakan tim FE, lihat `suite.md`).
- Urutan kolom default Stock List: `Photo | Device Name | SKU | Type | Range Type | Brand | Model/Type | Total Registered | Available | In Use | Last Updated`.
- Data uji TC-AC-ACHS-236 (kelas data; kolom yang di-uncheck dan di-check kembali pada popup):

  | No | Kolom |
  |---|---|
  | 1 | `Device Name` |
  | 2 | `SKU` |
  | 3 | `Type` |
  | 4 | `Range Type` |
  | 5 | `Brand` |
  | 6 | `Model/Type` |
  | 7 | `Total Registered` |
  | 8 | `Available` |
  | 9 | `In Use` |
  | 10 | `Last Updated` |

- Data uji TC-AC-ACHS-237 (drag ke posisi paling kiri pada popup; baris terakhir `Device Name` adalah kolom yang disimpan):

  | No | Kolom |
  |---|---|
  | 1 | `SKU` |
  | 2 | `Type` |
  | 3 | `Range Type` |
  | 4 | `Brand` |
  | 5 | `Model/Type` |
  | 6 | `Total Registered` |
  | 7 | `Available` |
  | 8 | `In Use` |
  | 9 | `Last Updated` |
  | 10 | `Device Name` |

- Pilihan spec: TC-AC-ACHS-237 dan TC-AC-ACHS-240 hanya menulis "diulang dengan posisi berbeda" tanpa posisi; spec memindahkan tiap anggota ke posisi paling kiri. Photo sudah berada di posisi pertama pada urutan default, sehingga TC-AC-ACHS-240 lebih dulu memindahkan Photo ke posisi terakhir dan menyimpannya (precondition TC, tidak diasersi) sebelum memindahkannya kembali ke posisi paling kiri. Pemulihan antar-TC memakai `[Reset to Default]` lalu `[Save]` (aksi sisi klien).
- Kemampuan teknis (disediakan tim FE): drag and drop baris kolom di popup Setup Column; hover icon Pin untuk membaca tooltip; viewport dipersempit sehingga tabel dapat digulir horizontal (TC tidak menyebut lebar viewport); muat ulang halaman (F5) pada konteks browser yang sama sehingga preferensi kolom di browser tetap ada; menghapus preferensi kolom di browser.
- State global yang diubah: preferensi kolom Stock List di browser (disimpan di localStorage menurut TC, bukan lewat API). Pemulihan: `[Reset to Default]` lalu `[Save]` di akhir tiap TC yang menyimpan, dan hook suite `after` menghapus preferensi kolom (didaftarkan di `suite.md`).
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACHS-234: Screening overlay Column Visibility

1. Arahkan kursor ke header kolom Actions `(⋯)`
2. Verifikasi tooltip `Column Visibility`
3. Klik header kolom Actions `(⋯)`
4. Verifikasi overlay memuat kolom Photo, Device Name, SKU, Type, Range Type, Brand, Model/Type, Total Registered, Available, In Use, Last Updated
5. Verifikasi setiap kolom pada overlay memiliki checkbox checked dan enabled (Hideable)
6. Verifikasi setiap kolom pada overlay memiliki drag handle
7. Verifikasi item `Setup Column...` tampil di bagian bawah overlay
8. Tutup overlay Column Visibility

### TC-AC-ACHS-235: Screening popup Setup Column

9. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
10. Verifikasi header popup memuat Title `Setup Column`
11. Verifikasi deskripsi header `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
12. Verifikasi tombol close `[✕]` tampil di header
13. Verifikasi body memuat daftar kolom Photo, Device Name, SKU, Type, Range Type, Brand, Model/Type, Total Registered, Available, In Use, Last Updated
14. Verifikasi setiap kolom pada body memiliki checkbox checked (Hideable)
15. Verifikasi setiap kolom pada body memiliki drag handle
16. Verifikasi setiap kolom pada body memiliki icon Pin
17. Verifikasi Live Preview urutan header tampil
18. Verifikasi footer memuat `[Reset to Default]` dan `[Save]` rata kanan
19. Verifikasi footer tidak memuat `[Cancel]`
20. Klik `[✕]` untuk menutup popup

### TC-AC-ACHS-236: Setup Column kelas data, uncheck dan check, Save, persist F5

21. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
22. Untuk setiap baris tabel Data uji TC-AC-ACHS-236 (langkah 22 sampai 25): hilangkan centang kolom di popup
23. Verifikasi kolom hilang dari Live Preview
24. Ceklis kembali kolom di popup
25. Verifikasi kolom muncul kembali di Live Preview
26. Hilangkan centang `Device Name`, klik `[Save]`
27. Verifikasi kolom `Device Name` tidak tampil di tabel
28. Verifikasi kolom `SKU` tampil di tabel
29. Muat ulang halaman (F5)
30. Verifikasi kolom `SKU` tampil di tabel
31. Verifikasi kolom `Device Name` tetap tidak tampil
32. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`

### TC-AC-ACHS-237: Setup Column kelas data, drag reorder, Save, persist F5

33. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
34. Untuk setiap baris tabel Data uji TC-AC-ACHS-237 (langkah 34 sampai 35): drag kolom ke posisi paling kiri pada popup
35. Verifikasi Live Preview menampilkan kolom di posisi pertama
36. Klik `[Save]`
37. Verifikasi tabel menampilkan `Device Name` di posisi pertama
38. Muat ulang halaman (F5)
39. Verifikasi tabel tetap menampilkan `Device Name` di posisi pertama
40. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`

### TC-AC-ACHS-238: Setup Column kelas data, pin dan unpin

41. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
42. Klik icon Pin pada `Device Name`, klik `[Save]`
43. Gulir tabel secara horizontal
44. Verifikasi kolom `Device Name` membeku di sisi kiri saat tabel digulir horizontal
45. Muat ulang halaman (F5)
46. Gulir tabel secara horizontal
47. Verifikasi kolom `Device Name` tetap membeku di sisi kiri setelah F5
48. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
49. Klik icon Pin pada `Device Name` (unpin), klik `[Save]`
50. Gulir tabel secara horizontal
51. Verifikasi kolom `Device Name` ikut bergeser saat tabel digulir horizontal
52. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`

### TC-AC-ACHS-239: Setup Column kelas photo, uncheck dan check, Save, persist F5

53. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
54. Hilangkan centang `Photo`
55. Verifikasi kolom `Photo` hilang dari Live Preview
56. Ceklis kembali `Photo`
57. Verifikasi kolom `Photo` muncul kembali di Live Preview
58. Hilangkan centang `Photo`, klik `[Save]`
59. Verifikasi kolom `Photo` tidak tampil di tabel
60. Verifikasi kolom `Device Name` tampil di tabel
61. Muat ulang halaman (F5)
62. Verifikasi kolom `Device Name` tampil di tabel
63. Verifikasi kolom `Photo` tetap tidak tampil
64. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`

### TC-AC-ACHS-240: Setup Column kelas photo, drag reorder, Save, persist F5

65. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
66. Drag kolom `Photo` ke posisi terakhir pada popup, klik `[Save]`
67. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
68. Drag kolom `Photo` ke posisi paling kiri pada popup
69. Verifikasi Live Preview menampilkan `Photo` di posisi pertama
70. Klik `[Save]`
71. Verifikasi tabel menampilkan `Photo` di posisi pertama
72. Muat ulang halaman (F5)
73. Verifikasi tabel tetap menampilkan `Photo` di posisi pertama
74. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`

### TC-AC-ACHS-241: Setup Column kelas photo, pin dan unpin

75. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
76. Klik icon Pin pada `Photo`, klik `[Save]`
77. Gulir tabel secara horizontal
78. Verifikasi kolom `Photo` membeku di sisi kiri saat tabel digulir horizontal
79. Muat ulang halaman (F5)
80. Gulir tabel secara horizontal
81. Verifikasi kolom `Photo` tetap membeku di sisi kiri setelah F5
82. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
83. Klik icon Pin pada `Photo` (unpin), klik `[Save]`
84. Gulir tabel secara horizontal
85. Verifikasi kolom `Photo` ikut bergeser saat tabel digulir horizontal
86. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`


## Notes

- Sumber TC: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md`. (bagian 4a, Stock List). Seluruh TC sumber spec ini dikerjakan di sini.
- Langkah 22 sampai 25 dan 34 sampai 35 berulang untuk setiap baris tabel Data uji (sepuluh iterasi masing-masing; bagian 8b butir 7).
- Langkah penghubung (aksi tanpa `Verifikasi`): penutupan overlay dan popup, pemulihan susunan kolom lewat `[Reset to Default]` lalu `[Save]` di akhir tiap TC yang menyimpan (`[Save]` Setup Column adalah aksi sisi klien sehingga tanpa langkah "Tunggu aksi selesai"), serta penggeseran `Photo` ke posisi terakhir pada TC-AC-ACHS-240 (precondition TC agar pemindahan ke paling kiri bermakna). Langkah "Verifikasi kolom `SKU` tampil" pada TC-AC-ACHS-236 dan "kolom `Device Name` tampil" pada TC-AC-ACHS-239 adalah anchor positif sebelum asersi absence kolom (bagian 8b butir 2, absence sesudah muat ulang).
- Spec memiliki 86 langkah nominal dan 140 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Column Visibility dan Setup Column Stock List pada akun yang sama tanpa seeding), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari dua perulangan per kolom data tanpa langkah bersyarat.
- Temuan untuk QA:
  - TC-AC-ACHS-237 dan TC-AC-ACHS-240 tidak menyebut posisi tujuan anggota selain posisi paling kiri ("diulang dengan posisi berbeda"); TC-AC-ACHS-238 dan TC-AC-ACHS-241 hanya merinci pin `Device Name` dan `Photo` walau Data Uji memuat semua anggota. Spec mengikuti rincian TC dan memakai pilihan spec yang tertulis di Prerequisites.
  - TC-AC-ACHS-240: kolom Photo sudah berada di posisi pertama pada urutan default sehingga drag ke posisi paling kiri tidak mengubah apa pun tanpa precondition; spec menambah precondition (pemindahan Photo ke posisi terakhir lalu Save).
  - TC-AC-ACHS-238, 241 (gulir horizontal) tidak menyebut lebar viewport yang membuat tabel dapat digulir; dicatat sebagai kemampuan yang disediakan tim FE.
  - TC-AC-ACHS-236, 239 menyebut penyimpanan di `localStorage`; spec tidak menyebut endpoint atau mekanisme penyimpanan (S-13).
