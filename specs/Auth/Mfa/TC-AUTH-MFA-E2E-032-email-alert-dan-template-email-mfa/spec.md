---
id: TC-AUTH-MFA-E2E-032-email-alert-dan-template-email-mfa
title: "Template Email OTP Faktor-2 dan Email Alert Login Tak Biasa"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-65
  - TC-AUTH-MFA-152
  - TC-AUTH-MFA-153
  - TC-AUTH-MFA-154
  - TC-AUTH-MFA-155
coverage:
  web: automated
---

# Template Email OTP Faktor-2 dan Email Alert Login Tak Biasa

## Prerequisites

- Mode: FE+BE.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah IP uji browser uji B (lokasi koneksi yang diresolusi geo-IP: dipasang ke IP uji tanpa data lokasi pada TC-AUTH-MFA-155); hook `after` memulihkan IP uji itu ke default (Jakarta, ID).
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): lima user, password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-65: `Sinta Maharani` (`sintamaharani+{runId}-032@qwertysystem.net`), profil NEWDEV (Tabel Data Uji Pre-setup #4: Activated, Active ON, seperti BASE tetapi ID device browser uji B belum ada di daftar trusted device, Authenticator belum terdaftar)
  - TC-AUTH-MFA-152: `Kiki Amalia` (`kikiamalia+{runId}-032@qwertysystem.net`), profil NEWDEVE (Tabel Data Uji Pre-setup #5: seperti NEWDEV tetapi Authenticator sudah terdaftar)
  - TC-AUTH-MFA-153: `Surya Darmawan` (`suryadarmawan+{runId}-032@qwertysystem.net`), profil NEWDEVE
  - TC-AUTH-MFA-154: `Febri Yulianto` (`febriyulianto+{runId}-032@qwertysystem.net`), profil NEWDEVE
  - TC-AUTH-MFA-155: `Lutfi Anwar` (`lutfianwar+{runId}-032@qwertysystem.net`), profil NEWDEVE
- Hook `after`: hapus kelima user; lepas IP uji tanpa data lokasi (TC-AUTH-MFA-155) dan kembalikan IP uji ke default (Jakarta, ID). Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC dimulai di jendela privat baru, yang memberi ID device belum dikenali (browser uji B).
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Mail-catcher lingkungan uji: membaca subject dan isi email (teks, button, tautan) tiap user, dan membuka tautan button email di browser (TC-AUTH-MFA-65, 152, 153, 154, 155).
  - Browser uji B = Chrome di Windows (TC-AUTH-MFA-152, nilai baris Device email alert).
  - IP uji Jakarta (ID) yang teresolusi geo-IP ke Jakarta, Indonesia (TC-AUTH-MFA-152), dan IP uji tanpa data lokasi yang dapat dipasang lalu dilepas (TC-AUTH-MFA-155).
  - reCAPTCHA mode uji di environment.
  - Seeding state BE per user: login sukses sebelumnya dari browser uji A (device dikenali), lokasi dan waktu login terakhir (IP uji Jakarta, ID; logout web terakhir kurang dari 30 hari), ID device browser uji B belum ada di daftar trusted device, dan Authenticator sudah terdaftar (profil NEWDEVE); mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
- Semua user berprofil NEWDEV atau NEWDEVE (bukan login pertama), jadi tiap login langsung menuju Choose Verification Method tanpa layar Confirm to Continue.

## Test Steps

### TC-AUTH-MFA-65: Email OTP faktor-2 sesuai template email OTP

1. Buka jendela privat baru (tanpa sesi login)
2. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
3. Ketik `sintamaharani+{runId}-032@qwertysystem.net` pada field Email
4. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
5. Centang widget reCAPTCHA "I'm not a robot"
6. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
7. Pilih opsi "OTP via email" pada halaman Choose Verification Method
8. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `sintamaharani+{runId}-032@qwertysystem.net`
9. Buka email OTP di mail-catcher untuk `sintamaharani+{runId}-032@qwertysystem.net`
10. Verifikasi Subject email: "Your TAG Samurai one-time password (OTP)"
11. Verifikasi Body menyapa "Hi Sinta Maharani,"
12. Verifikasi Body memuat: "We received a request to sign in to your TAG Samurai account. Use the one-time password (OTP) below to complete your login:"
13. Verifikasi Setelah kalimat tersebut tampil kode 6 digit numerik
14. Verifikasi Kode 6 digit tersebut tampil menonjol
15. Verifikasi Kode 6 digit tersebut bukan button
16. Verifikasi Kode 6 digit tersebut tanpa tautan
17. Verifikasi Body memuat: "This one-time password is valid for 5 minutes and can only be used once. If it expires before you enter it, go back to the login page and request a new code."
18. Verifikasi Body memuat: "To keep your data secure, please don't share this code with anyone. If you didn't request this, you can safely ignore this email."
19. Verifikasi Body ditutup dengan "— TAG Samurai"
20. Verifikasi Tepat satu email OTP diterima untuk pengiriman ini
21. Verifikasi Email OTP dikirim ke `sintamaharani+{runId}-032@qwertysystem.net` (email akun terdaftar)

### TC-AUTH-MFA-152: Isi email alert login tak biasa sesuai template

22. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
23. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
24. Ketik `kikiamalia+{runId}-032@qwertysystem.net` pada field Email
25. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
26. Centang widget reCAPTCHA "I'm not a robot"
27. Klik button [Log in] dari IP uji Jakarta (ID) → halaman `Auth > MFA > Choose Verification Method` tampil
28. Buka email alert di mail-catcher untuk `kikiamalia+{runId}-032@qwertysystem.net`
29. Verifikasi Subject email: "New sign-in to your TAG Samurai account"
30. Verifikasi Body menyapa "Hi Kiki Amalia,"
31. Verifikasi Body memuat: "We noticed a new sign-in to your account from a device or location we don't recognize."
32. Verifikasi Body memuat baris "Device: Chrome on Windows" (format [Browser] on [OS] dari browser uji B)
33. Verifikasi Body memuat baris "Location: Jakarta, Indonesia (approximate, based on IP address)" (format "Location: [City, Country] (approximate, based on IP address)")
34. Verifikasi Body memuat baris "Time:" berisi tanggal dan waktu login
35. Verifikasi Body memuat baris "IP Address:" berisi IP uji
36. Verifikasi Body memuat: "If this was you, no action is needed."
37. Verifikasi Body memuat: "If you don't recognize this activity, reset your password immediately to secure your account."
38. Verifikasi Button [Reset Password] tampil di email
39. Verifikasi Body ditutup dengan "— TAG Samurai"

### TC-AUTH-MFA-153: Email alert dikirim segera saat login tak biasa terdeteksi, sebelum MFA selesai

40. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
41. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
42. Ketik `suryadarmawan+{runId}-032@qwertysystem.net` pada field Email
43. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
44. Centang widget reCAPTCHA "I'm not a robot"
45. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
46. Tanpa memilih opsi atau menyelesaikan MFA, buka mail-catcher untuk `suryadarmawan+{runId}-032@qwertysystem.net`
47. Verifikasi Email alert "New sign-in to your TAG Samurai account" sudah diterima padahal MFA belum diselesaikan
48. Verifikasi Halaman Choose Verification Method masih tampil di jendela privat
49. Verifikasi Sesi penuh belum ada (Portal tidak tampil)

### TC-AUTH-MFA-154: Button Reset Password pada email alert membuka halaman request Reset Password

50. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
51. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
52. Ketik `febriyulianto+{runId}-032@qwertysystem.net` pada field Email
53. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
54. Centang widget reCAPTCHA "I'm not a robot"
55. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
56. Buka email alert di mail-catcher untuk `febriyulianto+{runId}-032@qwertysystem.net`
57. Klik button [Reset Password] pada email
58. Verifikasi Halaman request Reset Password (`Auth > Reset Password`) terbuka
59. Verifikasi Halaman Set Password tidak langsung terbuka

### TC-AUTH-MFA-155: Lokasi pada email alert menampilkan Unknown location saat geo-IP tidak terparse

60. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
61. Arahkan request browser uji B melalui IP uji tanpa data lokasi (geo-IP tidak dapat meresolusi IP ini)
62. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
63. Ketik `lutfianwar+{runId}-032@qwertysystem.net` pada field Email
64. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
65. Centang widget reCAPTCHA "I'm not a robot"
66. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
67. Buka email alert di mail-catcher untuk `lutfianwar+{runId}-032@qwertysystem.net`
68. Verifikasi Baris Location pada email alert berisi "Unknown location" (bukan tanda strip)
69. Lepas IP uji tanpa data lokasi dan kembalikan IP uji browser uji B ke default (Jakarta, ID)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Kelas harness d (objek uji: isi dan template email di mail-catcher). Spec ini hanya memuat asersi isi email; pencatatan log MFA ada di spec `TC-AUTH-MFA-E2E-033`, `034`, dan `035`.
- Melewati ±35 langkah (±39 netto setelah langkah prefix login faktor-1 tidak dihitung) hanya karena asersi isi email yang dipecah per klausa (S-01); kelima TC independen (user dan jendela privat sendiri) dan TC-AUTH-MFA-155 yang mengubah IP uji ditaruh paling akhir, sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal dan spec tidak dipecah.
- Urutan mengikuti TC sumber. TC-AUTH-MFA-155 ditaruh paling akhir karena mengubah IP uji (state global yang dipulihkan di langkah 69 dan hook `after`).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): buka jendela privat baru di awal tiap TC (langkah 1, 22, 40, 50, 60); langkah 61 dan 69 (pasang dan lepas IP uji tanpa data lokasi) mewujudkan Data Uji TC-AUTH-MFA-155 dan pemulihannya.
- Asersi "tidak ada entri log untuk pengiriman email" (Post Condition TC-AUTH-MFA-65 dan 152) tidak ditulis di spec ini (S-05).
- Temuan untuk QA:
  - TC-AUTH-MFA-65 dan seluruh TC di spec ini menulis "password valid `Nama User`" pada Langkah Uji; spec memakai `Spectra.env.MFA_PASSWORD` sebagai password valid user seeding.
  - Post Condition tanpa langkah observasi di TC dan tanpa Expected padanan tidak diasersi: TC-AUTH-MFA-65 "Satu kode OTP faktor-2 aktif untuk `Sinta Maharani`", TC-AUTH-MFA-153 "Sesi pre-auth MFA aktif untuk `Surya Darmawan`" (teramati lewat halaman Choose Verification Method tampil, langkah 48), dan TC-AUTH-MFA-154 "Tidak ada perubahan password `Febri Yulianto`".
  - TC-AUTH-MFA-65 dan 152: Post Condition "tidak ada entri log untuk pengiriman email" tidak masuk TC absence mana pun di batch spec 035 (yang memuat TC-AUTH-MFA-168, 169, 170, 171, 207).
  - TC-AUTH-MFA-152 Expected butir c menulis format Time "tanggal dan waktu login dalam zona waktu user" tanpa format literal; spec hanya mengasersi baris "Time:" terisi tanggal dan waktu login; zona waktu user dan format literalnya tidak diasersi.
  - TC-AUTH-MFA-152 Data Uji menyebut IP uji Jakarta (ID) dan TC lain di spec ini tidak menyebut IP; TC-AUTH-MFA-153 dan 154 memakai IP default browser uji B.
  - Mekanisme seeding state BE per user (login sebelumnya dari browser uji A, lokasi dan waktu login terakhir, Authenticator terdaftar) belum ada di Pre-setup (#20/#21) TC.
