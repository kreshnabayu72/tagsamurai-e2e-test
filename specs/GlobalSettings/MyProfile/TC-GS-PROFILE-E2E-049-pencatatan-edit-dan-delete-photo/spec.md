---
id: TC-GS-PROFILE-E2E-049-pencatatan-edit-dan-delete-photo
title: "Pencatatan Edit Photo dan Delete Photo di Changelog, System Log, dan Activity Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-218
  - TC-GS-PROFILE-219
  - TC-GS-PROFILE-220
  - TC-GS-PROFILE-221
  - TC-GS-PROFILE-222
  - TC-GS-PROFILE-223
coverage:
  web: automated
---

# Pencatatan Edit Photo dan Delete Photo di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Akun aktor pertama spec: Pre-setup #10 (Fajar Nugroho, Total Control, tanpa foto) `noPhotoProfile_automated_{namaCompany}@qwertysystem.net`, login di hook `before` spec ini dengan `Spectra.env.GS_PROFILE_NOPHOTO_PASSWORD`. Ganti akun ke Pre-setup #9 (Nadia Putri, Total Control, foto aktif `nadia-photo.jpg`) `photoProfile_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_PHOTO_PASSWORD`. Pembaca log: admin Pre-setup #6 (Hendra Wijaya) `adminActor_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_ADMIN_PASSWORD`, login lewat UI pada langkah ganti akun.
- Env var: `GS_PROFILE_NOPHOTO_PASSWORD`, `GS_PROFILE_PHOTO_PASSWORD`, `GS_PROFILE_ADMIN_PASSWORD`.
- File uji (Pre-setup #17): `valid-photo.png`.
- Kemampuan teknis: hover Avatar; menangani file picker native; membaca jumlah baris Tab Changelog dan Tab System Log Detail User serta Activity Log sebelum dan sesudah aksi (baseline, S-12; disediakan tim FE/BE karena audit trail permanen tidak bisa diturunkan dari seeding); fixture BE untuk memulihkan foto profil.
- Pemulihan (R-08): langkah 17 mengembalikan Fajar Nugroho ke keadaan tanpa foto dan langkah 39 memasang kembali `nadia-photo.jpg` sebagai foto aktif Nadia Putri lewat fixture BE; hook `after` suite memulihkan foto #9 dan #10 bila spec gagal di tengah. Entri audit trail permanen yang ditambahkan spec tidak dihapus.
- State global yang diubah: foto profil Pre-setup #9 dan #10. Suite berjalan serial (`parallel: false`).

## Test Steps

### Edit Photo oleh Fajar Nugroho

1. Catat baseline lewat kemampuan baca: jumlah baris Tab Changelog dan Tab System Log Detail Fajar Nugroho, serta jumlah baris Field `Photo` Fajar Nugroho di Activity Log
2. Hover Avatar lalu klik `[Edit]`
3. Pilih file `valid-photo.png`
4. Tunggu aksi selesai
5. Logout
6. Login sebagai admin Hendra Wijaya (Pre-setup #6)
7. Buka Global Settings > User > Detail Fajar Nugroho

### TC-GS-PROFILE-218: Edit Photo di Changelog Detail User

8. Buka Tab Changelog
9. Verifikasi jumlah baris Tab Changelog bertambah tepat satu dibanding baseline
10. Verifikasi baris baru: Action `Edit`, Field `Photo`, Old Value `—`, New Value `—`, Modified By `Fajar N`

### TC-GS-PROFILE-219: Edit Photo di System Log Detail User

11. Buka Tab System Log
12. Verifikasi jumlah baris Tab System Log bertambah tepat satu dibanding baseline
13. Verifikasi baris baru: Action `Edit`, Object `User`, Name `Fajar Nugroho`, Field `Photo`, Old Value `—`, New Value `—`

### TC-GS-PROFILE-220: Edit Photo di Activity Log Global Settings

14. Buka Global Settings > Activity Log
15. Verifikasi jumlah baris Field `Photo` Fajar Nugroho di Activity Log bertambah tepat satu dibanding baseline
16. Verifikasi baris Photo baru: Action `Edit`, Object `User`, Name `Fajar Nugroho`, Field `Photo`, Old Value `—`, New Value `—`, Modified By `Fajar N`
17. Kembalikan Fajar Nugroho ke keadaan tanpa foto lewat fixture BE

### Delete Photo oleh Nadia Putri

18. Logout
19. Login sebagai Nadia Putri (Pre-setup #9)
20. Buka My Profile dari account menu navbar
21. Catat baseline lewat kemampuan baca: jumlah baris Tab Changelog dan Tab System Log Detail Nadia Putri, serta jumlah baris Activity Log dengan Name `Nadia Putri` (Field `Photo`) dan Name `nadia-photo.jpg`
22. Hover Avatar lalu klik `[Delete]`
23. Klik `[Remove]`
24. Tunggu aksi selesai
25. Logout
26. Login sebagai admin Hendra Wijaya (Pre-setup #6)
27. Buka Global Settings > User > Detail Nadia Putri

### TC-GS-PROFILE-221: Delete Photo di Changelog Detail User

28. Buka Tab Changelog
29. Verifikasi jumlah baris Tab Changelog bertambah tepat satu dibanding baseline
30. Verifikasi baris baru: Action `Edit`, Field `Photo`, Old Value `—`, New Value `—`, Modified By `Nadia P`

### TC-GS-PROFILE-222: Delete Photo di System Log Detail User

31. Buka Tab System Log
32. Verifikasi jumlah baris Tab System Log bertambah tepat dua dibanding baseline
33. Verifikasi baris Photo: Action `Edit`, Object `User`, Name `Nadia Putri`, Field `Photo`, Old Value `—`, New Value `—`
34. Verifikasi baris sisi File untuk foto lama: Action `Delete`, Name `nadia-photo.jpg`, aktor Nadia Putri (bukan System)

### TC-GS-PROFILE-223: Delete Photo di Activity Log Global Settings

35. Buka Global Settings > Activity Log
36. Verifikasi jumlah baris Activity Log dengan Name `Nadia Putri` (Field `Photo`) dan Name `nadia-photo.jpg` bertambah tepat dua dibanding baseline
37. Verifikasi baris Photo: Action `Edit`, Object `User`, Name `Nadia Putri`, Field `Photo`, Old Value `—`, New Value `—`, Modified By `Nadia P`
38. Verifikasi baris sisi File untuk foto lama: Action `Delete`, Name `nadia-photo.jpg`, Modified By `Nadia P` (bukan System)
39. Pasang kembali `nadia-photo.jpg` sebagai foto aktif Nadia Putri lewat fixture BE

## Notes

- Mode: FE+BE. Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (39 langkah nominal) karena enam TC berada di satu kelas (pencatatan, satu surface log, dua aksi foto) dan dua blok aktor berdiri sendiri (Step ganti akun eksplisit, bagian sesudah ganti akun tetap bermakna walau blok sebelumnya gagal). Enam blok baca-log berpola (langkah 8 sampai 16 dan 28 sampai 38, yaitu buka surface, cari entri, `Verifikasi` kolom log) tidak dihitung menurut bagian 3 sehingga langkah efektif sekitar 22.
- TC-GS-PROFILE-218, 219, dan 220 memakai satu aksi Edit Photo (langkah 2 dan 3) yang sama untuk tiga surface; TC-GS-PROFILE-221, 222, dan 223 memakai satu aksi Delete Photo (langkah 22 dan 23) yang sama untuk tiga surface. Baseline dicatat per surface sebelum aksi (S-12).
- TC-GS-PROFILE-220 menyatakan entri sisi File Manager ber-aktor System tidak diasersi (menunggu OI-01 File Manager); spec tidak mengasersinya.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 4 dan 24 (tunggu aksi selesai sebelum ganti akun), 17 dan 39 (pemulihan foto), 20 (membuka My Profile setelah login Nadia).
- Temuan untuk QA:
  - TC-GS-PROFILE-222 Expected butir (2) menulis "aktor Nadia Putri (bukan System)" tanpa nama kolom di System Log; spec mengasersi aktor pada kolom aktor System Log dan nama kolomnya ditetapkan tim FE di tahap script.
  - TC-GS-PROFILE-218 sampai 220 memakai Pre-setup #10 (Fajar Nugroho) sedangkan TC-GS-PROFILE-221 sampai 223 memakai Pre-setup #9 (Nadia Putri); spec memuat dua blok aktor dengan Step ganti akun.
  - TC-GS-PROFILE-221 sampai 223 mensyaratkan foto aktif `nadia-photo.jpg` sebagai kondisi awal, sehingga pemulihan foto Nadia Putri ditulis di Prerequisites (langkah 39).
