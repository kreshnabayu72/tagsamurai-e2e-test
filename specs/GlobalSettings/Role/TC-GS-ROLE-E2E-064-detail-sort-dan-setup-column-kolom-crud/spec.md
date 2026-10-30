---
id: TC-GS-ROLE-E2E-064-detail-sort-dan-setup-column-kolom-crud
title: "Detail Role: Sort per Kolom Data, Kolom CRUD Tidak Sortable, dan Setup Column Kolom CRUD"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-191
  - TC-GS-ROLE-192
  - TC-GS-ROLE-193
coverage:
  web: automated
---

# Detail Role: Sort per Kolom Data, Kolom CRUD Tidak Sortable, dan Setup Column Kolom CRUD

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Ahmad Fauzi (`Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission > System > Detail "Manage TAG".
- Data Pre-setup (tetap di environment, hanya dibaca): Detail "Manage TAG" berisi sedikitnya empat user dengan Position dan Division berbeda, yaitu Ahmad Fauzi (TAG `TG-00451`), Budi Santoso (Default User; Position dan Division `—`), Doni Pratama, Hendra Wijaya, Siti Nurhaliza, Rina Putri, Bayu Nugraha dan Intan Permata (Temporary User, Temporary Until terisi dengan tanggal berbeda; Pre-setup #19).
- Seeding milik spec (dibuat lewat API oleh akun Ahmad Fauzi di hook `before`; kemampuan POST/DELETE `/v2/iam/products/{product}/roles/access-level` dan DELETE `/v2/iam/products/{product}/roles/capabilities/users` dari `openapi.yaml`): Rudi Hartono (Pre-setup #11, Pending Activation) di-assign Total Control agar Detail "Manage TAG" memuat dua nilai Activation Status berbeda (Activated dan Pending Activation). Hook `after` memulihkan Rudi Hartono ke kondisi kandidat Pre-setup #11 (tanpa access level, tanpa baris role) tanpa berasumsi seeding berhasil penuh.
- Data uji lain yang diperlukan asersi sort (dua nilai berbeda atau lebih pada kolom yang diurutkan, S-11) disediakan tim FE: Custom Field aktif `Region` (Dropdown) terisi pada sedikitnya dua user Detail "Manage TAG" dengan label badge berbeda (salah satunya `Bandung`); kolom TAG terisi pada sedikitnya dua user dengan kode TAG berbeda (Ahmad Fauzi `TG-00451` dan satu user lain), sedangkan user lain tanpa TAG.
- Sort per kolom (tiga klik berurutan; "default" = urutan baris awal tabel yang dibaca sebelum klik pertama):

| Kolom | Klik 1 | Klik 2 | Klik 3 | Nilai kosong |
|---|---|---|---|---|
| Name | A-Z | Z-A | default | tidak ada |
| Position | A-Z | Z-A | default | Default User (`—`) di akhir pada klik 1 (ascending), di awal pada klik 2 (descending) |
| Division | A-Z | Z-A | default | Default User (`—`) di akhir pada klik 1 (ascending), di awal pada klik 2 (descending) |
| Activation Status | A-Z | Z-A | default | tidak ada |
| Temporary User | Yes First | No First | default | tidak ada |
| Temporary Until | Oldest First | Newest First | default | baris tanpa Temporary Until di akhir pada klik 1 (ascending), di awal pada klik 2 (descending) |
| TAG | A-Z menurut kode TAG | Z-A | default | baris tanpa TAG di akhir pada klik 1 (ascending), di awal pada klik 2 (descending) |
| Region | A-Z menurut label badge | Z-A | default | tidak ada |

- State yang diubah dan dipulihkan: konfigurasi kolom Detail "Manage TAG" dikembalikan ke default (`[Reset to Default]`) oleh langkah akhir spec dan oleh hook `after` sebagai cadangan; konfigurasi Detail "Manage user and role" tidak diubah.
- Kemampuan teknis: membaca urutan baris dan ikon sort header tabel; hover header kolom; menekan F5.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-191: Sort Detail per kolom data dan kolom CRUD tidak sortable

1. Klik header `Name`
2. Verifikasi urutan baris kolom `Name` A-Z
3. Klik header `Name`
4. Verifikasi urutan baris kolom `Name` Z-A
5. Klik header `Name`
6. Verifikasi urutan baris kembali ke default
7. Untuk setiap kolom `Position` lalu `Division` (langkah 7 sampai 14, parameter di tabel Sort per kolom): klik header kolom
8. Verifikasi urutan baris kolom sesuai kolom "Klik 1" pada tabel
9. Verifikasi baris Default User (`Budi Santoso`, nilai `—`) berada di akhir
10. Klik header kolom
11. Verifikasi urutan baris kolom sesuai kolom "Klik 2" pada tabel
12. Verifikasi baris Default User (`Budi Santoso`, nilai `—`) berada di awal
13. Klik header kolom
14. Verifikasi urutan baris kembali ke default
15. Klik header (⋯)
16. Klik `[Setup Column]`
17. Centang `Activation Status`
18. Centang `Temporary User`
19. Centang `Temporary Until`
20. Centang `TAG`
21. Centang `Region`
22. Klik `[Save]`
23. Untuk setiap kolom `Activation Status` lalu `Temporary User` (langkah 23 sampai 28, parameter di tabel Sort per kolom): klik header kolom
24. Verifikasi urutan baris kolom sesuai kolom "Klik 1" pada tabel
25. Klik header kolom
26. Verifikasi urutan baris kolom sesuai kolom "Klik 2" pada tabel
27. Klik header kolom
28. Verifikasi urutan baris kembali ke default
29. Untuk setiap kolom `Temporary Until` lalu `TAG` (langkah 29 sampai 36, parameter di tabel Sort per kolom): klik header kolom
30. Verifikasi urutan baris kolom sesuai kolom "Klik 1" pada tabel
31. Verifikasi baris tanpa nilai kolom berada di akhir
32. Klik header kolom
33. Verifikasi urutan baris kolom sesuai kolom "Klik 2" pada tabel
34. Verifikasi baris tanpa nilai kolom berada di awal
35. Klik header kolom
36. Verifikasi urutan baris kembali ke default
37. Klik header `Region`
38. Verifikasi urutan baris kolom `Region` A-Z menurut label badge
39. Klik header `Region`
40. Verifikasi urutan baris kolom `Region` Z-A menurut label badge
41. Klik header `Region`
42. Verifikasi urutan baris kembali ke default
43. Arahkan kursor ke header `Read`
44. Verifikasi header `Read` tidak memiliki ikon sort
45. Arahkan kursor ke header `Update`
46. Verifikasi header `Update` tidak memiliki ikon sort
47. Klik breadcrumb `System`
48. Klik Role Name `Manage user and role`
49. Arahkan kursor ke header `Create`
50. Verifikasi header `Create` tidak memiliki ikon sort
51. Arahkan kursor ke header `Delete`
52. Verifikasi header `Delete` tidak memiliki ikon sort
53. Klik breadcrumb `System`
54. Klik Role Name `Manage TAG`

### TC-GS-ROLE-192: Setup Column Detail, kolom CRUD dinamis

55. Klik header (⋯)
56. Verifikasi overlay Column Visibility hanya mendaftar `Name`, `Position`, `Division`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, dan `Region`
57. Verifikasi overlay Column Visibility tidak mencantumkan kolom `Read` dan `Update`
58. Klik `[Setup Column]`
59. Verifikasi popup Setup Column hanya mendaftar `Name`, `Position`, `Division`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, dan `Region`
60. Verifikasi popup Setup Column tidak mencantumkan kolom `Read` dan `Update` sehingga keduanya tidak dapat di-hide, di-drag, maupun di-pin
61. Hapus centang `Position`
62. Hapus centang `Division`
63. Hapus centang `Activation Status`
64. Hapus centang `Temporary User`
65. Hapus centang `Temporary Until`
66. Hapus centang `TAG`
67. Hapus centang `Region`
68. Klik `[Save]`
69. Verifikasi kolom `Read` tampil di tabel
70. Verifikasi kolom `Update` tampil di tabel
71. Klik header (⋯)
72. Klik `[Setup Column]`
73. Klik `[Reset to Default]`
74. Klik `[Save]`

### TC-GS-ROLE-193: Setup Column Detail, hide dan show kolom Name, Position, Division, dan kolom kurasi

75. Klik header (⋯)
76. Klik `[Setup Column]`
77. Hapus centang `Position`
78. Hapus centang `Division`
79. Centang `Activation Status`
80. Centang `Temporary User`
81. Centang `Temporary Until`
82. Centang `TAG`
83. Klik `[Save]`
84. Verifikasi kolom `Activation Status` tampil di tabel
85. Verifikasi kolom `Temporary User` tampil di tabel
86. Verifikasi kolom `Temporary Until` tampil di tabel
87. Verifikasi kolom `TAG` tampil di tabel
88. Verifikasi kolom `Position` dan `Division` tersembunyi
89. Tekan F5
90. Verifikasi kolom `Activation Status` tetap tampil
91. Verifikasi kolom `Temporary User` tetap tampil
92. Verifikasi kolom `Temporary Until` tetap tampil
93. Verifikasi kolom `TAG` tetap tampil
94. Verifikasi kolom `Position` dan `Division` tetap tersembunyi
95. Klik header (⋯)
96. Klik `[Setup Column]`
97. Klik `[Reset to Default]`
98. Klik `[Save]`

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE (tabel dimuat dari backend nyata; preferensi kolom disimpan di browser per tabel).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (191, 192, 193) dipertahankan.
- Langkah yang diulang per kolom memakai tabel Sort per kolom di Prerequisites: langkah 7 sampai 14 untuk `Position` lalu `Division`, langkah 23 sampai 28 untuk `Activation Status` lalu `Temporary User`, langkah 29 sampai 36 untuk `Temporary Until` lalu `TAG`. `Name` (langkah 1 sampai 6) dan `Region` (langkah 37 sampai 42) ditulis eksplisit karena tidak punya nilai kosong dan berada di sisi lain Setup Column.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 47, 48, 53, dan 54 (pindah ke Detail "Manage user and role" untuk header Create dan Delete, lalu kembali ke Detail "Manage TAG"); langkah 71 sampai 74 dan 95 sampai 98 (`[Reset to Default]` lalu `[Save]` untuk mengembalikan konfigurasi kolom ke default sebelum blok berikutnya dan di akhir spec).
- Langkah 15 sampai 22 memenuhi Langkah Uji 4 TC-GS-ROLE-191 (menampilkan Activation Status, Temporary User, Temporary Until, TAG, dan Region lewat Setup Column lalu `[Save]`).
- Blok TC-GS-ROLE-193 dimulai dari konfigurasi default (hasil langkah 71 sampai 74) agar `Position` dan `Division` tampil dan keempat kolom kurasi tersembunyi sebelum diubah; Region tidak diubah pada blok ini karena TC-GS-ROLE-193 tidak menyebutnya.
- Verifikasi daftar kolom yang sama-sama tidak ada (langkah 57, 60, 88, 94) digabung per daftar utuh dan didahului anchor positif pada permukaan yang sama (langkah 56, 59, 84 sampai 87, 90 sampai 93; bagian 8b butir 2). Daftar kolom yang tampil dipecah satu `Verifikasi` per kolom (S-01).
- Spec melewati sekitar 35 langkah (98 langkah nominal, sekitar 120 dengan ekspansi tiga blok ulang) karena TC-GS-ROLE-191 mengurutkan delapan kolom dengan tiga klik tiap kolom dan satu `Verifikasi` per klausa (S-01). Semuanya satu kelas harness (fungsional Detail "Manage TAG"), satu akun, data baca saja; kegagalan sort satu kolom tidak membuat blok Setup Column kehilangan makna, dan blok TC-GS-ROLE-192 dan 193 tidak mengandalkan hasil blok sebelumnya karena konfigurasi kolom dikembalikan ke default (langkah 71 sampai 74).
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-ROLE-191 tidak menyebut cara menentukan urutan "default"; spec membaca urutan baris awal tabel sebelum klik pertama (Prerequisites).
  - TC-GS-ROLE-191 Expected a sampai h menyebut arah urutan tanpa menyebut nilai konkret baris; spec mengasersi arah urutan pada kolom yang diklik dan data uji dengan dua nilai berbeda atau lebih disediakan tim FE (Region, TAG, Temporary Until).
  - TC-GS-ROLE-191 Langkah Uji 6 mengunjungi Detail "Manage user and role" tanpa menyebut cara kembali; spec memakai breadcrumb `System` dan Role Name sebagai langkah penghubung, dan mengasumsikan kolom Create dan Delete Detail tersebut berperilaku sama dengan kolom Read dan Update.
  - TC-GS-ROLE-192 Expected c tidak menyebut apakah kolom Read dan Update diamati sebelum atau sesudah `[Save]`; spec mengasersi sesudah `[Save]`.
  - TC-GS-ROLE-192 dan 193 tidak menyebut kondisi awal konfigurasi kolom; spec mengaturnya lewat `[Reset to Default]` dan `[Save]` (langkah 71 sampai 74).
