---
id: TC-AC-SG-E2E-093-sinkron-lintas-modul-reassign-entitas-total-user-dan-create-distributor
title: "Sinkron Lintas Modul: Reassign Entitas, Total User dari Group Role dan Read Only, serta Create Distributor"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-349
  - TC-AC-SG-350
  - TC-AC-SG-353
  - TC-AC-SG-354
coverage:
  web: automated
---

# Sinkron Lintas Modul: Reassign Entitas, Total User dari Group Role dan Read Only, serta Create Distributor

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control entitas Principal, `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (ganti akun di langkah 39): Total Control `Distributor Baru {runId}-093` yang dibuat langkah 37. Email dan password akun ini tidak tertulis di Pre-setup TC; disediakan tim FE (lihat Temuan untuk QA).
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Akses akun aktor ke modul Distributor (Edit), Settings > User (Detail user > Tab Role), Settings > Role & Permission, Activity Log, dan form Create Distributor tersedia (Pre-setup #40).
- Data milik spec (seed lewat Fixture BE di hook `before`, dihapus atau dipulihkan hook `after`; setiap nama bersuffix `{runId}-093`; Pohon Uji Utama dan Pre-setup #19 tidak diubah):
  - TC-AC-SG-349: `Region A Asal {runId}-093` dengan 4 anggota Distributor Active (`Distributor Alpha {runId}-093`, `Distributor Beta {runId}-093`, `Distributor Delta {runId}-093`, `Distributor Gamma {runId}-093`) dan `Region C Tujuan {runId}-093` dengan 1 anggota (`Distributor Sigma {runId}-093`), meniru Total Member `Region A` 4 dan `Region C` 1 pada Pre-setup #19.
  - TC-AC-SG-353: `Region B Pengguna {runId}-093` (level 1, tanpa penugasan; Total User awal 2 dari Total Control `Budi Santoso` dan Read Only `Rina Wijaya`). User `Yoga Pratama` (Pre-setup #18) dengan role Group Role `Manage allocation`.
  - TC-AC-SG-354: user `Read Only Baru {runId}-093` tanpa role.
- Data yang dibuat langkah spec: `Distributor Baru {runId}-093` (TC-AC-SG-350; pembersihan entitas hasil Create Distributor disediakan tim FE/BE di hook `after`).
- Baseline Changelog Group (audit trail permanen): jumlah total entri dicatat sebelum aksi pada TC-AC-SG-349 (kemampuan baca jumlah entri disediakan tim FE/BE).
- Kemampuan teknis: Fixture BE (seeding group, anggota, user, penugasan; pemulihan; disediakan tim FE/BE). Hook `after` mengembalikan sesi ke akun aktor pertama.
- Ukuran halaman tabel All Groups: default 10 baris per halaman; jumlah group pada tree Principal (Pohon Uji Utama ditambah tiga group milik spec) lebih dari 10 dan tidak lebih dari 20, sehingga seluruh baris diamati pada halaman 1 dan halaman 2 dengan pindah halaman eksplisit (S-14).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SG-349: Reassign entitas dari modul entitas mengubah Total Member node lama dan baru

1. Catat Total Member `Region A Asal {runId}-093` (4) dan `Region C Tujuan {runId}-093` (1) pada tabel All Groups
2. Klik ikon Changelog pada toolbar
3. Catat jumlah total entri Modal "Changelog: Group" sebagai baseline BC
4. Tutup Modal Changelog dengan `✕`
5. Buka Distributor > Edit `Distributor Alpha {runId}-093`
6. Ubah Group menjadi `Region C Tujuan {runId}-093` lalu klik `[Save]`
7. Tunggu aksi selesai (dialog/popup tertutup)
8. Buka halaman Settings > Group lewat sidebar
9. Verifikasi Total Member `Region A Asal {runId}-093` menjadi 3
10. Verifikasi Total Member `Region C Tujuan {runId}-093` menjadi 2
11. Klik ikon Changelog pada toolbar
12. Verifikasi jumlah total entri Modal "Changelog: Group" sama dengan BC (tidak ada entri Changelog Group tambahan di modul ini)
13. Tutup Modal Changelog dengan `✕`

### TC-AC-SG-353: Total User terefleksi setelah penugasan Group Role dari Settings > User

14. Catat Total User `Region B Pengguna {runId}-093` (2) pada tabel All Groups
15. Buka Settings > User > Detail `Yoga Pratama` > Tab Role > Sub-tab Group Role
16. Klik `[Assign Group]` pada baris role `Manage allocation`
17. Klik `[+ Assign Group]`
18. Centang `Region B Pengguna {runId}-093` pada Popup Select Group lalu klik `[Select]`
19. Klik `[Save]`
20. Tunggu aksi selesai (dialog/popup tertutup)
21. Buka halaman Settings > Group lewat sidebar
22. Verifikasi Total User `Region B Pengguna {runId}-093` menjadi 3
23. Klik angka Total User baris `Region B Pengguna {runId}-093` untuk membuka popup Users
24. Verifikasi popup Users memuat `Yoga Pratama`
25. Tutup popup Users dengan `✕`

### TC-AC-SG-354: Total Control atau Read Only baru otomatis menambah Total User di semua node

26. Catat Total User setiap baris halaman 1 tabel All Groups
27. Pindah ke halaman 2 pada Pagination
28. Catat Total User setiap baris halaman 2 tabel All Groups
29. Buka Settings > Role & Permission
30. Tetapkan user `Read Only Baru {runId}-093` sebagai Read Only
31. Tunggu aksi selesai (dialog/popup tertutup)
32. Buka halaman Settings > Group lewat sidebar
33. Verifikasi tabel All Groups memuat sedikitnya satu baris
34. Verifikasi Total User setiap baris halaman 1 tabel All Groups bertambah 1 dari nilai yang dicatat pada langkah 26
35. Pindah ke halaman 2 pada Pagination
36. Verifikasi Total User setiap baris halaman 2 tabel All Groups bertambah 1 dari nilai yang dicatat pada langkah 28

### TC-AC-SG-350: Create Distributor otomatis menyiapkan root All Groups dan Default Group

37. Buat Distributor baru `Distributor Baru {runId}-093` melalui form Create Distributor
38. Tunggu aksi selesai (dialog/popup tertutup)
39. Ganti akun: Logout, lalu login sebagai Total Control `Distributor Baru {runId}-093`
40. Buka halaman Settings > Group lewat sidebar
41. Verifikasi Sidebar Group Tree menampilkan `All Groups (1)` dengan satu group `Default Group`
42. Verifikasi tabel menampilkan 1 baris

## Notes

- Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 7, 20, 31, dan 38 (`Tunggu aksi selesai (dialog/popup tertutup)`, bagian 8b butir 8) menunggu aksi `[Save]`, penetapan Read Only, atau Create Distributor selesai sebelum surface atau akun berganti; mencatat nilai dan baseline (langkah 1 sampai 4, 14, 26, dan 28), pindah halaman tabel All Groups (langkah 27 dan 35), menutup Modal Changelog dan popup Users dengan `✕`, serta membuka kembali Settings > Group lewat sidebar.
- Langkah 39 adalah ganti akun eksplisit (S-07).
- Spec ini 42 langkah, di atas smell sekitar 35 langkah. Alasan: satu topik (sinkron lintas modul terhadap Settings > Group) pada satu aktor dan satu harness (fungsional lintas modul di backend nyata); empat blok TC memakai data milik spec sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain, dan setiap blok membuka surface berbeda sehingga langkah navigasi tidak dapat digabung. Empat langkah tunggu (langkah 7, 20, 31, dan 38) dan empat langkah catat atau pindah halaman tabel All Groups (langkah 26 sampai 28, 35) termasuk dalam hitungan.
- TC-AC-SG-349 dan TC-AC-SG-353 memakai node milik spec dengan jumlah anggota dan user yang meniru Pre-setup #19 dan #17 (S-06); pemulihan antar TC dilakukan hook `after` lewat Fixture BE.
- TC-AC-SG-350 ditaruh paling akhir karena berpindah akun (S-07, S-10); sesi dipulihkan ke akun aktor pertama di hook `after`.
- Temuan untuk QA:
  - TC-AC-SG-349 Expected "tidak ada entri Changelog Group tambahan di modul ini" tidak punya langkah observasi baseline; spec mencatat jumlah total entri sebelum Edit sebagai baseline.
  - TC-AC-SG-354 menyebut "Total User semua node" dan "assign satu user baru sebagai Read Only" tanpa nama user, ukuran halaman tabel, dan jalur assign di Role & Permission; spec memakai user seed `Read Only Baru {runId}-093` dan membaca seluruh halaman tabel.
  - TC-AC-SG-350 tidak menyebut field wajib form Create Distributor dan tidak menyebut akun Total Control Distributor baru; akun disediakan tim FE.
