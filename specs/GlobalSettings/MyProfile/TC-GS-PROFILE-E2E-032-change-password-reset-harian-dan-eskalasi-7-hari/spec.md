---
id: TC-GS-PROFILE-E2E-032-change-password-reset-harian-dan-eskalasi-7-hari
title: "Change Password: Reset Hitungan Harian per Timezone, Lock Melewati Tengah Malam, dan Eskalasi 7 Hari"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-PROFILE-131
  - TC-GS-PROFILE-132
  - TC-GS-PROFILE-133
  - TC-GS-PROFILE-134
  - TC-GS-PROFILE-135
coverage:
  web: automated
---

# Change Password: Reset Hitungan Harian per Timezone, Lock Melewati Tengah Malam, dan Eskalasi 7 Hari

## Prerequisites

- Mode: FE+BE (state lock, counter, jam server, dan User Log dari backend nyata).
- Suite serial (`parallel: false`): spec mengubah state global (jam server dan jam browser, counter dan lock Change Password akun #7).
- Akun aktor: Pre-setup #7 (Maya Anggraini, Total Control, `passwordProfile_automated_{namaCompany}@qwertysystem.net`, password aktif lewat `Spectra.env.GS_PROFILE_PWD_PASSWORD`, Time Format 24 jam, timezone Asia/Jakarta). Akun pembaca User Log: Pre-setup #6 (Hendra Wijaya, Total Control, `Spectra.env.GS_PROFILE_ADMIN_PASSWORD`) untuk TC-GS-PROFILE-131; ganti akun memakai Step eksplisit.
- Password baru Data Dinamis #3 memakai `Spectra.env.PROFILE_PASSWORD_NEW`. Current Password salah `Wr0ngPass!` ditulis literal karena submit selalu ditolak server.
- Login akun Pre-setup #1 (default suite) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke password awal masing-masing (`Spectra.env.GS_PROFILE_PWD_PASSWORD`, `Spectra.env.GS_PROFILE_PWD12H_PASSWORD`, `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`), counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan; S-13): (a) mereset lock dan mengatur counter Change Password akun #7; (b) memasang lock tier 15 menit dengan waktu mulai tertentu; (c) memasang riwayat tujuh hari berturut-turut mencapai lock 1 jam pada counter Change Password; (d) mengatur jam server dan jam browser ke nilai absolut (UTC dan WIB) dan memulihkannya; (e) membaca jumlah entri User Log akun #7; (f) menangani dialog `beforeunload` saat muat ulang dengan form dirty (S-08).
- Tanggal untuk semua nilai jam adalah tanggal fixture Pre-setup #7 (TC tidak menyebut tanggal; lihat Temuan untuk QA).
- Jam server dan jam browser diatur bersama dan dibekukan pada nilai yang diset. Jam dipulihkan sebelum admin membuka User Log (S-09, langkah 35).
- Pemulihan di hook `after` spec: jam server dan jam browser ke waktu nyata, counter dan lock akun #7 ke 0.

## Test Steps

1. Catat baseline jumlah entri User Log akun #7 dengan Note "Account locked (change password)"

### TC-GS-PROFILE-132: Pergantian hari menurut timezone user mereset hitungan

2. Reset lock akun #7, atur counter Change Password ke 2, dan atur jam server dan jam browser ke 16:50 UTC (23:50 WIB)
3. Muat ulang halaman (F5)
4. Geser jam server dan jam browser ke 17:10 UTC (00:10 WIB hari berikutnya)
5. Klik [Change Password]
6. Isi Current Password "Wr0ngPass!", New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
7. Klik [Save]
8. Verifikasi inline error "Current password is incorrect"
9. Verifikasi tidak ada toast terkunci

### TC-GS-PROFILE-133: Pergantian hari UTC tanpa pergantian hari timezone user

10. Reset lock akun #7, atur counter Change Password ke 2, dan atur jam server dan jam browser ke 23:50 UTC (06:50 WIB)
11. Muat ulang halaman (F5) dan terima konfirmasi bawaan browser
12. Geser jam server dan jam browser ke 00:10 UTC hari berikutnya (07:10 WIB, tanggal WIB sama)
13. Klik [Change Password]
14. Isi Current Password "Wr0ngPass!", New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
15. Klik [Save]
16. Verifikasi toast error: "Error, failed to update your password. Too many failed attempts, please try again at 07:25."
17. Verifikasi tidak ada inline error "Current password is incorrect"

### TC-GS-PROFILE-134: Lock 15 menit tetap berlaku melewati tengah malam

18. Reset lock akun #7, pasang lock tier 15 menit mulai 23:55 WIB sampai 00:10 WIB hari berikutnya, dan atur jam server dan jam browser ke 23:55 WIB
19. Muat ulang halaman (F5) dan terima konfirmasi bawaan browser
20. Geser jam server dan jam browser ke 00:05 WIB hari berikutnya
21. Klik [Change Password]
22. Verifikasi [Save] masih Disabled pada 00:05 WIB

### TC-GS-PROFILE-131: Eskalasi 7 hari

23. Reset lock akun #7, pasang riwayat tujuh hari berturut-turut mencapai lock 1 jam pada counter Change Password, dan atur jam server dan jam browser ke 09:00 pada hari ke-8
24. Muat ulang halaman (F5)
25. Klik [Change Password]
26. Isi Current Password "Wr0ngPass!", New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
27. Klik [Save]
28. Verifikasi toast error: "Error, failed to update your password. Too many failed attempts, please reset your password."
29. Verifikasi [Save] Disabled

### TC-GS-PROFILE-135: Tier wajib-reset tidak ter-reset oleh pergantian hari

30. Muat ulang halaman (F5) dan terima konfirmasi bawaan browser; tier wajib-reset dari langkah 27 tetap berlaku
31. Geser jam server dan jam browser ke hari berikutnya 00:10 WIB
32. Klik [Change Password]
33. Verifikasi [Save] masih Disabled
34. Klik [✕]

### TC-GS-PROFILE-131: Note User Log

35. Pulihkan jam server dan jam browser ke waktu nyata
36. Klik Logout
37. Login dengan akun Pre-setup #6 (`Spectra.env.GS_PROFILE_ADMIN_PASSWORD`)
38. Buka User Detail akun #7 > Tab User Log (Global Settings > User, Search email akun #7)
39. Cari entri User Log akun #7 dengan Note "Account locked (change password)" berdasarkan Note dan email, bukan posisi teratas
40. Verifikasi entri tersebut memuat Note "Account locked (change password)"
41. Verifikasi jumlah entri User Log akun #7 dengan Note "Account locked (change password)" lebih banyak daripada baseline pada langkah 1

## Notes

- Kelas harness: d (jam server, time-travel). Spec melewati sekitar 35 langkah (41 langkah nominal; blok baca-log berpola tidak dihitung). Alasan: seluruh blok berkelas d yang sama dan memakai fixture jam dan lock yang sama; tiap blok mengatur ulang lock, counter, dan jam sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; ganti akun (langkah 36 dan 37) memakai Step eksplisit dan bagian sesudahnya tetap bermakna.
- Urutan kasus di spec (132, 133, 134, 131, 135) mengikuti state lock: TC-GS-PROFILE-131 membentuk tier wajib-reset permanen yang dipakai TC-GS-PROFILE-135 dan harus sesudah kasus yang membutuhkan lock tidak wajib-reset (S-05). Pembacaan User Log TC-GS-PROFILE-131 dilakukan di akhir setelah jam dipulihkan (langkah 35 sampai 41).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 2, 4, 10, 12, 18, 20, 23, 31 (mengatur state dan jam), 3, 11, 19, 24, 30 (muat ulang agar state lock dibaca; form dirty dari kasus sebelumnya ditangani lewat kemampuan `beforeunload`, S-08), 34 (menutup modal bersih), 35 sampai 37 (pemulihan jam dan ganti akun), dan 39 (mencari entri; Search disebut dalam langkah 38).
- Baseline log (S-12): langkah 1 dicatat sebelum aksi pertama; entri bercap waktu geser sehingga langkah 39 mencari berdasarkan Note dan email dan langkah 41 membandingkan jumlah entri terhadap baseline.
- Anchor absence: langkah 8 dan 16 (inline error atau toast tampil) mendahului langkah 9 dan 17.
- Temuan untuk QA:
  - TC-GS-PROFILE-131 mengharapkan Note User Log (Expected c) tanpa langkah membaca User Log dan tanpa menyebut akun pembaca; spec memakai admin Pre-setup #6 seperti TC-GS-PROFILE-119 (langkah 36 sampai 41).
  - TC-GS-PROFILE-132, 133, 134, 135, dan 131 tidak menyebut tanggal untuk jam server; spec memakai tanggal fixture Pre-setup #7. TC-GS-PROFILE-134 tidak menyebut jam awal pasang lock selain "lock mulai 23:55 WIB".
  - Post Condition tanpa langkah observasi tidak diasersi: TC-GS-PROFILE-131 (terkunci permanen sampai Reset Password), TC-GS-PROFILE-132 (counter 1), dan TC-GS-PROFILE-133 (counter 3).
