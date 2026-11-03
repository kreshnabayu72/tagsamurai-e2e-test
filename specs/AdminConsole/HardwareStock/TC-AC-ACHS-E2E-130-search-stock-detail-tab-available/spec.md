---
id: TC-AC-ACHS-E2E-130-search-stock-detail-tab-available
title: "Search Stock Detail Tab Available: Siklus Kotak, Kolom Teks, Badge, Pengguna, dan Angka, Empty State, Kolom Non-Searchable, Visibilitas Kolom, dan Spasi Tepi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-262
  - TC-AC-ACHS-263
  - TC-AC-ACHS-264
  - TC-AC-ACHS-265
  - TC-AC-ACHS-266
  - TC-AC-ACHS-267
  - TC-AC-ACHS-268
  - TC-AC-ACHS-269
  - TC-AC-ACHS-270
coverage:
  web: automated
---

# Search Stock Detail Tab Available: Siklus Kotak, Kolom Teks, Badge, Pengguna, dan Angka, Empty State, Kolom Non-Searchable, Visibilitas Kolom, dan Spasi Tepi

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
  | Device Name unit 13 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 13, Tabel E (#17) | `Fixture.hardwareStock.p17.e[13].deviceName` |
  | Device Name unit 16 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 16, Tabel E (#17) | `Fixture.hardwareStock.p17.e[16].deviceName` |
  | Device Name unit 19 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 19, Tabel E (#17) | `Fixture.hardwareStock.p17.e[19].deviceName` |
  | Device Name unit 20 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 20, Tabel E (#17) | `Fixture.hardwareStock.p17.e[20].deviceName` |
  | Device Name unit 22 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 22, Tabel E (#17) | `Fixture.hardwareStock.p17.e[22].deviceName` |
  | Device Name unit 24 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 24, Tabel E (#17) | `Fixture.hardwareStock.p17.e[24].deviceName` |
  | Device Name unit 25 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 25, Tabel E (#17) | `Fixture.hardwareStock.p17.e[25].deviceName` |
  | Device Name unit 26 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 26, Tabel E (#17) | `Fixture.hardwareStock.p17.e[26].deviceName` |
  | Device Name unit 27 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 27, Tabel E (#17) | `Fixture.hardwareStock.p17.e[27].deviceName` |
  | Device Name unit 28 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Device Name unit nomor 28, Tabel E (#17) | `Fixture.hardwareStock.p17.e[28].deviceName` |
  | Registered At unit 28 Tabel E | #17 Unit Available SKU RFD40 (Tabel E) | Registered At unit 28 Tabel E (#17), format General Settings #15 | `Fixture.hardwareStock.p17.e[28].registeredAt` |
  | Nilai turunan searchDeviceNameU20 | turunan dari `Fixture.hardwareStock.p17.e[20].deviceName` | keyword Search: bagian Device Name unit 20 Tabel E yang juga cocok dengan unit 21 sampai 28 (`Scanner - 2`; 9 baris; sama dengan keyword TC-AC-ACHS-263) | `Fixture.hardwareStock.derived.searchDeviceNameU20` |
  | Nilai turunan searchRegisteredAtMonth | turunan dari `Fixture.hardwareStock.p17.e[10].registeredAt` | keyword Search: bulan dan tahun Registered At unit Tabel E (`May 2026`; substring dari Registered At unit 10) | `Fixture.hardwareStock.derived.searchRegisteredAtMonth` |
  | Nilai turunan searchRegisteredByU10 | turunan dari `Fixture.hardwareStock.p17.e[10].registeredBy` | keyword Search: kata pertama Registered By unit 10 Tabel E (`Dedi`; substring; sama dengan keyword TC-AC-ACHS-265) | `Fixture.hardwareStock.derived.searchRegisteredByU10` |
  | Nilai turunan searchSerialU20 | turunan dari `Fixture.hardwareStock.p17.e[20].serialNumber` | keyword Search: bagian akhir Serial Number unit 20 Tabel E (`000020`; hanya angka; 1 baris; sama dengan keyword TC-AC-ACHS-263) | `Fixture.hardwareStock.derived.searchSerialU20` |
- Urutan default Tab Available (Registered At Newest First): `Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName`, `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[24].deviceName`.
- Data uji TC-AC-ACHS-263 sampai TC-AC-ACHS-265 (kolom "Keyword huruf kapital" adalah keyword yang sama dalam huruf kapital):

  | No | TC | Kolom | Keyword | Keyword huruf kapital | Hasil |
  |---|---|---|---|---|---|
  | 1 | 263 | Device Name | `Fixture.hardwareStock.derived.searchDeviceNameU20` | `upper(Fixture.hardwareStock.derived.searchDeviceNameU20)` | 9 baris; lima teratas `Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName`, `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[24].deviceName` |
  | 2 | 263 | Serial Number | `Fixture.hardwareStock.derived.searchSerialU20` | `Fixture.hardwareStock.derived.searchSerialU20` | 1 baris: `Fixture.hardwareStock.p17.e[20].deviceName` |
  | 3 | 264 | Status | `Waiting` | `WAITING` | 1 baris: `Fixture.hardwareStock.p17.e[28].deviceName` |
  | 4 | 265 | Registered By | `Fixture.hardwareStock.derived.searchRegisteredByU10` | `upper(Fixture.hardwareStock.derived.searchRegisteredByU10)` | 6 baris: `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[22].deviceName`, `Fixture.hardwareStock.p17.e[19].deviceName`, `Fixture.hardwareStock.p17.e[16].deviceName`, `Fixture.hardwareStock.p17.e[13].deviceName`, `Fixture.hardwareStock.p17.e[10].deviceName` |

- Data uji TC-AC-ACHS-266 (kelas angka):

  | No | Kolom | Keyword | Hasil |
  |---|---|---|---|
  | 1 | Min Power | `-20` | 19 baris; lima teratas `Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName`, `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[24].deviceName` |
  | 2 | Max Power | `30` | 19 baris; lima teratas `Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName`, `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[24].deviceName` |
  | 3 | Current Power | `27` | 3 baris: `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[16].deviceName` |

- Kemampuan teknis (disediakan tim FE): menutup kotak Search lewat `←` untuk mereset tabel.
- State global yang diubah: visibilitas kolom Registered By (langkah 44 sampai 48) dipulihkan di langkah 48. Preferensi kolom di browser dihapus oleh hook suite `after`.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Pastikan Tab Available aktif

### TC-AC-ACHS-262: Siklus Search toolbar

3. Arahkan kursor ke icon Search
4. Verifikasi tooltip `Search`
5. Klik icon Search
6. Verifikasi kotak Search melebar
7. Verifikasi kursor fokus di input Search
8. Verifikasi placeholder input Search `Search by name or serial number...`
9. Ketik `Fixture.hardwareStock.derived.searchDeviceNameU20` di kotak Search tanpa menekan Enter
10. Verifikasi icon `✕` muncul di kotak Search
11. Verifikasi tabel belum tersaring (info `Showing 1–10 of 19 entries`)
12. Tekan Enter
13. Verifikasi tabel menampilkan 9 baris, lima teratas `Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName`, `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[24].deviceName`
14. Klik `✕` pada kotak Search
15. Verifikasi input Search kosong
16. Verifikasi kotak Search tetap terbuka
17. Verifikasi kursor tetap fokus di input Search
18. Verifikasi tabel masih menampilkan hasil search terakhir (9 baris)
19. Tekan Enter pada input yang sudah kosong
20. Verifikasi tabel kembali menampilkan seluruh baris (info `Showing 1–10 of 19 entries`)
21. Ketik Search `Fixture.hardwareStock.derived.searchDeviceNameU20`, tekan Enter
22. Klik `←` di kiri toolbar
23. Verifikasi kotak Search menutup menjadi icon Search
24. Verifikasi keyword Search dikosongkan
25. Verifikasi tabel langsung kembali ke seluruh baris tanpa Enter (info `Showing 1–10 of 19 entries`)

### TC-AC-ACHS-263, 264, 265: Search kelas teks, badge, dan pengguna

26. Untuk setiap baris tabel Data uji TC-AC-ACHS-263 sampai 265 (langkah 26 sampai 30): ketik Search keyword, tekan Enter
27. Verifikasi jumlah baris dan baris sesuai kolom "Hasil"
28. Ganti isi kotak search dengan keyword huruf kapital, tekan Enter
29. Verifikasi hasil identik dengan hasil keyword semula (jumlah baris dan baris sama)
30. Klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-266: Search kelas angka

31. Untuk setiap baris tabel Data uji TC-AC-ACHS-266 (langkah 31 sampai 33): ketik Search keyword, tekan Enter
32. Verifikasi jumlah baris dan baris sesuai kolom "Hasil"
33. Klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-267: Search tanpa hasil

34. Ketik Search `zzqx-tidak-ada`, tekan Enter
35. Verifikasi tabel tidak menampilkan baris data
36. Verifikasi empty state berupa ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
37. Klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-268: Kolom non-searchable (Registered At)

38. Verifikasi baris `Fixture.hardwareStock.p17.e[28].deviceName` menampilkan Registered At `Fixture.hardwareStock.p17.e[28].registeredAt`
39. Ketik Search `Fixture.hardwareStock.derived.searchRegisteredAtMonth`, tekan Enter
40. Verifikasi tabel menampilkan 0 baris dengan empty state `No results found`
41. Klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-269: Search terikat visibilitas kolom Registered By

42. Ketik Search `Fixture.hardwareStock.derived.searchRegisteredByU10`, tekan Enter
43. Verifikasi tabel menampilkan 6 baris: `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[22].deviceName`, `Fixture.hardwareStock.p17.e[19].deviceName`, `Fixture.hardwareStock.p17.e[16].deviceName`, `Fixture.hardwareStock.p17.e[13].deviceName`, `Fixture.hardwareStock.p17.e[10].deviceName`
44. Klik header kolom Actions `(⋯)`, hilangkan centang `Registered By`, tutup overlay Column Visibility
45. Tekan Enter pada kotak Search berisi `Fixture.hardwareStock.derived.searchRegisteredByU10`
46. Verifikasi tabel menampilkan 0 baris dengan empty state `No results found`
47. Klik header kolom Actions `(⋯)`, ceklis kembali `Registered By`, tutup overlay Column Visibility
48. Tekan Enter pada kotak Search berisi `Fixture.hardwareStock.derived.searchRegisteredByU10`
49. Verifikasi tabel kembali menampilkan 6 baris: `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[22].deviceName`, `Fixture.hardwareStock.p17.e[19].deviceName`, `Fixture.hardwareStock.p17.e[16].deviceName`, `Fixture.hardwareStock.p17.e[13].deviceName`, `Fixture.hardwareStock.p17.e[10].deviceName` (sama dengan sebelum hide)
50. Klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-270: Spasi awal dan akhir query dibuang saat Enter

51. Ketik Search `  Fixture.hardwareStock.derived.searchDeviceNameU20  ` (spasi di awal dan akhir), tekan Enter
52. Verifikasi tabel menampilkan 9 baris, lima teratas `Fixture.hardwareStock.p17.e[28].deviceName`, `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName`, `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[24].deviceName`
53. Verifikasi isi kotak Search di layar tetap sama seperti yang diketik (`  Fixture.hardwareStock.derived.searchDeviceNameU20  `)
54. Ganti isi kotak search dengan `   ` (hanya spasi), tekan Enter
55. Verifikasi tabel kembali ke seluruh 19 baris (info `Showing 1–10 of 19 entries`)

### Pemulihan state

56. Klik `←` pada kotak Search untuk menutup Search dan mereset tabel


## Notes

- Sumber TC: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md`. (bagian 4b, Stock Detail Tab Available). Seluruh TC sumber spec ini dikerjakan di sini.
- Konfirmasi S-12 (keyword Search, #8): keyword turunan `Fixture.hardwareStock.derived.*` pada spec ini adalah substring yang sama dengan keyword literal TC (bukan nilai kolom penuh): `Scanner - 2`, `000020`, `Dedi` (TC-AC-ACHS-263 dan 265). Dicocokkan dengan Tabel E Pre-setup #17 (Device Name unit 20 sampai 28 = 9 baris; Serial Number unit 20 = 1 baris; Registered By `Dedi K` pada unit 10, 13, 16, 19, 22, 25 = 6 baris); himpunan hasil identik dengan hasil di TC. Tidak ada perbedaan.
- TC-AC-ACHS-263, 264, dan 265 berbagi satu perulangan (langkah 26 sampai 30, empat iterasi) karena langkahnya identik; TC-AC-ACHS-266 memakai perulangan tanpa varian kapital (langkah 31 sampai 33, tiga iterasi; bagian 8b butir 7).
- Langkah penghubung (aksi tanpa `Verifikasi`): "Pastikan Tab Available aktif", pengosongan Search antar-iterasi dan antar-TC, penutupan overlay Column Visibility, pemulihan visibilitas kolom Registered By (langkah 48), dan penutupan Search di langkah akhir (hook suite `after` sebagai cadangan).
- Asersi tambahan (S-03): langkah "Verifikasi baris `Fixture.hardwareStock.p17.e[28].deviceName` menampilkan Registered At `Fixture.hardwareStock.p17.e[28].registeredAt`" pada TC-AC-ACHS-268 adalah anchor positif bahwa nilai `Fixture.hardwareStock.derived.searchRegisteredAtMonth` memang ada di tabel.
- Spec memiliki 56 langkah nominal dan 77 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Search Stock Detail Tab Available pada akun dan dataset read-only yang sama), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari dua perulangan per kolom data tanpa langkah bersyarat.
- Temuan untuk QA:
  - TC, PRD, dan LLD yang dibaca tidak menyebut apakah halaman Stock Detail punya flag Guided Tooltip sendiri; spec menyetel flag halaman Stock Detail seperti flag Stock List dengan kemampuan yang disediakan tim FE.
  - TC-AC-ACHS-263 sampai 265 meminta varian huruf kapital untuk setiap anggota; untuk Serial Number `Fixture.hardwareStock.derived.searchSerialU20` (hanya angka) varian kapital identik dan tidak menguji ketidakpekaan huruf besar kecil. TC-AC-ACHS-266 tidak meminta varian kapital.
  - TC-AC-ACHS-263 Expected c menulis keyword `Fixture.hardwareStock.derived.searchSerialU20` pada kolom Serial Number dengan hasil `Fixture.hardwareStock.p17.e[20].deviceName`; Search mencocokkan semua kolom searchable sehingga asersi hanya pada hasil menurut Expected TC.
