---
id: TC-GS-UOM-E2E-053-detail-item-type-list-screening-dan-empty
title: "Unit Detail: Screening, Item Type List, Empty State, Accordion, Klik Baris, dan Tanpa Aksi Kelola"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-191
  - TC-GS-UOM-192
  - TC-GS-UOM-197
  - TC-GS-UOM-199
  - TC-GS-UOM-200
  - TC-GS-UOM-206
  - TC-GS-UOM-256
  - TC-GS-UOM-257
coverage:
  web: automated
tags: [principal]
---

# Unit Detail: Screening, Item Type List, Empty State, Accordion, Klik Baris, dan Tanpa Aksi Kelola

## Prerequisites

- Mode: FE+BE.
- Akun yang dipakai (dengan langkah ganti akun eksplisit):
  - Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Akun aktor pertama dan akun default suite: login di hook `before` suite. Dipakai langkah 1 sampai 37.
  - Total Control (Principal), Hendra Wijaya, `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 8), kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`. Login lewat UI di langkah 39. Dipakai langkah 39 sampai 59.
- Environment variable: `GS_TC_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel true oleh hook suite untuk akun aktor yang dipakai suite (lihat bagian "Hook suite" di `suite.md`); untuk akun Principal, mekanisme penyetelan flag disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`). Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, Sari Dewi) bila spec berakhir di akun Principal.
- Data Pre-setup (tetap di environment, hanya dibaca, tanpa suffix `{runId}`; spec ini tidak membuat atau mengubah data sehingga tidak ada seeding dan cleanup data):
  - Client A: `Pieces` (Symbol `pc`; Item Type FAMS `Laptop` dan `Monitor`, Item Type Supply `Printer Ink`; Total Item 3). Referensi Supply (SAMS) disiapkan lewat fixture backend (NC-09), disediakan tim FE. `Meter` (Symbol `m`; bebas relasi).
  - Principal: `Watt` (Symbol `W`; Device Name `BLE Gateway` dan `Handheld Reader`, tanpa Asset Name maupun Item Name). Entri Changelog Principal: sedikitnya satu baris pada Modal Changelog instance Principal untuk TC-GS-UOM-256 (disediakan tim FE; lihat Temuan untuk QA).
- Baris unit dicari lewat Search nama unit (`Pieces`, `Meter`, `Watt`) supaya tidak bergantung pada halaman Pagination.
- Kemampuan teknis: login/logout dalam satu spec (ganti akun Client A ke Principal); hook `after` logout dan login ulang sebagai akun default suite; klik baris tabel; membaca state accordion (expanded/collapsed) dan arah chevron.
- Precondition TC-GS-UOM-191, 192, 197, 199, 200, 206: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement. TC-GS-UOM-256, 257: login sebagai Total Control (Principal); Watt dipakai BLE Gateway dan Handheld Reader.

## Test Steps

### TC-GS-UOM-191: Screening Modal Unit Detail pada instance client

1. Ketik Search `Pieces`, tekan Enter
2. Klik `⋯` pada baris Pieces
3. Klik Detail
4. Verifikasi Header: Title `Unit Detail`
5. Verifikasi Header: icon `[✕]`
6. Verifikasi Header tanpa tombol teks Close
7. Verifikasi General Info: Unit Name `Pieces`
8. Verifikasi General Info: Symbol `pc`
9. Verifikasi General Info: `Total Item` `3`
10. Verifikasi accordion `Item Type List` expanded
11. Verifikasi Search accordion Item Type List dengan placeholder `Search item type or product...`
12. Verifikasi Filter Product dan Download tampil pada accordion Item Type List
13. Verifikasi kolom tabel `Item Type | Product`
14. Verifikasi accordion `Device Name List` tidak dirender sama sekali (instance milik Client, entitas tanpa Admin Console)

### TC-GS-UOM-192: Isi dan urutan default Item Type List

15. Verifikasi baris A-Z: `Laptop` (Fixed Asset), `Monitor` (Fixed Asset), `Printer Ink` (Supply)
16. Verifikasi tidak ada kolom Model/Type
17. Verifikasi accordion Item Type List tanpa pagination

### TC-GS-UOM-200: Accordion dapat di-collapse dan di-expand

18. Klik header Item Type List
19. Verifikasi accordion Item Type List collapsed
20. Verifikasi chevron berputar menunjuk state collapsed
21. Klik header Item Type List
22. Verifikasi accordion Item Type List expanded
23. Verifikasi chevron berputar menunjuk state expanded

### TC-GS-UOM-199: Klik baris Item Type List tidak menavigasi

24. Klik baris `Laptop`
25. Verifikasi tidak ada aksi maupun navigasi
26. Verifikasi pengguna tetap di Modal Unit Detail

### TC-GS-UOM-206: Modal Unit Detail ditutup lewat icon close dan Esc

27. Klik `[✕]`
28. Verifikasi Modal Unit Detail tertutup
29. Klik `⋯` pada baris Pieces, lalu klik Detail
30. Tekan Esc
31. Verifikasi Modal Unit Detail tertutup

### TC-GS-UOM-197: Empty state Item Type List untuk unit tanpa Item Type

32. Ganti isi kotak search dengan `Meter`, tekan Enter
33. Klik `⋯` pada baris dengan Unit Name `Meter`
34. Klik Detail
35. Verifikasi empty state Title `No item types linked`
36. Verifikasi empty state Description `No products or items currently reference this measurement unit.`
37. Klik `[✕]`

### Ganti akun ke Total Control (Principal)

38. Logout dari akun Total Control Client A
39. Login sebagai Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` dengan `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`
40. Buka Global Settings > Master Reference > Measurement

### TC-GS-UOM-256: Klik baris tabel Device Name List dan Changelog tidak menavigasi

41. Ketik Search `Watt`, tekan Enter
42. Klik `⋯` pada baris Watt
43. Klik Detail
44. Klik baris `BLE Gateway` pada Device Name List
45. Verifikasi klik baris Device Name List tidak menjalankan aksi maupun navigasi
46. Verifikasi pengguna tetap di Modal Unit Detail
47. Verifikasi tidak ada row action pada tabel Device Name List
48. Klik `[✕]`
49. Klik icon Changelog
50. Klik baris pertama Changelog
51. Verifikasi klik baris Changelog tidak menjalankan aksi maupun navigasi
52. Verifikasi tidak ada row action pada tabel Changelog
53. Klik `[✕]` pada Modal Changelog

### TC-GS-UOM-257: Modal Unit Detail tidak menyediakan aksi kelola Item Type atau Device Name

54. Klik `⋯` pada baris Watt, lalu klik Detail
55. Verifikasi kontrol pada accordion Item Type List hanya Search, Filter Product, dan Download
56. Verifikasi kontrol pada accordion Device Name List hanya Search
57. Verifikasi icon `[✕]` tampil
58. Verifikasi tidak ada tombol tambah, ubah, atau hapus Item Type maupun Device Name
59. Verifikasi tidak ada row action pada kedua tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-UOM-191, 192, 200, 199, 206, 197, lalu (Principal) 256, 257. Alasan: Detail Pieces dibuka sekali untuk 191, 192, 200, 199 (precondition sama); TC-GS-UOM-206 menutup modal sehingga dijalankan sesudahnya; TC-GS-UOM-197 membuka Detail unit lain.
- Pembagian TC lintas spec: spec ini memegang screening struktur Detail dan empty state Item Type List; filter dan sort Item Type List ada di `TC-GS-UOM-E2E-054-detail-item-type-list-search-filter-sort-dan-chip`; Device Name List Principal dan Distributor di `TC-GS-UOM-E2E-055-detail-device-name-list-principal-dan-distributor`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 41 (Search untuk menemukan baris target unit), langkah 29 (membuka kembali Detail Pieces untuk uji Esc), langkah 32 (mengganti Search), langkah 37, 48, 53 (menutup modal), dan langkah 38 sampai 40 (ganti akun Client A ke Principal; hook `after` memulihkan sesi).
- Ganti akun (butir b prinsip "Beda akun" konvensi 3): bagian Principal (TC-GS-UOM-256, 257) tetap bermakna walau bagian Client A gagal, karena memulai dari login dan pembukaan layar sendiri.
- Spec ini melewati sekitar 35 langkah (59 langkah). Alasan: semua blok baca-saja (satu kelas harness, fungsional) pada Modal Unit Detail dengan data Pre-setup; bagian Client A (langkah 1 sampai 37) memakai satu pembukaan Detail Pieces untuk empat TC, dan bagian Principal berdiri sendiri sesudah ganti akun. Spec tidak membuat data, sehingga pemisahan hanya menambah login dan pembukaan layar berulang.
- Temuan untuk QA:
  - TC-GS-UOM-256 langkah 4 membutuhkan sedikitnya satu baris pada Changelog instance Principal tetapi precondition TC tidak menyebut entri Changelog Principal; spec menuliskannya sebagai kebutuhan "disediakan tim FE" di Prerequisites.
  - TC-GS-UOM-257 Expected a menyebut "kontrol yang ada hanya ..." untuk kedua accordion; urutan dan penempatan kontrol tidak disebut TC dan tidak diasersi.
  - TC-GS-UOM-191 tidak menyebut cara mengamati "tidak dirender sama sekali" selain absennya accordion Device Name List; spec mengasersi absensi dengan accordion Item Type List sebagai anchor positif.
