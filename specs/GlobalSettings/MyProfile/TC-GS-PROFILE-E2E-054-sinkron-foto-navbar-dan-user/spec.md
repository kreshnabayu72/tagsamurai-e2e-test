---
id: TC-GS-PROFILE-E2E-054-sinkron-foto-navbar-dan-user
title: "Sinkron Foto: Avatar Navbar, User List, dan Detail User Setelah Edit atau Delete Photo"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-238
  - TC-GS-PROFILE-239
  - TC-GS-PROFILE-240
  - TC-GS-PROFILE-241
coverage:
  web: automated
---

# Sinkron Foto: Avatar Navbar, User List, dan Detail User Setelah Edit atau Delete Photo

## Prerequisites

- Mode: FE+BE.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Akun aktor pertama spec: Pre-setup #10 (Fajar Nugroho, Total Control, tanpa foto) `noPhotoProfile_automated_{namaCompany}@qwertysystem.net`, login di hook `before` spec ini dengan `Spectra.env.GS_PROFILE_NOPHOTO_PASSWORD`. Ganti akun ke Pre-setup #9 (Nadia Putri, Total Control, foto aktif `nadia-photo.jpg`) `photoProfile_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_PHOTO_PASSWORD`. Pembaca User List dan Detail User: admin Pre-setup #6 (Hendra Wijaya) `adminActor_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_ADMIN_PASSWORD`, login lewat UI pada langkah ganti akun.
- Env var: `GS_PROFILE_NOPHOTO_PASSWORD`, `GS_PROFILE_PHOTO_PASSWORD`, `GS_PROFILE_ADMIN_PASSWORD`.
- File uji (Pre-setup #17): `valid-photo.png`.
- Kemampuan teknis: hover Avatar; menangani file picker native; fixture BE memulihkan foto profil.
- Pemulihan (R-08): langkah 12 mengembalikan Fajar Nugroho ke keadaan tanpa foto dan langkah 27 memasang kembali `nadia-photo.jpg` sebagai foto aktif Nadia Putri lewat fixture BE; hook `after` suite memulihkan foto #9 dan #10 bila spec gagal di tengah.
- State global yang diubah: foto profil Pre-setup #9 dan #10. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-PROFILE-238: Edit Photo, Avatar navbar ikut berubah

1. Hover Avatar lalu klik `[Edit]`
2. Pilih file `valid-photo.png`
3. Verifikasi Avatar profil di navbar menampilkan foto baru

### TC-GS-PROFILE-240: Edit Photo, User List dan Detail User menampilkan foto baru

4. Tunggu aksi selesai
5. Logout
6. Login sebagai admin Hendra Wijaya (Pre-setup #6)
7. Buka Global Settings > User > User List
8. Ketik Search `Fajar Nugroho`, tekan Enter
9. Verifikasi kolom Name pada User List menampilkan foto baru Fajar Nugroho
10. Buka Detail Fajar Nugroho
11. Verifikasi Avatar Header Detail User menampilkan foto baru
12. Pulihkan Fajar Nugroho ke keadaan tanpa foto lewat fixture BE
13. Logout

### TC-GS-PROFILE-239: Delete Photo, Avatar navbar kembali ke inisial

14. Login sebagai Nadia Putri (Pre-setup #9)
15. Buka My Profile dari account menu navbar
16. Hover Avatar lalu klik `[Delete]`
17. Klik `[Remove]`
18. Verifikasi Avatar profil di navbar menampilkan inisial `NP`

### TC-GS-PROFILE-241: Delete Photo, User List dan Detail User menampilkan inisial

19. Tunggu aksi selesai
20. Logout
21. Login sebagai admin Hendra Wijaya (Pre-setup #6)
22. Buka Global Settings > User > User List
23. Ketik Search `Nadia Putri`, tekan Enter
24. Verifikasi User List menampilkan inisial `NP` untuk Nadia Putri
25. Buka Detail Nadia Putri
26. Verifikasi Avatar Header Detail User menampilkan inisial `NP`
27. Pasang kembali `nadia-photo.jpg` sebagai foto aktif Nadia Putri lewat fixture BE

## Notes

- Mode: FE+BE. Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan: tiap pasangan TC memakai satu aksi yang sama dari sumbernya (TC-GS-PROFILE-238 dan 240 memakai satu Edit Photo oleh Fajar Nugroho pada langkah 1 dan 2; TC-GS-PROFILE-239 dan 241 memakai satu Delete Photo oleh Nadia Putri pada langkah 16 dan 17). Dalam tiap pasangan, asersi navbar di sesi aktor lebih dulu, lalu User List dan Detail User di sesi admin. Tiap pasangan berdiri sendiri; Step ganti akun eksplisit (langkah 5, 6, 13, 14, 20, 21).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 4 dan 19 (tunggu aksi selesai sebelum ganti akun), 8 dan 23 (Search untuk menemukan baris target di User List, R-16), 12 dan 27 (pemulihan foto), 15 (membuka My Profile setelah login Nadia).
- Temuan untuk QA:
  - TC-GS-PROFILE-240 dan 241 Expected menyebut "foto baru" tanpa cara mengamatinya selain tampilnya gambar (bukan inisial); spec mengasersi tampilan foto pada Avatar tanpa membandingkan isi gambar.
  - TC-GS-PROFILE-239 menyebut inisial `NP` untuk Nadia Putri; inisial dua huruf nama depan dan belakang diikuti seperti TC.
