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
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Changelog Group sebelum aksi (baseline, 8b butir 10).
- Password user subjek yang di-seed: `Spectra.env.FA_GRP_SUBJECT_PASSWORD` (env baru).

## Test Steps

### TC-902: Node Excess tampil tetapi tidak dapat dipilih

1. Buka Fixed Asset > Register Asset
2. Buka field Group Register Asset
3. Verifikasi Warehouse B (Assignable) tetap tampil tetapi tidak dapat dipilih di field Group Register Asset
4. Verifikasi Sold Yard tidak tampil di field Group Register Asset
5. Buka Fixed Asset > Transfer
6. Buka field tujuan Transfer
7. Verifikasi Warehouse B (Assignable) tetap tampil tetapi tidak dapat dipilih di field tujuan Transfer
8. Verifikasi Sold Yard tidak tampil di field tujuan Transfer
9. Buka Fixed Asset > Disposal
10. Buka dropdown tujuan Disposal
11. Verifikasi Sold Yard (Disposal Group) tetap tampil tetapi tidak dapat dipilih
12. Verifikasi Warehouse B tidak tampil
13. Buka Fixed Asset > Settings > Groups
14. Ketik Search `Warehouse B`, tekan Enter
15. Buka Detail Warehouse B (Tab Assets)
16. Catat jumlah aset di Warehouse B sebagai baseline
17. Verifikasi aset existing di Warehouse B tetap ada (jumlah sama dengan yang dicatat)

### TC-903: Aset di node non-Assignable tetap bisa ditransaksikan keluar

18. Buat Transfer keluar aset dari `Old Assign {runId}-203`
19. Verifikasi aset eligible sesuai syarat "Available dalam kuasa group asal user"
20. Buat Disposal aset dari `Old Assign {runId}-203`
21. Verifikasi aset eligible sesuai syarat "Custody=Available, Lifecycle=Active"
22. Buat Assignment aset dari `Old Assign {runId}-203`
23. Verifikasi aset eligible sesuai syarat "status Available + Normal + group user"
24. Verifikasi Function node asal (None) tidak memengaruhi eligibility pada ketiga transaksi

### TC-992: Node Excess tetap dapat dipilih di scope Role & Permission, lisensi, Reader Group, dan Home Group

25. Buka Settings > Role & Permission, assign Group Role: buka pilihan group
26. Verifikasi Warehouse B tersedia dan dapat dipilih di pilihan scope Role & Permission
27. Buka License Allocation per Group
28. Verifikasi Warehouse B tersedia dan dapat dipilih di License Allocation per Group
29. Buka Reader Group (Smart Fixed Reader dan Asset Control Station)
30. Verifikasi Warehouse B tersedia dan dapat dipilih di Reader Group
31. Buka Home Group user
32. Verifikasi Warehouse B tersedia dan dapat dipilih di Home Group user
33. Buka Fixed Asset > Settings > Groups
34. Ketik Search `Warehouse B`, tekan Enter
35. Buka elipsis Warehouse B
36. Verifikasi menu elipsis Warehouse B terbuka dan memuat sedikitnya satu item menu lain (anchor)
37. Verifikasi Edit dan Add Subgroup Hidden pada Warehouse B
38. Buka Fixed Asset > Register Asset
39. Buka field Group Register Asset
40. Verifikasi sedikitnya satu opsi group lain tampil di field Group Register Asset (anchor)
41. Verifikasi Warehouse B tetap tampil di field Group Register Asset
42. Verifikasi Warehouse B tidak dapat dipilih di field Group Register Asset
43. Buka Fixed Asset > Transfer
44. Buka field tujuan Transfer
45. Verifikasi sedikitnya satu opsi group lain tampil di field tujuan Transfer (anchor)
46. Verifikasi Warehouse B tetap tampil di field tujuan Transfer
47. Verifikasi Warehouse B tidak dapat dipilih di field tujuan Transfer
48. Buka Fixed Asset > Disposal
49. Buka dropdown tujuan Disposal
50. Verifikasi sedikitnya satu opsi group lain tampil di dropdown tujuan Disposal (anchor)
51. Verifikasi Sold Yard tetap tampil di dropdown tujuan Disposal
52. Verifikasi Sold Yard tidak dapat dipilih di dropdown tujuan Disposal

### TC-994: Transaksi berjalan tetap selesai

53. Buka Fixed Asset > Settings > Groups
54. Ketik Search `Dest Assign {runId}-203`, tekan Enter
55. Ubah Function `Dest Assign {runId}-203` menjadi None, klik [Save] dan [Save] pada Dialog Change Function
56. Tunggu aksi selesai
57. Jadikan `Dest Disposal {runId}-203` berstatus Excess lewat hook uji T-0 atau fixture BE
58. Tunggu aksi selesai
59. Selesaikan Transfer sampai Arrival
60. Verifikasi Transfer selesai: Group aset berpindah ke `Dest Assign {runId}-203` saat Transfer Arrival
61. Selesaikan Disposal Batch (Complete)
62. Verifikasi Disposal Batch Complete berhasil
63. Buat Transfer dan Disposal baru, buka pilihan tujuan
64. Verifikasi sedikitnya satu opsi tujuan Transfer lain tampil (anchor)
65. Verifikasi `Dest Assign {runId}-203` (Function None) tidak tersedia sebagai tujuan Transfer baru
66. Verifikasi `Dest Disposal {runId}-203` (Excess) tidak dapat dipilih sebagai tujuan Disposal baru

### TC-993: Import dengan parent berstatus Excess ditolak (akun importer)

67. Buka Fixed Asset > Settings > Groups
68. Catat jumlah baris Changelog Group yang memuat Warehouse B
69. Ganti akun: Logout, lalu login sebagai importer
70. Buka modul Import, unggah berkas Group `Fixture.groupsImport.parentExcess`
71. Jalankan import
72. Buka Fixed Asset > Settings > Groups
73. Ketik Search `Warehouse B`, tekan Enter
74. Verifikasi baris dengan parent Warehouse B ditolak karena parent berstatus Excess (terkunci)
75. Klik `(←)` pada kotak Search
76. Klik `Warehouse B` di sidebar
77. Verifikasi Groups List tampil
78. Verifikasi tidak ada group baru di bawah Warehouse B
79. Buka Modal Changelog: Group
80. Filter Changelog dengan Group Name Warehouse B
81. Verifikasi jumlah baris Changelog Warehouse B sama dengan baseline (tidak ada baris Create baru dari Import)
82. Tutup Modal Changelog

## Notes

- Urutan di dalam spec: TC-902, 903, 992, 994 sebagai Total Control, lalu TC-993 sebagai importer (ganti akun eksplisit); TC-993 ditaruh paling akhir untuk satu kali Ganti akun (S-10). Akun aktor pertama login di hook `before`; hook `after` memulihkan sesi ke akun default.
- Langkah penghubung (S-03): mencatat jumlah aset (langkah 16, baseline dicatat tepat sesudah Detail Warehouse B dibuka lewat Search `Warehouse B` pada langkah 14, sebelum aksi lain; dibandingkan pada langkah 17) dan baseline Changelog, Tunggu aksi selesai, dan menutup Modal Changelog. Navigasi ke modul konsumen (S-14): Buka Fixed Asset > Register Asset, > Transfer, dan > Disposal ditulis sebelum membuka field atau dropdown; asersi TC-992 Expected b klausa gating dipecah satu Verifikasi per klausa dengan anchor positif sebelum asersi tidak dapat dipilih (S-01, 8b butir 2). Langkah "Buka Fixed Asset > Settings > Groups" ditulis di awal tiap blok yang aksinya di Groups (sebelum Detail Warehouse B, sebelum ubah Function `Dest Assign`, dan sebelum baseline Changelog) karena blok sebelumnya berakhir di modul konsumen (S-14). Asersi tambahan (S-03, 8b butir 2): Verifikasi sedikitnya satu item menu elipsis lain sebelum asersi Edit dan Add Subgroup Hidden, dan Verifikasi sedikitnya satu opsi tujuan Transfer lain tampil sebelum asersi `Dest Assign` tidak tersedia, sebagai anchor positif absence.
- Spec memiliki 82 langkah, di atas smell 35 langkah. Alasan: lima TC kelas sama (perilaku node Excess pada modul konsumen) dengan fixture bersama; tiap TC berdiri sendiri, dan TC-903, 992, dan 994 melintasi modul Transfer, Disposal, Assignment, Role & Permission, License, dan Reader.
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Langkah penghubung (S-03, S-14, 8b butir 2): langkah 75 (Klik `(←)` pada kotak Search) mengosongkan Search `Warehouse B` dari langkah 73 supaya anak Warehouse B yang namanya tidak memuat "Warehouse B" tidak tersaring (S-03), langkah 76 memilih node `Warehouse B` di sidebar supaya anak Warehouse B dapat diamati, dan langkah 77 (Verifikasi Groups List tampil) menjadi anchor positif sebelum asersi tidak ada group baru di bawah Warehouse B.
- Temuan untuk QA:
  - Sold Yard (Disposal Group, Excess), Old Assign, dan akun importer tidak tertulis di Tabel Pre-setup; ditulis sebagai data atau akun yang disediakan tim FE (S-11). TC-994 menyebut Warehouse A dan Disposal Yard dari Pre-setup; spec memakai fixture milik spec (`Dest Assign`, `Dest Disposal`) agar Pre-setup bersama tidak diubah.
  - TC-903 dan 994 tidak menyebut langkah rinci membuat Transfer, Disposal, dan Assignment; spec mengikuti teks TC dan hanya memverifikasi Expected. TC-992 Expected b memuat dua klausa (kunci Edit/Add Subgroup dan gating tujuan aset baru); spec memverifikasinya terpisah.
  - TC-993: daftar anak Warehouse B yang sudah ada tidak tertulis di Pre-setup, sehingga pembanding "sedikitnya satu baris anak" tidak dapat dijamin; anchor memakai Groups List tampil.
  - TC-993 menyebut pesan penolakan hanya sebagai "ditolak karena parent Excess"; teks pesan tidak ada di TC.
  - TC-992 Expected b tidak menyebut item menu elipsis lain pada Warehouse B (Excess); anchor absence memakai "sedikitnya satu item menu lain" tanpa menyebut nama item. TC-994 tidak menyebut cara tujuan Transfer baru dibandingkan; anchor memakai "sedikitnya satu opsi tujuan lain".
