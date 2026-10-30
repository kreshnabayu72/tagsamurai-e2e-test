---
id: TC-GS-POS-E2E-007-role-matrix-visibilitas-elemen-per-role
title: "Role Matrix: Visibilitas Elemen Tab Position per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-25
  - TC-GS-POS-26
  - TC-GS-POS-27
  - TC-GS-POS-28
  - TC-GS-POS-29
  - TC-GS-POS-30
  - TC-GS-POS-31
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Tab Position per Role

## Prerequisites

- Mode: FE+BE (backend nyata).
- Langkah mengikuti TC masing-masing; akun login dan hasil yang diharapkan berbeda per role. Password tidak ditulis di spec atau fixture.
- Layar awal: pembukaan Global Settings > User per role adalah bagian dari objek uji (visibilitas sub-tab Position pada halaman itu), sehingga ditulis di `## Test Steps`, bukan di hook `beforeEach`.

Role yang diuji (Tabel Data Uji Pre-setup):

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-GS-POS-25 | System Role tanpa capability "Manage user and role" | `noCapabilityGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 8) | `Spectra.env.GS_NOCAP_PASSWORD` |
| TC-GS-POS-26 | Manage user and role: Read-Only | `manageUserRoleRead_automated_{namaCompany}@qwertysystem.net` (Pre-setup 4) | `Spectra.env.GS_READ_PASSWORD` |
| TC-GS-POS-27 | Manage user and role: Create-Only (C+R) | `manageUserRoleCreate_automated_{namaCompany}@qwertysystem.net` (Pre-setup 5) | `Spectra.env.GS_CREATE_PASSWORD` |
| TC-GS-POS-28 | Manage user and role: Update-Only (U+R) | `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net` (Pre-setup 6) | `Spectra.env.GS_UPDATE_PASSWORD` |
| TC-GS-POS-29 | Manage user and role: Delete-Only (D+R) | `manageUserRoleDelete_automated_{namaCompany}@qwertysystem.net` (Pre-setup 7) | `Spectra.env.GS_DELETE_PASSWORD` |
| TC-GS-POS-30 | Total Control | `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1) | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-POS-31 | Read Only (Access Level) | `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 3) | `Spectra.env.GS_RO_PASSWORD` |

- Akun aktor pertama (System Role tanpa capability) login di hook `before`; akun berikutnya login lewat langkah ganti akun eksplisit di awal tiap TC. Karena spec berakhir di akun Read Only, hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Data Pre-setup: Position Pre-setup 10 sampai 16 (tanpa suffix), termasuk baris `IT Manager` (Pre-setup 10, bebas relasi) yang dipakai untuk memeriksa menu `⋯` dan checkbox; tabel berisi 7 record (precondition "≥1 record"). Spec tidak membuat, mengubah, atau menghapus data; aksi Create, Edit, dan Delete tidak dijalankan, hanya visibilitasnya yang diperiksa. Tidak ada Data Dinamis.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true, lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan sesi ke akun default suite (flag Guided Tooltip dipulihkan hook suite `after`).
- State global yang diubah: hanya flag Guided Tooltip (dipulihkan hook suite `after`). Capability tiap akun adalah data Pre-setup dan tidak diubah.

## Test Steps

### TC-GS-POS-25: Visibilitas elemen tab Position untuk System Role tanpa capability Manage user and role

1. Buka Global Settings > User
2. Verifikasi halaman Global Settings > User termuat (breadcrumb `User` tampil)
3. Verifikasi sub-tab Position Hidden pada halaman Global Settings > User
4. Verifikasi tabel, Table Tools, `[+ Position]`, kolom Checkbox, dan row action Position tidak pernah dirender

### TC-GS-POS-26: Visibilitas elemen tab Position untuk Manage user and role Read-Only

5. Ganti akun: logout, lalu login sebagai Manage user and role: Read-Only
6. Buka Global Settings > User
7. Verifikasi sub-tab Position tampil
8. Klik sub-tab Position
9. Verifikasi Table Tools `Search | Filter | Download | Changelog` tampil
10. Verifikasi `[+ Position]` Hidden
11. Verifikasi kolom Checkbox Hidden
12. Verifikasi tidak ada checkbox pada baris tabel
13. Verifikasi Bulk Action Bar tidak muncul
14. Arahkan ke baris `IT Manager`
15. Verifikasi menu `⋯` per baris Hidden (`Edit` dan `Delete` Hidden)
16. Verifikasi header Actions (⋯) (tooltip "Column Visibility") tampil
17. Verifikasi Search tampil dan aktif
18. Verifikasi Filter tampil dan aktif
19. Verifikasi Sort tampil dan aktif
20. Verifikasi Pagination tampil dan aktif
21. Verifikasi Column Visibility tampil dan aktif

### TC-GS-POS-27: Visibilitas elemen tab Position untuk Manage user and role Create-Only

22. Ganti akun: logout, lalu login sebagai Manage user and role: Create-Only
23. Buka Global Settings > User
24. Verifikasi sub-tab Position tampil
25. Klik sub-tab Position
26. Verifikasi Table Tools `Search | Filter | Download | Changelog` tampil
27. Verifikasi `[+ Position]` tampil
28. Arahkan ke baris `IT Manager`
29. Verifikasi menu `⋯` per baris Hidden (`Edit` dan `Delete` Hidden)
30. Verifikasi kolom Checkbox Hidden

### TC-GS-POS-28: Visibilitas elemen tab Position untuk Manage user and role Update-Only

31. Ganti akun: logout, lalu login sebagai Manage user and role: Update-Only
32. Buka Global Settings > User
33. Verifikasi sub-tab Position tampil
34. Klik sub-tab Position
35. Verifikasi Table Tools `Search | Filter | Download | Changelog` tampil
36. Verifikasi `[+ Position]` Hidden
37. Klik `⋯` pada baris `IT Manager`
38. Verifikasi menu `⋯` per baris tampil dan hanya berisi `Edit`
39. Verifikasi `Delete` Hidden
40. Tutup menu `⋯` dengan Esc
41. Verifikasi kolom Checkbox Hidden

### TC-GS-POS-29: Visibilitas elemen tab Position untuk Manage user and role Delete-Only

42. Ganti akun: logout, lalu login sebagai Manage user and role: Delete-Only
43. Buka Global Settings > User
44. Verifikasi sub-tab Position tampil
45. Klik sub-tab Position
46. Verifikasi Table Tools `Search | Filter | Download | Changelog` tampil
47. Verifikasi `[+ Position]` Hidden
48. Klik `⋯` pada baris `IT Manager`
49. Verifikasi menu `⋯` per baris tampil dan hanya berisi `Delete`
50. Verifikasi `Edit` Hidden
51. Tutup menu `⋯` dengan Esc
52. Arahkan ke kolom Checkbox
53. Verifikasi kolom Checkbox tampil
54. Centang baris `IT Manager`
55. Verifikasi Bulk Action Bar dengan aksi Delete tampil
56. Hapus centang baris `IT Manager`

### TC-GS-POS-30: Visibilitas elemen tab Position untuk Total Control

57. Ganti akun: logout, lalu login sebagai Total Control
58. Buka Global Settings > User
59. Verifikasi sub-tab Position tampil
60. Klik sub-tab Position
61. Verifikasi Table Tools `Search | Filter | Download | Changelog` tampil
62. Verifikasi `[+ Position]` tampil
63. Klik `⋯` pada baris `IT Manager`
64. Verifikasi menu `⋯` per baris berisi `Edit` dan `Delete`
65. Tutup menu `⋯` dengan Esc
66. Arahkan ke kolom Checkbox
67. Verifikasi kolom Checkbox tampil
68. Centang baris `IT Manager`
69. Verifikasi Bulk Action Bar dengan aksi Delete tampil
70. Hapus centang baris `IT Manager`

### TC-GS-POS-31: Visibilitas elemen tab Position untuk Read Only (Access Level)

71. Ganti akun: logout, lalu login sebagai Read Only
72. Buka Global Settings > User
73. Verifikasi sub-tab Position tampil
74. Klik sub-tab Position
75. Verifikasi Table Tools `Search | Filter | Download | Changelog` tampil
76. Verifikasi `[+ Position]` Hidden
77. Arahkan ke baris `IT Manager`
78. Verifikasi menu `⋯` per baris Hidden
79. Verifikasi header Actions (⋯) (tooltip "Column Visibility") tampil
80. Verifikasi kolom Checkbox Hidden
81. Verifikasi Search tampil dan aktif
82. Verifikasi Filter tampil dan aktif
83. Verifikasi Sort tampil dan aktif
84. Verifikasi Pagination tampil dan aktif

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi) berupa matriks visibilitas elemen per role yang memuat polaritas tampil dan Hidden dengan alur identik per role; `caseType` Positive mengikuti alur dominan (bagian 8). Jumlah langkah (84) di atas smell sekitar 35 langkah karena tujuh role dijalankan berurutan, bukan karena beberapa kelas harness; satu kelas, tiap blok role berdiri sendiri dengan langkah ganti akun eksplisit, dan kegagalan satu blok tidak menghilangkan makna blok lain. Bila tim FE ingin memangkas, setiap blok TC bisa dijalankan sebagai perulangan atas tabel "Role yang diuji".
- Urutan TC mengikuti TC sumber (25 sampai 31). TC-GS-POS-25 ditaruh pertama karena akun tanpa capability menjadi akun hook `before`.
- Asersi tidak dirender pada TC-GS-POS-25 (langkah 4, Expected b) diamati pada halaman Global Settings > User sesuai langkah 3 TC ("Amati area konten halaman User").
- Expected TC-GS-POS-26 e dan TC-GS-POS-31 e menyebut Search, Filter, Sort, Pagination (dan Column Visibility pada TC-GS-POS-26) "tampil dan aktif"; spec mengasersi tiap elemen tampil dan aktif tanpa menjalankan fungsinya, dan perilaku fungsinya diuji di spec 028 sampai 031. Aksi Delete tidak dijalankan; centang baris pada langkah 54 dan 68 hanya untuk memunculkan Bulk Action Bar.
- Langkah penghubung (tanpa `Verifikasi`): ganti akun (langkah 5, 22, 31, 42, 57, 71), menutup menu `⋯` dengan Esc (langkah 40, 51, 65), menghapus centang baris (langkah 56 dan 70), mengarahkan kursor ke baris atau kolom Checkbox sebagai pemicu hover.
- Langkah 2 adalah asersi tambahan (anchor permukaan) yang tidak ada di Expected TC-GS-POS-25: membuktikan halaman Global Settings > User termuat sebelum langkah 3 dan 4 mengasersi Hidden dan tidak dirender, supaya halaman kosong atau error tidak meloloskannya.
- Kombinasi role yang tidak punya TC sumber tidak ditambahkan. Eksekusi Create, Edit, Delete, dan Bulk Delete oleh aktor capability spesifik ada di spec 009; akses langsung URL oleh aktor tanpa capability ada di spec 008.
- Temuan untuk QA:
  - TC-GS-POS-25 tidak menyebut apakah halaman Global Settings > User dapat dibuka oleh akun tanpa capability "Manage user and role"; spec mengikuti langkah TC.
  - TC-GS-POS-25 tidak menyebut elemen halaman yang tetap tampil bagi akun tanpa capability; langkah 2 memakai breadcrumb `User` (dasar: breadcrumb `User > Position` pada TC-GS-POS-1) sebagai anchor, dan keberadaan elemen itu perlu dikonfirmasi QA.
