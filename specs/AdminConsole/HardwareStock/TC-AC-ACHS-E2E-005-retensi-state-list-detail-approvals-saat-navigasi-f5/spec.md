---
id: TC-AC-ACHS-E2E-005-retensi-state-list-detail-approvals-saat-navigasi-f5
title: "Retensi State List, Stock Detail, dan Approvals saat Navigasi dan Refresh"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-21
  - TC-AC-ACHS-22
  - TC-AC-ACHS-23
  - TC-AC-ACHS-24
  - TC-AC-ACHS-56
  - TC-AC-ACHS-57
coverage:
  web: automated
---

# Retensi State List, Stock Detail, dan Approvals saat Navigasi dan Refresh

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `{Fixture.hardwareStock.account.p01.totalControl.email}` (Pre-setup No 1; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca): Katalog SKU 30 baris (No 16), unit SKU `{Fixture.hardwareStock.p16.a[4].sku}` (No 17, 18), Approvals Tab Active 12 Subject dan Tab History 12 Subject yang memuat `{Fixture.hardwareStock.p18.f[1].client}` (Tab Active dan In Use `{Fixture.hardwareStock.p16.a[4].sku}`) dan `{Fixture.hardwareStock.derived.historyRequesterClient}` (Tab History) (No 21, 22). Tenant dalam keadaan baseline Pre-setup; suite menjalankan spec baca sebelum spec yang mengubah baseline (lihat suite.md).
- Kemampuan teknis: muat ulang halaman (F5); persistensi state memakai `sessionStorage` per tab browser (NC-11).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<kunci>`, identitas data bukan rahasia; berkas fixture belum ada dan dibuat tim FE/BE dari tabel Data Uji Pre-setup TC; nilai tidak ditulis ulang di spec ini):

  | Parameter | Pre-setup item | Peran/atribut | Fixture key |
  |---|---|---|---|
  | `{Fixture.hardwareStock.account.p01.totalControl.email}` | No 1 | email akun Pre-setup No 1 (kredensial login; password lewat env) | `Fixture.hardwareStock.account.p01.totalControl.email` |
  | `{Fixture.hardwareStock.p16.a[4].sku}` | No 16, 17, 18, Tabel A baris 4 | kode SKU Handheld Reader Long Range (25 Total Registered: 18 Available, 7 In Use) | `Fixture.hardwareStock.p16.a[4].sku` |
  | `{Fixture.hardwareStock.p16.a[4].brand}` | No 16, Tabel A baris 4 | Brand SKU Handheld Reader Long Range (kata kunci Search dan opsi Filter) | `Fixture.hardwareStock.p16.a[4].brand` |
  | `{Fixture.hardwareStock.p16.a[4].deviceName}` | No 16, Tabel A baris 4 | Device Name SKU Handheld Reader Long Range | `Fixture.hardwareStock.p16.a[4].deviceName` |
  | `{Fixture.hardwareStock.derived.searchDeviceNameU20}` | No 17, Tabel E baris N = 20 sampai 28 | keyword Search Tab Available: bagian Device Name unit 20 Tabel E yang juga cocok dengan unit 21 sampai 28 (`Scanner - 2`; 9 baris; sama dengan keyword TC-23 dan TC-24) | `Fixture.hardwareStock.derived.searchDeviceNameU20` |
  | `{Fixture.hardwareStock.p18.f[1].client}` | No 18, 21, 22, Tabel F baris 1 | Client unit In Use N = 1 (juga N = 2 dan 3); muncul di Tab Active; kata kunci Search | `Fixture.hardwareStock.p18.f[1].client` |
  | `{Fixture.hardwareStock.derived.historyRequesterClient}` | No 22, Tabel D baris 8 | kata kunci Search turunan: nilai kolom Requested By Tabel D baris 8 tanpa sufiks peran `(Client)`; muncul pada Requested By Tab History | `Fixture.hardwareStock.derived.historyRequesterClient` |

- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACHS-21: List state Stock List dipertahankan saat kembali dari Detail lewat breadcrumb

1. Ketik Search Brand `{Fixture.hardwareStock.p16.a[4].brand}`, tekan Enter
2. Klik icon Filter, pilih Type `Handheld Reader`, klik `[Apply]`
3. Klik header Total Registered (Ascending)
4. Ganti rows per page ke `25`
5. Klik teks SKU `{Fixture.hardwareStock.p16.a[4].sku}`
6. Klik segmen breadcrumb `Stock`
7. Verifikasi kotak Search Stock List berisi Brand `{Fixture.hardwareStock.p16.a[4].brand}`
8. Verifikasi Filter Type = `Handheld Reader` masih ter-set
9. Verifikasi sort Total Registered Ascending masih aktif
10. Verifikasi rows per page `25` masih ter-set

### TC-AC-ACHS-22: Refresh F5 mempertahankan state, klik ulang menu sidebar mereset

11. Klik menu Hardware > Stock di sidebar
12. Ketik Search Brand `{Fixture.hardwareStock.p16.a[4].brand}`, tekan Enter
13. Klik icon Filter, pilih Brand `{Fixture.hardwareStock.p16.a[4].brand}`, klik `[Apply]`
14. Tekan F5
15. Verifikasi kotak Search berisi Brand `{Fixture.hardwareStock.p16.a[4].brand}` setelah F5
16. Verifikasi Filter Brand = `{Fixture.hardwareStock.p16.a[4].brand}` masih ter-set setelah F5
17. Klik menu Hardware > Stock di sidebar
18. Verifikasi kotak Search kosong
19. Verifikasi Filter kosong
20. Verifikasi sort kembali default
21. Verifikasi paginasi kembali default (halaman 1, 10 baris per halaman)

### TC-AC-ACHS-23: State per tab Stock Detail dipertahankan saat pindah tab

22. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
23. Ketik Search Device Name unit `{Fixture.hardwareStock.derived.searchDeviceNameU20}` pada Tab Available, tekan Enter
24. Klik Tab `In Use`
25. Ketik Search Client `{Fixture.hardwareStock.p18.f[1].client}` pada Tab In Use, tekan Enter
26. Klik Tab `Available`
27. Verifikasi kotak Search Tab Available berisi Device Name unit `{Fixture.hardwareStock.derived.searchDeviceNameU20}`
28. Verifikasi kotak Search Tab Available tidak berisi Client `{Fixture.hardwareStock.p18.f[1].client}`
29. Klik Tab `In Use`
30. Verifikasi kotak Search Tab In Use berisi Client `{Fixture.hardwareStock.p18.f[1].client}`
31. Verifikasi kotak Search Tab In Use tidak berisi Device Name unit `{Fixture.hardwareStock.derived.searchDeviceNameU20}`

### TC-AC-ACHS-24: State Stock Detail dipertahankan saat F5, Add Stock membuka Tab Available default

32. Klik menu Hardware > Stock di sidebar
33. Klik `(⋯)` pada baris `{Fixture.hardwareStock.p16.a[4].sku}`, klik row action `Detail`
34. Ketik Search Device Name unit `{Fixture.hardwareStock.derived.searchDeviceNameU20}` pada Tab Available, tekan Enter
35. Ganti rows per page ke `25`
36. Tekan F5
37. Verifikasi SKU Info Header menampilkan Device Name `{Fixture.hardwareStock.p16.a[4].deviceName}` dan SKU `{Fixture.hardwareStock.p16.a[4].sku}` yang sama setelah F5
38. Verifikasi Tab Available aktif setelah F5
39. Verifikasi kotak Search berisi Device Name unit `{Fixture.hardwareStock.derived.searchDeviceNameU20}` setelah F5
40. Verifikasi rows per page `25` setelah F5
41. Klik `[Add Stock]`
42. Klik `[Cancel]` pada halaman Add Stock
43. Verifikasi Stock Detail Tab Available terbuka
44. Verifikasi kotak Search kosong
45. Verifikasi rows per page `10`
46. Verifikasi halaman 1 aktif

### TC-AC-ACHS-56: State tiap tab Approvals dipertahankan saat pindah tab

47. Klik menu Approvals > Hardware Stock di sidebar
48. Ketik Search Client `{Fixture.hardwareStock.p18.f[1].client}` pada Tab Active, tekan Enter
49. Klik Tab `History`
50. Ketik Search Client `{Fixture.hardwareStock.derived.historyRequesterClient}` pada Tab History, tekan Enter
51. Klik Tab `Active`
52. Verifikasi kotak Search Tab Active berisi Client `{Fixture.hardwareStock.p18.f[1].client}`
53. Verifikasi kotak Search Tab Active tidak berisi Client `{Fixture.hardwareStock.derived.historyRequesterClient}`
54. Klik Tab `History`
55. Verifikasi kotak Search Tab History berisi Client `{Fixture.hardwareStock.derived.historyRequesterClient}`
56. Verifikasi kotak Search Tab History tidak berisi Client `{Fixture.hardwareStock.p18.f[1].client}`

### TC-AC-ACHS-57: State Approvals dipertahankan saat F5 dan kembali dari dialog Detail Approval

57. Klik menu Approvals > Hardware Stock di sidebar
58. Ketik Search Client `{Fixture.hardwareStock.p18.f[1].client}` pada Tab Active, tekan Enter
59. Catat info jumlah entri Tab Active
60. Tekan F5
61. Verifikasi kotak Search berisi Client `{Fixture.hardwareStock.p18.f[1].client}` setelah F5
62. Klik `[Review]` pada baris pertama
63. Klik `[Cancel]` pada dialog Detail Approval
64. Verifikasi kotak Search berisi Client `{Fixture.hardwareStock.p18.f[1].client}` setelah dialog ditutup
65. Verifikasi info jumlah entri sama dengan yang dicatat pada langkah 59

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-21, 22, 23, 24, 56, 57). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 11, 17, 32, 47, dan 57 (klik menu di sidebar mereset Search, Sort, dan Filter sebelum TC berikutnya; bagian 4 konvensi), langkah 59 (mencatat info jumlah entri sebagai pembanding untuk langkah 65).
- Spec di atas smell 35 langkah (65 langkah). Alasan: seluruh blok adalah asersi retensi state pada satu pola (set state, pindah halaman atau tab, cek state) di tiga surface, keenam TC berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Tidak ada literal Pre-setup: spec merujuk lewat tabel Parameter Pre-setup (`{Fixture.hardwareStock.p16.a[4].sku}`, `{Fixture.hardwareStock.derived.searchDeviceNameU20}`, `{Fixture.hardwareStock.p18.f[1].client}`, `{Fixture.hardwareStock.derived.historyRequesterClient}`) sehingga tidak memerlukan pengecualian S-12. Kata kunci Search memakai nilai penuh kolom yang dirujuk, kecuali keyword Tab Available yang memakai keyword turunan `{Fixture.hardwareStock.derived.searchDeviceNameU20}` (substring yang sama dengan keyword TC); perbandingan hasil ada pada butir Perbandingan kata kunci di bawah.
  - TC-21 Expected menyebut keempat state dalam satu butir; spec memecahnya menjadi satu `Verifikasi` per state (langkah 7 sampai 10).
  - TC-22 Expected b ("sort dan paginasi kembali default") tidak mendefinisikan indikator default; spec mengasersi sort default umum dan paginasi halaman 1 dengan 10 baris per halaman.
  - TC-57 langkah 4 memilih "satu baris" tanpa menyebut baris; spec memakai baris pertama hasil Search Client `{Fixture.hardwareStock.p18.f[1].client}`. Expected b ("hasil search yang sama") tidak menyebut cara membandingkan; spec membandingkan kotak Search dan info jumlah entri.
  - TC-24 Expected b menyebut state default tanpa menyebut halaman; spec mengasersi Search kosong, rows per page `10`, dan halaman 1.
  - Perbandingan kata kunci Search terhadap substring TC (S-12): (1) Brand `Zebra` (TC-21, 22) sama dengan Brand penuh `Zebra`: hasil sama (SKU TC52, FX9600, RFD40). (2) Client `Sejahtera` (TC-23 Tab In Use) dan nilai penuh `PT Sejahtera`: hasil sama (3 unit In Use N = 1 sampai 3). (3) Client `Sejahtera` (TC-56, 57 Tab Active) dan `PT Sejahtera`: hasil sama (3 Subject: Tabel C baris 1, 5, 11). (4) `Apotek` (TC-56 Tab History) dan `Apotek Sehat Sentosa` (nilai Requested By tanpa sufiks `(Client)`): hasil sama (2 Subject: Tabel D baris 8 dan 12).
