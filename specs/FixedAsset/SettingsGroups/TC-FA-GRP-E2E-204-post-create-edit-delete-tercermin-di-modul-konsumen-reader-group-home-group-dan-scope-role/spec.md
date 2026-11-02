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
4. Buka field Group Register Asset
5. Verifikasi `Sync New {runId}-204` tersedia sebagai pilihan di Register Asset
6. Buka Home Group di Settings > User
7. Verifikasi `Sync New {runId}-204` tersedia sebagai pilihan Home Group
8. Buka Reader Group di GS Hardware
9. Verifikasi `Sync New {runId}-204` tersedia sebagai pilihan Reader Group
10. Buka scope Settings > Role & Permission
11. Verifikasi `Sync New {runId}-204` tersedia sebagai pilihan scope

### TC-905: Post-Edit rename tercermin live

12. Buka Fixed Asset > Settings > Groups
13. Rename `Sync Rename {runId}-204` menjadi `Sync Renamed {runId}-204`
14. Verifikasi toast sukses "Success, group has been updated."
15. Buka Settings > Role & Permission
16. Verifikasi `Sync Renamed {runId}-204` tampil di Role & Permission
17. Buka Asset list
18. Verifikasi `Sync Renamed {runId}-204` tampil di Asset list
19. Buka Transfer
20. Verifikasi `Sync Renamed {runId}-204` tampil di Transfer
21. Buka GS Hardware
22. Verifikasi `Sync Renamed {runId}-204` tampil di GS Hardware
23. Buka detail Transfer yang selesai ke group itu di modul Transfer
24. Verifikasi Transfer tersebut berstatus selesai
25. Verifikasi baris log historis pada log detail Transfer tersebut menampilkan nama lama `Sync Rename {runId}-204` pada kolom Note (snapshot), bukan `Sync Renamed {runId}-204`
26. Verifikasi baris log historis lain pada log detail Transfer tersebut juga tetap bernama lama `Sync Rename {runId}-204`

### TC-906: Post-Delete node hilang dari dropdown

27. Buka field Group Register Asset
28. Verifikasi sedikitnya satu group lain tampil sebagai pilihan (anchor)
29. Tutup field Group
30. Buka Fixed Asset > Settings > Groups
31. Buka elipsis `Sync Del {runId}-204`, pilih Delete, klik [Delete]
32. Verifikasi toast sukses "Success, group has been deleted."
33. Buka dropdown Register Asset, Transfer, Disposal, Home Group, dan Reader Group
34. Verifikasi sedikitnya satu group lain tampil di kelima dropdown (anchor)
35. Verifikasi `Sync Del {runId}-204` dan descendant tidak lagi tersedia di kelima dropdown

### TC-907: Delete group Reader Group tidak diblok

36. Buka Fixed Asset > Settings > Groups
37. Buka elipsis `Del Reader {runId}-204`, pilih Delete, klik [Delete]
38. Verifikasi toast sukses "Success, group has been deleted." (tanpa dialog blok)
39. Buka GS Hardware Smart Fixed Reader dan Asset Control Station
40. Verifikasi Reader Group SFR-01 dan ACS-01 kosong (orphan)

### TC-908: Delete Home Group user dan alokasi lisensi tidak diblok

41. Buka Fixed Asset > Settings > Groups
42. Buka elipsis `Del Home Lic {runId}-204`, pilih Delete
43. Verifikasi dialog konfirmasi normal tampil
44. Klik [Delete]
45. Verifikasi toast sukses "Success, group has been deleted."
46. Buka Settings > User (user E)
47. Verifikasi Home Group user E kosong tanpa entri log
48. Verifikasi constraint assignment Group Role dan Group Manager yang bersumber dari Home Group itu ikut lepas
49. Buka License > Allocation Quota
50. Verifikasi alokasi ikut terhapus
51. Verifikasi kuota kembali ke pool

### TC-909: Delete group aset Disposed/Deleted

52. Buka Fixed Asset > Settings > Groups
53. Buka elipsis `Del Disposed {runId}-204`, pilih Delete, klik [Delete]
54. Verifikasi toast sukses "Success, group has been deleted."
55. Buka Asset list dengan filter Disposed
56. Verifikasi ketiga aset tetap ada dengan Group kosong
57. Buka Disposal Log
58. Verifikasi nama `Del Disposed {runId}-204` terbaca via snapshot

### TC-910: User kehilangan scope Role

59. Buka Fixed Asset > Settings > Groups
60. Buka elipsis `Del Scope {runId}-204`, pilih Delete
61. Klik [Delete] pada dialog warning
62. Verifikasi toast sukses "Success, group has been deleted."
63. Buka Settings > Role & Permission user F
64. Verifikasi assignment user F di `Del Scope {runId}-204` hilang

## Notes

- Langkah penghubung (S-03): Tutup field Group, dan "Buka Fixed Asset > Settings > Groups" di awal tiap blok TC-905 sampai 910 karena blok sebelumnya berakhir di modul konsumen (S-14). Asersi tambahan (S-03, 8b butir 2): Verifikasi sedikitnya satu group lain tampil di kelima dropdown sebelum asersi group terhapus tidak tersedia (TC-906), dan Verifikasi toast sukses Delete sebelum asersi assignment user F hilang (TC-910; menggantikan Tunggu aksi selesai karena hasil aksi kini diasersi). Urutan: aksi menghapus (TC-906 sampai 910) ditaruh sesudah TC-904 dan 905 karena menghapus data (S-10).
- Spec memiliki 64 langkah, di atas smell 35 langkah. Alasan: tujuh TC satu topik (propagasi perubahan group ke modul konsumen) dengan fixture terpisah per TC; tiap TC berdiri sendiri, dan banyak langkah berasal dari Expected yang memeriksa beberapa modul konsumen (S-01).
- Temuan untuk QA:
  - TC-904 sampai 910 menulis nama literal (`Sync New`, `Sync Del`, `Del Reader`, `Del Home Lic`, `Del Disposed`, `Del Scope`) yang diberi suffix per run (S-12). TC-905 "Transaksi selesai & baris log historis tetap nama lama" tidak punya precondition transaksi selesai; spec meminta satu Transfer selesai ke group itu (disediakan tim FE).
  - TC-907 dan 908 memakai Reader SFR-01, ACS-01, dan user E dari Pre-setup No 11; memindahkannya ke group milik spec mengubah data Pre-setup bersama selama spec berjalan (S-06 pengecualian 2026-10-30 dipakai, dengan pemulihan fixture BE).
  - TC-905 b memecah klausa "transaksi selesai" dan "baris log historis" menjadi dua Verifikasi (S-01); surface log adalah log pada detail Transfer, nama lama pada kolom Note.
  - TC-910 Expected hanya menyebut assignment user F hilang tanpa anchor; spec memakai toast sukses Delete sebagai anchor (8b butir 2).
  - TC-908 b menyebut referensi FARP-LOGIC-16 dan E-FASU-09 tanpa teks yang dapat diasersi; spec memverifikasi constraint assignment lepas sebagai satu klausa.

