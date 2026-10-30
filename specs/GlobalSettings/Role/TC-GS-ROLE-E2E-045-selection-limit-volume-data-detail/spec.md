---
id: TC-GS-ROLE-E2E-045-selection-limit-volume-data-detail
title: "Selection Limit Detail: Volume Data Melewati Batas Seleksi"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-124
  - TC-GS-ROLE-125
coverage:
  web: automated
---

# Selection Limit Detail: Volume Data Melewati Batas Seleksi

## Prerequisites

- Mode: FE+BE.
- Kelas harness: volume data (Selection Limit, 101 baris eligible).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti pernyataan hook suite di `suite.md`.
- Akun aktor hook `before`: Ahmad Fauzi (Total Control, Pre-setup #1), email `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan di hook `before`; hook `beforeEach` membuka Global Settings > Role & Permission > Tab System. Spec memakai satu akun; tidak ada ganti akun.
- State global yang diubah: Selection Limit diturunkan ke 100 (nilai minimum) di hook `before` lewat Admin Console > Plans & Licensing > Lifecycle Settings > System Limits; hook `before` mencatat nilai awal dan hook `after` memulihkannya. Pelaku perubahan Selection Limit tidak disebut TC, PRD, atau LLD yang dirujuk spec ini: disediakan tim FE. Suite berjalan serial (`parallel: false`, `suite.md`).
- Data Dinamis (disiapkan di hook `before` lewat seeding API, kemampuan disediakan tim FE/BE; Pre-setup #17): Detail `Manage hardware` berisi tepat 103 baris. Dua di antaranya baris dengan checkbox seleksi disabled (Ahmad Fauzi sebagai Self dan Budi Santoso sebagai Default User, Pre-setup #1 dan #2) dan 101 baris eligible. Jumlah baris eligible N = 101 ditetapkan seeding: hook mencatat jumlah baris eligible yang sudah ada (K, Pre-setup tetap), lalu men-seed 101 - K user Active (Access Global Settings, nama bersuffix `Selection Limit {nnn}+{runId}-045`) dengan baris `Manage hardware`. N tidak dibaca dari tabel yang hanya menampilkan satu halaman. Dengan Pagination default 10 baris dan urutan default Name A-Z, tabel terdiri atas 11 halaman: halaman 1 memuat Ahmad Fauzi, Budi Santoso, dan 8 baris eligible; halaman 2 sampai 10 masing-masing 10 baris eligible; halaman 11 memuat 3 baris eligible.
- Pemilihan baris per halaman pada TC-GS-ROLE-124 (langkah 3 dan 4):

| Halaman | Jumlah baris eligible yang dicentang (dari baris eligible pertama) |
|---|---|
| 1 | 8 |
| 2 | 10 |
| 3 | 10 |
| 4 | 10 |
| 5 | 10 |
| 6 | 10 |
| 7 | 10 |
| 8 | 10 |
| 9 | 10 |
| 10 | 10 |
| 11 | 2 |

- Data yang diubah spec: user seeding bersuffix `+{runId}-045` dan nilai Selection Limit. Hook `after` menghapus user seeding dan memulihkan Selection Limit ke nilai awal. Spec tidak menjalankan aksi Remove; seleksi hanya dibuat lalu dibatalkan.
- Kemampuan teknis: hover pada checkbox disabled; menunggu 10 detik (jeda pendek) untuk mengamati toast yang tidak hilang otomatis.
- Pre-setup #1 dan #2 dibaca hanya sebagai baris disabled.

## Test Steps

### TC-GS-ROLE-124: Selection Limit, centang manual melewati batas

1. Klik Role Name `Manage hardware`
2. Untuk setiap baris tabel "Pemilihan baris per halaman" (langkah 3 sampai 4):
3. Buka halaman sesuai kolom Halaman
4. Centang satu per satu (bukan checkbox header) baris eligible pertama sebanyak nilai kolom Jumlah
5. Verifikasi dua baris eligible pertama di halaman 11 checked
6. Verifikasi checkbox baris eligible ketiga di halaman 11 (baris ke-101) tampil dan disabled
7. Arahkan kursor ke checkbox baris ke-101
8. Verifikasi tooltip "You've reached the maximum selection of 100 rows."
9. Verifikasi counter "100 Users selected"
10. Verifikasi Bulk Action Bar tetap tampil dan aktif

### TC-GS-ROLE-125: Selection Limit, Select All di-cap otomatis

11. Klik `(X)` pada Bulk Action Bar
12. Buka halaman 1
13. Centang satu baris eligible di halaman 1
14. Verifikasi button "Select All (101 records)"
15. Klik button "Select All (101 records)"
16. Verifikasi toast error "Error, only the first 100 of 101 rows were selected. Narrow your filter to include the rest."
17. Verifikasi counter "100 Users selected"
18. Buka halaman 11
19. Verifikasi baris eligible ketiga di halaman 11 (baris ke-101) unchecked
20. Verifikasi Bulk Action Bar tetap tampil dan aktif
21. Tunggu 10 detik
22. Verifikasi toast error masih tampil
23. Dismiss toast error
24. Verifikasi toast error hilang
25. Klik `(X)` pada Bulk Action Bar

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC sumber.
- Langkah 2 sampai 4 diulang per baris tabel "Pemilihan baris per halaman" (11 iterasi, 8 + 90 + 2 = 100 baris tercentang). Hitungan langkah dengan ekspansi: 2 (langkah 1 dan 2) + 11 x 2 + 6 (langkah 5 sampai 10) = 30 langkah di TC-GS-ROLE-124 dan 15 langkah di TC-GS-ROLE-125, total 45 langkah.
- Spec melewati sekitar 35 langkah (45 dengan ekspansi) karena dua TC berada di satu kelas harness (volume data) dan berbagi seeding 101 baris eligible; memisahkannya menggandakan seeding volume besar. TC-GS-ROLE-125 berdiri sendiri (dimulai dari `(X)`, buka halaman 1, dan centang satu baris) sehingga kegagalan blok sebelumnya tidak membuat blok ini kehilangan makna.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka halaman (langkah 12, 18), mencentang satu baris agar Bulk Action Bar muncul (langkah 13), dan membatalkan seleksi dengan `(X)` (langkah 11, 25).
- Langkah 5 (dua baris eligible pertama halaman 11 checked) menjadi anchor positif sebelum asersi checkbox baris ke-101 disabled (langkah 6). Langkah 22 mengasersi toast error masih tampil sesudah jeda 10 detik (jeda pendek yang disebut di Prerequisites).
- Temuan untuk QA:
  - TC-GS-ROLE-124 dan TC-GS-ROLE-125 tidak punya Post Condition.
  - TC-GS-ROLE-125 langkah 1 tidak menyebut centang satu baris yang memunculkan Bulk Action Bar (button Select All hanya ada di bar); spec menambah langkah 13.
  - TC-GS-ROLE-125 Expected b ("persist sampai di-dismiss") tidak menyebut durasi pengamatan; spec memakai jeda 10 detik dan menganggap toast hilang otomatis berdurasi lebih pendek bila tidak persist.
  - TC-GS-ROLE-124 langkah 1 ("Centang 100 baris") tidak menyebut apakah checkbox header boleh dipakai; spec mencentang baris satu per satu karena judul TC menyebut "centang manual".
  - TC-GS-ROLE-124 tidak menyebut cara menurunkan Selection Limit dan pelakunya; spec menuliskannya sebagai kemampuan yang disediakan tim FE (S-13).
