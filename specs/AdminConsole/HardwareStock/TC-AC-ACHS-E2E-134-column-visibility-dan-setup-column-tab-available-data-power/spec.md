---
id: TC-AC-ACHS-E2E-134-column-visibility-dan-setup-column-tab-available-data-power
title: "Column Visibility dan Setup Column Stock Detail Tab Available: Screening Overlay dan Popup, Kelas Data dan Power (Uncheck, Drag, Pin)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-293
  - TC-AC-ACHS-294
  - TC-AC-ACHS-295
  - TC-AC-ACHS-296
  - TC-AC-ACHS-297
  - TC-AC-ACHS-298
  - TC-AC-ACHS-299
  - TC-AC-ACHS-300
coverage:
  web: automated
---

# Column Visibility dan Setup Column Stock Detail Tab Available: Screening Overlay dan Popup, Kelas Data dan Power (Uncheck, Drag, Pin)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Stock List; flag halaman Stock Detail disetel dengan cara yang sama (disediakan tim FE; lihat `suite.md`).
- Data Pre-setup (read-only, tidak diubah spec): SKU `Fixture.hardwareStock.p16.a[4].sku` (Long Range) dengan 18 unit Available dan 1 unit Waiting for Approval (#17, Tabel E: `Fixture.hardwareStock.p17.e[10].deviceName` sampai `Fixture.hardwareStock.p17.e[28].deviceName`; Tab Available 19 baris) dan General Settings #15 (Date Format `DD MMM YYYY`, Time Format 24-hour `HH:mm`). Tidak ada Data Dinamis.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | SKU baris 4 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 4 Tabel A (#16): Handheld Reader Long Range, 18 Available dan 7 In Use (#17, #18) | `Fixture.hardwareStock.p16.a[4].sku` |
  | Device Name unit 10 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 10, Tabel E (#17) | `Fixture.hardwareStock.p17.e[10].deviceName` |
  | Device Name unit 28 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 28, Tabel E (#17) | `Fixture.hardwareStock.p17.e[28].deviceName` |
- Setup Column: preferensi kolom disimpan di browser; hook suite `after` menghapusnya (bukan `[Reset to Default]`; kemampuan disediakan tim FE, lihat `suite.md`).
- Urutan kolom default Tab Available: `Device Name | Serial Number | Status | Registered At | Registered By | Min Power | Max Power | Current Power`.
- Data uji TC-AC-ACHS-295 (kelas data; kolom yang di-uncheck dan di-check kembali pada popup):

  | No | Kolom |
  |---|---|
  | 1 | `Device Name` |
  | 2 | `Serial Number` |
  | 3 | `Status` |
  | 4 | `Registered At` |
  | 5 | `Registered By` |

- Data uji TC-AC-ACHS-296 (drag ke posisi paling kiri pada popup; baris terakhir `Device Name` adalah kolom yang disimpan):

  | No | Kolom |
  |---|---|
  | 1 | `Serial Number` |
  | 2 | `Status` |
  | 3 | `Registered At` |
  | 4 | `Registered By` |
  | 5 | `Device Name` |

- Data uji TC-AC-ACHS-298 (kelas power; kolom yang di-uncheck dan di-check kembali pada popup):

  | No | Kolom |
  |---|---|
  | 1 | `Min Power` |
  | 2 | `Max Power` |
  | 3 | `Current Power` |

- Data uji TC-AC-ACHS-299 (drag ke posisi paling kiri pada popup; baris terakhir `Min Power` adalah kolom yang disimpan):

  | No | Kolom |
  |---|---|
  | 1 | `Max Power` |
  | 2 | `Current Power` |
  | 3 | `Min Power` |

- Pilihan spec: TC-AC-ACHS-296 dan TC-AC-ACHS-299 hanya menulis "diulang dengan posisi berbeda"; spec memindahkan tiap anggota ke posisi paling kiri. TC-AC-ACHS-297 dan TC-AC-ACHS-300 hanya merinci pin `Device Name` dan `Min Power`. Pemulihan antar-TC memakai `[Reset to Default]` lalu `[Save]` (aksi sisi klien).
- Kemampuan teknis (disediakan tim FE): drag and drop baris kolom di popup Setup Column; viewport dipersempit sehingga tabel dapat digulir horizontal (TC tidak menyebut lebar viewport); muat ulang halaman (F5) pada konteks browser yang sama; menghapus preferensi kolom di browser.
- State global yang diubah: preferensi kolom Tab Available di browser; dipulihkan lewat `[Reset to Default]` dan `[Save]` di akhir tiap TC yang menyimpan, dan hook suite `after` menghapusnya (didaftarkan di `suite.md`).
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Pastikan Tab Available aktif

### TC-AC-ACHS-293: Screening overlay Column Visibility

3. Arahkan kursor ke header kolom Actions `(⋯)`
4. Verifikasi tooltip `Column Visibility`
5. Klik header kolom Actions `(⋯)`
6. Verifikasi overlay memuat kolom Device Name, Serial Number, Status, Registered At, Registered By, Min Power, Max Power, Current Power
7. Verifikasi setiap kolom pada overlay memiliki checkbox checked dan enabled (Hideable)
8. Verifikasi setiap kolom pada overlay memiliki drag handle
9. Verifikasi item `Setup Column...` tampil di bagian bawah overlay
10. Tutup overlay Column Visibility

### TC-AC-ACHS-294: Screening popup Setup Column

11. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
12. Verifikasi header popup memuat Title `Setup Column`
13. Verifikasi deskripsi header `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
14. Verifikasi tombol close `[✕]` tampil di header
15. Verifikasi body memuat daftar kolom Device Name, Serial Number, Status, Registered At, Registered By, Min Power, Max Power, Current Power
16. Verifikasi setiap kolom pada body memiliki checkbox checked (Hideable)
17. Verifikasi setiap kolom pada body memiliki drag handle
18. Verifikasi setiap kolom pada body memiliki icon Pin
19. Verifikasi Live Preview urutan header tampil
20. Verifikasi footer memuat `[Reset to Default]` dan `[Save]` rata kanan
21. Verifikasi footer tidak memuat `[Cancel]`
22. Klik `[✕]` untuk menutup popup

### TC-AC-ACHS-295: Setup Column kelas data, uncheck dan check, Save, persist F5

23. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
24. Untuk setiap baris tabel Data uji TC-AC-ACHS-295 (langkah 24 sampai 27): hilangkan centang kolom di popup
25. Verifikasi kolom hilang dari Live Preview
26. Ceklis kembali kolom di popup
27. Verifikasi kolom muncul kembali di Live Preview
28. Hilangkan centang `Device Name`, klik `[Save]`
29. Verifikasi kolom `Device Name` tidak tampil di tabel
30. Verifikasi kolom `Serial Number` tampil di tabel
31. Muat ulang halaman (F5)
32. Verifikasi kolom `Serial Number` tampil di tabel
33. Verifikasi kolom `Device Name` tetap tidak tampil
34. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`

### TC-AC-ACHS-296: Setup Column kelas data, drag reorder, Save, persist F5

35. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
36. Untuk setiap baris tabel Data uji TC-AC-ACHS-296 (langkah 36 sampai 37): drag kolom ke posisi paling kiri pada popup
37. Verifikasi Live Preview menampilkan kolom di posisi pertama
38. Klik `[Save]`
39. Verifikasi tabel menampilkan `Device Name` di posisi pertama
40. Muat ulang halaman (F5)
41. Verifikasi tabel tetap menampilkan `Device Name` di posisi pertama
42. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`

### TC-AC-ACHS-297: Setup Column kelas data, pin dan unpin

43. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
44. Klik icon Pin pada `Device Name`, klik `[Save]`
45. Gulir tabel secara horizontal
46. Verifikasi kolom `Device Name` membeku di sisi kiri saat tabel digulir horizontal
47. Muat ulang halaman (F5)
48. Gulir tabel secara horizontal
49. Verifikasi kolom `Device Name` tetap membeku di sisi kiri setelah F5
50. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
51. Klik icon Pin pada `Device Name` (unpin), klik `[Save]`
52. Gulir tabel secara horizontal
53. Verifikasi kolom `Device Name` ikut bergeser saat tabel digulir horizontal
54. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`

### TC-AC-ACHS-298: Setup Column kelas power, uncheck dan check, Save, persist F5

55. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
56. Untuk setiap baris tabel Data uji TC-AC-ACHS-298 (langkah 56 sampai 59): hilangkan centang kolom di popup
57. Verifikasi kolom hilang dari Live Preview
58. Ceklis kembali kolom di popup
59. Verifikasi kolom muncul kembali di Live Preview
60. Hilangkan centang `Min Power`, klik `[Save]`
61. Verifikasi kolom `Min Power` tidak tampil di tabel
62. Verifikasi kolom `Max Power` tampil di tabel
63. Muat ulang halaman (F5)
64. Verifikasi kolom `Max Power` tampil di tabel
65. Verifikasi kolom `Min Power` tetap tidak tampil
66. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`

### TC-AC-ACHS-299: Setup Column kelas power, drag reorder, Save, persist F5

67. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
68. Untuk setiap baris tabel Data uji TC-AC-ACHS-299 (langkah 68 sampai 69): drag kolom ke posisi paling kiri pada popup
69. Verifikasi Live Preview menampilkan kolom di posisi pertama
70. Klik `[Save]`
71. Verifikasi tabel menampilkan `Min Power` di posisi pertama
72. Muat ulang halaman (F5)
73. Verifikasi tabel tetap menampilkan `Min Power` di posisi pertama
74. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`

### TC-AC-ACHS-300: Setup Column kelas power, pin dan unpin

75. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
76. Klik icon Pin pada `Min Power`, klik `[Save]`
77. Gulir tabel secara horizontal
78. Verifikasi kolom `Min Power` membeku di sisi kiri saat tabel digulir horizontal
79. Muat ulang halaman (F5)
80. Gulir tabel secara horizontal
81. Verifikasi kolom `Min Power` tetap membeku di sisi kiri setelah F5
82. Klik header kolom Actions `(⋯)`, klik `Setup Column...`
83. Klik icon Pin pada `Min Power` (unpin), klik `[Save]`
84. Gulir tabel secara horizontal
85. Verifikasi kolom `Min Power` ikut bergeser saat tabel digulir horizontal
86. Klik header kolom Actions `(⋯)`, klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`


## Notes

- Sumber TC: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md`. (bagian 4b, Stock Detail Tab Available). Seluruh TC sumber spec ini dikerjakan di sini.
- Langkah 24 sampai 27 (lima iterasi), 36 sampai 37 (lima), 56 sampai 59 (tiga), dan 68 sampai 69 (tiga) berulang untuk setiap baris tabel Data uji (bagian 8b butir 7).
- Langkah penghubung (aksi tanpa `Verifikasi`): "Pastikan Tab Available aktif", penutupan overlay dan popup, serta pemulihan susunan kolom lewat `[Reset to Default]` lalu `[Save]` di akhir tiap TC yang menyimpan (`[Save]` Setup Column adalah aksi sisi klien sehingga tanpa langkah "Tunggu aksi selesai"). Verifikasi kolom lain tampil sebelum asersi absence kolom adalah anchor positif (bagian 8b butir 2).
- Spec memiliki 86 langkah nominal dan 122 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Column Visibility dan Setup Column Tab Available pada akun yang sama tanpa seeding), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari empat perulangan per kolom data tanpa langkah bersyarat.
- Temuan untuk QA:
  - TC, PRD, dan LLD yang dibaca tidak menyebut apakah halaman Stock Detail punya flag Guided Tooltip sendiri; spec menyetel flag halaman Stock Detail seperti flag Stock List dengan kemampuan yang disediakan tim FE.
  - TC-AC-ACHS-296 dan TC-AC-ACHS-299 tidak menyebut posisi tujuan anggota selain posisi paling kiri ("diulang dengan posisi berbeda"); TC-AC-ACHS-297 dan TC-AC-ACHS-300 hanya merinci pin `Device Name` dan `Min Power` walau Data Uji memuat semua anggota. Spec mengikuti rincian TC.
  - TC-AC-ACHS-297 dan TC-AC-ACHS-300 (gulir horizontal) tidak menyebut lebar viewport yang membuat tabel dapat digulir; dicatat sebagai kemampuan yang disediakan tim FE.
  - TC-AC-ACHS-295 dan TC-AC-ACHS-298 menyebut penyimpanan di `localStorage`; spec tidak menyebut endpoint atau mekanisme penyimpanan (S-13).
