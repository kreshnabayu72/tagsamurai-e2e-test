---
id: TC-FA-SU-E2E-092-constraint-home-group-dialog-role-outside-constraint-konfirmasi-revoke-cancel-dan
title: "Constraint Home Group: Dialog Role Outside Constraint, Konfirmasi Revoke, Cancel, dan Pelepasan Constraint"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-290
  - TC-FA-SU-291
  - TC-FA-SU-292
  - TC-FA-SU-293
coverage:
  web: automated
---

# Constraint Home Group: Dialog Role Outside Constraint, Konfirmasi Revoke, Cancel, dan Pelepasan Constraint

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23). Pengguna target: Gita Permata (Home Group Finance & Accounting; Group Role Manage group pada Finance & Accounting) dan Wawan Setiawan (Group Role Manage files pada IT Infrastructure dan Branch Surabaya; Manage purchase pada General Affairs dan Logistics Warehouse; Manage group pada Branch Surabaya, Finance & Accounting, dan Logistics Warehouse). Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Edit Home Group` pada Tab Changelog pengguna target, Tab System Log aktor, dan Activity Log, dibaca sebelum dan sesudah aksi. Audit trail bersifat permanen sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Pemulihan Gita Permata pada langkah 34 dan di hook `after`. Efek pada Pre-setup: Home Group dan Group Role Manage group Gita Permata berubah (Last Updated dan Modified By), entri log permanen `Edit Home Group` bertambah; Wawan Setiawan tidak diubah (dialog dibatalkan).

## Test Steps

1. Catat jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline; catat Role Count dan daftar Group Role Gita Permata

### TC-FA-SU-290: Dialog Role Outside Constraint Will Be Revoked

2. Klik ⋯ pada baris Gita Permata lalu klik `Edit Home Group`
3. Klik node IT Infrastructure lalu klik `[Select]`
4. Verifikasi dialog Title `Role Outside Constraint Will Be Revoked` dengan Body bullet `• Manage group — Finance & Accounting`, kalimat `Setting the Home Group constraint to IT Infrastructure for Gita Permata will revoke this assignment outside this group.`, dan `Are you sure you want to revoke it?`
5. Verifikasi tombol `[Cancel]` (Text, Contrast) dan `[Revoke]` (filled danger) tampil
6. Verifikasi satu assignment menggunakan bentuk tunggal

### TC-FA-SU-292: Cancel dialog Revoke

7. Klik `[Cancel]` pada dialog
8. Verifikasi dialog tertutup
9. Verifikasi Home Group Gita Permata tetap Finance & Accounting
10. Verifikasi tidak ada toast
11. Klik `[Cancel]` pada popup Select Home Group

### TC-FA-SU-290: Dialog untuk Wawan Setiawan

12. Klik ⋯ pada baris Wawan Setiawan lalu klik `Edit Home Group`
13. Klik node IT Infrastructure lalu klik `[Select]`
14. Verifikasi dialog memuat `for Wawan Setiawan`
15. Verifikasi dialog memuat satu bullet per assignment dan penutup `Are you sure you want to revoke them?`
16. Klik `[Cancel]` pada dialog lalu klik `[Cancel]` pada popup Select Home Group

### TC-FA-SU-291: Konfirmasi Revoke

17. Klik ⋯ pada baris Gita Permata lalu klik `Edit Home Group`
18. Klik node IT Infrastructure lalu klik `[Select]`
19. Klik `[Revoke]`
20. Verifikasi toast "Success, home group has been updated." tampil
21. Verifikasi Home Group Gita Permata berubah menjadi IT Infrastructure
22. Buka Detail Gita Permata > Tab Role > Sub-tab Group Role
23. Verifikasi Group Role Manage group pada Finance & Accounting hilang dari Sub-tab Group Role (Group `—`)
24. Verifikasi Role Count Gita Permata berkurang dibanding baseline
25. Buka Tab Changelog Gita Permata
26. Verifikasi entri `Edit Home Group` dengan Old Value `Finance & Accounting` dan New Value `IT Infrastructure` tercatat
27. Baca jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
28. Verifikasi jumlah entri `Edit Home Group` bertambah 1 dibanding baseline pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log

### TC-FA-SU-293: Melepas constraint tidak mengembalikan Group Role

29. Kembali ke User List lalu klik ⋯ pada baris Gita Permata dan klik `Edit Home Group`
30. Klik ulang node IT Infrastructure lalu klik `[Select]`
31. Verifikasi tidak ada dialog saat melepas constraint
32. Buka Detail Gita Permata > Tab Role > Sub-tab Group Role
33. Verifikasi Group Role Manage group pada Finance & Accounting yang dicabut sebelumnya tidak kembali
34. Pulihkan Home Group dan Group Role Gita Permata ke kondisi Pre-setup lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-FA-SU-292 (Cancel) diletakkan sebelum TC-FA-SU-291 (Revoke) karena TC-FA-SU-292 mensyaratkan Home Group Gita Permata masih Finance & Accounting; langkah 4 TC-FA-SU-290 (Wawan Setiawan) diletakkan sebelum Revoke supaya Wawan Setiawan tidak berubah. TC-FA-SU-291 dan TC-FA-SU-293 bergantung pada TC-FA-SU-290 ("Ulangi perubahan hingga dialog tampil" ditulis lengkap pada tiap TC, S-04).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (baseline), menutup popup Select Home Group dengan `[Cancel]`, kembali ke User List, dan langkah 34 (pemulihan). Selisih jumlah entri akhir TC-FA-SU-291 adalah 1 terhadap baseline langkah 1, sehingga Cancel pada TC-FA-SU-290 dan TC-FA-SU-292 tidak menambah entri.
- Temuan untuk QA (S-15): TC-FA-SU-290 Expected c (lebih dari satu assignment) tidak menyebut pengguna dan isi bullet; spec memakai Wawan Setiawan dengan Home Group IT Infrastructure dan hanya mengamati bagian dialog yang disebut Expected (satu bullet per assignment dan penutup). Post Condition TC-FA-SU-291 butir b (satu entri pada Tab System Log aktor dan Activity Log) diamati lewat selisih jumlah; Post Condition TC-FA-SU-290 dan TC-FA-SU-293 butir lain tanpa langkah observasi tidak diasersi.
