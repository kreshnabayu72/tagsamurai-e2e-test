---
id: TC-FA-SU-E2E-105-edit-home-group-aktor-manage-global-user-dan-role-kunci-baris-group-manager-dan-dialog-gabungan
title: "Edit Home Group oleh Aktor Manage global user & role: Kunci Baris Group Manager dan Dialog Gabungan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1068
coverage:
  web: automated
---

# Edit Home Group oleh Aktor Manage global user & role: Kunci Baris Group Manager dan Dialog Gabungan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage global user & role (Update) Qori Akbar (Pre-setup #4), email akun ini tidak tertulis di Pre-setup TC (disediakan tim FE), kredensial `Spectra.env.FA_MURG_UPD_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite (Total Control Lina Marlina, `FA_TC_PASSWORD`).
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23). Pengguna target: Oscar Pranata (Pre-setup #9; Group Manager IT Infrastructure dan Accounts Payable dengan Group Role Manage group C/R/U/D pada kedua grup). Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Edit Home Group` pada Tab Changelog pengguna target, Tab System Log aktor, dan Activity Log, dibaca sebelum dan sesudah aksi. Audit trail bersifat permanen sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Pemulihan Oscar Pranata pada langkah 26 dan di hook `after`. Efek pada Pre-setup: Home Group dan status Group Manager Oscar Pranata berubah (Last Updated, Modified By) dan entri log permanen `Edit Home Group` serta `Auto-Revert` bertambah.

## Test Steps

1. Catat jumlah entri `Edit Home Group` dan `Auto-Revert` pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log sebagai baseline

### TC-FA-SU-1068: Edit Home Group oleh Manage global user & role

2. Buka Detail Oscar Pranata > Tab Role > Sub-tab Group Role
3. Klik row action `[Assign Group]` pada baris Manage group
4. Hover checkbox CRUD dan ikon hapus baris IT Infrastructure dan Accounts Payable
5. Verifikasi checkbox CRUD dan ikon hapus baris IT Infrastructure dan Accounts Payable Disabled dengan tooltip "You don't have permission to edit."
6. Klik `[+ Assign Group]`
7. Hover node IT Infrastructure dan Accounts Payable pada popup Select Group
8. Verifikasi node IT Infrastructure dan Accounts Payable pada popup Select Group Disabled dengan tooltip "You don't have permission to edit."
9. Tutup kedua popup tanpa perubahan
10. Kembali ke User List lalu klik ⋯ pada baris Oscar Pranata
11. Verifikasi aksi `Edit Home Group` tampil pada baris Oscar Pranata
12. Klik `Edit Home Group`
13. Klik node Accounts Payable lalu klik `[Select]`
14. Verifikasi dialog Title `Remove Group Manager` memuat bagian konfirmasi constraint lebih dulu, diikuti `This edit will remove Group Manager status for this group. Their role permissions in this group will remain as edited.` dan `Are you sure you want to remove it?`
15. Verifikasi tombol `[Cancel]` (Text, Contrast) dan `[Remove]` tampil
16. Klik `[Remove]`
17. Verifikasi Home Group Oscar Pranata berubah menjadi Accounts Payable
18. Verifikasi toast "Success, home group has been updated." tampil
19. Buka Detail Oscar Pranata > Tab Role
20. Verifikasi banner Group Manager Oscar Pranata hanya memuat grup yang masih dikelola
21. Buka Tab Changelog Oscar Pranata
22. Verifikasi entri `Edit Home Group` tercatat
23. Verifikasi entri `Auto-Revert` / Object `Group Manager` / Field `Group Manager — IT Infrastructure` / Old Value `Assigned` / New Value `—` tercatat
24. Baca jumlah entri `Edit Home Group` dan `Auto-Revert` pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log
25. Verifikasi jumlah entri `Edit Home Group` dan `Auto-Revert` bertambah masing-masing 1 dibanding baseline pada Tab Changelog Oscar Pranata, Tab System Log aktor, dan Activity Log
26. Pulihkan Home Group dan status Group Manager Oscar Pranata ke kondisi Pre-setup lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular. Aktor Manage global user & role (Update) Qori Akbar login di hook `before` (akun pertama spec).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (baseline), menutup kedua popup tanpa perubahan, kembali ke User List, membuka Detail dan Tab Changelog, serta langkah 26 (pemulihan).
- Temuan untuk QA (S-15): (1) Post Condition TC-FA-SU-1068 butir c (notifikasi in-app view-only terkirim ke pengguna target) tidak punya langkah observasi dan tidak diasersi; notifikasi diasersi pada spec 094 (TC-FA-SU-319). (2) Email akun Qori Akbar tidak tertulis di Pre-setup TC. (3) TC-FA-SU-1068 langkah 6 membuka Tab Changelog pada Detail Oscar Pranata; Post Condition butir b meminta entri pada Tab System Log aktor dan Activity Log, diamati lewat selisih jumlah.
