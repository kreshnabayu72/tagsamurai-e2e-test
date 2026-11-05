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
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23), varian Home Group + Role Transaksi `FaUserHGT` (#51). Pengguna target: Gita Permata (Home Group Finance & Accounting; Group Role Manage group pada Finance & Accounting; Role Transaksi Disposal × Asset Admin pada Finance & Accounting, Disposal × Approver pada Accounts Payable, dan Damaged × Staff pada IT Infrastructure yang berada di dalam constraint baru) dan Wawan Setiawan (Group Role Manage files pada IT Infrastructure dan Branch Surabaya; Manage purchase pada General Affairs dan Logistics Warehouse; Manage group pada Branch Surabaya, Finance & Accounting, dan Logistics Warehouse). Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Edit Home Group` pada Tab Changelog pengguna target, Tab System Log aktor, dan Activity Log, dibaca sebelum dan sesudah aksi. Audit trail bersifat permanen sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Pemulihan Gita Permata pada langkah 43 dan di hook `after`. Efek pada Pre-setup: Home Group, Group Role Manage group, dan dua Role Transaksi Gita Permata berubah (Last Updated dan Modified By), entri log permanen `Edit Home Group` bertambah; Wawan Setiawan tidak diubah (dialog dibatalkan).

## Test Steps

1. Catat jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline; catat Role Count serta daftar Group Role dan Role Transaksi Gita Permata

### TC-FA-SU-290: Dialog Role Outside Constraint Will Be Revoked

2. Klik ⋯ pada baris Gita Permata lalu klik `Edit Home Group`
3. Klik node IT Infrastructure lalu klik `[Select]`
4. Verifikasi dialog Title `Role Outside Constraint Will Be Revoked` dengan Body tiga bullet `• Manage group — Finance & Accounting`, `• Asset Admin — Disposal — Finance & Accounting`, dan `• Approver — Disposal — Accounts Payable`
5. Verifikasi dialog memuat kalimat `Setting the Home Group constraint to IT Infrastructure for Gita Permata will revoke these assignments outside this group.` dan `Are you sure you want to revoke them?`
6. Verifikasi tombol `[Cancel]` (Text, Contrast) dan `[Revoke]` (filled danger) tampil
7. Verifikasi Damaged × Staff pada IT Infrastructure (di dalam constraint baru) tidak didaftar pada dialog

### TC-FA-SU-292: Cancel dialog Revoke

8. Klik `[Cancel]` pada dialog
9. Verifikasi dialog tertutup
10. Verifikasi Home Group Gita Permata tetap Finance & Accounting
11. Verifikasi tidak ada toast
12. Klik `[Cancel]` pada popup Select Home Group
13. Buka Detail Gita Permata > Tab Role
14. Verifikasi Group Role dan Role Transaksi Gita Permata tidak berubah dibanding baseline
15. Kembali ke User List

### TC-FA-SU-290: Dialog untuk Wawan Setiawan

16. Klik ⋯ pada baris Wawan Setiawan lalu klik `Edit Home Group`
17. Klik node IT Infrastructure lalu klik `[Select]`
18. Verifikasi dialog memuat `for Wawan Setiawan`
19. Verifikasi dialog memuat satu bullet per assignment dan penutup `Are you sure you want to revoke them?`
20. Klik `[Cancel]` pada dialog lalu klik `[Cancel]` pada popup Select Home Group

### TC-FA-SU-291: Konfirmasi Revoke

21. Klik ⋯ pada baris Gita Permata lalu klik `Edit Home Group`
22. Klik node IT Infrastructure lalu klik `[Select]`
23. Klik `[Revoke]`
24. Verifikasi toast "Success, home group has been updated." tampil
25. Verifikasi Home Group Gita Permata berubah menjadi IT Infrastructure
26. Buka Detail Gita Permata > Tab Role > Sub-tab Group Role
27. Verifikasi Group Role Manage group pada Finance & Accounting hilang dari Sub-tab Group Role (Group `—`)
28. Buka Sub-tab Transaction Role
29. Verifikasi baris Disposal × Asset Admin dan Disposal × Approver hilang dari Sub-tab Transaction Role
30. Verifikasi baris Damaged × Staff (IT Infrastructure) tetap tampil
31. Verifikasi Role Count Gita Permata berkurang tiga dibanding baseline (satu per assignment yang tercabut)
32. Buka Tab Changelog Gita Permata
33. Verifikasi entri `Edit Home Group` dengan Old Value `Finance & Accounting` dan New Value `IT Infrastructure` tercatat
34. Baca jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
35. Verifikasi jumlah entri `Edit Home Group` bertambah 1 dibanding baseline pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log

### TC-FA-SU-293: Melepas constraint tidak mengembalikan Group Role

36. Kembali ke User List lalu klik ⋯ pada baris Gita Permata dan klik `Edit Home Group`
37. Klik ulang node IT Infrastructure lalu klik `[Select]`
38. Verifikasi tidak ada dialog saat melepas constraint
39. Buka Detail Gita Permata > Tab Role > Sub-tab Group Role
40. Verifikasi Group Role Manage group pada Finance & Accounting yang dicabut sebelumnya tidak kembali
41. Buka Sub-tab Transaction Role
42. Verifikasi baris Disposal × Asset Admin dan Disposal × Approver yang dicabut sebelumnya tidak kembali
43. Pulihkan Home Group, Group Role, dan Role Transaksi Gita Permata ke kondisi Pre-setup lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-FA-SU-292 (Cancel) diletakkan sebelum TC-FA-SU-291 (Revoke) karena TC-FA-SU-292 mensyaratkan Home Group Gita Permata masih Finance & Accounting; langkah 4 TC-FA-SU-290 (Wawan Setiawan) diletakkan sebelum Revoke supaya Wawan Setiawan tidak berubah. TC-FA-SU-291 dan TC-FA-SU-293 bergantung pada TC-FA-SU-290 ("Ulangi perubahan hingga dialog tampil" ditulis lengkap pada tiap TC, S-04).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 (baseline), menutup popup Select Home Group dengan `[Cancel]`, membuka Detail dan Sub-tab, kembali ke User List, dan langkah 43 (pemulihan). Selisih jumlah entri akhir TC-FA-SU-291 adalah 1 terhadap baseline langkah 1, sehingga Cancel pada TC-FA-SU-290 dan TC-FA-SU-292 tidak menambah entri.
- Jumlah langkah 43 (di atas 35 langkah) dengan alasan: empat TC (290-293) memakai satu seed Gita Permata (Pre-setup #51) dan satu dialog D-10 yang sama; Revoke mencabut Group Role dan Role Transaksi dalam satu transaksi sehingga tiap Expected (bullet per assignment, Role Count, baris Role Transaksi) butuh Verifikasi sendiri, dan tiap TC memulihkan seed. Memecah akan menggandakan seed dan pembukaan dialog yang sama; auditor dapat memindahkan TC-FA-SU-292/293 ke cadangan 438.
- Temuan untuk QA (S-15): TC-FA-SU-290 diperbarui (gate Home Group, Pre-setup #51): dialog Gita Permata memuat tiga bullet termasuk Role Transaksi dan bentuk jamak; Expected d (bentuk tunggal bila hanya satu assignment tercabut) tidak punya target pada Pre-setup #51 sehingga tidak diasersi, dan bullet Role Transaksi bertanda copy usulan (perlu persetujuan PM). TC-FA-SU-290 Expected c (lebih dari satu assignment) tidak menyebut pengguna dan isi bullet; spec memakai Wawan Setiawan dengan Home Group IT Infrastructure dan hanya mengamati bagian dialog yang disebut Expected (satu bullet per assignment dan penutup). Post Condition TC-FA-SU-291 butir b (satu entri pada Tab System Log aktor dan Activity Log) diamati lewat selisih jumlah; Post Condition TC-FA-SU-290 dan TC-FA-SU-293 butir lain tanpa langkah observasi tidak diasersi.
