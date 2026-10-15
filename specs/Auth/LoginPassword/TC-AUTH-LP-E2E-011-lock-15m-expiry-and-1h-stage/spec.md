---
id: TC-AUTH-LP-E2E-011-lock-15m-expiry-and-1h-stage
title: "Lock 15 Menit Berakhir dan Masuk Tahap Lock 1 Jam"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-151
  - TC-AUTH-LP-44
  - TC-AUTH-LP-45
  - TC-AUTH-LP-46
  - TC-AUTH-LP-47
coverage:
  web: automated
---

# Lock 15 Menit Berakhir dan Masuk Tahap Lock 1 Jam

## Prerequisites

- Mode: FE+BE.
- Seeding: dua user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) lalu diaktivasi. Kedua user dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG`.
- Kemampuan teknis: atur jam server uji (batas eksak "satu detik sebelum {time}" dan "tepat {time}" diset ABSOLUT atau dibekukan pada nilai itu, bukan digeser relatif; melewati {time} pada TC-AUTH-LP-44 boleh dimajukan); fixture BE yang menaruh user pada status terkunci 15 menit di web dengan waktu berakhirnya lock diketahui penguji; reCAPTCHA mode uji; device terpercaya dan tanpa gate Agreement atau MFA untuk user pertama. Pemulihan: hook `after` mengembalikan jam server uji ke waktu nyata dan menghapus kedua user.
- State global: suite berjalan serial (`parallel: false`) karena jam server uji diubah; hook `after` memulihkan jam server uji ke waktu nyata (tetap jalan walau spec gagal di tengah).
- TC-AUTH-LP-151: Tanpa login (guest, browser web)
- TC-AUTH-LP-151: User `Rina Putri` (`rinaputri+{runId}-011a@qwertysystem.net`) berstatus Activated dan Active, device terpercaya, tanpa gate Agreement dan MFA, terkunci 15 menit di web dengan waktu berakhir {time} yang diketahui penguji (di-seed oleh fixture BE)
- TC-AUTH-LP-151 data: Password benar `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-44: Tanpa login (guest, browser web)
- TC-AUTH-LP-44: User `Rina Putri` (`rinaputri+{runId}-011b@qwertysystem.net`) berstatus Activated dan Active, terkunci 15 menit di web setelah 3 kegagalan hari ini, belum ada kegagalan sesudahnya (di-seed oleh fixture BE; lock dipicu bersamaan dengan lock user pertama)
- TC-AUTH-LP-44 data: Password salah `Spectra.env.LP_PASSWORD_WRONG`
- TC-AUTH-LP-45: Tanpa login (guest); user kedua sudah 4 kali salah password hari ini dan tidak sedang terkunci (hasil TC-AUTH-LP-44 dalam spec ini)
- TC-AUTH-LP-46: Tanpa login (guest); user kedua sudah 5 kali salah password hari ini dan tidak sedang terkunci (hasil TC-AUTH-LP-45 dalam spec ini)
- TC-AUTH-LP-47: Tanpa login (guest); user kedua sedang terkunci 1 jam di web (hasil TC-AUTH-LP-46 dalam spec ini) dengan password benar `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-151: Submit tepat pada waktu lock 15 menit berakhir dievaluasi seperti biasa

1. Buka halaman Login with Password
2. Catat waktu berakhirnya lock 15 menit user `rinaputri+{runId}-011a@qwertysystem.net` sebagai {time} (dari fixture BE)
3. Set jam server uji secara absolut ke satu detik sebelum {time}
4. Isi Email `rinaputri+{runId}-011a@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD`
5. Selesaikan reCAPTCHA
6. Klik [Log in]
7. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil
8. Verifikasi tidak ada sesi dibuat
9. Set jam server uji secara absolut ke tepat {time}
10. Muat ulang halaman Login with Password
11. Isi Email `rinaputri+{runId}-011a@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD`
12. Selesaikan reCAPTCHA
13. Klik [Log in]
14. Verifikasi login berhasil dan browser menuju Portal — Product Hub
15. Verifikasi caption lock tidak tampil
16. Logout dari Portal — Product Hub

### TC-AUTH-LP-44: Password salah ke-4 setelah lock 15 menit berakhir tidak mengunci

17. Buka halaman Login with Password
18. Majukan jam server uji melebihi durasi lock 15 menit user `rinaputri+{runId}-011b@qwertysystem.net`
19. Isi Email `rinaputri+{runId}-011b@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
20. Selesaikan reCAPTCHA
21. Klik [Log in]
22. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
23. Verifikasi caption lock tidak tampil

### TC-AUTH-LP-45: Password salah ke-5 belum memicu lock

24. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
25. Selesaikan reCAPTCHA
26. Klik [Log in]
27. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
28. Verifikasi caption lock tidak tampil

### TC-AUTH-LP-46: Password salah ke-6 pada hari yang sama memicu lock 1 jam

29. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
30. Selesaikan reCAPTCHA
31. Klik [Log in]
32. Verifikasi Alert Danger di atas Button [Log in]: "Too many failed login attempts. Your account is locked for 1 hour. You can try again at {time}." ({time} = jam berakhirnya lock dalam Time Format General Settings dan Time Zone entitas, hanya jam tanpa tanggal)
33. Catat nilai {time} pada Alert
34. Verifikasi Alert tidak memuat tautan [Reset password]
35. Verifikasi Link "Forgot your password? " [Reset here] di footer tetap tampil
36. Verifikasi field Email tetap enabled
37. Verifikasi field Password tetap enabled
38. Verifikasi Button [Log in] tetap enabled

### TC-AUTH-LP-47: Submit selama lock 1 jam aktif menampilkan caption lock 1 jam yang sama

39. Isi Password `Spectra.env.LP_PASSWORD`
40. Selesaikan reCAPTCHA
41. Klik [Log in]
42. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 1 hour. You can try again at {time}." tampil dengan nilai {time} sama seperti pada langkah 33
43. Verifikasi tidak ada sesi dibuat

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Dua user dipakai karena TC-AUTH-LP-151 berakhir dengan login berhasil yang mereset data lock harian user pertama, sehingga tidak dapat dilanjutkan oleh rantai TC-AUTH-LP-44 sampai TC-AUTH-LP-47 (aturan TC-AUTH-LP-68). Sufiks `a` dan `b` ditambahkan pada sufiks per run agar kedua email berbeda.
- Urutan TC-AUTH-LP-151 di awal spec: boundary lock memakai user yang lock-nya masih aktif; rantai TC-AUTH-LP-44 sampai 47 menyusul. Penyimpangan dari urutan nomor TC sumber ini disengaja (S-05).
- TC-AUTH-LP-44 sampai TC-AUTH-LP-47 bergantung berantai di TC sumber (TC-AUTH-LP-40, 44, 45, 46). State awal rantai (user terkunci 15 menit dengan 3 kegagalan) disiapkan lewat seeding fixture BE (S-04); progresi yang membangunnya diuji di spec `TC-AUTH-LP-E2E-009-lock-15m-progression`.
- Jumlah langkah melewati ~35 (smell): satu topik (ekspirasi lock 15 menit dan eskalasi ke lock 1 jam), TC-AUTH-LP-151 berdiri sendiri pada user pertama dan rantai TC-AUTH-LP-44 sampai 47 membangun state berurutan pada user kedua sehingga tidak bisa dipecah tanpa seeding ulang.
- Langkah penghubung (S-03): langkah 10 (muat ulang halaman) dan langkah 16 (logout) mengembalikan state sebelum TC berikutnya; pengisian ulang Password dan reCAPTCHA sebelum tiap submit karena field Password dikosongkan dan reCAPTCHA kembali Unsolved setelah respons.
- Temuan untuk QA (TC-AUTH-LP-151): Caption {time} hanya memuat jam dan menit (HH:mm), sedangkan langkah "satu detik sebelum {time}" butuh ketelitian detik; spec memakai waktu berakhir lock dari fixture BE, bukan nilai yang dibaca dari Alert.
- Temuan untuk QA (TC-AUTH-LP-44): precondition mensyaratkan "waktu lock sudah terlewat" sedangkan Langkah Uji 2 meminta menunggu {time} terlewati; spec menulis langkah majukan jam server uji dan menganggap precondition awal sebagai state terkunci yang belum berakhir.
- Temuan untuk QA (TC-AUTH-LP-44, TC-AUTH-LP-45): Post Condition "Hitungan gagal hari ini = 4" dan "= 5" tidak punya langkah observasi di TC (UI tidak menampilkan hitungan) sehingga tidak diasersi.
