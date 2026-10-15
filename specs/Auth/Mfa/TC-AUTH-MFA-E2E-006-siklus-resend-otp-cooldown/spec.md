---
id: TC-AUTH-MFA-E2E-006-siklus-resend-otp-cooldown
title: "Siklus Resend OTP dan Cooldown 60 Detik"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-76
  - TC-AUTH-MFA-77
  - TC-AUTH-MFA-78
  - TC-AUTH-MFA-80
  - TC-AUTH-MFA-81
coverage:
  web: automated
---

# Siklus Resend OTP dan Cooldown 60 Detik

## Prerequisites

- Mode: FE+BE.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah jam server uji dan jam browser uji; hook `after` memulihkan jam server uji dan jam browser uji ke waktu nyata.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): lima user profil NEWDEV (Tabel Data Uji Pre-setup #4: Activated, Active ON, sudah pernah login sukses di web, Authenticator belum terdaftar; TC pertama berjalan di browser awal; browser awal dan tiap jendela privat tanpa ID device tersimpan, dikenali sebagai browser uji B; login dari browser uji B memicu MFA karena ID device belum dikenali; tanpa layar Confirm to Continue), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-77: `Gita Purnama` (`gitapurnama+{runId}-006@qwertysystem.net`)
  - TC-AUTH-MFA-76: `Edo Pramudya` (`edopramudya+{runId}-006@qwertysystem.net`)
  - TC-AUTH-MFA-81: `Laras Setyowati` (`larassetyowati+{runId}-006@qwertysystem.net`)
  - TC-AUTH-MFA-80: `Kevin Ardiansyah` (`kevinardiansyah+{runId}-006@qwertysystem.net`)
  - TC-AUTH-MFA-78: `Hasan Basri` (`hasanbasri+{runId}-006@qwertysystem.net`)
- Hook `after`: hapus kelima user (beserta sesi web yang terbentuk dari TC-AUTH-MFA-80 dan 78) dan pulihkan jam server uji dan jam browser uji ke waktu nyata. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah TC pertama dimulai di jendela privat baru.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Jendela privat; reCAPTCHA mode uji di environment; muat ulang halaman (F5) dengan sesi pre-auth tetap aktif.
  - Mail-catcher lingkungan uji untuk membaca tiap kode OTP faktor-2 beserta urutan kedatangannya dan menghitung jumlah email; asersi "email baru" dan "tidak ada email baru" memakai baseline jumlah email untuk email user yang dicatat sebelum aksi yang diamati.
  - Manipulasi jam (K§6): langkah "Majukan jam server uji dan jam browser uji N detik" menggeser jam server dan jam browser/klien bersama, karena hitung mundur Resend berjalan di jam klien; langkah "Pulihkan jam server uji dan jam browser uji ke waktu nyata" ada di akhir tiap TC yang menggesernya (TC-AUTH-MFA-77, 76, 81, 78), dengan hook `after` sebagai cadangan. Mekanisme pengaturan jam disediakan tim FE/BE; Pre-setup #20 hanya menyebut manipulasi jam server.
  - Jeda nyata ≤30 detik: menunggu 10 detik agar hitung mundur turun (langkah 11) dan menunggu toast hilang otomatis 4 detik (langkah 89).
  - Pembacaan hitungan resend sesi pre-auth (TC-AUTH-MFA-80 butir c, TC-AUTH-MFA-81 butir c; langkah 49 dan 70): mekanisme baca disediakan tim FE/BE karena hitungan itu tidak terlihat di UI dan tidak didefinisikan sebagai endpoint baca di TC, PRD, atau LLD.
  - Seeding state BE per user: riwayat login web sukses dengan trusted device ber-ID device browser uji A untuk kelima user; mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
- Tiap TC harus selesai dalam TTL sesi pre-auth 10 menit sejak Log in, termasuk pergeseran jam 60 detik yang dipakainya.

## Test Steps

### TC-AUTH-MFA-77: Button Resend disabled dengan hitung mundur di dalam label selama cooldown lalu aktif

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `gitapurnama+{runId}-006@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
6. Pilih opsi "OTP via email" pada halaman Choose Verification Method
7. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `gitapurnama+{runId}-006@qwertysystem.net`
8. Amati button Text pada area Resend segera setelah halaman tampil
9. Verifikasi Button Text disabled
10. Verifikasi Label "Resend code in Ns" dengan N maksimal 60
11. Tunggu 10 detik lalu amati ulang label button
12. Verifikasi Label menunjukkan N yang lebih kecil sekitar 10 detik dari sebelumnya (hitung mundur berjalan di dalam label)
13. Muat ulang halaman (F5)
14. Verifikasi Hitung mundur melanjutkan dari sisa waktu menurut waktu server (N lebih kecil dari nilai sebelum muat ulang, bukan mulai ulang dari 60 detik)
15. Majukan jam server uji dan jam browser uji 60 detik
16. Verifikasi Button berlabel "Resend code"
17. Verifikasi Button enabled
18. Pulihkan jam server uji dan jam browser uji ke waktu nyata

### TC-AUTH-MFA-76: Kode OTP lama ditolak setelah Resend menerbitkan kode baru

19. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
20. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
21. Ketik `edopramudya+{runId}-006@qwertysystem.net` pada field Email
22. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
23. Centang widget reCAPTCHA "I'm not a robot"
24. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
25. Pilih opsi "OTP via email" pada halaman Choose Verification Method
26. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `edopramudya+{runId}-006@qwertysystem.net`
27. Catat kode OTP pertama dari email `edopramudya+{runId}-006@qwertysystem.net`
28. Majukan jam server uji dan jam browser uji 60 detik
29. Klik button [Resend code]
30. Ketik kode OTP pertama pada kotak digit
31. Verifikasi Kode pertama ditolak walau belum lewat 5 menit
32. Verifikasi Tidak ada sesi yang dibuat (Portal tidak tampil)
33. Verifikasi Caption error di bawah kotak digit: "Invalid code"
34. Pulihkan jam server uji dan jam browser uji ke waktu nyata

### TC-AUTH-MFA-81: Memilih OTP via email lagi setelah cooldown dihitung sebagai resend dan membatalkan kode lama

35. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
36. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
37. Ketik `larassetyowati+{runId}-006@qwertysystem.net` pada field Email
38. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
39. Centang widget reCAPTCHA "I'm not a robot"
40. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
41. Pilih opsi "OTP via email" pada halaman Choose Verification Method
42. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `larassetyowati+{runId}-006@qwertysystem.net`
43. Klik button Text [Use a different method]
44. Majukan jam server uji dan jam browser uji 60 detik (sejak pengiriman pertama)
45. Catat jumlah email di mail-catcher untuk `larassetyowati+{runId}-006@qwertysystem.net` sebagai baseline
46. Pilih opsi "OTP via email" lalu klik button [Login]
47. Verifikasi Halaman `Auth > MFA > OTP Verification` tampil
48. Verifikasi Email OTP kedua diterima di `larassetyowati+{runId}-006@qwertysystem.net` (jumlah email bertambah satu dari baseline)
49. Verifikasi Pilihan ini dihitung sebagai resend: hitungan resend sesi pre-auth bertambah satu
50. Verifikasi Cooldown 60 detik berlaku lagi: button Text [Resend code in Ns] disabled
51. Verifikasi Cooldown 60 detik berlaku lagi: N pada label maksimal 60
52. Ketik kode OTP pertama pada kotak digit
53. Verifikasi Kode pertama ditolak
54. Verifikasi Tidak ada sesi yang dibuat (Portal tidak tampil)
55. Pulihkan jam server uji dan jam browser uji ke waktu nyata

### TC-AUTH-MFA-80: Memilih OTP via email lagi saat cooldown masih berjalan tidak mengirim OTP baru

56. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
57. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
58. Ketik `kevinardiansyah+{runId}-006@qwertysystem.net` pada field Email
59. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
60. Centang widget reCAPTCHA "I'm not a robot"
61. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
62. Pilih opsi "OTP via email" pada halaman Choose Verification Method
63. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `kevinardiansyah+{runId}-006@qwertysystem.net`
64. Klik button Text [Use a different method] sebelum hitung mundur selesai
65. Catat jumlah email di mail-catcher untuk `kevinardiansyah+{runId}-006@qwertysystem.net` sebagai baseline
66. Pilih opsi "OTP via email" lalu klik button [Login]
67. Verifikasi Halaman `Auth > MFA > OTP Verification` tampil lagi
68. Verifikasi Tidak ada email OTP baru yang terkirim ke `kevinardiansyah+{runId}-006@qwertysystem.net` (jumlah email sama dengan baseline)
69. Verifikasi Hitung mundur pada button Resend melanjutkan dari sisa cooldown (bukan mulai ulang dari 60 detik)
70. Verifikasi Hitungan resend tidak bertambah
71. Ketik kode OTP faktor-2 dari satu-satunya email `kevinardiansyah+{runId}-006@qwertysystem.net` pada kotak digit
72. Verifikasi Kode terakhir tetap berlaku: verifikasi berhasil
73. Verifikasi Browser dialihkan ke Portal — Product Hub (Portal tampil menandakan sesi web aktif untuk `Kevin Ardiansyah`)

### TC-AUTH-MFA-78: Resend menerbitkan kode OTP baru yang dapat dipakai untuk verifikasi

74. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
75. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
76. Ketik `hasanbasri+{runId}-006@qwertysystem.net` pada field Email
77. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
78. Centang widget reCAPTCHA "I'm not a robot"
79. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
80. Pilih opsi "OTP via email" pada halaman Choose Verification Method
81. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `hasanbasri+{runId}-006@qwertysystem.net`
82. Catat kode OTP pertama dari email `hasanbasri+{runId}-006@qwertysystem.net`
83. Majukan jam server uji dan jam browser uji 60 detik
84. Catat jumlah email di mail-catcher untuk `hasanbasri+{runId}-006@qwertysystem.net` sebagai baseline
85. Klik button [Resend code]
86. Verifikasi Email OTP kedua diterima di `hasanbasri+{runId}-006@qwertysystem.net` (jumlah email bertambah satu dari baseline)
87. Verifikasi Kode pada email kedua berbeda dari kode pertama
88. Verifikasi Toast sukses: "Success, the code has been sent." tampil setelah klik [Resend code]
89. Verifikasi Toast hilang otomatis setelah 4 detik
90. Ketik 6 digit kode OTP kedua dari email terbaru pada kotak digit
91. Verifikasi Verifikasi dengan kode kedua berhasil
92. Verifikasi Browser dialihkan ke Portal — Product Hub
93. Pulihkan jam server uji dan jam browser uji ke waktu nyata

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal tiap TC setelah TC pertama; mengetik digit kode lama atau kode terbaru yang diperlukan Expected; mencatat kode OTP pertama dan baseline jumlah email; mengatur dan memulihkan jam) bukan asersi tambahan (S-03, S-09, S-12).
- Penyimpangan urutan (S-05, S-10): TC sumber berurut 76, 77, 78, 80, 81; spec memakai 77 (screening cooldown), 76 dan 81 (kode lama ditolak), 80 (berujung login sukses), lalu 78 (Resend yang berhasil dan login sukses) paling akhir. Dalam TC-AUTH-MFA-81, butir c Expected (hitungan resend dan cooldown) dicek sebelum mengetik kode pertama (butir b) supaya hitung mundur 60 detik belum berjalan jauh.
- Penantian cooldown 60 detik dan jeda 60 detik di TC sumber (TC-AUTH-MFA-77 Langkah 10, 76 Langkah 9, 81 Langkah 9, 78 Langkah 8) diwujudkan sebagai pengaturan jam (K§6): jam server dan jam browser digeser 60 detik bersama, dipulihkan di akhir TC. TC-AUTH-MFA-80 tidak menggeser jam.
- Browser/jendela privat berbeda dipakai berurutan hanya untuk membentuk identitas device (browser uji B), tanpa asersi lintas jendela; bukan konteks kedua (tidak butuh butir P-2).
- Pembagian TC lintas spec: Post Condition pencatatan (Failed `Incorrect OTP` pada TC-AUTH-MFA-76; "Resend tidak menghasilkan entri log" pada TC-AUTH-MFA-78 yang bertanda "detail pada TC Logging") tidak diasersi di spec fungsional ini (S-05). Kuota Resend 5 kali dan kegagalan 5xx pada Resend dicakup spec lain.
- Posisi toast: TC-AUTH-MFA-78 Expected b menyebut toast tampil dan hilang otomatis setelah 4 detik tanpa menyebut posisi, sehingga posisi "kanan bawah" tidak diasersi di spec ini; posisi toast Resend diasersi pada TC-AUTH-MFA-56 Expected d di spec 002.
- Ukuran spec (smell sekitar 35 langkah): spec ini sekitar 69 langkah setelah langkah prefix login faktor-1 yang identik (buka Login with Password sampai klik [Log in]) tidak dihitung. Tidak dipecah karena kelima TC independen: tiap TC memakai user dan jendela privat sendiri serta memulihkan jam di akhir, sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA: (1) TC-AUTH-MFA-77 Expected d ("setelah muat ulang halaman (F5) hitung mundur melanjutkan dari sisa waktu") tidak punya langkah F5 di Langkah Uji, dan setelah hitung mundur selesai (langkah 10 TC) tidak ada hitung mundur yang bisa dilanjutkan; spec menaruh F5 di tengah hitung mundur, sebelum menggeser jam, sehingga butir d dicek sebelum butir c (S-14, S-15). (2) TC-AUTH-MFA-80 Expected b ("kode terakhir tetap berlaku") tidak punya langkah pengecekan; spec menambahkan langkah mengetik kode dari email dan memverifikasi login berhasil di akhir TC. (3) TC-AUTH-MFA-76 Post Condition "hanya kode kedua yang masih berlaku" dibuktikan lewat TC-AUTH-MFA-78 pada spec ini dan tidak diasersi ulang; TC-AUTH-MFA-81 Post Condition "Hanya kode kedua yang berlaku" dicakup Expected b (kode pertama ditolak). (4) TC-AUTH-MFA-80 Expected c dan TC-AUTH-MFA-81 Expected c menyebut hitungan resend (tidak bertambah, bertambah satu) yang tidak terlihat di UI; LLD hanya menyebut `resend_count` sebagai kolom `otp_codes` tanpa endpoint baca, jadi mekanisme baca tidak dikarang di spec dan dicatat sebagai kebutuhan di Prerequisites (langkah 49 dan 70; S-11, S-13). (5) Post Condition tanpa langkah observasi dan tanpa Expected padanan tidak diasersi di spec (S-01, S-15): TC-AUTH-MFA-77 "Tidak ada kode OTP baru yang diterbitkan" (tidak diamati setelah hitung mundur selesai); TC-AUTH-MFA-78 "Satu sesi web aktif untuk `Hasan Basri`" (sesi web teramati sebagai Portal tampil, sudah menjadi `Verifikasi` Expected c). Perlu Expected atau langkah observasi di TC bila Post itu hendak diasersi. (6) Pre-setup #20 hanya menyebut manipulasi jam server; jam browser/klien (diperlukan agar hitung mundur UI maju) belum ada di Pre-setup. TC-AUTH-MFA-77, 76, 81, 78 menyebut tunggu hitung mundur atau tunggu 60 detik, bukan pengaturan jam (K§6). (7) Mekanisme seed state BE (trusted device ber-ID device browser uji A) belum ada di Pre-setup (#20/#21); spec tidak menyebut endpoint karangan (S-11, S-13).
