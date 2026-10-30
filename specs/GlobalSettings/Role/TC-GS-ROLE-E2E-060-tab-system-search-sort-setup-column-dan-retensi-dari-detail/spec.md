---
id: TC-GS-ROLE-E2E-060-tab-system-search-sort-setup-column-dan-retensi-dari-detail
title: "Tab System: Search, Sort Tidak Tersedia, Setup Column, dan Retensi Search Setelah Kembali dari Detail"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-181
  - TC-GS-ROLE-182
  - TC-GS-ROLE-183
  - TC-GS-ROLE-184
  - TC-GS-ROLE-195
coverage:
  web: automated
---

# Tab System: Search, Sort Tidak Tersedia, Setup Column, dan Retensi Search Setelah Kembali dari Detail

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Role; seluruh data hanya dibaca.
- Akun: Total Control, Ahmad Fauzi (Pre-setup #1), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Role & Permission > System dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data (katalog tetap, hanya dibaca): Tab System memuat enam Role Name berurutan fixed `Import data`, `Manage files`, `Manage hardware`, `Manage master reference`, `Manage TAG`, `Manage user and role`; kolom `Role Name` dan `Users`. Tab System tidak memiliki Pagination dan tidak memiliki Filter. Role Name yang memuat kata `manage` berjumlah lima (semua kecuali `Import data`); tidak ada Role Name yang memuat `6`.
- Data uji: keyword Search `master`, `6`, dan `manage`; kolom `Role Name` dan `Users`.
- Preferensi kolom (visibilitas, urutan, pin) tersimpan per user di browser per tabel dan menjadi permanen setelah `[Save]` (prd-conventions.md §9.3); "muat ulang halaman" (F5) dilakukan pada konteks browser yang sama supaya penyimpanan browser tetap ada.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom tabel Tab System dikembalikan ke default (`Role Name` dan `Users` tampil berurutan, tanpa pin) lewat `[Reset to Default]` atau penghapusan preferensi kolom tabel itu di browser. Konfigurasi dikembalikan juga oleh langkah 50 dan 51 di spec.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission, Tab System (Search dikosongkan).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: mengarahkan kursor ke header kolom dan ke checkbox disabled untuk membaca ikon dan tooltip; drag and drop kolom pada popup Setup Column; klik tombol Back browser; membaca dan menghapus preferensi kolom di penyimpanan browser.

## Test Steps

### TC-GS-ROLE-181: Search Tab System

1. Klik icon Search
2. Verifikasi placeholder `Search role...`
3. Ketik Search `master`, tekan Enter
4. Verifikasi baris `Manage master reference` tampil
5. Verifikasi baris `Import data`, `Manage files`, `Manage hardware`, `Manage TAG`, `Manage user and role` tidak tampil
6. Ganti isi kotak search dengan `6`, tekan Enter
7. Verifikasi `No results found` tampil
8. Klik `(←)` pada kotak Search

### TC-GS-ROLE-182: Kolom Tab System tidak dapat di-sort

9. Catat urutan baris tabel Tab System
10. Arahkan kursor ke header `Role Name`
11. Verifikasi header `Role Name` tampil
12. Verifikasi tidak ada ikon sort pada header `Role Name`
13. Klik header `Role Name`
14. Verifikasi urutan baris sama dengan urutan yang dicatat
15. Arahkan kursor ke header `Users`
16. Verifikasi header `Users` tampil
17. Verifikasi tidak ada ikon sort pada header `Users`
18. Klik header `Users`
19. Verifikasi urutan baris sama dengan urutan yang dicatat

### TC-GS-ROLE-183: Screening overlay dan popup Setup Column Tab System

20. Klik header kolom Column Visibility (⋯)
21. Verifikasi overlay memuat item `Setup Column...`
22. Verifikasi kolom `Role Name` dan `Users` tercentang dan enabled
23. Klik item `Setup Column...`
24. Verifikasi Header: Title `Setup Column`
25. Verifikasi Header: icon close `[✕]`
26. Verifikasi Body: daftar kolom `Role Name` dan `Users`
27. Verifikasi Footer: tombol `[Reset to Default]` dan `[Save]`

### TC-GS-ROLE-184: Setup Column Tab System: hide, drag, pin, reset, discard, guard

28. Hilangkan centang `Users`
29. Klik `[Save]`
30. Verifikasi kolom `Users` tidak tampil di tabel
31. Tekan F5
32. Verifikasi kolom `Users` tetap tidak tampil di tabel
33. Klik header kolom Column Visibility (⋯)
34. Klik item `Setup Column...`
35. Centang `Users` agar urutan kolom dapat diamati di tabel
36. Drag kolom `Users` ke posisi sebelum `Role Name`
37. Klik `[Save]`
38. Verifikasi tabel menampilkan urutan kolom `Users`, `Role Name`
39. Klik header kolom Column Visibility (⋯)
40. Klik item `Setup Column...`
41. Klik icon pin pada kolom `Role Name`
42. Klik `[Save]`
43. Verifikasi kolom `Role Name` ter-pin
44. Klik header kolom Column Visibility (⋯)
45. Klik item `Setup Column...`
46. Hilangkan centang `Users`
47. Arahkan kursor ke checkbox `Role Name`
48. Verifikasi checkbox `Role Name` disabled
49. Verifikasi tooltip `At least one column must remain visible.`
50. Klik `[Reset to Default]`
51. Klik `[Save]`
52. Verifikasi tabel menampilkan kolom `Role Name` dan `Users` berurutan `Role Name`, `Users`
53. Klik header kolom Column Visibility (⋯)
54. Klik item `Setup Column...`
55. Hilangkan centang `Users`
56. Klik `[✕]`
57. Verifikasi kolom `Users` tetap tampil di tabel

### TC-GS-ROLE-195: Back dari Detail mempertahankan Search Tab System

58. Ketik Search `manage`, tekan Enter
59. Klik Role Name `Manage TAG`
60. Klik tombol Back browser
61. Verifikasi kotak Search berisi keyword `manage`
62. Verifikasi baris `Manage files`, `Manage hardware`, `Manage master reference`, `Manage TAG`, `Manage user and role` tampil
63. Verifikasi baris `Import data` tidak tampil

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE (katalog role dimuat dari backend nyata; preferensi kolom disimpan di browser).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (181, 182, 183, 184, 195) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah "Klik `(←)` pada kotak Search" di akhir TC-GS-ROLE-181 (menutup Search dan mereset tabel), langkah "Catat urutan baris tabel Tab System" di TC-GS-ROLE-182, langkah "Centang `Users` agar urutan kolom dapat diamati di tabel" di TC-GS-ROLE-184 (kolom `Users` disembunyikan oleh langkah sebelumnya, sehingga perlu ditampilkan untuk mengamati urutan), dan langkah 50 sampai 51 (mengembalikan konfigurasi default, hook `after` sebagai cadangan). Langkah 1 TC-GS-ROLE-184 ("Popup") memakai popup Setup Column yang masih terbuka dari TC-GS-ROLE-183.
- Asersi absence didahului anchor positif: baris `Manage master reference` tampil sebelum baris lain diasersi tidak tampil; baris hasil `manage` tampil sebelum `Import data` diasersi tidak tampil; `No results found` adalah anchor sah untuk Search tanpa hasil. Header kolom tampil mendahului asersi ikon sort tidak ada.
- Spec melewati sekitar 35 langkah (63 langkah) karena lima TC memakai tabel Tab System yang sama dan satu kelas harness (fungsional, tanpa data tulis). Tiap blok berdiri sendiri: blok 181 dan 195 memulai Search dari kotak yang dikosongkan, blok 182 hanya membaca urutan, dan blok 183 dan 184 membuka popup Setup Column sendiri atau meneruskan popup yang terbuka, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok 184 sendiri memiliki enam sub-bagian berurutan karena TC sumber merangkum hide, drag, pin, reset, discard, dan guard dalam satu TC.
- Pembagian TC lintas spec: TC-GS-ROLE-185 (Download Tab System) di spec 061; TC-GS-ROLE-186 sampai 190 (Search dan Filter Detail) di spec 062 dan 063; retensi Search untuk Tab Total Control dan Tab Read Only (TC-GS-ROLE-160 dan 161) di spec 055.
- Temuan untuk QA:
  - TC-GS-ROLE-183 menulis item "[Setup Column]" sedangkan PRD dan TC Setup Column lain menulis "Setup Column..."; spec memakai `Setup Column...`.
  - TC-GS-ROLE-184 langkah 4 ("Uncheck Role Name saat Users hidden"): TC tidak menyebut apakah `Users` tersembunyi dalam popup yang sama atau tersimpan; spec menyembunyikan `Users` di popup (belum disimpan) lalu mengarahkan kursor ke checkbox `Role Name`.
  - TC-GS-ROLE-184 Expected b dan c: urutan dan pin tidak dapat diamati bila `Users` tersembunyi; spec menampilkan `Users` kembali sebelum langkah drag (langkah penghubung). Cara mengamati pin (mis. ikon pin aktif pada popup atau kolom diam saat scroll) tidak disebut TC; spec mengasersi kolom `Role Name` ter-pin tanpa menyebut cara pengamatan.
  - TC-GS-ROLE-184 Expected e: TC tidak menyebut urutan sesudah Reset selain "Role Name | Users"; spec mengasersi urutan itu.
  - TC-GS-ROLE-195: Expected "hasilnya" tidak menyebut baris; spec mengasersi lima role yang memuat kata `manage` tampil dan `Import data` tidak tampil.
