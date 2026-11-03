---
id: TC-AC-ACHS-E2E-160-search-stock-detail-tab-in-use
title: "Search Stock Detail Tab In Use"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-318
  - TC-AC-ACHS-319
  - TC-AC-ACHS-320
  - TC-AC-ACHS-321
  - TC-AC-ACHS-322
  - TC-AC-ACHS-323
  - TC-AC-ACHS-324
  - TC-AC-ACHS-325
  - TC-AC-ACHS-326
coverage:
  web: automated
---

# Search Stock Detail Tab In Use

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; tanpa intercept).
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email `Fixture.hardwareStock.account.p01.totalControl.email`, nama tampil `Fixture.hardwareStock.account.p01.totalControl.fullName`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List disetel true di hook `before` suite dan dipulihkan di `after` (lihat suite.md); spec ini tidak menguji flag itu. Suite serial (`parallel: false`).
- Data Pre-setup (hanya dibaca, tidak diubah spec): SKU `Fixture.hardwareStock.p18.sku` (SKU Long Range, Pre-setup #16 dan #18) dengan 7 unit In Use (Pre-setup #18, Tabel F TC). Spec tidak menulis nama, Serial Number, Client, atau nama pendaftar Pre-setup secara literal: baris unit dirujuk `Fixture.hardwareStock.p18.f[n].<kolom>` dengan n = nilai kolom N Tabel F (kolom: deviceName, serialNumber, client, status, registeredBy, registeredAt, activatedAt, minPower, maxPower, currentPower); pada langkah dan tabel, sebuah baris unit ditulis dengan kunci `.deviceName`-nya. Peran data:

| Peran | Baris Tabel F (N) | Sumber nilai |
|---|---|---|
| Client yang sama pada tiga unit | 1, 2, 3 | `Fixture.hardwareStock.p18.f[1].client` |
| Client yang sama pada dua unit | 4, 5 | `Fixture.hardwareStock.p18.f[4].client` |
| Client berbeda, satu unit tiap Client | 6 dan 7 | `Fixture.hardwareStock.p18.f[6].client`, `Fixture.hardwareStock.p18.f[7].client` |
| Status Damaged | 1, 6 | label Status (teks UI) |
| Status Missing | 3 | label Status (teks UI) |
| Pendaftar yang sama pada dua unit | 3, 6 | `Fixture.hardwareStock.p18.f[3].registeredBy` |
| Min Power dan Max Power | sama pada seluruh unit | `Fixture.hardwareStock.p18.f[1].minPower`, `Fixture.hardwareStock.p18.f[1].maxPower` |
| Current Power unik | 3 | `Fixture.hardwareStock.p18.f[3].currentPower` |

- Urutan tampil default Tab In Use: Activated At terbaru di atas, yaitu `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName`.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Nama tampil akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.fullName` |
  | SKU Long Range In Use | #18 SKU RFD40 (sama dengan Tabel A baris 4) | kode SKU Handheld Reader Long Range dengan 7 unit In Use (#16, #18) | `Fixture.hardwareStock.p18.sku` |
  | Client baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Client unit nomor 1, Tabel F (#18) | `Fixture.hardwareStock.p18.f[1].client` |
  | Device Name baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 1, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[1].deviceName` |
  | Max Power baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Max Power unit nomor 1, Tabel F (#18) | `Fixture.hardwareStock.p18.f[1].maxPower` |
  | Min Power baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Min Power unit nomor 1, Tabel F (#18) | `Fixture.hardwareStock.p18.f[1].minPower` |
  | Device Name baris 2 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 2, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[2].deviceName` |
  | Current Power baris 3 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Current Power unit nomor 3, Tabel F (#18) | `Fixture.hardwareStock.p18.f[3].currentPower` |
  | Device Name baris 3 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 3, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[3].deviceName` |
  | Registered By baris 3 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Registered By unit nomor 3, Tabel F (#18) | `Fixture.hardwareStock.p18.f[3].registeredBy` |
  | Client baris 4 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Client unit nomor 4, Tabel F (#18) | `Fixture.hardwareStock.p18.f[4].client` |
  | Device Name baris 4 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 4, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[4].deviceName` |
  | Device Name baris 5 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 5, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[5].deviceName` |
  | Client baris 6 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Client unit nomor 6, Tabel F (#18) | `Fixture.hardwareStock.p18.f[6].client` |
  | Device Name baris 6 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 6, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[6].deviceName` |
  | Client baris 7 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Client unit nomor 7, Tabel F (#18) | `Fixture.hardwareStock.p18.f[7].client` |
  | Device Name baris 7 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 7, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[7].deviceName` |
  | Nilai turunan inUseActivatedMonth | turunan dari `Fixture.hardwareStock.p18.f[1].activatedAt` | keyword Search: bulan dan tahun Activated At baris 1 Tabel F sebagaimana tampil di tabel (`May 2026`; TC-AC-ACHS-324) | `Fixture.hardwareStock.derived.inUseActivatedMonth` |
  | Nilai turunan inUseClientA | turunan dari `Fixture.hardwareStock.p18.f[1].client` | keyword Search: kata nama Client baris 1 Tabel F setelah awalan badan usaha (`Sejahtera`; substring Client baris 1 sampai 3; sama dengan keyword TC-AC-ACHS-318) | `Fixture.hardwareStock.derived.inUseClientA` |
  | Nilai turunan inUseClientB | turunan dari `Fixture.hardwareStock.p18.f[4].client` | keyword Search: kata nama Client baris 4 Tabel F setelah awalan badan usaha (`Makmur`; substring Client baris 4 dan 5; sama dengan keyword TC-AC-ACHS-319 dan 325) | `Fixture.hardwareStock.derived.inUseClientB` |
  | Nilai turunan inUseCurrentPower3 | turunan dari `Fixture.hardwareStock.p18.f[3].currentPower` | keyword Search: angka Current Power baris 3 Tabel F tanpa satuan (`24`; TC-AC-ACHS-322) | `Fixture.hardwareStock.derived.inUseCurrentPower3` |
  | Nilai turunan inUseDeviceName3 | turunan dari `Fixture.hardwareStock.p18.f[3].deviceName` | keyword Search: bagian Device Name baris 3 Tabel F dari kata terakhir sebelum tanda hubung sampai nomor unit (`Scanner - 3`; 1 baris; sama dengan keyword TC-AC-ACHS-319) | `Fixture.hardwareStock.derived.inUseDeviceName3` |
  | Nilai turunan inUseMaxPower | turunan dari `Fixture.hardwareStock.p18.f[1].maxPower` | keyword Search: angka Max Power tanpa satuan (`30`), sama pada seluruh unit (TC-AC-ACHS-322) | `Fixture.hardwareStock.derived.inUseMaxPower` |
  | Nilai turunan inUseMinPower | turunan dari `Fixture.hardwareStock.p18.f[1].minPower` | keyword Search: angka Min Power tanpa satuan (`-20`), sama pada seluruh unit (TC-AC-ACHS-322) | `Fixture.hardwareStock.derived.inUseMinPower` |
  | Nilai turunan inUseRegistrarC | turunan dari `Fixture.hardwareStock.p18.f[3].registeredBy` | keyword Search: kata pertama Registered By baris 3 Tabel F (`Rina`; sama dengan keyword TC-AC-ACHS-321) | `Fixture.hardwareStock.derived.inUseRegistrarC` |
  | Nilai turunan inUseSerial5 | turunan dari `Fixture.hardwareStock.p18.f[5].serialNumber` | keyword Search: enam digit terakhir Serial Number baris 5 Tabel F (`000005`; 1 baris; sama dengan keyword TC-AC-ACHS-319) | `Fixture.hardwareStock.derived.inUseSerial5` |

- Parameter Search per kolom (dipakai langkah 26 sampai 33, TC 319 sampai 322; hasil dalam urutan tampil):

| Kolom | Keyword | Hasil (baris, urutan tampil) |
|---|---|---|
| Device Name | `Fixture.hardwareStock.derived.inUseDeviceName3` | 1 baris: `Fixture.hardwareStock.p18.f[3].deviceName` |
| Serial Number | `Fixture.hardwareStock.derived.inUseSerial5` | 1 baris: `Fixture.hardwareStock.p18.f[5].deviceName` |
| Client | `Fixture.hardwareStock.derived.inUseClientB` | 2 baris: `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName` |
| Status | `Damaged` | 2 baris: `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName` |
| Registered By | `Fixture.hardwareStock.derived.inUseRegistrarC` | 2 baris: `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName` |
| Min Power | `Fixture.hardwareStock.derived.inUseMinPower` | 7 baris: `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName` |
| Max Power | `Fixture.hardwareStock.derived.inUseMaxPower` | 7 baris: `Fixture.hardwareStock.p18.f[7].deviceName` sampai `Fixture.hardwareStock.p18.f[1].deviceName` (urutan sama dengan Min Power) |
| Current Power | `Fixture.hardwareStock.derived.inUseCurrentPower3` | 1 baris: `Fixture.hardwareStock.p18.f[3].deviceName` |

- Keyword huruf kapital tiap baris tabel di atas adalah keyword yang sama dalam huruf besar; untuk keyword angka (`Fixture.hardwareStock.derived.inUseMinPower`, `Fixture.hardwareStock.derived.inUseMaxPower`, `Fixture.hardwareStock.derived.inUseCurrentPower3`) identik dengan keyword persis.

## Test Steps

### Screening dan siklus kotak Search (TC-AC-ACHS-318)

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p18.sku` di Stock List
2. Klik Tab `In Use`
3. Hover icon Search
4. Verifikasi tooltip `Search`
5. Klik icon Search
6. Verifikasi kotak Search melebar
7. Verifikasi kursor fokus di input
8. Verifikasi placeholder `Search by serial number or client...`
9. Ketik `Fixture.hardwareStock.derived.inUseClientA` tanpa menekan Enter
10. Verifikasi icon `(✕)` muncul
11. Verifikasi tabel belum tersaring, tetap 7 baris
12. Tekan Enter
13. Verifikasi tabel menampilkan 3 baris: `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName`
14. Klik icon `(✕)` di kotak Search
15. Verifikasi input kosong
16. Verifikasi kotak Search tetap terbuka
17. Verifikasi kursor tetap fokus
18. Verifikasi hasil tabel masih hasil search terakhir: 3 baris `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName`
19. Tekan Enter pada input yang sudah kosong
20. Verifikasi tabel kembali menampilkan 7 baris
21. Ketik Search `Fixture.hardwareStock.derived.inUseClientA`, tekan Enter
22. Klik icon `(←)` di kiri toolbar
23. Verifikasi kotak Search menutup menjadi icon Search
24. Verifikasi keyword dikosongkan
25. Verifikasi tabel langsung kembali ke seluruh 7 baris tanpa Enter

### Search per kelas kolom, substring dan case-insensitive (TC-AC-ACHS-319, 320, 321, 322)

26. Untuk setiap baris tabel "Parameter Search per kolom" (langkah 27 sampai 33): lakukan langkah berikut
27. Ketik Search keyword persis, tekan Enter
28. Verifikasi hasil sesuai kolom "Hasil" tabel parameter
29. Ganti isi kotak search dengan keyword yang sama dalam huruf kapital, tekan Enter
30. Verifikasi hasil identik dengan hasil keyword persis
31. Kosongkan isi kotak search, tekan Enter
32. Verifikasi tabel kembali menampilkan 7 baris
33. Klik icon `(←)` pada kotak Search

### Search tanpa hasil (TC-AC-ACHS-323)

34. Ketik Search `zzqx-tidak-ada`, tekan Enter
35. Verifikasi empty state: ilustrasi dengan Title `No results found` dan Description `Try adjusting your search or filter.`
36. Verifikasi tabel tidak menampilkan baris data
37. Klik icon `(←)` pada kotak Search

### Kolom non-searchable (TC-AC-ACHS-324)

38. Ketik Search `Fixture.hardwareStock.derived.inUseActivatedMonth`, tekan Enter
39. Verifikasi empty state `No results found` dan tabel menampilkan 0 baris
40. Verifikasi nilai kolom Registered At dan Activated At tidak memicu match (tidak ada baris cocok untuk `Fixture.hardwareStock.derived.inUseActivatedMonth`)
41. Klik icon Filter
42. Verifikasi Filter Panel memuat field Registered At dan Activated At sebagai jalur penyaringan kolom itu
43. Klik icon Filter untuk menutup panel
44. Klik icon `(←)` pada kotak Search

### Search terikat visibilitas kolom Client (TC-AC-ACHS-325)

45. Ketik Search `Fixture.hardwareStock.derived.inUseClientB`, tekan Enter
46. Verifikasi tabel menampilkan 2 baris: `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName`
47. Hover header kolom Actions `(⋯)`
48. Verifikasi tooltip `Column Visibility`
49. Klik header kolom Actions `(⋯)`, uncheck `Client`
50. Tekan Enter pada kotak Search (keyword `Fixture.hardwareStock.derived.inUseClientB` masih terisi)
51. Verifikasi empty state `No results found` dan tabel menampilkan 0 baris (kolom Client tidak lagi dicari)
52. Klik header kolom Actions `(⋯)`, check `Client`
53. Tekan Enter pada kotak Search
54. Verifikasi tabel menampilkan 2 baris: `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName`, sama dengan sebelum hide
55. Klik icon `(←)` pada kotak Search

### Spasi tepi query (TC-AC-ACHS-326)

56. Ketik Search `Fixture.hardwareStock.derived.inUseClientA` dengan spasi di awal dan akhir (`  <Fixture.hardwareStock.derived.inUseClientA>  `) (spasi di awal dan akhir), tekan Enter
57. Verifikasi tabel menampilkan 3 baris: `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName`, sama dengan keyword tanpa spasi tepi
58. Verifikasi isi kotak Search di layar tetap `  <Fixture.hardwareStock.derived.inUseClientA>  ` (keyword dengan spasi tepi)
59. Ganti isi kotak search dengan `   ` (hanya spasi), tekan Enter
60. Verifikasi tabel kembali menampilkan seluruh 7 baris
61. Klik icon `(←)` pada kotak Search

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-318 sampai 326). Tidak ada TC hanya-BE di spec ini.
- Konfirmasi S-12 (keyword Search, #8): keyword turunan `Fixture.hardwareStock.derived.*` pada spec ini adalah substring yang sama dengan keyword literal TC (bukan nilai kolom penuh): `Sejahtera`, `Makmur`, `Scanner - 3`, `000005`, `Rina`, `-20`, `30`, `24`, `May 2026` (TC-AC-ACHS-318 sampai 326). Dicocokkan dengan Tabel F Pre-setup #18 (Client baris 1 sampai 3 = `Sejahtera`; baris 4 dan 5 = `Makmur`; Device Name baris 3 = `Scanner - 3`; Serial Number baris 5 = `...000005`; Registered By baris 3 dan 6 = `Rina`; Min/Max/Current Power sesuai Tabel F; Activated At baris 1 = `May 2026` sebagai kolom non-searchable); himpunan hasil identik dengan hasil di TC. Tidak ada perbedaan.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 37, 44, 55, dan 61 (klik `(←)` untuk menutup input dan mereset tabel sebelum TC berikutnya, S-09); langkah 41 sampai 43 hanya membuka dan menutup Filter Panel untuk Verifikasi langkah 42 (Expected c TC-324); langkah 52 dan 53 (check kembali `Client` lalu Enter) adalah bagian TC-325 langkah 7. Langkah buka Stock List ada di hook `beforeEach` (langkah 1 TC); langkah 1 dan 2 spec membuka Stock Detail dan Tab In Use (langkah 2 dan 3 TC).
- Nilai Pre-setup tidak ditulis literal; dirujuk lewat nomor item Pre-setup (#18, Tabel F) dan kunci fixture, nilai dibaca penulis script dari tabel TC (R-06); tidak ada pengecualian S-12 dipakai. Teks UI asli (label Status, placeholder, tooltip, empty state) tetap ditulis verbatim.
- Search untuk menemukan baris target bukan dipakai spec ini; seluruh Search adalah objek uji (R-16 tidak berlaku).
- Idiom ulang "Untuk setiap baris tabel" dipakai pada langkah 26 sampai 33; tiap iterasi memuat `Verifikasi` per klausa (S-01), ekspansi 8 iterasi.
- Spec melewati sekitar 35 langkah: alasan, seluruh blok satu surface (Tab In Use SKU Pre-setup #18) dan satu dataset Pre-setup #18 yang hanya dibaca; topik Search satu dataset dipertahankan satu spec (prinsip 1); tiap blok TC memulihkan Search sendiri sehingga kegagalan satu blok tidak mengubah state blok lain.
- Pilihan spec (bukan nilai TC): tidak ada nilai waktu; keyword huruf kapital TC-322 (`-20`, `30`, `24`) adalah angka sehingga identik dengan keyword persis.
- Temuan untuk QA:
  - TC-319 sampai TC-322 meminta "Ulangi dengan keyword yang sama dalam huruf kapital"; untuk keyword angka (Min Power `-20`, Max Power `30`, Current Power `24`) huruf kapital tidak ada bedanya, sehingga asersi case-insensitive tidak bermakna pada kolom itu.
  - TC-324 Expected c ("penyaringan kolom itu hanya lewat Filter Panel") adalah pernyataan aturan; spec mengasersinya sebagai keberadaan field Registered At dan Activated At di Filter Panel (langkah 42). Penyaringan hasil per field diasersi di spec 161 (TC-330).
