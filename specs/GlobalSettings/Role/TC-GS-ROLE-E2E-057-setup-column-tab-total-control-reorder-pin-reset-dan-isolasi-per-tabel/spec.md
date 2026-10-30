---
id: TC-GS-ROLE-E2E-057-setup-column-tab-total-control-reorder-pin-reset-dan-isolasi-per-tabel
title: "Setup Column Tab Total Control: Reorder, Pin, Reset to Default, dan Isolasi Konfigurasi per Tabel"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-166
  - TC-GS-ROLE-167
  - TC-GS-ROLE-168
  - TC-GS-ROLE-169
  - TC-GS-ROLE-170
  - TC-GS-ROLE-173
coverage:
  web: automated
---

# Setup Column Tab Total Control: Reorder, Pin, Reset to Default, dan Isolasi Konfigurasi per Tabel

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Role; tabel dimuat dari backend nyata dan seluruh data Pre-setup hanya dibaca.
- Akun: Total Control, Ahmad Fauzi (Pre-setup #1), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Role & Permission > Total Control dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (tetap di environment, hanya dibaca): Tab Total Control dan Tab Read Only masing-masing berisi sedikitnya 3 user dengan Position dan Division berbeda (precondition TC); Tab System memuat Role Name `Manage TAG` yang membuka Detail "Manage TAG".
- Data uji: kolom K1 (default tampil) `Name`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated`; kolom K2 (default tersembunyi) `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, dan Custom Field aktif `Region` (disediakan tim FE; nama `Region` mengikuti TC-GS-ROLE-188).
- Tabel "Pemindahan kolom K1" untuk TC-GS-ROLE-166 (dijalankan berurutan dari atas ke bawah; urutan akhir `Last Updated`, `Modified By`, `Status`, `Division`, `Position`, `Name`):

  | Kolom | Posisi tujuan (urutan di antara kolom K1) |
  |---|---|
  | Last Updated | 1 |
  | Modified By | 2 |
  | Status | 3 |
  | Division | 4 |
  | Position | 5 |
  | Name | 6 |

- Tabel "Pin kolom K1" untuk TC-GS-ROLE-167: `Name`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated`.
- Tabel "Pemindahan kolom K2" untuk TC-GS-ROLE-168 (dijalankan berurutan dari atas ke bawah; urutan akhir `Region`, `TAG`, `Temporary Until`, `Temporary User`, `Activation Status`):

  | Kolom | Posisi tujuan (urutan di antara kolom K2) |
  |---|---|
  | Region | 1 |
  | TAG | 2 |
  | Temporary Until | 3 |
  | Temporary User | 4 |
  | Activation Status | 5 |

- Tabel "Pin kolom K2" untuk TC-GS-ROLE-169: `Region`, `TAG`, `Temporary Until`, `Temporary User`, `Activation Status`.
- Preferensi kolom (visibilitas, urutan, pin) tersimpan per user di browser per tabel dan menjadi permanen setelah `[Save]` (prd-conventions.md §9.3); "muat ulang halaman" (F5) dilakukan pada konteks browser yang sama supaya penyimpanan browser tetap ada.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom tabel Tab Total Control dikembalikan ke default (K1 tampil berurutan `Name` sampai `Last Updated`, K2 tersembunyi, tanpa pin) lewat `[Reset to Default]` atau penghapusan preferensi kolom tabel itu di browser. Tab Read Only dan Detail "Manage TAG" tidak diubah.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission, Tab Total Control.
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: drag and drop kolom pada popup Setup Column; mengatur ukuran viewport browser sehingga tabel memiliki scroll horizontal (TC tidak menyebutnya, lihat Temuan untuk QA); scroll horizontal tabel dan membaca posisi kolom ter-pin; membaca dan menghapus preferensi kolom di penyimpanan browser.

## Test Steps

### TC-GS-ROLE-166: Setup Column: drag reorder kolom kelas K1

1. Klik header kolom Column Visibility (⋯)
2. Klik item `Setup Column...`
Untuk setiap baris tabel "Pemindahan kolom K1" (langkah 3):
3. Drag kolom sesuai baris tabel ke posisi tujuan
4. Verifikasi tabel di balik modal mempratinjau urutan kolom `Last Updated`, `Modified By`, `Status`, `Division`, `Position`, `Name`
5. Klik `[Save]`
6. Verifikasi tabel menampilkan urutan kolom `Last Updated`, `Modified By`, `Status`, `Division`, `Position`, `Name`
7. Tekan F5
8. Verifikasi tabel tetap menampilkan urutan kolom `Last Updated`, `Modified By`, `Status`, `Division`, `Position`, `Name`

### TC-GS-ROLE-167: Setup Column: pin kolom kelas K1

9. Klik header kolom Column Visibility (⋯)
10. Klik item `Setup Column...`
Untuk setiap kolom pada tabel "Pin kolom K1" (langkah 11):
11. Klik icon pin pada kolom sesuai tabel
12. Klik `[Save]`
13. Scroll horizontal tabel
14. Verifikasi kolom K1 ter-pin tetap diam saat scroll horizontal
15. Tekan F5
16. Scroll horizontal tabel
17. Verifikasi kolom K1 tetap ter-pin dan diam saat scroll horizontal

### TC-GS-ROLE-168: Setup Column: drag reorder kolom kelas K2

18. Klik header kolom Column Visibility (⋯)
19. Klik item `Setup Column...`
20. Centang `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, dan `Region` agar kolom K2 tampil
Untuk setiap baris tabel "Pemindahan kolom K2" (langkah 21):
21. Drag kolom sesuai baris tabel ke posisi tujuan
22. Verifikasi tabel di balik modal mempratinjau urutan kolom K2 `Region`, `TAG`, `Temporary Until`, `Temporary User`, `Activation Status`
23. Klik `[Save]`
24. Verifikasi tabel menampilkan urutan kolom K2 `Region`, `TAG`, `Temporary Until`, `Temporary User`, `Activation Status`
25. Tekan F5
26. Verifikasi tabel tetap menampilkan urutan kolom K2 `Region`, `TAG`, `Temporary Until`, `Temporary User`, `Activation Status`

### TC-GS-ROLE-169: Setup Column: pin kolom kelas K2

27. Klik header kolom Column Visibility (⋯)
28. Klik item `Setup Column...`
Untuk setiap kolom pada tabel "Pin kolom K2" (langkah 29):
29. Klik icon pin pada kolom sesuai tabel
30. Klik `[Save]`
31. Scroll horizontal tabel
32. Verifikasi kolom K2 ter-pin tetap diam saat scroll horizontal
33. Tekan F5
34. Scroll horizontal tabel
35. Verifikasi kolom K2 tetap ter-pin dan diam saat scroll horizontal

### TC-GS-ROLE-170: Setup Column: Reset to Default

36. Klik header kolom Column Visibility (⋯)
37. Klik item `Setup Column...`
38. Hilangkan centang `Division`
39. Klik `[Save]`
40. Klik header kolom Column Visibility (⋯)
41. Klik item `Setup Column...`
42. Klik `[Reset to Default]`
43. Klik `[Save]`
44. Verifikasi tabel menampilkan kolom `Name`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated`
45. Verifikasi tabel tidak menampilkan kolom `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Region`
46. Tekan F5
47. Verifikasi tabel tetap menampilkan kolom `Name`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated`
48. Verifikasi tabel tetap tidak menampilkan kolom `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Region`

### TC-GS-ROLE-173: Setup Column: konfigurasi terpisah per tabel

49. Klik header kolom Column Visibility (⋯)
50. Klik item `Setup Column...`
51. Hilangkan centang `Division`
52. Klik `[Save]`
53. Klik Tab `Read Only`
54. Verifikasi kolom `Division` tampil di Tab Read Only
55. Klik Tab `System`
56. Klik Role Name `Manage TAG`
57. Verifikasi kolom `Division` tampil di Detail "Manage TAG"
58. Klik tombol Back browser
59. Klik Tab `Total Control`
60. Verifikasi kolom `Division` tetap tidak tampil di Tab Total Control
61. Klik header kolom Column Visibility (⋯)
62. Klik item `Setup Column...`
63. Centang `Division`
64. Klik `[Save]`

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE (preferensi kolom disimpan di browser; tabel dan Detail dimuat dari backend nyata).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (166, 167, 168, 169, 170, 173) dipertahankan; TC-GS-ROLE-170 (Reset to Default) mengembalikan konfigurasi hasil reorder, pin, dan kolom K2 yang tampil ke default sebelum TC-GS-ROLE-173.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 20 yang mencentang kolom K2 karena kolom K2 harus tampil agar dapat dipratinjau, di-reorder, dan di-pin di TC-GS-ROLE-168 dan 169; langkah 38 dan 39 (langkah 1 TC-GS-ROLE-170: "Ubah konfigurasi kolom lalu Save"); dan langkah 61 sampai 64 (membuka popup, mencentang kembali `Division`, `[Save]`) yang memulihkan kolom `Division` (hook `after` sebagai cadangan).
- Langkah 3, 11, 21, dan 29 diulang per baris tabel pada Prerequisites: 6 iterasi untuk langkah 3 dan 11 dan 5 iterasi untuk langkah 21 dan 29 (18 langkah tambahan setelah ekspansi).
- Spec melewati sekitar 35 langkah (64 langkah nominal, 82 setelah ekspansi) karena enam TC memakai tabel dan modal Setup Column yang sama dan satu kelas harness (fungsional, preferensi di browser); TC-GS-ROLE-166 sampai 169 masing-masing menguji enam atau lima kolom sesuai Data Uji TC dan memakai ekspansi tabel. Kegagalan keras satu blok tidak membuat blok lain kehilangan makna karena tiap blok membuka popup sendiri lewat header Column Visibility, dan blok TC-GS-ROLE-170 mengubah konfigurasi lebih dulu sebelum Reset sehingga tidak bergantung pada blok sebelumnya; hanya TC-GS-ROLE-173 meminta kolom `Division` tampil di awal, yang dipenuhi oleh Reset pada TC-GS-ROLE-170.
- Asersi tambahan (konkretisasi Expected): TC-GS-ROLE-170 Expected a mengasersi daftar kolom tampil dan tersembunyi sesudah Reset; urutan dan pin tidak diasersi karena tidak disebut Expected.
- Pembagian TC lintas spec: TC-GS-ROLE-162 sampai 165, 171, 172 (screening, hide/show, tutup tanpa Save, kolom visible terakhir) berada di spec 056; Setup Column Tab System (TC-GS-ROLE-183 dan 184) di spec 060.
- Temuan untuk QA:
  - TC-GS-ROLE-167 dan 169: TC tidak menyebut kondisi agar tabel dapat di-scroll horizontal; spec meminta viewport yang membuat tabel memiliki scroll horizontal (Prerequisites).
  - TC-GS-ROLE-168 dan 169: TC tidak menyebut bahwa kolom K2 harus ditampilkan lebih dulu agar dapat dipratinjau dan di-pin ("yang tampil" hanya ada di TC-GS-ROLE-169); spec mencentang kolom K2 sebagai langkah penghubung.
  - TC-GS-ROLE-166 dan 168: posisi baru tiap kolom tidak disebut; spec memakai urutan terbalik pada tabel Prerequisites.
  - TC-GS-ROLE-170 Expected a: TC tidak menyebut urutan dan pin sesudah Reset; spec tidak mengasersinya.
  - TC-GS-ROLE-173: TC tidak menyebut cara kembali dari Detail; spec memakai tombol Back browser.
