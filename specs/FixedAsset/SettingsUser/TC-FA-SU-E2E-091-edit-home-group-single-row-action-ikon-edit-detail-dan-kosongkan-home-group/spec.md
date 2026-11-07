---
id: TC-FA-SU-E2E-091-edit-home-group-single-row-action-ikon-edit-detail-dan-kosongkan-home-group
title: "Edit Home Group Single: Row Action, Ikon Edit Detail, dan Kosongkan Home Group"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-285
  - TC-FA-SU-286
  - TC-FA-SU-288
coverage:
  web: automated
---

# Edit Home Group Single: Row Action, Ikon Edit Detail, dan Kosongkan Home Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21). Pengguna target: Hana Kusuma (General Affairs, diubah ke IT Infrastructure lalu Branch Surabaya) dan Gita Permata (Finance & Accounting, dikosongkan; Global Role Import Data dan Manage accounting, Group Role Manage group pada Finance & Accounting). Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Edit Home Group` pada Tab Changelog pengguna target, Tab System Log aktor, dan Activity Log, dibaca sebelum dan sesudah aksi. Audit trail bersifat permanen sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Pemulihan Hana Kusuma dan Gita Permata (Home Group serta Group Role) dikerjakan hook `after`. Efek pada Pre-setup: Last Updated dan Modified By kedua pengguna berubah dan entri log permanen `Edit Home Group` bertambah.

## Test Steps

1. Catat jumlah entri `Edit Home Group` pada Tab Changelog Hana Kusuma, Tab System Log aktor, dan Activity Log sebagai baseline TC-FA-SU-285

### TC-FA-SU-285: Edit Home Group tunggal dari row action

2. Ketik Search `Hana Kusuma`, tekan Enter
3. Klik ⋯ pada baris Hana Kusuma lalu klik `Edit Home Group`
4. Klik node IT Infrastructure
5. Verifikasi node IT Infrastructure ter-highlight dan menjadi pilihan aktif
6. Verifikasi `[Select]` Enabled
7. Klik `[Select]`
8. Verifikasi popup menutup tanpa dialog
9. Verifikasi toast "Success, home group has been updated." tampil
10. Verifikasi kolom Home Group baris Hana Kusuma menjadi IT Infrastructure
11. Buka Detail Hana Kusuma
12. Verifikasi field Home Group di Detail Hana Kusuma menjadi IT Infrastructure
13. Baca jumlah entri `Edit Home Group` pada Tab Changelog Hana Kusuma, Tab System Log aktor, dan Activity Log
14. Verifikasi jumlah entri `Edit Home Group` bertambah 1 dibanding baseline TC-FA-SU-285 pada Tab Changelog Hana Kusuma, Tab System Log aktor, dan Activity Log

### TC-FA-SU-286: Edit Home Group dari ikon edit di Detail User

15. Catat jumlah entri `Edit Home Group` pada Tab Changelog Hana Kusuma, Tab System Log aktor, dan Activity Log sebagai baseline TC-FA-SU-286
16. Klik ikon edit Home Group di samping badge
17. Verifikasi popup singular `Select Home Group` terbuka
18. Klik node Branch Surabaya
19. Klik `[Select]`
20. Verifikasi toast "Success, home group has been updated." tampil
21. Verifikasi badge Home Group Hana Kusuma berubah menjadi Branch Surabaya
22. Baca jumlah entri `Edit Home Group` pada Tab Changelog Hana Kusuma, Tab System Log aktor, dan Activity Log
23. Verifikasi jumlah entri `Edit Home Group` bertambah 1 dibanding baseline TC-FA-SU-286 pada Tab Changelog Hana Kusuma, Tab System Log aktor, dan Activity Log

### TC-FA-SU-288: Kosongkan Home Group singular

24. Kembali ke User List
25. Ganti isi kotak search dengan `Gita Permata`, tekan Enter
26. Catat jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log serta daftar Global Role, Group Role, dan Transaction Role Gita Permata sebagai baseline TC-FA-SU-288
27. Klik ⋯ pada baris Gita Permata lalu klik `Edit Home Group`
28. Klik node Finance & Accounting yang ter-highlight
29. Verifikasi tidak ada node ter-highlight
30. Verifikasi `[Select]` Enabled
31. Klik `[Select]`
32. Verifikasi tidak ada dialog
33. Verifikasi toast "Success, home group has been updated." tampil
34. Verifikasi Home Group Gita Permata menjadi `—`
35. Baca jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
36. Verifikasi jumlah entri `Edit Home Group` bertambah 1 dibanding baseline TC-FA-SU-288 pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
37. Buka Detail Gita Permata > Tab Role
38. Verifikasi Global Role, Group Role, dan Transaction Role Gita Permata sama dengan yang dicatat pada baseline TC-FA-SU-288
39. Buka Tab Changelog Hana Kusuma
40. Verifikasi entri `Edit Home Group` / Object `User` / Field `Home Group` / Old Value `General Affairs` / New Value `IT Infrastructure` tercatat
41. Verifikasi entri `Edit Home Group` dengan Old Value `IT Infrastructure` dan New Value `Branch Surabaya` tercatat
42. Buka Tab Changelog Gita Permata
43. Verifikasi entri `Edit Home Group` dengan New Value `—` tercatat

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Baseline entri log dicatat per TC sebelum aksi pemicu (langkah 1, 15, dan 26) dan selisih diverifikasi tepat sesudah aksi tiap TC (langkah 14, 23, dan 36): masing-masing bertambah 1 entri (S-12). Satu entri yang diamati pada tiga surface (Tab Changelog target, Tab System Log aktor, Activity Log) ditulis satu `Verifikasi` (S-01).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1, 15, dan 26 (baseline per TC), langkah 2 dan 25 (Search nama baris target sebelum membuka menu ⋯, karena User List memuat 3 halaman; R-16, bagian 8b butir 9 dan 13), kembali ke User List, dan membuka Tab Changelog.
- Jumlah langkah 43, di atas smell 35 langkah; semua blok satu topik (Edit Home Group) dan satu kelas harness (fungsional), tiap TC berdiri sendiri; kelebihan berasal dari baseline per TC dengan selisih tepat sesudah aksi (S-12) dan satu Verifikasi per klausa Expected (S-01).
- Temuan untuk QA (S-15): Post Condition TC-FA-SU-285 butir c (kandidat Table User Picker Group Role dan popup Assign Role Transaksi di Role & Permission mengikuti constraint Home Group; gate yang sama, menggantikan penyaringan afiliasi lama) dan TC-FA-SU-286 serta TC-FA-SU-288 (penugasan peran) tidak punya langkah observasi pada TC masing-masing dan tidak diasersi; TC-FA-SU-317 menguji kandidat kedua popup.
