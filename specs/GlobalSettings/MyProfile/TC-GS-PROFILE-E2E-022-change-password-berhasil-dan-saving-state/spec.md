---
id: TC-GS-PROFILE-E2E-022-change-password-berhasil-dan-saving-state
title: "Change Password berhasil: toast, saving state, klik ganda, auto-hide 4 detik, tanpa guard"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-105
  - TC-GS-PROFILE-106
  - TC-GS-PROFILE-109
  - TC-GS-PROFILE-110
  - TC-GS-PROFILE-156
coverage:
  web: automated
---

# Change Password berhasil: toast, saving state, klik ganda, auto-hide 4 detik, tanpa guard

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
- Kemampuan teknis (disediakan tim FE/BE): fixture BE yang memulihkan password akun #7 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`) dan counter ke 0 di antara blok; membaca counter Change Password akun #7 (TC-GS-PROFILE-110 butir c); perekam dialog bawaan browser (`beforeunload`) sehingga munculnya konfirmasi bawaan browser dapat diasersi (TC-GS-PROFILE-156), karena hook `beforeEach` suite mengonfirmasinya secara otomatis.
- Intercept parsial di atas backend nyata (`Spectra.intercept()`) pada request Change Password: TC-GS-PROFILE-109 menahan respons 3 detik lalu melepasnya; TC-GS-PROFILE-110 hanya mencatat jumlah request tanpa menahan. Endpoint tidak disebut TC; mengikuti kontrak modul My Profile dan disediakan tim FE. Intercept dilepas segera setelah dipakai (S-09).
- Jeda nyata pendek: TC-GS-PROFILE-106 menunggu 5 detik (batas auto-hide toast 4 detik) tanpa memanipulasi jam.
- State global yang berubah: tiap blok mengubah password akun #7 menjadi `Spectra.env.PROFILE_PASSWORD_NEW`. Pemulihan ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`) dan counter 0 dilakukan fixture BE di antara blok dan hook `after` suite (Hook suite 7). Suite berjalan serial (`parallel: false`).

## Test Steps

### Berhasil: toast, modal tertutup, sesi tetap aktif, dan toast hilang otomatis (TC-GS-PROFILE-105 dan 106)
1. Klik [Change Password]
2. Ketik `Spectra.env.GS_PROFILE_PWD_PASSWORD` di Current Password
3. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di New Password
4. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di Confirm New Password
5. Klik [Save]
6. Verifikasi toast sukses: "Success, your password has been updated." tampil di kanan bawah
7. Verifikasi modal Change Password tertutup
8. Verifikasi sesi ini tetap aktif: menu navbar dan halaman My Profile tetap tampil dan bisa dipakai
9. Verifikasi tidak ada Dialog "Password Changed"
10. Verifikasi tidak ada toast lain selain toast sukses
11. Tunggu 5 detik
12. Verifikasi toast "Success, your password has been updated." hilang otomatis
13. Pulihkan password akun #7 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`) dan counter Change Password serta Login ke 0 lewat fixture BE
### Saving state (TC-GS-PROFILE-109)
14. Tahan respons request Change Password selama 3 detik lewat intercept
15. Klik [Change Password]
16. Ketik `Spectra.env.GS_PROFILE_PWD_PASSWORD` di Current Password
17. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di New Password
18. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di Confirm New Password
19. Klik [Save]
20. Verifikasi [Save] menampilkan indikator loading
21. Verifikasi [Save] Disabled
22. Verifikasi field input, [Cancel], dan [✕] Disabled selama request berlangsung
23. Lepas tahanan respons request Change Password
24. Verifikasi toast sukses: "Success, your password has been updated."
25. Pulihkan password akun #7 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`) dan counter Change Password serta Login ke 0 lewat fixture BE
### Klik ganda cepat [Save] (TC-GS-PROFILE-110)
26. Pasang pencatat request Change Password tanpa menahan respons
27. Klik [Change Password]
28. Ketik `Spectra.env.GS_PROFILE_PWD_PASSWORD` di Current Password
29. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di New Password
30. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di Confirm New Password
31. Tunggu toast lama hilang otomatis
32. Klik [Save] dua kali dengan cepat
33. Verifikasi hanya satu request Change Password terkirim
34. Verifikasi hanya satu toast "Success, your password has been updated." tampil
35. Verifikasi counter Change Password akun #7 tetap 0 (tidak ada percobaan salah yang tercatat)
36. Lepas pencatat request Change Password
37. Pulihkan password akun #7 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`) dan counter Change Password serta Login ke 0 lewat fixture BE
### Tanpa guard sesudah berhasil (TC-GS-PROFILE-156)
38. Klik [Change Password]
39. Ketik `Spectra.env.GS_PROFILE_PWD_PASSWORD` di Current Password
40. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di New Password
41. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di Confirm New Password
42. Klik [Save]
43. Tunggu modal Change Password tertutup
44. Klik logo di navbar
45. Verifikasi halaman tujuan navigasi navbar tampil
46. Verifikasi tidak ada dialog "Unsaved Changes"
47. Verifikasi tidak ada konfirmasi bawaan browser

## Notes

- Pembagian TC: TC-GS-PROFILE-105, 106, 109, 110, dan 156 berada di spec ini.
- TC-GS-PROFILE-105 dan 106 memiliki precondition dan langkah 1 sampai 3 yang identik, jadi dijalankan sebagai satu blok: Expected TC-GS-PROFILE-105 diasersi saat toast tampil dan Expected TC-GS-PROFILE-106 (toast hilang otomatis sesudah 4 detik) diasersi sesudah jeda 5 detik. Urutan TC di dalam spec diubah dari 105, 106, 109, 110, 156 menjadi 105 bersama 106, 109, 110, 156; TC-GS-PROFILE-156 terakhir karena meninggalkan halaman My Profile.
- Langkah penghubung (S-03): "Pulihkan password ... lewat fixture BE" di antara blok mengembalikan precondition tiap TC (password aktif `Spectra.env.GS_PROFILE_PWD_PASSWORD`, counter 0); "Tunggu toast lama hilang otomatis" sebelum klik ganda memenuhi R-12 untuk asersi "hanya satu toast"; "Tunggu modal Change Password tertutup" mengikuti bagian 8b butir 8 karena langkah berikutnya meninggalkan halaman. Pada TC-GS-PROFILE-156 item navigasi yang dipilih adalah logo di navbar (lihat Temuan untuk QA).
- Spec ini di atas smell 35 langkah. Alasan: seluruh blok satu topik (Change Password berhasil dan perilaku modal serta toast), satu akun, satu kelas harness; empat blok mandiri karena masing-masing dimulai dengan password dan counter dipulihkan fixture, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah terbanyak berasal dari tiga langkah isi field per blok dan satu `Verifikasi` per klausa Expected (S-01).
- Temuan untuk QA:
  - TC-GS-PROFILE-156: langkah uji ke-4 hanya menulis "item navigasi in-app di navbar" tanpa menyebut item; spec memakai logo di navbar (item yang sama dipakai TC-GS-PROFILE-155 dan 309).
  - TC-GS-PROFILE-105: Post Condition "Password akun menjadi `Spectra.env.PROFILE_PASSWORD_NEW`" tidak punya langkah observasi di TC (login dengan password baru diuji di TC-GS-PROFILE-107), jadi tidak diasersi di spec ini. TC-GS-PROFILE-110: Post Condition "Password akun berubah satu kali" juga tidak diasersi.
  - TC-GS-PROFILE-110: Expected "Tidak ada percobaan salah yang tercatat" tidak memberi cara memeriksa; spec memakai kemampuan baca counter Change Password akun #7 yang disediakan tim FE/BE.
