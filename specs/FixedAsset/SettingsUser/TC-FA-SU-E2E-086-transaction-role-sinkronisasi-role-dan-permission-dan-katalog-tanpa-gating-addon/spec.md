---
id: TC-FA-SU-E2E-086-transaction-role-sinkronisasi-role-dan-permission-dan-katalog-tanpa-gating-addon
title: "Transaction Role: Sinkronisasi Role & Permission dan Katalog Tanpa Gating Addon"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-277
  - TC-FA-SU-279
coverage:
  web: automated
---

# Transaction Role: Sinkronisasi Role & Permission dan Katalog Tanpa Gating Addon

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan penugasan (Pre-setup #23), Responsibilities (Pre-setup #25), dan Transaction Role (Pre-setup #39) untuk TC-FA-SU-277; tenant tanpa lisensi Addon dan tanpa Approval Workflow (Pre-setup #32, varian `FaUserStarter`/`FaUserPro`) untuk TC-FA-SU-279. Perpindahan tenant dengan akun aktor yang sama adalah kemampuan "disediakan tim FE" (TC tidak menyebut caranya, lihat Temuan untuk QA).
- Pengguna target: Mira Anggraini untuk TC-FA-SU-277; Eka Wulandari (approver permohonan Waiting for Approval; Pre-setup #25) untuk TC-FA-SU-277 butir c; pengguna target pada tenant tanpa Addon untuk TC-FA-SU-279 disediakan tim FE (TC tidak menyebutnya).
- Data uji: Transfer × Asset Admin pada Finance & Accounting untuk Mira Anggraini (TC-FA-SU-277); Group Finance & Accounting, Transaction Transfer, Role Approver (TC-FA-SU-279).
- Kemampuan teknis: seed API untuk memulihkan Transaction Role Mira Anggraini dan pengguna target tenant tanpa Addon ke Pre-setup #39 (disediakan tim FE/BE).
- State global yang diubah: Transaction Role Mira Anggraini dan pengguna target tenant tanpa Addon (Transfer × Asset Admin dan Transfer × Approver ditambahkan; baris Mira dihapus dari Panel Role Assignment); dipulihkan lewat seed API di hook `after`. Hook `after` juga mengembalikan sesi ke tenant `FaUserMain`.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-277: Sinkronisasi dua arah Transaction Role dengan Role & Permission Panel Role Assignment

1. Ketik Search `Mira Anggraini`, tekan Enter
2. Assign Transfer × Asset Admin pada Finance & Accounting untuk Mira Anggraini di Detail User > Tab Role > Sub-tab Transaction Role
3. Tunggu aksi selesai: penugasan Transfer × Asset Admin pada langkah 2 tersimpan dan popup Assign tertutup
4. Buka Role & Permission > Tab Transaction Role > Sub-tab Transfer
5. Verifikasi assignment Transfer × Asset Admin Mira Anggraini tampil di Panel Role Assignment
6. Hapus Mira Anggraini dari Panel Role Assignment
7. Tunggu aksi selesai: penghapusan Mira Anggraini dari Panel Role Assignment pada langkah 6 selesai
8. Buka Settings > User lewat sidebar, ganti isi kotak search dengan `Mira Anggraini`, tekan Enter
9. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role
10. Verifikasi perubahan dari Panel Role Assignment (Mira Anggraini dihapus dari Transfer × Asset Admin) tampil di Sub-tab Transaction Role Mira Anggraini tanpa reload manual
11. Kembali ke User List, ganti isi kotak search dengan `Eka Wulandari`, tekan Enter
12. Buka Detail Eka Wulandari > Tab Responsibilities > Sub-tab Pending Approvals
13. Verifikasi Sub-tab Pending Approvals Eka Wulandari menampilkan permohonan Waiting for Approval yang ia tunggu secara read-only

### TC-FA-SU-279: Katalog Jenis Transaksi dan role Approver tersedia tanpa gating Addon atau plan di Settings > User

14. Pindah ke tenant tanpa lisensi Addon dan tanpa Approval Workflow dengan akun aktor yang sama
15. Ketik Search nama pengguna target (disediakan tim FE), tekan Enter
16. Buka Detail pengguna target > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, pilih Group Finance & Accounting, lalu buka dropdown Transaction
17. Verifikasi dropdown Transaction memuat kesembilan Jenis Transaksi termasuk Audit, Repair Ticketing, Tracking, dan Maintenance Routine
18. Pilih Transaction Transfer dan Role Approver lalu klik `[Submit]`
19. Verifikasi penugasan Transfer × Approver pada Finance & Accounting tersimpan tanpa toast error
20. Buka Tab Transaction Admin Log
21. Verifikasi sub-tab Tab Transaction Admin Log memuat kesembilan Jenis Transaksi

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 14 (pindah tenant), langkah 3 dan 7 (menunggu aksi tulis selesai sebelum berpindah surface, bagian 8b butir 8), dan langkah 1, 8, 11, dan 15 (Search nama pengguna target sebelum membuka Detail, karena User List memuat 3 halaman; R-16, bagian 8b butir 9 dan 13; langkah 8 dan 11 mengganti isi kotak search).
- Temuan untuk QA:
  - TC-FA-SU-277 butir b menyebut "assignment yang dibuat dari Panel Role Assignment tampil di Sub-tab Transaction Role Mira", sedangkan langkah 3 menghapus Mira dari Panel Role Assignment; spec mengasersi penghapusan itu tampil di Sub-tab Transaction Role Mira. TC-FA-SU-277 langkah 1 tidak menyebut Group untuk Transfer × Asset Admin; spec memakai Finance & Accounting. TC-FA-SU-277 butir c tidak menyebut hubungan Pending Approvals Eka Wulandari dengan penugasan Mira; spec mengasersi sesuai teks Expected.
  - TC-FA-SU-279 langkah 1 tidak menyebut akun, tenant tanpa Addon, dan pengguna target; spec menulisnya sebagai kemampuan "disediakan tim FE". Butir a tidak menyebut pemeriksaan sebelum dan sesudah gating; spec hanya mengasersi kesembilan Jenis Transaksi pada tenant itu.
  - Post Condition TC-FA-SU-277 (penugasan sama pada Settings > User dan Panel Role Assignment) dan TC-FA-SU-279 (penugasan tersimpan) sudah tercakup oleh Expected di atas.
