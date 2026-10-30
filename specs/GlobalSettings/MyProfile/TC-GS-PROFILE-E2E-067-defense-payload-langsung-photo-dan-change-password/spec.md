---
id: TC-GS-PROFILE-E2E-067-defense-payload-langsung-photo-dan-change-password
title: "Defense-in-Depth: Payload Edit Photo Tidak Sah (422) dan Request Change Password Langsung (Field-Level, 429)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-PROFILE-122
  - TC-GS-PROFILE-129
  - TC-GS-PROFILE-277
  - TC-GS-PROFILE-278
  - TC-GS-PROFILE-279
  - TC-GS-PROFILE-280
  - TC-GS-PROFILE-281
  - TC-GS-PROFILE-308
coverage:
  web: automated
---

# Defense-in-Depth: Payload Edit Photo Tidak Sah (422) dan Request Change Password Langsung (Field-Level, 429)

## Prerequisites

- Mode: FE+BE.
- Akun aktor (ganti akun eksplisit): Total Control Pre-setup #10 (Fajar Nugroho, tanpa foto) `noPhotoProfile_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.GS_PROFILE_NOPHOTO_PASSWORD`), login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Total Control Pre-setup #7 (Maya Anggraini) `passwordProfile_automated_{namaCompany}@qwertysystem.net` (password aktif `Passw0rd!Old`, `Spectra.env.GS_PROFILE_PWD_PASSWORD`; Time Format 24 jam; timezone Asia/Jakarta). Password baru uji `N3wPassw0rd!` (Data Dinamis #3, `Spectra.env.PROFILE_PASSWORD_NEW`) hanya dipakai pada request yang ditolak. Password tidak ditulis di spec atau fixture.
- File uji Pre-setup #17: `document.pdf`, `animated.gif`, `not-an-image.png` (isi teks), `valid-photo.png`, `incompressible-5mb.png` (5 MB), `1mb-plus-1byte.png` (1.048.577 byte). Input uji yang submit-nya ditolak boleh literal: Confirm New Password `Different1!`.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): memberikan file ke file chooser tanpa filter ekstensi picker (bypass file picker); `Spectra.intercept()` yang mengganti isi request unggahan foto dengan file lain tanpa resize FE; kemampuan membaca status dan isi respons server atas unggahan; klien HTTP yang mengirim request langsung ke server memakai token sesi akun yang login (unggahan Edit Photo dan Change Password); login lewat sesi API aktor untuk memeriksa password lama tanpa mengusir sesi UI; fixture BE jam server absolut (09:05) dan fixture BE lock Change Password tier 15 menit (terkunci sampai 09:15) serta tier wajib-reset (counter 8); fixture BE reset counter Change Password dan Login ke 0.
- State global yang diubah: jam server dan lock Change Password akun #7. Dipulihkan oleh langkah pemulihan di akhir spec dan hook `after` suite. Suite berjalan serial (`parallel: false`).
- Tabel 2, file uji pada blok Edit Photo (langkah 1 sampai 5):

| TC | File |
|---|---|
| TC-GS-PROFILE-277 | `document.pdf` |
| TC-GS-PROFILE-278 | `animated.gif` |
| TC-GS-PROFILE-279 | `not-an-image.png` |

- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Pelaku kedua admin (Pre-setup #6) memicu perubahan state lewat sesi API aktor yang tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE. Lihat `suite.md`, Hook suite 4.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.

## Test Steps

### Edit Photo dengan payload tidak sah, akun Pre-setup #10 (TC-GS-PROFILE-277, 278, 279, 280, 281)

Untuk setiap baris Tabel 2 (langkah 1 sampai 5):

1. Hover Avatar, klik [Edit], berikan file pada kolom "File" ke file chooser tanpa filter ekstensi (bypass file picker)
2. Verifikasi respons server atas unggahan berstatus 422 dengan pesan `Unsupported file format`
3. Verifikasi toast error `Error, failed to update photo.` tampil
4. Verifikasi Avatar tetap menampilkan inisial "FN"
5. Tutup toast Error

TC-GS-PROFILE-280:

6. Pasang intercept yang mengganti isi request unggahan foto dengan `incompressible-5mb.png` tanpa resize FE
7. Hover Avatar, klik [Edit], pilih file `valid-photo.png`
8. Verifikasi respons server atas unggahan berstatus 422
9. Verifikasi toast error `Error, failed to update photo.` tampil
10. Verifikasi Avatar tetap menampilkan inisial "FN"
11. Lepas intercept, lalu tutup toast Error

TC-GS-PROFILE-281:

12. Kirim request unggahan Edit Photo langsung ke server dengan file `1mb-plus-1byte.png` tanpa resize FE
13. Verifikasi respons server berstatus 422
14. Muat ulang halaman My Profile
15. Verifikasi Avatar tetap menampilkan inisial "FN" (foto tidak berubah)

### Request Change Password langsung, akun Pre-setup #7 (TC-GS-PROFILE-308, 122, 129)

16. Ganti akun: klik Logout, lalu login sebagai Pre-setup #7 dengan `Spectra.env.GS_PROFILE_PWD_PASSWORD`, lalu buka My Profile lewat account menu navbar > My Profile

TC-GS-PROFILE-308, langkah 1 dan 2 (tidak terkunci):

17. Kirim request Change Password langsung ke server dengan Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD`, New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Different1!`
18. Verifikasi respons server berupa error field-level pada Confirm New Password
19. Login lewat sesi API aktor akun #7 dengan password lama `Spectra.env.GS_PROFILE_PWD_PASSWORD`
20. Verifikasi login dengan password lama berhasil (password tidak berubah)
21. Kirim request Change Password langsung ke server dengan Current Password, New Password, dan Confirm New Password kosong
22. Verifikasi respons server berupa error field-level pada Current Password, New Password, dan Confirm New Password

TC-GS-PROFILE-308, langkah 3 (terkunci tier 15 menit pada jam server 09:05):

23. Fixture BE mengatur jam server ke 09:05 dan memasang lock tier 15 menit pada Change Password akun #7 (terkunci sampai 09:15) hingga tersimpan
24. Kirim request Change Password langsung ke server dengan Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD`, New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Different1!`
25. Verifikasi respons server berupa error field-level pada Confirm New Password
26. Verifikasi respons server bukan respons terkunci 429
27. Muat ulang halaman My Profile
28. Verifikasi sesi web akun #7 tidak di-invalidate pada ketiga request (My Profile tampil tanpa pengalihan ke halaman Login)

TC-GS-PROFILE-122 (lock tier 15 menit dari langkah 23 masih berlaku):

29. Kirim request Change Password langsung ke server dengan Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD`, New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
30. Verifikasi respons server 429 (terkunci) tanpa memverifikasi Current Password
31. Login lewat sesi API aktor akun #7 dengan password lama `Spectra.env.GS_PROFILE_PWD_PASSWORD`
32. Verifikasi login dengan password lama berhasil (password tidak berubah)
33. Muat ulang halaman My Profile
34. Verifikasi sesi web akun #7 tidak terpengaruh (My Profile tampil tanpa pengalihan ke halaman Login)

TC-GS-PROFILE-129 (tier wajib-reset):

35. Fixture BE mengatur counter Change Password akun #7 ke 8 (tier wajib-reset) hingga tersimpan
36. Kirim request Change Password langsung ke server dengan Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD`, New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
37. Verifikasi respons server 429 tanpa memverifikasi Current Password
38. Login lewat sesi API aktor akun #7 dengan password lama `Spectra.env.GS_PROFILE_PWD_PASSWORD`
39. Verifikasi login dengan password lama berhasil (password tidak berubah dan Login tidak terpengaruh)
40. Muat ulang halaman My Profile
41. Verifikasi sesi web akun #7 tidak terpengaruh (My Profile tampil tanpa pengalihan ke halaman Login)

### Pemulihan state

42. Fixture BE memulihkan jam server ke waktu nyata dan mereset counter Change Password dan Login akun #7 ke 0

## Notes

- Alasan di atas sekitar 35 langkah: seluruh isi spec satu kelas harness (a, defense-in-depth: payload dan request langsung ke server) dengan dua blok yang berdiri sendiri (akun #10 untuk Edit Photo, akun #7 untuk Change Password); kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah 1 sampai 5 diulang untuk 3 baris Tabel 2 (ekspansi 15 langkah). Memecah hanya menambah login, hook, dan cleanup untuk kelas ringan yang sama.
- K-1: TC-GS-PROFILE-122, 129, 277 sampai 281, dan 308 adalah TC defense-in-depth dengan Expected respons API (status respons dan state data) yang tumpang tindih dengan kontrak BE; tetap di spec FE+BE karena TC granular tetap sumber dan tiap TC tepat satu spec. Pada request langsung (TC-GS-PROFILE-122, 129, 281, 308) hanya status respons dan state data yang diasersi (bagian 8b butir 1).
- Pemicu bypass file picker TC-GS-PROFILE-277 sampai 279 dijalankan lewat UI (file chooser tanpa filter ekstensi), sehingga toast dan Avatar ikut diasersi sesuai Expected TC.
- Fixture lock tier 15 menit dan wajib-reset adalah state berat sebagai pemicu TC-GS-PROFILE-122, 129, dan 308 langkah 3; TC-GS-PROFILE-122 memakai lock dari langkah 23 sehingga dibuat sekali.
- Langkah penghubung (S-03): langkah 5 dan 11 menutup toast Error; langkah 14, 27, 33 dan 40 memuat ulang halaman sebagai observasi; langkah 16 mengganti akun; langkah 42 memulihkan jam server dan counter (R-08, S-09).
- Pembagian TC lintas spec: TC-GS-PROFILE-122 dan 129 mengasersi respons request langsung; perilaku UI saat lock ada di spec 029 sampai 031.
- Temuan untuk QA:
  - "Bypass file picker" pada TC-GS-PROFILE-277 sampai 279 tidak menyebut mekanisme dan tidak menyebut apakah FE memvalidasi ekstensi sebelum mengirim; spec mengasumsikan FE tetap mengirim file sehingga respons 422 teramati.
  - TC-GS-PROFILE-308 langkah 1 sampai 3 tidak menyebut Current Password pada langkah 3 selain "benar"; spec memakai `Passw0rd!Old`.
  - Post Condition TC-GS-PROFILE-308 ("Counter Change Password tidak bertambah") dan Post Condition TC-GS-PROFILE-122 tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-GS-PROFILE-122 dan 129 menyebut "Login dan sesi tidak terpengaruh" tanpa cara cek; spec memakai login lewat sesi API aktor dan muat ulang halaman web.
  - Nilai durasi lock 15 menit pada TC-GS-PROFILE-122, 129, dan 308 bertanda PRD? di sumber; spec mengikuti TC.
