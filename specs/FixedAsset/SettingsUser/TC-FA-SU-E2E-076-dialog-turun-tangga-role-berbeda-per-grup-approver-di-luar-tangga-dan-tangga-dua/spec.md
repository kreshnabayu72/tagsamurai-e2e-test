---
id: TC-FA-SU-E2E-076-dialog-turun-tangga-role-berbeda-per-grup-approver-di-luar-tangga-dan-tangga-dua
title: "Dialog Turun Tangga Role Berbeda per Grup, Approver di Luar Tangga, dan Tangga Dua Tingkat"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-250
  - TC-FA-SU-251
  - TC-FA-SU-252
coverage:
  web: automated
---

# Dialog Turun Tangga Role Berbeda per Grup, Approver di Luar Tangga, dan Tangga Dua Tingkat

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan Transaction Role (Pre-setup #39) untuk TC-FA-SU-251 dan 252; tenant `FaUserTR` (Pre-setup #44, varian `FaUserMain`) untuk TC-FA-SU-250. Perpindahan tenant ke `FaUserTR` dengan akun aktor yang sama adalah kemampuan "disediakan tim FE" (TC tidak menyebut caranya, lihat Temuan untuk QA).
- Pengguna target: Mira Anggraini (Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting) pada `FaUserMain`; Putri Anggraeni pada `FaUserTR` (Disposal × Asset Admin pada Finance & Accounting dan Disposal × Staff pada IT Infrastructure).
- Data uji: Disposal × Approver pada Finance & Accounting (TC-FA-SU-251); Transfer × Asset Admin, turun ke Monitoring & Report, naik kembali ke Asset Admin pada Finance & Accounting (TC-FA-SU-252); Disposal ke Monitoring & Report pada Finance & Accounting dan IT Infrastructure (TC-FA-SU-250).
- Kemampuan teknis: seed API untuk memulihkan Transaction Role Mira Anggraini dan Putri Anggraeni ke Pre-setup #39 dan #44 (disediakan tim FE/BE); pembacaan jumlah entri Tab Changelog target sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: Transaction Role Mira Anggraini dan Putri Anggraeni; dipulihkan lewat seed API di hook `after`. Hook `after` juga mengembalikan sesi ke tenant `FaUserMain`.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-251: Approver di luar tangga: dapat dipegang bersamaan dengan role tangga tanpa konfirmasi

1. Catat jumlah entri `Assign` Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
2. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, lalu pilih Group Finance & Accounting, Transaction Disposal, dan Role Approver
3. Klik `[Submit]`
4. Verifikasi tidak ada dialog konfirmasi dan Staff yang sudah ada tidak digantikan
5. Verifikasi tabel menampilkan baris Disposal × Staff dan Disposal × Approver untuk Finance & Accounting
6. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang sampai entri tampil
7. Verifikasi entri `Assign` untuk Approver (Disposal — Finance & Accounting — Approver) bertambah satu dibanding baseline pada Tab Changelog
8. Verifikasi tidak ada entri `Assign` lain pada Tab Changelog dibanding baseline (entri log untuk Approver saja)

### TC-FA-SU-252: Jenis Transaksi tanpa Staff bertangga dua tingkat: turun dari Asset Admin ke Monitoring & Report memicu dialog

9. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, pilih Group Finance & Accounting, Transaction Transfer, Role Asset Admin, lalu klik `[Submit]`
10. Klik `[+ Assign]`, pilih Group Finance & Accounting, Transaction Transfer, Role Monitoring & Report, lalu klik `[Submit]`
11. Verifikasi dialog `Change Transaction Role` tampil (Asset Admin ke Monitoring & Report pada Transfer)
12. Klik `[Change]` pada dialog
13. Klik `[+ Assign]`, pilih Group Finance & Accounting dan Transaction Transfer, lalu buka dropdown Role
14. Verifikasi opsi Staff tidak tersedia pada Transfer
15. Pilih Role Asset Admin lalu klik `[Submit]`
16. Verifikasi tidak ada dialog dan penugasan tersimpan langsung (Monitoring & Report ke Asset Admin)
17. Verifikasi baris Transfer × Asset Admin memuat Finance & Accounting

### TC-FA-SU-250: Dialog turun tangga mendaftar role lama berbeda per grup

18. Pindah ke tenant `FaUserTR` dengan akun aktor yang sama
19. Catat jumlah entri `Remove` dan `Assign` Object `Transaction Role` Putri Anggraeni pada Tab Changelog sebagai baseline
20. Buka Detail Putri Anggraeni > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, pilih Group Finance & Accounting dan IT Infrastructure, Transaction Disposal, dan Role Monitoring & Report, lalu klik `[Submit]`
21. Verifikasi dialog mendaftar `• Finance & Accounting (currently Asset Admin)` dan `• IT Infrastructure (currently Staff)` dengan `[New Role]` Monitoring & Report yang sama
22. Klik `[Change]`
23. Tunggu aksi selesai: permintaan `[Change]` pada langkah 22 selesai dan dialog tertutup
24. Buka Tab Changelog, Search `Putri Anggraeni`, tekan Enter, lalu muat ulang sampai entri tampil
25. Verifikasi untuk Finance & Accounting tercatat entri `Remove` Asset Admin disusul entri `Assign` Monitoring & Report dibanding baseline pada Tab Changelog
26. Verifikasi untuk IT Infrastructure tercatat entri `Remove` Staff disusul entri `Assign` Monitoring & Report dibanding baseline pada Tab Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-FA-SU-251, 252, lalu 250, supaya perpindahan tenant ke `FaUserTR` terjadi satu kali di akhir (TC-FA-SU-251 dan 252 memakai `FaUserMain`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 18, 19 dan 23. Baseline log mengikuti S-12.
- Langkah pola baca-log: langkah 6 sampai 8 dan 24 sampai 26. Search nama target pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16).
- Temuan untuk QA:
  - TC-FA-SU-250 tidak menyebut tenant `FaUserTR` pada langkah dan Data Uji tidak menyebut cara berpindah tenant; spec menulisnya sebagai kemampuan "disediakan tim FE".
  - TC-FA-SU-251 butir c ("entri log Assign untuk Approver saja") tidak menyebut permukaan log; spec mengasersi Tab Changelog. TC-FA-SU-252 dan 250 menyebut pasangan entri Remove dan Assign pada Post Condition tanpa langkah observasi; spec mengasersinya pada Tab Changelog sebagai bagian dari Expected butir b TC-FA-SU-250 dan tidak mengasersi Post Condition TC-FA-SU-252 selain yang tercantum di atas.
  - TC-FA-SU-252 langkah 3 sampai 5 tidak menyebut `Verifikasi` untuk toast tiap Submit; spec tidak mengasersi toast.
