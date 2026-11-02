---
id: TC-FA-GRP-E2E-203-node-excess-di-dropdown-konsumen-import-ditolak-dan-transaksi-berjalan-tetap-selesai
title: "Node Excess di Modul Konsumen: Tampil Tidak Dapat Dipilih, Tetap Dapat Dipilih di Scope Role/Lisensi/Reader/Home Group, Import Parent Excess Ditolak, dan Transaksi Berjalan Tetap Selesai"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-902
  - TC-FA-GRP-903
  - TC-FA-GRP-992
  - TC-FA-GRP-993
  - TC-FA-GRP-994
coverage:
  web: automated
---

# Node Excess di Modul Konsumen: Tampil Tidak Dapat Dipilih, Tetap Dapat Dipilih di Scope Role/Lisensi/Reader/Home Group, Import Parent Excess Ditolak, dan Transaksi Berjalan Tetap Selesai

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Akun importer: user ber-Global Role Import Data, `Fixture.groupsLog.importer.email`, password `Spectra.env.FA_GRP_IMPORTER_PASSWORD` (env baru; didaftarkan di tempat yang sama dengan `FA_TC_PASSWORD`); akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Kelas h (status Excess): kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): membuat node berstatus Excess lewat hook uji T-0 atau fixture BE. State global yang diubah spec: status Excess node milik spec dan Function node milik spec; dipulihkan dan dihapus di hook `after`.
- Data Pre-setup (dibaca, tidak diubah): Warehouse B (Assignable, Excess, Pre-setup No 9); Sold Yard (Disposal Group, Excess) tidak tertulis di Tabel Pre-setup dan disediakan tim FE (lihat Temuan untuk QA).
- Data Dinamis (Pre-setup tambahan, di-seed lewat API di hook `before`, nama bersuffix `{runId}-203`): `Old Assign {runId}-203` (Function diubah Assignable ke None, berisi aset Available); `Dest Assign {runId}-203` (Assignable) sebagai tujuan Transfer berstatus Waiting for Departure dan `Dest Disposal {runId}-203` (Disposal Group) sebagai tujuan Disposal Batch berstatus In Disposal Process; berkas import Group `Fixture.groupsImport.parentExcess` dengan baris Parent = Warehouse B. Fixture milik spec dipakai sebagai pengganti Warehouse A dan Disposal Yard pada TC-994 agar data Pre-setup bersama tidak diubah (S-06).
- Password user subjek yang di-seed: `Spectra.env.FA_GRP_SUBJECT_PASSWORD` (env baru).

## Test Steps

1. Catat jumlah aset di Warehouse B

### TC-902: Node Excess tampil tetapi tidak dapat dipilih

2. Buka field Group Register Asset dan field tujuan Transfer
3. Verifikasi Warehouse B (Assignable) tetap tampil tetapi tidak dapat dipilih
4. Verifikasi Sold Yard tidak tampil
5. Buka dropdown tujuan Disposal
6. Verifikasi Sold Yard (Disposal Group) tetap tampil tetapi tidak dapat dipilih
7. Verifikasi Warehouse B tidak tampil
8. Buka Fixed Asset > Settings > Groups
9. Buka Detail Warehouse B (Tab Assets)
10. Verifikasi aset existing di Warehouse B tetap ada (jumlah sama dengan yang dicatat)

### TC-903: Aset di node non-Assignable tetap bisa ditransaksikan keluar

11. Buat Transfer keluar aset dari `Old Assign {runId}-203`
12. Verifikasi aset eligible sesuai syarat "Available dalam kuasa group asal user"
13. Buat Disposal aset dari `Old Assign {runId}-203`
14. Verifikasi aset eligible sesuai syarat "Custody=Available, Lifecycle=Active"
15. Buat Assignment aset dari `Old Assign {runId}-203`
16. Verifikasi aset eligible sesuai syarat "status Available + Normal + group user"
17. Verifikasi Function node asal (None) tidak memengaruhi eligibility pada ketiga transaksi

### TC-992: Node Excess tetap dapat dipilih di scope Role & Permission, lisensi, Reader Group, dan Home Group

18. Buka Settings > Role & Permission, assign Group Role: buka pilihan group
19. Verifikasi Warehouse B tersedia dan dapat dipilih di pilihan scope Role & Permission
20. Buka License Allocation per Group
21. Verifikasi Warehouse B tersedia dan dapat dipilih di License Allocation per Group
22. Buka Reader Group (Smart Fixed Reader dan Asset Control Station)
23. Verifikasi Warehouse B tersedia dan dapat dipilih di Reader Group
24. Buka Home Group user
25. Verifikasi Warehouse B tersedia dan dapat dipilih di Home Group user
26. Buka Fixed Asset > Settings > Groups, buka elipsis Warehouse B
27. Verifikasi menu elipsis Warehouse B terbuka dan memuat sedikitnya satu item menu lain (anchor)
28. Verifikasi Edit dan Add Subgroup Hidden pada Warehouse B
29. Verifikasi pada pilihan tujuan aset baru Warehouse B tidak dapat dipilih (Assignable pada Register Asset dan Transfer) dan Sold Yard tidak dapat dipilih (Disposal Group pada Disposal), keduanya tetap tampil

### TC-994: Transaksi berjalan tetap selesai

30. Buka Fixed Asset > Settings > Groups
31. Ubah Function `Dest Assign {runId}-203` menjadi None, klik [Save] dan [Save] pada Dialog Change Function
32. Tunggu aksi selesai
33. Jadikan `Dest Disposal {runId}-203` berstatus Excess lewat hook uji T-0 atau fixture BE
34. Tunggu aksi selesai
35. Selesaikan Transfer sampai Arrival
36. Verifikasi Transfer selesai: Group aset berpindah ke `Dest Assign {runId}-203` saat Transfer Arrival
37. Selesaikan Disposal Batch (Complete)
38. Verifikasi Disposal Batch Complete berhasil
39. Buat Transfer dan Disposal baru, buka pilihan tujuan
40. Verifikasi sedikitnya satu opsi tujuan Transfer lain tampil (anchor)
41. Verifikasi `Dest Assign {runId}-203` (Function None) tidak tersedia sebagai tujuan Transfer baru
42. Verifikasi `Dest Disposal {runId}-203` (Excess) tidak dapat dipilih sebagai tujuan Disposal baru

### TC-993: Import dengan parent berstatus Excess ditolak (akun importer)

43. Buka Fixed Asset > Settings > Groups
44. Catat jumlah baris Changelog Group yang memuat Warehouse B
45. Ganti akun: Logout, lalu login sebagai importer
46. Buka modul Import, unggah berkas Group `Fixture.groupsImport.parentExcess`
47. Jalankan import
48. Buka Fixed Asset > Settings > Groups
49. Verifikasi baris dengan parent Warehouse B ditolak karena parent berstatus Excess (terkunci)
50. Verifikasi tidak ada group baru di bawah Warehouse B
51. Buka Modal Changelog: Group
52. Filter Changelog dengan Group Name Warehouse B
53. Verifikasi jumlah baris Changelog Warehouse B sama dengan baseline (tidak ada baris Create baru dari Import)
54. Tutup Modal Changelog

## Notes

- Urutan di dalam spec: TC-902, 903, 992, 994 sebagai Total Control, lalu TC-993 sebagai importer (ganti akun eksplisit); TC-993 ditaruh paling akhir untuk satu kali Ganti akun (S-10). Akun aktor pertama login di hook `before`; hook `after` memulihkan sesi ke akun default.
- Langkah penghubung (S-03): mencatat jumlah aset dan baseline Changelog, Tunggu aksi selesai, dan menutup Modal Changelog. Langkah "Buka Fixed Asset > Settings > Groups" ditulis di awal tiap blok yang aksinya di Groups (sebelum Detail Warehouse B, sebelum ubah Function `Dest Assign`, dan sebelum baseline Changelog) karena blok sebelumnya berakhir di modul konsumen (S-14). Asersi tambahan (S-03, 8b butir 2): Verifikasi sedikitnya satu item menu elipsis lain sebelum asersi Edit dan Add Subgroup Hidden, dan Verifikasi sedikitnya satu opsi tujuan Transfer lain tampil sebelum asersi `Dest Assign` tidak tersedia, sebagai anchor positif absence.
- Spec memiliki 54 langkah, di atas smell 35 langkah. Alasan: lima TC kelas sama (perilaku node Excess pada modul konsumen) dengan fixture bersama; tiap TC berdiri sendiri, dan TC-903, 992, dan 994 melintasi modul Transfer, Disposal, Assignment, Role & Permission, License, dan Reader.
- Temuan untuk QA:
  - Sold Yard (Disposal Group, Excess), Old Assign, dan akun importer tidak tertulis di Tabel Pre-setup; ditulis sebagai data atau akun yang disediakan tim FE (S-11). TC-994 menyebut Warehouse A dan Disposal Yard dari Pre-setup; spec memakai fixture milik spec (`Dest Assign`, `Dest Disposal`) agar Pre-setup bersama tidak diubah.
  - TC-903 dan 994 tidak menyebut langkah rinci membuat Transfer, Disposal, dan Assignment; spec mengikuti teks TC dan hanya memverifikasi Expected. TC-992 Expected b memuat dua klausa (kunci Edit/Add Subgroup dan gating tujuan aset baru); spec memverifikasinya terpisah.
  - TC-993 menyebut pesan penolakan hanya sebagai "ditolak karena parent Excess"; teks pesan tidak ada di TC.
  - TC-992 Expected b tidak menyebut item menu elipsis lain pada Warehouse B (Excess); anchor absence memakai "sedikitnya satu item menu lain" tanpa menyebut nama item. TC-994 tidak menyebut cara tujuan Transfer baru dibandingkan; anchor memakai "sedikitnya satu opsi tujuan lain".
