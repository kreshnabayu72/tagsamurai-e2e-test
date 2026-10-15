---
id: TC-AUTH-LP-E2E-052-lock-daily-reset-keeps-consecutive-days
title: "Password Benar Mengatur Ulang Data Lock Harian Tanpa Mengubah Hitungan Hari Berturut-turut"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-LP-163
coverage:
  web: automated
---

# Password Benar Mengatur Ulang Data Lock Harian Tanpa Mengubah Hitungan Hari Berturut-turut

## Prerequisites

- Mode: FE+BE.
- Seeding: satu user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) lalu diaktivasi. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG`.
- Kemampuan teknis: fixture BE untuk user Zainal berupa device terpercaya, tanpa gate Agreement dan MFA, bukan login pertama, dan tidak idle; geser jam server uji maju; fixture BE yang dapat membaca data lock user (hitungan hari berturut-turut dan status akun); reCAPTCHA mode uji.
- State global: jam server uji dimajukan pada langkah 12 dan 23; suite berjalan serial (`parallel: false`) karena jam server adalah state global. Pemulihan: hook `after` (tetap jalan walau spec gagal di tengah) mengembalikan jam server uji ke waktu nyata dan menghapus user.
- TC-AUTH-LP-163: Tanpa login (guest, browser web)
- TC-AUTH-LP-163: User `Zainal Abidin` (`zainalabidin+{runId}-052@qwertysystem.net`) berstatus Activated dan Active, hitungan gagal 0 hari ini (web), hitungan hari berturut-turut 0, device terpercaya, tanpa gate Agreement dan MFA (di-seed oleh fixture BE)
- TC-AUTH-LP-163 data: Password salah `Spectra.env.LP_PASSWORD_WRONG`; password benar `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-163: Password benar setelah tahap 1 jam lewat mengatur ulang data lock harian tanpa mengubah hitungan hari berturut-turut

1. Buka halaman Login with Password
2. Isi Email `zainalabidin+{runId}-052@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
3. Selesaikan reCAPTCHA
4. Klik [Log in]
5. Isi Email `zainalabidin+{runId}-052@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
6. Selesaikan reCAPTCHA
7. Klik [Log in]
8. Isi Email `zainalabidin+{runId}-052@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
9. Selesaikan reCAPTCHA
10. Klik [Log in]
11. Verifikasi Alert Danger lock 15 menit "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil pada salah ke-3
12. Majukan jam server uji sampai lock 15 menit lewat
13. Isi Email `zainalabidin+{runId}-052@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
14. Selesaikan reCAPTCHA
15. Klik [Log in]
16. Isi Email `zainalabidin+{runId}-052@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
17. Selesaikan reCAPTCHA
18. Klik [Log in]
19. Isi Email `zainalabidin+{runId}-052@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
20. Selesaikan reCAPTCHA
21. Klik [Log in]
22. Verifikasi Alert Danger lock 1 jam "Too many failed login attempts. Your account is locked for 1 hour. You can try again at {time}." tampil pada salah ke-6
23. Majukan jam server uji sampai lock 1 jam lewat (masih hari kalender yang sama)
24. Isi Email `zainalabidin+{runId}-052@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD`
25. Selesaikan reCAPTCHA
26. Klik [Log in]
27. Verifikasi Login berhasil, Portal — Product Hub tampil
28. Logout dari Portal — Product Hub
29. Buka halaman Login with Password
30. Isi Email `zainalabidin+{runId}-052@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
31. Selesaikan reCAPTCHA
32. Klik [Log in]
33. Verifikasi Alert Danger "Incorrect email or password" tampil pada salah baru ke-1
34. Isi Email `zainalabidin+{runId}-052@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
35. Selesaikan reCAPTCHA
36. Klik [Log in]
37. Verifikasi Alert Danger "Incorrect email or password" tampil pada salah baru ke-2
38. Isi Email `zainalabidin+{runId}-052@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
39. Selesaikan reCAPTCHA
40. Klik [Log in]
41. Verifikasi Alert Danger lock 15 menit "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil pada salah baru ke-3, bukan lock 1 jam atau Requires Reset
42. Baca data lock user `zainalabidin+{runId}-052@qwertysystem.net` lewat fixture BE
43. Verifikasi Hitungan hari berturut-turut tetap 1 dan tidak menjadi 2
44. Verifikasi Status akun tetap bukan Requires Reset dan bukan Permanent

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini berisi 44 langkah (melewati batas tinjau sekitar 35 langkah) karena TC-AUTH-LP-163 satu alur tiga tahap lock (15 menit, 1 jam, lalu login berhasil dan tiga salah baru) yang tidak bermakna bila dipecah. Eskalasi lock Permanent ada di spec `TC-AUTH-LP-E2E-014-lock-permanent-escalation`; user dan state seeding kedua spec berbeda dan tidak ada ketergantungan data antar-spec.
- Email diisi bersama Password pada tiap percobaan sebagaimana TC-AUTH-LP-163 (Langkah Uji 2, 3, 5, dan 7: "Isi Email ... dan Password ...").
- Sumber teks Alert lock 1 jam pada langkah 22: PRD §7.1 dan TC-AUTH-LP-46 ("Too many failed login attempts. Your account is locked for 1 hour. You can try again at {time}."); TC-AUTH-LP-163 hanya menyebut "Alert Danger lock 1 jam".
- Langkah penghubung (S-03): logout dari Portal (langkah 28) dan buka ulang halaman Login with Password (langkah 29) memulai ulang sesi guest (langkah 6 TC sumber); pengisian ulang Email, Password, dan reCAPTCHA sebelum tiap submit karena field Password dikosongkan dan reCAPTCHA kembali Unsolved setelah respons.
- Temuan untuk QA (TC-AUTH-LP-163): (1) Expected Result (d) mensyaratkan pemeriksaan data lock lewat fixture BE (tidak terjangkau UI); spec menulisnya sebagai langkah baca fixture BE (langkah spec 42). (2) Langkah Uji 3 menyebut "3× salah lagi" tanpa merinci langkah per percobaan; spec menguraikannya menjadi tiga submit. (3) Expected Result (d) menyebut hitungan hari berturut-turut "tetap 1" sedangkan precondition menyatakan 0 dan TC tidak menyebut kapan hitungan menjadi 1; spec mengasersi "tetap 1 dan tidak menjadi 2" (langkah spec 43) sesuai TC tanpa menambal nilai awalnya.
