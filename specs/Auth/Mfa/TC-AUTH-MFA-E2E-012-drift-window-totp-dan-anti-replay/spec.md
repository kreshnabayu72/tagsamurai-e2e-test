---
id: TC-AUTH-MFA-E2E-012-drift-window-totp-dan-anti-replay
title: "Drift Window TOTP dan Anti-Replay Kode Authenticator"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-96
  - TC-AUTH-MFA-97
  - TC-AUTH-MFA-98
  - TC-AUTH-MFA-99
coverage:
  web: automated
---

# Drift Window TOTP dan Anti-Replay Kode Authenticator

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): empat user profil NEWDEVE (Tabel Data Uji Pre-setup #5: Activated, Active ON, sudah pernah login sukses di web dari browser uji A (device dikenali), login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari, Authenticator sudah terdaftar dengan secret yang diketahui aplikasi authenticator uji), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-98: `Xena Larasati` (`xenalarasati+{runId}-012@qwertysystem.net`)
  - TC-AUTH-MFA-96: `Vera Kurnia` (`verakurnia+{runId}-012@qwertysystem.net`)
  - TC-AUTH-MFA-97: `Wisnu Aji` (`wisnuaji+{runId}-012@qwertysystem.net`)
  - TC-AUTH-MFA-99: `Yusuf Maulidi` (`yusufmaulidi+{runId}-012@qwertysystem.net`)
- Hook `after`: kembalikan jam aplikasi authenticator uji ke waktu nyata (sinkron dengan jam server uji), hapus keempat user, dan tutup semua jendela privat. Hook ini tetap jalan walau spec gagal di tengah.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah TC pertama dimulai di jendela privat baru; TC pertama berjalan di browser awal; browser awal dan tiap jendela privat tanpa ID device tersimpan, dikenali sebagai browser uji B. Login dari IP uji Jakarta (ID) hanya memicu MFA karena device baru. TC-AUTH-MFA-99 login pertama di jendela privat sebagai browser uji B, lalu jendela itu ditutup dan jendela privat baru dibuka sebagai browser uji C (device baru tambahan; langkah 56), keduanya dipakai berurutan hanya untuk membentuk identitas device. Semua user berprofil NEWDEVE, jadi tiap login Password melewati Choose Verification Method tanpa layar Confirm to Continue.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis, seeding state BE per user: status Activated dan Active ON, trusted device ber-ID device browser uji A (device dikenali), lokasi dan waktu login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari, consent sudah disetujui sehingga tanpa layar Confirm to Continue, dan Authenticator terdaftar dengan secret yang diketahui aplikasi authenticator uji. Mekanisme seeding (endpoint atau skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
- Kemampuan teknis: jendela privat; reCAPTCHA mode uji di environment; aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik, drift window server ±1 step) yang memegang secret tiap user seeding, jamnya dapat digeser maju dan mundur dari spec dan dikembalikan ke waktu nyata, serta jam awalnya sinkron dengan jam server uji; kode yang dicatat dapat dibaca automation.
- Pemulihan state global: jam aplikasi authenticator uji dikembalikan ke waktu nyata di akhir TC-AUTH-MFA-98 dan TC-AUTH-MFA-97 (langkah eksplisit) dan di hook `after` sebagai cadangan. Jam server uji dan jam browser uji tidak diubah.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah jam aplikasi authenticator uji; hook `after` memulihkan jam aplikasi authenticator uji.
- Jeda nyata: TC-AUTH-MFA-96 menunggu aplikasi authenticator uji berpindah ke kode berikutnya, sampai 30 detik (langkah 24), jeda di batas konvensi bagian 6.
- TC-AUTH-MFA-99: kode yang sama harus dipakai pada kedua login dalam satu window drift (kode masih dalam ±1 step server saat login kedua); kedua login dijalankan berurutan tanpa jeda tambahan.

## Test Steps

### TC-AUTH-MFA-98: Kode TOTP yang benar tetapi di luar drift window ditolak

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `xenalarasati+{runId}-012@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
6. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
7. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
8. Putar jam aplikasi authenticator uji 90 detik ke belakang sehingga menampilkan kode 3 step sebelumnya
9. Ketik kode TOTP tersebut pada kotak digit
10. Klik button [Login]
11. Verifikasi Caption error di bawah kotak digit: "Invalid code"
12. Verifikasi Tidak ada sesi yang dibuat
13. Verifikasi Halaman tetap Authenticator Verification
14. Kembalikan jam aplikasi authenticator uji ke waktu nyata

### TC-AUTH-MFA-96: Kode TOTP dari step sebelumnya (30 detik lalu) masih diterima

15. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
16. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
17. Ketik `verakurnia+{runId}-012@qwertysystem.net` pada field Email
18. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
19. Centang widget reCAPTCHA "I'm not a robot"
20. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
21. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
22. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
23. Catat kode TOTP yang tampil pada aplikasi authenticator uji
24. Tunggu sampai aplikasi authenticator uji berpindah ke kode berikutnya (kode yang dicatat menjadi kode step sebelumnya)
25. Ketik kode TOTP yang dicatat pada langkah 23 pada kotak digit
26. Klik button [Login]
27. Verifikasi Verifikasi berhasil (drift window ±1 step)
28. Verifikasi Browser dialihkan ke Portal — Product Hub

### TC-AUTH-MFA-97: Kode TOTP dari step berikutnya (30 detik ke depan) masih diterima

29. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
30. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
31. Ketik `wisnuaji+{runId}-012@qwertysystem.net` pada field Email
32. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
33. Centang widget reCAPTCHA "I'm not a robot"
34. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
35. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
36. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
37. Putar jam aplikasi authenticator uji 30 detik ke depan sehingga menampilkan kode step berikutnya
38. Ketik kode TOTP tersebut pada kotak digit
39. Klik button [Login]
40. Verifikasi Verifikasi berhasil (drift window ±1 step)
41. Verifikasi Browser dialihkan ke Portal — Product Hub
42. Kembalikan jam aplikasi authenticator uji ke waktu nyata

### TC-AUTH-MFA-99: Kode TOTP yang sudah dipakai sukses ditolak saat dipakai ulang pada login berikutnya

43. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
44. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
45. Ketik `yusufmaulidi+{runId}-012@qwertysystem.net` pada field Email
46. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
47. Centang widget reCAPTCHA "I'm not a robot"
48. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
49. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
50. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
51. Catat kode TOTP valid yang tampil pada aplikasi authenticator uji sebagai Kode-A
52. Ketik Kode-A pada kotak digit
53. Klik button [Login]
54. Verifikasi Login pertama berhasil: browser dialihkan ke Portal — Product Hub
55. Logout dari Portal — Product Hub
56. Tutup jendela privat ini, lalu buka jendela privat baru sebagai browser uji C (device baru, tanpa sesi login)
57. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
58. Ketik `yusufmaulidi+{runId}-012@qwertysystem.net` pada field Email
59. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
60. Centang widget reCAPTCHA "I'm not a robot"
61. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
62. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
63. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
64. Ketik Kode-A pada kotak digit (masih dalam drift window)
65. Klik button [Login]
66. Verifikasi Login kedua ditolak: caption "Invalid code" di bawah kotak digit
67. Verifikasi Halaman tetap Authenticator Verification
68. Verifikasi Tidak ada sesi kedua yang dibuat

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Kelas harness d (time-travel jam authenticator uji). Jam yang digeser adalah jam aplikasi authenticator uji, bukan jam server; pemulihannya ada di langkah 14 dan 42 dan di hook `after`.
- Urutan menyimpang dari rencana: TC-AUTH-MFA-98 (ditolak, tidak membuat sesi) dijalankan lebih dulu, lalu TC-AUTH-MFA-96 dan TC-AUTH-MFA-97 (sukses), dan TC-AUTH-MFA-99 (dua login) paling akhir; jam digeser mundur pada TC-AUTH-MFA-98 dan maju pada TC-AUTH-MFA-97 sehingga tiap penggeseran dipulihkan sebelum TC berikutnya (S-05, S-09, S-10).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru, kembalikan jam, logout pada langkah 55, dan penutupan jendela pada langkah 56 supaya browser uji C benar-benar device baru) bukan asersi tambahan (S-03).
- Ukuran spec (smell sekitar 35 langkah): spec ini sekitar 48 langkah setelah langkah prefix login faktor-1 yang identik (buka Login with Password sampai klik [Log in]) tidak dihitung. Tidak dipecah karena keempat TC independen: tiap TC memakai user dan jendela privat sendiri serta mengembalikan jam authenticator uji di akhir TC yang menggesernya, sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Pencatatan pada Post Condition TC-AUTH-MFA-98 dan TC-AUTH-MFA-99 (Failed `Incorrect OTP`) tidak diasersikan di spec ini; asersi pencatatan berada di spec pencatatan.
- Temuan untuk QA: (1) TC-AUTH-MFA-96 Langkah Uji 10 merujuk kode yang dicatat pada "langkah 7", sedangkan pencatatan ada di langkah 8; spec memakai langkah pencatatan sendiri (langkah 23). (2) TC-AUTH-MFA-99 Langkah Uji 10 juga merujuk "langkah 7" (seharusnya langkah 8) dan tidak menyebut batas waktu antar dua login; replay hanya terbukti bila kode masih dalam drift window saat login kedua, jika tidak penolakan berasal dari kode kedaluwarsa dan bukan anti-replay. (3) TC-AUTH-MFA-99 Langkah Uji 9 menggabungkan logout dan pergantian ke browser uji C dalam satu butir; spec memecahnya menjadi logout (langkah 55) dan jendela privat baru (langkah 56). (4) Post Condition tanpa langkah observasi dan tanpa Expected padanan tidak diasersi (S-01): TC-AUTH-MFA-96 "Satu sesi web aktif untuk `Vera Kurnia`" dan TC-AUTH-MFA-97 "Satu sesi web aktif untuk `Wisnu Aji`" (sesi web teramati sebagai Portal tampil pada Expected). (5) Pre-setup TC (#20/#21) belum memuat mekanisme seeding state BE per user (trusted device ber-ID device browser A, lokasi dan waktu login terakhir, secret authenticator yang dikenal authenticator uji, consent, logout web terakhir); mekanisme seed disediakan tim FE/BE.
