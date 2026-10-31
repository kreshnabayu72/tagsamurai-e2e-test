---
id: TC-GS-UOM-E2E-055-detail-device-name-list-principal-dan-distributor
title: "Unit Detail: Device Name List pada Principal dan Distributor (Screening, Search, Sort, Empty State)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-202
  - TC-GS-UOM-203
  - TC-GS-UOM-204
  - TC-GS-UOM-205
  - TC-GS-UOM-255
  - TC-GS-UOM-348
  - TC-GS-UOM-366
coverage:
  web: automated
tags: [principal]
---

# Unit Detail: Device Name List pada Principal dan Distributor (Screening, Search, Sort, Empty State)

## Prerequisites

- Mode: FE+BE.
- Akun yang dipakai (dengan langkah ganti akun eksplisit):
  - Total Control (Principal), Hendra Wijaya, `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 8), kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`. Akun aktor pertama: login di hook `before` spec ini. Dipakai langkah 1 sampai 44.
  - Total Control (Distributor), Bayu Pratama, `totalControlDistributor_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 9), kredensial `Spectra.env.GS_DISTRIBUTOR_TC_PASSWORD`. Login lewat UI di langkah 46. Dipakai langkah 46 sampai 54.
  - Total Control Client A, Sari Dewi, `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`: akun default suite, hanya dipakai hook `after` untuk memulihkan sesi.
- Environment variable: `GS_PRINCIPAL_TC_PASSWORD`, `GS_DISTRIBUTOR_TC_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel true oleh hook suite untuk akun aktor suite (lihat bagian "Hook suite" di `suite.md`); untuk akun Principal dan Distributor, mekanisme penyetelan flag disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`). Hook `after` logout dari akun Distributor dan login kembali sebagai akun default suite.
- Data Pre-setup (tetap di environment, hanya dibaca, tanpa suffix `{runId}`; spec tidak membuat atau mengubah data sehingga tidak ada seeding dan cleanup data):
  - Principal: `Watt` (Symbol `W`; Device Name `BLE Gateway` dan `Handheld Reader`; tanpa Asset Name maupun Item Name), `Volt` (Symbol `V`; bebas relasi), `Ampere` (Symbol `A`; Asset Name FAMS `Power Meter`, Item Name Supply `Battery Pack`, Device Name `Fixed Reader`). Referensi Supply (SAMS) disiapkan lewat fixture backend (NC-09), disediakan tim FE.
  - Distributor: `Hertz` (Symbol `Hz`; bebas relasi).
- Baris unit dicari lewat Search nama unit supaya tidak bergantung pada halaman Pagination.
- Kemampuan teknis: login/logout dalam satu spec (Principal ke Distributor); hook `after` logout dan login ulang sebagai akun default suite.
- Precondition TC-GS-UOM-202, 203, 204, 205, 255, 348: login sebagai Total Control (Principal). TC-GS-UOM-366: login sebagai Total Control (Distributor).

## Test Steps

### TC-GS-UOM-202: Accordion Device Name List pada instance Principal

1. Ketik Search `Watt`, tekan Enter
2. Klik `⋯` pada baris Watt
3. Klik Detail
4. Verifikasi accordion `Device Name List` expanded
5. Verifikasi accordion Device Name List memuat Search dengan placeholder `Search device name...`
6. Verifikasi accordion Device Name List tanpa Filter
7. Verifikasi accordion Device Name List tanpa Download
8. Verifikasi baris A-Z: `BLE Gateway`, `Handheld Reader`
9. Verifikasi tabel Device Name List memiliki satu kolom `Device Name`

### TC-GS-UOM-348: Item Type List tidak memuat Device Name; unit yang hanya dipakai Device Name tampil tanpa Item Type

10. Verifikasi Detail Watt: accordion Item Type List menampilkan Title `No item types linked`
11. Verifikasi Detail Watt: accordion Item Type List menampilkan Description `No products or items currently reference this measurement unit.`
12. Verifikasi Detail Watt: Device Name List memuat `BLE Gateway` dan `Handheld Reader`

### TC-GS-UOM-203: Search Device Name List

13. Ketik Search `hand` pada Device Name List, tekan Enter
14. Verifikasi tabel Device Name List memuat `Handheld Reader`
15. Verifikasi tabel Device Name List tidak memuat `BLE Gateway`

### TC-GS-UOM-205: Empty state Device Name List saat Search tidak cocok

16. Ganti isi kotak search dengan `zzqx`, tekan Enter
17. Verifikasi Title `No results found`

### TC-GS-UOM-255: Sort 3-state kolom Device Name pada tabel Device Name List

18. Klik `(←)` pada kotak Search Device Name List
19. Verifikasi tabel memuat `BLE Gateway` dan `Handheld Reader`
20. Klik header Device Name
21. Verifikasi klik 1 ascending: `BLE Gateway`, `Handheld Reader`
22. Klik header Device Name
23. Verifikasi klik 2 descending: `Handheld Reader`, `BLE Gateway`
24. Klik header Device Name
25. Verifikasi klik 3 netral: kolom Device Name tanpa panah sort aktif dan urutan kembali ke default Device Name A-Z (`BLE Gateway`, `Handheld Reader`)
26. Klik `[✕]`

### TC-GS-UOM-348 (lanjutan): Detail Ampere dan opsi Filter Product

27. Ganti isi kotak search tabel utama dengan `Ampere`, tekan Enter
28. Klik `⋯` pada baris Ampere, lalu klik Detail
29. Verifikasi Detail Ampere: Item Type List memuat `Battery Pack` (Supply)
30. Verifikasi Detail Ampere: Item Type List memuat `Power Meter` (Fixed Asset)
31. Verifikasi Detail Ampere: Item Type List tidak memuat `Fixed Reader`
32. Verifikasi Detail Ampere: Device Name List memuat `Fixed Reader`
33. Klik Filter Product pada Item Type List Ampere
34. Buka dropdown Product
35. Verifikasi opsi dropdown Product hanya `Fixed Asset` dan `Supply`
36. Verifikasi opsi dropdown Product tidak memuat `Admin Console`
37. Tutup dropdown Product, lalu klik `[✕]`

### TC-GS-UOM-204: Accordion Device Name List tetap dirender dengan empty state saat kosong

38. Ganti isi kotak search tabel utama dengan `Volt`, tekan Enter
39. Klik `⋯` pada baris Volt, lalu klik Detail
40. Verifikasi accordion Device Name List tampil
41. Verifikasi Search pada Device Name List tetap dirender
42. Verifikasi empty state Title `No device names linked`
43. Verifikasi empty state Description `No devices currently reference this measurement unit.`
44. Klik `[✕]`

### Ganti akun ke Total Control (Distributor)

45. Logout dari akun Total Control (Principal)
46. Login sebagai Total Control (Distributor) `totalControlDistributor_automated_qaTeam1@qwertysystem.net` dengan `Spectra.env.GS_DISTRIBUTOR_TC_PASSWORD`
47. Buka Global Settings > Master Reference > Measurement

### TC-GS-UOM-366: Accordion Device Name List dirender pada instance entitas non-Principal yang memiliki Admin Console

48. Ketik Search `Hertz`, tekan Enter
49. Klik `⋯` pada baris Hertz
50. Klik Detail
51. Verifikasi accordion `Device Name List` dirender dan expanded
52. Verifikasi Search pada Device Name List dengan placeholder `Search device name...`
53. Verifikasi empty state Title `No device names linked`
54. Verifikasi empty state Description `No devices currently reference this measurement unit.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-UOM-202, 348 (butir a pada Detail Watt), 203, 205, 255, 348 (butir b dan c pada Detail Ampere), 204, lalu (Distributor) 366. Alasan: Detail Watt dibuka sekali untuk 202, 348a, 203, 205, 255 (precondition sama, Search dikosongkan sebelum Sort, S-09); TC-GS-UOM-348 terbelah dua blok karena butir b dan c membutuhkan Detail Ampere sesudah modal Watt ditutup. Ganti akun ke Distributor di akhir (butir b prinsip "Beda akun" konvensi 3): bagian Distributor tetap bermakna walau bagian Principal gagal.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 27, 38, 48 (Search nama unit untuk menemukan baris target), langkah 18 (mengosongkan Search), langkah 26, 37, 44 (menutup modal atau dropdown), langkah 45 sampai 47 (ganti akun; hook `after` memulihkan sesi).
- Pembagian TC lintas spec: accordion Item Type List dan screening Detail ada di `TC-GS-UOM-E2E-053-detail-item-type-list-screening-dan-empty`; Setup Column Device Name List di `TC-GS-UOM-E2E-057-detail-setup-column-device-name-list`.
- Langkah 10 sampai 12 memakai Detail Watt yang sama dengan langkah 4 sampai 9 tanpa membuka ulang modal. Langkah 31 (absence `Fixed Reader` di Item Type List) didahului langkah 29 dan 30 sebagai anchor positif pada accordion yang sama; langkah 15 didahului langkah 14; langkah 36 didahului langkah 35.
- Spec ini melewati sekitar 35 langkah (54 langkah). Alasan: semua blok baca-saja (satu kelas harness, fungsional) pada Modal Unit Detail dengan data Pre-setup; bagian Distributor berdiri sendiri sesudah ganti akun, sedangkan bagian Principal memakai satu pembukaan Detail Watt untuk lima butir TC. Spec tidak membuat data, sehingga pemisahan hanya menambah login dan pembukaan layar berulang.
- Temuan untuk QA:
  - Akun Distributor `totalControlDistributor_automated_qaTeam1@qwertysystem.net` (Bayu Pratama) tertulis di Pre-setup TC; password env `GS_DISTRIBUTOR_TC_PASSWORD` mengikuti penamaan suite lain dan perlu didaftarkan tim FE.
  - TC-GS-UOM-202 Expected b menyebut Search "tanpa Filter dan tanpa Download" pada Device Name List; spec mengasersi absensi keduanya dengan Search sebagai anchor positif.
