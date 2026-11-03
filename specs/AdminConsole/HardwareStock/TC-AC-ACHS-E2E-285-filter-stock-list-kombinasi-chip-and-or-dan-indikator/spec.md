---
id: TC-AC-ACHS-E2E-285-filter-stock-list-kombinasi-chip-and-or-dan-indikator
title: "Filter Stock List: Kombinasi Chip, OR dan AND, Search, Draft, Indikator, Kolom Tersembunyi, Overflow Chip, dan Opsi Sumber Hilang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-217
  - TC-AC-ACHS-218
  - TC-AC-ACHS-219
  - TC-AC-ACHS-220
  - TC-AC-ACHS-221
  - TC-AC-ACHS-222
  - TC-AC-ACHS-223
  - TC-AC-ACHS-224
  - TC-AC-ACHS-225
  - TC-AC-ACHS-226
  - TC-AC-ACHS-607
  - TC-AC-ACHS-608
coverage:
  web: automated
---

# Filter Stock List: Kombinasi Chip, OR dan AND, Search, Draft, Indikator, Kolom Tersembunyi, Overflow Chip, dan Opsi Sumber Hilang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Stock List (lihat `suite.md`).
- Data Pre-setup (read-only, tidak diubah spec): #16 Katalog SKU 30 baris Stock List (Tabel A: 8 SKU nama dan 22 SKU `Fixture.hardwareStock.p16.a[9].sku` sampai `Fixture.hardwareStock.p16.a[30].sku`) dan #15 General Settings (Date Format `DD MMM YYYY`, Time Format 24-hour `HH:mm`). Tidak ada Data Dinamis.
- Baseline Pre-setup (S-06): spec ini membaca baseline Katalog SKU 30 baris Stock List (Pre-setup #16, Tabel A) beserta hitungan unit dari Pre-setup #17, #18, #19, #24, dan #27 tanpa mengubahnya, sedangkan nomor spec ini sesudah spec penulis (240 sampai 284). Syarat: baseline Pre-setup dipulihkan fixture environment automation ke keadaan awal sebelum spec ini dimulai (`suite.md`, bagian "Urutan jalan" dan "Seeding ulang Pre-setup"); fixture dan skrip pemulihannya disediakan tim FE/BE dan belum ada. Spec ini tidak menumpang hasil spec lain.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

| Parameter | Pre-setup | Peran dan atribut penentu | Kunci fixture |
|---|---|---|---|
| `brand_a1` | #16 (Tabel A baris ke-1) | Brand baris 1 Tabel A (#16): Handheld Reader Short Range, 34 Available dan 16 In Use (#19); Brand yang sama pada baris 3 dan 4 | `Fixture.hardwareStock.p16.a[1].brand` |
| `sku_a1` | #16 (Tabel A baris ke-1) | kode SKU baris 1 Tabel A (#16): Handheld Reader Short Range, 34 Available dan 16 In Use (#19) | `Fixture.hardwareStock.p16.a[1].sku` |
| `brand_a2` | #16 (Tabel A baris ke-2) | Brand baris 2 Tabel A (#16): Handheld Reader Short Range, 12 Available; Brand yang sama pada baris 6 dan 8 | `Fixture.hardwareStock.p16.a[2].brand` |
| `sku_a2` | #16 (Tabel A baris ke-2) | kode SKU baris 2 Tabel A (#16): Handheld Reader Short Range, 12 Available | `Fixture.hardwareStock.p16.a[2].sku` |
| `sku_a3` | #16 (Tabel A baris ke-3) | kode SKU baris 3 Tabel A (#16): Smart Fixed Reader, 8 Available (#27) | `Fixture.hardwareStock.p16.a[3].sku` |
| `sku_a4` | #16 (Tabel A baris ke-4) | kode SKU baris 4 Tabel A (#16): Handheld Reader Long Range, 18 Available dan 7 In Use (#17, #18) | `Fixture.hardwareStock.p16.a[4].sku` |
| `sku_a6` | #16 (Tabel A baris ke-6) | kode SKU baris 6 Tabel A (#16): Smart Fixed Reader tanpa unit (Total Registered 0, Last Updated kosong) | `Fixture.hardwareStock.p16.a[6].sku` |
| `sku_a8` | #16 (Tabel A baris ke-8) | kode SKU baris 8 Tabel A (#16): Smart Fixed Reader dengan 120 Available (#24) | `Fixture.hardwareStock.p16.a[8].sku` |
| `model_pad_01` | #16 (SKU padding nomor 01) | Model/Type baris padding nomor 01 (#16) | `Fixture.hardwareStock.p16.a[9].modelType` |
| `sku_pad_01` | #16 (SKU padding nomor 01) | kode SKU baris padding nomor 01 (#16) | `Fixture.hardwareStock.p16.a[9].sku` |
| `model_pad_10` | #16 (SKU padding nomor 10) | Model/Type baris padding nomor 10 (#16) | `Fixture.hardwareStock.p16.a[18].modelType` |
| `sku_pad_10` | #16 (SKU padding nomor 10) | kode SKU baris padding nomor 10 (#16) | `Fixture.hardwareStock.p16.a[18].sku` |
| `sku_pad_17` | #16 (SKU padding nomor 17) | kode SKU baris padding nomor 17 (#16) | `Fixture.hardwareStock.p16.a[25].sku` |
| `sku_pad_19` | #16 (SKU padding nomor 19) | kode SKU baris padding nomor 19 (#16) | `Fixture.hardwareStock.p16.a[27].sku` |
| `sku_pad_21` | #16 (SKU padding nomor 21) | kode SKU baris padding nomor 21 (#16) | `Fixture.hardwareStock.p16.a[29].sku` |
| `sku_pad_22` | #16 (SKU padding nomor 22) | kode SKU baris padding nomor 22 (#16) | `Fixture.hardwareStock.p16.a[30].sku` |
| `brand_16h` | #16h (seed sesaat) | Brand SKU seed sesaat 16h (#16) | `Fixture.hardwareStock.p16h.brand` |
| `name_16h` | #16h (seed sesaat) | Device Name SKU seed sesaat 16h (#16): Smart Fixed Reader, dimuat tepat sebelum TC pemakainya | `Fixture.hardwareStock.p16h.deviceName` |
| `model_16h` | #16h (seed sesaat) | Model/Type SKU 16h (#16) | `Fixture.hardwareStock.p16h.modelType` |
| `sku_16h` | #16h (seed sesaat) | kode SKU seed sesaat 16h (#16): Smart Fixed Reader stok 0, dimuat tepat sebelum TC pemakainya | `Fixture.hardwareStock.p16h.sku` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email` |
| `akun defaultUserPrincipal` | #2 | Akun Principal Default User | `Fixture.hardwareStock.account.p02.defaultUser.email`, `Fixture.hardwareStock.account.p02.defaultUser.fullName` |

- Data Dinamis (hanya TC-AC-ACHS-607; Pre-setup #16h, SKU sementara di luar 30 baris baseline, dimuat tepat sebelum TC itu): SKU `Fixture.hardwareStock.p16h.sku` (Smart Fixed Reader, Device Name `Fixture.hardwareStock.p16h.deviceName`, Brand `Fixture.hardwareStock.p16h.brand`, Model/Type `Fixture.hardwareStock.p16h.modelType`, stok 0). SKU ini dihapus oleh aksi di langkah 81; hook `after` spec ini menghapusnya lewat sesi API bila masih ada.
- Pelaku kedua TC-AC-ACHS-607: Default User Principal `Fixture.hardwareStock.account.p02.defaultUser.fullName` `Fixture.hardwareStock.account.p02.defaultUser.email` (Pre-setup #2) lewat sesi API aktor (suite.md), password `Spectra.env.AC_DEFAULT_USER_PASSWORD` (nama env ditetapkan dan didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Penghapusan SKU di Settings > Device > SKU lewat sesi API memakai kemampuan yang disediakan tim BE/FE (tanpa endpoint karangan di spec).
- Pilihan spec: TC-AC-ACHS-225 hanya menulis "isi satu field" sehingga spec memakai Brand = `Fixture.hardwareStock.p16.a[2].brand`.
- Kemampuan teknis (disediakan tim FE): membaca chip yang tampil dan chip `+N more` pada closed-state field; sesi API pelaku kedua (suite.md); muat ulang data Stock List sesudah seed SKU `Fixture.hardwareStock.p16h.sku` (langkah 76).
- State global yang diubah: seed dan penghapusan SKU `Fixture.hardwareStock.p16h.sku` (langkah 76 sampai 81); sort Total Registered dipulihkan ke netral pada TC-AC-ACHS-223. Preferensi kolom di browser dihapus oleh hook suite `after`.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACHS-217: Dua opsi satu field dihitung OR

1. Klik icon Filter
2. Buka dropdown Brand, centang `Fixture.hardwareStock.p16.a[1].brand` lalu `Fixture.hardwareStock.p16.a[2].brand`, tutup dropdown
3. Verifikasi dua chip `Fixture.hardwareStock.p16.a[1].brand` dan `Fixture.hardwareStock.p16.a[2].brand` tampil di dalam closed-state field, sejajar
4. Klik `[Apply]`
5. Verifikasi tabel menampilkan gabungan (OR) 6 baris: `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku`, `Fixture.hardwareStock.p16.a[2].sku`, `Fixture.hardwareStock.p16.a[6].sku`
6. Klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACHS-218: Hapus chip lewat (X) menyinkronkan checkbox

7. Buka dropdown Brand, centang `Fixture.hardwareStock.p16.a[1].brand` dan `Fixture.hardwareStock.p16.a[2].brand`, tutup dropdown
8. Klik `(X)` pada chip `Fixture.hardwareStock.p16.a[1].brand` (tanpa membuka dropdown)
9. Verifikasi chip `Fixture.hardwareStock.p16.a[1].brand` hilang
10. Verifikasi chip `Fixture.hardwareStock.p16.a[2].brand` tetap ada
11. Buka dropdown Brand
12. Verifikasi checkbox `Fixture.hardwareStock.p16.a[1].brand` di dalam dropdown ter-uncheck
13. Verifikasi checkbox `Fixture.hardwareStock.p16.a[2].brand` tetap tercentang
14. Tutup dropdown, klik `[Apply]`
15. Verifikasi tabel menampilkan 3 baris: `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[2].sku`, `Fixture.hardwareStock.p16.a[6].sku`
16. Klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACHS-219: Uncheck di dalam dropdown menghapus chip

17. Buka dropdown Brand, centang `Fixture.hardwareStock.p16.a[1].brand` dan `Fixture.hardwareStock.p16.a[2].brand`
18. Dengan dropdown tetap terbuka, hilangkan centang `Fixture.hardwareStock.p16.a[2].brand`
19. Tutup dropdown
20. Verifikasi chip `Fixture.hardwareStock.p16.a[2].brand` hilang dari field
21. Verifikasi chip `Fixture.hardwareStock.p16.a[1].brand` tetap ada
22. Klik `[Apply]`
23. Verifikasi tabel menampilkan 3 baris: `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku`
24. Klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACHS-220: Dua field berbeda dihitung AND

25. Isi Type = `Smart Fixed Reader` dan Brand = `Fixture.hardwareStock.p16.a[2].brand`
26. Klik `[Apply]`
27. Verifikasi tabel menampilkan irisan 2 baris: `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[6].sku`
28. Klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACHS-221: Search lalu Filter, filter menimpa tanpa mereset keyword

29. Ketik Search `Fixture.hardwareStock.p16.a[1].brand`, tekan Enter
30. Isi Type = `Smart Fixed Reader`, klik `[Apply]`
31. Verifikasi tabel menampilkan irisan Search dan Filter: 1 baris `Fixture.hardwareStock.p16.a[3].sku`
32. Verifikasi keyword `Fixture.hardwareStock.p16.a[1].brand` tetap terisi di kotak Search
33. Klik `[Clear Field]`, klik `[Apply]`, klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-222: Filter lalu Search, hasil identik

34. Isi Type = `Smart Fixed Reader`, klik `[Apply]`
35. Ketik Search `Fixture.hardwareStock.p16.a[1].brand`, tekan Enter
36. Verifikasi tabel menampilkan 1 baris `Fixture.hardwareStock.p16.a[3].sku`, identik dengan hasil urutan Search lalu Filter
37. Klik `[Clear Field]`, klik `[Apply]`, klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-223: Clear Field mempertahankan Search dan Sort aktif

38. Ketik Search `Fixture.hardwareStock.p16.a[1].brand`, tekan Enter
39. Klik header kolom Total Registered sekali (Ascending)
40. Isi Type = `Smart Fixed Reader`, klik `[Apply]`
41. Klik `[Clear Field]`, klik `[Apply]`
42. Verifikasi field Type pada Filter Panel kosong kembali
43. Verifikasi keyword `Fixture.hardwareStock.p16.a[1].brand` tetap menyaring tabel: 3 baris `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[4].sku`, `Fixture.hardwareStock.p16.a[1].sku`
44. Verifikasi indikator sort Ascending tetap aktif pada Total Registered
45. Klik header kolom Total Registered dua kali sampai netral, klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-224: Menutup panel tanpa Apply membuang draft

46. Isi Type = `Smart Fixed Reader`, klik `[Apply]`
47. Ubah field Brand menjadi `Fixture.hardwareStock.p16.a[2].brand` tanpa klik `[Apply]`
48. Klik icon Filter untuk menutup panel
49. Klik icon Filter untuk membuka panel kembali
50. Verifikasi panel menampilkan nilai ter-Apply terakhir (Type = `Smart Fixed Reader`)
51. Verifikasi draft Brand `Fixture.hardwareStock.p16.a[2].brand` tidak tampil (field Brand kosong)
52. Verifikasi tabel tetap menampilkan hasil filter terakhir yang di-Apply: 25 baris, lima teratas `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[29].sku`, `Fixture.hardwareStock.p16.a[27].sku`, `Fixture.hardwareStock.p16.a[25].sku`
53. Klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACHS-225: Indikator filter aktif berupa badge titik

54. Verifikasi ikon Filter tanpa badge
55. Isi Brand = `Fixture.hardwareStock.p16.a[2].brand`, klik `[Apply]`
56. Verifikasi badge titik (tanpa angka) tampil pada ikon Filter saat panel terbuka
57. Klik icon Filter untuk menutup panel
58. Verifikasi badge titik (tanpa angka) tampil pada ikon Filter saat panel tertutup
59. Klik icon Filter untuk membuka panel, klik `[Clear Field]`, klik `[Apply]`
60. Verifikasi badge titik pada ikon Filter hilang

### TC-AC-ACHS-226: Filter independen dari Column Visibility

61. Isi Type = `Smart Fixed Reader`, klik `[Apply]`
62. Klik header kolom Actions `(⋯)`, hilangkan centang `Type`, tutup overlay Column Visibility
63. Klik icon Filter untuk menutup panel, klik icon Filter untuk membuka kembali Filter Panel
64. Verifikasi field Type tetap ada di Filter Panel dengan nilai `Smart Fixed Reader`
65. Verifikasi filter yang sudah di-Apply tetap berlaku: 25 baris, lima teratas `Fixture.hardwareStock.p16.a[8].sku`, `Fixture.hardwareStock.p16.a[3].sku`, `Fixture.hardwareStock.p16.a[29].sku`, `Fixture.hardwareStock.p16.a[27].sku`, `Fixture.hardwareStock.p16.a[25].sku`
66. Klik header kolom Actions `(⋯)`, ceklis kembali `Type`, tutup overlay Column Visibility
67. Klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACHS-608: Overflow chip dropdown multi-select

68. Buka dropdown Model/Type, centang opsi `Fixture.hardwareStock.p16.a[9].modelType` sampai `Fixture.hardwareStock.p16.a[18].modelType` satu per satu, tutup dropdown
69. Verifikasi chip yang muat tampil dan sisanya diringkas dalam satu chip `+N more`, dengan jumlah chip tampil ditambah N sama dengan 10
70. Verifikasi field tidak melebar keluar panel Filter
71. Verifikasi field tidak digulir horizontal
72. Klik `[Apply]`
73. Verifikasi tabel menampilkan 10 baris `Fixture.hardwareStock.p16.a[9].sku` sampai `Fixture.hardwareStock.p16.a[18].sku`
74. Verifikasi footer `Showing 1–10 of 10 entries`
75. Klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACHS-607: Filter aktif dengan opsi sumber hilang

76. Muat SKU sementara `Fixture.hardwareStock.p16h.sku` (Pre-setup #16h) lewat seed API, lalu muat ulang halaman Hardware > Stock (F5) dan klik icon Filter
77. Verifikasi tabel menampilkan seluruh baris termasuk SKU sementara (info `Showing 1–10 of 31 entries`)
78. Pilih Model/Type = `Fixture.hardwareStock.p16h.modelType`, klik `[Apply]`
79. Verifikasi tabel menampilkan 1 baris `Fixture.hardwareStock.p16h.sku`
80. Verifikasi badge titik tampil pada ikon Filter
81. Sesi API Default User Principal `Fixture.hardwareStock.account.p02.defaultUser.fullName` menghapus SKU `Fixture.hardwareStock.p16h.sku` di Settings > Device > SKU hingga penghapusan tersimpan
82. Tunggu aksi selesai (penghapusan SKU tersimpan)
83. Klik `[Apply]` pada Filter Panel tanpa memuat ulang halaman
84. Verifikasi tidak ada toast error
85. Verifikasi tabel menampilkan seluruh 30 baris tanpa kriteria filter (info `Showing 1–10 of 30 entries`)
86. Verifikasi field Model/Type kosong (`Fixture.hardwareStock.p16h.modelType` tidak lagi menjadi kriteria filter)
87. Verifikasi tidak ada pesan error pada halaman
88. Verifikasi badge titik pada ikon Filter hilang
89. Buka dropdown Model/Type
90. Verifikasi opsi `Fixture.hardwareStock.p16.a[9].modelType` tampil di dropdown Model/Type
91. Verifikasi dropdown Model/Type tidak memuat `Fixture.hardwareStock.p16h.modelType`
92. Tutup dropdown Model/Type, klik icon Filter untuk menutup panel


## Notes

- Sumber TC: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md`. (bagian 4a, Stock List). Seluruh TC sumber spec ini dikerjakan di sini.
- Konfirmasi keyword Search terhadap nilai penuh Pre-setup (#8): keyword Search `Fixture.hardwareStock.p16.a[1].brand` adalah nilai penuh kolom Brand baris 1 Tabel A (Pre-setup #16), bukan potongan. Dicocokkan dengan Tabel A: Search tersebut + Type `Smart Fixed Reader` menghasilkan 1 baris (baris 3), dan Search saja menghasilkan 3 baris (baris 1, 3, 4) sesuai asersi langkah 31, 36, dan 43. Nilai penuh itu tidak memuat baris lain pada kolom yang dicari (SKU seluruh baris lain memakai Brand berbeda atau padding). Tidak ada perbedaan.
- Urutan TC: TC-AC-ACHS-217 sampai 226, lalu TC-AC-ACHS-608, dan TC-AC-ACHS-607 paling akhir karena menambah dan menghapus SKU (mengubah baseline sementara). Filter Panel tetap terbuka setelah `[Apply]` sehingga langkah "Klik icon Filter" TC berikutnya tidak diulang kecuali TC-AC-ACHS-224, 225, dan 226 yang menutup dan membuka panel.
- Absence toast error (langkah 84) ditulis tepat sesudah pemicu `[Apply]` (langkah 83) dan sebelum `Verifikasi` tabel (butir 8b nomor 11); `[Apply]` menjadi anchor positif yang buktinya menyusul pada langkah 85.
- Langkah penghubung (aksi tanpa `Verifikasi`): `[Clear Field]` lalu `[Apply]` antar-TC, pengosongan Search, pemulihan sort Total Registered ke netral (TC-AC-ACHS-223), pengembalian kolom `Type` (TC-AC-ACHS-226), penutupan dropdown dan panel, serta langkah "Tunggu aksi selesai" setelah aksi sesi API.
- TC-AC-ACHS-607 melibatkan dua sesi (sesi A UI, sesi B Default User Principal `Fixture.hardwareStock.account.p02.defaultUser.fullName`). Sesi B hanya memicu perubahan state (hapus SKU) sehingga memakai sesi API aktor dan bukan konteks UI kedua kelas c (keputusan 2026-10-21 dan 2026-10-30); tidak memakai `P-2`.
- Spec memiliki 92 langkah nominal di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Filter Stock List pada akun dan dataset yang sama, kombinasi chip, AND, OR, dan indikator), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan tidak ada perulangan atau langkah bersyarat; TC-AC-ACHS-607 di akhir spec sehingga perubahan baseline tidak memengaruhi TC lain.
- Temuan untuk QA:
  - Nomor spec ini (285) sesudah spec penulis (240 sampai 284), padahal spec membaca baseline Pre-setup dan `suite.md` bagian "Urutan jalan" menempatkan spec baca di bawah nomor 240. Spec tidak direnumber; syarat pemulihan baseline ditulis di `## Prerequisites`, dan keputusan penomoran (folder baru di bawah 240) menunggu keputusan di luar spec ini.
  - TC-AC-ACHS-607 berlabel Manual Only (dua sesi paralel) pada kolom Automation; label itu bukan alasan mengeluarkan TC (bagian 2 konvensi), sehingga pelaku kedua ditulis sebagai sesi API yang disediakan tim BE/FE. TC menyebut sesi B menghapus SKU di Settings > Device SKU tanpa mekanismenya.
  - TC-AC-ACHS-607 menyebut Total Control lain `Fixture.hardwareStock.account.p02.defaultUser.fullName` sebagai sesi B; env var password akun itu tidak terdaftar (nama `AC_DEFAULT_USER_PASSWORD` ditetapkan tim FE).
  - TC-AC-ACHS-607 Expected b memuat "tanpa kriteria: seluruh 30 baris" sebagai kondisi; spec mengasersi 30 baris karena tidak ada kriteria lain di Filter Panel.
  - TC-AC-ACHS-225 menyebut "isi satu field" tanpa nilai; spec memilih Brand = `Fixture.hardwareStock.p16.a[2].brand`.
  - TC-AC-ACHS-608 Expected a ("jumlah chip tampil ditambah N sama dengan 10") tidak menyebut jumlah chip tampil karena bergantung lebar field; spec mengasersi penjumlahan.
