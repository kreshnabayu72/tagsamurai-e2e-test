---
id: TC-AC-ACHS-E2E-162-filter-tab-in-use-kombinasi-chip-and-or-dan-indikator
title: "Filter Tab In Use Kombinasi Chip AND OR dan Indikator"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-331
  - TC-AC-ACHS-332
  - TC-AC-ACHS-333
  - TC-AC-ACHS-334
  - TC-AC-ACHS-335
  - TC-AC-ACHS-336
  - TC-AC-ACHS-337
  - TC-AC-ACHS-338
  - TC-AC-ACHS-339
  - TC-AC-ACHS-340
coverage:
  web: automated
---

# Filter Tab In Use Kombinasi Chip AND OR dan Indikator

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API; tanpa intercept).
- Akun aktor: Total Control Principal (akun Pre-setup #1 TC; email `Fixture.hardwareStock.account.p01.totalControl.email`, nama tampil `Fixture.hardwareStock.account.p01.totalControl.fullName`), kata sandi `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: flag Guided Tooltip halaman Stock List disetel true di hook `before` suite dan dipulihkan di `after` (lihat suite.md). Suite serial (`parallel: false`).
- Data Pre-setup (hanya dibaca): SKU `Fixture.hardwareStock.p18.sku` dengan 7 unit In Use (Pre-setup #18, Tabel F TC); baris unit dirujuk `Fixture.hardwareStock.p18.f[n].<kolom>` dengan n = nilai kolom N Tabel F (kolom: deviceName, serialNumber, client, status, registeredBy, registeredAt, activatedAt, minPower, maxPower, currentPower); pada langkah dan tabel, sebuah baris unit ditulis dengan kunci `.deviceName`-nya. Client sama pada baris 1 sampai 3 (`Fixture.hardwareStock.p18.f[1].client`) dan baris 4 dan 5 (`Fixture.hardwareStock.p18.f[4].client`); baris 6 dan 7 berbeda. Urutan tampil default: `Fixture.hardwareStock.p18.f[7].deviceName`, `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[5].deviceName`, `Fixture.hardwareStock.p18.f[4].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName`. Keyword Search `Fixture.hardwareStock.derived.inUseClientA` = kata nama Client baris 1 setelah awalan badan usaha. Status unit 1 sampai 7: Damaged, Active, Missing, Active, Active, Damaged, Active (label UI). Status Damaged: baris 6 dan 1; Missing: baris 3; Client baris 1 dengan Status Active: baris 2.
- Pilihan spec (bukan nilai TC): TC-339 tidak menyebut field yang diisi ("isi satu field"); spec memakai Client = `Fixture.hardwareStock.p18.f[1].client`.
- Kolom Client disembunyikan di langkah 70 dan dimunculkan kembali di langkah 74; konfigurasi kolom Tab In Use tersimpan di browser dan dihapus hook `after` suite (kemampuan disediakan tim FE).
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture kanonis `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Skema kunci: baris tabel Pre-setup `p<NN>.<tabel huruf kecil>[<baris>].<kolom>` (Tabel A: `<baris>` = urutan baris 1 sampai 30, SKU `SKU-PAD-NN` pada baris 8+NN; Tabel E dan F: `<baris>` = nilai kolom N); akun `account.p<NN>.<peran>.<atribut>`; keyword turunan `derived.<nama>` (diturunkan dari kunci baris yang tertulis di kolom peran). `upper(<kunci>)` berarti nilai yang sama dalam huruf kapital. Spec tidak memerlukan pengecualian S-12 untuk nama literal.

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | Email akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | Nama tampil akun Total Control (Principal) | #1 Akun Principal Total Control | akun login aktor spec ini (`Spectra.env.AC_TC_PASSWORD`) | `Fixture.hardwareStock.account.p01.totalControl.fullName` |
  | SKU Long Range In Use | #18 SKU RFD40 (sama dengan Tabel A baris 4) | kode SKU Handheld Reader Long Range dengan 7 unit In Use (#16, #18) | `Fixture.hardwareStock.p18.sku` |
  | Client baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Client unit nomor 1, Tabel F (#18) | `Fixture.hardwareStock.p18.f[1].client` |
  | Device Name baris 1 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 1, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[1].deviceName` |
  | Device Name baris 2 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 2, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[2].deviceName` |
  | Device Name baris 3 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 3, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[3].deviceName` |
  | Client baris 4 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Client unit nomor 4, Tabel F (#18) | `Fixture.hardwareStock.p18.f[4].client` |
  | Device Name baris 4 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 4, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[4].deviceName` |
  | Device Name baris 5 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 5, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[5].deviceName` |
  | Device Name baris 6 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 6, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[6].deviceName` |
  | Device Name baris 7 Tabel F | #18 Unit In Use SKU RFD40 (Tabel F) | Device Name unit nomor 7, Tabel F (#18) (identitas baris unit pada hasil Search, Filter, Sort, dan berkas) | `Fixture.hardwareStock.p18.f[7].deviceName` |
  | Nilai turunan inUseClientA | turunan dari `Fixture.hardwareStock.p18.f[1].client` | keyword Search: kata nama Client baris 1 Tabel F setelah awalan badan usaha (`Sejahtera`; substring Client baris 1 sampai 3; sama dengan keyword TC-AC-ACHS-318) | `Fixture.hardwareStock.derived.inUseClientA` |

## Test Steps

### Dua opsi satu field dihitung OR (TC-AC-ACHS-331)

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p18.sku` di Stock List
2. Klik Tab `In Use`
3. Klik icon Filter
4. Buka dropdown Status, centang `Damaged` lalu `Missing`
5. Klik `[Apply]`
6. Verifikasi dua chip `Damaged` dan `Missing` tampil di dalam closed-state field, sejajar
7. Verifikasi tabel menampilkan gabungan (OR) 3 baris: `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName`
8. Klik `[Clear Field]`, klik `[Apply]`

### Hapus satu chip lewat (X) menyinkronkan checkbox (TC-AC-ACHS-332)

9. Centang `Damaged` dan `Missing` pada dropdown Status
10. Klik `(X)` pada chip `Damaged` (tanpa membuka dropdown)
11. Verifikasi chip `Damaged` hilang
12. Verifikasi chip `Missing` tetap ada
13. Buka dropdown Status
14. Verifikasi checkbox `Damaged` di dalam dropdown ter-uncheck
15. Verifikasi checkbox `Missing` tetap tercentang
16. Klik `[Apply]`
17. Verifikasi tabel menampilkan 1 baris: `Fixture.hardwareStock.p18.f[3].deviceName`
18. Klik `[Clear Field]`, klik `[Apply]`

### Uncheck di dalam dropdown menghapus chip (TC-AC-ACHS-333)

19. Centang `Damaged` dan `Missing` pada dropdown Status
20. Dengan dropdown tetap terbuka, uncheck `Missing`
21. Verifikasi chip `Missing` hilang dari field
22. Verifikasi chip `Damaged` tetap ada
23. Tutup dropdown, klik `[Apply]`
24. Verifikasi tabel menampilkan 2 baris: `Fixture.hardwareStock.p18.f[6].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName`
25. Klik `[Clear Field]`, klik `[Apply]`

### Dua field berbeda dihitung AND (TC-AC-ACHS-334)

26. Isi Client = `Fixture.hardwareStock.p18.f[1].client` dan Status = `Active`
27. Klik `[Apply]`
28. Verifikasi tabel menampilkan irisan 1 baris: `Fixture.hardwareStock.p18.f[2].deviceName`
29. Klik `[Clear Field]`, klik `[Apply]`

### Search lalu Filter (TC-AC-ACHS-335)

30. Klik icon Filter untuk menutup panel
31. Ketik Search `Fixture.hardwareStock.derived.inUseClientA`, tekan Enter
32. Klik icon Filter
33. Isi Client = `Fixture.hardwareStock.p18.f[1].client`
34. Klik `[Apply]`
35. Verifikasi tabel menampilkan irisan Search dan Filter 3 baris: `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName`
36. Verifikasi keyword `Fixture.hardwareStock.derived.inUseClientA` tetap terisi di kotak Search
37. Klik `[Clear Field]`, klik `[Apply]`
38. Klik icon `(←)` pada kotak Search

### Filter lalu Search (TC-AC-ACHS-336)

39. Isi Client = `Fixture.hardwareStock.p18.f[1].client`, klik `[Apply]`
40. Ketik Search `Fixture.hardwareStock.derived.inUseClientA`, tekan Enter
41. Verifikasi tabel menampilkan 3 baris: `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName`, identik dengan hasil urutan Search lalu Filter (langkah 35)
42. Klik icon `(←)` pada kotak Search
43. Klik `[Clear Field]`, klik `[Apply]`

### Clear Field mempertahankan Search dan Sort (TC-AC-ACHS-337)

44. Ketik Search `Fixture.hardwareStock.derived.inUseClientA`, tekan Enter
45. Klik header kolom Activated At sekali (Ascending)
46. Isi Client = `Fixture.hardwareStock.p18.f[1].client`, klik `[Apply]`
47. Klik `[Clear Field]`, klik `[Apply]`
48. Verifikasi field Client kosong kembali
49. Verifikasi keyword `Fixture.hardwareStock.derived.inUseClientA` tetap menyaring: 3 baris `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName` (himpunan baris, urutan tidak diasersi)
50. Verifikasi indikator sort Ascending tetap aktif pada Activated At
51. Klik header kolom Activated At dua kali sampai netral
52. Klik icon `(←)` pada kotak Search

### Menutup panel tanpa Apply membuang draft (TC-AC-ACHS-338)

53. Isi Client = `Fixture.hardwareStock.p18.f[1].client`, klik `[Apply]`
54. Ubah field Status menjadi `Active` tanpa klik `[Apply]`
55. Klik icon Filter untuk menutup panel
56. Klik icon Filter untuk membuka panel kembali
57. Verifikasi panel menampilkan nilai ter-Apply terakhir: Client = `Fixture.hardwareStock.p18.f[1].client`
58. Verifikasi draft Status `Active` tidak tampil
59. Verifikasi tabel tetap menampilkan hasil filter terakhir yang di-Apply: 3 baris `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName`
60. Klik `[Clear Field]`, klik `[Apply]`

### Indikator filter aktif (TC-AC-ACHS-339)

61. Verifikasi ikon Filter tanpa badge
62. Isi Client = `Fixture.hardwareStock.p18.f[1].client`, klik `[Apply]`
63. Verifikasi badge titik (tanpa angka) tampil pada ikon Filter saat panel terbuka
64. Klik icon Filter untuk menutup panel
65. Verifikasi badge titik (tanpa angka) tampil pada ikon Filter saat panel tertutup
66. Klik icon Filter untuk membuka panel
67. Klik `[Clear Field]`, klik `[Apply]`
68. Verifikasi badge titik pada ikon Filter hilang

### Filter independen dari Column Visibility (TC-AC-ACHS-340)

69. Isi Client = `Fixture.hardwareStock.p18.f[1].client`, klik `[Apply]`
70. Klik `(⋯)` header kolom Actions, uncheck `Client`
71. Buka kembali Filter Panel
72. Verifikasi field Client tetap ada di Filter Panel dengan nilai `Fixture.hardwareStock.p18.f[1].client`
73. Verifikasi filter yang sudah di-Apply tetap berlaku: 3 baris `Fixture.hardwareStock.p18.f[3].deviceName`, `Fixture.hardwareStock.p18.f[2].deviceName`, `Fixture.hardwareStock.p18.f[1].deviceName`
74. Klik `(⋯)` header kolom Actions, check `Client`
75. Klik `[Clear Field]`, klik `[Apply]`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-331 sampai 340). Tidak ada TC hanya-BE di spec ini.
- Konfirmasi S-12 (keyword Search, #8): keyword turunan `Fixture.hardwareStock.derived.*` pada spec ini adalah substring yang sama dengan keyword literal TC (bukan nilai kolom penuh): `Sejahtera` (TC-AC-ACHS-318). Dicocokkan dengan Tabel F Pre-setup #18 (Client baris 1 sampai 3 = 3 baris); himpunan hasil identik dengan hasil di TC. Tidak ada perbedaan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 8, 18, 25, 29, 37, 43, 47 (bagian TC-337), 60, 67 (bagian TC-339), dan 75 (`[Clear Field]` lalu `[Apply]` memulihkan Filter, S-09); langkah 38, 42, 52 (klik `(←)` pada Search mereset Search); langkah 30, 55, 64, dan 66 (menutup dan membuka panel Filter sesuai kebutuhan blok); langkah 51 (kembali netral setelah sort Activated At); langkah 74 (check `Client` kembali, memulihkan Column Visibility).
- Rujukan langkah memakai nomor langkah spec ini (R-04): langkah 41 merujuk langkah 35; Prerequisites merujuk langkah 70 dan 74.
- Spec melewati sekitar 35 langkah (75 langkah): alasan, semua blok satu surface (Filter Panel Tab In Use) dan satu dataset; tiap blok memulihkan Filter (dan Search/Sort bila diubah) sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; topik satu dataset dipertahankan satu spec (prinsip 1).
- Nilai Pre-setup tidak ditulis literal; dirujuk lewat nomor item Pre-setup (#18, Tabel F) dan kunci fixture, nilai dibaca penulis script dari tabel TC (R-06); tidak ada pengecualian S-12 dipakai. Teks UI asli (label kolom, placeholder, tooltip, empty state, label Status) tetap ditulis verbatim.
- Temuan untuk QA:
  - TC-337 Expected b menulis urutan baris `3, 2, 1` setelah sort Activated At Ascending, padahal Ascending Activated At menempatkan `Fixture.hardwareStock.p18.f[1].deviceName` di atas; spec mengasersi himpunan 3 baris tanpa urutan.
  - TC-339 langkah 5 ("isi satu field") tidak menyebut field; spec memilih Client = `Fixture.hardwareStock.p18.f[1].client` (Prerequisites).
  - TC-332 dan TC-333 tidak menyebut apakah dropdown ditutup sebelum klik `[Apply]` (TC-333 menyebutnya, TC-332 tidak); spec mengikuti TC.
