---
id: TC-AUTH-MFA-E2E-046-guard-double-submit
title: "Guard Double-Submit pada OTP Verification, Authenticator Verification, dan Enrollment"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-194
  - TC-AUTH-MFA-195
  - TC-AUTH-MFA-196
coverage:
  web: automated
---

# Guard Double-Submit pada OTP Verification, Authenticator Verification, dan Enrollment

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`), password user `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-194: `Rizky Rahmawati` (`rizkyrahmawati+{runId}-046@qwertysystem.net`), profil NEWDEV (Tabel Data Uji Pre-setup #4: Activated, Active ON, device browser uji B belum ada di daftar trusted device, Authenticator belum terdaftar).
  - TC-AUTH-MFA-195: `Nur Rahmawati` (`nurrahmawati+{runId}-046@qwertysystem.net`), profil NEWDEVE (Tabel Data Uji Pre-setup #5: seperti NEWDEV, Authenticator sudah terdaftar dengan secret yang dikenali aplikasi authenticator uji).
  - TC-AUTH-MFA-196: `Agus Rahmawati` (`agusrahmawati+{runId}-046@qwertysystem.net`), profil FIRST (Tabel Data Uji Pre-setup #3: Activated, Active ON, belum pernah login di platform mana pun, Authenticator belum terdaftar).
- Hook `after`: hapus ketiga user (beserta sesi web yang terbentuk). Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk ketiga TC. Tiap TC dimulai di jendela baru tanpa sesi login: jendela privat baru browser uji B (ID device belum dikenali) untuk TC-AUTH-MFA-194 dan 195, jendela baru browser uji A (konteks bersih) untuk TC-AUTH-MFA-196. Pengecekan log TC-AUTH-MFA-195 memakai jendela sesi akun aktor Total Control (Global Settings) yang dibuka di hook `before` (kredensial `Spectra.env.GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Pemicu dua aksi hampir bersamaan pada satu halaman (digit ke-6 OTP lalu klik [Login] segera, dan klik ganda cepat pada [Login] atau [Verify]).
  - Penghitungan request jaringan browser ke `POST /v2/iam/auth/mfa/otp/verify`, `POST /v2/iam/auth/mfa/authenticator/verify`, dan `POST /v2/iam/auth/mfa/authenticator/enroll/verify` (nama endpoint dari `auth/mfa/API/openapi.yaml`).
  - Mail-catcher lingkungan uji untuk kode OTP faktor-2 (TC-AUTH-MFA-194).
  - Aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) untuk kode TOTP valid dan untuk memindai QR code Enrollment (TC-AUTH-MFA-196).
  - Penanda waktu (baseline) Activity Log Session yang dicatat sebelum klik ganda, supaya asersi entri Success hanya membaca baris sesudah penanda (TC-AUTH-MFA-195).
  - Pembacaan status enrollment Authenticator oleh sisi BE untuk butir b TC-AUTH-MFA-196 ("Enrollment aktif sekali"); kemampuan ini disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD, dan spec tidak menyebut endpoint pembacaannya.
  - Seeding state BE per user: profil NEWDEV/NEWDEVE tanpa ID device browser uji B di daftar trusted device, Authenticator terdaftar dengan secret yang dikenal aplikasi authenticator uji untuk profil NEWDEVE (`Nur Rahmawati`), dan profil FIRST yang belum pernah login di platform mana pun; mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - reCAPTCHA mode uji di environment.
- Pemulihan state global: tidak ada (spec tidak mengubah jam server, geo-IP, email service, atau counter rate limit).

## Test Steps

### TC-AUTH-MFA-194: Auto-submit OTP bersamaan dengan klik [Login] diproses satu kali

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `rizkyrahmawati+{runId}-046@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
6. Pilih opsi "OTP via email" pada halaman Choose Verification Method
7. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `rizkyrahmawati+{runId}-046@qwertysystem.net`
8. Ketik 5 digit pertama kode OTP faktor-2 dari email pada kotak digit
9. Ketik digit ke-6 dan segera klik button [Login] sebelum halaman berpindah
10. Verifikasi Button [Login] disabled setelah pemicu pertama
11. Verifikasi Spinner tampil pada button [Login] setelah pemicu pertama
12. Verifikasi Hanya satu request ke `POST /v2/iam/auth/mfa/otp/verify` yang terkirim (hanya satu verifikasi yang diproses)
13. Verifikasi Satu sesi web dibuat
14. Verifikasi Browser dialihkan ke Portal — Product Hub

### TC-AUTH-MFA-195: Klik ganda [Login] pada Authenticator Verification diproses satu kali

15. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
16. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
17. Ketik `nurrahmawati+{runId}-046@qwertysystem.net` pada field Email
18. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
19. Centang widget reCAPTCHA "I'm not a robot"
20. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
21. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
22. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
23. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `nurrahmawati+{runId}-046@qwertysystem.net` pada kotak digit
24. Catat penanda waktu (baseline) Activity Log Session sebelum klik ganda
25. Klik button [Login] dua kali dengan cepat
26. Verifikasi Button [Login] disabled setelah klik pertama
27. Verifikasi Hanya satu request ke `POST /v2/iam/auth/mfa/authenticator/verify` yang terkirim (hanya satu request verifikasi diproses)
28. Verifikasi Satu sesi web dibuat
29. Verifikasi Browser dialihkan ke Portal — Product Hub
30. Pindah ke jendela sesi akun aktor Total Control (Global Settings), lalu buka `Global Settings > Activity Log > Session` dan cari entri sesudah penanda waktu untuk `Nur Rahmawati`
31. Verifikasi Tepat satu entri baru sesudah penanda waktu dengan Status "Success" untuk `Nur Rahmawati` (tidak ada log atau efek ganda)

### TC-AUTH-MFA-196: Klik ganda [Verify] pada Enrollment diproses satu kali

32. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih, tanpa sesi login)
33. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
34. Ketik `agusrahmawati+{runId}-046@qwertysystem.net` pada field Email
35. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
36. Centang widget reCAPTCHA "I'm not a robot"
37. Klik button [Log in] → layar Confirm to Continue tampil
38. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
39. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
40. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
41. Pindai QR code dengan aplikasi authenticator uji, lalu ketik 6 digit kode dari aplikasi authenticator uji pada kotak digit
42. Klik button [Verify] dua kali dengan cepat
43. Verifikasi Hanya satu request ke `POST /v2/iam/auth/mfa/authenticator/enroll/verify` yang terkirim (hanya satu request verifikasi diproses)
44. Verifikasi Enrollment Authenticator aktif sekali (status enrollment dibaca oleh sisi BE)
45. Verifikasi Login final satu kali: browser dialihkan ke Portal — Product Hub

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela baru di awal tiap TC setelah TC pertama, mencatat penanda waktu baseline log dan pindah ke jendela sesi akun aktor pada TC-AUTH-MFA-195) bukan asersi tambahan (S-03).
- Penghitungan request jaringan ke endpoint verifikasi pada TC-AUTH-MFA-194, 195, dan 196 adalah cara spec mengukur "hanya satu verifikasi/request diproses"; TC tidak menyebut cara pengukurannya (lihat Temuan untuk QA butir 1).
- Temuan untuk QA: (1) TC-AUTH-MFA-194 butir a, TC-AUTH-MFA-195 butir a, dan TC-AUTH-MFA-196 butir a menyebut "hanya satu verifikasi/request diproses" tanpa cara pengukuran; spec menghitung request jaringan browser ke endpoint verifikasi masing-masing. (2) TC-AUTH-MFA-194 Post Condition "Satu sesi web aktif untuk `Rizky Rahmawati`" dan "Tepat satu entri Success login final pada tiap surface log" tidak punya Expected padanan maupun langkah observasi di Langkah Uji, sehingga tidak diasersi dan spec tidak menambah langkah pembacaan Activity Log Session dan User Log. (3) TC-AUTH-MFA-195 butir b menyebut "tidak ada log atau efek ganda" dan Post Condition "tepat satu entri Success login final"; spec mengecek Activity Log Session saja (Status "Success", kolom Activity tidak diasersi karena TC tidak menyebutnya), memakai akun aktor hook walau TC-AUTH-MFA-195 tidak mencantumkan akun Total Control di Precondition. (4) TC-AUTH-MFA-195 butir b "tidak ada log atau efek ganda" ditulis sebagai satu entri Success; tidak ada cara pengecekan "efek ganda" lain di Langkah Uji. (5) TC-AUTH-MFA-196 Post Condition "Satu sesi web aktif; tepat satu entri Success login final" tidak punya Expected padanan (butir b hanya "Enrollment aktif sekali dan login final satu kali") maupun langkah observasi di Langkah Uji, sehingga tidak diasersi dan spec tidak menambah langkah pembacaan Activity Log Session. (6) Mekanisme seeding state BE per user (profil NEWDEV/NEWDEVE/FIRST: trusted device, Authenticator dengan secret dikenal) belum ada di Pre-setup TC (#20/#21). (7) TC-AUTH-MFA-196 butir b "Enrollment aktif sekali" tidak memberi cara cek di Langkah Uji; spec memakai pembacaan status enrollment oleh sisi BE (disediakan tim FE/BE).
