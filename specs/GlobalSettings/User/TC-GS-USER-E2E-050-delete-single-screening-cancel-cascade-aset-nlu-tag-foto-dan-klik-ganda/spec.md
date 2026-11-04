---
id: TC-GS-USER-E2E-050-delete-single-screening-cancel-cascade-aset-nlu-tag-foto-dan-klik-ganda
title: "Delete User Single: Screening Dialog, Cancel, Cascade Aset dan Approval, Non-Login User, TAG, dan Foto, Klik Ganda, serta dari Header Detail"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-261
  - TC-GS-USER-265
  - TC-GS-USER-263
  - TC-GS-USER-262
  - TC-GS-USER-264
  - TC-GS-USER-266
  - TC-GS-USER-267
  - TC-GS-USER-268
  - TC-GS-USER-269
  - TC-GS-USER-272
  - TC-GS-USER-270
coverage:
  web: automated
---

# Delete User Single: Screening Dialog, Cancel, Cascade Aset dan Approval, Non-Login User, TAG, dan Foto, Klik Ganda, serta dari Header Detail

## Prerequisites

- Mode: FE+BE. Spec menghapus data (aksi destruktif) sehingga dijalankan sesudah spec lain selesai (suite `parallel: false`).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-25) tidak dipakai sebagai target aksi dan tidak diubah. John Doe Pre-setup (No. 18) hanya dibaca fotonya sebagai pembanding di File Manager (TC-GS-USER-268).
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Semua user Activated, Active, Division `Finance`, Access `Fixed Asset` kecuali dinyatakan lain:
  - R-1: Name `Rudi Hakim {runId}-050`, email `rudihakim+{runId}-050@qwertysystem.net`, tanpa aset, approval, dan foto (TC-GS-USER-261, 263, 262).
  - A-1: Name `Ahmad Fauzi {runId}-050`, email `ahmadfauzi+{runId}-050@qwertysystem.net`; mewakili Non-Login User N-1 (TC-GS-USER-265, 266). N-1: Non-Login User Name `Agus Prasetyo {runId}-050` dengan Represented By A-1.
  - J-1: Name `Joko Susilo {runId}-050`, email `jokosusilo+{runId}-050@qwertysystem.net`, Access `Fixed Asset` dan `Supply Asset`, punya borrowed asset dengan transaksi di Fixed Asset > Borrow, dan approval in-flight (HK8; seeding aset dan approval disediakan tim FE/BE) (TC-GS-USER-264).
  - T-1: Name `John Doe {runId}-050`, email `johndoe+{runId}-050@qwertysystem.net`, TAG `TAG-USR-0001` terpasang (HK7; pairing TAG pada seeding dan simulasi scan disediakan tim FE/BE) (TC-GS-USER-267). TAG `TAG-USR-0001` bebas (Tabel Data Uji Pre-setup No. 25) dan tidak dipakai spec lain pada saat spec ini berjalan.
  - P-1: Name `John Doe Foto {runId}-050`, email `johndoefoto+{runId}-050@qwertysystem.net`, 1 foto aktif dan 2 foto lama di Recycle Bin File Manager (HK8; seeding File Manager disediakan tim FE/BE; foto dikenali sebagai milik P-1) (TC-GS-USER-268).
  - R-2: Name `Rudi Hakim Dua {runId}-050`, email `rudihakimdua+{runId}-050@qwertysystem.net`, tanpa foto (TC-GS-USER-269).
  - R-3: Name `Rudi Hakim Tiga {runId}-050`, email `rudihakimtiga+{runId}-050@qwertysystem.net` (TC-GS-USER-272).
  - R-4: Name `Rudi Hakim Empat {runId}-050`, email `rudihakimempat+{runId}-050@qwertysystem.net` (TC-GS-USER-270).
  - U-N: user baru yang dibuat langkah 41 sampai 46: Name `Tag Baru {runId}-050`, email `tagbaru+{runId}-050@qwertysystem.net`.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus R-1, A-1, N-1, J-1, T-1, P-1, R-2, R-3, R-4, dan U-N lewat API bila masih ada; lepaskan TAG `TAG-USR-0001`.
- Kemampuan teknis: simulasi scan TAG (`TAG-USR-0001`) pada form Create; klik ganda cepat pada tombol dialog; membuka Fixed Asset > Borrow, File Manager (list dan Recycle Bin) dengan akun Total Control; mengetahui proses purge foto selesai (polling idiom bagian 6: muat ulang tiap 5 detik, batas tunggu 2 menit; purge tidak menunggu 30 hari).
- State global yang diubah: Custom Field `Emergency Phone` tidak Required selama spec ini (Tabel Pre-setup No. 24: Required hanya aktif untuk TC-GS-USER-158 dan 349, TC Create dan Edit lain dijalankan saat Required nonaktif; pembuatan user U-N pada langkah 41 sampai 46 tidak mengisinya dan mengharapkan Create sukses). Pengubahan dan pemulihan status Required disediakan tim FE/BE; hook `before` mencatat status awal, hook `after` memulihkannya walau spec gagal di tengah. Suite berjalan serial; spec ini menghapus data milik spec saja.

## Test Steps

### Persiapan

1. Klik icon Search, ketik `{runId}-050`, tekan Enter

### TC-GS-USER-261: Screening dialog Delete User

2. Klik (⋯) baris `Rudi Hakim {runId}-050` lalu `Delete`
3. Verifikasi Title dialog `Delete User`
4. Verifikasi body memuat bullet `• Rudi Hakim {runId}-050`
5. Verifikasi body memuat `Historical transaction data will be preserved.`
6. Verifikasi body memuat `This action cannot be undone. Are you sure you want to delete it?`
7. Verifikasi tombol `[Cancel]` dan `[Delete]`

### TC-GS-USER-263: Delete dialog [Cancel] tidak menghapus

8. Klik `[Cancel]`
9. Verifikasi baris `Rudi Hakim {runId}-050` tetap ada
10. Verifikasi tidak ada toast

### TC-GS-USER-265: Delete user yang mewakili Non-Login User menambah daftar NLU terdampak di dialog

11. Klik (⋯) baris `Ahmad Fauzi {runId}-050` lalu `Delete`
12. Verifikasi body menambah `Represented By will be cleared for the following non-login user(s):`
13. Verifikasi body memuat bullet `• Agus Prasetyo {runId}-050` tanpa angka
14. Klik `[Cancel]`

### TC-GS-USER-262: Delete happy path, user hilang dari list

15. Klik (⋯) baris `Rudi Hakim {runId}-050` lalu `Delete`
16. Klik `[Delete]`
17. Verifikasi toast sukses "Success, user has been deleted."
18. Verifikasi baris `Ahmad Fauzi {runId}-050` tampil di tabel (pembanding)
19. Verifikasi baris `Rudi Hakim {runId}-050` hilang dari User List

### TC-GS-USER-264: Delete user yang punya aset dan approval menampilkan nama tanpa angka lalu tetap bisa diproses

20. Klik (⋯) baris `Joko Susilo {runId}-050` lalu `Delete`
21. Verifikasi body menampilkan bullet `• Joko Susilo {runId}-050` tanpa angka jumlah aset atau approval
22. Klik `[Delete]`
23. Verifikasi toast sukses "Success, user has been deleted."
24. Buka Fixed Asset > Borrow, cari transaksi `Joko Susilo {runId}-050`
25. Verifikasi transaksi historis tetap menampilkan `Joko Susilo {runId}-050`

### TC-GS-USER-266: Delete user yang mewakili Non-Login User mengosongkan Represented By

26. Klik menu User di sidebar Global Settings
27. Klik icon Search, ketik `{runId}-050`, tekan Enter
28. Klik (⋯) baris `Ahmad Fauzi {runId}-050` lalu `Delete`
29. Klik `[Delete]`
30. Verifikasi toast "Success, user has been deleted."
31. Klik sub-tab `Non-Login User`
32. Klik icon Search, ketik `Agus Prasetyo {runId}-050`, tekan Enter
33. Buka Detail `Agus Prasetyo {runId}-050` dengan klik Name
34. Verifikasi Represented By `Agus Prasetyo {runId}-050` kosong

### TC-GS-USER-267: Delete user dengan TAG terpasang melepas TAG

35. Klik menu User di sidebar Global Settings
36. Klik icon Search, ketik `{runId}-050`, tekan Enter
37. Klik (⋯) baris `John Doe {runId}-050` lalu `Delete`
38. Klik `[Delete]`
39. Verifikasi toast delete sukses "Success, user has been deleted."
40. Klik `[+ User]` di Table Tools
41. Isi First Name `Tag`, Last Name `Baru {runId}-050`, Division `Finance`, Email `tagbaru+{runId}-050@qwertysystem.net`, pilih Access `Fixed Asset` pada multi dropdown Access (placeholder `Select access`)
42. Klik `Scan TAG`
43. Scan `TAG-USR-0001`
44. Verifikasi tidak ada pesan error pada pemasangan TAG
45. Verifikasi `TAG-USR-0001` terpasang pada form user baru
46. Klik `[Submit]`
47. Verifikasi toast sukses "Success, user has been created."

### TC-GS-USER-268: Delete user dengan foto aktif dan foto di Recycle Bin, semua foto terhapus permanen

48. Buka File Manager (list)
49. Verifikasi foto aktif milik `John Doe Foto {runId}-050` tampil
50. Buka Recycle Bin File Manager
51. Verifikasi 2 foto lama milik `John Doe Foto {runId}-050` tampil
52. Klik menu User di sidebar Global Settings
53. Klik icon Search, ketik `{runId}-050`, tekan Enter
54. Klik (⋯) baris `John Doe Foto {runId}-050` lalu `Delete`
55. Klik `[Delete]`
56. Verifikasi toast delete sukses "Success, user has been deleted." tampil tanpa menunggu purge
57. Tunggu proses purge selesai (polling: muat ulang File Manager tiap 5 detik sampai foto aktif milik `John Doe Foto {runId}-050` tidak ada, batas tunggu 2 menit)
58. Buka File Manager (list)
59. Verifikasi foto `John Doe` Pre-setup (No. 18) tampil (pembanding)
60. Verifikasi foto aktif milik `John Doe Foto {runId}-050` tidak ada di File Manager
61. Buka Recycle Bin File Manager
62. Verifikasi 2 foto lama milik `John Doe Foto {runId}-050` tidak ada di Recycle Bin

### TC-GS-USER-269: Delete user tanpa foto, purge no-op dan delete tetap sukses

63. Klik menu User di sidebar Global Settings
64. Klik icon Search, ketik `{runId}-050`, tekan Enter
65. Klik (⋯) baris `Rudi Hakim Dua {runId}-050` lalu `Delete`
66. Klik `[Delete]`
67. Verifikasi toast sukses "Success, user has been deleted."

### TC-GS-USER-272: Delete double-click [Delete] hanya satu request

68. Tunggu toast lama hilang otomatis
69. Klik (⋯) baris `Rudi Hakim Tiga {runId}-050` lalu `Delete`
70. Double-click `[Delete]`
71. Verifikasi hanya 1 toast sukses "Success, user has been deleted."
72. Verifikasi tidak ada toast error dari request kedua

### TC-GS-USER-270: Delete User dari menu [⋯] header Detail kembali ke User List

73. Buka Detail `Rudi Hakim Empat {runId}-050` dengan klik Name
74. Klik `[⋯]` header lalu `Delete User` (danger)
75. Verifikasi Title dialog `Delete User`
76. Verifikasi body dialog sama dengan Delete dari List: bullet `• Rudi Hakim Empat {runId}-050`, `Historical transaction data will be preserved.`, dan `This action cannot be undone. Are you sure you want to delete it?`
77. Verifikasi tombol `[Cancel]` dan `[Delete]`
78. Klik `[Delete]`
79. Verifikasi toast sukses "Success, user has been deleted."
80. Verifikasi navigasi kembali ke User List

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (80 langkah) karena sebelas TC Delete single berada di satu kelas harness (fungsional), satu aksi (Delete User), dan satu layar (User List dan header Detail). Tiap blok berdiri sendiri pada user seed sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Pembukaan ulang User List (langkah 26, 27, 35, 36, 52, 53, 63, 64) dan pembacaan halaman lain (24, 31 sampai 33, 48, 50, 58, 61) memakai langkah pendek tanpa asersi tambahan.
- Urutan TC sumber diubah: TC-GS-USER-263 mengikuti TC-GS-USER-261 pada dialog yang sama (langkah "Klik (⋯) ... `Delete`" TC-263 sumber dipenuhi langkah 2); TC-GS-USER-265 (dialog saja, ditutup dengan `[Cancel]`) ditaruh sebelum semua Delete yang mengonfirmasi, dan TC-GS-USER-266 (Delete user yang sama, `Ahmad Fauzi {runId}-050`) sesudahnya; aksi yang menghapus data ditaruh sesudah screening dan Cancel (bagian 3 prinsip 5). TC-GS-USER-270 paling akhir karena pindah ke halaman Detail.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1, 27, 36, 53, 64 (Search), 8, 14 (menutup dialog dengan `[Cancel]`), 24, 26, 31 sampai 33, 35, 48, 50, 52, 58, 61, 63, 73, 74 (membuka halaman dan surface), 57 (menunggu purge), 68 (menunggu toast lama hilang agar hitungan toast langkah 71 tidak tercampur), 40 sampai 43 dan 46 (membuat user baru dan scan TAG).
- Asersi tambahan: langkah 18 (baris pembanding sebelum asersi baris hilang, bagian 8b butir 2); 47 (toast "Success, user has been created." menandai pemasangan TAG pada user baru berhasil tanpa error; TC-GS-USER-267 butir b hanya menyebut "tanpa error"); 49 dan 51 (foto milik P-1 tampil sebelum Delete, menjadi pembanding positif untuk absence di langkah 60 dan 62 pada surface dan pencarian yang sama); 59 (foto Pre-setup tampil sebagai pembanding di File Manager); 75 sampai 77 (isi dialog dari header sebagai pembuktian "dialog sama dengan Delete dari List").
- Cara mencari file di File Manager (nama file atau pemilik) ditentukan tim FE di tahap script; asersi memakai foto yang dikenali sebagai milik user terkait.
- TAG: TC-GS-USER-267 memakai `TAG-4F7K2XQ9`, yang dipasang pada John Doe Pre-setup (No. 18). Spec memakai `TAG-USR-0001` (bebas, Tabel Data Uji Pre-setup No. 25) pada user seed T-1 supaya data Pre-setup tidak berubah (S-06).
- Pembagian TC: log Delete di Changelog, System Log, dan Activity Log, Delete gagal 5xx, serta Delete record yang sudah dihapus admin lain diverifikasi di spec lain.
- Temuan untuk QA:
  - TC-GS-USER-262 Post Condition a (email dan Employee ID dapat dipakai user baru), b (sesi aktif Rudi diakhiri), dan c (terdampak user list Fixed Asset/Supply Asset) tanpa langkah observasi; tidak diasersi. Employee ID `EMP-0300` pada precondition TC tidak dipakai langkah, sehingga tidak di-seed.
  - TC-GS-USER-264 Post Condition ("Approval in-flight Joko ditangani Total Control/override") tanpa langkah observasi; tidak diasersi.
  - TC-GS-USER-266 Post Condition (terdampak Non-Login User) punya padanan di Expected b; TC-GS-USER-267 Post Condition (TAG Registry status TAG tersedia) punya padanan di Expected b.
  - TC-GS-USER-267 tidak menyebut apakah `[Submit]` pada user baru diperlukan agar TAG dipasang; spec men-submit user baru dan mengasersi toast sukses.
  - TC-GS-USER-268 tidak menyebut lokasi File Manager list dan Recycle Bin, cara mengetahui purge selesai, dan batas waktu penantian; langkah "amati berulang" ditulis sebagai polling idiom bagian 6 (muat ulang tiap 5 detik, batas 2 menit).
  - TC-GS-USER-268 mensyaratkan 3 foto John Doe di Recycle Bin pada precondition (1 aktif, 2 di Recycle Bin); spec memakai seed P-1 dan pembanding foto John Doe Pre-setup.
  - TC-GS-USER-264 langkah 4 ("Buka Fixed Asset > Borrow, cari transaksi Joko") tidak menyebut cara mencari; spec mencari berdasarkan Name user.
  - TC-GS-USER-266 butir b ("Represented By kosong") tidak menyebut representasi nilai kosong (`—` atau teks kosong).
  - TC-GS-USER-272 butir b ("tidak ada toast error dari request kedua") adalah asersi absence tanpa pembanding spesifik; spec mengasersinya sesudah langkah 71 yang menampilkan toast sukses pada surface yang sama.
