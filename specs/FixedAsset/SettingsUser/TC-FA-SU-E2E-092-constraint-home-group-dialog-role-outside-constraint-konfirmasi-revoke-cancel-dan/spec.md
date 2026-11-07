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
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Pemulihan Gita Permata pada langkah 50 dan di hook `after`. Efek pada Pre-setup: Home Group, Group Role Manage group, dan dua Role Transaksi Gita Permata berubah (Last Updated dan Modified By), entri log permanen `Edit Home Group` bertambah; Wawan Setiawan tidak diubah (dialog dibatalkan).

## Test Steps

1. Catat jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline TC-FA-SU-292, serta daftar Group Role dan Role Transaksi Gita Permata

### TC-FA-SU-290: Dialog Role Outside Constraint Will Be Revoked

2. Ketik Search `Gita Permata`, tekan Enter
3. Klik ⋯ pada baris Gita Permata lalu klik `Edit Home Group`
4. Klik node IT Infrastructure lalu klik `[Select]`
5. Verifikasi dialog Title `Role Outside Constraint Will Be Revoked` dengan Body tiga bullet `• Manage group — Finance & Accounting`, `• Asset Admin — Disposal — Finance & Accounting`, dan `• Approver — Disposal — Accounts Payable`
6. Verifikasi dialog memuat kalimat `Setting the Home Group constraint to IT Infrastructure for Gita Permata will revoke these assignments outside this group.` dan `Are you sure you want to revoke them?`
7. Verifikasi tombol `[Cancel]` (Text, Contrast) dan `[Revoke]` (filled danger) tampil
8. Verifikasi Damaged × Staff pada IT Infrastructure (di dalam constraint baru) tidak didaftar pada dialog

### TC-FA-SU-292: Cancel dialog Revoke

9. Klik `[Cancel]` pada dialog
10. Verifikasi dialog tertutup
11. Verifikasi Home Group Gita Permata tetap Finance & Accounting
12. Verifikasi tidak ada toast
13. Klik `[Cancel]` pada popup Select Home Group
14. Buka Detail Gita Permata > Tab Role
15. Verifikasi Group Role dan Role Transaksi Gita Permata tidak berubah dibanding baseline TC-FA-SU-292
16. Baca jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
17. Verifikasi jumlah entri `Edit Home Group` sama dengan baseline TC-FA-SU-292 pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
18. Kembali ke User List

### TC-FA-SU-290: Dialog untuk Wawan Setiawan

19. Ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter
20. Klik ⋯ pada baris Wawan Setiawan lalu klik `Edit Home Group`
21. Klik node IT Infrastructure lalu klik `[Select]`
22. Verifikasi dialog memuat `for Wawan Setiawan`
23. Verifikasi dialog memuat satu bullet per assignment dan penutup `Are you sure you want to revoke them?`
24. Klik `[Cancel]` pada dialog lalu klik `[Cancel]` pada popup Select Home Group

### TC-FA-SU-291: Konfirmasi Revoke

25. Ganti isi kotak search dengan `Gita Permata`, tekan Enter
26. Catat jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log serta Role Count Gita Permata sebagai baseline TC-FA-SU-291
27. Klik ⋯ pada baris Gita Permata lalu klik `Edit Home Group`
28. Klik node IT Infrastructure lalu klik `[Select]`
29. Klik `[Revoke]`
30. Verifikasi toast "Success, home group has been updated." tampil
31. Verifikasi Home Group Gita Permata berubah menjadi IT Infrastructure
32. Buka Detail Gita Permata > Tab Role > Sub-tab Group Role
33. Verifikasi Group Role Manage group pada Finance & Accounting hilang dari Sub-tab Group Role (Group `—`)
34. Buka Sub-tab Transaction Role
35. Verifikasi baris Disposal × Asset Admin dan Disposal × Approver hilang dari Sub-tab Transaction Role
36. Verifikasi baris Damaged × Staff (IT Infrastructure) tetap tampil
37. Kembali ke User List
38. Verifikasi Role Count Gita Permata pada User List berkurang tiga dibanding baseline TC-FA-SU-291 (satu per assignment yang tercabut)
39. Buka Detail Gita Permata > Tab Changelog
40. Verifikasi entri `Edit Home Group` dengan Old Value `Finance & Accounting` dan New Value `IT Infrastructure` tercatat
41. Baca jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
42. Verifikasi jumlah entri `Edit Home Group` bertambah 1 dibanding baseline TC-FA-SU-291 pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log

### TC-FA-SU-293: Melepas constraint tidak mengembalikan Group Role

43. Kembali ke User List lalu klik ⋯ pada baris Gita Permata dan klik `Edit Home Group`
44. Klik ulang node IT Infrastructure lalu klik `[Select]`
45. Verifikasi tidak ada dialog saat melepas constraint
46. Buka Detail Gita Permata > Tab Role > Sub-tab Group Role
47. Verifikasi Group Role Manage group pada Finance & Accounting yang dicabut sebelumnya tidak kembali
48. Buka Sub-tab Transaction Role
49. Verifikasi baris Disposal × Asset Admin dan Disposal × Approver yang dicabut sebelumnya tidak kembali
50. Pulihkan Home Group, Group Role, dan Role Transaksi Gita Permata ke kondisi Pre-setup lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-FA-SU-292 (Cancel) diletakkan sebelum TC-FA-SU-291 (Revoke) karena TC-FA-SU-292 mensyaratkan Home Group Gita Permata masih Finance & Accounting; langkah 4 TC-FA-SU-290 (Wawan Setiawan) diletakkan sebelum Revoke supaya Wawan Setiawan tidak berubah. TC-FA-SU-291 dan TC-FA-SU-293 bergantung pada TC-FA-SU-290 ("Ulangi perubahan hingga dialog tampil" ditulis lengkap pada tiap TC, S-04).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 dan 26 (baseline per TC), langkah 2, 19, dan 25 (Search nama baris target sebelum membuka menu ⋯, karena User List memuat 3 halaman; R-16, bagian 8b butir 9 dan 13), menutup popup Select Home Group dengan `[Cancel]`, membuka Detail dan Sub-tab, kembali ke User List (langkah 18, 37, dan 43; Role Count pada langkah 38 diasersi di User List, bukan di Detail), dan langkah 50 (pemulihan). Baseline dicatat per TC (S-12): Cancel pada TC-FA-SU-292 tidak menambah entri (langkah 17 sama dengan baseline langkah 1) dan Revoke pada TC-FA-SU-291 menambah 1 entri (langkah 42 terhadap baseline langkah 26).
- Jumlah langkah 50 (di atas smell 35 langkah) dengan alasan: empat TC (290-293) memakai satu seed Gita Permata (Pre-setup #51) dan satu dialog D-10 yang sama; Revoke mencabut Group Role dan Role Transaksi dalam satu transaksi sehingga tiap Expected (bullet per assignment, Role Count, baris Role Transaksi) butuh Verifikasi sendiri, dan tiap TC memulihkan seed. Memecah akan menggandakan seed dan pembukaan dialog yang sama; auditor dapat memindahkan TC-FA-SU-292/293 ke cadangan 438.
- Temuan untuk QA (S-15): TC-FA-SU-290 diperbarui (gate Home Group, Pre-setup #51): dialog Gita Permata memuat tiga bullet termasuk Role Transaksi dan bentuk jamak; Expected d (bentuk tunggal bila hanya satu assignment tercabut) tidak punya target pada Pre-setup #51 sehingga tidak diasersi, dan bullet Role Transaksi bertanda copy usulan (perlu persetujuan PM). TC-FA-SU-290 Expected c (lebih dari satu assignment) tidak menyebut pengguna dan isi bullet; spec memakai Wawan Setiawan dengan Home Group IT Infrastructure dan hanya mengamati bagian dialog yang disebut Expected (satu bullet per assignment dan penutup). Post Condition TC-FA-SU-291 butir b (satu entri pada Tab System Log aktor dan Activity Log) diamati lewat selisih jumlah; Post Condition TC-FA-SU-290 dan TC-FA-SU-293 butir lain tanpa langkah observasi tidak diasersi.
