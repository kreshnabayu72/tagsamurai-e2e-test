---
id: TC-FA-TDC-E2E-155-setup-column-tabel-utama-kolom-tersembunyi-default-dan-reset
title: "Setup Column Tabel Utama: Kolom Tersembunyi Secara Default dan Reset to Default"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-544
  - TC-FA-TDC-545
  - TC-FA-TDC-546
  - TC-FA-TDC-547
sourceRules: ["§5#b9", "§4.1.1#r2", "§9.5#r4"]
smoke: []
dependsOn: []
trace:
  "§5#b9": [6, 8, 14]
  "§4.1.1#r2": 13
  "§9.5#r4": [54, 57]
anchor: [4, 22, 24, 26, 36, 39, 45]
coverage:
  web: automated
---

# Setup Column Tabel Utama: Kolom Tersembunyi Secara Default dan Reset to Default

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Konfigurasi kolom awal adalah default: 10 kolom tampil (`Active`, `Class Code`, `Class Name`, `Asset Type`, `Useful Life (years)`, `Straight Line Rate`, `Declining Balance Rate`, `Allowed Methods`, `Used By`, `Effective From`) dan tiga kolom tersembunyi.
- Tabel parameter perulangan TC-FA-TDC-544, 545, dan 546 (kolom tersembunyi secara default), literal TC:

  | Kolom | Posisi semula (saat ditampilkan) |
  |---|---|
  | `Regulation Reference` | 11 |
  | `Modified By` | 12 |
  | `Last Updated` | 13 |

- Data Dinamis: tidak ada.
- Kemampuan teknis: seeding sembilan class Example Data lewat API (`suite.md`); Popup Setup Column dengan seret kolom (drag), icon Pin, dan `[Reset to Default]`; viewport yang membuat tabel dapat di-scroll horizontal; muat ulang halaman (F5); preferensi kolom tersimpan di browser dan dihapus di hook `after` (`suite.md`); pemulihan Setup Column dengan langkah eksplisit (8b.14, R-24).
- State global yang diubah: konfigurasi kolom tabel utama (tiga kolom ditampilkan, digeser, di-Pin, lalu dikembalikan; keadaan akhir default oleh `[Reset to Default]` langkah 53 dan 55). Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### Ceklis dan unceklis di Popup Setup Column: kolom tersembunyi secara default (TC-FA-TDC-544)

Untuk setiap baris tabel parameter pada Prerequisites, lakukan langkah 1 sampai 14.

1. Klik icon `⋯` pada header kolom Actions
2. Klik `Setup Column...`
3. Centang checkbox kolom pada baris tabel
4. Verifikasi kolom tampil di Live Preview beserta data selnya
5. Klik `[Save]`
6. Verifikasi kolom tampil di tabel
7. Refresh halaman (F5)
8. Verifikasi kolom tetap tampil di tabel setelah F5
9. Klik icon `⋯` pada header kolom Actions
10. Klik `Setup Column...`
11. Hapus centang checkbox kolom pada baris tabel
12. Klik `[Save]`
13. Verifikasi kolom Class Code tampil di tabel
14. Verifikasi kolom pada baris tabel tersembunyi kembali

### Menampilkan ketiga kolom (prasyarat TC-FA-TDC-545 dan 546)

15. Klik icon `⋯` pada header kolom Actions
16. Klik `Setup Column...`
17. Centang checkbox Regulation Reference, Modified By, dan Last Updated
18. Klik `[Save]`

### Geser urutan kolom di Popup Setup Column: kolom tersembunyi secara default (TC-FA-TDC-545)

Untuk setiap baris tabel parameter pada Prerequisites, lakukan langkah 19 sampai 30.

19. Klik icon `⋯` pada header kolom Actions
20. Klik `Setup Column...`
21. Seret kolom pada baris tabel ke posisi paling atas daftar
22. Verifikasi Live Preview menempatkan kolom sebagai kolom pertama
23. Klik `[Save]`
24. Verifikasi urutan tabel sama dengan Live Preview (kolom sebagai kolom pertama)
25. Refresh halaman (F5)
26. Verifikasi urutan tabel tetap sama setelah F5
27. Klik icon `⋯` pada header kolom Actions
28. Klik `Setup Column...`
29. Seret kolom kembali ke posisi semula pada baris tabel
30. Klik `[Save]`

### Pin dan unpin kolom di Popup Setup Column: kolom tersembunyi secara default (TC-FA-TDC-546)

Untuk setiap baris tabel parameter pada Prerequisites, lakukan langkah 31 sampai 45.

31. Klik icon `⋯` pada header kolom Actions
32. Klik `Setup Column...`
33. Klik icon Pin pada baris kolom
34. Klik `[Save]`
35. Scroll tabel horizontal
36. Verifikasi kolom membeku (sticky) saat tabel di-scroll horizontal
37. Refresh halaman (F5)
38. Scroll tabel horizontal
39. Verifikasi kolom tetap membeku setelah F5
40. Klik icon `⋯` pada header kolom Actions
41. Klik `Setup Column...`
42. Klik icon Pin kolom yang sama (Unpin)
43. Klik `[Save]`
44. Scroll tabel horizontal
45. Verifikasi kolom ikut bergeser saat scroll

### Reset to Default di Popup Setup Column (TC-FA-TDC-547)

46. Klik icon `⋯` pada header kolom Actions
47. Klik `Setup Column...`
48. Hapus centang checkbox Active
49. Seret Class Code ke posisi paling atas daftar
50. Klik `[Save]`
51. Klik icon `⋯` pada header kolom Actions
52. Klik `Setup Column...`
53. Klik `[Reset to Default]`
54. Verifikasi Live Preview kembali ke susunan default (urutan dan visibilitas awal)
55. Klik `[Save]`
56. Refresh halaman (F5)
57. Verifikasi susunan kolom tabel sama dengan default awal

## Notes

- Urutan TC dalam spec: TC-FA-TDC-544, 545, 546, 547. Langkah 15 sampai 18 menampilkan ketiga kolom sekaligus karena precondition d TC-FA-TDC-545 dan 546 mensyaratkan ketiga kolom "sudah ditampilkan lewat Popup Setup Column dan tersimpan"; langkah ini langkah penghubung (S-03) tanpa asersi.
- Langkah penghubung (S-03): langkah 9 sampai 12 pada tiap iterasi TC-FA-TDC-544 (menyembunyikan kolom kembali; Expected d TC-FA-TDC-544 dan pemulihan Setup Column, 8b.14, R-24), langkah 27 sampai 30 (menggeser kolom kembali ke posisi semula), dan Unpin langkah 40 sampai 43 (pemulihan Pin). Kolom 11 sampai 13 diseret kembali ke posisi semula pada langkah 29 dan keadaan akhir default dicapai oleh `[Reset to Default]` langkah 53 dan `[Save]` langkah 55 (TC-FA-TDC-547). Hook `after` hanya cadangan.
- Asersi absence langkah 14 didahului anchor positif langkah 13 (kolom Class Code tampil pada tabel yang sama; asersi tambahan di luar TC, 8b.2).
- Perulangan langkah 1 sampai 14, 19 sampai 30, dan 31 sampai 45 memakai idiom "Untuk setiap baris tabel ... (langkah X sampai Y)" (8b.7); `Verifikasi` yang diulang tetap satu per klausa.
- Spec ini 57 langkah nominal dan sekitar 139 langkah setelah ekspansi perulangan (tiga kolom), di atas ~35 langkah. Alasan: satu topik (Setup Column tabel utama, kolom tersembunyi secara default) pada dataset Example Data yang sama, tiap blok TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan perulangan per kolom mengikuti idiom 8b.7 dengan parameter di Prerequisites; S-01 mengharuskan satu `Verifikasi` per klausa.
- Temuan untuk QA:
  - TC-FA-TDC-545 dan 546 precondition d menyebut ketiga kolom "sudah ditampilkan dan tersimpan" tanpa cara; spec menambah langkah penghubung 15 sampai 18.
  - TC-FA-TDC-546 Expected "tetap membeku setelah F5" tidak menyebut scroll sesudah F5; spec menambah langkah scroll (langkah 38).
  - TC-FA-TDC-547 langkah 3 ("Klik `[Save]` dan refresh (F5)") dan Expected a ("Live Preview kembali ke susunan default") tidak menyebut apakah `[Reset to Default]` menyimpan sendiri; spec mengikuti TC.
  - TC-FA-TDC-544 sampai 546 tidak menyebut apakah Popup Setup Column menutup sesudah `[Save]`; spec mengasumsikan menutup.
  - Email akun Total Control tidak tertulis di TC.
