---
id: TC-GS-UOM-E2E-013-role-matrix-visibilitas-elemen-per-role
title: "Role Matrix: Visibilitas Elemen Tab Measurement per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-24
  - TC-GS-UOM-25
  - TC-GS-UOM-26
  - TC-GS-UOM-27
  - TC-GS-UOM-28
  - TC-GS-UOM-29
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Tab Measurement per Role

## Prerequisites

- Mode: FE+BE.
- Hook suite (login akun default, `beforeEach` membuka Global Settings > Master Reference > Measurement, flag Guided Tooltip `guided_tooltip_seen_gs-measurement`, Population dan Pre-setup): lihat `suite.md`; flag Guided Tooltip disetel true untuk keenam akun di bawah oleh hook suite.
- Kerangka langkah per role serupa (login, buka Tab Measurement, buka row action baris Kilogram, arahkan ke kolom Checkbox baris Meter), tetapi langkah dan hasil yang diharapkan berbeda per role (elemen yang tampil berbeda), sehingga tiap blok `###` ditulis per role. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables`.

Role yang diuji (Client A, Tabel Data Uji Pre-setup):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-UOM-28 | Total Control | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-UOM-29 | Read Only | Maya Putri | `readOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |
| TC-GS-UOM-24 | System Role: Read saja | Tono Hartono | `readCapability_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_READ_PASSWORD` |
| TC-GS-UOM-25 | System Role: Create dan Read | Rina Marlina | `createOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_CREATE_PASSWORD` |
| TC-GS-UOM-26 | System Role: Update dan Read | Agus Wijaya | `updateOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_UPDATE_PASSWORD` |
| TC-GS-UOM-27 | System Role: Delete dan Read | Dewi Lestari | `deleteOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_DELETE_PASSWORD` |

- Aktor hook `before`: Total Control Client A (akun default suite, `Spectra.env.GS_TC_PASSWORD`); blok pertama (TC-GS-UOM-28) berjalan di sesi itu. Karena spec berakhir di akun System Role: Delete dan Read, hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup Client A (data baca): baris Kilogram (row action dibuka) dan Meter (dicentang lalu dicentang-lepas) berada di halaman pertama tabel (urutan A-Z). Spec tidak membuat, mengubah, atau menghapus data; aksi Edit, Delete, dan Bulk Delete tidak dijalankan, hanya visibilitasnya yang diperiksa.
- State global: tidak ada yang diubah. Capability tiap akun adalah data Pre-setup.

## Test Steps

### TC-GS-UOM-28: Visibilitas elemen Tab Measurement untuk Total Control

1. Verifikasi `[+ Unit]` tampil
2. Klik `⋯` pada baris Kilogram
3. Verifikasi row action `Detail`, `Edit`, dan `Delete` tampil
4. Tutup row action menu dengan Esc
5. Verifikasi Checkbox baris tampil
6. Centang baris Meter
7. Hapus centang baris Meter
8. Verifikasi Search, Filter, Download, Changelog, dan Setup Column tampil serta aktif
9. Verifikasi header kolom sortable tampil serta aktif
10. Verifikasi Pagination tampil serta aktif

### TC-GS-UOM-29: Visibilitas elemen Tab Measurement untuk Read Only

11. Logout, lalu login sebagai Read Only
12. Buka Tab Measurement (Global Settings > Master Reference > Measurement)
13. Verifikasi `[+ Unit]` Hidden
14. Klik `⋯` pada baris Kilogram
15. Verifikasi row action hanya `Detail`
16. Tutup row action menu dengan Esc
17. Verifikasi Checkbox baris Hidden
18. Verifikasi Search, Filter, Download, Changelog, dan Setup Column tampil serta aktif
19. Verifikasi header kolom sortable tampil serta aktif
20. Verifikasi Pagination tampil serta aktif
21. Klik `⋯` pada baris Kilogram, lalu klik `Detail`
22. Verifikasi Modal Unit Detail dapat dibuka
23. Tutup Modal Unit Detail lewat `[✕]`

### TC-GS-UOM-24: Visibilitas elemen Tab Measurement untuk System Role: Read saja

24. Logout, lalu login sebagai System Role: Read saja
25. Buka Tab Measurement (Global Settings > Master Reference > Measurement)
26. Verifikasi Tab `Measurement` tampil
27. Verifikasi `[+ Unit]` Hidden
28. Klik `⋯` pada baris Kilogram
29. Verifikasi row action hanya berisi `Detail`
30. Verifikasi row action `Edit` dan `Delete` Hidden
31. Tutup row action menu dengan Esc
32. Verifikasi Checkbox baris Hidden
33. Verifikasi Bulk Action Bar Hidden
34. Verifikasi Search, Filter, Download, Changelog, dan Setup Column tampil serta aktif
35. Verifikasi header kolom sortable tampil serta aktif
36. Verifikasi Pagination tampil serta aktif

### TC-GS-UOM-25: Visibilitas elemen Tab Measurement untuk System Role: Create dan Read

37. Logout, lalu login sebagai System Role: Create dan Read
38. Buka Tab Measurement (Global Settings > Master Reference > Measurement)
39. Verifikasi Tab `Measurement` tampil
40. Verifikasi baris tabel termuat walau capability yang diberikan hanya Create (C mengimplikasikan R)
41. Verifikasi `[+ Unit]` tampil
42. Klik `⋯` pada baris Kilogram
43. Verifikasi row action hanya `Detail`
44. Tutup row action menu dengan Esc
45. Verifikasi Checkbox baris Hidden
46. Verifikasi Search, Filter, Download, Changelog, dan Setup Column tampil serta aktif
47. Verifikasi header kolom sortable tampil serta aktif
48. Verifikasi Pagination tampil serta aktif

### TC-GS-UOM-26: Visibilitas elemen Tab Measurement untuk System Role: Update dan Read

49. Logout, lalu login sebagai System Role: Update dan Read
50. Buka Tab Measurement (Global Settings > Master Reference > Measurement)
51. Verifikasi Tab `Measurement` tampil
52. Verifikasi baris tabel termuat walau capability yang diberikan hanya Update (U mengimplikasikan R)
53. Verifikasi `[+ Unit]` Hidden
54. Klik `⋯` pada baris Kilogram
55. Verifikasi row action `Detail` dan `Edit` tampil
56. Verifikasi row action `Delete` Hidden
57. Tutup row action menu dengan Esc
58. Verifikasi Checkbox baris Hidden
59. Verifikasi Search, Filter, Download, Changelog, dan Setup Column tampil serta aktif
60. Verifikasi header kolom sortable tampil serta aktif
61. Verifikasi Pagination tampil serta aktif

### TC-GS-UOM-27: Visibilitas elemen Tab Measurement untuk System Role: Delete dan Read

62. Logout, lalu login sebagai System Role: Delete dan Read
63. Buka Tab Measurement (Global Settings > Master Reference > Measurement)
64. Verifikasi Tab `Measurement` tampil
65. Verifikasi baris tabel termuat walau capability yang diberikan hanya Delete (D mengimplikasikan R)
66. Verifikasi `[+ Unit]` Hidden
67. Klik `⋯` pada baris Kilogram
68. Verifikasi row action `Detail` dan `Delete` tampil
69. Verifikasi row action `Edit` Hidden
70. Tutup row action menu dengan Esc
71. Verifikasi Checkbox baris tampil
72. Centang baris Meter
73. Verifikasi Bulk Action Bar tampil saat satu baris atau lebih dicentang
74. Klik `Bulk Action` pada Bulk Action Bar
75. Verifikasi overlay `Bulk Action` memuat aksi `Delete`
76. Tutup overlay `Bulk Action` dengan Esc
77. Hapus centang baris Meter
78. Verifikasi Search, Filter, Download, Changelog, dan Setup Column tampil serta aktif
79. Verifikasi header kolom sortable tampil serta aktif
80. Verifikasi Pagination tampil serta aktif

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi): matriks visibilitas elemen per role yang memuat polaritas tampil dan Hidden; `caseType` Positive mengikuti alur dominan. Ditulis per blok role dan bukan perulangan karena langkah tiap role berbeda (elemen yang tampil berbeda) dan ganti akun menuntut Step eksplisit; akun pertama (Total Control) login di hook `before` (bagian 3a konvensi, `[KEPUTUSAN 2026-10-30]`).
- Urutan blok menyimpang dari urutan TC sumber (24 sampai 29): TC-GS-UOM-28 (Total Control) dijalankan pertama karena sesi hook `before` sudah Total Control (S-07), lalu 29, 24, 25, 26, 27.
- Spec memuat sekitar 80 langkah (melewati batas 35 langkah) karena enam role dijalankan berurutan dalam satu kelas harness (Role Matrix), bukan beberapa kelas; blok tiap role berdiri sendiri (ada login sendiri), sehingga kegagalan satu blok tidak menghilangkan makna blok lain (bagian 3 butir "ganti akun").
- Langkah penghubung (aksi tanpa `Verifikasi`): menutup row action menu dengan Esc (langkah 4, 16, 31, 44, 57, 70), menghapus centang baris Meter (langkah 7 dan 77), menutup Modal Unit Detail (langkah 23), menutup overlay `Bulk Action` (langkah 76), serta logout lalu login ke role berikutnya dan membuka Tab Measurement (langkah 11, 12, 24, 25, 37, 38, 49, 50, 62, 63).
- Langkah 21 sampai 23 (membuka Modal Unit Detail lewat `Detail` pada baris Kilogram) tidak ada di Langkah Uji TC-GS-UOM-29 tetapi diperlukan agar Expected Result e ("Modal Unit Detail dapat dibuka") dapat diasersi. Langkah 73 sampai 75 menjalankan klausa Expected Result d TC-GS-UOM-27 (Bulk Action Bar dan overlay `Bulk Action`).
- Pengecekan Hidden (langkah 13, 17, 27, 32, 33, 45, 53, 58, 66) memakai Table Tools (Search, Filter, dan seterusnya) pada layar yang sama sebagai anchor permukaan termuat (butir 2 bagian 8b).
- Kombinasi role yang tidak punya TC sumber tidak ditambahkan. Aktor Tanpa Capability diuji di spec `TC-GS-UOM-E2E-014-role-matrix-negatif-tanpa-capability`.
- Temuan untuk QA:
  - Langkah Uji TC-GS-UOM-24 sampai 29 memakai kondisional ("Centang baris Meter bila checkbox tersedia", "Klik `Bulk Action` bila Bulk Action Bar tampil"). Spec menuliskannya deterministik per role mengikuti Expected Result tiap TC: checkbox hanya ada di role Total Control dan Delete dan Read, sehingga centang baris Meter hanya ditulis di blok kedua role itu (langkah 6 dan 72).
  - TC-GS-UOM-28 dan 29 tidak punya klausa "Tab Measurement tampil" di Expected Result; spec tidak menambahkannya untuk dua role itu.
