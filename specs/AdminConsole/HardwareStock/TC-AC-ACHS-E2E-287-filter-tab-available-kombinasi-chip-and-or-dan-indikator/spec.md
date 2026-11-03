---
id: TC-AC-ACHS-E2E-287-filter-tab-available-kombinasi-chip-and-or-dan-indikator
title: "Filter Stock Detail Tab Available: Kombinasi Chip, OR dan AND, Search, Draft, Indikator, Kolom Tersembunyi, dan Opsi Waiting for Approval"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-275
  - TC-AC-ACHS-276
  - TC-AC-ACHS-277
  - TC-AC-ACHS-278
  - TC-AC-ACHS-279
  - TC-AC-ACHS-280
  - TC-AC-ACHS-281
  - TC-AC-ACHS-282
  - TC-AC-ACHS-283
  - TC-AC-ACHS-284
  - TC-AC-ACHS-316
coverage:
  web: automated
---

# Filter Stock Detail Tab Available: Kombinasi Chip, OR dan AND, Search, Draft, Indikator, Kolom Tersembunyi, dan Opsi Waiting for Approval

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Stock List; flag halaman Stock Detail disetel dengan cara yang sama (disediakan tim FE; lihat `suite.md`).
- Data Pre-setup (read-only, tidak diubah spec): SKU `Fixture.hardwareStock.p16.a[4].sku` (Long Range) dengan 18 unit Available dan 1 unit Waiting for Approval (#17, Tabel E: `Fixture.hardwareStock.p17.e[10].deviceName` sampai `Fixture.hardwareStock.p17.e[28].deviceName`; Tab Available 19 baris) dan General Settings #15 (Date Format `DD MMM YYYY`, Time Format 24-hour `HH:mm`). Tidak ada Data Dinamis.
- Baseline Pre-setup (S-06): spec ini membaca baseline unit SKU `Fixture.hardwareStock.p16.a[4].sku` (Pre-setup #17, Tabel E, dan #18) tanpa mengubahnya, sedangkan nomor spec ini sesudah spec penulis (240 sampai 284). Syarat: baseline Pre-setup dipulihkan fixture environment automation ke keadaan awal sebelum spec ini dimulai (`suite.md`, bagian "Urutan jalan" dan "Seeding ulang Pre-setup"); fixture dan skrip pemulihannya disediakan tim FE/BE dan belum ada. Spec ini tidak menumpang hasil spec lain.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

| Parameter | Pre-setup | Peran dan atribut penentu | Kunci fixture |
|---|---|---|---|
| `kw_unit_name` | - | keyword Search turunan: `Fixture.hardwareStock.p17.e[20].deviceName` tanpa karakter terakhir (Device Name unit nomor 20 tanpa digit satuan); cocok dengan Device Name unit nomor 20 sampai 28 saja (`p17.e[20]` sampai `p17.e[28]`, 9 baris) | `Fixture.hardwareStock.derived.unitNameKeyword` |
| `sku_a4` | #16 (Tabel A baris ke-4) | kode SKU baris 4 Tabel A (#16): Handheld Reader Long Range, 18 Available dan 7 In Use (#17, #18) | `Fixture.hardwareStock.p16.a[4].sku` |
| `unit_10` | #17 (Tabel E baris N = 10) | Device Name unit nomor 10, Tabel E (#17) | `Fixture.hardwareStock.p17.e[10].deviceName` |
| `reg_u10` | #17 (Tabel E baris N = 10) | Registered By unit nomor 10 (Tabel E baris N = 10); pendaftar yang sama untuk unit 13, 16, 19, 22, 25 | `Fixture.hardwareStock.p17.e[10].registeredBy` |
| `unit_12` | #17 (Tabel E baris N = 12) | Device Name unit nomor 12, Tabel E (#17) | `Fixture.hardwareStock.p17.e[12].deviceName` |
| `reg_u12` | #17 (Tabel E baris N = 12) | Registered By unit nomor 12 (Tabel E baris N = 12); pendaftar yang sama untuk unit 15, 18, 21, 24, 27 | `Fixture.hardwareStock.p17.e[12].registeredBy` |
| `unit_13` | #17 (Tabel E baris N = 13) | Device Name unit nomor 13, Tabel E (#17) | `Fixture.hardwareStock.p17.e[13].deviceName` |
| `unit_15` | #17 (Tabel E baris N = 15) | Device Name unit nomor 15, Tabel E (#17) | `Fixture.hardwareStock.p17.e[15].deviceName` |
| `unit_16` | #17 (Tabel E baris N = 16) | Device Name unit nomor 16, Tabel E (#17) | `Fixture.hardwareStock.p17.e[16].deviceName` |
| `unit_18` | #17 (Tabel E baris N = 18) | Device Name unit nomor 18, Tabel E (#17) | `Fixture.hardwareStock.p17.e[18].deviceName` |
| `unit_19` | #17 (Tabel E baris N = 19) | Device Name unit nomor 19, Tabel E (#17) | `Fixture.hardwareStock.p17.e[19].deviceName` |
| `unit_20` | #17 (Tabel E baris N = 20) | Device Name unit nomor 20, Tabel E (#17) | `Fixture.hardwareStock.p17.e[20].deviceName` |
| `unit_21` | #17 (Tabel E baris N = 21) | Device Name unit nomor 21, Tabel E (#17) | `Fixture.hardwareStock.p17.e[21].deviceName` |
| `unit_22` | #17 (Tabel E baris N = 22) | Device Name unit nomor 22, Tabel E (#17) | `Fixture.hardwareStock.p17.e[22].deviceName` |
| `unit_23` | #17 (Tabel E baris N = 23) | Device Name unit nomor 23, Tabel E (#17) | `Fixture.hardwareStock.p17.e[23].deviceName` |
| `unit_24` | #17 (Tabel E baris N = 24) | Device Name unit nomor 24, Tabel E (#17) | `Fixture.hardwareStock.p17.e[24].deviceName` |
| `unit_25` | #17 (Tabel E baris N = 25) | Device Name unit nomor 25, Tabel E (#17) | `Fixture.hardwareStock.p17.e[25].deviceName` |
| `unit_26` | #17 (Tabel E baris N = 26) | Device Name unit nomor 26, Tabel E (#17) | `Fixture.hardwareStock.p17.e[26].deviceName` |
| `unit_27` | #17 (Tabel E baris N = 27) | Device Name unit nomor 27, Tabel E (#17) | `Fixture.hardwareStock.p17.e[27].deviceName` |
| `unit_28` | #17 (Tabel E baris N = 28) | Device Name unit nomor 28, Tabel E (#17) | `Fixture.hardwareStock.p17.e[28].deviceName` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email` |

- Data Dinamis (hanya TC-AC-ACHS-316; data milik spec karena TC menyetujui Subject yang mengubah baseline Pre-setup #17, S-06): satu SKU Handheld Reader milik spec dengan Model/Type `E2E287-{runId}` (`{runId}` terdiri atas digit) yang memiliki 1 unit Available dan 1 unit Waiting for Approval beserta satu Subject Register Duplicate pending untuk unit itu pada Approvals Tab Active (struktur sama dengan unit `Fixture.hardwareStock.p17.e[28].deviceName` pada Pre-setup #17). Seeding SKU, unit, dan Subject disediakan tim BE/FE di hook `before` spec ini tanpa endpoint karangan; hook `after` menghapus data itu.
- Pelaku kedua TC-AC-ACHS-316 ("sesi lain" menurut TC): sesi API akun aktor yang sama (Pre-setup #1, suite.md), yang berhak Approve, memutuskan Subject lewat kemampuan yang disediakan tim BE/FE.
- Data uji turunan (kolom "Hasil" dipakai oleh langkah Verifikasi):
  - OR TC-AC-ACHS-275: Registered By `Fixture.hardwareStock.p17.e[12].registeredBy` dan `Fixture.hardwareStock.p17.e[10].registeredBy` menghasilkan 12 baris, lima teratas `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[24].deviceName`, `Fixture.hardwareStock.p17.e[22].deviceName`, `Fixture.hardwareStock.p17.e[21].deviceName`.
  - AND TC-AC-ACHS-278: Status = `Available` dan Registered By = `Fixture.hardwareStock.p17.e[12].registeredBy` menghasilkan 6 baris `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[24].deviceName`, `Fixture.hardwareStock.p17.e[21].deviceName`, `Fixture.hardwareStock.p17.e[18].deviceName`, `Fixture.hardwareStock.p17.e[15].deviceName`, `Fixture.hardwareStock.p17.e[12].deviceName`.
  - Search dan Filter TC-AC-ACHS-279 dan TC-AC-ACHS-280: keyword `Fixture.hardwareStock.derived.unitNameKeyword` dan Status = `Available` menghasilkan 8 baris `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName`, `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[24].deviceName`, `Fixture.hardwareStock.p17.e[23].deviceName`, `Fixture.hardwareStock.p17.e[22].deviceName`, `Fixture.hardwareStock.p17.e[21].deviceName`, `Fixture.hardwareStock.p17.e[20].deviceName`.
- Pilihan spec: TC-AC-ACHS-283 hanya menulis "isi satu field" sehingga spec memakai Registered By = `Fixture.hardwareStock.p17.e[10].registeredBy`.
- Kemampuan teknis (disediakan tim FE): membaca chip pada closed-state field; muat ulang halaman (F5) mempertahankan SKU dan tab aktif Stock Detail (NC-11 dalam TC).
- State global yang diubah: seed dan keputusan Subject milik spec (langkah 75); tidak ada Pre-setup yang diubah. Preferensi kolom di browser dihapus oleh hook suite `after`.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Klik Tab `Available`
3. Klik icon Filter

### TC-AC-ACHS-275: Dua opsi satu field dihitung OR

4. Buka dropdown Registered By, centang `Fixture.hardwareStock.p17.e[12].registeredBy` lalu `Fixture.hardwareStock.p17.e[10].registeredBy`, tutup dropdown
5. Verifikasi dua chip `Fixture.hardwareStock.p17.e[12].registeredBy` dan `Fixture.hardwareStock.p17.e[10].registeredBy` tampil di dalam closed-state field, sejajar
6. Klik `[Apply]`
7. Verifikasi tabel menampilkan gabungan (OR) 12 baris, lima teratas `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[24].deviceName`, `Fixture.hardwareStock.p17.e[22].deviceName`, `Fixture.hardwareStock.p17.e[21].deviceName`
8. Klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACHS-276: Hapus chip lewat (X) menyinkronkan checkbox

9. Buka dropdown Registered By, centang `Fixture.hardwareStock.p17.e[12].registeredBy` dan `Fixture.hardwareStock.p17.e[10].registeredBy`, tutup dropdown
10. Klik `(X)` pada chip `Fixture.hardwareStock.p17.e[12].registeredBy` (tanpa membuka dropdown)
11. Verifikasi chip `Fixture.hardwareStock.p17.e[12].registeredBy` hilang
12. Verifikasi chip `Fixture.hardwareStock.p17.e[10].registeredBy` tetap ada
13. Buka dropdown Registered By
14. Verifikasi checkbox `Fixture.hardwareStock.p17.e[12].registeredBy` di dalam dropdown ter-uncheck
15. Verifikasi checkbox `Fixture.hardwareStock.p17.e[10].registeredBy` tetap tercentang
16. Tutup dropdown, klik `[Apply]`
17. Verifikasi tabel menampilkan 6 baris: `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[22].deviceName`, `Fixture.hardwareStock.p17.e[19].deviceName`, `Fixture.hardwareStock.p17.e[16].deviceName`, `Fixture.hardwareStock.p17.e[13].deviceName`, `Fixture.hardwareStock.p17.e[10].deviceName`
18. Klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACHS-277: Uncheck di dalam dropdown menghapus chip

19. Buka dropdown Registered By, centang `Fixture.hardwareStock.p17.e[12].registeredBy` dan `Fixture.hardwareStock.p17.e[10].registeredBy`
20. Dengan dropdown tetap terbuka, hilangkan centang `Fixture.hardwareStock.p17.e[10].registeredBy`
21. Tutup dropdown
22. Verifikasi chip `Fixture.hardwareStock.p17.e[10].registeredBy` hilang dari field
23. Verifikasi chip `Fixture.hardwareStock.p17.e[12].registeredBy` tetap ada
24. Klik `[Apply]`
25. Verifikasi tabel menampilkan 6 baris: `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[24].deviceName`, `Fixture.hardwareStock.p17.e[21].deviceName`, `Fixture.hardwareStock.p17.e[18].deviceName`, `Fixture.hardwareStock.p17.e[15].deviceName`, `Fixture.hardwareStock.p17.e[12].deviceName`
26. Klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACHS-278: Dua field berbeda dihitung AND

27. Isi Status = `Available` dan Registered By = `Fixture.hardwareStock.p17.e[12].registeredBy`
28. Klik `[Apply]`
29. Verifikasi tabel menampilkan irisan 6 baris: `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[24].deviceName`, `Fixture.hardwareStock.p17.e[21].deviceName`, `Fixture.hardwareStock.p17.e[18].deviceName`, `Fixture.hardwareStock.p17.e[15].deviceName`, `Fixture.hardwareStock.p17.e[12].deviceName`
30. Klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACHS-279: Search lalu Filter, filter menimpa tanpa mereset keyword

31. Ketik Search `Fixture.hardwareStock.derived.unitNameKeyword`, tekan Enter
32. Isi Status = `Available`, klik `[Apply]`
33. Verifikasi tabel menampilkan irisan Search dan Filter: 8 baris `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName`, `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[24].deviceName`, `Fixture.hardwareStock.p17.e[23].deviceName`, `Fixture.hardwareStock.p17.e[22].deviceName`, `Fixture.hardwareStock.p17.e[21].deviceName`, `Fixture.hardwareStock.p17.e[20].deviceName`
34. Verifikasi keyword `Fixture.hardwareStock.derived.unitNameKeyword` tetap terisi di kotak Search
35. Klik `[Clear Field]`, klik `[Apply]`, klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-280: Filter lalu Search, hasil identik

36. Isi Status = `Available`, klik `[Apply]`
37. Ketik Search `Fixture.hardwareStock.derived.unitNameKeyword`, tekan Enter
38. Verifikasi tabel menampilkan 8 baris `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName`, `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[24].deviceName`, `Fixture.hardwareStock.p17.e[23].deviceName`, `Fixture.hardwareStock.p17.e[22].deviceName`, `Fixture.hardwareStock.p17.e[21].deviceName`, `Fixture.hardwareStock.p17.e[20].deviceName`, identik dengan hasil urutan Search lalu Filter
39. Klik `[Clear Field]`, klik `[Apply]`, klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-281: Clear Field mempertahankan Search dan Sort aktif

40. Ketik Search `Fixture.hardwareStock.derived.unitNameKeyword`, tekan Enter
41. Klik header kolom Registered At sekali (Ascending)
42. Isi Status = `Available`, klik `[Apply]`
43. Klik `[Clear Field]`, klik `[Apply]`
44. Verifikasi field Status pada Filter Panel kosong kembali
45. Verifikasi keyword `Fixture.hardwareStock.derived.unitNameKeyword` tetap menyaring tabel: 9 baris
46. Verifikasi indikator sort Ascending tetap aktif pada Registered At
47. Klik header kolom Registered At dua kali sampai netral, klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-282: Menutup panel tanpa Apply membuang draft

48. Isi Status = `Available`, klik `[Apply]`
49. Ubah field Registered By menjadi `Fixture.hardwareStock.p17.e[12].registeredBy` tanpa klik `[Apply]`
50. Klik icon Filter untuk menutup panel
51. Klik icon Filter untuk membuka panel kembali
52. Verifikasi panel menampilkan nilai ter-Apply terakhir (Status = `Available`)
53. Verifikasi draft Registered By `Fixture.hardwareStock.p17.e[12].registeredBy` tidak tampil (field Registered By kosong)
54. Verifikasi tabel tetap menampilkan hasil filter terakhir yang di-Apply: 18 baris, lima teratas `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName`, `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[24].deviceName`, `Fixture.hardwareStock.p17.e[23].deviceName`
55. Klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACHS-283: Indikator filter aktif berupa badge titik

56. Verifikasi ikon Filter tanpa badge
57. Isi Registered By = `Fixture.hardwareStock.p17.e[10].registeredBy`, klik `[Apply]`
58. Verifikasi badge titik (tanpa angka) tampil pada ikon Filter saat panel terbuka
59. Klik icon Filter untuk menutup panel
60. Verifikasi badge titik (tanpa angka) tampil pada ikon Filter saat panel tertutup
61. Klik icon Filter untuk membuka panel, klik `[Clear Field]`, klik `[Apply]`
62. Verifikasi badge titik pada ikon Filter hilang

### TC-AC-ACHS-284: Filter independen dari Column Visibility

63. Isi Status = `Available`, klik `[Apply]`
64. Klik header kolom Actions `(⋯)`, hilangkan centang `Status`, tutup overlay Column Visibility
65. Klik icon Filter untuk menutup panel, klik icon Filter untuk membuka kembali Filter Panel
66. Verifikasi field Status tetap ada di Filter Panel dengan nilai `Available`
67. Verifikasi filter yang sudah di-Apply tetap berlaku: 18 baris, lima teratas `Fixture.hardwareStock.p17.e[27].deviceName`, `Fixture.hardwareStock.p17.e[26].deviceName`, `Fixture.hardwareStock.p17.e[25].deviceName`, `Fixture.hardwareStock.p17.e[24].deviceName`, `Fixture.hardwareStock.p17.e[23].deviceName`
68. Klik header kolom Actions `(⋯)`, ceklis kembali `Status`, tutup overlay Column Visibility
69. Klik `[Clear Field]`, klik `[Apply]`, klik icon Filter untuk menutup panel

### TC-AC-ACHS-316: Opsi Waiting for Approval mengikuti keberadaan unit Waiting for Approval

70. Buka Hardware > Stock, ketik Search `E2E287-{runId}`, tekan Enter
71. Klik row action `Detail` pada SKU milik spec, lalu klik Tab `Available`
72. Klik icon Filter, buka dropdown Status
73. Verifikasi dropdown Status memuat opsi `Available` dan `Waiting for Approval`
74. Tutup dropdown Status
75. Sesi API akun aktor menyetujui (Approve) Subject Register Duplicate unit Waiting for Approval milik spec hingga keputusan tersimpan
76. Tunggu aksi selesai (keputusan Subject tersimpan)
77. Muat ulang halaman (F5)
78. Klik icon Filter, buka dropdown Status
79. Verifikasi dropdown Status hanya memuat opsi `Available`
80. Tutup dropdown Status, klik icon Filter untuk menutup panel
81. Buka Hardware > Stock, klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`, klik Tab In Use
82. Klik icon Filter, buka dropdown Status
83. Verifikasi dropdown Status Tab In Use memuat opsi `Active`, `Damaged`, dan `Missing`
84. Verifikasi dropdown Status Tab In Use tidak memuat opsi `Waiting for Approval`
85. Tutup dropdown Status, klik icon Filter untuk menutup panel

## Notes

- Sumber TC: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md`. (bagian 4b, Stock Detail Tab Available). Seluruh TC sumber spec ini dikerjakan di sini.
- Konfirmasi keyword Search terhadap nilai penuh Pre-setup (#8): keyword Search `Fixture.hardwareStock.derived.unitNameKeyword` diturunkan dari `Fixture.hardwareStock.p17.e[20].deviceName` (Device Name unit nomor 20) tanpa karakter terakhir. Dicocokkan dengan Tabel E (Pre-setup #17): hanya Device Name unit nomor 20 sampai 28 yang diawali nilai itu, yaitu 9 baris di Tab Available (8 dengan Status `Available`, 1 Waiting for Approval), sesuai asersi langkah 33, 38, dan 45. Tidak ada perbedaan.
- Urutan TC: TC-AC-ACHS-275 sampai 284 pada Detail `Fixture.hardwareStock.p16.a[4].sku`, lalu TC-AC-ACHS-316 paling akhir karena memutuskan Subject milik spec dan membuka SKU lain. Filter Panel tetap terbuka setelah `[Apply]` sehingga langkah "Klik icon Filter" TC berikutnya tidak diulang kecuali TC-AC-ACHS-282, 283, dan 284 yang menutup dan membuka panel.
- Langkah penghubung (aksi tanpa `Verifikasi`): `Klik Tab` `Available` pada langkah 2 dan 71 (menggantikan langkah TC "Pastikan Tab Available aktif", `[KEPUTUSAN 2026-11-02]`), `[Clear Field]` lalu `[Apply]` antar-TC, pengosongan Search, pemulihan sort Registered At ke netral (TC-AC-ACHS-281), pengembalian kolom `Status` (TC-AC-ACHS-284), penutupan dropdown dan panel, serta navigasi antar-halaman pada TC-AC-ACHS-316.
- TC-AC-ACHS-316 bergantung pada TC-AC-ACHS-180 menurut kolom Dependensi TC; spec membangun Subject milik sendiri dan memutuskannya lewat sesi API, sehingga tidak menumpang hasil spec lain (S-06).
- Spec memiliki 85 langkah nominal di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Filter Stock Detail Tab Available pada akun dan dataset yang sama, kombinasi chip, AND, OR, dan indikator), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan tidak ada perulangan atau langkah bersyarat; TC-AC-ACHS-316 di akhir spec memakai data milik spec.
- Temuan untuk QA:
  - Nomor spec ini (287) sesudah spec penulis (240 sampai 284), padahal spec membaca baseline Pre-setup dan `suite.md` bagian "Urutan jalan" menempatkan spec baca di bawah nomor 240. Spec tidak direnumber; syarat pemulihan baseline ditulis di `## Prerequisites`, dan keputusan penomoran (folder baru di bawah 240) menunggu keputusan di luar spec ini.
  - TC, PRD, dan LLD yang dibaca tidak menyebut apakah halaman Stock Detail punya flag Guided Tooltip sendiri; spec menyetel flag halaman Stock Detail seperti flag Stock List dengan kemampuan yang disediakan tim FE.
  - TC-AC-ACHS-281 Expected b menulis lima baris teratas `Fixture.hardwareStock.p17.e[28].deviceName` sampai `24` (urutan default), sedangkan Expected c menyatakan sort Registered At Ascending tetap aktif (kelima baris teratas seharusnya `Fixture.hardwareStock.p17.e[20].deviceName` dan seterusnya); spec hanya mengasersi jumlah 9 baris dan indikator sort.
  - TC-AC-ACHS-283 menyebut "isi satu field" tanpa nilai; spec memakai Registered By = `Fixture.hardwareStock.p17.e[10].registeredBy` (pilihan spec).
  - TC-AC-ACHS-316 menyetujui Subject Pre-setup (`Fixture.hardwareStock.p17.e[28].deviceName`) pada "sesi lain" yang tidak didefinisikan; spec memakai SKU, unit, dan Subject milik spec dengan struktur sama dan sesi API akun aktor, sedangkan Tab In Use diamati pada Pre-setup read-only. Mekanisme seeding unit Waiting for Approval beserta Subject tidak didefinisikan di TC, PRD, atau LLD sehingga ditulis sebagai kemampuan "disediakan tim BE/FE".
  - TC-AC-ACHS-316 langkah 6 "Muat ulang halaman" mengandalkan retensi SKU dan tab aktif setelah F5 (NC-11 dalam TC).
