---
id: TC-FA-RP-E2E-102-require-approval-transaction-role-prasyarat-aktivasi-1
title: "Require Approval Transaction Role: prasyarat aktivasi (1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-336
  - TC-FA-RP-338
  - TC-FA-RP-339
coverage:
  web: automated
---

# Require Approval Transaction Role: prasyarat aktivasi (1/2)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`; akun kedua untuk TC-FA-RP-339: Total Control `Company Isolated` (Pre-setup #35), akun disediakan tim FE (email tidak tertulis di Pre-setup TC, lihat Temuan untuk QA), `Spectra.env.FA_ISOLATED_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun ke `Company Isolated` pada langkah 10 sampai 12; hook `after` mengembalikan sesi ke akun default suite (Total Control Siti Rahmawati).
- Environment variable: `FA_TC_PASSWORD`, `FA_ISOLATED_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #18, #19 (Seed Role Transaksi `IT Infrastructure` sub-tab Disposal; Pandu Wijaya Approver; Require Approval OFF di semua node), #43 (Kevin Susanto Group Manager di `Data Center`, aktif; node `Data Center` tanpa Approver), dan #35 (`Company Isolated`; node `Helpdesk` tanpa Approver dan tanpa Group Manager).
- State yang diubah: toggle `Require Approval for Disposal` pada `IT Infrastructure` dan `Data Center` (Company Alpha) diaktifkan; dipulihkan ke OFF di hook `after` lewat seed API (disediakan tim FE/BE).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (toggle Require Approval OFF pada `IT Infrastructure` dan `Data Center` sub-tab `Disposal`), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-336: Aktifkan Require Approval saat ada Approver terdaftar

1. Klik Tab `Transaction Role`, klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
2. Aktifkan toggle `Require Approval for Disposal`
3. Verifikasi muncul toast sukses: `Success, permissions have been updated.`
4. Verifikasi toggle ON dan RadioGroup tampil dengan `Any approver (OR)` terpilih dan `All approvers (AND)`
5. Verifikasi teks opsi: `Any approver (OR)` dengan `One approval from any eligible approver is enough.` dan `All approvers (AND)` dengan `Every assigned approver must approve.`

### TC-FA-RP-338: Aktifkan Require Approval saat hanya ada Group Manager yang menaungi node

6. Klik node `Data Center` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
7. Aktifkan toggle `Require Approval for Disposal`
8. Verifikasi muncul toast sukses: `Success, permissions have been updated.`
9. Verifikasi toggle ON

### TC-FA-RP-339: Aktifkan Require Approval tanpa Approver dan tanpa Group Manager diblok dialog

10. Ganti akun: Logout dari akun Total Control Siti Rahmawati
11. Login sebagai Total Control `Company Isolated`
12. Buka Fixed Asset > Settings > Role & Permission > Tab Transaction Role
13. Klik node `Helpdesk` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
14. Aktifkan toggle `Require Approval for Disposal`
15. Verifikasi dialog blok severity warning: Title `Cannot Require Approval`; Body `Add at least one approver before enabling approval.`; satu tombol `[OK]`
16. Verifikasi tidak ada toast sukses
17. Klik `[OK]`
18. Verifikasi toggle kembali OFF
19. Verifikasi radio tidak tampil

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-336, TC-FA-RP-338, TC-FA-RP-339).
- Langkah penghubung (S-03): membuka Tab Transaction Role, node, dan sub-tab; ganti akun (langkah 10 sampai 12).
- Asersi "tidak ada toast sukses" (langkah 16) diletakkan segera setelah pemicu dan sesudah dialog blok tampil sebagai anchor positif (bagian 8b butir 2 dan 11).
- Temuan untuk QA:
  - TC-FA-RP-339 menyebut "Login pada `Company Isolated`" tanpa akun; akun Total Control `Company Isolated` tidak tertulis di Pre-setup TC, dicatat "disediakan tim FE" (S-11). Aktor utama spec ini Total Control Siti Rahmawati; ganti akun ke tenant `Company Isolated` dibutuhkan oleh TC-FA-RP-339.
  - Copy teks opsi dan sub-label bertanda `copy usulan, PRD 12 #1` (keputusan NC-02) diasersi literal sesuai TC; bergantung pada persetujuan PM.
  - TC-FA-RP-336 dan TC-FA-RP-338 tidak menyebut toggle dikembalikan OFF; state dipulihkan di hook `after`.
