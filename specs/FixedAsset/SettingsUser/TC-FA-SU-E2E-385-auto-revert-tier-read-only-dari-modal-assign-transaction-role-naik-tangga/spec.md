---
id: TC-FA-SU-E2E-385-auto-revert-tier-read-only-dari-modal-assign-transaction-role-naik-tangga
title: "Auto-Revert Tier Read Only dari Modal Assign Transaction Role: Naik Tangga"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1071
coverage:
  web: automated
---

# Auto-Revert Tier Read Only dari Modal Assign Transaction Role: Naik Tangga

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan penugasan (Pre-setup #23) dan Transaction Role (Pre-setup #39). Citra Lestari ber-Home Group General Affairs (Pre-setup #43/#48), sehingga Finance & Accounting di luar constraint dan Disabled di pemilih Group (tooltip S-45); sesuai Catatan TC (Home Group constraint FI-32), target tanpa Home Group memakai seed `FaUserNoHG` (Pre-setup #50), diterapkan per target: hanya Home Group Citra Lestari yang dikosongkan lewat seed API di hook `before`; penugasan lain tidak berubah. Seed `FaUserNoHG` wajib disediakan tim FE/BE sebelum eksekusi.
- Pengguna target: Citra Lestari, Read Only (Pre-setup #3 dan #23) dengan baris pola Monitoring & Report.
- Data uji: Transfer pada Finance & Accounting: Monitoring & Report ke Asset Admin (naik tangga).
- Kemampuan teknis (disediakan tim FE/BE): seed API untuk mengosongkan Home Group Citra Lestari (Pre-setup #50 per target) di hook `before` dan memulihkan penugasan serta Home Group Citra Lestari ke Pre-setup #23, #39, dan #43; pembacaan jumlah entri Tab Changelog target, Tab System Log aktor, Activity Log, dan jumlah notifikasi in-app Citra Lestari sebelum aksi sebagai baseline (bagian 8b butir 10); jalur navigasi ke Tab System Log aktor dan Activity Log (tidak disebut TC). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: penugasan Transaction Role, tier Read Only, dan Home Group (dikosongkan di hook `before`) Citra Lestari; dipulihkan ke Pre-setup #23, #39, dan #43 lewat seed API pada langkah penghubung dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1071: Naik tangga pada target Read Only dari modal: dialog Auto-Revert D-05b dan tier lepas

1. Catat jumlah entri Tab Changelog Citra Lestari, Tab System Log aktor, dan Activity Log, serta jumlah notifikasi in-app Citra Lestari, sebagai baseline
2. Ketik Search `Citra Lestari`, tekan Enter, lalu klik Name `Citra Lestari`
3. Klik Tab Role lalu Sub-tab Transaction Role
4. Verifikasi banner `This user has Read Only access.` tampil di Sub-tab Transaction Role
5. Klik `[+ Assign]`
6. Pilih Group Finance & Accounting, Transaction Transfer, Role Asset Admin
7. Klik `[Submit]`
8. Verifikasi dialog Auto-Revert D-05b dengan Title `Remove Read Only` tampil
9. Verifikasi penutup `Are you sure you want to remove it?`
10. Verifikasi tombol `[Cancel]` dan `[Remove]` tampil, bukan `[Continue]`
11. Klik `[Remove]`
12. Verifikasi penugasan Asset Admin untuk Transfer x Finance & Accounting tersimpan
13. Verifikasi banner `This user has Read Only access.` hilang di Sub-tab Transaction Role
14. Verifikasi baris Transaction Role lain milik Citra Lestari tidak direset
15. Buka Tab Changelog, Search `Citra Lestari`, tekan Enter, lalu muat ulang sampai entri tampil
16. Verifikasi entri `Assign` dan entri `Auto-Revert` tercatat (selisih baseline) di Tab Changelog Citra Lestari
17. Buka Tab System Log aktor
18. Verifikasi entri `Assign` dan entri `Auto-Revert` tercatat (selisih baseline) di Tab System Log aktor
19. Buka Activity Log
20. Verifikasi entri `Assign` dan entri `Auto-Revert` tercatat (selisih baseline) di Activity Log
21. Verifikasi jumlah notifikasi in-app ke Citra Lestari bertambah sesuai baseline
22. Pulihkan penugasan dan Home Group Citra Lestari ke Pre-setup #23, #39, dan #43 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 15, 17, 19 dan 22. Search `Citra Lestari` pada langkah 2 dan 15 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Baseline log mengikuti S-12; pemulihan lewat seed API memulihkan Pre-setup #23, #39, dan #43 (S-06, S-09).
- Langkah pola baca-log: langkah 15 sampai 20.
- TC-FA-SU-1070 dan TC-FA-SU-1073 (target Total Control) ada di spec 380.
- Temuan untuk QA:
  - TC-FA-SU-1071 Precondition tidak menyebut Pre-setup #50 sedangkan Citra Lestari ber-Home Group, sehingga Finance & Accounting akan Disabled (S-45) dan penugasan ditolak 422 V-09; spec mengikuti Catatan TC (Home Group constraint FI-32) dan memakai seed `FaUserNoHG` (Pre-setup #50) per target, bukan seluruh 25 pengguna. Mohon dikonfirmasi bila #50 harus diterapkan penuh atau Precondition TC diperbarui.
  - Copy dialog D-05b varian Role Transaksi bertanda "copy usulan, perlu persetujuan PM" (PRD 12 #1 `settings-role-permission`); spec tidak mengasersi kalimat Body, hanya Title, penutup, dan tombol.
  - TC-FA-SU-1071 menyebut `#20` pada ACC (id Client `FaUserMain`, bukan nomor akun); aktor diambil dari langkah "Login sebagai Ahmad Dahlan (Default User)". Mohon dikonfirmasi.
  - TC-FA-SU-1071 Expected butir b ("baris Transaction Role lain tidak direset") tidak menyebut baris pembanding; spec membandingkan terhadap Pre-setup #39 dan #23.
