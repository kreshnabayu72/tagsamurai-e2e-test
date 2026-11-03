---
id: TC-FA-SU-E2E-130-node-sidebar-group-tree-sebagai-kriteria-data-search-filter-seleksi-select-all-dan-download
title: "Node Sidebar Group Tree sebagai Kriteria Data: Search, Filter, Seleksi, Select All, dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-375
coverage:
  web: automated
---

# Node Sidebar Group Tree sebagai Kriteria Data: Search, Filter, Seleksi, Select All, dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Data Pre-setup tambahan: pohon grup (#21), node `Finance & Accounting` (12 pengguna, seluruhnya Active). Search `corp.id` pada kolom Email menghasilkan 21 baris (Data TC).
- Kemampuan baca isi berkas unduhan CSV dan XLSX (nama berkas, header kolom, jumlah dan isi baris, encoding, nama sheet) disediakan tim FE.

## Test Steps

### TC-FA-SU-375: Node Sidebar Group Tree sebagai kriteria data

1. Klik ikon Filter, buka dropdown Status, centang `Active`, klik `[Apply]`
2. Ketik Search `corp.id`, tekan Enter
3. Pindah ke halaman 2
4. Centang satu baris pada halaman 2
5. Klik node `Finance & Accounting` pada Sidebar Group Tree
6. Verifikasi tabel kembali ke halaman 1
7. Verifikasi Search `corp.id` dan Filter Status `Active` tetap aktif dan halaman 1 memuat 10 baris
8. Pindah ke halaman 2
9. Verifikasi halaman 2 memuat 2 baris (irisan node, Search, dan Filter berjumlah 12 baris)
10. Verifikasi counter `1 User selected` tidak direset
11. Verifikasi baris yang dicentang pada langkah 4 tetap tercentang
12. Ganti isi kotak search dengan `Budi`, tekan Enter
13. Verifikasi tabel menyisakan `Budi Santoso`, `Putri Anggraeni` (2 baris)
14. Verifikasi tombol `Select All (2 records)` tampil
15. Klik `Select All`
16. Klik `Unselect All`
17. Klik ikon Download, pilih `Download as CSV`
18. Verifikasi berkas `User.csv` hanya memuat `Budi Santoso` dan `Putri Anggraeni` (irisan Search, Filter, dan node aktif)
19. Klik ⋯ pada baris Budi Santoso, klik `Detail`
20. Klik breadcrumb `User`
21. Verifikasi node `Finance & Accounting` tetap aktif setelah Back dari Detail
22. Muat ulang halaman (F5)
23. Verifikasi node `Finance & Accounting` dipulihkan setelah refresh
24. Klik node `Finance & Accounting` yang aktif
25. Verifikasi node `Finance & Accounting` tidak lagi aktif pada Sidebar Group Tree

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 dan 2 (menyiapkan Filter dan Search sesuai langkah 1 TC), 3 (pindah ke halaman 2), 16 (membersihkan seleksi, S-09), dan 19 (membuka Detail dari baris hasil).
- Urutan Expected d dipecah: pemulihan node sesudah Detail dan refresh diasersi lebih dulu, kriteria node dihapus pada langkah terakhir (8b butir 5).
- TC-FA-SU-373 dan TC-FA-SU-374 ada di spec 109.
- Temuan untuk QA (S-15): (1) Expected b TC-FA-SU-375 menyebut baris yang sudah dicentang tetap tercentang, tetapi tidak menyebut baris mana yang dicentang pada halaman 2 dan apakah baris itu masih tampil setelah node dipilih; spec mengasersi baris yang dicentang pada langkah 4 tetap tercentang (langkah 11) dan counter `1 User selected` tidak direset (langkah 10). (2) Expected d TC-FA-SU-375 tidak menyebut hasil tabel setelah node aktif dilepas; hanya status node pada Sidebar Group Tree yang diasersi.
