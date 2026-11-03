---
id: TC-AC-ACHS-E2E-164-column-visibility-dan-setup-column-tab-in-use-data-power
title: "Column Visibility dan Setup Column Tab In Use Kelas Data dan Power"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-349
  - TC-AC-ACHS-350
  - TC-AC-ACHS-351
  - TC-AC-ACHS-352
  - TC-AC-ACHS-353
  - TC-AC-ACHS-354
  - TC-AC-ACHS-355
  - TC-AC-ACHS-356
coverage:
  web: automated
---

# Column Visibility dan Setup Column Tab In Use Kelas Data dan Power

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; tanpa intercept).
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email `Fixture.hardwareStock.account.p01.totalControl.email`, nama tampil `Fixture.hardwareStock.account.p01.totalControl.fullName`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List disetel true di hook `before` suite dan dipulihkan di `after` (lihat suite.md). Suite serial (`parallel: false`).
- Data Pre-setup (hanya dibaca): SKU `Fixture.hardwareStock.p18.sku` (Long Range) dengan 7 unit In Use (Pre-setup #18, Tabel F TC; nilai sel tidak diasersi di spec ini); tabel menampilkan 10 kolom default: Device Name, Serial Number, Client, Status, Registered At, Registered By, Activated At, Min Power, Max Power, Current Power.
- State global browser: spec ini menyimpan konfigurasi kolom Tab In Use (Setup Column, disimpan di `localStorage`). Antar blok TC konfigurasi dipulihkan lewat `[Reset to Default]` lalu `[Save]`; hook `after` suite menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE). Preferensi kolom seluruh tabel modul berada pada kondisi default saat spec dimulai.
- Kemampuan teknis (disediakan tim FE): drag and drop baris kolom di popup Setup Column; scroll horizontal tabel; penghapusan preferensi kolom di browser.
- Anggota yang diulang (Setup Column):
  - Kelas data (TC-351, 352, 353): Device Name, Serial Number, Client, Status, Registered At, Registered By, Activated At.
  - Kelas power (TC-354, 355, 356): Min Power, Max Power, Current Power.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Nama tampil akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.fullName` |
  | SKU Long Range In Use | #18 SKU RFD40 (sama dengan Tabel A baris 4) | kode SKU Handheld Reader Long Range dengan 7 unit In Use (#16, #18) | `Fixture.hardwareStock.p18.sku` |

## Test Steps

### Screening overlay Column Visibility (TC-AC-ACHS-349)

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p18.sku` di Stock List
2. Klik Tab `In Use`
3. Hover header kolom Actions `(⋯)`
4. Verifikasi tooltip `Column Visibility`
5. Klik header kolom Actions `(⋯)`
6. Verifikasi overlay memuat kolom Device Name, Serial Number, Client, Status, Registered At, Registered By, Activated At, Min Power, Max Power, Current Power dengan checkbox berstatus checked dan enabled (Hideable)
7. Verifikasi tiap kolom pada overlay punya drag handle
8. Verifikasi item `Setup Column...` di bagian bawah overlay

### Screening popup Setup Column (TC-AC-ACHS-350)

9. Klik `Setup Column...`
10. Verifikasi header popup: Title `Setup Column` dan deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
11. Verifikasi tombol close `[✕]` di header popup
12. Verifikasi body memuat daftar kolom Device Name, Serial Number, Client, Status, Registered At, Registered By, Activated At, Min Power, Max Power, Current Power dengan checkbox checked (Hideable)
13. Verifikasi tiap kolom punya drag handle
14. Verifikasi tiap kolom punya icon Pin
15. Verifikasi Live Preview urutan header
16. Verifikasi footer: `[Reset to Default]` dan `[Save]` rata kanan
17. Verifikasi tidak ada `[Cancel]` di footer
18. Klik `[✕]` untuk menutup popup

### Kelas data: uncheck dan check, Save, persist F5 (TC-AC-ACHS-351)

19. Buka popup Setup Column
20. Untuk setiap anggota kelas data (langkah 21 sampai 24): lakukan langkah berikut
21. Uncheck anggota
22. Verifikasi anggota hilang dari Live Preview
23. Check kembali anggota
24. Verifikasi anggota muncul kembali di Live Preview
25. Uncheck Device Name, klik `[Save]`
26. Verifikasi kolom Device Name tidak tampil di tabel
27. Muat ulang halaman (F5)
28. Verifikasi tabel Tab In Use tampil dengan kolom Serial Number
29. Verifikasi kolom Device Name tetap tidak tampil (tersimpan di localStorage)
30. Pulihkan konfigurasi: buka popup Setup Column, klik `[Reset to Default]`, klik `[Save]`

### Kelas data: drag reorder, Save, persist F5 (TC-AC-ACHS-352)

31. Untuk setiap anggota kelas data (langkah 32 sampai 38): lakukan langkah berikut
32. Buka popup Setup Column
33. Drag kolom anggota ke posisi paling kiri
34. Verifikasi Live Preview menampilkan anggota di posisi pertama
35. Klik `[Save]`
36. Verifikasi tabel menampilkan anggota di posisi pertama
37. Muat ulang halaman (F5)
38. Verifikasi urutan tetap, anggota di posisi pertama
39. Pulihkan konfigurasi: buka popup Setup Column, klik `[Reset to Default]`, klik `[Save]`

### Kelas data: pin dan unpin (TC-AC-ACHS-353)

40. Untuk setiap anggota kelas data (langkah 41 sampai 50): lakukan langkah berikut
41. Buka popup Setup Column
42. Klik icon Pin pada anggota
43. Klik `[Save]`
44. Scroll tabel horizontal
45. Verifikasi anggota membeku di kiri saat scroll horizontal
46. Muat ulang halaman (F5)
47. Verifikasi anggota tetap membeku di kiri setelah F5
48. Buka popup Setup Column, klik Pin pada anggota yang sama (unpin), klik `[Save]`
49. Scroll tabel horizontal
50. Verifikasi anggota ikut bergeser saat scroll

### Kelas power: uncheck dan check, Save, persist F5 (TC-AC-ACHS-354)

51. Buka popup Setup Column
52. Untuk setiap anggota kelas power (langkah 53 sampai 56): lakukan langkah berikut
53. Uncheck anggota
54. Verifikasi anggota hilang dari Live Preview
55. Check kembali anggota
56. Verifikasi anggota muncul kembali di Live Preview
57. Uncheck Min Power, klik `[Save]`
58. Verifikasi kolom Min Power tidak tampil di tabel
59. Muat ulang halaman (F5)
60. Verifikasi tabel Tab In Use tampil dengan kolom Serial Number
61. Verifikasi kolom Min Power tetap tidak tampil (tersimpan di localStorage)
62. Pulihkan konfigurasi: buka popup Setup Column, klik `[Reset to Default]`, klik `[Save]`

### Kelas power: drag reorder, Save, persist F5 (TC-AC-ACHS-355)

63. Untuk setiap anggota kelas power (langkah 64 sampai 70): lakukan langkah berikut
64. Buka popup Setup Column
65. Drag kolom anggota ke posisi paling kiri
66. Verifikasi Live Preview menampilkan anggota di posisi pertama
67. Klik `[Save]`
68. Verifikasi tabel menampilkan anggota di posisi pertama
69. Muat ulang halaman (F5)
70. Verifikasi urutan tetap, anggota di posisi pertama
71. Pulihkan konfigurasi: buka popup Setup Column, klik `[Reset to Default]`, klik `[Save]`

### Kelas power: pin dan unpin (TC-AC-ACHS-356)

72. Untuk setiap anggota kelas power (langkah 73 sampai 82): lakukan langkah berikut
73. Buka popup Setup Column
74. Klik icon Pin pada anggota
75. Klik `[Save]`
76. Scroll tabel horizontal
77. Verifikasi anggota membeku di kiri saat scroll horizontal
78. Muat ulang halaman (F5)
79. Verifikasi anggota tetap membeku di kiri setelah F5
80. Buka popup Setup Column, klik Pin pada anggota yang sama (unpin), klik `[Save]`
81. Scroll tabel horizontal
82. Verifikasi anggota ikut bergeser saat scroll

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-349 sampai 356). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 18 (tutup popup) dan langkah 30, 39, 62, 71 (pulihkan konfigurasi kolom, S-09). Langkah 28 dan 60 memuat `Verifikasi` tabel Tab In Use termuat sebagai anchor positif untuk asersi absence kolom sesudah F5 (bagian 8b butir 2, R-21).
- Idiom ulang "Untuk setiap anggota": isi iterasi langkah 21 sampai 24, 32 sampai 38, 41 sampai 50, 53 sampai 56, 64 sampai 70, 73 sampai 82; tiap iterasi punya `Verifikasi` per klausa; parameter anggota di Prerequisites. Langkah 39, 71 memulihkan konfigurasi sesudah iterasi terakhir; iterasi berikutnya dalam blok yang sama mengandalkan konfigurasi dari iterasi sebelumnya yang dipulihkan oleh langkah Reset pada akhir blok (anggota drag dan pin menimpa konfigurasi sebelumnya karena `[Save]` menyimpan susunan baru; unpin di langkah 48 dan 80 mengembalikan pin).
- Spec melewati sekitar 35 langkah dengan ekspansi (7 anggota dikali blok drag dan pin): alasan, semua blok satu surface (Setup Column Tab In Use) dan satu dataset; tiap blok memulihkan konfigurasi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; topik satu dataset dipertahankan satu spec (prinsip 1).
- Nilai Pre-setup tidak ditulis literal; dirujuk lewat nomor item Pre-setup (#18, Tabel F) dan kunci fixture, nilai dibaca penulis script dari tabel TC (R-06); tidak ada pengecualian S-12 dipakai. Teks UI asli (label kolom, placeholder, tooltip, empty state) tetap ditulis verbatim.
- Temuan untuk QA:
  - TC-352 dan TC-355 menyebut "Drag kolom Device Name ke posisi paling kiri (anggota lain ... diulang dengan posisi berbeda)"; Device Name sudah di posisi pertama pada urutan default, sehingga asersi "posisi pertama" untuk anggota itu tidak membuktikan reorder. Spec mengulang tiap anggota ke posisi paling kiri sesuai TC.
  - TC-353 dan TC-356 Expected a memuat "tetap setelah F5" padahal langkah TC tidak memuat F5; spec menambah langkah F5 (langkah 46 dan 78) dari Expected.
  - TC-351 sampai TC-356 tidak menyebut halaman yang tampil sesudah F5; spec mengasumsikan halaman Stock Detail Tab In Use tetap tampil (diverifikasi lewat kolom Serial Number tampil di langkah 28 dan 60).
