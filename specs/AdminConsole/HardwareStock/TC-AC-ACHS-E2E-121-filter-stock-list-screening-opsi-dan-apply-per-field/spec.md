---
id: TC-AC-ACHS-E2E-121-filter-stock-list-screening-opsi-dan-apply-per-field
title: "Filter Stock List: Screening Panel, Isi Opsi, Apply per Field, Opsi Tanpa Nilai Kosong, dan State Loading Opsi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-212
  - TC-AC-ACHS-213
  - TC-AC-ACHS-214
  - TC-AC-ACHS-215
  - TC-AC-ACHS-216
  - TC-AC-ACHS-259
  - TC-AC-ACHS-606
coverage:
  web: automated
---

# Filter Stock List: Screening Panel, Isi Opsi, Apply per Field, Opsi Tanpa Nilai Kosong, dan State Loading Opsi

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
  | Device Name baris 1 Tabel A | #16 Katalog SKU (Tabel A) | Device Name baris 1 Tabel A (#16): Handheld Reader Short Range, 34 Available dan 16 In Use (#19) | `Fixture.hardwareStock.p16.a[1].deviceName` |
  | Model/Type baris 1 Tabel A | #16 Katalog SKU (Tabel A) | Model/Type baris 1 Tabel A (#16): Handheld Reader Short Range, 34 Available dan 16 In Use (#19) | `Fixture.hardwareStock.p16.a[1].modelType` |
  | SKU baris 1 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 1 Tabel A (#16): Handheld Reader Short Range, 34 Available dan 16 In Use (#19) | `Fixture.hardwareStock.p16.a[1].sku` |
  | Brand baris 2 Tabel A | #16 Katalog SKU (Tabel A) | Brand baris 2 Tabel A (#16): Handheld Reader Short Range, 12 Available; Brand yang sama pada baris 6 dan 8 | `Fixture.hardwareStock.p16.a[2].brand` |
  | Model/Type baris 2 Tabel A | #16 Katalog SKU (Tabel A) | Model/Type baris 2 Tabel A (#16): Handheld Reader Short Range, 12 Available | `Fixture.hardwareStock.p16.a[2].modelType` |
  | SKU baris 2 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 2 Tabel A (#16): Handheld Reader Short Range, 12 Available | `Fixture.hardwareStock.p16.a[2].sku` |
  | Device Name baris 3 Tabel A | #16 Katalog SKU (Tabel A) | Device Name baris 3 Tabel A (#16): Smart Fixed Reader, 8 Available (#27) | `Fixture.hardwareStock.p16.a[3].deviceName` |
  | Model/Type baris 3 Tabel A | #16 Katalog SKU (Tabel A) | Model/Type baris 3 Tabel A (#16): Smart Fixed Reader, 8 Available (#27) | `Fixture.hardwareStock.p16.a[3].modelType` |
  | SKU baris 3 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 3 Tabel A (#16): Smart Fixed Reader, 8 Available (#27) | `Fixture.hardwareStock.p16.a[3].sku` |
  | SKU baris 4 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 4 Tabel A (#16): Handheld Reader Long Range, 18 Available dan 7 In Use (#17, #18) | `Fixture.hardwareStock.p16.a[4].sku` |
  | Brand baris 5 Tabel A | #16 Katalog SKU (Tabel A) | Brand baris 5 Tabel A (#16): BLE Gateway | `Fixture.hardwareStock.p16.a[5].brand` |
  | Device Name baris 5 Tabel A | #16 Katalog SKU (Tabel A) | Device Name baris 5 Tabel A (#16): BLE Gateway, 4 Available dan 1 In Use (#27) | `Fixture.hardwareStock.p16.a[5].deviceName` |
  | SKU baris 5 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 5 Tabel A (#16): BLE Gateway, 4 Available dan 1 In Use (#27) | `Fixture.hardwareStock.p16.a[5].sku` |
  | Model/Type baris 6 Tabel A | #16 Katalog SKU (Tabel A) | Model/Type baris 6 Tabel A (#16): Smart Fixed Reader tanpa unit (Total Registered 0, Last Updated kosong) | `Fixture.hardwareStock.p16.a[6].modelType` |
  | SKU baris 6 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 6 Tabel A (#16): Smart Fixed Reader tanpa unit (Total Registered 0, Last Updated kosong) | `Fixture.hardwareStock.p16.a[6].sku` |
  | Brand baris 7 Tabel A | #16 Katalog SKU (Tabel A) | Brand baris 7 Tabel A (#16): BLE Gateway dengan Brand bernilai panjang | `Fixture.hardwareStock.p16.a[7].brand` |
  | Model/Type baris 7 Tabel A | #16 Katalog SKU (Tabel A) | Model/Type baris 7 Tabel A (#16): BLE Gateway dengan Brand dan Model/Type bernilai panjang | `Fixture.hardwareStock.p16.a[7].modelType` |
  | Model/Type baris 8 Tabel A | #16 Katalog SKU (Tabel A) | Model/Type baris 8 Tabel A (#16): Smart Fixed Reader dengan 120 Available (#24) | `Fixture.hardwareStock.p16.a[8].modelType` |
  | SKU baris 8 Tabel A | #16 Katalog SKU (Tabel A) | kode SKU baris 8 Tabel A (#16): Smart Fixed Reader dengan 120 Available (#24) | `Fixture.hardwareStock.p16.a[8].sku` |
  | Brand baris padding 01 (Tabel A baris 9) | #16 Katalog SKU (Tabel A) | Brand semua baris padding (#16), juga Brand SKU seed sesaat 16e dan 16h | `Fixture.hardwareStock.p16.a[9].brand` |
  | Device Name baris padding 01 (Tabel A baris 9) | #16 Katalog SKU (Tabel A) | Device Name baris padding nomor 01 (#16) | `Fixture.hardwareStock.p16.a[9].deviceName` |
  | Model/Type baris padding 01 (Tabel A baris 9) | #16 Katalog SKU (Tabel A) | Model/Type baris padding nomor 01 (#16) | `Fixture.hardwareStock.p16.a[9].modelType` |
  | SKU baris padding 01 (Tabel A baris 9) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 01 (#16) | `Fixture.hardwareStock.p16.a[9].sku` |
  | Device Name baris padding 02 (Tabel A baris 10) | #16 Katalog SKU (Tabel A) | Device Name baris padding nomor 02 (#16) | `Fixture.hardwareStock.p16.a[10].deviceName` |
  | Model/Type baris padding 02 (Tabel A baris 10) | #16 Katalog SKU (Tabel A) | Model/Type baris padding nomor 02 (#16) | `Fixture.hardwareStock.p16.a[10].modelType` |
  | Device Name baris padding 03 (Tabel A baris 11) | #16 Katalog SKU (Tabel A) | Device Name baris padding nomor 03 (#16) | `Fixture.hardwareStock.p16.a[11].deviceName` |
  | Model/Type baris padding 03 (Tabel A baris 11) | #16 Katalog SKU (Tabel A) | Model/Type baris padding nomor 03 (#16) | `Fixture.hardwareStock.p16.a[11].modelType` |
  | Device Name baris padding 04 (Tabel A baris 12) | #16 Katalog SKU (Tabel A) | Device Name baris padding nomor 04 (#16) | `Fixture.hardwareStock.p16.a[12].deviceName` |
  | Model/Type baris padding 04 (Tabel A baris 12) | #16 Katalog SKU (Tabel A) | Model/Type baris padding nomor 04 (#16) | `Fixture.hardwareStock.p16.a[12].modelType` |
  | Device Name baris padding 05 (Tabel A baris 13) | #16 Katalog SKU (Tabel A) | Device Name baris padding nomor 05 (#16) | `Fixture.hardwareStock.p16.a[13].deviceName` |
  | Model/Type baris padding 05 (Tabel A baris 13) | #16 Katalog SKU (Tabel A) | Model/Type baris padding nomor 05 (#16) | `Fixture.hardwareStock.p16.a[13].modelType` |
  | Device Name baris padding 06 (Tabel A baris 14) | #16 Katalog SKU (Tabel A) | Device Name baris padding nomor 06 (#16) | `Fixture.hardwareStock.p16.a[14].deviceName` |
  | Model/Type baris padding 06 (Tabel A baris 14) | #16 Katalog SKU (Tabel A) | Model/Type baris padding nomor 06 (#16) | `Fixture.hardwareStock.p16.a[14].modelType` |
  | Device Name baris padding 07 (Tabel A baris 15) | #16 Katalog SKU (Tabel A) | Device Name baris padding nomor 07 (#16) | `Fixture.hardwareStock.p16.a[15].deviceName` |
  | Model/Type baris padding 07 (Tabel A baris 15) | #16 Katalog SKU (Tabel A) | Model/Type baris padding nomor 07 (#16) | `Fixture.hardwareStock.p16.a[15].modelType` |
  | Device Name baris padding 08 (Tabel A baris 16) | #16 Katalog SKU (Tabel A) | Device Name baris padding nomor 08 (#16) | `Fixture.hardwareStock.p16.a[16].deviceName` |
  | Device Name baris padding 09 (Tabel A baris 17) | #16 Katalog SKU (Tabel A) | Device Name baris padding nomor 09 (#16) | `Fixture.hardwareStock.p16.a[17].deviceName` |
  | SKU baris padding 17 (Tabel A baris 25) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 17 (#16) | `Fixture.hardwareStock.p16.a[25].sku` |
  | SKU baris padding 19 (Tabel A baris 27) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 19 (#16) | `Fixture.hardwareStock.p16.a[27].sku` |
  | SKU baris padding 21 (Tabel A baris 29) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 21 (#16) | `Fixture.hardwareStock.p16.a[29].sku` |
  | SKU baris padding 22 (Tabel A baris 30) | #16 Katalog SKU (Tabel A) | kode SKU baris padding nomor 22 (#16) | `Fixture.hardwareStock.p16.a[30].sku` |
  | Nilai turunan dropdownSearchBrandA1 | turunan dari `Fixture.hardwareStock.p16.a[1].brand` | keyword pencarian internal dropdown Brand: 3 huruf pertama Brand baris 1 Tabel A dalam huruf kecil (`zeb`) | `Fixture.hardwareStock.derived.dropdownSearchBrandA1` |
  | Nilai turunan lastUpdatedA1Date | turunan dari `Fixture.hardwareStock.p16.a[1].lastUpdated` | bagian tanggal (tanpa jam) Last Updated baris 1 Tabel A (`10 Jun 2026`) | `Fixture.hardwareStock.derived.lastUpdatedA1Date` |
  | Nilai turunan lastUpdatedA5Date | turunan dari `Fixture.hardwareStock.p16.a[5].lastUpdated` | bagian tanggal (tanpa jam) Last Updated baris 5 Tabel A (`18 Jun 2026`) | `Fixture.hardwareStock.derived.lastUpdatedA5Date` |
- Data uji TC-AC-ACHS-213 (isi opsi dropdown Filter kelas multi; sumber opsi DISTINCT dari baris tabel):

  | No | Field | Placeholder | Opsi | Jumlah |
  |---|---|---|---|---|
  | 1 | Device Name | `All device names` | `Fixture.hardwareStock.p16.a[5].deviceName`, `Fixture.hardwareStock.p16.a[3].deviceName`, `Fixture.hardwareStock.p16.a[1].deviceName`, `Fixture.hardwareStock.p16.a[9].deviceName`, `Fixture.hardwareStock.p16.a[10].deviceName`, `Fixture.hardwareStock.p16.a[11].deviceName`, `Fixture.hardwareStock.p16.a[12].deviceName`, `Fixture.hardwareStock.p16.a[13].deviceName`, `Fixture.hardwareStock.p16.a[14].deviceName`, `Fixture.hardwareStock.p16.a[15].deviceName`, `Fixture.hardwareStock.p16.a[16].deviceName`, `Fixture.hardwareStock.p16.a[17].deviceName` dan 13 opsi lain | 25 |
  | 2 | Type | `All types` | `BLE Gateway`, `Handheld Reader`, `Smart Fixed Reader` | 3 |
  | 3 | Range Type | `All range types` | `Long Range`, `Short Range` | 2 |
  | 4 | Brand | `All brands` | `Fixture.hardwareStock.p16.a[9].brand`, `Fixture.hardwareStock.p16.a[2].brand`, `Fixture.hardwareStock.p16.a[5].brand`, `Fixture.hardwareStock.p16.a[7].brand`, `Fixture.hardwareStock.p16.a[1].brand` | 5 |
  | 5 | Model/Type | `All model/type` | `Fixture.hardwareStock.p16.a[7].modelType`, `Fixture.hardwareStock.p16.a[2].modelType`, `Fixture.hardwareStock.p16.a[3].modelType`, `Fixture.hardwareStock.p16.a[6].modelType`, `Fixture.hardwareStock.p16.a[8].modelType`, `Fixture.hardwareStock.p16.a[9].modelType`, `Fixture.hardwareStock.p16.a[10].modelType`, `Fixture.hardwareStock.p16.a[11].modelType`, `Fixture.hardwareStock.p16.a[12].modelType`, `Fixture.hardwareStock.p16.a[13].modelType`, `Fixture.hardwareStock.p16.a[14].modelType`, `Fixture.hardwareStock.p16.a[15].modelType` dan 18 opsi lain | 30 |

- Data uji TC-AC-ACHS-214 (Apply kelas multi):

  | No | Field | Nilai | Hasil |
  |---|---|---|---|
  | 1 | Device Name | `Fixture.hardwareStock.p16.a[3].deviceName` | 3 baris: `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[6].sku` |
  | 2 | Type | `Smart Fixed Reader` | 25 baris; lima teratas `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[29].sku`, `Fixture.hardwareStock.p16.a[27].sku`, `Fixture.hardwareStock.p16.a[25].sku` |
  | 3 | Range Type | `Short Range` | 2 baris: `Fixture.hardwareStock.p16.a[1].sku`, `Fixture.hardwareStock.p16.a[2].sku` |
  | 4 | Brand | `Fixture.hardwareStock.p16.a[2].brand` | 3 baris: `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[2].sku`, `Fixture.hardwareStock.p16.a[6].sku` |
  | 5 | Model/Type | `Fixture.hardwareStock.p16.a[1].modelType` | 1 baris: `Fixture.hardwareStock.p16.a[1].sku` |

- Data uji TC-AC-ACHS-215 (Apply kelas range; batas inklusif):

  | No | Field | Min | Max | Hasil |
  |---|---|---|---|---|
  | 1 | Total Registered | `10` | `50` | 16 baris; lima teratas `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku`, `Fixture.hardwareStock.p16.a[2].sku`, `Fixture.hardwareStock.p16.a[29].sku`, `Fixture.hardwareStock.p16.a[27].sku` |
  | 2 | Available | `4` | `34` | 24 baris; lima teratas `Fixture.hardwareStock.p16.a[5].sku`, `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku`, `Fixture.hardwareStock.p16.a[2].sku` |
  | 3 | In Use | `1` | `16` | 3 baris: `Fixture.hardwareStock.p16.a[5].sku`, `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku` |

- Data uji TC-AC-ACHS-216 dan TC-AC-ACHS-259: Last Updated rentang `Fixture.hardwareStock.derived.lastUpdatedA1Date` sampai `Fixture.hardwareStock.derived.lastUpdatedA5Date` (Start tidak sama dengan End; hasil 4 baris `Fixture.hardwareStock.p16.a[5].sku`, `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku`); rentang `01 Jan 2026` sampai `31 Dec 2026` (mencakup seluruh 2026; pilihan spec karena TC hanya menulis "mencakup seluruh 2026").
- Pilihan spec: keyword pencarian internal dropdown pada TC-AC-ACHS-213 adalah `Fixture.hardwareStock.derived.dropdownSearchBrandA1` pada dropdown Brand (3 huruf pertama opsi `Fixture.hardwareStock.p16.a[1].brand`, huruf kecil untuk menguji ketidakpekaan huruf besar kecil) dan `zzqx-tidak-ada` (tanpa kecocokan); rows per page 50 dipilih pada TC-AC-ACHS-259 supaya seluruh hasil berada pada satu halaman.
- Kemampuan teknis (disediakan tim FE): menahan respons opsi dropdown Filter Stock List selama 3 detik (intercept penundaan; TC-AC-ACHS-606) dan melepasnya; intercept hanya di atas backend nyata.
- State global yang diubah: tidak ada yang bertahan (filter dan rows per page direset oleh klik menu sidebar pada langkah 41).
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACHS-212: Screening Filter Panel

1. Arahkan kursor ke icon Filter
2. Verifikasi tooltip `Filter`
3. Klik icon Filter
4. Verifikasi ikon Filter menjadi gelap saat panel terbuka
5. Verifikasi field Filter Panel berurutan sesuai urutan kolom tabel: Device Name (multi-select searchable, placeholder `All device names`), Type (multi-select searchable, placeholder `All types`), Range Type (multi-select searchable, placeholder `All range types`), Brand (multi-select searchable, placeholder `All brands`), Model/Type (multi-select searchable, placeholder `All model/type`), Total Registered (range Min–Max, placeholder `Min / Max`), Available (range Min–Max, placeholder `Min / Max`), In Use (range Min–Max, placeholder `Min / Max`), Last Updated (date range picker, placeholder `Select date`)
6. Verifikasi tombol `[Clear Field]` (kiri) dan `[Apply]` (kanan)
7. Verifikasi tidak ada field Photo atau identifier teks

### TC-AC-ACHS-213: Isi opsi dropdown Filter kelas multi

8. Untuk setiap baris tabel Data uji TC-AC-ACHS-213 (langkah 8 sampai 11): buka dropdown field pada Filter Panel
9. Verifikasi daftar opsi dropdown sesuai kolom "Opsi" dan "Jumlah"
10. Verifikasi kotak pencarian internal ada di dropdown
11. Tutup dropdown
12. Buka dropdown Brand, ketik `Fixture.hardwareStock.derived.dropdownSearchBrandA1` pada kotak pencarian internal
13. Verifikasi daftar opsi menyempit dan memuat `Fixture.hardwareStock.p16.a[1].brand`
14. Ganti isi kotak pencarian internal dengan `zzqx-tidak-ada`
15. Verifikasi tampil teks `No results found` pada dropdown
16. Tutup dropdown Brand

### TC-AC-ACHS-214: Apply kelas multi per field

17. Untuk setiap baris tabel Data uji TC-AC-ACHS-214 (langkah 17 sampai 20): pilih nilai pada dropdown field lalu klik `[Apply]`
18. Verifikasi jumlah baris dan baris sesuai kolom "Hasil"
19. Klik `[Clear Field]`, klik `[Apply]`
20. Verifikasi tabel kembali ke seluruh baris (info `Showing 1–10 of 30 entries`)

### TC-AC-ACHS-215: Apply kelas range per field

21. Untuk setiap baris tabel Data uji TC-AC-ACHS-215 (langkah 21 sampai 24): isi Min dan Max pada field, klik `[Apply]`
22. Verifikasi jumlah baris dan baris sesuai kolom "Hasil"
23. Klik `[Clear Field]`, klik `[Apply]`
24. Verifikasi tabel kembali ke seluruh baris (info `Showing 1–10 of 30 entries`)

### TC-AC-ACHS-216: Apply kelas date

25. Isi field Last Updated dengan rentang `Fixture.hardwareStock.derived.lastUpdatedA1Date` sampai `Fixture.hardwareStock.derived.lastUpdatedA5Date`, klik `[Apply]`
26. Verifikasi tabel menampilkan 4 baris: `Fixture.hardwareStock.p16.a[5].sku`, `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku`
27. Klik `[Clear Field]`, klik `[Apply]`
28. Verifikasi tabel kembali ke seluruh baris (info `Showing 1–10 of 30 entries`)

### TC-AC-ACHS-259: Opsi tanpa nilai kosong dan baris kosong tersaring keluar

29. Buka dropdown Range Type pada Filter Panel
30. Verifikasi dropdown Range Type hanya memuat opsi `Long Range` dan `Short Range` (tanpa opsi untuk nilai kosong)
31. Centang `Short Range` dan `Long Range`, tutup dropdown, klik `[Apply]`
32. Verifikasi baris `Fixture.hardwareStock.p16.a[4].sku` dan `Fixture.hardwareStock.p16.a[1].sku` tampil
33. Verifikasi baris Smart Fixed Reader dan BLE Gateway (Range Type `—`) tidak tampil
34. Klik `[Clear Field]`, klik `[Apply]`
35. Pilih rows per page 50
36. Isi field Last Updated dengan rentang `01 Jan 2026` sampai `31 Dec 2026`, klik `[Apply]`
37. Verifikasi baris `Fixture.hardwareStock.p16.a[8].sku` dan `Fixture.hardwareStock.p16.a[9].sku` tampil
38. Verifikasi baris tanpa aktivitas (Last Updated `—`: `Fixture.hardwareStock.p16.a[6].sku` dan SKU `{sku_pad_NN}` bernomor genap) tidak tampil
39. Klik `[Clear Field]`, klik `[Apply]`, klik icon Filter untuk menutup panel

### TC-AC-ACHS-606: State loading opsi dropdown Filter

40. Aktifkan penahanan respons opsi dropdown Filter Stock List selama 3 detik
41. Buka Hardware > Stock lewat klik menu sidebar
42. Klik icon Filter
43. Buka dropdown Model/Type sebelum respons opsi tiba
44. Verifikasi dropdown Model/Type menampilkan skeleton atau spinner mini
45. Verifikasi dropdown Model/Type tidak kosong tanpa indikator dan tidak menampilkan teks `No options available`
46. Tunggu respons opsi tiba (penahanan 3 detik berakhir) lalu lepas penahanan respons
47. Verifikasi dropdown Model/Type menampilkan 30 opsi
48. Verifikasi indikator loading hilang dan digantikan 30 opsi
49. Tutup dropdown Model/Type, klik icon Filter untuk menutup panel


## Notes

- Sumber TC: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md`. (bagian 4a, Stock List). Seluruh TC sumber spec ini dikerjakan di sini.
- Urutan TC: screening (212, 213), Apply per field (214, 215, 216, 259), lalu TC-AC-ACHS-606 paling akhir karena membuka ulang halaman lewat menu sidebar dengan respons ditahan (state UI, bukan kegagalan yang dipaksa; bagian 3 prinsip 13 kelas b). Penahanan respons dilepas pada langkah "lepas penahanan respons" (S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`): penutupan dropdown (langkah 11), `[Clear Field]` lalu `[Apply]` antar-iterasi dan antar-TC, rows per page 50 pada TC-AC-ACHS-259 (anchor posisi: seluruh hasil berada pada satu halaman sehingga asersi absence bermakna, S-14), penutupan panel Filter, dan pembukaan Hardware > Stock lewat sidebar (langkah 41, mereset rows per page).
- Langkah 8 sampai 11, 17 sampai 20, dan 21 sampai 24 berulang untuk setiap baris tabel Data uji (lima, lima, dan tiga iterasi; bagian 8b butir 7).
- Asersi tambahan (S-03): pada TC-AC-ACHS-259 baris `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku`, `Fixture.hardwareStock.p16.a[8].sku`, dan `Fixture.hardwareStock.p16.a[9].sku` adalah anchor positif sebelum asersi absence.
- Spec memiliki 49 langkah nominal dan 89 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Filter Stock List pada akun dan dataset read-only yang sama), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari tiga perulangan per field tanpa langkah bersyarat.
- Temuan untuk QA:
  - TC-AC-ACHS-213 Expected tidak menyebut kata kunci pencarian internal; spec memilih `Fixture.hardwareStock.derived.dropdownSearchBrandA1` pada Brand dan `zzqx-tidak-ada` (pilihan spec). Daftar opsi Device Name dan Model/Type dipotong oleh TC ("dan 13 opsi lain", "dan 18 opsi lain"); spec mengasersi jumlah total dan opsi yang disebut.
  - TC-AC-ACHS-259 menyebut "date range Last Updated yang mencakup seluruh 2026" tanpa nilai; spec memilih `01 Jan 2026` sampai `31 Dec 2026` dan menambah rows per page 50 sebagai penghubung.
  - TC-AC-ACHS-606 tidak menyebut cara melepas penahanan respons selain "tunggu response tiba"; durasi 3 detik adalah nilai TC, bukan aturan PRD.
