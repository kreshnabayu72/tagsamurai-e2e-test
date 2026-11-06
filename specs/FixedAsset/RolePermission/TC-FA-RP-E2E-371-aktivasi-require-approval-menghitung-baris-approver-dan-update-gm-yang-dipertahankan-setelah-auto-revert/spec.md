---
id: TC-FA-RP-E2E-371-aktivasi-require-approval-menghitung-baris-approver-dan-update-gm-yang-dipertahankan-setelah-auto-revert
title: "Setelah auto-revert Group Manager, baris Approver dan Manage asset & TAG Update yang dipertahankan dihitung sebagai approver terdaftar saat aktivasi Require Approval"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1203
coverage:
  web: automated
---

# Setelah auto-revert Group Manager, baris Approver dan Manage asset & TAG Update yang dipertahankan dihitung sebagai approver terdaftar saat aktivasi Require Approval

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada `Company Isolated` (Pre-setup #35). Email tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE, password `Spectra.env.FA_ISOLATED_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, bagian "Hook suite".
- Data Pre-setup (dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas belum ada, disediakan tim FE): #18 (struktur group, `Helpdesk` di bawah `IT Infrastructure`) dan #35 (`Company Isolated`: struktur group sama dengan #18; tanpa Group Manager; `Helpdesk` tanpa Approver manual dan tanpa pemegang Update `Manage asset & TAG`; Require Approval transaksi OFF di semua node; Pandu Wijaya mencakup `Helpdesk` hanya pada sub-tab `Disposal`, sehingga sub-tab `Damaged` yang tanpa Approver manual di node mana pun, termasuk ancestor, dipakai untuk langkah Transaction Role).
- Kondisi awal yang di-seed di hook `before` (precondition TC, dipakai sebagai precondition, tidak diasersi): Kevin Susanto (Active) ditugaskan Group Manager hanya di `Helpdesk` pada `Company Isolated` dengan baris pola GM (Group Role termasuk `Manage group` dan `Manage asset & TAG` Update, serta Approver sub-tab `Damaged`). `Helpdesk` tanpa pemegang Update lain, tanpa Approver manual yang mencakup sub-tab `Damaged`, dan tanpa Group Manager lain; toggle `Require Approval for Registration` dan `Require Approval for Damaged` OFF. Seeding lewat kemampuan seeding API yang disediakan tim FE/BE (tanpa endpoint karangan).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: penugasan Group Manager Kevin Susanto di `Helpdesk` dilepas oleh langkah 6 (baris pola GM dipertahankan sebagai penugasan biasa; baris `Manage group` `Helpdesk` berubah menjadi Delete tidak tercentang); toggle `Require Approval for Registration` pada Detail Role `Manage asset & TAG` `Helpdesk` diaktifkan oleh langkah 11 dan `Require Approval for Damaged` pada `Helpdesk` diaktifkan oleh langkah 18. Hook `after` memulihkan Kevin Susanto ke state Pre-setup #35 dan mengembalikan kedua toggle ke OFF, dijamin fixture backend yang disediakan tim FE/BE; tidak berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_ISOLATED_TC_PASSWORD` dan `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1203: baris Approver dan Manage asset & TAG Update yang dipertahankan dihitung sebagai approver terdaftar

1. Klik Tab `System`
2. Buka Detail Role `Manage group`
3. Klik node `Helpdesk` pada Sidebar Group Tree
4. Hapus centang Delete pada baris Kevin Susanto
5. Verifikasi dialog D-05 varian edit tampil dengan `This edit will remove Group Manager status for this group.` lalu `Their individual role permissions will remain as edited.`
6. Klik `[Remove]` pada dialog
7. Verifikasi toast sukses `Success, permissions have been updated. Kevin Susanto is no longer Group Manager for Helpdesk.`
8. Klik Tab `System`
9. Buka Detail Role `Manage asset & TAG`
10. Klik node `Helpdesk` pada Sidebar Group Tree
11. Aktifkan toggle `Require Approval for Registration`
12. Verifikasi toggle `Require Approval for Registration` menjadi ON
13. Verifikasi dialog blok `Cannot Require Approval` tidak tampil
14. Klik Tab `Transaction Role`
15. Klik node `Helpdesk` pada Sidebar Group Tree
16. Klik sub-tab `Damaged`
17. Verifikasi Kevin Susanto tampil di section Approver pada `Helpdesk` sub-tab `Damaged`
18. Aktifkan toggle `Require Approval for Damaged`
19. Verifikasi toast sukses `Success, permissions have been updated.`
20. Verifikasi toggle `Require Approval for Damaged` menjadi ON
21. Verifikasi dialog blok `Cannot Require Approval` tidak tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 21 langkah.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): navigasi Tab, Detail Role, node, dan sub-tab (langkah 1 sampai 3, 8 sampai 10, 14 sampai 16). Langkah 12 menjadi anchor positif atas asersi absence dialog blok langkah 13 (efek aktivasi tampil), dan langkah 19 dan 20 atas langkah 21 (HINT g: aktivasi berhasil).
- Pembagian TC lintas spec: TC-FA-RP-1203 hanya ada di spec ini. Pasangan negatifnya (baris pola GM selama GM aktif atau nonaktif tidak dihitung) ada di spec 359 (TC-FA-RP-1202). Post Condition TC ("Kevin Susanto dipulihkan ke state Pre-setup #35 oleh automation baseline") tidak punya langkah observasi di TC dan tidak diasersi; pemulihan ada di hook `after` (Prerequisites).
- Temuan untuk QA:
  - NC-18 (menunggu PM, belum dikonfirmasi): aturan 21b bahwa baris Approver dan `Manage asset & TAG` Update yang dipertahankan setelah auto-revert dihitung sebagai Approver manual atau pemegang Update. TC-FA-RP-1203 meng-assert perilaku PRD saat ini; bila PM menetapkan lain, langkah 12, 13, 19, 20, dan 21 perlu diubah.
  - Akun login Total Control `Company Isolated` tidak tertulis di Pre-setup TC (#35 hanya menyebut "Total Control tersedia"); akun disediakan tim FE.
  - TC-FA-RP-1203 Precondition d menugaskan Kevin Susanto Group Manager di `Helpdesk` pada `Company Isolated`, sedangkan Pre-setup #35 menyebut `Company Isolated` tanpa Group Manager dan Pre-setup #13 dan #43 menyebut Kevin Susanto Group Manager hanya di `Data Center`; keberadaan Kevin Susanto pada `Company Isolated` dan state seed-nya perlu direkonsiliasi. Spec men-seed kondisi precondition d.
  - TC-FA-RP-1203 Expected b tidak menyebut toast untuk aktivasi `Require Approval for Registration`; spec hanya mengasersi toggle ON dan tidak adanya dialog blok (toast tidak diasersi).
  - Copy dialog D-05 bertanda `copy usulan, PRD 12 #7` di TC; spec menyalin teks TC dan bergantung pada persetujuan PM. Toast langkah 7 diambil dari TC apa adanya.
  - Expected c menyatakan Kevin Susanto tampil di section Approver `Helpdesk` sub-tab `Damaged` sebelum toggle diaktifkan; spec mengasersinya sebagai anchor positif (langkah 17).
