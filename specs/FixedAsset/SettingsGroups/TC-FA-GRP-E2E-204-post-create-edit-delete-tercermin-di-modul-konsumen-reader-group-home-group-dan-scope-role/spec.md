---
id: TC-FA-GRP-E2E-204-post-create-edit-delete-tercermin-di-modul-konsumen-reader-group-home-group-dan-scope-role
title: "Post-Create/Edit/Delete Tercermin di Modul Konsumen: Dropdown, Reader Group, Home Group/Lisensi, Aset Disposed/Deleted, dan Scope Role & Permission"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-904
  - TC-FA-GRP-905
  - TC-FA-GRP-906
  - TC-FA-GRP-907
  - TC-FA-GRP-908
  - TC-FA-GRP-909
  - TC-FA-GRP-910
coverage:
  web: automated
---

# Post-Create/Edit/Delete Tercermin di Modul Konsumen: Dropdown, Reader Group, Home Group/Lisensi, Aset Disposed/Deleted, dan Scope Role & Permission

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Password user subjek yang di-seed: `Spectra.env.FA_GRP_SUBJECT_PASSWORD` (env baru).
- Data Dinamis (Pre-setup tambahan, di-seed lewat API di hook `before`, nama bersuffix `{runId}-204`, dibersihkan di hook `after`): `Sync Rename {runId}-204` (dipakai sebagai Reader Group dan scope role, dengan satu Transfer selesai ke group itu); `Sync Del {runId}-204` kosong beserta satu descendant kosong, tersedia di dropdown; `Del Reader {runId}-204` kosong aset, dengan Reader SFR-01 (Smart Fixed Reader) dan ACS-01 (Asset Control Station) Pre-setup No 11 dipindahkan ke Reader Group itu; `Del Home Lic {runId}-204` sebagai Home Group user E dengan alokasi kuota lisensi 5; `Del Disposed {runId}-204` dengan 2 aset Disposed dan 1 aset Deleted; `Del Scope {runId}-204` dengan user F ber-Group Role di group itu. Group `Sync New {runId}-204` dibuat oleh spec.
- Pemulihan Reader SFR-01 dan ACS-01 ke Reader Group semula dan alokasi lisensi (kuota Pre-setup tidak dapat dimiliki spec, S-06): dijamin fixture BE yang disediakan tim FE/BE di hook `before` dan `after`; efeknya (Reader Group dan kuota lisensi sementara berubah) dicatat di sini, dan suite berjalan serial.

## Test Steps

### TC-904: Post-Create node baru muncul di dropdown konsumen

1. Klik [+] Group
2. Isi Group Name `Sync New {runId}-204`, pilih Assignable, klik [Submit]
3. Verifikasi toast sukses "Success, group has been created."
4. Buka Fixed Asset > Register Asset
5. Buka field Group Register Asset
6. Verifikasi `Sync New {runId}-204` tersedia sebagai pilihan di Register Asset
7. Buka Home Group di Settings > User
8. Verifikasi `Sync New {runId}-204` tersedia sebagai pilihan Home Group
9. Buka Reader Group di GS Hardware
10. Verifikasi `Sync New {runId}-204` tersedia sebagai pilihan Reader Group
11. Buka scope Settings > Role & Permission
12. Verifikasi `Sync New {runId}-204` tersedia sebagai pilihan scope

### TC-905: Post-Edit rename tercermin live

13. Buka Fixed Asset > Settings > Groups
14. Ketik Search `Sync Rename {runId}-204`, tekan Enter
15. Rename `Sync Rename {runId}-204` menjadi `Sync Renamed {runId}-204`
16. Verifikasi toast sukses "Success, group has been updated."
17. Buka Settings > Role & Permission
18. Verifikasi `Sync Renamed {runId}-204` tampil di Role & Permission
19. Buka Asset list
20. Verifikasi `Sync Renamed {runId}-204` tampil di Asset list
21. Buka Transfer
22. Verifikasi `Sync Renamed {runId}-204` tampil di Transfer
23. Buka GS Hardware
24. Verifikasi `Sync Renamed {runId}-204` tampil di GS Hardware
25. Buka detail Transfer yang selesai ke group itu di modul Transfer
26. Verifikasi Transfer tersebut berstatus selesai
27. Verifikasi baris log historis pada log detail Transfer tersebut menampilkan nama lama `Sync Rename {runId}-204` pada kolom Note (snapshot), bukan `Sync Renamed {runId}-204`
28. Verifikasi baris log historis lain pada log detail Transfer tersebut juga tetap bernama lama `Sync Rename {runId}-204`

### TC-906: Post-Delete node hilang dari dropdown

29. Buka Fixed Asset > Register Asset
30. Buka field Group Register Asset
31. Verifikasi sedikitnya satu group lain tampil sebagai pilihan (anchor)
32. Tutup field Group
33. Buka Fixed Asset > Settings > Groups
34. Ketik Search `Sync Del {runId}-204`, tekan Enter
35. Buka elipsis `Sync Del {runId}-204`, pilih Delete, klik [Delete]
36. Verifikasi toast sukses "Success, group has been deleted."
37. Buka Fixed Asset > Register Asset
38. Buka dropdown Group di Register Asset
39. Verifikasi sedikitnya satu group lain tampil di Register Asset (anchor)
40. Verifikasi `Sync Del {runId}-204` dan descendant tidak lagi tersedia di Register Asset
41. Buka Fixed Asset > Transfer
42. Buka dropdown Group di Transfer
43. Verifikasi sedikitnya satu group lain tampil di Transfer (anchor)
44. Verifikasi `Sync Del {runId}-204` dan descendant tidak lagi tersedia di Transfer
45. Buka Fixed Asset > Disposal
46. Buka dropdown Group di Disposal
47. Verifikasi sedikitnya satu group lain tampil di Disposal (anchor)
48. Verifikasi `Sync Del {runId}-204` dan descendant tidak lagi tersedia di Disposal
49. Buka Settings > User
50. Buka dropdown Home Group
51. Verifikasi sedikitnya satu group lain tampil di Home Group di Settings > User (anchor)
52. Verifikasi `Sync Del {runId}-204` dan descendant tidak lagi tersedia di Home Group di Settings > User
53. Buka GS Hardware
54. Buka dropdown Reader Group
55. Verifikasi sedikitnya satu group lain tampil di Reader Group di GS Hardware (anchor)
56. Verifikasi `Sync Del {runId}-204` dan descendant tidak lagi tersedia di Reader Group di GS Hardware

### TC-907: Delete group Reader Group tidak diblok

57. Buka Fixed Asset > Settings > Groups
58. Ketik Search `Del Reader {runId}-204`, tekan Enter
59. Buka elipsis `Del Reader {runId}-204`, pilih Delete, klik [Delete]
60. Verifikasi toast sukses "Success, group has been deleted." (tanpa dialog blok)
61. Buka GS Hardware Smart Fixed Reader dan Asset Control Station
62. Verifikasi Reader Group SFR-01 dan ACS-01 kosong (orphan)

### TC-908: Delete Home Group user dan alokasi lisensi tidak diblok

63. Buka License > Allocation Quota
64. Catat kuota pool License > Allocation Quota sebelum Delete (baseline) dan alokasi `Del Home Lic {runId}-204` sebesar 5
65. Buka Fixed Asset > Settings > Groups
66. Ketik Search `Del Home Lic {runId}-204`, tekan Enter
67. Buka elipsis `Del Home Lic {runId}-204`, pilih Delete
68. Verifikasi dialog konfirmasi normal tampil
69. Klik [Delete]
70. Verifikasi toast sukses "Success, group has been deleted."
71. Buka Settings > User (user E)
72. Verifikasi Home Group user E kosong
73. Verifikasi constraint assignment Group Role dan Group Manager yang bersumber dari Home Group itu ikut lepas
74. Buka License > Allocation Quota
75. Verifikasi alokasi ikut terhapus
76. Verifikasi kuota pool License > Allocation Quota sama dengan baseline ditambah 5 (kuota kembali ke pool)

### TC-909: Delete group aset Disposed/Deleted

77. Buka Fixed Asset > Settings > Groups
78. Ketik Search `Del Disposed {runId}-204`, tekan Enter
79. Buka elipsis `Del Disposed {runId}-204`, pilih Delete, klik [Delete]
80. Verifikasi toast sukses "Success, group has been deleted."
81. Buka Asset list dengan filter Disposed
82. Verifikasi ketiga aset tetap ada dengan Group kosong
83. Buka Disposal Log
84. Verifikasi nama `Del Disposed {runId}-204` terbaca via snapshot

### TC-910: User kehilangan scope Role

85. Buka Fixed Asset > Settings > Groups
86. Ketik Search `Del Scope {runId}-204`, tekan Enter
87. Buka elipsis `Del Scope {runId}-204`, pilih Delete
88. Klik [Delete] pada dialog warning
89. Verifikasi toast sukses "Success, group has been deleted."
90. Buka Settings > Role & Permission user F
91. Verifikasi assignment user F di `Del Scope {runId}-204` hilang

## Notes

- Langkah penghubung (S-03): Tutup field Group, mencatat baseline kuota pool (TC-908), dan navigasi (S-14): "Buka Fixed Asset > Register Asset" sebelum dropdown Group Register Asset (TC-904 dan TC-906), navigasi ke tiap modul konsumen (Register Asset, Transfer, Disposal, Settings > User, GS Hardware) sebelum dropdown-nya dibuka sesudah Delete (TC-906), serta "Buka Fixed Asset > Settings > Groups" di awal tiap blok TC-905 sampai 910 karena blok sebelumnya berakhir di modul konsumen. Asersi tambahan (S-03, 8b butir 2): Verifikasi sedikitnya satu group lain tampil di tiap dropdown (satu per modul) sebelum asersi group terhapus tidak tersedia (TC-906), dan Verifikasi toast sukses Delete sebelum asersi assignment user F hilang (TC-910; menggantikan Tunggu aksi selesai karena hasil aksi kini diasersi). Urutan: aksi menghapus (TC-906 sampai 910) ditaruh sesudah TC-904 dan 905 karena menghapus data (S-10).
- Spec memiliki 91 langkah, di atas smell 35 langkah. Alasan: tujuh TC satu topik (propagasi perubahan group ke modul konsumen) dengan fixture terpisah per TC; tiap TC berdiri sendiri, dan banyak langkah berasal dari Expected yang memeriksa beberapa modul konsumen (S-01) dan dari navigasi per modul konsumen pada TC-906 (S-14).
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-904 sampai 910 menulis nama literal (`Sync New`, `Sync Del`, `Del Reader`, `Del Home Lic`, `Del Disposed`, `Del Scope`) yang diberi suffix per run (S-12). TC-905 "Transaksi selesai & baris log historis tetap nama lama" tidak punya precondition transaksi selesai; spec meminta satu Transfer selesai ke group itu (disediakan tim FE).
  - TC-907 dan 908 memakai Reader SFR-01, ACS-01, dan user E dari Pre-setup No 11; memindahkannya ke group milik spec mengubah data Pre-setup bersama selama spec berjalan (S-06 pengecualian 2026-10-30 dipakai, dengan pemulihan fixture BE).
  - TC-905 b memecah klausa "transaksi selesai" dan "baris log historis" menjadi dua Verifikasi (S-01); surface log adalah log pada detail Transfer, nama lama pada kolom Note.
  - TC-910 Expected hanya menyebut assignment user F hilang tanpa anchor; spec memakai toast sukses Delete sebagai anchor (8b butir 2).
  - TC-908 b menyebut referensi FARP-LOGIC-16 dan E-FASU-09 tanpa teks yang dapat diasersi; spec memverifikasi constraint assignment lepas sebagai satu klausa.
  - TC-908 c: baseline kuota pool dibaca dari License > Allocation Quota, surface yang sama yang dibuka TC pada langkah 2; TC tidak menyebut label kuota pool, sehingga spec membaca kuota pool pada surface itu (kemampuan baca disediakan tim FE/BE, tanpa label karangan).
  - TC-908 b klausa "tanpa entri log" tidak teruji: TC tidak menyebut surface log (Changelog: User, System Log, atau Activity Log) sehingga baseline dan anchor tidak dapat ditetapkan (S-12, 8b butir 2); spec hanya mengasersi Home Group user E kosong. Menunggu TC menamai surface log.

