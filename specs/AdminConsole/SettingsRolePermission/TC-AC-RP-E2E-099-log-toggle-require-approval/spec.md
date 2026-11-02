---
id: TC-AC-RP-E2E-099-log-toggle-require-approval
title: "Pencatatan Toggle Require Approval Allocation dan Wallet, Termasuk Pelaku Manage User and Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-330
  - TC-AC-RP-331
  - TC-AC-RP-442
coverage:
  web: automated
---

# Pencatatan Toggle Require Approval Allocation dan Wallet, Termasuk Pelaku Manage User and Role

## Prerequisites

- Mode: FE+BE (backend nyata; aksi dan pembacaan log lewat UI).
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Ganti akun di tengah spec: Hendra Wijaya, Global Role Manage user and role R+U (`manageUserRoleU_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_RP_MUR_U_PASSWORD`) untuk TC-AC-RP-442.
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #4 (aktor `Hendra Wijaya`), dan #17 (approver dan toggle: `Manage allocation` `Region Jawa` ON, `Sumatera` OFF tersimpan; `Manage wallet & pricing` seluruh group OFF). Target aksi memakai user, role, dan group Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Kemampuan teknis: membaca jumlah entri audit trail (Changelog, System Log, Activity Log, Changelog: User) lewat kemampuan baca tanpa mengasersi angka absolut (disediakan tim FE/BE; bagian 8b butir 10). Langkah "Catat baseline" mencatat jumlah entri sebelum aksi; asersi memakai selisih terhadap baseline (S-12). Entri yang baru dibuat aksi spec ini dikenali lewat Action, Object, dan Modified By pada halaman pertama (Date Newest First).
- Kemampuan teknis: halaman `Settings > User > Detail User` (Tab System Log) dan halaman Admin Console > Activity Log tersedia untuk akun Total Control dan `Hendra Wijaya`.
- Pemulihan baseline: kemampuan reset data Pre-setup (tingkat akses, penugasan Group Manager, peran individual, approver, toggle) ke kondisi Tabel Data Uji Pre-setup TC disediakan tim FE/BE dan dinyatakan di `suite.md`; dijalankan di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan baseline". Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Env var `AC_RP_TC_PASSWORD`, `AC_RP_MUR_U_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-330: Toggle Require Approval tercatat dengan label sesuai surface

1. Klik tab `System`
2. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
3. Klik node `Sumatera`
4. Catat baseline jumlah entri: Changelog Detail Role `Manage allocation`, System Log `Siti Nurhaliza`, dan Activity Log Admin Console
5. Klik toggle "Require Approval for Allocation" sehingga ON
6. Klik ikon Changelog
7. Verifikasi jumlah entri Changelog Detail Role bertambah 1 dibanding baseline langkah 4
8. Verifikasi entri baru: Action `Edit`, Object "Manage allocation", Field "Require Approval — Sumatera", Old Value `Off`, New Value `On`
9. Tutup modal Changelog
10. Buka Detail User `Siti Nurhaliza` > Tab System Log
11. Verifikasi jumlah entri System Log bertambah 1 dibanding baseline langkah 4
12. Verifikasi entri baru ber-Object `Group Role`, Name "Manage allocation", Field "Require Approval for Allocation — Sumatera"
13. Buka Activity Log Admin Console
14. Verifikasi jumlah entri Activity Log bertambah 1 dibanding baseline langkah 4
15. Verifikasi entri baru ber-Object `Group Role`, Name "Manage allocation", Field "Require Approval for Allocation — Sumatera"
16. Pulihkan baseline: toggle `Manage allocation` `Sumatera` kembali OFF

### TC-AC-RP-331: Toggle wallet tercatat dengan label Wallet Allocation

17. Buka halaman `Settings > Role & Permission`
18. Klik tab `System`
19. Pada section Group Role, klik `⋯` pada baris `Manage wallet & pricing` lalu klik `Detail`
20. Klik node `Region Jawa`
21. Catat baseline jumlah entri System Log `Siti Nurhaliza`
22. Klik toggle "Require Approval for Wallet Allocation" sehingga ON
23. Buka Detail User `Siti Nurhaliza` > Tab System Log
24. Verifikasi jumlah entri System Log bertambah 1 dibanding baseline langkah 21
25. Verifikasi entri baru ber-Field "Require Approval for Wallet Allocation — Region Jawa", Old Value `Off`, New Value `On`
26. Pulihkan baseline: toggle `Manage wallet & pricing` `Region Jawa` kembali OFF

### TC-AC-RP-442: Toggle oleh Manage user and role (Update) tercatat dengan pelaku aktor

27. Ganti akun: Logout, lalu login sebagai `Hendra Wijaya` (`manageUserRoleU_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_RP_MUR_U_PASSWORD`)
28. Klik menu `Settings > Role & Permission` di sidebar
29. Klik tab `System`
30. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
31. Klik node `Sumatera`
32. Catat baseline jumlah entri: Changelog Detail Role `Manage allocation`, System Log `Hendra Wijaya`, dan Activity Log Admin Console
33. Klik toggle "Require Approval for Allocation" sehingga ON
34. Klik ikon Changelog
35. Verifikasi jumlah entri Changelog Detail Role bertambah 1 dibanding baseline langkah 32
36. Verifikasi entri baru: Action `Edit`, Object "Manage allocation", Field "Require Approval — Sumatera", Old Value `Off`, New Value `On`, Modified By "Hendra W"
37. Tutup modal Changelog
38. Buka Detail User `Hendra Wijaya` > Tab System Log
39. Verifikasi jumlah entri System Log bertambah 1 dibanding baseline langkah 32
40. Verifikasi entri baru ber-Object `Group Role`, Name "Manage allocation", Field "Require Approval for Allocation — Sumatera"
41. Buka Activity Log Admin Console
42. Verifikasi jumlah entri Activity Log bertambah 1 dibanding baseline langkah 32
43. Verifikasi entri baru ber-Object `Group Role`, Name "Manage allocation", Field "Require Approval for Allocation — Sumatera"
44. Pulihkan baseline: toggle `Manage allocation` `Sumatera` kembali OFF

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 4, 9, 16, 17, 21, 26, 28, 32, 37, 44.
- Ganti akun eksplisit pada langkah 27 (S-07): TC-AC-RP-442 mensyaratkan pelaku `Hendra Wijaya`; login dan pembukaan halaman sesudahnya adalah langkah penghubung ganti akun.
- Perubahan toggle disimpan otomatis tanpa toast yang diasersi TC; asersi log dibaca sesudah memulihkan modal Changelog atau berpindah surface.
- Pemulihan baseline: kemampuan reset yang disediakan tim FE/BE (mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; S-13); dijalankan sebagai langkah penghubung "Pulihkan baseline" dan di hook `after`.
- Alasan sekitar 35 langkah (44 langkah): blok pencatatan satu kelas fungsional pada surface log yang sama; tiap blok punya aksi, target, dan baseline jumlah entri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Mekanisme "dipulihkan automation baseline" (kolom Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
  - Expected TC menyebut entri log tanpa baseline jumlah entri; karena audit trail permanen, spec mencatat baseline lewat kemampuan baca yang disediakan tim FE/BE dan mengasersi selisih (S-12).
  - Post Condition TC "Data dipulihkan automation baseline" tidak punya langkah observasi di TC sehingga tidak diasersi; spec hanya menjalankan langkah pemulihan.
  - TC-AC-RP-330 dan 331 tidak menyatakan halaman "System Log aktor"; spec membuka Tab System Log pada Detail User aktor. TC-AC-RP-442 "System Log aktor" dibaca pada Detail User `Hendra Wijaya`; akses `Hendra Wijaya` ke Detail User sendiri tidak dinyatakan TC.
  - TC-AC-RP-330 dan 442 tidak menyatakan filter Activity Log; spec membaca entri baru lewat selisih jumlah terhadap baseline.
