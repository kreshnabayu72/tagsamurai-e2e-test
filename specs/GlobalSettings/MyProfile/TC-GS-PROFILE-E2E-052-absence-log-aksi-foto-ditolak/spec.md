---
id: TC-GS-PROFILE-E2E-052-absence-log-aksi-foto-ditolak
title: "Absence Log: Delete Photo No-op, Ekstensi Ditolak, dan Storage Penuh Tidak Menulis Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-PROFILE-224
  - TC-GS-PROFILE-225
  - TC-GS-PROFILE-226
coverage:
  web: automated
---

# Absence Log: Delete Photo No-op, Ekstensi Ditolak, dan Storage Penuh Tidak Menulis Log

## Prerequisites

- Mode: FE+BE.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`, `Spectra.env.GS_PROFILE_PWD12H_PASSWORD`, `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`), counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Akun aktor pertama spec: Pre-setup #10 (Fajar Nugroho, Total Control, tanpa foto) `noPhotoProfile_automated_{namaCompany}@qwertysystem.net`, login di hook `before` spec ini dengan `Spectra.env.GS_PROFILE_NOPHOTO_PASSWORD`. Ganti akun ke Pre-setup #11 (Client Storage penuh: kuota 50.0 GB, usage 50.0 GB) `totalControlStorageFull_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_STORAGEFULL_PASSWORD`. Pembaca log: admin Pre-setup #6 (Hendra Wijaya) `adminActor_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_ADMIN_PASSWORD`, login lewat UI pada langkah ganti akun.
- Env var: `GS_PROFILE_NOPHOTO_PASSWORD`, `GS_PROFILE_STORAGEFULL_PASSWORD`, `GS_PROFILE_ADMIN_PASSWORD`.
- File uji (Pre-setup #17): `document.pdf` dan `valid-photo.png`.
- Kemampuan teknis: klien HTTP untuk request langsung ke server atas sesi Fajar Nugroho (Delete Photo dan Edit Photo lewat bypass file picker; pemicu kelas a yang tidak menjadi objek uji, `P-5` butir a); hover Avatar; menangani file picker native; membaca jumlah baris Tab Changelog, Tab System Log, dan Activity Log sebelum dan sesudah aksi (baseline, S-12; disediakan tim FE/BE); membaca foto aktif user lewat fixture BE.
- Admin pembaca log untuk Client Storage penuh: admin Pre-setup #6 sesuai TC; bila Pre-setup #6 bukan anggota Client itu, admin Total Control Client tersebut disediakan tim FE (lihat Temuan untuk QA).
- Data Pre-setup yang ditulis: tidak ada (aksi ditolak atau no-op). Kuota dan ledger Storage Pre-setup #11 tidak diubah spec; hook `after` suite memulihkannya bila fixture mengubahnya.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-PROFILE-224: Delete Photo no-op tidak menulis log

1. Catat baseline lewat kemampuan baca: jumlah baris Tab Changelog dan Tab System Log Detail Fajar Nugroho, serta jumlah baris Activity Log dengan Name `Fajar Nugroho`
2. Kirim request Delete Photo langsung ke server atas akun Fajar Nugroho
3. Verifikasi respons `200 OK`
4. Logout
5. Login sebagai admin Hendra Wijaya (Pre-setup #6)
6. Buka Global Settings > User > Detail Fajar Nugroho > Tab Changelog
7. Verifikasi Tab Changelog memuat sedikitnya satu baris pembanding
8. Verifikasi jumlah baris Tab Changelog sama dengan baseline
9. Buka Tab System Log
10. Verifikasi Tab System Log memuat sedikitnya satu baris pembanding
11. Verifikasi jumlah baris Tab System Log sama dengan baseline
12. Buka Global Settings > Activity Log
13. Verifikasi Activity Log memuat sedikitnya satu baris pembanding
14. Verifikasi jumlah baris Activity Log dengan Name `Fajar Nugroho` sama dengan baseline

### TC-GS-PROFILE-225: Edit Photo ditolak karena ekstensi tidak diizinkan tidak menulis log

15. Logout
16. Login sebagai Fajar Nugroho (Pre-setup #10)
17. Buka My Profile dari account menu navbar
18. Catat baseline lewat kemampuan baca: jumlah baris Tab Changelog Detail Fajar Nugroho
19. Kirim file `document.pdf` lewat bypass file picker (request Edit Photo langsung ke server)
20. Verifikasi foto Fajar Nugroho tidak berubah (tetap tanpa foto, dibaca lewat fixture BE)
21. Logout
22. Login sebagai admin Hendra Wijaya (Pre-setup #6)
23. Buka Global Settings > User > Detail Fajar Nugroho > Tab Changelog
24. Verifikasi Tab Changelog memuat sedikitnya satu baris pembanding
25. Verifikasi jumlah baris Tab Changelog sama dengan baseline

### TC-GS-PROFILE-226: Edit Photo ditolak karena Storage penuh tidak menulis log

26. Logout
27. Login sebagai akun Client Storage penuh (Pre-setup #11)
28. Buka My Profile dari account menu navbar
29. Catat baseline lewat kemampuan baca: jumlah baris Field `Photo` pemilik akun Pre-setup #11 di Activity Log
30. Hover Avatar lalu klik `[Edit]`
31. Pilih file `valid-photo.png`
32. Tunggu aksi selesai
33. Logout
34. Login sebagai admin Hendra Wijaya (Pre-setup #6)
35. Buka Global Settings > Activity Log
36. Verifikasi Activity Log memuat sedikitnya satu baris pembanding
37. Verifikasi Activity Log tidak memuat baris Photo baru dari aksi itu (jumlah baris Field `Photo` pemilik akun Pre-setup #11 sama dengan baseline)

## Notes

- Mode: FE+BE. Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas g (asersi absence). Pemicu request langsung (kelas a, langkah 2 dan 19) dan Edit Photo saat Storage penuh (langkah 30 dan 31) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji: `P-5` butir a. Tiap TC punya user dan baseline sendiri (langkah 1, 18, dan 29). Perilaku FE untuk respons penolakan tidak diasersi di spec ini (bagian 8b butir 1).
- Spec melewati sekitar 35 langkah (37 langkah) karena tiga TC berada di satu kelas (g) dan tiap TC wajib punya user dan baseline sendiri (`P-5` butir a) sehingga ganti akun berulang tidak dapat digabung; kegagalan satu blok tidak membuat blok lain kehilangan makna. Tiga blok baca-log berpola (langkah 6 sampai 14, 23 sampai 25, 35 sampai 37) tidak dihitung menurut bagian 3.
- Anchor positif absence (8b butir 2): langkah 7, 10, 13, 24, dan 36 membuktikan surface sudah termuat dengan baris pembanding; langkah 3 (respons) dan langkah 20 (foto tidak berubah) membuktikan pemicu telah diproses server.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 17 dan 28 (membuka My Profile setelah login), 32 (tunggu aksi selesai sebelum ganti akun).
- Temuan untuk QA:
  - TC-GS-PROFILE-224 Expected (a) mengasersi "Respons 200 OK" untuk request langsung; spec mengasersi status itu tanpa tampilan FE (8b butir 1).
  - TC-GS-PROFILE-225 tidak menyebut status respons penolakan; spec tidak mengasersi status dan hanya mengasersi foto tidak berubah serta ketiadaan baris log.
  - TC-GS-PROFILE-226 memakai Pre-setup #11 (Client berbeda) tetapi membaca Activity Log lewat admin Pre-setup #6; TC tidak menyatakan admin Client Storage penuh. Pre-setup #11 juga menulis pemilik akun "Fajar Nugroho" yang sama dengan Pre-setup #10 padahal akun dan Client berbeda; spec memakai "pemilik akun Pre-setup #11".
  - TC-GS-PROFILE-226 tidak menyebut Expected tampilan FE (toast atau pesan) saat Edit Photo ditolak karena Storage penuh; spec tidak mengasersinya.
