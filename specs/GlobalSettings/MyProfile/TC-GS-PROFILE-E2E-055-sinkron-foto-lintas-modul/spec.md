---
id: TC-GS-PROFILE-E2E-055-sinkron-foto-lintas-modul
title: "Sinkron Foto: Fixed Asset, Admin Console, Recycle Bin, dan Changelog File Manager"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-242
  - TC-GS-PROFILE-243
  - TC-GS-PROFILE-244
  - TC-GS-PROFILE-245
  - TC-GS-PROFILE-312
coverage:
  web: automated
---

# Sinkron Foto: Fixed Asset, Admin Console, Recycle Bin, dan Changelog File Manager

## Prerequisites

- Mode: FE+BE.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`, `Spectra.env.GS_PROFILE_PWD12H_PASSWORD`, `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`), counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Akun aktor pertama spec: Pre-setup #1 (Andi Pratama, Total Control, tanpa foto, App Access Global Settings, Fixed Asset, dan Admin Console) `totalControlProfile_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_TC_PASSWORD`. Ganti akun ke Pre-setup #10 (Fajar Nugroho, tanpa foto, App Access Fixed Asset) `noPhotoProfile_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_NOPHOTO_PASSWORD`; lalu Pre-setup #9 (Nadia Putri, foto aktif `nadia-photo.jpg`) `photoProfile_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_PHOTO_PASSWORD`.
- Env var: `GS_PROFILE_TC_PASSWORD`, `GS_PROFILE_NOPHOTO_PASSWORD`, `GS_PROFILE_PHOTO_PASSWORD`.
- File uji (Pre-setup #17): `valid-photo.png`.
- Kemampuan teknis: hover Avatar; menangani file picker native; membaca jumlah entri Recycle Bin File Manager untuk `nadia-photo.jpg` per Deleted By dan jumlah baris Changelog File Manager Action `Delete`, Field `File Name`, Old Value `nadia-photo.jpg` per Modified By sebelum aksi (baseline, S-12; audit trail permanen, disediakan tim FE/BE); fixture BE memulihkan foto profil dan memasang `nadia-photo.jpg` sebagai foto aktif.
- Pemulihan (R-08): langkah 9 mengembalikan Andi Pratama ke keadaan tanpa foto, langkah 18 mengembalikan Fajar Nugroho ke keadaan tanpa foto, langkah 32 memasang `nadia-photo.jpg` sebagai foto aktif Nadia Putri (kondisi awal TC-GS-PROFILE-245), dan langkah 40 memasangnya kembali sesudah Delete, semuanya lewat fixture BE; hook `after` suite memulihkan foto #9 dan #10, dan hook `after` spec ini memulihkan foto Pre-setup #1 bila spec gagal di tengah. Entri audit trail permanen yang ditambahkan spec tidak dihapus.
- State global yang diubah: foto profil Pre-setup #1, #9, dan #10. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-PROFILE-312: Edit Photo, tampilan user di Admin Console > Settings > User

1. Hover Avatar lalu klik `[Edit]`
2. Pilih file `valid-photo.png`
3. Buka Admin Console > Settings > User
4. Ketik Search `Andi Pratama`, tekan Enter
5. Verifikasi kolom Name pada daftar user Admin Console menampilkan foto baru Andi Pratama
6. Buka Detail Andi Pratama
7. Verifikasi Avatar Header Detail Andi Pratama di Admin Console menampilkan foto baru
8. Verifikasi Avatar Header Detail Andi Pratama di Admin Console tanpa overlay edit
9. Kembalikan Andi Pratama ke keadaan tanpa foto lewat fixture BE

### TC-GS-PROFILE-242: Edit Photo, tampilan user di Fixed Asset > Settings > User

10. Logout
11. Login sebagai Fajar Nugroho (Pre-setup #10)
12. Buka My Profile dari account menu navbar
13. Hover Avatar lalu klik `[Edit]`
14. Pilih file `valid-photo.png`
15. Buka Fixed Asset > Settings > User
16. Ketik Search `Fajar Nugroho`, tekan Enter
17. Verifikasi Avatar Fajar Nugroho pada daftar Fixed Asset > Settings > User menampilkan foto baru
18. Kembalikan Fajar Nugroho ke keadaan tanpa foto lewat fixture BE

### TC-GS-PROFILE-243 dan TC-GS-PROFILE-244: Edit Photo, foto lama masuk Recycle Bin dan Changelog File Manager

19. Logout
20. Login sebagai Nadia Putri (Pre-setup #9)
21. Buka My Profile dari account menu navbar
22. Catat baseline lewat kemampuan baca: jumlah entri Recycle Bin `nadia-photo.jpg` dengan Deleted By `System`, dan jumlah baris Changelog File Manager Action `Delete` untuk `nadia-photo.jpg` dengan Modified By `System`
23. Hover Avatar lalu klik `[Edit]`
24. Pilih file `valid-photo.png`
25. Buka Global Settings > File Manager lalu klik Recycle Bin di toolbar
26. Cari `nadia-photo.jpg`
27. Verifikasi `nadia-photo.jpg` tampil di Recycle Bin dengan Deleted By `System` (jumlah entri dengan Deleted By itu bertambah tepat satu dibanding baseline)
28. Tutup Recycle Bin, bersihkan pencarian, buka tabel utama File Manager
29. Verifikasi tabel utama File Manager memuat `valid-photo.png` sebagai file aktif
30. Buka Global Settings > File Manager > Changelog
31. Verifikasi Changelog File Manager memuat satu baris baru: Action `Delete`, Field `File Name`, Old Value `nadia-photo.jpg`, New Value `—`, Modified By `System` (jumlah baris dengan Modified By itu bertambah tepat satu dibanding baseline)

### TC-GS-PROFILE-245: Delete Photo, foto lama masuk Recycle Bin dengan Deleted By pemilik sendiri

32. Pasang `nadia-photo.jpg` sebagai foto aktif Nadia Putri lewat fixture BE dan muat ulang halaman (F5)
33. Catat baseline lewat kemampuan baca: jumlah entri Recycle Bin `nadia-photo.jpg` dengan Deleted By `Nadia P`, dan jumlah baris Changelog File Manager Action `Delete` untuk `nadia-photo.jpg` dengan Modified By `Nadia P`
34. Hover Avatar lalu klik `[Delete]`
35. Klik `[Remove]`
36. Buka Global Settings > File Manager lalu klik Recycle Bin dan cari `nadia-photo.jpg`
37. Verifikasi `nadia-photo.jpg` tampil di Recycle Bin dengan Deleted By `Nadia P` (jumlah entri dengan Deleted By itu bertambah tepat satu dibanding baseline)
38. Buka Changelog File Manager
39. Verifikasi Changelog File Manager memuat satu baris baru: Action `Delete`, Field `File Name`, Old Value `nadia-photo.jpg`, New Value `—`, Modified By `Nadia P` (jumlah baris dengan Modified By itu bertambah tepat satu dibanding baseline)
40. Pasang kembali `nadia-photo.jpg` sebagai foto aktif Nadia Putri lewat fixture BE

## Notes

- Mode: FE+BE. Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (40 langkah) karena lima TC berada di satu kelas (sinkron foto lintas modul, FE+BE) dan tiap blok akun berdiri sendiri: Step ganti akun eksplisit (langkah 10, 11, 19, 20) dan bagian sesudah ganti akun tetap bermakna walau blok sebelumnya gagal. TC-GS-PROFILE-245 memakai Delete di akhir (bagian 3 butir 5).
- TC-GS-PROFILE-243 dan 244 memakai satu aksi Edit Photo yang sama (langkah 23 dan 24). TC-GS-PROFILE-312 memakai Pre-setup #1 (akun default suite) sehingga berada pertama tanpa ganti akun.
- Urutan blok TC-GS-PROFILE-312, 242, 243 dan 244, lalu 245 mengikuti akun (Andi, Fajar, Nadia) agar ganti akun seminimal mungkin (S-10); urutan ini berbeda dari urutan nomor TC.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 4, 16, dan 26 (Search untuk menemukan baris atau file target, R-16), 28 (menutup Recycle Bin, membersihkan pencarian, dan membuka tabel utama File Manager sebelum verifikasi tabel utama), 9, 18, 32, dan 40 (pemulihan foto, langkah 32 juga memuat ulang halaman), 12 dan 21 (membuka My Profile setelah login).
- Temuan untuk QA:
  - TC-GS-PROFILE-242 Expected hanya menyebut Avatar di Fixed Asset > Settings > User sedangkan langkah TC menyebut daftar lalu Detail; spec mengasersi Avatar pada daftar.
  - TC-GS-PROFILE-243 dan 245 mengasersi Recycle Bin untuk nama `nadia-photo.jpg` yang sama, sehingga entri bertambah antar run; spec memakai baseline jumlah entri per Deleted By (S-12).
  - TC-GS-PROFILE-245 mensyaratkan foto aktif `nadia-photo.jpg` yang sudah dihapus pada TC-GS-PROFILE-243; spec memasang kembali foto lewat fixture BE (langkah 32).
