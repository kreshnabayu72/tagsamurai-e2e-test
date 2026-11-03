---
id: TC-GS-PROFILE-E2E-062-multi-sesi-race-change-password-dan-user-log
title: "Multi-Sesi: Sesi yang Kalah, Dua Request Bersamaan, dan User Log Logout"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-PROFILE-229
  - TC-GS-PROFILE-295
  - TC-GS-PROFILE-296
  - TC-GS-PROFILE-297
coverage:
  web: automated
---

# Multi-Sesi: Sesi yang Kalah, Dua Request Bersamaan, dan User Log Logout

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #7 (Maya Anggraini) `passwordProfile_automated_{namaCompany}@qwertysystem.net`, password aktif `Spectra.env.GS_PROFILE_PWD_PASSWORD`; password baru `Spectra.env.PROFILE_PASSWORD_NEW` (Data Dinamis #3); password baru kedua untuk sesi B `Spectra.env.PROFILE_PASSWORD_NEW_ALT` (langkah 5 dan 30; bisa diterima server pada race, jadi tidak ditulis literal). Login sesi A di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Admin pembaca User Log: Pre-setup #6 (Hendra Wijaya) `adminActor_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.GS_PROFILE_ADMIN_PASSWORD`), login lewat UI di konteks browser ketiga pada TC-229 karena hasil di UI-nya diasersi. Password tidak ditulis di spec atau fixture.
- Konteks: dua sesi web akun #7 (sesi A konteks browser utama, sesi B konteks browser kedua) dan satu konteks browser ketiga untuk admin (kelas c). Environment mengizinkan dua sesi web bersamaan untuk akun #7. Konteks B dan konteks ketiga ditutup dan sesi loginnya dihapus di akhir tiap blok (S-09).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP yang mengirim dua request Change Password secara paralel dengan token sesi A dan sesi B (TC-296, TC-297); fixture BE reset counter Change Password dan Login ke 0, pengatur counter Change Password ke 1 (TC-297), pemulih password akun #7 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`); kemampuan baca counter dan status lock Change Password akun #7; kemampuan baca jumlah baris User Log Maya Anggraini dengan Activity "Logout" dan Note "Logged out (password changed)" untuk baseline (S-12). Input uji yang ditolak server boleh literal: Current Password salah `Wr0ngPass!`.
- State global yang diubah: password dan counter Change Password akun #7, lock Change Password. Request yang kalah pada TC-296 dapat mengakhiri sesi A atau sesi B, sehingga blok itu paling akhir dan sesi A dipulihkan oleh hook `after`. Dipulihkan oleh langkah pemulihan antar blok dan hook `after` suite. Suite berjalan serial (`parallel: false`).
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`, `Spectra.env.GS_PROFILE_PWD12H_PASSWORD`, `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`), counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.

## Test Steps

### TC-GS-PROFILE-295: Submit Change Password dari sesi yang kalah menampilkan Dialog Password Changed

1. Buka konteks browser kedua (sesi B), login sebagai Pre-setup #7 dengan `Spectra.env.GS_PROFILE_PWD_PASSWORD`, lalu buka My Profile lewat account menu navbar > My Profile
2. Di sesi A dan di sesi B masing-masing klik [Change Password]
3. Di sesi A isi Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD`, New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`, klik [Save]
4. Tunggu aksi selesai di sesi A: modal Change Password tertutup
5. Di sesi B isi Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD`, New Password `Spectra.env.PROFILE_PASSWORD_NEW_ALT`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW_ALT`, klik [Save]
6. Verifikasi sesi B langsung menampilkan dialog `Password Changed` dengan body `Your password has been changed. Please log in again.` dan tombol [OK]
7. Verifikasi sesi B tidak menampilkan toast error maupun inline error
8. Verifikasi modal Change Password di sesi B tertutup
9. Verifikasi counter Change Password akun #7 tetap 0 (submit sesi B tidak diproses)
10. Klik [OK] pada dialog di sesi B, lalu tutup konteks sesi B dan hapus sesi loginnya
11. Fixture BE memulihkan password akun #7 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`) dan mereset counter Change Password dan Login ke 0

### TC-GS-PROFILE-229: Sesi lain yang diakhiri Change Password tercatat di User Log dengan Activity Logout

12. Catat jumlah baris User Log Maya Anggraini dengan Activity "Logout" dan Note "Logged out (password changed)" sebagai baseline L0 (kemampuan baca)
13. Buka konteks browser kedua (sesi B), login sebagai Pre-setup #7 dengan `Spectra.env.GS_PROFILE_PWD_PASSWORD`, lalu buka My Profile lewat account menu navbar > My Profile
14. Di sesi A klik [Change Password], isi Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD`, New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`, klik [Save]
15. Tunggu aksi selesai di sesi A: modal Change Password tertutup
16. Di sesi B pilih opsi lain pada Product Selector hingga dialog `Password Changed` tampil
17. Buka konteks browser ketiga, login sebagai admin Pre-setup #6 dengan `Spectra.env.GS_PROFILE_ADMIN_PASSWORD`
18. Buka Global Settings > User, ketik Search `passwordProfile_automated_{namaCompany}@qwertysystem.net`, tekan Enter, buka Detail Maya Anggraini > Tab "User Log"
19. Verifikasi Tab User Log memuat baris baru Activity "Logout" dengan Note "Logged out (password changed)" untuk sesi B
20. Verifikasi jumlah baris Activity "Logout" dengan Note "Logged out (password changed)" tepat L0 + 1 (satu baris per sesi yang diakhiri)
21. Verifikasi tidak ada baris Logout baru untuk sesi A
22. Tutup konteks ketiga dan konteks sesi B, hapus sesi loginnya, lalu fixture BE memulihkan password akun #7 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`) dan mereset counter Change Password dan Login ke 0

### TC-GS-PROFILE-297: Dua sesi mengirim Current Password salah bersamaan, tiap percobaan dihitung tepat sekali

23. Fixture BE mengatur counter Change Password akun #7 ke 1 hingga tersimpan
24. Buka konteks browser kedua (sesi B) dan login sebagai Pre-setup #7 dengan `Spectra.env.GS_PROFILE_PWD_PASSWORD`
25. Kirim secara paralel dua request Change Password dari sesi A dan sesi B dengan Current Password `Wr0ngPass!`, New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
26. Verifikasi counter Change Password akun #7 menjadi 3 (kedua percobaan dihitung tepat sekali)
27. Verifikasi Change Password akun #7 terkunci tier 15 menit
28. Tutup konteks sesi B dan hapus sesi loginnya, lalu fixture BE mereset counter Change Password dan Login akun #7 ke 0

### TC-GS-PROFILE-296: Dua Change Password valid bersamaan, tepat satu berhasil

29. Buka konteks browser kedua (sesi B) dan login sebagai Pre-setup #7 dengan `Spectra.env.GS_PROFILE_PWD_PASSWORD`
30. Kirim secara paralel dua request Change Password valid dengan Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD`: dari sesi A New Password `Spectra.env.PROFILE_PASSWORD_NEW`, dari sesi B New Password `Spectra.env.PROFILE_PASSWORD_NEW_ALT` (Confirm New Password sama dengan New Password tiap request)
31. Verifikasi tepat satu dari kedua respons berstatus sukses
32. Verifikasi respons request yang kalah ditolak sebagai sesi tidak valid (bukan sebagai Current Password salah)
33. Verifikasi counter Change Password akun #7 tetap 0
34. Tutup konteks sesi B dan hapus sesi loginnya, lalu fixture BE memulihkan password akun #7 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`)

## Notes

- Urutan: TC-GS-PROFILE-295 dan TC-GS-PROFILE-229 mengganti password dengan sesi A tetap aktif; TC-GS-PROFILE-297 (hanya menaikkan counter) mendahului TC-GS-PROFILE-296 karena request yang kalah pada TC-GS-PROFILE-296 dapat mengakhiri sesi A atau sesi B.
- Pembagian TC lintas spec: sifat non-dismissable dialog `Password Changed` dan tombol [OK] ke halaman Login diasersi di spec 061 (TC-GS-PROFILE-293 dan 294); spec ini hanya mengasersi dialog tampil sebagai pengganti toast dan inline error pada TC-GS-PROFILE-295.
- Langkah penghubung (S-03): langkah 4, 15 menunggu aksi selesai (bagian 8b butir 8); langkah 10, 22, 28 dan 34 menutup konteks tambahan (S-09); langkah 11, 22, 28 dan 34 memulihkan password dan counter antar blok; langkah 18 mencari Maya Anggraini lewat Search untuk menemukan baris target (R-16); langkah 12 mencatat baseline User Log (S-12).
- Temuan untuk QA:
  - TC-GS-PROFILE-297 hanya menyebut Current Password `Wr0ngPass!` dan tidak menyebut New Password dan Confirm New Password; spec memakai `Spectra.env.PROFILE_PASSWORD_NEW` untuk keduanya.
  - Post Condition TC-GS-PROFILE-295 ("Password akun `Spectra.env.PROFILE_PASSWORD_NEW`; counter 0") hanya diasersi pada bagian counter (Expected butir c); password aktif tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-GS-PROFILE-296 tidak menyebut kode status respons yang berarti "sesi tidak valid"; spec mengasersi alasan penolakan tanpa angka status.
  - TC-GS-PROFILE-229 tidak menyebut cara membedakan baris Logout sesi A dan sesi B; spec memakai selisih jumlah baris terhadap baseline L0.
