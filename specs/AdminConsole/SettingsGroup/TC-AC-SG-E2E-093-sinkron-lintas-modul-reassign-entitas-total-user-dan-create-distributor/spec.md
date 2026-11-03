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
- Akun kedua (ganti akun di langkah 47): Total Control `Distributor Baru {runId}-093` yang dibuat langkah 45. Email dan password akun ini tidak tertulis di Pre-setup TC; disediakan tim FE (lihat Temuan untuk QA).
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Akses akun aktor ke modul Distributor (Edit), Settings > User (Detail user > Tab Role), Settings > Role & Permission, Activity Log, dan form Create Distributor tersedia (Pre-setup #40).
- Data milik spec (seed lewat Fixture BE di hook `before`, dihapus atau dipulihkan hook `after`; setiap nama bersuffix `{runId}-093`; Pohon Uji Utama dan Pre-setup #19 tidak diubah):
  - TC-AC-SG-349: `Region A Asal {runId}-093` dengan 4 anggota Distributor Active (`Distributor Alpha {runId}-093`, `Distributor Beta {runId}-093`, `Distributor Delta {runId}-093`, `Distributor Gamma {runId}-093`) dan `Region C Tujuan {runId}-093` dengan 1 anggota (`Distributor Sigma {runId}-093`), meniru Total Member `Region A` 4 dan `Region C` 1 pada Pre-setup #19.
  - TC-AC-SG-353: `Region B Pengguna {runId}-093` (level 1, tanpa penugasan; Total User awal 2 dari Total Control `Budi Santoso` dan Read Only `Rina Wijaya`). User `Yoga Pratama` (Pre-setup #18) dengan role Group Role `Manage allocation`.
  - TC-AC-SG-354: user `Read Only Baru {runId}-093` tanpa role.
- Data yang dibuat langkah spec: `Distributor Baru {runId}-093` (TC-AC-SG-350; pembersihan entitas hasil Create Distributor disediakan tim FE/BE di hook `after`).
- Baseline Changelog Group (audit trail permanen): jumlah total entri dicatat sebelum aksi pada TC-AC-SG-349 (kemampuan baca jumlah entri disediakan tim FE/BE).
- Kemampuan teknis: Fixture BE (seeding group, anggota, user, penugasan; pemulihan; disediakan tim FE/BE). Hook `after` mengembalikan sesi ke akun aktor pertama.
- Ukuran halaman tabel All Groups: default 10 baris per halaman; jumlah group pada tree Principal (Pohon Uji Utama ditambah tiga group milik spec) lebih dari 10 dan tidak lebih dari 20, sehingga TC-AC-SG-354 mengamati seluruh baris pada halaman 1 dan halaman 2 dengan pindah halaman eksplisit, dan baris target TC lain dicari lewat Search `{runId}-093` (S-14).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SG-349: Reassign entitas dari modul entitas mengubah Total Member node lama dan baru

1. Ketik Search `{runId}-093` pada toolbar tabel utama, tekan Enter
2. Catat Total Member `Region A Asal {runId}-093` (4) dan `Region C Tujuan {runId}-093` (1) pada tabel All Groups
3. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel
4. Klik ikon Changelog pada toolbar
5. Catat jumlah total entri Modal "Changelog: Group" sebagai baseline BC
6. Tutup Modal Changelog dengan `✕`
7. Buka Distributor > Edit `Distributor Alpha {runId}-093`
8. Ubah Group menjadi `Region C Tujuan {runId}-093` lalu klik `[Save]`
9. Tunggu aksi selesai (dialog/popup tertutup)
10. Buka halaman Settings > Group lewat sidebar
11. Ketik Search `{runId}-093` pada toolbar tabel utama, tekan Enter
12. Verifikasi Total Member `Region A Asal {runId}-093` menjadi 3
13. Verifikasi Total Member `Region C Tujuan {runId}-093` menjadi 2
14. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel
15. Klik ikon Changelog pada toolbar
16. Verifikasi jumlah total entri Modal "Changelog: Group" sama dengan BC (tidak ada entri Changelog Group tambahan di modul ini)
17. Tutup Modal Changelog dengan `✕`

### TC-AC-SG-353: Total User terefleksi setelah penugasan Group Role dari Settings > User

18. Ketik Search `{runId}-093` pada toolbar tabel utama, tekan Enter
19. Catat Total User `Region B Pengguna {runId}-093` (2) pada tabel All Groups
20. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel
21. Buka Settings > User > Detail `Yoga Pratama` > Tab Role > Sub-tab Group Role
22. Klik `[Assign Group]` pada baris role `Manage allocation`
23. Klik `[+ Assign Group]`
24. Centang `Region B Pengguna {runId}-093` pada Popup Select Group lalu klik `[Select]`
25. Klik `[Save]`
26. Tunggu aksi selesai (dialog/popup tertutup)
27. Buka halaman Settings > Group lewat sidebar
28. Ketik Search `{runId}-093` pada toolbar tabel utama, tekan Enter
29. Verifikasi Total User `Region B Pengguna {runId}-093` menjadi 3
30. Klik angka Total User baris `Region B Pengguna {runId}-093` untuk membuka popup Users
31. Verifikasi popup Users memuat `Yoga Pratama`
32. Tutup popup Users dengan `✕`
33. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel

### TC-AC-SG-354: Total Control atau Read Only baru otomatis menambah Total User di semua node

34. Catat Total User setiap baris halaman 1 tabel All Groups
35. Pindah ke halaman 2 pada Pagination
36. Catat Total User setiap baris halaman 2 tabel All Groups
37. Buka Settings > Role & Permission
38. Tetapkan user `Read Only Baru {runId}-093` sebagai Read Only
39. Tunggu aksi selesai (dialog/popup tertutup)
40. Buka halaman Settings > Group lewat sidebar
41. Verifikasi tabel All Groups memuat sedikitnya satu baris
42. Verifikasi Total User setiap baris halaman 1 tabel All Groups bertambah 1 dari nilai yang dicatat pada langkah 34
43. Pindah ke halaman 2 pada Pagination
44. Verifikasi Total User setiap baris halaman 2 tabel All Groups bertambah 1 dari nilai yang dicatat pada langkah 36

### TC-AC-SG-350: Create Distributor otomatis menyiapkan root All Groups dan Default Group

45. Buat Distributor baru `Distributor Baru {runId}-093` melalui form Create Distributor
46. Tunggu aksi selesai (dialog/popup tertutup)
47. Ganti akun: Logout, lalu login sebagai Total Control `Distributor Baru {runId}-093`
48. Buka halaman Settings > Group lewat sidebar
49. Verifikasi Sidebar Group Tree menampilkan `All Groups (1)` dengan satu group `Default Group`
50. Verifikasi tabel menampilkan 1 baris

## Notes

- Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 9, 26, 39, dan 46 (`Tunggu aksi selesai (dialog/popup tertutup)`, bagian 8b butir 8) menunggu aksi `[Save]`, penetapan Read Only, atau Create Distributor selesai sebelum surface atau akun berganti; mencatat nilai dan baseline (langkah 2 sampai 6, 19, 34, dan 36), pindah halaman tabel All Groups (langkah 35 dan 43), menutup Modal Changelog dan popup Users dengan `✕`, serta membuka kembali Settings > Group lewat sidebar.
- Langkah penghubung (S-03, S-14): langkah 1, 11, 18, dan 28 (Search `{runId}-093` agar baris `Region A Asal`, `Region B Pengguna`, dan `Region C Tujuan` terbaca; tree Principal lebih dari 10 group sehingga baris target tidak dijamin di halaman 1) dan langkah 3, 14, 20, serta 33 (klik `(←)` untuk menutup input dan mereset tabel).
- Langkah 47 adalah ganti akun eksplisit (S-07).
- Spec ini 50 langkah, di atas smell sekitar 35 langkah. Alasan: satu topik (sinkron lintas modul terhadap Settings > Group) pada satu aktor dan satu harness (fungsional lintas modul di backend nyata); empat blok TC memakai data milik spec sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain, dan setiap blok membuka surface berbeda sehingga langkah navigasi tidak dapat digabung. Empat langkah tunggu (langkah 9, 26, 39, dan 46) dan empat langkah catat atau pindah halaman tabel All Groups (langkah 34 sampai 36, 43) termasuk dalam hitungan.
- TC-AC-SG-349 dan TC-AC-SG-353 memakai node milik spec dengan jumlah anggota dan user yang meniru Pre-setup #19 dan #17 (S-06); pemulihan antar TC dilakukan hook `after` lewat Fixture BE.
- TC-AC-SG-350 ditaruh paling akhir karena berpindah akun (S-07, S-10); sesi dipulihkan ke akun aktor pertama di hook `after`.
- Temuan untuk QA:
  - TC-AC-SG-349 Expected "tidak ada entri Changelog Group tambahan di modul ini" tidak punya langkah observasi baseline; spec mencatat jumlah total entri sebelum Edit sebagai baseline.
  - TC-AC-SG-354 menyebut "Total User semua node" dan "assign satu user baru sebagai Read Only" tanpa nama user, ukuran halaman tabel, dan jalur assign di Role & Permission; spec memakai user seed `Read Only Baru {runId}-093` dan membaca seluruh halaman tabel.
  - TC-AC-SG-350 tidak menyebut field wajib form Create Distributor dan tidak menyebut akun Total Control Distributor baru; akun disediakan tim FE.
