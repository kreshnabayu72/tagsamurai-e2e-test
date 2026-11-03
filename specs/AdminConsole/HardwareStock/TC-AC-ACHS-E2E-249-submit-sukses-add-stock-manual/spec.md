---
id: TC-AC-ACHS-E2E-249-submit-sukses-add-stock-manual
title: "Submit Sukses Add Stock Manual"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-80
  - TC-AC-ACHS-81
  - TC-AC-ACHS-82
  - TC-AC-ACHS-83
  - TC-AC-ACHS-93
  - TC-AC-ACHS-94
  - TC-AC-ACHS-95
  - TC-AC-ACHS-600
coverage:
  web: automated
---

# Submit Sukses Add Stock Manual

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1; `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip halaman Stock List, sesi API aktor, seeding Population Stock Pre-setup #16 s.d. #20 dan #27. Suite serial (`parallel: false`).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuFx}` | #16 Tabel A baris 3; #27 | kode SKU Smart Fixed Reader, 8 Available | `Fixture.hardwareStock.p16.a[3].sku` |
| `{deviceNameFx}` | #16 Tabel A baris 3 | Device Name SKU Smart Fixed Reader | `Fixture.hardwareStock.p16.a[3].deviceName` |
| `{skuBle}` | #16 Tabel A baris 5; #27 | kode SKU BLE Gateway, 4 Available dan 1 In Use, Brand dan Model/Type 25 karakter atau kurang | `Fixture.hardwareStock.p16.a[5].sku` |
| `{skuIx4}` | #16 Tabel A baris 6 | kode SKU Smart Fixed Reader tanpa unit (Total Registered 0, Last Updated `—`) | `Fixture.hardwareStock.p16.a[6].sku` |
| `{deviceNameIx4}` | #16 Tabel A baris 6 | Device Name SKU Smart Fixed Reader tanpa unit | `Fixture.hardwareStock.p16.a[6].deviceName` |
| `{snCakraFx}` | #27 | Serial Number unit Available pertama SKU Smart Fixed Reader milik Distributor Pre-setup #10 | `Fixture.hardwareStock.p27.fx[1].serialNumber` |
| `{snFxRej}` | #27 | Serial Number unit Rejected SKU Smart Fixed Reader | `Fixture.hardwareStock.p27.fxRejectedSerial` |
| `{shortNameTc}` | #1 | nama pendek akun Total Control (kolom Registered By dan Modified By) | `Fixture.hardwareStock.account.p01.totalControl.shortName` |

- Data Pre-setup: SKU `{skuFx}` (Smart Fixed Reader), `{skuBle}` (BLE Gateway), dan `{skuIx4}` (Smart Fixed Reader, 0 unit, Pre-setup #16) dari Pre-setup #16 dan unit Pre-setup #27; unit Rejected `{snFxRej}` dan unit Available `{snCakraFx}` pada SKU {skuFx} (Pre-setup #27).
- Data Dinamis (suffix per run `{runId}-249`): `SN-ZEBRA-FX9600-100001-{runId}-249` (TC-80); `SN-ZEBRA-FX9600-100002-{runId}-249`, `SN-ZEBRA-FX9600-100003-{runId}-249`, `SN-ZEBRA-FX9600-100004-{runId}-249` (TC-81); `   SN-TRIM-0001-{runId}-249   ` dan `SN-TRIM-0002-{runId}-249` (TC-83); satu baris Serial Number tepat 120 karakter berbentuk `SN-LEN120-{runId}-249-` diikuti karakter `A` sampai total 120 karakter (TC-95); MAC `AA:BB:CC:{dd}:{dd}:{dd}` dengan tiga oktet terakhir diambil dari enam digit terakhir `{runId}` (TC-82, format MAC tidak menerima suffix teks); `SN-IX4-0001-{runId}-249` (TC-600). Serial Number `{snFxRej}` (TC-94) dan `{snCakraFx}` pada SKU {skuBle} (TC-93) bukan Data Dinamis: nilainya dibaca dari fixture Pre-setup #27 karena TC menguji kecocokan dengan unit Pre-setup itu.
- Kemampuan teknis (disediakan tim FE/BE): membaca nomor tertinggi Device Name yang pernah dialokasikan SKU (termasuk unit yang sudah dihapus), karena Device Name `{deviceNameFx} - [N]` melanjutkan nomor tersebut; fixture BE yang menghapus unit yang dibuat spec (bukan unit Pre-setup, termasuk unit baru bernomor `{snFxRej}` dan `{snCakraFx}` pada SKU {skuBle}) dan mengembalikan pencacah nomor urut SKU {skuIx4} sehingga unit pertama SKU itu kembali bernama `{deviceNameIx4} - 1` pada run berikutnya (mekanismenya tidak didefinisikan di TC, PRD, atau LLD, lihat Temuan untuk QA); jam server dan jam browser sinkron untuk asersi waktu Submit (toleransi satu menit).
- Efek pada Pre-setup: Total Registered, Available, dan Last Updated baris SKU {skuFx}, {skuBle}, dan {skuIx4} berubah selama spec berjalan; SKU Pre-setup tidak dapat dimiliki spec karena katalog dan fotonya Pre-setup #16. Hook `after` menghapus unit bersuffix `-249` dan unit literal yang dibuat spec; hitungan dicatat sebagai baseline sebelum aksi dan diasersi dengan selisih.
- Urutan jalan: spec ini mengubah baseline Stock List dan SKU {skuIx4} (kosong) sehingga dijalankan sesudah spec yang membaca baseline Pre-setup (lihat suite.md). Precondition TC-600 (TC-7, TC-46, dan TC-520 sudah dijalankan) hanya berarti SKU {skuIx4} masih tanpa unit saat spec dimulai; spec tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACHS-80: Submit satu Serial Number

1. Ketik Search `{skuFx}`, tekan Enter
2. Klik row action `Detail` pada baris SKU `{skuFx}`
3. Catat Total Registered, Available, dan In Use pada Summary bar sebagai baseline
4. Klik segmen `Stock` pada breadcrumb
5. Ketik Search `{skuFx}`, tekan Enter
6. Klik `(⋯)` pada baris SKU `{skuFx}`
7. Klik opsi `Add Stock`
8. Ketik `SN-ZEBRA-FX9600-100001-{runId}-249` di textarea
9. Klik `[Submit]`
10. Catat waktu sesudah Submit
11. Verifikasi toast sukses "Success, unit has been added to stock."
12. Verifikasi halaman berpindah ke Stock Detail > Tab Available SKU `{skuFx}`
13. Verifikasi baris `SN-ZEBRA-FX9600-100001-{runId}-249` berstatus `Available`
14. Verifikasi Registered By baris itu `{shortNameTc}`
15. Verifikasi Registered At baris itu berisi waktu Submit (selisih kurang dari satu menit)
16. Verifikasi Device Name baris itu `{deviceNameFx} - [N]` dengan N melanjutkan nomor tertinggi yang pernah dialokasikan SKU ini
17. Verifikasi Summary bar: Total Registered dan Available masing-masing bertambah 1 dari baseline langkah 3
18. Verifikasi Summary bar: In Use tidak berubah dari baseline langkah 3
19. Klik segmen `Stock` pada breadcrumb
20. Ketik Search `{skuFx}`, tekan Enter
21. Verifikasi baris SKU `{skuFx}` pada Stock List: Total Registered dan Available bertambah 1 dari baseline langkah 3
22. Verifikasi Last Updated baris SKU itu berubah ke waktu Submit langkah 10

### TC-AC-ACHS-81: Submit tiga Serial Number dalam satu batch

23. Klik `(⋯)` pada baris SKU `{skuFx}`
24. Klik opsi `Add Stock`
25. Ketik tiga baris `SN-ZEBRA-FX9600-100002-{runId}-249`, `SN-ZEBRA-FX9600-100003-{runId}-249`, `SN-ZEBRA-FX9600-100004-{runId}-249`
26. Klik `[Submit]`
27. Verifikasi toast sukses "Success, unit has been added to stock."
28. Verifikasi halaman berpindah ke Stock Detail > Tab Available
29. Verifikasi ketiga unit berstatus `Available`
30. Verifikasi Device Name ketiga unit `{deviceNameFx} - [N]` bernomor berurutan tanpa celah dan tanpa memakai nomor yang pernah dialokasikan
31. Verifikasi Summary bar: Total Registered dan Available bertambah 3 dari nilai langkah 17

### TC-AC-ACHS-83: Spasi tepi dibuang dan baris kosong diabaikan

32. Klik segmen `Stock` pada breadcrumb
33. Ketik Search `{skuFx}`, tekan Enter
34. Klik `(⋯)` pada baris SKU `{skuFx}`
35. Klik opsi `Add Stock`
36. Ketik `   SN-TRIM-0001-{runId}-249   ` lalu Enter, baris kosong, lalu `SN-TRIM-0002-{runId}-249`
37. Verifikasi counter "2 serial numbers detected"
38. Klik `[Submit]`
39. Verifikasi dua unit tersimpan dengan Serial Number `SN-TRIM-0001-{runId}-249` dan `SN-TRIM-0002-{runId}-249` tanpa spasi tepi pada Tab Available

### TC-AC-ACHS-94: Unit Rejected tidak dicocokkan pada validasi V-05

40. Klik segmen `Stock` pada breadcrumb
41. Ketik Search `{skuFx}`, tekan Enter
42. Klik `(⋯)` pada baris SKU `{skuFx}`
43. Klik opsi `Add Stock`
44. Ketik `{snFxRej}` (unit Rejected SKU yang sama, Pre-setup #27)
45. Klik `[Submit]`
46. Verifikasi toast sukses "Success, unit has been added to stock."

### TC-AC-ACHS-95: Serial Number tepat 120 karakter

47. Klik segmen `Stock` pada breadcrumb
48. Ketik Search `{skuFx}`, tekan Enter
49. Klik `(⋯)` pada baris SKU `{skuFx}`
50. Klik opsi `Add Stock`
51. Tempel satu baris Serial Number sepanjang 120 karakter (`SN-LEN120-{runId}-249-` diikuti karakter `A` sampai total 120 karakter)
52. Verifikasi banner V-16 tidak tampil
53. Klik `[Submit]`
54. Verifikasi toast sukses "Success, unit has been added to stock."

### TC-AC-ACHS-82: SKU {skuBle} dengan MAC Address

55. Klik segmen `Stock` pada breadcrumb
56. Ketik Search `{skuBle}`, tekan Enter
57. Klik `(⋯)` pada baris SKU `{skuBle}`
58. Klik opsi `Add Stock`
59. Ketik MAC Address `AA:BB:CC:{dd}:{dd}:{dd}` (Data Dinamis) di textarea
60. Klik `[Submit]`
61. Verifikasi toast sukses "Success, unit has been added to stock."
62. Verifikasi halaman berpindah ke Stock Detail > Tab Available SKU `{skuBle}`
63. Verifikasi unit baru dengan Serial Number sama dengan MAC langkah 59 berstatus `Available`
64. Verifikasi Tab Available tidak memiliki kolom Power

### TC-AC-ACHS-93: Serial Number sama pada SKU lain bukan duplikat

65. Klik `[Add Stock]` pada toolbar Tab Available SKU `{skuBle}` (form baru)
66. Ketik `{snCakraFx}` (SN yang sudah ada pada SKU {skuFx})
67. Klik `[Submit]`
68. Verifikasi toast sukses "Success, unit has been added to stock."
69. Verifikasi tidak ada error banner V-05
70. Verifikasi unit `{snCakraFx}` tersimpan pada SKU {skuBle} di Tab Available

### TC-AC-ACHS-600: Add Stock pertama pada SKU kosong

71. Klik segmen `Stock` pada breadcrumb
72. Ketik Search `{skuIx4}`, tekan Enter
73. Klik row action `Detail` pada baris SKU `{skuIx4}`
74. Verifikasi Tab Available menampilkan empty state `No available hardware units`
75. Klik segmen `Stock` pada breadcrumb
76. Ketik Search `{skuIx4}`, tekan Enter
77. Klik `(⋯)` pada baris SKU `{skuIx4}`
78. Klik opsi `Add Stock`
79. Ketik `SN-IX4-0001-{runId}-249` di textarea
80. Klik `[Submit]`
81. Verifikasi toast sukses "Success, unit has been added to stock."
82. Verifikasi halaman berpindah ke Stock Detail > Tab Available
83. Verifikasi empty state `No available hardware units` tidak tampil lagi
84. Verifikasi tabel menampilkan satu baris `{deviceNameIx4} - 1` dengan Serial Number `SN-IX4-0001-{runId}-249` dan Status `Available`
85. Verifikasi Summary bar `1 | 1 | 0`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-80, 81, 82, 83, 93, 94, 95, 600). Tidak ada TC hanya-BE di spec ini.
- Spec ini melewati sekitar 35 langkah (85 langkah). Alasan: delapan TC aksi sukses Add Stock manual dengan akun dan role yang sama; tiap Submit sukses mengalihkan halaman sehingga form harus dibuka ulang (8 kali buka, 8 kali Submit); blok TC-80/81/83/94/95 memakai SKU yang sama, blok TC-82/93 SKU {skuBle}, dan TC-600 SKU {skuIx4}; tiap blok membuat unit sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Memecah menjadi spec terpisah hanya menambah login, hook, dan cleanup (prinsip 1 dan 13 bagian 3).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target dan klik segmen `Stock` pada breadcrumb (form sudah selesai Submit sehingga tidak ada dialog), baseline (langkah 3), pencatatan waktu Submit (langkah 10), serta `[Add Stock]` toolbar pada langkah 65 (form baru dari Tab Available).
- Spec ini tidak memuat validasi yang diblokir (ada di spec validasi). Urutan blok: SKU {skuFx} (TC-80, 81, 83, 94, 95), SKU {skuBle} (TC-82, 93), lalu TC-600 paling akhir karena mengubah SKU {skuIx4} dari kosong ke berisi.
- Efek Post Condition: TC-80 (Activity Log `Add Stock`, System Log, saldo kuota Device Allocation) dan TC-81 (Activity Log `+3 units`, sesi Event Log) tidak punya langkah observasi di TC dan tidak diasersi di spec ini; asersinya ada di spec pencatatan dan lintas modul. Post Condition TC-600 (Stock List baris SKU `{skuIx4}` menjadi `1 | 1 | 0`) tidak punya langkah observasi di TC sehingga tidak diasersi (S-03); dicatat di Temuan untuk QA.
- Temuan untuk QA:
  - TC-80 butir c mengacu pada "nomor tertinggi yang pernah dialokasikan SKU ini" tanpa menyebut nilainya untuk SKU {skuFx} pada Pre-setup #16 sampai #20; spec memakai kemampuan baca nomor (disediakan tim FE/BE).
  - TC-600 mensyaratkan unit pertama bernama `{deviceNameIx4} - 1`; pada run berikutnya nama itu hanya terjadi bila pencacah nomor urut SKU {skuIx4} dikembalikan oleh fixture BE (tidak didefinisikan di TC, PRD, atau LLD).
  - TC-82 memakai `AA:BB:CC:00:11:22` tanpa suffix; spec memakai MAC turunan `{runId}` supaya unik per run (S-12); format MAC tidak menerima suffix teks.
  - TC-94 memuat Serial Number `{snFxRej}` yang sama dengan unit Rejected Pre-setup #27 dan TC lain memakai unit itu untuk Sync; unit Available hasil TC-94 dihapus fixture di `after` supaya status Rejected Pre-setup tidak berubah.
  - TC-600 Post Condition (Stock List baris SKU `{skuIx4}` menjadi `1 | 1 | 0`) tidak punya langkah observasi di TC (langkah TC berhenti pada Tab Available); spec tidak mengasersinya. QA diminta menambah langkah observasi Stock List di TC bila Post Condition itu harus diuji.
  - TC-80, 81, 82, 83, 93, 94, 95, dan 600 tidak memuat Post Condition yang punya langkah observasi selain yang tercantum pada Expected.
