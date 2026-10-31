---
id: TC-GS-PROFILE-E2E-029-change-password-lock-state-modal-dan-tooltip-save
title: "Change Password: [Save] Disabled saat Modal Dibuka Terkunci, Tooltip, Loading Baca Lock, dan Fail-Open"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-PROFILE-44
  - TC-GS-PROFILE-116
  - TC-GS-PROFILE-120
  - TC-GS-PROFILE-121
  - TC-GS-PROFILE-139
  - TC-GS-PROFILE-326
  - TC-GS-PROFILE-327
coverage:
  web: automated
---

# Change Password: [Save] Disabled saat Modal Dibuka Terkunci, Tooltip, Loading Baca Lock, dan Fail-Open

## Prerequisites

- Mode: FE+BE (intercept parsial baca status lock di atas backend nyata untuk TC-GS-PROFILE-326 dan TC-GS-PROFILE-327; request submit Change Password tidak diintersep).
- Suite serial (`parallel: false`): spec mengubah state global (jam server dan jam browser, counter dan lock Change Password akun #7).
- Akun aktor: Pre-setup #7 (Maya Anggraini, Total Control, `passwordProfile_automated_{namaCompany}@qwertysystem.net`, password aktif `Passw0rd!Old` lewat `Spectra.env.GS_PROFILE_PWD_PASSWORD`, Time Format 24 jam, timezone Asia/Jakarta).
- Password baru Data Dinamis #3 (`N3wPassw0rd!`) memakai `Spectra.env.PROFILE_PASSWORD_NEW`. Current Password salah `Wr0ngPass!` ditulis literal karena submit selalu ditolak server.
- Login akun Pre-setup #1 (default suite) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Sesi API aktor: login API untuk akun #7 tidak dihitung sebagai sesi web dan dipakai untuk memeriksa password lama pada langkah 47. Lihat `suite.md`, Hook suite 4.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan; S-13): (a) mengatur counter dan mereset lock akun #7; (b) mengatur jam server dan jam browser ke nilai absolut; (c) menahan respons baca status lock 3 detik dan memaksanya 500 lewat `Spectra.intercept()` (endpoint baca status lock tidak disebut TC; ditentukan tim FE di tahap script); (d) menunggu 30 detik nyata pada langkah 23 (jeda pendek eksplisit, bagian 6); (e) Tab keyboard fokus pada [Save] Disabled.
- Pemulihan di hook `after` spec: semua intercept dilepas walau spec gagal di tengah, jam server dan jam browser ke waktu nyata, counter dan lock akun #7 ke 0.

## Test Steps

### TC-GS-PROFILE-326: Loading state saat membaca status lock

1. Pasang intercept pada respons baca status lock: tahan 3 detik
2. Klik [Change Password]
3. Verifikasi modal Change Password terbuka
4. Verifikasi [Save] Disabled
5. Verifikasi [Save] menampilkan loading state selama pembacaan berlangsung
6. Verifikasi [Cancel] Enabled
7. Lepaskan respons yang ditahan dan lepas intercept baca status lock
8. Verifikasi [Save] Enabled
9. Verifikasi loading state pada [Save] hilang
10. Klik [✕]

### TC-GS-PROFILE-139: Status lock dibaca ulang setelah submit ditolak

11. Atur counter Change Password akun #7 ke 2, dan atur jam server dan jam browser ke 09:00 pada tanggal fixture Pre-setup #7
12. Klik [Change Password]
13. Isi Current Password "Wr0ngPass!", New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
14. Klik [Save]
15. Tunggu toast terkunci tampil
16. Verifikasi [Save] Disabled
17. Klik [✕]
18. Verifikasi dialog Unsaved Changes tampil
19. Klik [Leave]

### TC-GS-PROFILE-116: Teks jam pada tooltip [Save] statis

20. Klik [Change Password]
21. Hover tombol [Save]
22. Verifikasi tooltip: "Too many failed attempts. You can try again at 09:15."
23. Tunggu 30 detik dengan modal tetap terbuka
24. Pindahkan pointer keluar dari [Save], lalu hover tombol [Save] lagi
25. Verifikasi tooltip tetap "Too many failed attempts. You can try again at 09:15."
26. Verifikasi tooltip tidak berubah menjadi hitungan mundur

### TC-GS-PROFILE-44: Tooltip terbaca lewat keyboard focus

27. Pindahkan pointer keluar dari [Save]
28. Tekan Tab sampai fokus di [Save]
29. Verifikasi tooltip alasan tampil saat [Save] menerima keyboard focus

### TC-GS-PROFILE-120 dan TC-GS-PROFILE-121: Modal dibuka saat terkunci

30. Klik [✕]
31. Pastikan Change Password akun #7 terkunci tier 15 menit sampai 09:15 dan atur jam server dan jam browser ke 09:05
32. Klik [Change Password]
33. Verifikasi [Save] Disabled sejak modal tampil
34. Verifikasi [Cancel] Enabled
35. Verifikasi Current Password, New Password, dan Confirm New Password Enabled sehingga dapat diisi
36. Hover tombol [Save]
37. Verifikasi tooltip: "Too many failed attempts. You can try again at 09:15."

### TC-GS-PROFILE-327: Baca status lock gagal (fail-open)

38. Klik [✕]
39. Pasang intercept pada respons baca status lock: jawab 500 (request submit tidak diintersep)
40. Klik [Change Password]
41. Verifikasi modal Change Password tetap terbuka
42. Verifikasi [Save] Enabled
43. Lepas intercept baca status lock
44. Isi Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD`, New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
45. Klik [Save]
46. Verifikasi toast error: "Error, failed to update your password. Too many failed attempts, please try again at 09:15."
47. Verifikasi password tidak berubah: login API dengan `Passw0rd!Old` (`Spectra.env.GS_PROFILE_PWD_PASSWORD`) berhasil
48. Verifikasi modal Change Password tetap terbuka
49. Verifikasi Current Password, New Password, dan Confirm New Password tetap terisi
50. Klik [✕]
51. Verifikasi dialog Unsaved Changes tampil
52. Klik [Leave]

## Notes

- Kelas harness: d (lock dan jam server). P-5 (butir b): TC-GS-PROFILE-327 adalah satu objek uji ringan kelas b (satu kegagalan 500 pada baca status lock di atas backend nyata) pada permukaan yang sama (state lock [Save]); TC-GS-PROFILE-326 hanya menahan respons untuk mengamati loading dan bukan kelas b.
- Spec melewati sekitar 35 langkah (52 langkah nominal). Alasan: seluruh blok memakai satu state lock tier 15 menit akun #7 dan satu fixture jam, sehingga memecahnya mengulang login, fixture, dan penutupan modal tanpa memisahkan kelas harness; tiap blok mengatur state-nya sendiri (langkah 11, 31, 39) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Lock tier 15 menit yang dipakai TC-GS-PROFILE-116, 44, 120, 121, dan 327 terbentuk dari submit TC-GS-PROFILE-139 (langkah 14); langkah 31 memastikannya lewat fixture. Modal dari langkah 20 dipakai ulang oleh TC-GS-PROFILE-44 (state identik, bersih) dan modal dari langkah 32 dipakai ulang oleh TC-GS-PROFILE-121 (langkah 1 TC identik dengan TC-GS-PROFILE-120).
- Urutan kasus di spec (326, 139, 116, 44, 120 dan 121, 327) mengikuti state lock, bukan urutan nomor TC (S-05).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 10, 17, 30, 38, dan 50 (menutup modal), 11 dan 31 (mengatur state), 15 (menunggu toast), 18 sampai 19 dan 51 sampai 52 (menutup form dirty sesuai S-08), 23, 24, 27 (jeda dan pointer), 43 (melepas intercept).
- Temuan untuk QA:
  - TC-GS-PROFILE-44 tidak menyebut teks tooltip; spec mengasersi tooltip alasan tampil tanpa teks.
  - TC-GS-PROFILE-120 menulis "Field dapat diisi" tanpa langkah mengetik; spec mengasersi ketiga field Enabled (langkah 35).
  - TC-GS-PROFILE-327 tidak menyebut cara memeriksa "login dengan `Passw0rd!Old` masih berhasil"; spec memakai login API sesi aktor (Hook suite 4). Post Condition counter tidak bertambah tidak diasersi (tanpa langkah observasi).
  - TC-GS-PROFILE-116 menetapkan jeda 30 detik nyata pada jam server yang berjalan; tooltip tetap 09:15 selama jam server < 09:15.
