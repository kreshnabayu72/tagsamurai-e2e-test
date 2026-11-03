---
id: TC-AC-RP-E2E-013-role-detail-group-role-approval-settings
title: "Role Detail Group Role: Approval Settings Manage allocation dan Manage wallet & pricing"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-51
  - TC-AC-RP-52
  - TC-AC-RP-53
  - TC-AC-RP-54
  - TC-AC-RP-55
coverage:
  web: automated
---

# Role Detail Group Role: Approval Settings Manage allocation dan Manage wallet & pricing

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: Tabel Data Uji Pre-setup #11 (tree group Principal), #12 (`Dewi Anggreni`, QA Staff, Operations), #3 (`Dewi Anggraini` juga Additional Approver `Manage allocation` di `Region Jawa`), #6 (GM `Fajar Nugroho`), dan #17 (Approvers `Manage allocation` `Region Jawa` = `Dewi Anggraini`, `Dewi Anggreni`; toggle `Manage allocation` `Region Jawa` ON, `Sumatera` OFF tersimpan, group lain tanpa nilai; `Manage wallet & pricing` seluruh group OFF dan tanpa approver). Berkas fixture Pre-setup modul belum ada dan disediakan tim FE.
- Spec read-only: toggle dan "+ Assign" tidak diubah atau dijalankan; tidak ada data Dinamis, seeding, atau suffix `{runId}`. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-51: Approval Settings Manage allocation saat All Groups menampilkan prompt

1. Klik tab `System`
2. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
3. Perhatikan section di atas tabel dengan sidebar "All Groups"
4. Verifikasi section "Approval Settings" hanya berisi prompt "Select a group from the sidebar to view and manage its approvers."
5. Verifikasi toggle Require Approval, tabel Approvers, dan "+ Assign" Approvers tidak tampil

### TC-AC-RP-52: Approval Settings Manage allocation untuk group terpilih

6. Klik node `Region Jawa` di Sidebar Group Tree
7. Verifikasi toggle label "Require Approval for Allocation" bernilai ON
8. Verifikasi sub-label toggle "When enabled, hardware and license allocations, and Subscription actions (Add/Renew), submitted by users with this role will go to Waiting for Approval before the stock, license ledger, or subscription itself is updated. Group Manager and Total Control bypass this review."
9. Verifikasi sub-section "Approvers — Region Jawa" tampil dengan toolbar Search, Filter, "+ Assign"
10. Verifikasi tabel Approvers menampilkan 2 baris: `Dewi Anggraini` (Auditor, Finance) dan `Dewi Anggreni` (QA Staff, Operations)
11. Verifikasi Group Manager `Fajar Nugroho` dan Total Control tidak muncul sebagai baris Approvers

### TC-AC-RP-54: Group tanpa nilai toggle tersimpan dibaca OFF

12. Klik node `Jakarta` (belum pernah dikonfigurasi; induk `Region Jawa` bernilai ON)
13. Verifikasi toggle "Require Approval for Allocation" pada `Jakarta` bernilai OFF dan tidak mewarisi nilai `Region Jawa`

### TC-AC-RP-53: Approval Settings Manage wallet & pricing untuk group terpilih

14. Klik segmen "System" pada Breadcrumb untuk kembali ke Tab System
15. Pada section Group Role, klik `⋯` pada baris `Manage wallet & pricing` lalu klik `Detail`
16. Klik node `Region Jawa`
17. Verifikasi toggle label "Require Approval for Wallet Allocation" bernilai OFF
18. Verifikasi sub-label toggle "When enabled, Allocation Deposit/Product submitted by users with this role will go to Waiting for Approval before the wallet is debited. Group Manager and Total Control bypass this review."
19. Verifikasi sub-section "Approvers — Region Jawa" menampilkan empty state dengan Title "No approvers yet" dan Description "Assign an approver to review requests for this role."
20. Verifikasi "+ Assign" pada sub-section "Approvers — Region Jawa" tetap tersedia

### TC-AC-RP-55: Group Role lain tidak memiliki section Approval Settings

21. Klik segmen "System" pada Breadcrumb untuk kembali ke Tab System
22. Pada section Group Role, klik `⋯` pada baris `Manage partner` lalu klik `Detail`
23. Klik node `Region Jawa`
24. Verifikasi halaman Role Detail `Manage partner` tampil dengan Sidebar Group Tree dan tabel user assignments
25. Verifikasi tidak ada section "Approval Settings" di Detail `Manage partner`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Seluruh TC spec ini TC FE; spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan: TC-AC-RP-54 ditaruh sebelum TC-AC-RP-53 karena memakai Role Detail `Manage allocation` yang sama dengan TC-AC-RP-51 dan TC-AC-RP-52 (S-10, tanpa buka halaman ulang); urutan nomor TC sumber tidak memengaruhi state karena spec read-only.
- Langkah penghubung tanpa awalan Verifikasi (S-03): "Perhatikan section di atas tabel dengan sidebar All Groups" mengikuti Langkah Uji TC-AC-RP-51; langkah 14 dan 21 mengembalikan Tab System lewat Breadcrumb sebelum membuka Detail role lain (S-09).
- Verifikasi halaman Role Detail `Manage partner` tampil dengan Sidebar Group Tree dan tabel user assignments adalah anchor positif absence section Approval Settings (8b butir 2).
- Temuan untuk QA:
  - TC-AC-RP-53 menyebut sub-label toggle memuat "Group Manager and Total Control bypass this review." tetapi tidak menyatakan apakah toggle `Manage wallet & pricing` Region Jawa terkunci atau dapat diubah; spec hanya mengasersi nilai OFF dan label.
  - TC-AC-RP-52 Expected c ("Group Manager `Fajar Nugroho` dan Total Control tidak muncul sebagai baris Approvers") adalah asersi absence atas tabel dua baris; anchor memakai dua baris yang diasersi pada langkah sebelumnya.
  - Sub-label toggle TC-AC-RP-52 sangat panjang dan menyebut tiga aksi (hardware, license, Subscription); asersi memakai teks TC persis tanpa penyesuaian.
