---
id: TC-AC-ACHS-E2E-120-search-stock-list
title: "Search Stock List: Siklus Kotak, Kolom Teks, Badge, dan Angka, Empty State, Kolom Non-Searchable, Visibilitas Kolom, dan Spasi Tepi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-204
  - TC-AC-ACHS-205
  - TC-AC-ACHS-206
  - TC-AC-ACHS-207
  - TC-AC-ACHS-208
  - TC-AC-ACHS-209
  - TC-AC-ACHS-210
  - TC-AC-ACHS-211
coverage:
  web: automated
---

# Search Stock List: Siklus Kotak, Kolom Teks, Badge, dan Angka, Empty State, Kolom Non-Searchable, Visibilitas Kolom, dan Spasi Tepi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Stock List (lihat `suite.md`).
- Data Pre-setup (read-only, tidak diubah spec): #16 Katalog SKU 30 baris Stock List (Tabel A: 8 SKU nama dan 22 SKU `Fixture.hardwareStock.p16.a[9].sku` sampai `Fixture.hardwareStock.p16.a[30].sku`) dan #15 General Settings (Date Format `DD MMM YYYY`, Time Format 24-hour `HH:mm`). Tidak ada Data Dinamis.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Brand baris 1 Tabel A | #16 Katalog SKU (Tabel A) | Brand baris 1 Tabel A (#16): Handheld Reader Short Range, 34 Available dan 16 In Use (#19); Brand yang sama pada baris 3 dan 4 | `Fixture.hardwareStock.p16.a[1].brand` |
  | Last Updated baris 1 Tabel A | #16 Katalog SKU (Tabel A) | Last Updated baris 1 Tabel A (#16), format General Settings #15 | `Fixture.hardwareStock.p16.a[1].lastUpdated` |
  | SKU baris 1 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 1 Tabel A (#16): Handheld Reader Short Range, 34 Available dan 16 In Use (#19) | `Fixture.hardwareStock.p16.a[1].sku` |
  | Device Name baris 3 Tabel A | #16 Katalog SKU (Tabel A) | Device Name baris 3 Tabel A (#16): Smart Fixed Reader, 8 Available (#27) | `Fixture.hardwareStock.p16.a[3].deviceName` |
  | SKU baris 3 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 3 Tabel A (#16): Smart Fixed Reader, 8 Available (#27) | `Fixture.hardwareStock.p16.a[3].sku` |
  | SKU baris 4 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 4 Tabel A (#16): Handheld Reader Long Range, 18 Available dan 7 In Use (#17, #18) | `Fixture.hardwareStock.p16.a[4].sku` |
  | SKU baris 5 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 5 Tabel A (#16): BLE Gateway, 4 Available dan 1 In Use (#27) | `Fixture.hardwareStock.p16.a[5].sku` |
  | SKU baris 7 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 7 Tabel A (#16): BLE Gateway dengan Brand dan Model/Type bernilai panjang | `Fixture.hardwareStock.p16.a[7].sku` |
  | SKU baris 8 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 8 Tabel A (#16): Smart Fixed Reader dengan 120 Available (#24) | `Fixture.hardwareStock.p16.a[8].sku` |
  | SKU baris padding 01 (Tabel A baris 9) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 01 (#16) | `Fixture.hardwareStock.p16.a[9].sku` |
  | SKU baris padding 03 (Tabel A baris 11) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 03 (#16) | `Fixture.hardwareStock.p16.a[11].sku` |
  | SKU baris padding 05 (Tabel A baris 13) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 05 (#16) | `Fixture.hardwareStock.p16.a[13].sku` |
  | SKU baris padding 07 (Tabel A baris 15) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 07 (#16) | `Fixture.hardwareStock.p16.a[15].sku` |
  | SKU baris padding 09 (Tabel A baris 17) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 09 (#16) | `Fixture.hardwareStock.p16.a[17].sku` |
  | SKU baris padding 16 (Tabel A baris 24) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 16 (#16) | `Fixture.hardwareStock.p16.a[24].sku` |
  | SKU baris padding 17 (Tabel A baris 25) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 17 (#16) | `Fixture.hardwareStock.p16.a[25].sku` |
  | SKU baris padding 19 (Tabel A baris 27) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 19 (#16) | `Fixture.hardwareStock.p16.a[27].sku` |
  | SKU baris padding 21 (Tabel A baris 29) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 21 (#16) | `Fixture.hardwareStock.p16.a[29].sku` |
  | SKU baris padding 22 (Tabel A baris 30) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 22 (#16) | `Fixture.hardwareStock.p16.a[30].sku` |
  | Nilai turunan lastUpdatedA1Date | turunan dari `Fixture.hardwareStock.p16.a[1].lastUpdated` | bagian tanggal (tanpa jam) Last Updated baris 1 Tabel A (`10 Jun 2026`) | `Fixture.hardwareStock.derived.lastUpdatedA1Date` |
  | Nilai turunan searchBrandA5 | turunan dari `Fixture.hardwareStock.p16.a[5].brand` | keyword Search: bagian Brand baris 5 Tabel A sebelum tanda titik (`Kontakt`, substring dari nilai Brand; sama dengan keyword TC-AC-ACHS-206) | `Fixture.hardwareStock.derived.searchBrandA5` |
  | Nilai turunan searchModelA7 | turunan dari `Fixture.hardwareStock.p16.a[7].modelType` | keyword Search: satu kata pembeda dari Model/Type baris 7 Tabel A (`Professional`, substring; sama dengan keyword TC-AC-ACHS-206) | `Fixture.hardwareStock.derived.searchModelA7` |
  | Nilai turunan searchSkuPad0 | turunan dari `Fixture.hardwareStock.p16.a[9].sku` | keyword Search: awalan kode SKU baris padding nomor 01 sampai 09 tanpa digit terakhir (`SKU-PAD-0`; 9 baris) | `Fixture.hardwareStock.derived.searchSkuPad0` |
- Data uji TC-AC-ACHS-205 (Search kelas teks; kolom "Keyword huruf kapital" adalah keyword yang sama dalam huruf kapital):

  | No | Kolom | Keyword | Keyword huruf kapital | Hasil |
  |---|---|---|---|---|
  | 1 | Device Name | `Fixture.hardwareStock.p16.a[3].deviceName` | `upper(Fixture.hardwareStock.p16.a[3].deviceName)` | 25 baris; lima teratas `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[29].sku`, `Fixture.hardwareStock.p16.a[27].sku`, `Fixture.hardwareStock.p16.a[25].sku` |
  | 2 | SKU | `Fixture.hardwareStock.derived.searchSkuPad0` | `Fixture.hardwareStock.derived.searchSkuPad0` | 9 baris; lima teratas `Fixture.hardwareStock.p16.a[17].sku`, `Fixture.hardwareStock.p16.a[15].sku`, `Fixture.hardwareStock.p16.a[13].sku`, `Fixture.hardwareStock.p16.a[11].sku`, `Fixture.hardwareStock.p16.a[9].sku` |
  | 3 | Range Type | `Long Range` | `LONG RANGE` | 1 baris: `Fixture.hardwareStock.p16.a[4].sku` |

- Data uji TC-AC-ACHS-206 (Search kelas badge):

  | No | Kolom | Keyword | Keyword huruf kapital | Hasil |
  |---|---|---|---|---|
  | 1 | Type | `BLE Gateway` | `BLE GATEWAY` | 2 baris: `Fixture.hardwareStock.p16.a[7].sku`, `Fixture.hardwareStock.p16.a[5].sku` |
  | 2 | Brand | `Fixture.hardwareStock.derived.searchBrandA5` | `upper(Fixture.hardwareStock.derived.searchBrandA5)` | 1 baris: `Fixture.hardwareStock.p16.a[5].sku` |
  | 3 | Model/Type | `Fixture.hardwareStock.derived.searchModelA7` | `upper(Fixture.hardwareStock.derived.searchModelA7)` | 1 baris: `Fixture.hardwareStock.p16.a[7].sku` |

- Data uji TC-AC-ACHS-207 (Search kelas angka):

  | No | Kolom | Keyword | Hasil |
  |---|---|---|---|
  | 1 | Total Registered | `120` | 1 baris: `Fixture.hardwareStock.p16.a[8].sku` |
  | 2 | Available | `34` | 1 baris: `Fixture.hardwareStock.p16.a[1].sku` |
  | 3 | In Use | `16` | 2 baris: `Fixture.hardwareStock.p16.a[1].sku`, `Fixture.hardwareStock.p16.a[24].sku` |

- Kemampuan teknis (disediakan tim FE): menutup kotak Search lewat `←` untuk mereset tabel.
- State global yang diubah: visibilitas kolom Range Type (langkah 47 sampai 51) dipulihkan di langkah 51. Preferensi kolom di browser dihapus oleh hook suite `after`.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACHS-204: Siklus Search toolbar

1. Arahkan kursor ke icon Search
2. Verifikasi tooltip `Search`
3. Klik icon Search
4. Verifikasi kotak Search melebar
5. Verifikasi kursor fokus di input Search
6. Verifikasi placeholder input Search `Search by device name, SKU, type, range type, brand, model/type, total registered, available, or in use...`
7. Ketik `Fixture.hardwareStock.p16.a[1].brand` di kotak Search tanpa menekan Enter
8. Verifikasi icon `✕` muncul di kotak Search
9. Verifikasi tabel belum tersaring (info `Showing 1–10 of 30 entries`)
10. Tekan Enter
11. Verifikasi tabel menampilkan 3 baris: `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku`
12. Klik `✕` pada kotak Search
13. Verifikasi input Search kosong
14. Verifikasi kotak Search tetap terbuka
15. Verifikasi kursor tetap fokus di input Search
16. Verifikasi tabel masih menampilkan hasil search terakhir (3 baris `Fixture.hardwareStock.p16.a[1].brand`)
17. Tekan Enter pada input yang sudah kosong
18. Verifikasi tabel kembali menampilkan seluruh baris (info `Showing 1–10 of 30 entries`)
19. Ketik Search `Fixture.hardwareStock.p16.a[1].brand`, tekan Enter
20. Klik `←` di kiri toolbar
21. Verifikasi kotak Search menutup menjadi icon Search
22. Verifikasi keyword Search dikosongkan
23. Verifikasi tabel langsung kembali ke seluruh baris tanpa Enter (info `Showing 1–10 of 30 entries`)

### TC-AC-ACHS-205: Search kelas teks

24. Untuk setiap baris tabel Data uji TC-AC-ACHS-205 (langkah 24 sampai 28): ketik Search keyword, tekan Enter
25. Verifikasi jumlah baris dan baris teratas sesuai kolom "Hasil"
26. Ganti isi kotak search dengan keyword huruf kapital, tekan Enter
27. Verifikasi hasil identik dengan hasil keyword semula (jumlah baris dan baris teratas sama)
28. Klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-206: Search kelas badge

29. Untuk setiap baris tabel Data uji TC-AC-ACHS-206 (langkah 29 sampai 33): ketik Search keyword, tekan Enter
30. Verifikasi jumlah baris dan baris sesuai kolom "Hasil"
31. Ganti isi kotak search dengan keyword huruf kapital, tekan Enter
32. Verifikasi hasil identik dengan hasil keyword semula (jumlah baris dan baris sama)
33. Klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-207: Search kelas angka

34. Untuk setiap baris tabel Data uji TC-AC-ACHS-207 (langkah 34 sampai 36): ketik Search keyword, tekan Enter
35. Verifikasi jumlah baris dan baris sesuai kolom "Hasil"
36. Klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-208: Search tanpa hasil

37. Ketik Search `zzqx-tidak-ada`, tekan Enter
38. Verifikasi tabel tidak menampilkan baris data
39. Verifikasi empty state berupa ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
40. Klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-209: Kolom non-searchable (Last Updated, Photo)

41. Verifikasi baris `Fixture.hardwareStock.p16.a[1].sku` menampilkan Last Updated `Fixture.hardwareStock.p16.a[1].lastUpdated` di halaman pertama
42. Ketik Search `Fixture.hardwareStock.derived.lastUpdatedA1Date`, tekan Enter
43. Verifikasi tabel menampilkan 0 baris dengan empty state `No results found`
44. Klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-210: Search terikat visibilitas kolom Range Type

45. Ketik Search `Long Range`, tekan Enter
46. Verifikasi tabel menampilkan 1 baris: `Fixture.hardwareStock.p16.a[4].sku`
47. Klik header kolom Actions `(⋯)`, hilangkan centang `Range Type`, tutup overlay Column Visibility
48. Tekan Enter pada kotak Search berisi `Long Range`
49. Verifikasi tabel menampilkan 0 baris dengan empty state `No results found`
50. Klik header kolom Actions `(⋯)`, ceklis kembali `Range Type`, tutup overlay Column Visibility
51. Tekan Enter pada kotak Search berisi `Long Range`
52. Verifikasi tabel kembali menampilkan 1 baris: `Fixture.hardwareStock.p16.a[4].sku` (sama dengan sebelum hide)
53. Klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-211: Spasi awal dan akhir query dibuang saat Enter

54. Ketik Search `  Fixture.hardwareStock.p16.a[1].brand  ` (spasi di awal dan akhir), tekan Enter
55. Verifikasi tabel menampilkan 3 baris: `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku`
56. Verifikasi isi kotak Search di layar tetap sama seperti yang diketik (`  Fixture.hardwareStock.p16.a[1].brand  `)
57. Ganti isi kotak search dengan `   ` (hanya spasi), tekan Enter
58. Verifikasi tabel kembali ke seluruh baris (info `Showing 1–10 of 30 entries`)

### Pemulihan state

59. Klik `←` pada kotak Search untuk menutup Search dan mereset tabel


## Notes

- Sumber TC: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md`. (bagian 4a, Stock List). Seluruh TC sumber spec ini dikerjakan di sini.
- Konfirmasi S-12 (keyword Search, #8): keyword `Zebra` (`Fixture.hardwareStock.p16.a[1].brand`) adalah nilai kolom Brand penuh yang sama persis dengan keyword literal TC (TC-AC-ACHS-204, 211, 249, 250, 258 menurut spec ini). Dicocokkan dengan Tabel A Pre-setup #16: kolom Brand bernilai `Zebra` hanya pada baris 1, 3, dan 4, dan tidak ada kolom searchable lain di baris lain yang memuat `Zebra`, sehingga himpunan hasil 3 baris sama dengan hasil keyword TC. Tidak ada perbedaan. Keyword `Fixed Reader` (`Fixture.hardwareStock.p16.a[3].deviceName`) juga nilai kolom Device Name penuh yang sama dengan keyword TC-AC-ACHS-205: cocok pada Device Name baris 3, 6, 8 dan Type `Smart Fixed Reader` pada baris 3, 6, 8 serta 22 baris padding, total 25 baris sesuai TC. Keyword `SKU-PAD-0`, `Kontakt`, `Professional`, dan `10 Jun 2026` adalah substring turunan yang sama dengan keyword TC-AC-ACHS-205, 206, 209 (lihat tabel Parameter Pre-setup).
- Langkah penghubung (aksi tanpa `Verifikasi`): pengosongan Search antar-iterasi dan antar-TC (`✕` lalu Enter pada langkah 28, 33, 36, serta setelah TC-AC-ACHS-208, 209, dan 210), penutupan overlay Column Visibility, pemulihan visibilitas kolom Range Type (langkah 51), dan penutupan Search di langkah akhir (hook suite `after` sebagai cadangan). "Ketik Search" membuka kotak Search bila tertutup (bagian 8b butir 9).
- Asersi tambahan (S-03): langkah 1 dari TC-AC-ACHS-209 (`Verifikasi` baris `Fixture.hardwareStock.p16.a[1].sku` bernilai Last Updated `Fixture.hardwareStock.p16.a[1].lastUpdated`) adalah anchor positif bahwa keyword `Fixture.hardwareStock.derived.lastUpdatedA1Date` memang ada di tabel sehingga 0 baris bukan akibat data hilang.
- Langkah 24 sampai 28, 29 sampai 33, dan 34 sampai 36 berulang untuk setiap baris tabel Data uji (tiga iterasi masing-masing, bagian 8b butir 7).
- Spec memiliki 59 langkah nominal dan 85 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Search Stock List pada akun dan dataset read-only yang sama), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari tiga perulangan per kolom data tanpa langkah bersyarat.
- Temuan untuk QA:
  - TC-AC-ACHS-205 b, d, f menyebut keyword huruf kapital; untuk kolom SKU keyword `Fixture.hardwareStock.derived.searchSkuPad0` sudah berhuruf kapital sehingga varian kapitalnya identik dan tidak menguji ketidakpekaan huruf besar kecil. Spec mengikuti TC.
  - TC-AC-ACHS-205 sampai 207 menamai satu kolom per anggota Data Uji, tetapi Search mencocokkan semua kolom searchable (mis. `Fixture.hardwareStock.p16.a[3].deviceName` juga cocok dengan kolom Type `Smart Fixed Reader` sehingga hasilnya 25 baris; `16` pada In Use cocok dengan SKU `Fixture.hardwareStock.p16.a[24].sku`). Spec mengasersi hasil menurut Expected TC.
  - TC-AC-ACHS-209 Data Uji menyebut kolom Last Updated dan Photo, tetapi kolom Photo tidak punya nilai teks; spec hanya menguji keyword Last Updated `Fixture.hardwareStock.derived.lastUpdatedA1Date`. Expected b ("nilai kolom ... tidak memicu match") adalah kesimpulan dari Expected a dan Expected c ("penyaringan kolom itu hanya lewat Filter Panel") tidak punya langkah observasi; keduanya tidak punya `Verifikasi` terpisah (S-03).
