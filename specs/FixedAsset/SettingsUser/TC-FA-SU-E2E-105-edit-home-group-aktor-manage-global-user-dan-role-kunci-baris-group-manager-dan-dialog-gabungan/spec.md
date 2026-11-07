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
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23). Pengguna target: Oscar Pranata (Pre-setup #9; Group Manager IT Infrastructure dan Accounts Payable; memegang baris pola Group Manager pada kedua grup: Group Role katalog selain Manage user & role dengan CRUD penuh sesuai kolom yang berlaku dan Transaction Role Asset Admin serta Approver pada setiap Jenis Transaksi). Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Edit Home Group` dan `Auto-Revert` pada Tab Changelog pengguna target, serta entri `Remove (via Group Manager)` pada modal Changelog User > Group Role dan modal Changelog User > Transaction Role pengguna target, dibaca sebelum dan sesudah aksi. Audit trail bersifat permanen sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Pemulihan Oscar Pranata pada langkah 32 dan di hook `after`. Efek pada Pre-setup: Home Group, status Group Manager, dan baris pola Group Manager IT Infrastructure Oscar Pranata berubah (Last Updated, Modified By), entri log permanen `Edit Home Group` serta `Auto-Revert` bertambah, dan entri `Remove (via Group Manager)` bertambah di kedua modal Changelog User.

## Test Steps

1. Catat jumlah entri `Edit Home Group` dan `Auto-Revert` pada Tab Changelog Oscar Pranata, serta jumlah entri `Remove (via Group Manager)` pada modal Changelog User > Group Role dan modal Changelog User > Transaction Role Oscar Pranata sebagai baseline

### TC-FA-SU-1068: Edit Home Group oleh Manage global user & role

2. Ketik Search `Oscar Pranata`, tekan Enter
3. Buka Detail Oscar Pranata > Tab Role > Sub-tab Group Role
4. Klik row action `[Assign Group]` pada baris Manage group
5. Hover checkbox CRUD dan ikon hapus baris IT Infrastructure dan Accounts Payable
6. Verifikasi checkbox CRUD dan ikon hapus baris IT Infrastructure dan Accounts Payable Disabled dengan tooltip "You don't have permission to edit."
7. Klik `[+ Assign Group]`
8. Hover node IT Infrastructure dan Accounts Payable pada popup Select Group
9. Verifikasi node IT Infrastructure dan Accounts Payable pada popup Select Group Disabled dengan tooltip "You don't have permission to edit."
10. Tutup kedua popup tanpa perubahan
11. Kembali ke User List lalu klik ⋯ pada baris Oscar Pranata
12. Verifikasi aksi `Edit Home Group` tampil pada baris Oscar Pranata
13. Klik `Edit Home Group`
14. Klik node Accounts Payable lalu klik `[Select]`
15. Verifikasi dialog Title `Role Outside Constraint Will Be Revoked` memuat bullet `• Manage group — IT Infrastructure` dan `• Group Manager — IT Infrastructure`, kalimat `Setting the Home Group constraint to Accounts Payable for Oscar Pranata will revoke these assignments outside this group.` dan `Are you sure you want to revoke them?`
16. Verifikasi tombol `[Cancel]` (Text, Contrast) dan `[Revoke]` tampil
17. Klik `[Revoke]`
18. Verifikasi Home Group Oscar Pranata berubah menjadi Accounts Payable
19. Verifikasi toast "Success, home group has been updated." tampil
20. Buka Detail Oscar Pranata > Tab Role
21. Verifikasi banner Group Manager Oscar Pranata hanya memuat grup yang masih dikelola
22. Buka Tab Changelog Oscar Pranata
23. Verifikasi entri `Edit Home Group` tercatat
24. Verifikasi entri `Auto-Revert` / Object `Group Manager` / Field `Group Manager — IT Infrastructure` / Old Value `Assigned` / New Value `—` tercatat
25. Baca jumlah entri `Edit Home Group` dan `Auto-Revert` pada Tab Changelog Oscar Pranata
26. Verifikasi jumlah entri `Edit Home Group` dan `Auto-Revert` bertambah masing-masing 1 dibanding baseline pada Tab Changelog Oscar Pranata
27. Buka Detail Oscar Pranata > Tab Role > Sub-tab Group Role, buka modal Changelog User > Group Role, muat ulang sampai entri tampil, lalu baca jumlah entri `Remove (via Group Manager)`
28. Verifikasi baris pola Group Manager IT Infrastructure ikut dicabut per baris: jumlah entri `Remove (via Group Manager)` pada modal Changelog User > Group Role bertambah dibanding baseline
29. Tutup modal dengan `[✕]`, klik Sub-tab Transaction Role, buka modal Changelog User > Transaction Role, muat ulang sampai entri tampil, lalu baca jumlah entri `Remove (via Group Manager)`
30. Verifikasi baris pola Group Manager IT Infrastructure ikut dicabut per baris: jumlah entri `Remove (via Group Manager)` pada modal Changelog User > Transaction Role bertambah dibanding baseline
31. Tutup modal dengan `[✕]`
32. Pulihkan Home Group dan status Group Manager Oscar Pranata ke kondisi Pre-setup lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular. Aktor Manage global user & role (Update) Qori Akbar login di hook `before` (akun pertama spec).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (baseline), menutup kedua popup tanpa perubahan, kembali ke User List, membuka Detail dan Tab Changelog, langkah 27, 29, dan 31 (membuka dan menutup modal Changelog User per Sub-tab, sekaligus membaca jumlah entri `Remove (via Group Manager)` lewat kemampuan baca tim FE/BE), langkah 2 (Search untuk menemukan baris target, R-16 dan butir 8b.13; nilai Search dipertahankan sesudah kembali ke User List sehingga langkah ⋯ pada baris Oscar Pranata tidak mengulang Search, butir 8b.9), serta langkah 32 (pemulihan).
- Temuan untuk QA (S-15): (1) Post Condition TC-FA-SU-1068 butir c (notifikasi in-app view-only terkirim ke pengguna target) tidak punya langkah observasi dan tidak diasersi; notifikasi diasersi pada spec 094 (TC-FA-SU-319). (2) Email akun Qori Akbar tidak tertulis di Pre-setup TC. (3) TC-FA-SU-1068 langkah 6 hanya membuka Tab Changelog pada Detail Oscar Pranata (Expected d hanya menyebut Tab Changelog); Post Condition butir b juga meminta entri pada Tab System Log aktor dan Activity Log tanpa langkah observasi di TC, sehingga asersi kedua surface itu dihapus dari spec dan hanya Tab Changelog diasersi lewat selisih jumlah (F-14). (4) Expected d TC-FA-SU-1068 menyebut baris pola Group Manager IT Infrastructure "ikut dicabut per baris" tanpa daftar baris dan jumlah; spec mengasersi selisih jumlah entri `Remove (via Group Manager)` pada kedua modal tanpa angka absolut.
