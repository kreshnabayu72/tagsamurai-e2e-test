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

1. Catat jumlah entri `Edit Home Group` pada Tab Changelog Hana Kusuma, Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline; catat juga daftar Global Role, Group Role, dan Transaction Role Gita Permata

### TC-FA-SU-285: Edit Home Group tunggal dari row action

2. Klik ⋯ pada baris Hana Kusuma lalu klik `Edit Home Group`
3. Klik node IT Infrastructure
4. Verifikasi node IT Infrastructure ter-highlight dan menjadi pilihan aktif
5. Verifikasi `[Select]` Enabled
6. Klik `[Select]`
7. Verifikasi popup menutup tanpa dialog
8. Verifikasi toast "Success, home group has been updated." tampil
9. Verifikasi kolom Home Group baris Hana Kusuma menjadi IT Infrastructure
10. Buka Detail Hana Kusuma
11. Verifikasi field Home Group di Detail Hana Kusuma menjadi IT Infrastructure

### TC-FA-SU-286: Edit Home Group dari ikon edit di Detail User

12. Klik ikon edit Home Group di samping badge
13. Verifikasi popup singular `Select Home Group` terbuka
14. Klik node Branch Surabaya
15. Klik `[Select]`
16. Verifikasi toast "Success, home group has been updated." tampil
17. Verifikasi badge Home Group Hana Kusuma berubah menjadi Branch Surabaya

### TC-FA-SU-288: Kosongkan Home Group singular

18. Kembali ke User List
19. Klik ⋯ pada baris Gita Permata lalu klik `Edit Home Group`
20. Klik node Finance & Accounting yang ter-highlight
21. Verifikasi tidak ada node ter-highlight
22. Verifikasi `[Select]` Enabled
23. Klik `[Select]`
24. Verifikasi tidak ada dialog
25. Verifikasi toast "Success, home group has been updated." tampil
26. Verifikasi Home Group Gita Permata menjadi `—`
27. Buka Detail Gita Permata > Tab Role
28. Verifikasi Global Role, Group Role, dan Transaction Role Gita Permata sama dengan yang dicatat pada baseline
29. Buka Tab Changelog Hana Kusuma
30. Verifikasi entri `Edit Home Group` / Object `User` / Field `Home Group` / Old Value `General Affairs` / New Value `IT Infrastructure` tercatat
31. Verifikasi entri `Edit Home Group` dengan Old Value `IT Infrastructure` dan New Value `Branch Surabaya` tercatat
32. Buka Tab Changelog Gita Permata
33. Verifikasi entri `Edit Home Group` dengan New Value `—` tercatat
34. Baca jumlah entri `Edit Home Group` pada Tab Changelog Hana Kusuma, Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
35. Verifikasi jumlah entri `Edit Home Group` bertambah 2 untuk Hana Kusuma dan 1 untuk Gita Permata dibanding baseline pada Tab Changelog target, Tab System Log aktor, dan Activity Log

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Entri log diamati sekali pada akhir spec dengan satu baseline (langkah 1) sehingga selisih kumulatif: Hana Kusuma 2 entri (TC-FA-SU-285 dan TC-FA-SU-286), Gita Permata 1 entri (TC-FA-SU-288). Satu entri yang diamati pada tiga surface (Tab Changelog target, Tab System Log aktor, Activity Log) ditulis satu `Verifikasi` (S-01).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (baseline), kembali ke User List, dan membuka Tab Changelog.
- Temuan untuk QA (S-15): Post Condition TC-FA-SU-285 butir c (kandidat Table User Picker Group Role di Role & Permission mengikuti constraint) dan TC-FA-SU-286 serta TC-FA-SU-288 (penugasan peran) tidak punya langkah observasi pada TC masing-masing dan tidak diasersi; TC-FA-SU-317 menguji kandidat picker.
