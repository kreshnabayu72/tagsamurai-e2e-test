---
id: TC-AC-ACHS-E2E-007-screening-stock-detail-tab-available-semua-tipe-sku
title: "Screening Stock Detail Tab Available untuk Semua Tipe SKU"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-30
  - TC-AC-ACHS-31
  - TC-AC-ACHS-32
  - TC-AC-ACHS-33
  - TC-AC-ACHS-34
  - TC-AC-ACHS-35
  - TC-AC-ACHS-36
coverage:
  web: automated
---

# Screening Stock Detail Tab Available untuk Semua Tipe SKU

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `{Fixture.hardwareStock.account.p01.totalControl.email}` (Pre-setup No 1; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca): Katalog SKU 30 baris (No 16, Tabel A); SKU `{Fixture.hardwareStock.p16.a[4].sku}` (Long Range, 25 | 18 | 7) dengan 18 unit Available N = 10 sampai 27, satu unit Waiting for Approval N = 28 `{Fixture.hardwareStock.p17.e[28].deviceName}` (Subject Register Duplicate pending), satu unit Rejected `{Fixture.hardwareStock.p17.rejectedSerial}`, unit nomor 8 dan 9 pernah dihapus (No 17, Tabel E); 7 unit In Use (No 18); SKU `{Fixture.hardwareStock.p16.a[1].sku}` (Short Range, 50 | 34 | 16, No 19); SKU `{Fixture.hardwareStock.p16.a[3].sku}` (Smart Fixed Reader) dan `{Fixture.hardwareStock.p16.a[5].sku}` (BLE Gateway). Tenant dalam keadaan baseline Pre-setup; suite menjalankan spec baca sebelum spec yang mengubah baseline (lihat suite.md).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<kunci>`, identitas data bukan rahasia; berkas fixture belum ada dan dibuat tim FE/BE dari tabel Data Uji Pre-setup TC; nilai tidak ditulis ulang di spec ini):

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | `{Fixture.hardwareStock.account.p01.totalControl.email}` | No 1 | email akun Pre-setup No 1 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | `{Fixture.hardwareStock.p16.a[4].sku}` | No 16, 17, 18, Tabel A baris 4 | kode SKU Handheld Reader Long Range (25 Total Registered: 18 Available, 7 In Use) | `Fixture.hardwareStock.p16.a[4].sku` |
  | `{Fixture.hardwareStock.p16.a[4].deviceName}` | No 16, Tabel A baris 4 | Device Name SKU Handheld Reader Long Range | `Fixture.hardwareStock.p16.a[4].deviceName` |
  | `{Fixture.hardwareStock.p16.a[4].brand}` | No 16, Tabel A baris 4 | Brand SKU Handheld Reader Long Range (kata kunci Search dan opsi Filter) | `Fixture.hardwareStock.p16.a[4].brand` |
  | `{Fixture.hardwareStock.p16.a[4].modelType}` | No 16, Tabel A baris 4 | Model/Type SKU Handheld Reader Long Range | `Fixture.hardwareStock.p16.a[4].modelType` |
  | `{Fixture.hardwareStock.p16.a[1].sku}` | No 16, 19, Tabel A baris 1 | kode SKU Handheld Reader Short Range (50 Total Registered: 34 Available, 16 In Use) | `Fixture.hardwareStock.p16.a[1].sku` |
  | `{Fixture.hardwareStock.p16.a[3].sku}` | No 16, 27, Tabel A baris 3 | kode SKU Smart Fixed Reader (8 Total Registered, 8 Available, 0 In Use) | `Fixture.hardwareStock.p16.a[3].sku` |
  | `{Fixture.hardwareStock.p16.a[5].sku}` | No 16, 27, Tabel A baris 5 | kode SKU BLE Gateway (4 Available, 1 In Use) | `Fixture.hardwareStock.p16.a[5].sku` |
  | `{Fixture.hardwareStock.p17.e[10].deviceName}` | No 17, Tabel E baris N = 10 | Device Name unit Available SKU Long Range dengan N terkecil (N = 10) | `Fixture.hardwareStock.p17.e[10].deviceName` |
  | `{Fixture.hardwareStock.p17.e[28].deviceName}` | No 17, Tabel E baris N = 28 | Device Name unit Waiting for Approval SKU Long Range (N = 28; Current Power `—`) | `Fixture.hardwareStock.p17.e[28].deviceName` |
  | `{Fixture.hardwareStock.p17.rejectedSerial}` | No 17 | Serial Number unit Rejected SKU Long Range (tidak tampil di tab manapun; bukan baris Tabel E) | `Fixture.hardwareStock.p17.rejectedSerial` |
  | `{Fixture.hardwareStock.account.p01.totalControl.shortName}` | No 1 | singkatan tampil `[Nama Depan] [Inisial]` user akun Total Control | `Fixture.hardwareStock.account.p01.totalControl.shortName` |
  | `{Fixture.hardwareStock.account.p10.distributorCakra.shortName}` | No 10 | singkatan tampil user Distributor No 10 | `Fixture.hardwareStock.account.p10.distributorCakra.shortName` |
  | `{Fixture.hardwareStock.account.p11.distributorMitra.shortName}` | No 11 | singkatan tampil user Distributor No 11 | `Fixture.hardwareStock.account.p11.distributorMitra.shortName` |
  | `{Fixture.hardwareStock.account.p11.distributorMitra.fullName}` | No 11 | nama lengkap user Distributor No 11 (tampil pada hover) | `Fixture.hardwareStock.account.p11.distributorMitra.fullName` |

- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACHS-30: Screening Tab Available SKU Handheld Reader Long Range

1. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
2. Verifikasi Breadcrumb `Hardware > Stock > Detail`
3. Verifikasi segmen tengah `Stock` bisa diklik, sedangkan `Hardware` dan `Detail` statis
4. Verifikasi SKU Info Header memuat Photo, Device Name `{Fixture.hardwareStock.p16.a[4].deviceName}` dan SKU `{Fixture.hardwareStock.p16.a[4].sku}`, badge `Handheld Reader`, Range Type `Long Range`, Brand `{Fixture.hardwareStock.p16.a[4].brand}`, serta Model/Type `{Fixture.hardwareStock.p16.a[4].modelType}`
5. Verifikasi Summary bar `Total Registered 25 | Available 18 | In Use 7`
6. Verifikasi angka In Use berwarna success
7. Verifikasi Tabs `Available (aktif) | In Use`
8. Verifikasi Banner Waiting for Approval tampil di atas toolbar
9. Verifikasi Table Tools `Search | Filter | Download | Event Log | Add Stock`
10. Verifikasi kolom `Device Name (sortable) | Serial Number (sortable) | Status (sortable) | Registered At (sortable) | Registered By (sortable) | Min Power (sortable) | Max Power (sortable) | Current Power (sortable) | Column Visibility (⋯) (unsortable)`
11. Verifikasi baris unit tampil dengan Device Name berformat `{Fixture.hardwareStock.p16.a[4].deviceName} - [N]`
12. Verifikasi pagination default 10 baris per halaman
13. Verifikasi info pagination `Showing 1–10 of 19 entries`

### TC-AC-ACHS-31: Screening Tab Available SKU Short Range tanpa kolom Power

14. Klik segmen breadcrumb `Stock`
15. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[1].sku}`, klik row action `Detail`
16. Verifikasi Breadcrumb `Hardware > Stock > Detail`
17. Verifikasi SKU Info Header memuat Range Type `Short Range`
18. Verifikasi Summary bar `Total Registered 50 | Available 34 | In Use 16`
19. Verifikasi kolom `Device Name | Serial Number | Status | Registered At | Registered By | Column Visibility (⋯)`
20. Verifikasi kolom `Min Power`, `Max Power`, dan `Current Power` tidak dirender sama sekali (bukan kolom kosong atau `—`)
21. Verifikasi pagination default 10 baris per halaman

### TC-AC-ACHS-32: Screening SKU Smart Fixed Reader dan BLE Gateway tanpa Range Type dan tanpa kolom Power

22. Klik segmen breadcrumb `Stock`
23. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[3].sku}`, klik row action `Detail`
24. Verifikasi SKU Info Header `{Fixture.hardwareStock.p16.a[3].sku}` tanpa baris Range Type
25. Verifikasi SKU Info Header menampilkan badge tipe `Smart Fixed Reader`
26. Verifikasi kolom Power tidak dirender
27. Klik segmen breadcrumb `Stock`
28. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[5].sku}`, klik row action `Detail`
29. Verifikasi SKU Info Header `{Fixture.hardwareStock.p16.a[5].sku}` tanpa baris Range Type
30. Verifikasi SKU Info Header menampilkan badge tipe `BLE Gateway`
31. Verifikasi kolom Power tidak dirender

### TC-AC-ACHS-33: Isi sel Tab Available

32. Klik segmen breadcrumb `Stock`
33. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
34. Ganti rows per page ke `25`
35. Verifikasi Device Name berformat `{Fixture.hardwareStock.p16.a[4].deviceName} - [N]` dengan N unik: N = 10 sampai 27 (18 unit Available) dan N = 28 (`{Fixture.hardwareStock.p17.e[28].deviceName}`)
36. Verifikasi tidak ada baris dengan N = 8 maupun N = 9
37. Verifikasi Registered By tampil `{Fixture.hardwareStock.account.p10.distributorCakra.shortName}`, `{Fixture.hardwareStock.account.p11.distributorMitra.shortName}`, `{Fixture.hardwareStock.account.p01.totalControl.shortName}`
38. Hover nilai Registered By `{Fixture.hardwareStock.account.p11.distributorMitra.shortName}`
39. Verifikasi hover menampilkan nama lengkap `{Fixture.hardwareStock.account.p11.distributorMitra.fullName}`
40. Verifikasi Min Power `-20 dBm` dan Max Power `30 dBm`
41. Verifikasi Current Power berisi `dBm` pada tiap baris berstatus Available
42. Hover sel Current Power baris `{Fixture.hardwareStock.p17.e[28].deviceName}`
43. Verifikasi Current Power baris `{Fixture.hardwareStock.p17.e[28].deviceName}` tampil `—`

### TC-AC-ACHS-34: Badge Status Tab Available

44. Verifikasi badge `Available` severity success pada baris unit Available
45. Verifikasi baris `{Fixture.hardwareStock.p17.e[28].deviceName}` menampilkan badge `Waiting for Approval` severity warning
46. Ketik Search Serial Number `{Fixture.hardwareStock.p17.rejectedSerial}`, tekan Enter
47. Verifikasi Tab Available menampilkan empty state `No results found`
48. Klik Tab `In Use`
49. Ketik Search Serial Number `{Fixture.hardwareStock.p17.rejectedSerial}`, tekan Enter
50. Verifikasi Tab In Use menampilkan empty state `No results found`
51. Klik `(←)` pada kotak Search Tab In Use
52. Klik Tab `Available`
53. Klik `(←)` pada kotak Search Tab Available

### TC-AC-ACHS-35: Row action Tab Available

54. Ketik Search Device Name `{Fixture.hardwareStock.p17.e[10].deviceName}`, tekan Enter
55. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p17.e[10].deviceName}`
56. Verifikasi overlay berisi `Hardware Log` lalu `Delete` berurutan
57. Verifikasi opsi `Delete` berikon merah (danger)
58. Verifikasi tidak ada opsi `Edit` pada overlay unit Available
59. Tutup overlay dengan `Esc`
60. Ganti isi kotak search dengan Device Name `{Fixture.hardwareStock.p17.e[28].deviceName}`, tekan Enter
61. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p17.e[28].deviceName}`
62. Verifikasi overlay unit Waiting for Approval hanya berisi `Hardware Log`
63. Verifikasi opsi `Delete` Hidden pada overlay unit Waiting for Approval
64. Verifikasi tidak ada opsi `Edit` pada overlay unit Waiting for Approval
65. Tutup overlay dengan `Esc`
66. Klik `(←)` pada kotak Search

### TC-AC-ACHS-36: Icon Event Log dan tombol Add Stock hanya di toolbar Tab Available

67. Verifikasi toolbar Tab Available `Search | Filter | Download | Event Log | Add Stock`
68. Klik Tab `In Use`
69. Verifikasi toolbar Tab In Use `Search | Filter | Download`
70. Verifikasi toolbar Tab In Use tanpa `[Event Log]` dan tanpa `[Add Stock]`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-30, 31, 32, 33, 34, 35, 36). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 14, 22, 27, dan 32 (kembali ke Stock List lewat breadcrumb), langkah 34 (menampilkan seluruh 19 unit pada satu halaman agar asersi absence N = 8 dan N = 9 bermakna dengan anchor baris N = 10 pada langkah 35), langkah 51, 52, 53, 59, 65, dan 66 (membersihkan Search dan menutup overlay, S-09). Search pada langkah 54 dan 60 menemukan baris target (R-16). TC-34 dan TC-33 memakai sesi Stock Detail yang sama dengan TC-30 sampai TC-32 tanpa membuka ulang halaman yang tidak diuji.
- Spec di atas smell 35 langkah (70 langkah). Alasan: seluruh blok adalah screening Stock Detail Tab Available dari SKU yang sama atau SKU pembanding, ketujuh TC berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-34 Expected c ("unit Rejected tidak tampil di tab manapun") hanya memuat langkah Search di Tab Available; spec juga mencari Serial Number `{Fixture.hardwareStock.p17.rejectedSerial}` di Tab In Use (langkah 48 sampai 50) agar klausa "tab manapun" teramati.
  - TC-33 langkah 5 (hover sel Current Power unit Waiting for Approval) tidak punya Expected untuk hover; spec hanya mengasersi nilai `—` pada langkah 43.
  - TC-30 Expected a.v ("Banner Waiting for Approval di atas toolbar") tidak menyebut teks banner; teks diasersi di spec banner (spec 008).
  - Population Stock tidak ditulis literal: spec merujuk Pre-setup lewat tabel Parameter Pre-setup di Prerequisites (nilai persis dari Tabel A dan E TC) sehingga tidak memerlukan pengecualian S-12. Nilai numerik (N, hitungan, dBm) dan teks UI (nama kolom, badge, Type) dipertahankan.
  - Perbandingan kata kunci Search terhadap substring TC (S-12): Serial Number `000077` (TC-34) dan nilai penuh `SN-ZEBRA-RFD40-000077`: hasil sama (empty state `No results found`, unit Rejected tidak tampil). Search Device Name unit (langkah 54, 60) adalah Search penghubung, bukan penggantian substring TC; `Handheld Scanner - 10` dan `Handheld Scanner - 28` masing-masing hanya cocok dengan satu unit. Tidak ada perbedaan hasil.
