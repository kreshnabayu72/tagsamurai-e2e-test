---
id: TC-AC-ACHS-E2E-180-search-approvals-tab-active
title: "Search Approvals Tab Active"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-369
  - TC-AC-ACHS-370
  - TC-AC-ACHS-371
  - TC-AC-ACHS-372
  - TC-AC-ACHS-373
  - TC-AC-ACHS-374
  - TC-AC-ACHS-375
coverage:
  web: automated
---

# Search Approvals Tab Active

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; tanpa intercept).
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email dari `Fixture.hardwareStock.account.p01.totalControl.email`, kata sandi `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; hook `beforeEach` suite membuka Stock List, dan spec ini membuka Approvals > Hardware Stock sebagai langkah pertama. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Approvals Hardware Stock disetel true di hook `before` suite dan dipulihkan di `after` (lihat suite.md). Suite serial (`parallel: false`).
- Data Pre-setup (hanya dibaca; spec tidak melakukan Approve, Reject, atau Cancel): Approvals Tab Active dengan 12 Subject pending (Pre-setup #21, Tabel C TC). Baris dirujuk lewat nomor baris Tabel C: `#n` (n = 1 sampai 12) berarti baris ke-n Tabel C (`Fixture.hardwareStock.p21.c[n]`). Urutan default FIFO (Requested At terlama di atas) sama dengan urutan Tabel C (#1 teratas, #12 terbawah). Nilai sel tidak ditulis di spec ini; penulis script membaca nilainya dari fixture lewat kunci pada tabel Parameter Pre-setup (R-06).
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture pada tabel berikut, dibaca dari `fixtures/hardwareStock.json` (identitas data, bukan rahasia; berkas belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Kunci fixture |
  |---|---|---|---|
  | Email akun Total Control Principal #1 | #1 | Total Control Principal; akun aktor, login di hook `before`; kata sandi `Spectra.env.AC_TC_PASSWORD` | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Type baris #n (n = 1 sampai 12) | #21 Tabel C | Activation Collision pada #1, #4, #5, #9, #11, #12; Register Duplicate pada #2, #3, #6, #7, #8, #10 | `Fixture.hardwareStock.p21.c[n].type` |
  | Device Name (SKU) baris #n (n = 1 sampai 12) | #21 Tabel C | Device Name diikuti kode SKU dalam kurung; #9 adalah Subject BYO tanpa SKU (Device Name (SKU) tanpa kode SKU, Category `—`) | `Fixture.hardwareStock.p21.c[n].deviceName` |
  | Category baris #n (n = 1 sampai 12) | #21 Tabel C | Long Range pada #1 dan #10; Short Range pada #2, #3, #5, #6, #7, #8, #11; Smart Fixed Reader pada #4; BLE Gateway pada #12; `—` pada #9 | `Fixture.hardwareStock.p21.c[n].category` |
  | Matched Identifier baris #n (n = 1 sampai 12) | #21 Tabel C | Serial Number atau MAC address unik tiap baris, identitas baris hasil; #3, #9, #12 berformat MAC | `Fixture.hardwareStock.p21.c[n].matchedIdentifier` |
  | Existing Record baris #n (n = 1 sampai 12) | #21 Tabel C | memuat kata `Registrant` pada #2, #3, #6, #7, #8, #10; memuat `Active (Client: ...)` pada baris lain | `Fixture.hardwareStock.p21.c[n].existingRecord` |
  | Requested By baris #n (n = 1 sampai 12) | #21 Tabel C | Client, Distributor, atau Principal (Pre-setup #23) dengan label peran dalam kurung; Distributor pada #3, #6, #8, #10 | `Fixture.hardwareStock.p21.c[n].requestedBy` |
  | Requested At baris #n (n = 1 sampai 12) | #21 Tabel C | naik menurut n (FIFO); bulan dan tahun sama pada seluruh baris | `Fixture.hardwareStock.p21.c[n].requestedAt` |
  | Keyword Search nama Client | #21 Tabel C | diturunkan dari `Fixture.hardwareStock.p21.c[5].requestedBy`: nama Client tanpa awalan badan usaha dan tanpa label peran dalam kurung; nama yang sama muncul pada Existing Record #1 dan #11, sehingga Search menghasilkan tepat tiga baris #1, #5, #11 (semua Activation Collision) | `Fixture.hardwareStock.derived.clientCoreNameActive` |
  | Keyword Search Device Name | #21 Tabel C | diturunkan dari `Fixture.hardwareStock.p21.c[12].deviceName`: dua kata pertama (tanpa kode SKU); hanya #12 yang memuatnya | `Fixture.hardwareStock.derived.deviceNameBleActive` |
  | Keyword Search Matched Identifier | #21 Tabel C | diturunkan dari `Fixture.hardwareStock.p21.c[3].matchedIdentifier`: dua oktet pertama, awalan yang dipakai bersama #3 dan #12; tidak mengandung huruf kecil | `Fixture.hardwareStock.derived.macPrefixSharedActive` |
  | Keyword Search bulan dan tahun | #21 Tabel C | diturunkan dari `Fixture.hardwareStock.p21.c[1].requestedAt`: bagian bulan dan tahun (tanpa hari dan jam); Requested At bukan kolom searchable | `Fixture.hardwareStock.derived.requestedAtMonthYearActive` |
- Parameter Search per kolom (dipakai langkah 26 sampai 32, TC 370 dan 371; baris hasil dirujuk lewat nomor baris Tabel C, urutan tampil FIFO):

| Kolom | Keyword | Keyword kapital | Hasil |
|---|---|---|---|
| Type | `Collision` | `COLLISION` | 6 baris: #1, #4, #5, #9, #11, #12 |
| Device Name (SKU) | `Fixture.hardwareStock.derived.deviceNameBleActive` | `Fixture.hardwareStock.derived.deviceNameBleActive` dalam huruf kapital | 1 baris: #12 |
| Category | `Short Range` | `SHORT RANGE` | 7 baris: #2, #3, #5, #6, #7, #8, #11 |
| Matched Identifier | `Fixture.hardwareStock.derived.macPrefixSharedActive` | `Fixture.hardwareStock.derived.macPrefixSharedActive` (tidak mengandung huruf kecil; identik) | 2 baris: #3, #12 |
| Existing Record | `Registrant` | `REGISTRANT` | 6 baris: #2, #3, #6, #7, #8, #10 |
| Requested By | `Distributor` | `DISTRIBUTOR` | 4 baris: #3, #6, #8, #10 |

## Test Steps

### Screening dan siklus kotak Search (TC-AC-ACHS-369)

1. Buka Approvals > Hardware Stock
2. Klik Tab `Active`
3. Hover icon Search
4. Verifikasi tooltip `Search`
5. Klik icon Search
6. Verifikasi kotak Search melebar
7. Verifikasi kursor fokus di input
8. Verifikasi placeholder `Search by device name, identifier, or entity...`
9. Ketik `Fixture.hardwareStock.derived.clientCoreNameActive` tanpa menekan Enter
10. Verifikasi icon `(✕)` muncul
11. Verifikasi tabel belum tersaring, tetap 12 baris
12. Tekan Enter
13. Verifikasi tabel menampilkan 3 baris: #1, #5, #11
14. Klik icon `(✕)` di kotak Search
15. Verifikasi input kosong
16. Verifikasi kotak Search tetap terbuka
17. Verifikasi kursor tetap fokus
18. Verifikasi hasil tabel masih hasil search terakhir: 3 baris #1, #5, #11
19. Tekan Enter pada input yang sudah kosong
20. Verifikasi tabel kembali menampilkan 12 baris
21. Ketik Search `Fixture.hardwareStock.derived.clientCoreNameActive`, tekan Enter
22. Klik icon `(←)` di kiri toolbar
23. Verifikasi kotak Search menutup menjadi icon Search
24. Verifikasi keyword dikosongkan
25. Verifikasi tabel langsung kembali ke seluruh 12 baris tanpa Enter

### Search per kolom, substring dan case-insensitive (TC-AC-ACHS-370, 371)

26. Untuk setiap baris tabel "Parameter Search per kolom" (langkah 27 sampai 32): lakukan langkah berikut
27. Ketik Search keyword persis, tekan Enter
28. Verifikasi hasil sesuai kolom "Hasil" tabel parameter
29. Ganti isi kotak search dengan keyword kapital, tekan Enter
30. Verifikasi hasil identik dengan hasil keyword persis
31. Kosongkan isi kotak search, tekan Enter
32. Verifikasi tabel kembali menampilkan 12 baris
33. Klik icon `(←)` pada kotak Search

### Search tanpa hasil (TC-AC-ACHS-372)

34. Ketik Search `zzqx-tidak-ada`, tekan Enter
35. Verifikasi empty state: ilustrasi dengan Title `No results found` dan Description `Try adjusting your search or filter.`
36. Verifikasi tabel tidak menampilkan baris data
37. Klik icon `(←)` pada kotak Search

### Kolom non-searchable (TC-AC-ACHS-373)

38. Ketik Search `Fixture.hardwareStock.derived.requestedAtMonthYearActive`, tekan Enter
39. Verifikasi empty state `No results found` dan tabel menampilkan 0 baris
40. Verifikasi nilai kolom Requested At tidak memicu match (tidak ada baris cocok untuk keyword bulan dan tahun)
41. Klik icon Filter
42. Verifikasi Filter Panel memuat field Requested At sebagai jalur penyaringan kolom itu
43. Klik icon Filter untuk menutup panel
44. Klik icon `(←)` pada kotak Search

### Search terikat visibilitas kolom Category (TC-AC-ACHS-374)

45. Ketik Search `Long Range`, tekan Enter
46. Verifikasi tabel menampilkan 2 baris: #1, #10
47. Hover header kolom Actions `(⋯)`
48. Verifikasi tooltip `Column Visibility`
49. Klik header kolom Actions `(⋯)`, uncheck `Category`
50. Tekan Enter pada kotak Search (keyword `Long Range` masih terisi)
51. Verifikasi empty state `No results found` dan tabel menampilkan 0 baris (kolom Category tidak lagi dicari)
52. Klik header kolom Actions `(⋯)`, check `Category`
53. Tekan Enter pada kotak Search
54. Verifikasi tabel menampilkan 2 baris: #1, #10, sama dengan sebelum hide
55. Klik icon `(←)` pada kotak Search

### Spasi tepi query (TC-AC-ACHS-375)

56. Ketik Search `Fixture.hardwareStock.derived.clientCoreNameActive` diapit dua spasi di awal dan akhir, tekan Enter
57. Verifikasi tabel menampilkan 3 baris: #1, #5, #11, sama dengan keyword tanpa spasi tepi
58. Verifikasi isi kotak Search di layar tetap `Fixture.hardwareStock.derived.clientCoreNameActive` diapit dua spasi di awal dan akhir
59. Ganti isi kotak search dengan `   ` (hanya spasi), tekan Enter
60. Verifikasi tabel kembali menampilkan seluruh 12 baris
61. Klik icon `(←)` pada kotak Search

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-369 sampai 375). Tidak ada TC hanya-BE di spec ini.
- Nilai Pre-setup tidak ditulis literal; dirujuk lewat nomor item Pre-setup (#21/#22, Tabel C/D) dan kunci fixture, nilai dibaca penulis script dari tabel TC (R-06); tidak ada pengecualian S-12 dipakai. Teks antarmuka asli (nama kolom, label Type dan Category, placeholder, tooltip, teks empty state, nama berkas unduhan) tetap ditulis verbatim.
- Langkah penghubung (bukan dari langkah TC): langkah 33, 37, 44, 55, 61 (klik `(←)` mereset Search, S-09); langkah 41 sampai 43 (membuka dan menutup Filter Panel untuk `Verifikasi` langkah 42, Expected c TC-373); langkah 52 dan 53 (check kembali `Category` lalu Enter, langkah 6 TC-374). Langkah 2 TC (pastikan Tab Active aktif) ditulis sebagai klik Tab `Active` pada langkah 2.
- Idiom ulang "Untuk setiap baris tabel" pada langkah 26 sampai 32 (6 iterasi); parameter di Prerequisites; tiap iterasi memuat `Verifikasi` per klausa.
- Spec melewati sekitar 35 langkah: alasan, semua blok satu surface (Approvals Tab Active) dan satu dataset read-only; tiap blok mengembalikan Search (dan Column Visibility) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; topik satu dataset tetap satu spec (prinsip 1).
- Konfirmasi (#8): kata kunci turunan Search diperiksa terhadap Tabel C TC. Nama inti Client (`Fixture.hardwareStock.derived.clientCoreNameActive`), dua kata pertama Device Name #12 (`Fixture.hardwareStock.derived.deviceNameBleActive`), dua oktet pertama Matched Identifier #3 (`Fixture.hardwareStock.derived.macPrefixSharedActive`), dan bulan-tahun Requested At #1 sama dengan substring yang ditulis TC-369, 371, 373, dan 375, bukan nilai kolom penuh; himpunan hasil identik dengan TC: `Fixture.hardwareStock.derived.clientCoreNameActive` tiga baris (#1, #5, #11), `Fixture.hardwareStock.derived.deviceNameBleActive` satu baris (#12), `Fixture.hardwareStock.derived.macPrefixSharedActive` dua baris (#3, #12), bulan-tahun 0 baris. Tidak ada perbedaan.
- Temuan untuk QA:
  - TC-371 mencampur lima kolom dalam satu TC dengan satu Data Uji; keyword kapital `Fixture.hardwareStock.derived.macPrefixSharedActive` identik dengan keyword persis sehingga asersi case-insensitive tidak bermakna pada kolom Matched Identifier.
  - TC-373 Expected c ("penyaringan kolom itu hanya lewat Filter Panel") adalah pernyataan aturan; spec mengasersinya sebagai keberadaan field Requested At di Filter Panel (langkah 42); hasil Filter diasersi di spec 181 (TC-379).
