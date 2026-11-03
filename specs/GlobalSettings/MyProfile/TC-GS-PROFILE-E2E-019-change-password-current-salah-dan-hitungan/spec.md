---
id: TC-GS-PROFILE-E2E-019-change-password-current-salah-dan-hitungan
title: "Change Password: Current Password salah, hitungan percobaan, dan urutan evaluasi"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-PROFILE-88
  - TC-GS-PROFILE-89
  - TC-GS-PROFILE-102
  - TC-GS-PROFILE-103
coverage:
  web: automated
---

# Change Password: Current Password salah, hitungan percobaan, dan urutan evaluasi

## Prerequisites

- Mode: FE+BE (backend nyata)
- Akun aktor: Pre-setup #7 `passwordProfile_automated_{namaCompany}@qwertysystem.net` (Maya Anggraini; Total Control; password aktif `Spectra.env.GS_PROFILE_PWD_PASSWORD`; Time Format 24 jam; timezone Asia/Jakarta), kredensial `Spectra.env.GS_PROFILE_PWD_PASSWORD`. Akun ini bukan akun default suite.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke password awal masing-masing (`Spectra.env.GS_PROFILE_PWD_PASSWORD`, `Spectra.env.GS_PROFILE_PWD12H_PASSWORD`, `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`), counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Environment variable: `Spectra.env.GS_PROFILE_PWD_PASSWORD` (login akun #7 di hook `before` spec dan Current Password benar), `Spectra.env.PROFILE_PASSWORD_NEW` (Data Dinamis #3). Password tidak ditulis di spec atau fixture.
- Data input uji (`Fixture.myProfile.changePassword`, literal input yang ditolak, bukan kredensial): `Wr0ngPass!` (Current Password salah) dan `abc` (New Password yang melanggar Password Policy).
- Kemampuan baca state BE (disediakan tim FE/BE, tanpa endpoint karangan): jumlah sesi aktif akun Pre-setup #7. Nilainya dicatat sebagai baseline di langkah pertama dan dibandingkan di setiap `Verifikasi` "tidak ada sesi yang di-invalidate".
- Kemampuan teknis (disediakan tim FE/BE): mengatur counter Change Password akun #7 ke nilai tertentu (0 sebelum TC-GS-PROFILE-88 dan 89), serta mengatur jam server dan jam browser ke waktu absolut. Pilihan spec: jam server dan jam browser diatur bersama ke 09:00 pada tanggal hari run sebelum TC-GS-PROFILE-103, karena TC menulis "tanggal fixture Pre-setup #7" tanpa tanggal (lihat Temuan untuk QA); waktu boleh-coba-lagi 09:15 dihitung server dari jam itu.
- State global yang berubah: counter Change Password akun #7 (menjadi 3 dan terkunci 15 menit di akhir spec) dan jam server serta jam browser. Pemulihan jam, counter, dan password dilakukan hook `after` suite (Hook suite 7); jam dipulihkan sebelum akun aktor membuka log mana pun. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat jumlah sesi aktif akun Pre-setup #7 lewat kemampuan baca state BE sebagai baseline
2. Klik [Change Password]
### Urutan evaluasi: Current salah ditolak sebelum Policy (TC-GS-PROFILE-102)
3. Ketik `Wr0ngPass!` di Current Password
4. Ketik `abc` di New Password
5. Ketik `abc` di Confirm New Password
6. Klik [Save]
7. Verifikasi inline error di bawah Current Password: "Current password is incorrect"
8. Verifikasi tidak ada caption Password Policy di bawah New Password
9. Atur counter Change Password akun #7 ke 0 lewat fixture BE
### Percobaan salah ke-1 (TC-GS-PROFILE-88)
10. Ganti isi New Password dengan `Spectra.env.PROFILE_PASSWORD_NEW`
11. Ganti isi Confirm New Password dengan `Spectra.env.PROFILE_PASSWORD_NEW`
12. Kosongkan isi Current Password lalu ketik ulang `Wr0ngPass!`
13. Klik [Save]
14. Verifikasi inline error di bawah Current Password: "Current password is incorrect"
15. Verifikasi tidak ada toast terkunci
16. Verifikasi [Save] tetap Enabled
17. Verifikasi modal Change Password tetap terbuka
18. Verifikasi jumlah sesi aktif akun #7 sama dengan baseline (tidak ada sesi lain yang di-invalidate)
### Percobaan salah ke-2 tanpa lock (TC-GS-PROFILE-89)
19. Kosongkan isi Current Password lalu ketik ulang `Wr0ngPass!`
20. Klik [Save]
21. Verifikasi inline error di bawah Current Password: "Current password is incorrect"
22. Verifikasi [Save] tetap Enabled
23. Verifikasi tidak ada toast terkunci
### Policy gagal dengan Current benar tidak menaikkan counter (TC-GS-PROFILE-103)
24. Atur jam server dan jam browser ke 09:00 pada tanggal hari run
25. Ganti isi Current Password dengan `Spectra.env.GS_PROFILE_PWD_PASSWORD`
26. Ganti isi New Password dengan `abc`
27. Ganti isi Confirm New Password dengan `abc`
28. Klik [Save]
29. Verifikasi caption Password Policy tampil di bawah New Password
30. Verifikasi tidak ada toast terkunci
31. Ganti isi Current Password dengan `Wr0ngPass!`
32. Ganti isi New Password dengan `Spectra.env.PROFILE_PASSWORD_NEW`
33. Ganti isi Confirm New Password dengan `Spectra.env.PROFILE_PASSWORD_NEW`
34. Klik [Save]
35. Verifikasi toast error: "Error, failed to update your password. Too many failed attempts, please try again at 09:15."
36. Verifikasi percobaan salah ke-3 dijawab terkunci tanpa inline error "Current password is incorrect"
### Menutup modal yang terisi
37. Klik [✕]
38. Verifikasi dialog "Unsaved Changes" dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] serta [Leave]
39. Klik [Leave]

## Notes

- Pembagian TC: TC-GS-PROFILE-88, 89, 102, dan 103 berada di spec ini. TC-GS-PROFILE-84 sampai 87 dan 90 sampai 92 ada di spec 018.
- Urutan TC di dalam spec diubah dari 88, 89, 102, 103 menjadi 102, 88, 89, 103. Alasan: TC-GS-PROFILE-102 mengirim satu percobaan salah dari counter 0, sedangkan TC-GS-PROFILE-88 dan 89 harus mulai dari counter 0 dan 1; TC-GS-PROFILE-103 memakai counter 2 yang dihasilkan langsung oleh TC-GS-PROFILE-88 dan 89 dan berakhir dengan lock 15 menit sehingga harus terakhir. Counter diatur ulang ke 0 sekali, di antara TC-GS-PROFILE-102 dan 88.
- Langkah penghubung (S-03): "Kosongkan isi Current Password lalu ketik ulang" membersihkan inline error identik dari percobaan sebelumnya (R-12); langkah 12 melakukan hal yang sama sebelum submit TC-GS-PROFILE-88 agar inline error TC-GS-PROFILE-102 tidak dibaca sebagai hasil submit baru (R-12). Pada TC-GS-PROFILE-103 `Verifikasi` toast terkunci diletakkan sebelum `Verifikasi` tidak ada inline error "Current password is incorrect" karena toast adalah anchor positif untuk asersi absence tersebut (bagian 8b butir 2). Langkah mengganti isi field sebelum percobaan ke-3 mengikuti langkah uji ke-3 TC-GS-PROFILE-103. Tiga langkah penutup memulihkan form dirty (S-08, S-09).
- Spec ini di atas smell 35 langkah. Alasan: seluruh blok adalah penolakan Current Password dan Policy pada satu modal Change Password dengan akun yang sama; keempat TC berbagi counter yang dibangun berurutan (counter 0 sampai 3) sehingga memisahkannya mengulang login, pembukaan modal, dan pengaturan counter. Blok memakai fixture counter sebagai titik awal sendiri.
- Temuan untuk QA:
  - TC-GS-PROFILE-103: precondition "Jam server digeser ke 09:00 pada tanggal fixture Pre-setup #7" tidak menyebut tanggalnya. Spec memakai tanggal hari run.
  - TC-GS-PROFILE-88, 89, 102, 103: Post Condition counter ("menjadi 1", "2", "1", "3") tidak punya langkah observasi di TC, jadi tidak diasersi.
  - TC-GS-PROFILE-88: Expected "Tidak ada sesi lain yang di-invalidate" tidak memberi cara memeriksa; spec memakai kemampuan baca jumlah sesi aktif akun #7 yang disediakan tim FE/BE.
