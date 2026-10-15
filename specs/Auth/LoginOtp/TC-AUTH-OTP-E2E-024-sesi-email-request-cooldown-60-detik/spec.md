---
id: TC-AUTH-OTP-E2E-024-sesi-email-request-cooldown-60-detik
title: "Sesi Email-Request: Penolakan Request OTP Saat Cooldown 60 Detik dan Sesi Baru Setelah Verifikasi Sukses"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-169
  - TC-AUTH-OTP-90
  - TC-AUTH-OTP-189
  - TC-AUTH-OTP-95
coverage:
  web: automated
---

# Sesi Email-Request: Penolakan Request OTP Saat Cooldown 60 Detik dan Sesi Baru Setelah Verifikasi Sukses

## Prerequisites

- Mode: FE+BE.
- Tanpa login (halaman publik, tidak ada sesi aktif di browser). reCAPTCHA memakai mode uji environment.
- Kemampuan teknis: mail-catcher lingkungan uji untuk membaca email dan kode OTP 6 digit. Spec ini tidak memajukan jam (§6), baik jam server maupun jam browser, dan tidak ada tunggu waktu nyata: semua penolakan terjadi dalam jendela cooldown 60 detik sejak Request OTP pertama, sehingga seluruh langkah antara Request OTP pertama dan Request OTP kedua dijalankan tanpa jeda.
- Environment variable: `OTP_PASSWORD` (password yang dipasang ke user uji saat seeding aktivasi; tidak dipakai langkah uji).
- Hook `before` (seeding API, email bersuffix per run) membuat user Activated dengan Toggle Active ON, profil BASE (sudah login web dalam 30 hari terakhir pada device dikenal, persetujuan Privacy Policy versi terbaru ada, MFA tidak aktif; Tabel Data Uji Pre-setup #2):
  - TC-AUTH-OTP-169 dan TC-AUTH-OTP-90 (satu alur pada satu sesi email-request): `Laras Santoso` (`larassantoso+{runId}-024@qwertysystem.net`).
  - TC-AUTH-OTP-189: `Hana Kusumawati` (`hanakusumawati+{runId}-024@qwertysystem.net`).
  - TC-AUTH-OTP-95: `Siti Utami` (`sitiutami+{runId}-024@qwertysystem.net`).
- Hook `after`: tutup sesi login yang terbentuk (TC-AUTH-OTP-95) dan hapus ketiga user. Hook ini tetap jalan walau spec gagal di tengah.

## Test Steps

### TC-AUTH-OTP-169: reCAPTCHA kosong saat cooldown Resend berjalan menampilkan caption reCAPTCHA, bukan penolakan cooldown

1. Buka halaman `Auth > Login with OTP > Request OTP` di jendela privat baru (tanpa sesi)
2. Ketik `larassantoso+{runId}-024@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Klik tautan [Back to Login with Password]
6. Klik tautan [Log in with OTP]
7. Biarkan widget reCAPTCHA tidak dicentang
8. Klik button [Request OTP]
9. Verifikasi caption error di bawah widget reCAPTCHA: "Please verify that you are not a robot"
10. Verifikasi Alert "Too many requests. Please try again later." tidak tampil
11. Verifikasi tidak ada email OTP baru di mail-catcher untuk `larassantoso+{runId}-024@qwertysystem.net`

### TC-AUTH-OTP-90: Request OTP ulang pada email yang sama saat cooldown 60 detik masih berjalan ditolak

12. Centang widget reCAPTCHA "I'm not a robot"
13. Klik button [Request OTP]
14. Verifikasi Alert inline di atas button [Request OTP]: "Too many requests. Please try again later."
15. Verifikasi layar tetap di Request OTP dan tidak berpindah ke Verify OTP
16. Verifikasi tidak ada email OTP baru di mail-catcher untuk `larassantoso+{runId}-024@qwertysystem.net`

### TC-AUTH-OTP-189: Variasi kapitalisasi dan spasi email tidak menghindari cooldown sesi email-request

17. Buka halaman `Auth > Login with OTP > Request OTP` di jendela privat baru (tanpa sesi)
18. Ketik `hanakusumawati+{runId}-024@qwertysystem.net` pada field Email
19. Centang widget reCAPTCHA "I'm not a robot"
20. Klik button [Request OTP]
21. Klik tautan [Back to Login with Password]
22. Pada Login with Password ketik spasi, lalu `HanaKusumawati+{runId}-024@QwertySystem.net`, lalu spasi pada field Email
23. Klik tautan [Log in with OTP]
24. Centang widget reCAPTCHA "I'm not a robot" dan klik button [Request OTP] dalam 60 detik sejak langkah 20
25. Verifikasi Request OTP kedua ditolak dengan Alert inline di atas button [Request OTP]: "Too many requests. Please try again later."
26. Verifikasi layar tetap di Request OTP
27. Verifikasi caption "Email is not registered yet" dan "Email format is incorrect" tidak tampil (email dinormalisasi ke akun yang sama)
28. Verifikasi tidak ada email OTP baru di mail-catcher untuk `hanakusumawati+{runId}-024@qwertysystem.net`

### TC-AUTH-OTP-95: Request OTP setelah verifikasi sukses memulai sesi email-request baru

29. Buka halaman `Auth > Login with OTP > Request OTP` di jendela privat baru (tanpa sesi)
30. Ketik `sitiutami+{runId}-024@qwertysystem.net` pada field Email
31. Centang widget reCAPTCHA "I'm not a robot"
32. Klik button [Request OTP]
33. Ketik 6 digit kode OTP dari email pada kotak digit
34. Logout dari Portal — Product Hub
35. Buka halaman `Auth > Login with OTP > Request OTP` di browser
36. Ketik `sitiutami+{runId}-024@qwertysystem.net` pada field Email
37. Centang widget reCAPTCHA "I'm not a robot"
38. Klik button [Request OTP]
39. Verifikasi toast sukses: "Success, the code has been sent."
40. Verifikasi halaman Verify OTP tampil
41. Verifikasi area Resend menampilkan "Resend code in (00:59)"
42. Verifikasi area Resend dalam keadaan disabled
43. Verifikasi tidak ada Alert "Too many requests. Please try again later."

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Pengecualian P-3 (user berurutan, `docs/e2e-conventions.md` §3): TC-169 dan TC-90 di sumber memakai dua user berbeda (`Laras Santoso` dan `Sinta Nugroho`) tetapi keduanya menolak Request OTP kedua dalam cooldown 60 detik sejak Request OTP pertama yang sama. Spec memakai satu user (`Laras Santoso`) dan satu Request OTP pertama: TC-169 (reCAPTCHA kosong) dulu, lalu TC-90 (reCAPTCHA dicentang), dalam satu jendela 60 detik. Urutan di sumber (90 lalu 169 pada daftar TC) dibalik supaya penolakan reCAPTCHA yang tidak memulai sesi baru ditaruh sebelum penolakan cooldown.
- Langkah penghubung (S-03): langkah 12 (mencentang reCAPTCHA di form yang sama setelah langkah 8, email tetap terisi), langkah 33 (login sukses TC-95 tanpa `Verifikasi` karena TC sumber hanya menuliskan aksi itu), langkah 34 (logout sebagai prasyarat membuka Request OTP lagi).
- Asersi absence: Expected d TC-90 ("tidak ada entri log untuk penolakan ini") dipindah ke spec absence E2E-047 (kelas g, S-05). Tidak ada akun admin Total Control yang dipakai spec ini.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Temuan untuk QA:
  - TC-95 tidak punya Expected untuk langkah 5 (login sukses) dan langkah 6 (logout); hanya Expected setelah Request OTP kedua yang diasersi. Spec tidak menambah `Verifikasi` untuk login sukses.
  - TC-95 Post Condition ("sesi sebelumnya berakhir saat verifikasi sukses; sesi baru dimulai dengan jumlah resend 0") hanya teramati lewat "Resend code in (00:59)" tanpa Alert; hitungan resend 0 diasersi tidak langsung lewat State A (langkah 41 dan 42).
  - TC-189 langkah 8 ("dalam 60 detik sejak langkah 4") menuntut seluruh langkah 20 sampai 24 selesai di bawah 60 detik; spec tidak memajukan jam server di antaranya.
  - Post Condition TC-169 a (Failed `Captcha not completed`, detail pada TC Logging) tidak punya langkah observasi di TC, sehingga tidak diasersi di spec ini; pencatatan itu diuji di spec pencatatan Request OTP.
  - TC-169 dan TC-90 di sumber memakai dua user berbeda dan TC tidak menyatakan bahwa keduanya dijalankan berurutan pada satu sesi email-request dalam satu jendela 60 detik; spec mengasumsikan urutan itu (P-3).
