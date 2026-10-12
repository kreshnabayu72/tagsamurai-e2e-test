---
id: TC-GS-BRAND-E2E-009-role-matrix-visibilitas-elemen-per-role
title: "Role Matrix: Visibilitas Elemen Tab Brand per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-27
  - TC-GS-BRAND-28
  - TC-GS-BRAND-29
  - TC-GS-BRAND-30
  - TC-GS-BRAND-31
  - TC-GS-BRAND-32
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Tab Brand per Role

## Prerequisites

- Mode: FE+BE.
- Langkah identik untuk setiap role (login, buka Tab Brand, buka row action baris Orion Tech, arahkan ke kolom Checkbox); yang berbeda hanya akun login dan hasil yang diharapkan. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables`.

Role yang diuji (Client A, Tabel Data Uji Pre-setup):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-BRAND-27 | Total Control | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-BRAND-28 | Read Only | Maya Putri | `readOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |
| TC-GS-BRAND-29 | System Role: Read saja | Tono Hartono | `readCapability_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_READ_PASSWORD` |
| TC-GS-BRAND-30 | System Role: Create dan Read | Rina Marlina | `createOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_CREATE_PASSWORD` |
| TC-GS-BRAND-31 | System Role: Update dan Read | Agus Wijaya | `updateOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_UPDATE_PASSWORD` |
| TC-GS-BRAND-32 | System Role: Delete dan Read | Dewi Lestari | `deleteOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_DELETE_PASSWORD` |

- Data Pre-setup Client A (12 brand, data environment tetap), termasuk baris Orion Tech (Bebas relasi). Spec tidak membuat atau menghapus data; aksi Edit, Delete, dan Create tidak dijalankan, hanya visibilitasnya yang diperiksa.
- Guided Tooltip: hook `before` mencatat nilai awal flag `guided_tooltip_seen_gs-brand` untuk keenam akun lalu menyetelnya ke true lewat API supaya walkthrough otomatis tidak menutupi layar; hook `after` memulihkan nilai awal tiap akun.
- Login per role adalah bagian perulangan spec Role Matrix (bagian 3a konvensi): login role pertama dan ganti akun ke role berikutnya ditulis sebagai langkah (logout lalu login di awal tiap TC). Karena spec berakhir di akun System Role: Delete dan Read, hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`).
- State global yang diubah: hanya flag Guided Tooltip (dipulihkan seperti di atas). Capability role tidak diubah di spec ini; capability tiap akun adalah data Pre-setup.

## Test Steps

### TC-GS-BRAND-27: Visibilitas elemen Tab Brand untuk Total Control

1. Login sebagai Total Control
2. Buka Tab Brand (Global Settings > Master Reference > Brand)
3. Verifikasi Tab `Brand` tampil dan baris tabel termuat
4. Verifikasi `[+ Brand]` tampil
5. Klik `⋯` pada baris Orion Tech
6. Verifikasi row action `Detail`, `Edit`, dan `Delete` tampil
7. Tutup row action menu dengan Esc
8. Arahkan ke kolom Checkbox
9. Verifikasi Checkbox baris tampil
10. Centang satu baris
11. Verifikasi Bulk Action Bar tampil saat satu baris atau lebih dicentang
12. Hapus centang baris
13. Verifikasi Search, Filter, Download, Changelog, header Column Visibility, sort header, dan Pagination tampil dan aktif

### TC-GS-BRAND-28: Visibilitas elemen Tab Brand untuk Read Only

14. Logout, lalu login sebagai Read Only
15. Buka Tab Brand (Global Settings > Master Reference > Brand)
16. Verifikasi Tab `Brand` tampil dan baris tabel termuat
17. Verifikasi `[+ Brand]` Hidden
18. Klik `⋯` pada baris Orion Tech
19. Verifikasi row action `Detail` tampil
20. Verifikasi row action `Edit` dan `Delete` Hidden
21. Tutup row action menu dengan Esc
22. Arahkan ke kolom Checkbox
23. Verifikasi Checkbox baris Hidden
24. Verifikasi Bulk Action Bar Hidden
25. Verifikasi Search, Filter, Download, Changelog, header Column Visibility, sort header, dan Pagination tampil dan aktif

### TC-GS-BRAND-29: Visibilitas elemen Tab Brand untuk System Role: Read saja

26. Logout, lalu login sebagai System Role: Read saja
27. Buka Tab Brand (Global Settings > Master Reference > Brand)
28. Verifikasi Tab `Brand` tampil dan baris tabel termuat
29. Verifikasi `[+ Brand]` Hidden
30. Klik `⋯` pada baris Orion Tech
31. Verifikasi row action hanya `Detail`
32. Tutup row action menu dengan Esc
33. Arahkan ke kolom Checkbox
34. Verifikasi Checkbox baris Hidden
35. Verifikasi Search, Filter, Download, Changelog, header Column Visibility, sort header, dan Pagination tampil dan aktif

### TC-GS-BRAND-30: Visibilitas elemen Tab Brand untuk System Role: Create dan Read

36. Logout, lalu login sebagai System Role: Create dan Read
37. Buka Tab Brand (Global Settings > Master Reference > Brand)
38. Verifikasi Tab `Brand` tampil dan baris tabel termuat (C mensyaratkan R)
39. Verifikasi `[+ Brand]` tampil
40. Klik `⋯` pada baris Orion Tech
41. Verifikasi row action hanya `Detail`
42. Tutup row action menu dengan Esc
43. Arahkan ke kolom Checkbox
44. Verifikasi Checkbox baris Hidden
45. Verifikasi Search, Filter, Download, Changelog, header Column Visibility, sort header, dan Pagination tampil dan aktif

### TC-GS-BRAND-31: Visibilitas elemen Tab Brand untuk System Role: Update dan Read

46. Logout, lalu login sebagai System Role: Update dan Read
47. Buka Tab Brand (Global Settings > Master Reference > Brand)
48. Verifikasi Tab `Brand` tampil dan baris tabel termuat (U mensyaratkan R)
49. Verifikasi `[+ Brand]` Hidden
50. Klik `⋯` pada baris Orion Tech
51. Verifikasi row action `Detail` dan `Edit` tampil
52. Verifikasi row action `Delete` Hidden
53. Tutup row action menu dengan Esc
54. Arahkan ke kolom Checkbox
55. Verifikasi Checkbox baris Hidden
56. Verifikasi Search, Filter, Download, Changelog, header Column Visibility, sort header, dan Pagination tampil dan aktif

### TC-GS-BRAND-32: Visibilitas elemen Tab Brand untuk System Role: Delete dan Read

57. Logout, lalu login sebagai System Role: Delete dan Read
58. Buka Tab Brand (Global Settings > Master Reference > Brand)
59. Verifikasi Tab `Brand` tampil dan baris tabel termuat (D mensyaratkan R)
60. Verifikasi `[+ Brand]` Hidden
61. Klik `⋯` pada baris Orion Tech
62. Verifikasi row action `Detail` dan `Delete` tampil
63. Verifikasi row action `Edit` Hidden
64. Tutup row action menu dengan Esc
65. Arahkan ke kolom Checkbox
66. Verifikasi Checkbox baris tampil
67. Centang satu baris
68. Verifikasi Bulk Action Bar `Delete` tampil saat satu baris atau lebih dicentang
69. Hapus centang baris
70. Verifikasi Search, Filter, Download, Changelog, header Column Visibility, sort header, dan Pagination tampil dan aktif

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi) berupa matriks visibilitas elemen per role yang memuat polaritas tampil dan Hidden/Disabled dengan alur identik per role; `caseType` Positive mengikuti alur dominan (bagian 8); jumlah langkah (70) melewati batas smell sekitar 35 karena enam role dijalankan berurutan, bukan karena beberapa kelas harness. Bila tim FE ingin memangkas, setiap blok TC bisa dijalankan sebagai perulangan atas tabel "Role yang diuji".
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): menutup row action menu dengan Esc (langkah 7, 21, 32, 42, 53, 64), menghapus centang baris (langkah 12 dan 69), serta logout lalu login ke role berikutnya (langkah 15, 26, 36, 46, 57) sebagai bagian perulangan role.
- Pengecekan Bulk Action Bar (langkah 10 sampai 12 dan 67 sampai 69) menambah satu centang baris karena Expected Result TC menyatakan "Bulk Action Bar tampil saat satu baris atau lebih dicentang"; tidak ada aksi Delete yang dijalankan.
- Kombinasi role yang tidak punya TC sumber tidak ditambahkan. Aktor tanpa capability diuji di spec `TC-GS-BRAND-E2E-010-role-matrix-negatif-tanpa-capability`.
