---
id: TC-FA-RP-E2E-306-identitas-user-dihapus-permanen-cascade-tanpa-entri-log-group-manager
title: "Identitas user dihapus permanen: seluruh baris FAMS dihapus cascade tanpa entri log per role (Group Manager)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1144
coverage:
  web: automated
---

# Identitas user dihapus permanen: seluruh baris FAMS dihapus cascade tanpa entri log per role (Group Manager)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup: #15 (Budi Santoso sebagai Standard), #43 (Kevin Susanto Group Manager di `Data Center`), dan #19 (seed Role Transaksi Disposal pada `IT Infrastructure`; Pandu Wijaya sebagai Approver).
- Kondisi awal TC-FA-RP-1144 yang di-seed: Budi Santoso memegang Group Manager di `Helpdesk` dan Asset Admin di `IT Infrastructure` (sub-tab `Disposal`), tanpa Total Control.
- Kemampuan teknis: penghapusan identitas dikerjakan lewat UI Global Settings > User sesuai langkah TC. Seeding kondisi awal (penugasan Group Manager dan Asset Admin Budi Santoso) lewat seeding API di hook `before` (kemampuan disediakan tim FE/BE, tanpa endpoint karangan). Pemulihan di hook `after`: identitas Budi Santoso beserta penugasannya dipulihkan ke Tabel Data Uji Pre-setup TC lewat seeding API (Catatan TC "Pemulihan fixture destruktif").
- Baseline audit trail (S-12): jumlah entri Changelog Tab Group Manager dicatat sebelum aksi lewat kemampuan baca yang disediakan tim FE/BE.
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`. Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1144: Identitas user dihapus permanen: seluruh baris FAMS dihapus cascade tanpa entri log per role (Group Manager)

1. Catat baseline (aksi tanpa `Verifikasi`): jumlah entri pada Changelog Tab Group Manager
2. Hapus identitas Budi Santoso di Global Settings > User
3. Tunggu aksi selesai: identitas terhapus
4. Buka Tab Group Manager
5. Verifikasi sedikitnya satu baris pengguna lain tampil di Tab Group Manager
6. Verifikasi Budi Santoso tidak ada di Tab Group Manager
7. Buka Tab Transaction Role, klik node `IT Infrastructure` lalu sub-tab `Disposal`
8. Verifikasi sedikitnya satu baris pengguna lain tampil di Tab Transaction Role
9. Verifikasi Budi Santoso tidak ada di Tab Transaction Role
10. Buka Tab Group Manager, lalu klik ikon Changelog di toolbar Tab Group Manager
11. Verifikasi modal Changelog Tab Group Manager tampil dengan jumlah entri yang terbaca
12. Verifikasi jumlah entri Changelog Tab Group Manager sama dengan baseline (tidak ada entri log per role untuk penghapusan cascade)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 12 langkah.
- Langkah penghubung (S-03): langkah 1 (pencatatan baseline), langkah 3 ("Tunggu aksi selesai"), serta pembukaan tab pada langkah 4, 7, dan 10. Pemulihan identitas dan penugasan Budi Santoso lewat seeding API di hook `after`. Asersi "tidak ada" pada langkah 6, 9, dan 12 didahului Verifikasi baris pengguna lain atau modal Changelog tampil sebagai anchor (langkah 5, 8, dan 11; bagian 8b butir 2).
- `P-1` (state berat): Expected b ("tidak ada entri log per role untuk penghapusan cascade") bergantung pada penghapusan identitas pengguna yang baru dibangun langkah 2 (cascade seluruh baris FAMS); asersi absence tetap di spec ini dengan baseline jumlah entri (S-05, S-12).
- Pembagian TC lintas spec: TC-FA-RP-905 (kasus Total Control, Tab Total Control) berada di spec `TC-FA-RP-E2E-267`; TC-FA-RP-1144 (kasus Group Manager, Tab Group Manager) berada di spec ini. Pilihan Changelog Tab Group Manager pada TC-FA-RP-1144 ditetapkan oleh editor TC, bukan oleh PRD.
- Temuan untuk QA:
  - TC-FA-RP-1144 tidak menyebut cara membaca jumlah entri Changelog; spec memakai baseline jumlah entri sebelum aksi dan membandingkannya sesudah (langkah 1 dan 12), lewat kemampuan baca yang disediakan tim FE/BE.
  - TC-FA-RP-1144 tidak menyebut baris pengguna lain pada Tab Group Manager; spec mengandalkan Kevin Susanto (Group Manager di `Data Center`, Pre-setup #43) sebagai baris lain sehingga anchor langkah 5 terpenuhi.
  - Post Condition kosong pada TC-FA-RP-1144.
