---
id: TC-AC-ACHS-E2E-182-filter-approvals-tab-active-kombinasi-chip-and-or-dan-indikator
title: "Filter Approvals Tab Active Kombinasi Chip AND OR dan Indikator"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-380
  - TC-AC-ACHS-381
  - TC-AC-ACHS-382
  - TC-AC-ACHS-383
  - TC-AC-ACHS-384
  - TC-AC-ACHS-385
  - TC-AC-ACHS-386
  - TC-AC-ACHS-387
  - TC-AC-ACHS-388
  - TC-AC-ACHS-389
coverage:
  web: automated
---

# Filter Approvals Tab Active Kombinasi Chip AND OR dan Indikator

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
  | Category baris #n (n = 1 sampai 12) | #21 Tabel C | Long Range pada #1 dan #10; Short Range pada #2, #3, #5, #6, #7, #8, #11; Smart Fixed Reader pada #4; BLE Gateway pada #12; `—` pada #9 | `Fixture.hardwareStock.p21.c[n].category` |
  | Matched Identifier baris #n (n = 1 sampai 12) | #21 Tabel C | Serial Number atau MAC address unik tiap baris, identitas baris hasil; #3, #9, #12 berformat MAC | `Fixture.hardwareStock.p21.c[n].matchedIdentifier` |
  | Requested By baris #n (n = 1 sampai 12) | #21 Tabel C | Client, Distributor, atau Principal (Pre-setup #23) dengan label peran dalam kurung; Distributor pada #3, #6, #8, #10 | `Fixture.hardwareStock.p21.c[n].requestedBy` |
  | Keyword Search nama Client | #21 Tabel C | diturunkan dari `Fixture.hardwareStock.p21.c[5].requestedBy`: nama Client tanpa awalan badan usaha dan tanpa label peran dalam kurung; nama yang sama muncul pada Existing Record #1 dan #11, sehingga Search menghasilkan tepat tiga baris #1, #5, #11 (semua Activation Collision) | `Fixture.hardwareStock.derived.clientCoreNameActive` |
- Pilihan spec (bukan nilai TC): TC-388 langkah 4 ("isi satu field") tidak menyebut field; spec memakai Type = `Register Duplicate`. TC-387 memakai Category `Handheld Reader - Long Range` sebagai draft.
- Kolom Type disembunyikan di langkah 70 dan dimunculkan kembali di langkah 74; konfigurasi kolom Tab Active disimpan di browser dan dihapus hook `after` suite (kemampuan disediakan tim FE).

## Test Steps

### Dua opsi satu field dihitung OR (TC-AC-ACHS-380)

1. Buka Approvals > Hardware Stock
2. Klik Tab `Active`
3. Klik icon Filter
4. Buka dropdown Type, centang `Register Duplicate` lalu `Activation Collision`
5. Klik `[Apply]`
6. Verifikasi dua chip `Register Duplicate` dan `Activation Collision` tampil di dalam closed-state field, sejajar
7. Verifikasi tabel menampilkan gabungan (OR) 12 baris, lima teratas: #1, #2, #3, #4, #5
8. Klik `[Clear Field]`, klik `[Apply]`

### Hapus satu chip lewat (X) menyinkronkan checkbox (TC-AC-ACHS-381)

9. Centang `Register Duplicate` dan `Activation Collision` pada dropdown Type
10. Klik `(X)` pada chip `Register Duplicate` (tanpa membuka dropdown)
11. Verifikasi chip `Register Duplicate` hilang
12. Verifikasi chip `Activation Collision` tetap ada
13. Buka dropdown Type
14. Verifikasi checkbox `Register Duplicate` di dalam dropdown ter-uncheck
15. Verifikasi checkbox `Activation Collision` tetap tercentang
16. Klik `[Apply]`
17. Verifikasi tabel menampilkan 6 baris: #1, #4, #5, #9, #11, #12
18. Klik `[Clear Field]`, klik `[Apply]`

### Uncheck di dalam dropdown menghapus chip (TC-AC-ACHS-382)

19. Centang `Register Duplicate` dan `Activation Collision` pada dropdown Type
20. Dengan dropdown tetap terbuka, uncheck `Activation Collision`
21. Verifikasi chip `Activation Collision` hilang dari field
22. Verifikasi chip `Register Duplicate` tetap ada
23. Tutup dropdown, klik `[Apply]`
24. Verifikasi tabel menampilkan 6 baris: #2, #3, #6, #7, #8, #10
25. Klik `[Clear Field]`, klik `[Apply]`

### Dua field berbeda dihitung AND (TC-AC-ACHS-383)

26. Isi Type = `Register Duplicate` dan Category = `Handheld Reader - Long Range`
27. Klik `[Apply]`
28. Verifikasi tabel menampilkan irisan 1 baris: #10
29. Klik `[Clear Field]`, klik `[Apply]`

### Search lalu Filter (TC-AC-ACHS-384)

30. Klik icon Filter untuk menutup panel
31. Ketik Search `Fixture.hardwareStock.derived.clientCoreNameActive`, tekan Enter
32. Klik icon Filter
33. Isi Type = `Register Duplicate`
34. Klik `[Apply]`
35. Verifikasi empty state `No results found` dan tabel menampilkan irisan Search dan Filter 0 baris
36. Verifikasi keyword `Fixture.hardwareStock.derived.clientCoreNameActive` tetap terisi di kotak Search
37. Klik `[Clear Field]`, klik `[Apply]`
38. Klik icon `(←)` pada kotak Search

### Filter lalu Search (TC-AC-ACHS-385)

39. Isi Type = `Register Duplicate`, klik `[Apply]`
40. Ketik Search `Fixture.hardwareStock.derived.clientCoreNameActive`, tekan Enter
41. Verifikasi empty state `No results found` dan tabel menampilkan 0 baris, identik dengan hasil urutan Search lalu Filter (langkah 35)
42. Klik icon `(←)` pada kotak Search
43. Klik `[Clear Field]`, klik `[Apply]`

### Clear Field mempertahankan Search dan Sort (TC-AC-ACHS-386)

44. Ketik Search `Fixture.hardwareStock.derived.clientCoreNameActive`, tekan Enter
45. Klik header kolom Type sekali (Ascending)
46. Isi Type = `Register Duplicate`, klik `[Apply]`
47. Klik `[Clear Field]`, klik `[Apply]`
48. Verifikasi field Type kosong kembali
49. Verifikasi keyword `Fixture.hardwareStock.derived.clientCoreNameActive` tetap menyaring: 3 baris #1, #5, #11
50. Verifikasi indikator sort Ascending tetap aktif pada Type
51. Klik header kolom Type dua kali sampai netral
52. Klik icon `(←)` pada kotak Search

### Menutup panel tanpa Apply membuang draft (TC-AC-ACHS-387)

53. Isi Type = `Register Duplicate`, klik `[Apply]`
54. Ubah field Category menjadi `Handheld Reader - Long Range` tanpa klik `[Apply]`
55. Klik icon Filter untuk menutup panel
56. Klik icon Filter untuk membuka panel kembali
57. Verifikasi panel menampilkan nilai ter-Apply terakhir: Type = `Register Duplicate`
58. Verifikasi draft Category `Handheld Reader - Long Range` tidak tampil
59. Verifikasi tabel tetap menampilkan hasil filter terakhir yang di-Apply: 6 baris #2, #3, #6, #7, #8, #10
60. Klik `[Clear Field]`, klik `[Apply]`

### Indikator filter aktif (TC-AC-ACHS-388)

61. Verifikasi ikon Filter tanpa badge
62. Isi Type = `Register Duplicate`, klik `[Apply]`
63. Verifikasi badge titik (tanpa angka) tampil pada ikon Filter saat panel terbuka
64. Klik icon Filter untuk menutup panel
65. Verifikasi badge titik (tanpa angka) tampil pada ikon Filter saat panel tertutup
66. Klik icon Filter untuk membuka panel
67. Klik `[Clear Field]`, klik `[Apply]`
68. Verifikasi badge titik pada ikon Filter hilang

### Filter independen dari Column Visibility (TC-AC-ACHS-389)

69. Isi Type = `Register Duplicate`, klik `[Apply]`
70. Klik `(⋯)` header kolom Actions, uncheck `Type`
71. Buka kembali Filter Panel
72. Verifikasi field Type tetap ada di Filter Panel dengan nilai `Register Duplicate`
73. Verifikasi filter yang sudah di-Apply tetap berlaku: 6 baris #2, #3, #6, #7, #8, #10
74. Klik `(⋯)` header kolom Actions, check `Type`
75. Klik `[Clear Field]`, klik `[Apply]`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-380 sampai 389). Tidak ada TC hanya-BE di spec ini.
- Nilai Pre-setup tidak ditulis literal; dirujuk lewat nomor item Pre-setup (#21/#22, Tabel C/D) dan kunci fixture, nilai dibaca penulis script dari tabel TC (R-06); tidak ada pengecualian S-12 dipakai. Teks antarmuka asli (nama kolom, label Type dan Category, placeholder, tooltip, teks empty state, nama berkas unduhan) tetap ditulis verbatim.
- Langkah penghubung (bukan dari langkah TC): langkah 8, 18, 25, 29, 37, 43, 47 (bagian TC-386), 60, 67, 75 (`[Clear Field]` lalu `[Apply]` memulihkan Filter, S-09); langkah 38, 42, 52 (klik `(←)` mereset Search); langkah 30, 55, 64, 66 (menutup dan membuka panel Filter); langkah 51 (sort Type kembali netral); langkah 74 (check `Type` kembali, memulihkan Column Visibility); langkah 2 (klik Tab `Active`). Langkah 41 merujuk langkah 35 (R-04).
- Spec melewati sekitar 35 langkah (75 langkah): alasan, semua blok satu surface (Filter Panel Approvals Tab Active) dan satu dataset read-only; tiap blok memulihkan Filter (dan Search atau Sort bila diubah) sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; topik satu dataset tetap satu spec (prinsip 1).
- Konfirmasi (#8): `Fixture.hardwareStock.derived.clientCoreNameActive` sama dengan substring yang ditulis TC-384, 385, dan 386 (nama inti Client, bukan nilai kolom penuh); pada Tabel C `Fixture.hardwareStock.derived.clientCoreNameActive` menghasilkan #1, #5, #11 (semua Activation Collision), sehingga irisan dengan Type = `Register Duplicate` kosong sesuai TC. Tidak ada perbedaan.
- Temuan untuk QA:
  - TC-380 Expected b hanya menyebut lima baris teratas dari 12 baris; spec mengasersi 12 baris dan lima teratas.
  - TC-384 dan TC-385: Search `Fixture.hardwareStock.derived.clientCoreNameActive` pada Subject Register Duplicate menghasilkan 0 baris karena kata `Fixture.hardwareStock.derived.clientCoreNameActive` hanya ada pada Subject Activation Collision; spec mengikuti TC.
  - TC-388 langkah 4 ("isi satu field") tidak menyebut field; spec memilih Type = `Register Duplicate`.
