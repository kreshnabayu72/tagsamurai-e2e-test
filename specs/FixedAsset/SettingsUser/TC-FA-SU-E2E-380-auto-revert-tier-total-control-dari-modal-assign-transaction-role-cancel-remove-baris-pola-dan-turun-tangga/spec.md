---
id: TC-FA-SU-E2E-380-auto-revert-tier-total-control-dari-modal-assign-transaction-role-cancel-remove-baris-pola-dan-turun-tangga
title: "Auto-Revert Tier Total Control dari Modal Assign Transaction Role: Cancel Remove Baris Pola dan Turun Tangga"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1073
  - TC-FA-SU-1070
coverage:
  web: automated
---

# Auto-Revert Tier Total Control dari Modal Assign Transaction Role: Cancel Remove Baris Pola dan Turun Tangga

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan penugasan (Pre-setup #23) dan Transaction Role (Pre-setup #39).
- Pengguna target: Lina Marlina, Total Control (Pre-setup #1, #23, dan #39) dengan baris pola Asset Admin dan Approver pada setiap Jenis Transaksi x Group.
- Data uji: Transfer pada Finance & Accounting: Asset Admin ke Monitoring & Report (TC-FA-SU-1070); baris pola yang di-Remove lalu dibatalkan: Transfer x Finance & Accounting x Asset Admin (TC-FA-SU-1073, lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE/BE): seed API untuk memulihkan penugasan Lina Marlina ke Pre-setup #23 dan #39; pembacaan jumlah entri Tab Changelog target, Tab System Log aktor, Activity Log, dan jumlah notifikasi in-app Lina Marlina sebelum aksi sebagai baseline (bagian 8b butir 10); jalur navigasi ke Tab System Log aktor dan Activity Log (tidak disebut TC). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: penugasan Transaction Role dan tier Total Control Lina Marlina; dipulihkan ke Pre-setup #23 dan #39 lewat seed API pada langkah penghubung dan di hook `after`. Suite berjalan serial.
- Target tanpa Home Group (Pre-setup #50, `FaUserNoHG`; Catatan TC: TC penugasan Tab Role Section 3d, 3e, 4c, 8, dan 9 yang memilih node bebas dijalankan pada varian tanpa Home Group, FI-32), diterapkan per target: Home Group Lina Marlina (IT Infrastructure pada Pre-setup #43) dikosongkan lewat seed API di hook `before` supaya node Finance & Accounting (langkah 16 dan 29) tidak Disabled oleh gate Home Group constraint; Home Group Lina Marlina dipulihkan ke IT Infrastructure di hook `after`. Seed per target disediakan tim FE/BE.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1073: Cancel dialog Auto-Revert pada Remove baris pola Transaction Role: tidak ada perubahan

1. Catat jumlah entri Tab Changelog Lina Marlina, Tab System Log aktor, dan Activity Log, serta jumlah notifikasi in-app Lina Marlina, sebagai baseline
2. Ketik Search `Lina Marlina`, tekan Enter, lalu klik Name `Lina Marlina`
3. Klik Tab Role lalu Sub-tab Transaction Role
4. Verifikasi banner `This user has Total Control access.` tampil di Sub-tab Transaction Role
5. Klik ⋯ pada baris pola Transfer x Finance & Accounting x Asset Admin lalu klik `Remove`
6. Verifikasi dialog Auto-Revert tampil
7. Klik `[Cancel]` pada dialog
8. Verifikasi tidak ada toast
9. Verifikasi dialog tertutup
10. Verifikasi baris Transfer x Finance & Accounting x Asset Admin tetap ada
11. Verifikasi banner `This user has Total Control access.` tetap tampil
12. Buka Tab Changelog, Search `Lina Marlina`, tekan Enter, lalu muat ulang
13. Verifikasi jumlah entri Tab Changelog Lina Marlina sama dengan baseline

### TC-FA-SU-1070: Assign Monitoring & Report (turun tangga) pada target Total Control dari modal: dialog Auto-Revert, bukan dialog turun tangga D-06

14. Klik Tab Role lalu Sub-tab Transaction Role
15. Klik `[+ Assign]`
16. Pilih Group Finance & Accounting, Transaction Transfer, Role Monitoring & Report
17. Klik `[Submit]`
18. Verifikasi dialog Auto-Revert D-05a dengan Title `Remove Total Control` tampil
19. Verifikasi penutup `Are you sure you want to remove it?`
20. Verifikasi tombol `[Cancel]` dan `[Remove]` tampil
21. Verifikasi dialog turun tangga D-06 (`Change Transaction Role`) tidak tampil dan tidak ada dialog kedua
22. Klik `[Cancel]`
23. Verifikasi tidak ada penugasan Monitoring & Report tersimpan untuk Transfer x Finance & Accounting
24. Verifikasi banner `This user has Total Control access.` tetap tampil
25. Buka Tab Changelog, Search `Lina Marlina`, tekan Enter, lalu muat ulang
26. Verifikasi jumlah entri Tab Changelog Lina Marlina sama dengan baseline
27. Klik Tab Role lalu Sub-tab Transaction Role
28. Klik `[+ Assign]`
29. Pilih Group Finance & Accounting, Transaction Transfer, Role Monitoring & Report
30. Klik `[Submit]`
31. Verifikasi dialog Auto-Revert D-05a dengan Title `Remove Total Control` tampil
32. Klik `[Remove]`
33. Verifikasi penugasan Monitoring & Report untuk Transfer x Finance & Accounting tersimpan
34. Verifikasi banner `This user has Total Control access.` hilang di Sub-tab Transaction Role
35. Verifikasi baris Transaction Role lain milik Lina Marlina tidak direset
36. Buka Tab Changelog, Search `Lina Marlina`, tekan Enter, lalu muat ulang sampai entri tampil
37. Verifikasi pasangan entri `Remove` dan `Assign` serta entri `Auto-Revert` tercatat (selisih baseline) di Tab Changelog Lina Marlina
38. Buka Tab System Log aktor
39. Verifikasi pasangan entri `Remove` dan `Assign` serta entri `Auto-Revert` tercatat (selisih baseline) di Tab System Log aktor
40. Buka Activity Log
41. Verifikasi pasangan entri `Remove` dan `Assign` serta entri `Auto-Revert` tercatat (selisih baseline) di Activity Log
42. Verifikasi jumlah notifikasi in-app ke Lina Marlina bertambah sesuai baseline
43. Pulihkan penugasan Lina Marlina ke Pre-setup #23 dan #39 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan: TC-FA-SU-1073 (Cancel tanpa perubahan) lebih dulu, lalu TC-FA-SU-1070 (Cancel lalu Remove) yang mengubah state.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 12, 14, 25, 27, 36, 38, 40 dan 43. Search `Lina Marlina` pada langkah 2, 12, 25 dan 36 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Baseline log mengikuti S-12; pemulihan lewat seed API memulihkan Pre-setup #23 dan #39 (S-06, S-09).
- Langkah pola baca-log: langkah 36 sampai 41. Asersi "tidak ada entri log" TC-FA-SU-1073 dan Cancel TC-FA-SU-1070 ditulis sebagai selisih nol terhadap baseline Tab Changelog (S-12), bukan absence kelas g.
- Alasan di atas sekitar 35 langkah (blok baca-log berpola tidak dihitung menurut bagian 3 prinsip 13, Smell): dua TC pada target yang sama (Lina Marlina) tanpa kelas harness, urutan mengikuti state (Cancel sebelum Remove); Expected memuat butir bermajemuk dan tiga surface log yang dibaca satu per satu (S-01).
- Dialog D-06 yang tidak tampil (langkah 21) didahului `Verifikasi` dialog Auto-Revert D-05a tampil (langkah 18) sebagai anchor (8b butir 2). Asersi "tidak ada toast" (langkah 8) diletakkan segera setelah `[Cancel]`, dengan dialog Auto-Revert pada langkah 6 sebagai anchor pemicu (8b butir 11).
- TC-FA-SU-1071 (naik tangga target Read Only) ada di spec 385.
- Pre-setup #50 diterapkan hanya pada Lina Marlina (bukan seluruh 25 pengguna): pemilih Group Role dan Role Transaksi men-Disabled node di luar Home Group constraint target (FI-32, tooltip S-45) dan permintaan langsung di luar constraint ditolak `422`, sedangkan TC ini memilih Finance & Accounting (langkah 16 dan 29); Home Group Lina Marlina dipulihkan di hook `after`. Mohon dikonfirmasi bila #50 harus diterapkan penuh.
- Temuan untuk QA:
  - Copy dialog D-05a varian Role Transaksi bertanda "copy usulan, perlu persetujuan PM" (TC-FA-SU-1070 butir a; PRD 12 #1 `settings-role-permission`); spec tidak mengasersi kalimat Body, hanya Title, penutup, dan tombol.
  - TC-FA-SU-1070, 1071 dan 1073 menyebut `#20` pada ACC (itu id Client `FaUserMain`, bukan nomor akun); aktor diambil dari langkah "Login sebagai Ahmad Dahlan (Default User)". Mohon dikonfirmasi.
  - TC-FA-SU-1073 langkah 2 ("satu baris pola") tidak menyebut baris yang di-Remove; spec memakai Transfer x Finance & Accounting x Asset Admin.
  - TC-FA-SU-1070 Expected butir c ("baris Transaction Role lain tidak direset") tidak menyebut baris pembanding; spec membandingkan terhadap Pre-setup #39 dan #23.
  - TC-FA-SU-1070 menyebut `[Cancel]` pada langkah 4 sebelum ulangi langkah 2 sampai 3; spec menutup alur Cancel (tanpa penugasan tersimpan) sebelum mengulang untuk `[Remove]`.
