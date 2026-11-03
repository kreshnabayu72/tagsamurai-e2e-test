---
id: TC-AC-ACHS-E2E-240-isi-sel-stock-list-badge-hitungan-link-sku-dan-placeholder-foto
title: "Isi Sel Stock List: Badge, Hitungan, Link SKU, dan Placeholder Foto"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-3
  - TC-AC-ACHS-4
  - TC-AC-ACHS-5
  - TC-AC-ACHS-6
  - TC-AC-ACHS-7
  - TC-AC-ACHS-8
  - TC-AC-ACHS-9
  - TC-AC-ACHS-11
  - TC-AC-ACHS-599
  - TC-AC-ACHS-605
  - TC-AC-ACHS-609
coverage:
  web: automated
---

# Isi Sel Stock List: Badge, Hitungan, Link SKU, dan Placeholder Foto

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup No 1; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca): Katalog SKU 30 baris Stock List (No 16, Tabel A), SKU `{skuLong}` dengan 18 Available, 7 In Use, dan 1 Waiting for Approval (No 17, 18), SKU `{skuIx4}` yang belum pernah Add Stock. Tenant dalam keadaan baseline Pre-setup; suite menjalankan spec baca sebelum spec yang mengubah baseline (lihat suite.md).
- Data seed sesaat milik spec (Pre-setup No 16f, 16g, 16i; bukan bagian 30 baris baseline; S-06): dimuat hook `before` spec ini dan dihapus hook `after` (idempotent, dilewati bila sudah tidak ada); kode SKU seed = nilai kunci fixture + sufiks `-{runId}-240` (S-12); kemampuan seeding lewat API atau DB disediakan tim FE/BE:
  - `{skuLongText}` (No 16f): Smart Fixed Reader dengan Device Name 106 karakter.
  - `{skuNoPhoto}` (No 16g): Smart Fixed Reader tanpa foto (form Settings > Device > SKU mewajibkan foto, sehingga dimuat lewat seed).
  - `{skuBrokenPhoto}` (No 16i): Smart Fixed Reader dengan foto berupa URL gambar yang tidak dapat dimuat (respons 404).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuTc52}` | #16 Tabel A baris 1; #19 | kode SKU Handheld Reader Short Range, Total Registered 50 (34 Available, 16 In Use) | `Fixture.hardwareStock.p16.a[1].sku` |
| `{deviceNameHandheld}` | #16 Tabel A baris 1 | Device Name yang dimiliki bersama baris 2 dan 4 (Handheld Scanner) | `Fixture.hardwareStock.p16.a[1].deviceName` |
| `{skuEda51}` | #16 Tabel A baris 2 | kode SKU Handheld Reader Short Range, 12 Available | `Fixture.hardwareStock.p16.a[2].sku` |
| `{skuFx}` | #16 Tabel A baris 3; #27 | kode SKU Smart Fixed Reader, 8 Available | `Fixture.hardwareStock.p16.a[3].sku` |
| `{modelFx}` | #16 Tabel A baris 3 | Model/Type SKU Smart Fixed Reader | `Fixture.hardwareStock.p16.a[3].modelType` |
| `{skuLong}` | #16 Tabel A baris 4; #17; #18 | kode SKU Handheld Reader Long Range, Total Registered 25 (18 Available, 7 In Use) dan 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `{skuBle}` | #16 Tabel A baris 5; #27 | kode SKU BLE Gateway, 4 Available dan 1 In Use, Brand dan Model/Type 25 karakter atau kurang | `Fixture.hardwareStock.p16.a[5].sku` |
| `{brandBle}` | #16 Tabel A baris 5 | Brand SKU BLE Gateway | `Fixture.hardwareStock.p16.a[5].brand` |
| `{modelBle}` | #16 Tabel A baris 5 | Model/Type SKU BLE Gateway | `Fixture.hardwareStock.p16.a[5].modelType` |
| `{skuIx4}` | #16 Tabel A baris 6 | kode SKU Smart Fixed Reader tanpa unit (Total Registered 0, Last Updated `—`) | `Fixture.hardwareStock.p16.a[6].sku` |
| `{deviceNameIx4}` | #16 Tabel A baris 6 | Device Name SKU Smart Fixed Reader tanpa unit | `Fixture.hardwareStock.p16.a[6].deviceName` |
| `{brandIx4}` | #16 Tabel A baris 6 | Brand SKU Smart Fixed Reader tanpa unit | `Fixture.hardwareStock.p16.a[6].brand` |
| `{modelIx4}` | #16 Tabel A baris 6 | Model/Type SKU Smart Fixed Reader tanpa unit | `Fixture.hardwareStock.p16.a[6].modelType` |
| `{skuBleLong}` | #16 Tabel A baris 7 | kode SKU BLE Gateway, Total Registered 3, Brand dan Model/Type lebih dari 25 karakter | `Fixture.hardwareStock.p16.a[7].sku` |
| `{brandBleLong}` | #16 Tabel A baris 7 | Brand lebih dari 25 karakter | `Fixture.hardwareStock.p16.a[7].brand` |
| `{modelBleLong}` | #16 Tabel A baris 7 | Model/Type lebih dari 25 karakter | `Fixture.hardwareStock.p16.a[7].modelType` |
| `{skuLongText}` | #16f (seed sesaat) | kode SKU Smart Fixed Reader dengan Device Name 106 karakter | `Fixture.hardwareStock.p16f.sku` |
| `{deviceNameLongText}` | #16f (seed sesaat) | Device Name 106 karakter | `Fixture.hardwareStock.p16f.deviceName` |
| `{skuNoPhoto}` | #16g (seed sesaat) | kode SKU Smart Fixed Reader tanpa foto | `Fixture.hardwareStock.p16g.sku` |
| `{modelNoPhoto}` | #16g (seed sesaat) | Model/Type SKU tanpa foto | `Fixture.hardwareStock.p16g.modelType` |
| `{skuBrokenPhoto}` | #16i (seed sesaat) | kode SKU Smart Fixed Reader dengan foto URL 404 | `Fixture.hardwareStock.p16i.sku` |

- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACHS-3: Badge Type tampil penuh dengan hover nama penuh

1. Ketik Search `Reader`, tekan Enter
2. Verifikasi badge Type `Handheld Reader` tampil penuh tanpa pemotongan `..`
3. Verifikasi badge Type `Smart Fixed Reader` tampil penuh tanpa pemotongan `..`
4. Hover badge Type `Handheld Reader`
5. Verifikasi hover menampilkan nama penuh `Handheld Reader`
6. Hover badge Type `Smart Fixed Reader`
7. Verifikasi hover menampilkan nama penuh `Smart Fixed Reader`
8. Verifikasi tidak ada nilai `Tablet` atau `GPS Tracker` pada kolom Type hasil pencarian
9. Ganti isi kotak search dengan `BLE Gateway`, tekan Enter
10. Verifikasi badge Type `BLE Gateway` tampil penuh tanpa pemotongan `..`
11. Hover badge Type `BLE Gateway`
12. Verifikasi hover menampilkan nama penuh `BLE Gateway`
13. Verifikasi tidak ada nilai `Tablet` atau `GPS Tracker` pada kolom Type hasil pencarian

### TC-AC-ACHS-4: Badge Brand dan Model/Type 25 karakter atau kurang tampil penuh

14. Ganti isi kotak search dengan Brand `{brandBle}`, tekan Enter
15. Verifikasi sel Brand baris `{skuBle}` tampil penuh sebagai badge dark dengan teks Brand `{brandBle}`
16. Verifikasi sel Model/Type baris `{skuBle}` tampil penuh sebagai badge dark dengan teks Model/Type `{modelBle}`
17. Hover badge Brand
18. Verifikasi hover menampilkan nama Brand penuh `{brandBle}`
19. Hover badge Model/Type
20. Verifikasi hover menampilkan nama Model/Type penuh `{modelBle}`

### TC-AC-ACHS-5: Badge lebih dari 25 karakter terpotong 12 + .. + 12

21. Ganti isi kotak search dengan SKU `{skuBleLong}`, tekan Enter
22. Verifikasi sel Brand baris `{skuBleLong}` tampil 12 karakter pertama nama Brand `{brandBleLong}`, lalu `..`, lalu 12 karakter terakhirnya
23. Verifikasi sel Model/Type baris `{skuBleLong}` tampil 12 karakter pertama nama Model/Type `{modelBleLong}`, lalu `..`, lalu 12 karakter terakhirnya, sebagai badge dark
24. Hover badge Brand
25. Verifikasi hover menampilkan nama Brand penuh `{brandBleLong}`
26. Hover badge Model/Type
27. Verifikasi hover menampilkan nama Model/Type penuh `{modelBleLong}`

### TC-AC-ACHS-6: Kolom Range Type

28. Klik `(←)` pada kotak Search
29. Verifikasi sel Range Type baris `{skuTc52}` tampil `Short Range`
30. Verifikasi sel Range Type baris `{skuLong}` tampil `Long Range`
31. Verifikasi sel Range Type baris `{skuFx}` dan `{skuBle}` tampil `—`

### TC-AC-ACHS-7: SKU baru tanpa aktivitas tampil dengan hitungan 0 dan Last Updated `—`

32. Ketik Search Model/Type `{modelIx4}`, tekan Enter
33. Verifikasi baris `{skuIx4}` tampil dengan Device Name `{deviceNameIx4}`, Brand `{brandIx4}`, Model/Type `{modelIx4}`, Type `Smart Fixed Reader`, Range Type `—`
34. Verifikasi Total Registered `0`, Available `0`, In Use `0`
35. Verifikasi Last Updated `—`

### TC-AC-ACHS-8: Total Registered = Available + In Use, Waiting for Approval tidak dihitung

36. Ganti isi kotak search dengan SKU `{skuLong}`, tekan Enter
37. Verifikasi baris `{skuLong}` tampil dengan Total Registered `25`, Available `18`, In Use `7` (25 = 18 + 7)
38. Verifikasi angka In Use tampil tebal berwarna hijau (success)
39. Klik `(⋯)` pada baris `{skuLong}`, klik row action `Detail`
40. Verifikasi Summary bar Stock Detail menampilkan angka yang sama `25`, `18`, `7`
41. Verifikasi Tab Available menampilkan 19 baris (18 Available + 1 Waiting for Approval) dengan info `Showing 1–10 of 19 entries`
42. Verifikasi Total Registered Summary bar tetap `25` sehingga tidak menghitung baris Waiting for Approval

### TC-AC-ACHS-9: SKU sebagai link, Device Name bukan link, klik area baris tidak berefek

43. Klik segmen breadcrumb `Stock`
44. Klik `(←)` pada kotak Search
45. Hover teks SKU `{skuFx}`
46. Verifikasi warna teks SKU berubah menjadi warna primary Admin Console
47. Verifikasi teks SKU saat hover tanpa garis bawah
48. Klik teks SKU `{skuFx}`
49. Verifikasi Stock Detail SKU `{skuFx}` terbuka di halaman yang sama dengan Breadcrumb `Hardware > Stock > Detail`
50. Verifikasi Tab Available aktif
51. Klik segmen breadcrumb `Stock`
52. Klik teks Device Name pada baris `{skuFx}`
53. Verifikasi klik Device Name tidak memicu navigasi (halaman tetap Hardware > Stock)
54. Verifikasi klik Device Name tidak mengubah tampilan
55. Klik area kosong di sel Brand baris `{skuFx}`
56. Verifikasi klik area baris tidak memicu navigasi (halaman tetap Hardware > Stock)
57. Verifikasi klik area baris tidak mengubah tampilan

### TC-AC-ACHS-11: Device Name yang sama pada beberapa SKU tampil sebagai baris terpisah

58. Ketik Search Device Name `{deviceNameHandheld}`, tekan Enter
59. Verifikasi tiga baris Device Name `{deviceNameHandheld}` tampil berurutan `{skuLong}`, `{skuTc52}`, `{skuEda51}` (urutan default Last Updated)
60. Verifikasi sedikitnya satu baris tampil
61. Verifikasi setiap baris memiliki SKU unik

### TC-AC-ACHS-599: Flat text Device Name panjang tampil utuh

62. Klik menu Hardware > Stock di sidebar
63. Ketik Search SKU `{skuLongText}`, tekan Enter
64. Verifikasi Device Name `{deviceNameLongText}` tampil utuh sebanyak 106 karakter tanpa pemotongan `..`
65. Hover Device Name pada baris hasil
66. Verifikasi tidak ada tooltip pemotong
67. Verifikasi kolom Device Name melebar mengikuti konten (hug content)
68. Verifikasi header kolom `Photo`, `Device Name`, `SKU`, `Type`, `Range Type`, `Brand`, `Model/Type`, `Total Registered`, `Available`, `In Use`, dan `Last Updated` tetap satu baris (tidak wrap)
69. Verifikasi badge Brand baris `{skuLongText}` dan kolom angka pada baris hasil tetap satu baris

### TC-AC-ACHS-605: Placeholder foto untuk SKU tanpa foto

70. Klik menu Hardware > Stock di sidebar
71. Ketik Search Model/Type `{modelFx}`, tekan Enter
72. Catat ukuran sel Photo baris `{skuFx}`
73. Ganti isi kotak search dengan Model/Type `{modelNoPhoto}`, tekan Enter
74. Verifikasi sel Photo baris `{skuNoPhoto}` menampilkan placeholder foto (komponen `Image` varian `Default Placeholder`) dengan ukuran dan bentuk sama dengan thumbnail yang dicatat pada langkah 72
75. Verifikasi sel Photo baris `{skuNoPhoto}` tidak berisi teks `—` dan tidak kosong
76. Klik row action `Detail` pada baris `{skuNoPhoto}`
77. Verifikasi SKU Info Header Stock Detail menampilkan placeholder foto yang sama
78. Klik segmen breadcrumb `Stock`
79. Klik `(⋯)` pada baris `{skuNoPhoto}`, klik opsi `Add Stock`
80. Verifikasi SKU Info Card halaman Add Stock menampilkan placeholder foto yang sama
81. Klik `[Cancel]` pada halaman Add Stock

### TC-AC-ACHS-609: Placeholder foto untuk foto yang gagal dimuat

82. Klik menu Hardware > Stock di sidebar
83. Ketik Search Model/Type `{modelFx}`, tekan Enter
84. Catat ukuran sel Photo baris `{skuFx}`
85. Ganti isi kotak search dengan SKU `{skuBrokenPhoto}`, tekan Enter
86. Verifikasi sel Photo baris `{skuBrokenPhoto}` menampilkan placeholder foto (komponen `Image` varian `Default Placeholder`) dengan ukuran dan bentuk sama dengan thumbnail yang dicatat pada langkah 84
87. Verifikasi sel Photo baris `{skuBrokenPhoto}` tidak berisi teks `—` dan tidak kosong
88. Klik row action `Detail` pada baris `{skuBrokenPhoto}`
89. Verifikasi SKU Info Header Stock Detail menampilkan placeholder foto yang sama
90. Klik segmen breadcrumb `Stock`
91. Klik `(⋯)` pada baris `{skuBrokenPhoto}`, klik opsi `Add Stock`
92. Verifikasi SKU Info Card halaman Add Stock menampilkan placeholder foto yang sama
93. Klik `[Cancel]` pada halaman Add Stock

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-3, 4, 5, 6, 7, 8, 9, 11, 599, 605, 609). Tidak ada TC hanya-BE di spec ini.
- TC-605 dan TC-609 masing-masing mencakup tiga surface (Stock List, Stock Detail, Add Stock) dan tetap satu spec dengan langkah per surface (langkah 74 sampai 80 dan 86 sampai 92).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 28 dan 44 (mereset Search), langkah 43, 51, 78, dan 90 (kembali ke Stock List lewat breadcrumb), langkah 62, 70, dan 82 (menyegarkan Stock List lewat menu sidebar), langkah 72 dan 84 (mencatat ukuran thumbnail pembanding), langkah 81 dan 93 (`[Cancel]` pada halaman Add Stock yang masih kosong sehingga dialog Unsaved Changes tidak muncul). SKU seed sesaat dimuat hook `before` dan dihapus hook `after` (lihat Prerequisites), bukan langkah.
- Cara memicu foto gagal dimuat (TC-609): SKU seed `{skuBrokenPhoto}` (No 16i) dengan URL foto 404 (disediakan tim FE/BE); P-2 tidak dipakai karena pemicunya adalah data seed, bukan intercept.
- Spec di atas smell 35 langkah (93 langkah). Alasan: semua blok adalah asersi isi sel dan tampilan satu layar Stock List pada Population Katalog SKU yang sama, kesebelas TC berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; SKU seed sesaat dimuat hook `before` dan tidak mengubah asersi TC lain karena tiap TC mencari baris lewat Search atau kode SKU yang tidak mencocokkan SKU seed, atau membandingkan baris spesifik.
- Konfirmasi kata kunci Search (S-12): kata kunci Search yang memakai nilai penuh kolom dibandingkan dengan nilai pada tabel Pre-setup TC (Tabel A dan butir 16f, 16g, 16i) dan himpunan hasilnya sama dengan substring pada TC asli. TC-4 `Kontakt` menjadi Brand `{brandBle}`: hanya baris 5 Tabel A. TC-5 `LONGNAME` menjadi SKU `{skuBleLong}`: hanya baris 7. TC-7 `IX4` menjadi Model/Type `{modelIx4}`: nilainya identik, hanya baris 6. TC-11 `Handheld Scanner` menjadi Device Name `{deviceNameHandheld}`: identik, tiga baris (baris 1, 2, 4). TC-599 `LONGTXT` menjadi SKU `{skuLongText}`: hanya SKU seed 16f. TC-605 `FX9600` menjadi Model/Type `{modelFx}`: identik, hanya baris 3; `NOPHOTO` menjadi Model/Type `{modelNoPhoto}`: hanya SKU seed 16g. TC-609 `BROKENPHOTO` menjadi SKU `{skuBrokenPhoto}`: hanya SKU seed 16i. Tidak ada perbedaan hasil.
- Temuan untuk QA:
  - TC-4 dan TC-5 menyebut ambang 25 karakter; nilai ambang berasal dari NC-05 dan `prd-conventions.md §9.14`, bukan dari baris PRD modul. Nilai 12 + `..` + 12 diasersi persis sesuai Expected TC-5.
  - TC-599 Expected a ("tanpa tooltip pemotong") tidak punya langkah hover di Langkah Uji; spec menambah satu hover pada Device Name (langkah 65). Frasa "hug content" pada Expected b tidak mendefinisikan cara ukur; spec mengasersi seluruh 106 karakter terlihat tanpa pemotongan.
  - TC-605 dan TC-609 mensyaratkan ukuran sel Photo FX9600 sebagai pembanding tanpa menyebut toleransi atau cara ukur; spec membandingkan lebar dan tinggi sel yang dicatat.
  - TC-609 tidak menyebut cara memicu foto gagal dimuat selain Pre-setup No 16i (URL 404 lewat seed API atau DB); mekanisme seeding diminta dari tim FE/BE.
  - TC-7 menyebut SKU `{skuIx4}` "baru diregister" padahal sudah menjadi bagian Population Tabel A; spec memakai SKU Pre-setup tanpa membuatnya. Spec Add Stock yang menambah unit `{skuIx4}` (TC-AC-ACHS-600) harus berjalan sesudah spec baca.
  - Population Katalog SKU tidak ditulis literal: spec merujuk Pre-setup lewat tabel Parameter Pre-setup di Prerequisites sehingga tidak memerlukan pengecualian S-12. Teks truncation badge (TC-5) diasersi sebagai aturan 12 + `..` + 12 atas nilai Tabel A; teks Type (`Handheld Reader`, `Smart Fixed Reader`, `BLE Gateway`, `Tablet`, `GPS Tracker`) adalah salinan UI dan dipertahankan.
