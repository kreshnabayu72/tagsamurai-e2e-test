---
id: TC-AUTH-RST-E2E-016-screening-email-sent-countdown
title: "Screening Halaman Email Sent!, Countdown Resend, dan Navigasi Kembali"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-39
  - TC-AUTH-RST-40
  - TC-AUTH-RST-41
  - TC-AUTH-RST-46
  - TC-AUTH-RST-45
coverage:
  web: automated
---

# Screening Halaman Email Sent!, Countdown Resend, dan Navigasi Kembali

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek `Budi Santoso` (`budisantoso+{runId}-016@qwertysystem.net`) dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`, tanpa token reset aktif dan tanpa percobaan reset. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: mail-catcher dengan pembacaan jumlah email per alamat (baseline jumlah email); pembekuan jam browser/perangkat sebelum klik [Reset Password] (langkah 3) sampai sebelum jeda nyata (langkah 18), supaya countdown tetap 1:00 selama pembacaan nilai awal C0 (langkah 5 dan 6) dan screening (langkah 7 sampai 17); jeda nyata 5 detik pada langkah 19 (pembacaan countdown C1; jeda pendek, jam browser sudah dilepas dan tidak digeser); reCAPTCHA mode uji; jendela privat tanpa sesi login; reload halaman (F5); pengamatan network request browser (HAR atau `Spectra.intercept` pasif) untuk memastikan tidak ada request ke endpoint reset pada langkah 42 dan 47; pengatur jam server uji dan jam browser/perangkat (jam browser dibekukan pada langkah 3; keduanya digeser bersama 61 detik pada langkah 26, karena countdown UI berjalan di jam klien).
- State global yang diubah: jam server uji dan jam browser/perangkat. Suite berjalan serial (`parallel: false`). Pemulihan: pembekuan jam browser dilepas sebagai langkah aksi (langkah 18) dan keduanya dikembalikan ke waktu nyata di hook `after` (tetap berjalan walau spec gagal di tengah).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-39, TC-AUTH-RST-40, TC-AUTH-RST-41, TC-AUTH-RST-45, TC-AUTH-RST-46: User belum login (guest); browser web.

## Test Steps

### TC-AUTH-RST-39: Screening halaman Email Sent! saat cooldown berjalan

1. Buka jendela privat baru lalu buka halaman Reset Password (Request)
2. Ketik `budisantoso+{runId}-016@qwertysystem.net` pada field Email lalu selesaikan reCAPTCHA (centang "I'm not a robot")
3. Bekukan jam browser
4. Klik Button [Reset Password] sampai halaman Email Sent! tampil
5. Baca nilai teks "Resend in [m:ss]" segera setelah halaman Email Sent! tampil sebagai nilai awal C0
6. Verifikasi teks abu-abu "Resend in [m:ss]" menghitung mundur dari 1:00 (60 detik): nilai awal C0 adalah 1:00
7. Susuri halaman dari atas ke bawah tanpa klik apa pun
8. Verifikasi **Header**: illustration envelope/email-sent
9. Verifikasi **Header**: Title "Email Sent!"
10. Verifikasi **Body**: Message "We've sent a password reset link to budisantoso+{runId}-016@qwertysystem.net. Please check your inbox and follow the instructions."
11. Verifikasi **Body**: Helper "Didn't receive the email? Check your spam folder."
12. Verifikasi **Body**: teks countdown abu-abu "Resend in [m:ss]" (bukan tombol)
13. Verifikasi **Footer**: Button [Back to Login] tampil
14. Verifikasi **Footer**: Button [Back to Login] bergaya solid
15. Verifikasi **Footer**: Button [Back to Login] bergaya primary
16. Verifikasi **Footer**: Button [Back to Login] berlebar penuh
17. Verifikasi **Must NOT**: toast tidak muncul; Button [Resend email] dan link "Back to Reset Password" tidak tampil (anchor: Button [Back to Login] tampil)

### TC-AUTH-RST-40: Countdown Resend menurun dan teksnya tidak dapat diklik

18. Lepaskan pembekuan jam browser sehingga jam berjalan nyata
19. Tunggu 5 detik nyata lalu baca nilai teks "Resend in [m:ss]" sebagai C1
20. Verifikasi nilai countdown menurun: C1 lebih kecil dari C0
21. Periksa mail-catcher dan catat jumlah email untuk `budisantoso+{runId}-016@qwertysystem.net` sebagai baseline B1
22. Klik teks "Resend in [m:ss]"
23. Verifikasi klik teks countdown tidak memicu toast
24. Periksa mail-catcher
25. Verifikasi jumlah email untuk `budisantoso+{runId}-016@qwertysystem.net` tetap sama dengan baseline B1 (tidak ada email baru)

### TC-AUTH-RST-41: Button Resend email aktif setelah cooldown 60 detik berakhir

26. Majukan jam server dan jam browser 61 detik
27. Verifikasi teks countdown hilang
28. Verifikasi Button [Resend email] tampil enabled
29. Verifikasi Button [Resend email] bergaya text
30. Verifikasi Button [Resend email] berseverity primary
31. Verifikasi Button [Resend email] berukuran sm
32. Verifikasi link "Back to Reset Password" tidak tampil

### TC-AUTH-RST-46: Halaman Email Sent! tanpa konteks email menampilkan fallback

33. Muat ulang halaman (F5)
34. Amati Message dan area Resend
35. Verifikasi Message tampil "We've sent a password reset link to your email. Please check your inbox and follow the instructions." (bukan null atau undefined)
36. Verifikasi section Resend disembunyikan: tidak ada countdown dan tidak ada Button [Resend email]
37. Verifikasi link "Back to Reset Password" tampil
38. Verifikasi link "Back to Reset Password" bergaya text
39. Verifikasi link "Back to Reset Password" berada di tengah
40. Klik link "Back to Reset Password"
41. Verifikasi browser menuju halaman Reset Password (Request)
42. Verifikasi tidak ada request ke endpoint reset pada pengamatan network (tanpa permintaan ke server)

### TC-AUTH-RST-45: Button Back to Login menuju Login with Password

43. Pada halaman Reset Password (Request), ketik `budisantoso+{runId}-016@qwertysystem.net`, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password] sampai halaman Email Sent! tampil
44. Periksa mail-catcher dan catat jumlah email untuk `budisantoso+{runId}-016@qwertysystem.net` sebagai baseline B2 (sesudah email Request kedua)
45. Klik Button [Back to Login]
46. Verifikasi browser menuju halaman Login with Password
47. Verifikasi tidak ada request ke endpoint reset pada pengamatan network sejak klik [Back to Login]
48. Periksa mail-catcher
49. Verifikasi jumlah email untuk `budisantoso+{runId}-016@qwertysystem.net` tetap sama dengan baseline B2 (tidak ada permintaan reset baru)

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Urutan di spec: TC-AUTH-RST-46 sebelum TC-AUTH-RST-45 karena TC-AUTH-RST-46 menghapus konteks halaman (F5) dan berakhir di halaman Request, dari mana TC-AUTH-RST-45 membuka Email Sent! baru. Request kedua dilakukan setelah lebih dari 60 detik sejak Request pertama (jam sudah dimajukan 61 detik pada langkah 26) sehingga memproses token baru (bukan no-op cooldown).
- Asersi "tidak ada entri log" TC-AUTH-RST-45 (Expected butir b) diasersi di spec `TC-AUTH-RST-E2E-043-absence-not-logged` lewat aksi nyata TC-AUTH-RST-45 dengan baseline log sendiri (id TC-AUTH-RST-45 tidak ada di `sourceTc` spec 043; S-05); TC-AUTH-RST-45 tetap di `sourceTc` spec ini dan rujukannya dicatat di Notes kedua spec (S-05). Spec ini tidak mengasersi log untuk TC-AUTH-RST-45.
- Langkah penghubung (S-03): membuka jendela privat baru (langkah 1), membekukan jam browser (langkah 3) dan melepasnya (langkah 18) supaya nilai awal countdown C0 tepat 1:00 terlepas dari kecepatan eksekusi (S-14), membaca nilai awal C0 (langkah 5, diasersi pada langkah 6), dan mengamati Message dan area Resend (langkah 34) bukan asersi TC.
- Temuan untuk QA: TC-AUTH-RST-46 berstatus Manual Only karena memuat ulang halaman; dapat diotomasi dengan reload browser (F5). Post Condition TC-AUTH-RST-40 ("Token reset tidak berubah") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
- Jumlah langkah 49 melampaui ±35: alasan Verifikasi dipecah per klausa sesuai S-01 (30 dari 49 langkah adalah Verifikasi; 19 sisanya aksi dan langkah penghubung). Satu topik (halaman Email Sent! dan countdown Resend), satu kelas harness (fungsional dengan jam), tanpa prefix login berulang (tidak ada login).
