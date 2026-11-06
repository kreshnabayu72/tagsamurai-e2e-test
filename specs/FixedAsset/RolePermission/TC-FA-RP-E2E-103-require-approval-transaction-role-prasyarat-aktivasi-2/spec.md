---
id: TC-FA-RP-E2E-103-require-approval-transaction-role-prasyarat-aktivasi-2
title: "Require Approval Transaction Role: prasyarat aktivasi (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-340
  - TC-FA-RP-341
  - TC-FA-RP-342
  - TC-FA-RP-1094
coverage:
  web: automated
---

# Require Approval Transaction Role: prasyarat aktivasi (2/2)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`; akun kedua untuk TC-FA-RP-340 sampai TC-FA-RP-342: Total Control `Company Isolated` (Pre-setup #35), akun disediakan tim FE (email tidak tertulis di Pre-setup TC, lihat Temuan untuk QA), `Spectra.env.FA_ISOLATED_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun ke `Company Isolated` pada langkah 6 sampai 8; hook `after` mengembalikan sesi ke akun default suite (Total Control Siti Rahmawati).
- Environment variable: `FA_TC_PASSWORD`, `FA_ISOLATED_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #18, #19, #43 (Fajar Nugroho Group Manager di `IT Infrastructure`, aktif; node `Helpdesk` Company Alpha sub-tab `Damaged` tanpa Approver manual yang mencakup, karena Pandu Wijaya #19 hanya pada sub-tab `Disposal`) untuk TC-FA-RP-1094; #35 (`Company Isolated`: `Helpdesk` tanpa pemegang Update; Pandu Wijaya Approver pada sub-tab `Disposal` di `IT Infrastructure` yang mencakup `Helpdesk`; sub-tab `Damaged` tanpa Approver manual di node mana pun, termasuk ancestor) untuk TC-FA-RP-340 sampai TC-FA-RP-342. Status Pandu Wijaya (aktif, nonaktif, atau Read Only) dipasang lewat seed API per blok sebagai langkah penghubung.
- State yang diubah: toggle `Require Approval for Damaged` pada `Helpdesk` Company Alpha diaktifkan (TC-FA-RP-1094) dan dikembalikan ke OFF di hook `after`; status Pandu Wijaya dan penugasan Approver `Company Isolated` dipulihkan di hook `after`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (toggle Require Approval OFF pada `Helpdesk` Company Alpha dan data `Company Isolated` (Pandu Wijaya aktif, Approver `IT Infrastructure`)), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-1094: Aktifkan Require Approval Transaction Role saat hanya ada Group Manager di ancestor node

1. Klik Tab `Transaction Role`, klik node `Helpdesk` di Sidebar Group Tree, lalu klik sub-tab `Damaged`
2. Aktifkan toggle `Require Approval for Damaged`
3. Verifikasi muncul toast sukses: `Success, permissions have been updated.`
4. Verifikasi toggle ON
5. Verifikasi tidak ada dialog `Cannot Require Approval`

### TC-FA-RP-340: Approver nonaktif tidak dihitung pada prasyarat aktivasi

6. Ganti akun: Logout dari akun Total Control Siti Rahmawati
7. Login sebagai Total Control `Company Isolated`
8. Buka Fixed Asset > Settings > Role & Permission > Tab Transaction Role
9. Pulihkan state lewat seed API: Pandu Wijaya satu-satunya Approver yang mencakup node `Helpdesk` sub-tab `Disposal` (ditugaskan di sana dan pada ancestor `IT Infrastructure`), lalu dinonaktifkan di Settings > User; muat ulang halaman
10. Klik node `Helpdesk` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
11. Aktifkan toggle `Require Approval for Disposal`
12. Verifikasi dialog `Cannot Require Approval` tampil
13. Klik `[OK]`
14. Verifikasi toggle kembali OFF

### TC-FA-RP-341: Approver yang menjadi Read Only tidak dihitung pada prasyarat aktivasi

15. Pulihkan state lewat seed API: Pandu Wijaya aktif kembali sebagai satu-satunya Approver yang mencakup node `Helpdesk` sub-tab `Disposal` (ditugaskan di sana dan pada ancestor `IT Infrastructure`), lalu di-Assign Read Only; muat ulang halaman
16. Klik node `Helpdesk` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
17. Aktifkan toggle `Require Approval for Disposal`
18. Verifikasi dialog `Cannot Require Approval` tampil
19. Klik `[OK]`
20. Verifikasi toggle kembali OFF

### TC-FA-RP-342: Total Control tidak dihitung sebagai approver terdaftar pada prasyarat aktivasi

21. Pulihkan state lewat seed API: node `Helpdesk` sub-tab `Damaged` tanpa Approver yang mencakup (termasuk ancestor) dan tanpa Group Manager; muat ulang halaman
22. Klik node `Helpdesk` di Sidebar Group Tree, lalu klik sub-tab `Damaged`
23. Aktifkan toggle `Require Approval for Damaged`
24. Verifikasi dialog `Cannot Require Approval` tampil
25. Klik `[OK]`
26. Verifikasi toggle kembali OFF

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-340, TC-FA-RP-341, TC-FA-RP-342, TC-FA-RP-1094).
- Langkah penghubung (S-03): membuka Tab Transaction Role, node, dan sub-tab; ganti akun (langkah 6 sampai 8); pemulihan state seed antar blok dan `[OK]` untuk menutup dialog blok (S-09).
- Blok TC-FA-RP-1094 dijalankan lebih dulu pada tenant Company Alpha dengan akun default suite; blok TC-FA-RP-340 sampai TC-FA-RP-342 pada tenant `Company Isolated` (urutan menyimpang dari nomor TC supaya hanya satu kali ganti akun, S-05).
- Temuan untuk QA:
  - TC-FA-RP-340 sampai TC-FA-RP-342 menyebut "Login pada `Company Isolated`" tanpa akun; akun Total Control `Company Isolated` tidak tertulis di Pre-setup TC, dicatat "disediakan tim FE" (S-11). Aktor utama spec ini Total Control Siti Rahmawati; ganti akun ke tenant `Company Isolated` dibutuhkan oleh ketiga TC itu.
  - Sub-tab TC-FA-RP-342 dan TC-FA-RP-1094 memakai `Damaged` karena Approver Pandu Wijaya pada `Disposal` di `IT Infrastructure` kini mencakup `Helpdesk`; TC-FA-RP-340 dan TC-FA-RP-341 tetap `Disposal` (Approver ancestor ikut nonaktif/Read Only dan tidak dihitung).
  - Expected TC-FA-RP-340 menyebut "baris tetap tersimpan" dalam kurung tanpa langkah observasi; spec tidak mengasersinya.
  - Expected TC-FA-RP-342 menyebut "walau Total Control tersedia sebagai fallback" sebagai penjelasan; hanya dialog dan toggle OFF yang diasersi.
