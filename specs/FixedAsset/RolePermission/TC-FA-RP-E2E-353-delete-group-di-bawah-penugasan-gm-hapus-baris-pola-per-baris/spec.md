---
id: TC-FA-RP-E2E-353-delete-group-di-bawah-penugasan-gm-hapus-baris-pola-per-baris
title: "Delete Group di bawah penugasan Group Manager menghapus baris pola pada node dan descendant dengan Remove (Group Deleted) per baris"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1201
coverage:
  web: automated
---

# Delete Group di bawah penugasan Group Manager menghapus baris pola pada node dan descendant dengan Remove (Group Deleted) per baris

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Akun kedua (ganti akun eksplisit pada langkah 30 dan 31): Kevin Susanto (Pre-setup #13), akun login `kevinsusanto@qwertysystem.net` (format email data pengguna Pre-setup); password disediakan tim FE, nama env belum tertulis di `suite.md` (lihat Temuan untuk QA).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE; hanya dibaca, tidak dihapus atau diubah): #5 dan #43 (Fajar Nugroho Group Manager di `IT Infrastructure`, pemegang baris pola GM pada `IT Infrastructure` dan descendant-nya termasuk `Helpdesk`), #13 (Kevin Susanto), #18 (pohon Group; `IT Infrastructure` menjadi induk subtree milik spec), #24 (`Company Changelog`, dipakai sebagai latar log, tidak diasersi).
- Data Dinamis milik spec (S-06, S-12; pola spec 130), di-seed lewat seeding API di hook `before`: subtree Group `Zona GM {runId}-353` di bawah `IT Infrastructure` dengan anak `Rak GM {runId}-353`; Kevin Susanto Group Manager di `Zona GM {runId}-353` (baris pola GM Kevin Susanto dan Fajar Nugroho tertulis pada kedua node). Group dalam TC bernama `Data Center` dan `Rack A1` (Pre-setup bersama); spec memakai subtree milik sendiri supaya Pre-setup #18 tidak ikut terhapus. Penugasan Group Manager Kevin Susanto di `Data Center` (Pre-setup #43) tidak diubah dan menjadi pembanding positif langkah 13.
- Kemampuan teknis: seeding API dan penghapusan subtree milik spec; membaca jumlah notifikasi in-app Kevin Susanto sebagai baseline (disediakan tim FE/BE, tanpa endpoint karangan). Jendela asersi notifikasi "Tunggu 5 detik tanpa memuat ulang halaman" adalah pilihan spec (bukan nilai TC atau PRD). Nama group bersuffix unik per run sehingga baseline entri Changelog nol (S-12).
- State yang diubah dan pemulihannya: Delete Group menghapus subtree `Zona GM {runId}-353` beserta penugasan dan baris polanya. Hook `after` menghapus subtree itu bila masih ada dan memulihkan Kevin Susanto serta Fajar Nugroho ke state Pre-setup #43 lewat fixture backend yang disediakan tim FE/BE (TC: "dipulihkan ke state Pre-setup #43 oleh automation baseline"), tidak berasumsi seeding berhasil penuh. Entri Changelog dan notifikasi bersifat permanen. Spec destruktif; suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1201: Delete Group di bawah penugasan GM

1. Catat jumlah notifikasi in-app Kevin Susanto sebagai baseline lewat kemampuan baca
2. Buka Fixed Asset > Settings > Groups
3. Ketik Search `Zona GM {runId}-353`, tekan Enter
4. Klik row action `Delete` pada group `Zona GM {runId}-353`
5. Klik `[Delete]` pada dialog `Delete Group`
6. Tunggu aksi selesai: group `Zona GM {runId}-353` hilang dari daftar Group
7. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `Group Manager`
8. Verifikasi baris Fajar Nugroho di `IT Infrastructure` tetap ada di Tab `Group Manager`
9. Verifikasi baris Kevin Susanto di `Zona GM {runId}-353` hilang dari Tab `Group Manager`
10. Buka Tab `System` lalu Detail Role `Manage files`
11. Klik node `All Groups` pada Sidebar Group Tree
12. Ketik Search `Kevin Susanto`, tekan Enter
13. Verifikasi baris Kevin Susanto pada node `Data Center` (Pre-setup #43) tampil
14. Verifikasi tidak ada baris pola Kevin Susanto pada `Zona GM {runId}-353` dan `Rak GM {runId}-353`
15. Ganti isi kotak search dengan `Fajar Nugroho`, tekan Enter
16. Verifikasi baris pola Fajar Nugroho tetap ada di `IT Infrastructure` dan `Helpdesk`
17. Verifikasi tidak ada baris Fajar Nugroho pada `Zona GM {runId}-353` dan `Rak GM {runId}-353`
18. Klik ikon Changelog di toolbar Detail Role
19. Verifikasi entri Action `Remove (Group Deleted)` per baris pola Kevin Susanto dan Fajar Nugroho pada `Zona GM {runId}-353` dan `Rak GM {runId}-353`
20. Verifikasi entri tersebut bukan `Remove (via Group Manager)` dan bukan satu entri ringkasan
21. Tutup modal Changelog
22. Klik Tab `Transaction Role`
23. Klik node `Helpdesk`
24. Klik sub-tab `Disposal`
25. Verifikasi Fajar Nugroho tetap tampil di section Asset Admin dan Approver pada `Helpdesk`
26. Klik node `IT Infrastructure`
27. Klik ikon Changelog pada baris sub-tab `Disposal`
28. Verifikasi entri Action `Remove (Group Deleted)` Field `Asset Admin — Zona GM {runId}-353` dan `Approver — Zona GM {runId}-353` untuk Kevin Susanto dan Fajar Nugroho
29. Tutup modal Changelog
30. Ganti akun: logout dari akun Total Control
31. Login sebagai Kevin Susanto
32. Buka Overlay Notifikasi
33. Verifikasi panel notifikasi tampil
34. Tunggu 5 detik tanpa memuat ulang halaman
35. Verifikasi jumlah notifikasi Kevin Susanto sama dengan baseline langkah 1 (tidak ada notifikasi tentang pelepasan Group Manager di `Zona GM {runId}-353`)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 35 langkah.
- Langkah penghubung (S-03): langkah 1 (baseline, S-12), langkah 2 sampai 4 (membuka Groups dan Search mencari baris target, R-16), langkah 6 (tunggu aksi selesai, 8b butir 8), langkah 7, 10, 11, 22 sampai 24, 26, 32 (navigasi), langkah 18, 21, 27, 29 (membuka dan menutup modal Changelog), langkah 30 dan 31 (ganti akun eksplisit, S-07), langkah 34 (jendela notifikasi, bagian 6). Langkah 8, 13, 16, dan 25 adalah pembanding positif atas asersi absence sesudahnya (8b butir 2); langkah 33 adalah anchor atas langkah 35. Search langkah 12 dan 15 mengikuti kata "cari" pada TC (All Groups memuat banyak baris).
- Tanpa Search pada tabel Tab `Group Manager`: tabel memuat paling banyak tujuh baris (Pre-setup #43 ditambah satu penugasan milik spec) dalam satu halaman.
- Temuan untuk QA:
  - TC-FA-RP-1201 menamai group `Data Center` dan `Rack A1` (Pre-setup #18, dipakai bersama spec lain); spec memakai subtree milik spec bersuffix supaya Pre-setup bersama tidak terhapus (S-06). Karena itu Field Changelog pada langkah 28 memuat nama subtree (`Asset Admin — Zona GM {runId}-353`), bukan `Asset Admin — Data Center` seperti TC.
  - TC-FA-RP-1201 Expected b menyebut "tidak ada baris Kevin Susanto", sedangkan Pre-setup #13 (yang juga dirujuk precondition) memberi Kevin Susanto baris non-pola di `Helpdesk` dan Group Manager di `Data Center` (#43); spec membatasi asersi pada node yang dihapus (`Zona GM {runId}-353` dan `Rak GM {runId}-353`) dan memakai baris Kevin Susanto di `Data Center` sebagai pembanding positif. Ketidakcocokan seed Kevin Susanto (Group Manager hanya `Data Center` pada #13 dan #43 versus `Data Center` dan `Helpdesk` pada #38) belum direkonsiliasi.
  - Expected b menyebut baris pola Fajar Nugroho "tidak ada di node `Data Center` dan `Rack A1`"; padanannya di spec adalah subtree milik spec (langkah 17).
  - Expected b dan c menyebut `Remove (Group Deleted)` tanpa jumlah entri; spec tidak mengasersi jumlah. Nama Action `Remove (via Group Manager)` dan `Remove (Group Deleted)` mengikuti TC dan menunggu keputusan PM (Open Item #7c).
  - Email dan password login Kevin Susanto tidak ada di Pre-setup TC maupun `suite.md`; didaftarkan tim FE (S-11).
  - Post Condition "Group `Data Center` dan `Rack A1` dipulihkan sesuai aturan pemulihan fixture destruktif" tidak punya langkah observasi di TC; tidak diasersi, dipulihkan di hook `after`.
