---
id: TC-AUTH-RST-E2E-028-submit-success-and-already-used
title: "Submit New Password Sukses, Halaman Hasil, Tautan Already Used, dan Request Tanpa Cooldown"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-81
  - TC-AUTH-RST-82
  - TC-AUTH-RST-83
  - TC-AUTH-RST-84
  - TC-AUTH-RST-85
  - TC-AUTH-RST-86
  - TC-AUTH-RST-143
coverage:
  web: automated
---

# Submit New Password Sukses, Halaman Hasil, Tautan Already Used, dan Request Tanpa Cooldown

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek `Budi Santoso` (`budisantoso+{runId}-028@qwertysystem.net`) dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password aktif `Spectra.env.RST_PASSWORD`; satu token reset aktif diterbitkan di hook `before` lewat API Request (waktu terbitnya dicatat sebagai T0; jam dibekukan pada T0 + 30 detik sebelum Submit dan dipulihkan sebelum admin membuka log, agar TC-AUTH-RST-143 menguji pembatalan cooldown di dalam jendela 60 detik), tautan diambil dari mail-catcher. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`.
- Hook `before` (akun aktor): membuka jendela privat guest dan jendela privat admin; di jendela admin login sebagai akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` (selesaikan reCAPTCHA) lalu membuka Global Settings > Activity Log > Session dengan Filter Activity = "Reset Password" dan Global Settings > User > Detail > User Log untuk user "Budi Santoso", kemudian mencatat jumlah baris Success milik user "Budi Santoso" pada kedua surface sebagai baseline (dicatat sesudah seeding token dan sebelum Submit). Hook `after` menutup kedua jendela, mengembalikan sesi ke akun default suite, dan memulihkan jam.
- State global yang diubah: jam server dan jam browser (dibekukan pada T0 + 30 detik di langkah 3, dipulihkan di langkah 11 sebelum admin membuka Activity Log Session dan User Log, dibekukan lagi pada T0 + 50 detik di langkah 35, dan dipulihkan di langkah 45). Suite berjalan serial (`parallel: false`); jam server dan jam browser dipulihkan di langkah 11 dan 45 serta di hook `after`; baseline log dicatat di hook `before` sebelum jam digeser.
- Kemampuan teknis: mail-catcher dengan pencatatan jumlah email per alamat; atur dan bekukan jam server dan jam browser; reCAPTCHA mode uji; pelambatan respons endpoint Submit (network throttle atau `Spectra.intercept` yang menahan lalu meneruskan ke backend nyata); jendela guest dan jendela admin terpisah (admin membaca Activity Log Session dan User Log).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat suite.md); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-81 sampai TC-AUTH-RST-86 dan TC-AUTH-RST-143: User belum login (guest); browser web.
- Data: Password dan Confirm Password `Spectra.env.RST_PASSWORD_NEW`.

## Test Steps

### TC-AUTH-RST-81: Button Reset Password menampilkan loading dan disabled selama submit

1. Di jendela guest buka tautan reset milik `budisantoso+{runId}-028@qwertysystem.net` dari mail-catcher sehingga Setup New Password tampil
2. Ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password
3. Bekukan jam server dan jam browser pada T0 + 30 detik
4. Perlambat respons endpoint Submit lalu klik Button [Reset Password]
5. Amati Button [Reset Password] sebelum respons server tiba
6. Verifikasi Button [Reset Password] disabled selama proses
7. Verifikasi loading spinner memutar pada Button [Reset Password] selama proses

### TC-AUTH-RST-82: Submit sukses menyimpan password, mengonsumsi token, dan menampilkan Password Reset Successful

8. Lepaskan respons server yang ditahan
9. Verifikasi browser menuju halaman Password Reset Successful
10. Verifikasi tidak ada toast
11. Pulihkan jam server dan jam browser ke waktu nyata
12. Pindah ke jendela admin, muat ulang Activity Log Session, dan buka Global Settings > User > Detail > User Log untuk user "Budi Santoso"
13. Verifikasi jumlah baris Success milik user "Budi Santoso" bertambah 1 dibanding baseline pada kedua surface
14. Verifikasi terdapat entri Success milik user "Budi Santoso" dengan Activity `Reset Password`, Status Success, Note `Password updated successfully` pada kedua surface (dicari berdasarkan Note dan user, bukan posisi teratas)
15. Pindah ke jendela guest

### TC-AUTH-RST-83: Screening halaman Password Reset Successful

16. Susuri halaman dari atas ke bawah tanpa klik apa pun
17. Verifikasi **Header**: illustration check-success
18. Verifikasi **Header**: Title "Password Reset Successful"
19. Verifikasi **Body**: Message "Your password has been reset successfully. You can now log in with your new credentials."
20. Verifikasi **Footer**: Button [Go to Login Page] tampil
21. Verifikasi **Footer**: Button [Go to Login Page] bergaya solid
22. Verifikasi **Footer**: Button [Go to Login Page] bergaya primary
23. Verifikasi **Footer**: Button [Go to Login Page] berlebar penuh
24. Verifikasi **Must NOT**: Button [Reset Password], Button [Resend email], dan field password tidak tampil (anchor: Button [Go to Login Page] tampil)

### TC-AUTH-RST-84: Button Go to Login Page menuju Login with Password

25. Klik Button [Go to Login Page]
26. Verifikasi browser menuju halaman Login with Password

### TC-AUTH-RST-85: Tautan yang sudah dipakai membuka Halaman 404 varian Already Used

27. Buka tautan reset yang sama dari email
28. Verifikasi Halaman 404 tampil dengan Title "Reset Link Already Used"
29. Verifikasi Message "This password reset link has already been used. Your password has been updated."
30. Verifikasi Button [Go to Login] tampil
31. Verifikasi Button [Request New Link] tidak tampil
32. Verifikasi Setup New Password tidak dirender

### TC-AUTH-RST-86: Button Go to Login pada Halaman 404 varian Already Used menuju Login with Password

33. Klik Button [Go to Login]
34. Verifikasi browser menuju halaman Login with Password

### TC-AUTH-RST-143: Request reset langsung setelah Setup New Password sukses diproses tanpa cooldown

35. Atur jam server dan jam browser ke T0 + 50 detik lalu bekukan (20 detik sejak Submit sukses pada T0 + 30 detik)
36. Buka halaman Reset Password lewat Login → [Forgot password?] (jam masih beku sehingga kurang dari 60 detik sejak Submit sukses)
37. Catat jumlah email di mail-catcher untuk `budisantoso+{runId}-028@qwertysystem.net` sebagai baseline
38. Ketik `budisantoso+{runId}-028@qwertysystem.net` pada field Email, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password]
39. Verifikasi browser menuju halaman Email Sent!
40. Verifikasi tidak ada toast
41. Periksa mail-catcher
42. Verifikasi jumlah email di mail-catcher untuk `budisantoso+{runId}-028@qwertysystem.net` bertambah 1 dibanding baseline (email reset baru diterima, bukan no-op)
43. Buka tautan dari email baru
44. Verifikasi tautan dari email baru membuka Setup New Password
45. Pulihkan jam server dan jam browser

## Notes

- Sumber: `auth/reset-password/TestCases/tc-reset-password.md`. Satu alur berurutan pada satu token: submit (dengan throttle), halaman hasil, tautan Already Used, lalu Request baru.
- Subjudul TC-AUTH-RST-82 sampai 86 memetakan langkah ke id TC; langkah TC-AUTH-RST-82 mengandalkan submit yang sama dengan TC-AUTH-RST-81 (satu klik, tidak diulang).
- Temuan untuk QA: TC-AUTH-RST-143 menyebut tautan "[Forgot password?]" di Login, sedangkan TC-AUTH-RST-04 menyebut tautan "[Reset here]"; label tautan menuju Reset Password perlu disamakan (S-15). Langkah ini mengikuti TC-AUTH-RST-143.
- TC-AUTH-RST-143 menyatakan 60 detik sejak Submit; supaya tidak bergantung pada kecepatan eksekusi, jam server dan jam browser dibekukan pada T0 + 30 detik sebelum Submit, dipulihkan sebelum admin membaca log (S-09), lalu dibekukan lagi pada T0 + 50 detik untuk blok TC-AUTH-RST-143 dan dipulihkan di akhir (konvensi bagian 6).
- Langkah penghubung (S-03): pindah jendela guest dan admin, muat ulang log, serta pemulihan dan pembekuan ulang jam.
- Temuan untuk QA: Post Condition TC-AUTH-RST-82 (password user menjadi baru, token consumed, lock progression dan counter dibersihkan), TC-AUTH-RST-85 (token tetap consumed), dan TC-AUTH-RST-143 (token baru terbit, counter per email 24 jam bernilai 1) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
- Jumlah langkah 45 melampaui ±35: alasan Verifikasi dipecah per klausa sesuai S-01 (25 dari 45 langkah adalah Verifikasi; 20 sisanya aksi dan langkah penghubung: perpindahan jendela, muat ulang log, jam). Satu topik (Submit sukses dan akibatnya pada satu token), satu kelas harness (fungsional; jendela admin membaca log, jam dibekukan), tanpa prefix login berulang (tidak ada login).
