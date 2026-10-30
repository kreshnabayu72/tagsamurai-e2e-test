---
id: TC-GS-PROFILE-E2E-031-change-password-lock-1-jam-dan-wajib-reset
title: "Change Password: Lock 1 Jam, Tier Wajib-Reset, dan Tidak Lepas oleh Waktu"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-PROFILE-126
  - TC-GS-PROFILE-127
  - TC-GS-PROFILE-128
  - TC-GS-PROFILE-130
coverage:
  web: automated
---

# Change Password: Lock 1 Jam, Tier Wajib-Reset, dan Tidak Lepas oleh Waktu

## Prerequisites

- Mode: FE+BE (state lock, counter, dan jam server dari backend nyata).
- Suite serial (`parallel: false`): spec mengubah state global (jam server dan jam browser, counter dan lock Change Password akun #7).
- Akun aktor: Pre-setup #7 (Maya Anggraini, Total Control, `passwordProfile_automated_{namaCompany}@qwertysystem.net`, password aktif `Passw0rd!Old` lewat `Spectra.env.GS_PROFILE_PWD_PASSWORD`, Time Format 24 jam, timezone Asia/Jakarta).
- Password baru Data Dinamis #3 (`N3wPassw0rd!`) memakai `Spectra.env.PROFILE_PASSWORD_NEW`. Current Password salah `Wr0ngPass!` ditulis literal karena submit selalu ditolak server.
- Login akun Pre-setup #1 (default suite) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan; S-13): mereset lock akun #7, mengatur counter Change Password ke 5 (tahap 15 menit sudah lewat) dan 8 (tahap 1 jam sudah lewat), dan mengatur jam server serta jam browser ke nilai absolut (09:20, 09:00, dan maju 2 jam ke 11:00).
- State awal tiap blok: TC-GS-PROFILE-126 counter 5, jam 09:20; TC-GS-PROFILE-127 counter 8, jam 09:00; TC-GS-PROFILE-128 dan TC-GS-PROFILE-130 memakai tier wajib-reset yang terbentuk dari TC-GS-PROFILE-127 sejak 09:00.
- Pemulihan di hook `after` spec: jam server dan jam browser ke waktu nyata, counter dan lock akun #7 ke 0.

## Test Steps

### TC-GS-PROFILE-126: Percobaan salah ke-6 mengunci 1 jam

1. Reset lock akun #7, atur counter Change Password ke 5 dengan tahap 15 menit sudah lewat, dan atur jam server dan jam browser ke 09:20
2. Klik [Change Password]
3. Isi Current Password "Wr0ngPass!", New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
4. Klik [Save]
5. Verifikasi toast error: "Error, failed to update your password. Too many failed attempts, please try again at 10:20."
6. Verifikasi tidak ada inline error "Current password is incorrect"
7. Verifikasi [Save] Disabled
8. Verifikasi modal Change Password tetap terbuka
9. Verifikasi Current Password, New Password, dan Confirm New Password tetap terisi
10. Klik [✕]
11. Verifikasi dialog Unsaved Changes tampil
12. Klik [Leave]

### TC-GS-PROFILE-127: Percobaan salah ke-9 masuk tier wajib-reset

13. Reset lock akun #7, atur counter Change Password ke 8 dengan tahap 1 jam sudah lewat, dan atur jam server dan jam browser ke 09:00
14. Klik [Change Password]
15. Isi Current Password "Wr0ngPass!", New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
16. Klik [Save]
17. Verifikasi toast error: "Error, failed to update your password. Too many failed attempts, please reset your password."
18. Verifikasi tidak ada inline error "Current password is incorrect"
19. Verifikasi [Save] Disabled
20. Verifikasi modal Change Password tetap terbuka
21. Verifikasi Current Password, New Password, dan Confirm New Password tetap terisi

### TC-GS-PROFILE-128: Modal dibuka pada tier wajib-reset

22. Klik [✕]
23. Verifikasi dialog Unsaved Changes tampil
24. Klik [Leave]
25. Klik [Change Password]
26. Verifikasi [Save] Disabled sejak modal tampil
27. Hover tombol [Save]
28. Verifikasi tooltip: "Too many failed attempts. Please reset your password."

### TC-GS-PROFILE-130: Tier wajib-reset tidak lepas oleh waktu

29. Klik [✕]
30. Geser jam server dan jam browser 2 jam (ke 11:00)
31. Klik [Change Password]
32. Verifikasi [Save] tetap Disabled
33. Klik [✕]

## Notes

- Kelas harness: d (jam server). Blok TC-GS-PROFILE-128 dan TC-GS-PROFILE-130 memakai tier wajib-reset yang terbentuk dari submit TC-GS-PROFILE-127 (langkah 16); bila tier tidak terbentuk, fixture menyetelnya pada langkah 22 dan 29 sebelum modal dibuka.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 13, 30 (mengatur state dan jam), 10 sampai 12 dan 22 sampai 24 (menutup form dirty sesuai S-08), 29 dan 33 (menutup modal bersih).
- Anchor absence: langkah 5 dan 17 (toast tampil) mendahului langkah 6 dan 18.
- Temuan untuk QA:
  - TC-GS-PROFILE-127 tidak menyebut jam server sedangkan TC-GS-PROFILE-130 menulis tier wajib-reset sejak 09:00; spec memakai 09:00 pada langkah 13.
  - Post Condition tanpa langkah observasi tidak diasersi: TC-GS-PROFILE-126 (terkunci 1 jam sampai 10:20; counter 6) dan TC-GS-PROFILE-127 (wajib reset; counter 9).
