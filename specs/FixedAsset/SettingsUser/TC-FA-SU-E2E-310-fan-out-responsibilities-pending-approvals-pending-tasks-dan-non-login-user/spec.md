---
id: TC-FA-SU-E2E-310-fan-out-responsibilities-pending-approvals-pending-tasks-dan-non-login-user
title: "Fan-out Responsibilities, Pending Approvals, Pending Tasks, dan Non-Login User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-952
  - TC-FA-SU-953
  - TC-FA-SU-954
coverage:
  web: automated
---

# Fan-out Responsibilities, Pending Approvals, Pending Tasks, dan Non-Login User

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), Responsibilities (#24 dan #25), Non-Login User (#26), User Log (#30), dan Transaction Role (#39). Target baca TC-FA-SU-954: Budi Santoso Pre-setup (5 Non-Login User, hanya dibaca). Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Budi Santoso {runId}-310`, email `budi.santoso+{runId}-310@qwertysystem.net`: Active; approver permohonan Transfer pada Finance & Accounting; tanpa aset terpinjam atau ter-assign (target TC-FA-SU-952 dan TC-FA-SU-953).
  - Aset milik spec `Aset Uji {runId}-310` dan `Aset Uji {runId}-310-2` (aset sampel yang dapat dipinjam dan di-assign), dihapus lewat seed API di hook `after`.
- Kemampuan transaksi lintas modul (disediakan tim FE/BE, tanpa endpoint karangan): membuat permohonan Borrow, Return, Assignment, dan Transfer, memproses persetujuan, dan membuat task konfirmasi untuk pengguna target; pelaku kedua (Budi Santoso sebagai approver atau PIC) lewat sesi API, ditulis "... hingga ... tersimpan" (R-20), bukan konteks UI kedua.
- Akun aktor kedua untuk TC-FA-SU-954: Read Only Citra Lestari (Pre-setup #3), `readOnly_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_RO_PASSWORD` sebagai aktor tanpa wewenang Non-Login User (TC tidak menyebut aktornya, lihat Temuan untuk QA); ganti akun dengan langkah eksplisit 35 dan 36, dan hook `after` mengembalikan sesi ke akun default suite (S-07).
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-952: Responsibilities Borrowed Assets dan Assigned Assets adalah fan-out live tanpa salinan data lokal

1. Ketik Search `Budi Santoso {runId}-310`, tekan Enter, klik nama Budi Santoso {runId}-310, lalu buka Tab Responsibilities > Sub-tab Borrowed Assets
2. Pinjam aset Aset Uji {runId}-310 untuk Budi Santoso {runId}-310 di modul Borrow hingga peminjaman tersimpan
3. Tunggu aksi selesai
4. Verifikasi baris aset Aset Uji {runId}-310 muncul di Sub-tab Borrowed Assets tanpa muat ulang manual
5. Kembalikan aset Aset Uji {runId}-310 di modul Borrow hingga pengembalian tersimpan
6. Tunggu aksi selesai
7. Verifikasi baris aset Aset Uji {runId}-310 hilang dari Sub-tab Borrowed Assets
8. Buka Tab User Log > Sub-tab Borrow
9. Verifikasi baris aset Aset Uji {runId}-310 tampil sebagai `Returned` di User Log sub-tab Borrow
10. Buka Tab Responsibilities > Sub-tab Assigned Assets
11. Assign aset Aset Uji {runId}-310-2 kepada Budi Santoso {runId}-310 di modul Assignment hingga penugasan tersimpan
12. Tunggu aksi selesai
13. Verifikasi baris aset Aset Uji {runId}-310-2 muncul di Sub-tab Assigned Assets tanpa muat ulang manual
14. Buka Tab User Log > Sub-tab Assignment
15. Verifikasi baris aset Aset Uji {runId}-310-2 tampil di Assignment User Log

### TC-FA-SU-953: Pending Approvals menampilkan permohonan Waiting for Approval untuk approver eligible dan Pending Tasks dari modul pemilik

16. Buat permohonan Transfer yang membutuhkan approval Budi Santoso {runId}-310 hingga permohonan tersimpan
17. Tunggu aksi selesai, lalu buka Tab Responsibilities > Sub-tab Pending Approvals Budi Santoso {runId}-310
18. Verifikasi permohonan baru berstatus Waiting for Approval dengan Budi Santoso {runId}-310 sebagai approver eligible muncul
19. Setujui permohonan sebagai Budi Santoso {runId}-310 lewat sesi API hingga persetujuan tersimpan
20. Tunggu aksi selesai, lalu muat ulang Sub-tab Pending Approvals
21. Verifikasi baris permohonan hilang dari Pending Approvals
22. Buat task konfirmasi belum tuntas untuk Budi Santoso {runId}-310 di modul pemilik hingga task tersimpan
23. Tunggu aksi selesai, lalu buka Sub-tab Pending Tasks
24. Verifikasi task konfirmasi belum tuntas muncul di Sub-tab Pending Tasks
25. Tuntaskan task konfirmasi itu di modul pemilik hingga penuntasan tersimpan
26. Tunggu aksi selesai, lalu muat ulang Sub-tab Pending Tasks
27. Verifikasi task konfirmasi itu hilang dari Sub-tab Pending Tasks

### TC-FA-SU-954: Tab Non-Login User adalah reverse-lookup read-only dari Global Settings

28. Ganti isi kotak search dengan `Budi`, tekan Enter, klik nama Budi Santoso (Pre-setup), lalu buka Tab Non-Login User
29. Verifikasi label tab `Non-Login User (5)` menghitung Non-Login User Active dan Inactive
30. Verifikasi tabel memuat Non-Login User `Printer Lantai 5` berstatus Inactive
31. Klik Name `Printer Lantai 5`
32. Verifikasi Detail Non-Login User `Printer Lantai 5` di Global Settings terbuka
33. Kembali ke Detail Budi Santoso > Tab Non-Login User
34. Verifikasi Tab Non-Login User tidak menyediakan aksi tulis
35. Ganti akun: klik Logout pada akun saat ini
36. Login sebagai Citra Lestari (`readOnly_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_RO_PASSWORD`) lalu buka Fixed Asset > Settings > User
37. Ketik Search `Budi`, tekan Enter, klik nama Budi Santoso (Pre-setup), lalu buka Tab Non-Login User
38. Verifikasi tabel memuat Non-Login User `Printer Lantai 5`
39. Klik Name `Printer Lantai 5`
40. Verifikasi Name `Printer Lantai 5` berupa teks biasa dan tidak membuka Detail Non-Login User

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 1, 3, 6, 8, 10, 12, 14, 17, 20, 23, 26, 28, 33, 37, 35, 36; langkah baseline jumlah entri (S-12): . Langkah 1, 28, dan 37 juga Search untuk menemukan baris target (R-16); langkah 35 dan 36 adalah ganti akun eksplisit.
- Alasan di atas sekitar 35 langkah: seluruh TC satu topik (fan-out live dari modul lain ke Responsibilities) dan tiap TC berdiri sendiri; kegagalan satu TC tidak membuat TC lain kehilangan makna (40 langkah).
- Pengguna dan aset milik spec bernama sama dengan Pre-setup TC dengan suffix `{runId}-310` (S-06); TC-FA-SU-954 hanya membaca Budi Santoso Pre-setup.
- Temuan untuk QA (S-15):
  - Langkah Uji TC-FA-SU-952 tidak menyebut pembuatan assignment sedangkan Expected butir c mengasersi aset yang baru di-assign di Assigned Assets dan Assignment User Log; spec menambah langkah assign aset kedua. TC-FA-SU-953 butir c (task konfirmasi muncul lalu hilang setelah tuntas) tidak punya langkah pembuatan dan penuntasan task; spec menambahkannya sebagai kemampuan transaksi lintas modul. Isi permohonan Transfer, task, dan jalur menu modul lain tidak ditentukan TC.
  - TC-FA-SU-954 butir a menyebut label `Non-Login User (5)` menghitung Active dan Inactive; spec memakai `Printer Lantai 5` (Inactive, Pre-setup #26) sebagai pembuktian. Aktor "tanpa wewenang Non-Login User" tidak disebut TC; spec memakai Read Only Citra Lestari. Butir c (tab tidak menyediakan aksi tulis) diasersi sekali pada aktor berwenang.
  - Post Condition TC-FA-SU-952 sampai TC-FA-SU-954 tidak ada.
