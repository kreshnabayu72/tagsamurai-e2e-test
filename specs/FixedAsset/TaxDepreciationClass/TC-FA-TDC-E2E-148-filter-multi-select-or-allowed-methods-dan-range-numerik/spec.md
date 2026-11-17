---
id: TC-FA-TDC-E2E-148-filter-multi-select-or-allowed-methods-dan-range-numerik
title: "Filter: Multi-Select, Logika OR, Allowed Methods, dan Range Numerik"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-511
  - TC-FA-TDC-512
  - TC-FA-TDC-513
  - TC-FA-TDC-514
  - TC-FA-TDC-515
sourceRules: ["§4.1.1#r1", "§4.1.1#r4", "§4.1.1#r8", "§4.1.1#r12", "§4.1.1#r5", "§4.1.1#r6", "§4.1.1#r7", "§4.1.1#r9"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r1": 4
  "§4.1.1#r4": [4, 19, 20]
  "§4.1.1#r8": [4, 9, 10, 14, 15]
  "§4.1.1#r12": 4
  "§4.1.1#r5": 25
  "§4.1.1#r6": 25
  "§4.1.1#r7": 25
  "§4.1.1#r9": [25, 30, 34, 38]
coverage:
  web: automated
---

# Filter: Multi-Select, Logika OR, Allowed Methods, dan Range Numerik

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; tabel muat pada satu halaman. NB-SL terakhir diubah oleh `Rina P`, class lain `System` (user penyunting disediakan tim FE). Nilai: Useful Life NB-1 `4`, NB-OLD `5`, NB-2 `8`, BLD-NP dan NB-KHS `10`, NB-SL `16`, BLD-P dan NB-4 `20`, LAND `—`; Straight Line Rate NB-4 dan BLD-P `5%`, NB-SL `6.25%`, BLD-NP dan NB-KHS `10%`, NB-2 `12.5%`, NB-OLD `20%`, NB-1 `25%`, LAND `—`; Declining Balance Rate NB-4 `10%`, NB-KHS `20%`, NB-2 `25%`, NB-1 `50%`, class lain `—`; Used By NB-1 `5`, NB-SL `4`, NB-2 `3`, BLD-P `1`, class lain `0`; Allowed Methods `Straight Line · Declining Balance` pada NB-1, NB-2, NB-4, NB-KHS, `Straight Line` pada BLD-NP, BLD-P, NB-OLD, NB-SL, dan `—` pada LAND.
- Tabel parameter perulangan TC-FA-TDC-511 (Filter satu per satu), literal TC:

  | Field | Opsi | Baris hasil |
  |---|---|---|
  | Active | `Inactive` | NB-OLD |
  | Asset Type | `Land` | LAND |
  | Allowed Methods | `Declining Balance` | NB-1, NB-2, NB-4, NB-KHS |
  | Modified By | `Rina P` | NB-SL |

- Tabel parameter perulangan TC-FA-TDC-514 (range numerik inklusif), literal TC:

  | Field | Min | Max | Baris hasil |
  |---|---|---|---|
  | Useful Life (years) | `10` | `16` | BLD-NP, NB-KHS, NB-SL |
  | Straight Line Rate | `10` | `20` | BLD-NP, NB-2, NB-KHS, NB-OLD |
  | Declining Balance Rate | `20` | `50` | NB-1, NB-2, NB-KHS |
  | Used By | `3` | `5` | NB-1, NB-2, NB-SL |

- Data Dinamis: tidak ada.
- Kemampuan teknis: seeding sembilan class Example Data lewat API (`suite.md`).
- State global yang diubah: Filter pada tabel (dilepas oleh langkah di spec dan oleh `beforeEach` suite).

## Test Steps

### Filter satu per satu pada field multi-select (TC-FA-TDC-511)

1. Klik icon Filter

Untuk setiap baris tabel parameter TC-FA-TDC-511 pada Prerequisites, lakukan langkah 2 sampai 6.

2. Pilih opsi pada kolom Opsi untuk field pada kolom Field
3. Klik `[Apply]`
4. Verifikasi tabel hanya menampilkan baris pada kolom Baris hasil
5. Klik `[Clear Field]`
6. Klik `[Apply]`

### Filter Allowed Methods menyaring class yang mengizinkan minimal satu metode terpilih (TC-FA-TDC-512)

7. Pilih Allowed Methods `Straight Line`
8. Klik `[Apply]`
9. Verifikasi tabel menampilkan tepat 8 baris: NB-1, NB-2, NB-4, NB-SL, BLD-P, BLD-NP, NB-KHS, dan NB-OLD (termasuk class yang mengizinkan Straight Line bersama Declining Balance)
10. Verifikasi LAND tidak tampil
11. Klik `[Clear Field]`
12. Pilih Allowed Methods `Straight Line` dan `Declining Balance`
13. Klik `[Apply]`
14. Verifikasi 8 baris yang sama tampil tanpa baris ganda
15. Verifikasi LAND tidak tampil

### Logika OR dalam satu field: dua opsi Asset Type (TC-FA-TDC-513)

16. Klik `[Clear Field]`
17. Pilih Asset Type `Land` dan `Building`
18. Klik `[Apply]`
19. Verifikasi tabel menampilkan tepat tiga baris: LAND, BLD-NP, dan BLD-P (gabungan OR)
20. Verifikasi class Non-building tidak tampil

### Filter range numerik inklusif (TC-FA-TDC-514)

21. Klik `[Clear Field]`
22. Klik `[Apply]`

Untuk setiap baris tabel parameter TC-FA-TDC-514 pada Prerequisites, lakukan langkah 23 sampai 27.

23. Isi Min dan Max pada field sesuai kolom Field, Min, dan Max
24. Klik `[Apply]`
25. Verifikasi tabel hanya menampilkan baris pada kolom Baris hasil (batas Min dan Max inklusif)
26. Klik `[Clear Field]`
27. Klik `[Apply]`

### Filter range dengan salah satu batas kosong dan Min sama dengan Max (TC-FA-TDC-515)

28. Isi Used By Min `4` saja (Max kosong)
29. Klik `[Apply]`
30. Verifikasi (hanya Min) tabel menampilkan NB-1 (5) dan NB-SL (4)
31. Klik `[Clear Field]`
32. Isi Used By Max `0` saja (Min kosong)
33. Klik `[Apply]`
34. Verifikasi (hanya Max) tabel menampilkan BLD-NP, LAND, NB-4, NB-KHS, dan NB-OLD (Used By 0)
35. Klik `[Clear Field]`
36. Isi Used By Min `3` dan Max `3`
37. Klik `[Apply]`
38. Verifikasi (Min sama dengan Max) tabel hanya menampilkan NB-2 (3)
39. Klik `[Clear Field]`
40. Klik `[Apply]`

## Notes

- Langkah penghubung (S-03, S-09): langkah 5 dan 6 pada iterasi keempat (TC-FA-TDC-511 tidak membersihkan Filter sesudah Modified By; pembersihan ditambahkan agar tabel kembali penuh sebelum TC-FA-TDC-512), langkah 16 (membersihkan field sebelum TC-FA-TDC-513 supaya hanya Asset Type yang berlaku), langkah 21 dan 22 (melepas Filter sebelum perulangan TC-FA-TDC-514), langkah 26 dan 27 pada iterasi keempat dan langkah 39 dan 40 (pemulihan Filter di akhir TC). Langkah perulangan memakai idiom "Untuk setiap baris tabel ... (langkah X sampai Y)" (8b.7); `Verifikasi` yang diulang tetap satu per klausa.
- Filter Panel dibuka sekali pada langkah 1 (di luar perulangan TC-FA-TDC-511) dan tetap terbuka sesudah `[Apply]` sampai akhir spec (8b.9): iterasi perulangan dan blok TC-FA-TDC-512 sampai TC-FA-TDC-515 langsung memakai `[Clear Field]` atau memilih opsi tanpa klik icon Filter (klik icon itu menutup panel).
- Asersi "hanya menampilkan" mengasersi baris hasil tampil dan baris Example Data lainnya (dijamin ada di tabel penuh) tidak tampil; klausa "LAND tidak tampil" pada Useful Life dan "class tanpa Declining Balance tidak tampil" pada Declining Balance Rate tercakup oleh `Verifikasi` himpunan baris hasil pada langkah 25.
- Spec ini sekitar 40 langkah nominal dan sekitar 70 langkah setelah ekspansi perulangan, di atas ~35 langkah. Alasan: satu topik (Filter tabel utama) pada dataset Example Data yang sama, tiap blok TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan perulangan per field mengikuti idiom 8b.7 dengan parameter di Prerequisites.
- Temuan untuk QA:
  - TC-FA-TDC-512 Expected b "tanpa baris ganda" tidak menyebut cara membuktikan baris ganda; spec mengasersi 8 baris yang sama tanpa baris ganda apa adanya.
  - TC-FA-TDC-511 tidak menyebut pembersihan Filter sesudah Modified By; spec menambah pembersihan sebagai langkah penghubung.
  - TC-FA-TDC-514 Expected a menyebut "LAND tidak tampil" tanpa langkah observasi tambahan; tercakup oleh `Verifikasi` himpunan baris hasil.
  - Email akun Total Control dan nama user penyunting selain `Rina P` tidak tertulis di TC.
