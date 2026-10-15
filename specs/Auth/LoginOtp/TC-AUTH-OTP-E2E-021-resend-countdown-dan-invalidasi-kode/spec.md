---
id: TC-AUTH-OTP-E2E-021-resend-countdown-dan-invalidasi-kode
title: "Countdown Resend 60 Detik, Resend Menerbitkan Kode Baru, dan Invalidasi Kode Lama"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-77
  - TC-AUTH-OTP-78
  - TC-AUTH-OTP-52
  - TC-AUTH-OTP-53
  - TC-AUTH-OTP-67
coverage:
  web: automated
---

# Countdown Resend 60 Detik, Resend Menerbitkan Kode Baru, dan Invalidasi Kode Lama

## Prerequisites

- Mode: FE+BE.
- Tanpa login (halaman publik, tidak ada sesi aktif di browser). reCAPTCHA memakai mode uji environment.
- Environment variable: `OTP_PASSWORD` (password yang dipasang ke user uji saat seeding aktivasi; tidak dipakai langkah uji).
- Kemampuan teknis:
  - Mail-catcher lingkungan uji untuk membaca email dan kode OTP 6 digit.
  - Percepatan jam (§6): setiap langkah "Tunggu countdown 60 detik selesai" dipenuhi dengan memajukan jam server uji dan jam browser (countdown UI berjalan di jam klien) bersama sebesar 60 detik, lalu menunggu UI menyegarkan state tombol Resend. Jam server dan jam browser diatur bersama dan tidak ada tunggu waktu nyata. Spec ini mengubah state global (jam), sehingga suite berjalan serial (`parallel: false`), dan hook `after` memulihkan keduanya.
- Hook `before` (seeding API, email bersuffix per run) membuat user Activated dengan Toggle Active ON, profil BASE (sudah login web dalam 30 hari terakhir pada device dikenal, persetujuan Privacy Policy versi terbaru ada, MFA tidak aktif; Tabel Data Uji Pre-setup #2). Pengguna dan peruntukannya:
  - TC-AUTH-OTP-77, 78, 52, 53 (satu alur berurutan pada satu sesi email-request): `Wulan Lubis` (`wulanlubis+{runId}-021@qwertysystem.net`).
  - TC-AUTH-OTP-67: `Intan Damayanti` (`intandamayanti+{runId}-021@qwertysystem.net`).
- Kode salah yang diketik pada TC-AUTH-OTP-67 adalah `000000` (kode yang berbeda dari kode yang diterbitkan untuk user itu), 3 kali per kode.
- Hook `after`: kembalikan jam server dan jam browser uji ke waktu nyata, tutup sesi login yang terbentuk, dan hapus kedua user. Hook ini tetap jalan walau spec gagal di tengah.

## Test Steps

### TC-AUTH-OTP-77: Tombol Resend disabled dengan countdown selama 60 detik pertama lalu aktif

1. Buka halaman `Auth > Login with OTP > Request OTP` di jendela privat baru (tanpa sesi)
2. Ketik `wulanlubis+{runId}-021@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Verifikasi halaman Verify OTP tampil
6. Verifikasi area Resend menampilkan teks "Resend code in (00:59)"
7. Verifikasi teks "Resend code in" dalam keadaan disabled
8. Verifikasi hitung mundur berkurang tiap detik
9. Klik teks "Resend code in" selama countdown berjalan
10. Verifikasi tidak ada email OTP baru di mail-catcher
11. Verifikasi tidak ada toast
12. Tunggu countdown 60 detik selesai
13. Verifikasi tampil button [Resend code]
14. Verifikasi button [Resend code] berupa variant text dengan severity primary
15. Verifikasi button [Resend code] dalam keadaan enabled
16. Catat kode OTP pertama dari email yang masuk ke mail-catcher

### TC-AUTH-OTP-78: Resend berhasil menerbitkan kode baru dan memulai ulang countdown

17. Klik [Resend code]
18. Verifikasi toast sukses: "Success, the code has been sent." di kanan bawah layar
19. Verifikasi area Resend kembali ke State A: teks "Resend code in (00:59)" tampil
20. Verifikasi area Resend State A dalam keadaan disabled
21. Periksa mail-catcher untuk `wulanlubis+{runId}-021@qwertysystem.net` dan hitung jumlah email OTP
22. Verifikasi email OTP baru dengan kode berbeda dari kode pertama diterima di `wulanlubis+{runId}-021@qwertysystem.net`
23. Verifikasi mail-catcher memuat tepat 2 email OTP (1 dari Request OTP dan 1 dari Resend)

### TC-AUTH-OTP-52: Kode lama ditolak setelah Resend menerbitkan kode baru

24. Ketik kode OTP pertama (yang dicatat pada langkah 16) pada kotak digit
25. Verifikasi kode pertama ditolak walau belum lewat 5 menit: kotak digit menampilkan shake animation
26. Verifikasi kotak digit berborder severity danger
27. Verifikasi caption error di bawah kotak digit: "Invalid code"
28. Verifikasi tidak ada sesi yang dibuat (layar tetap Verify OTP, tidak dialihkan ke Portal — Product Hub)

### TC-AUTH-OTP-53: Kode baru dari Resend diterima untuk login

29. Ketik 6 digit kode OTP kedua dari email terbaru pada kotak digit
30. Verifikasi verifikasi berhasil
31. Verifikasi browser dialihkan ke Portal — Product Hub
32. Verifikasi sesi aktif untuk `Wulan Lubis`

### TC-AUTH-OTP-67: Hitungan salah verify dihitung per kode dan dimulai ulang setelah Resend

33. Logout dari Portal — Product Hub, lalu buka halaman `Auth > Login with OTP > Request OTP` di jendela privat baru (tanpa sesi)
34. Ketik `intandamayanti+{runId}-021@qwertysystem.net` pada field Email
35. Centang widget reCAPTCHA "I'm not a robot"
36. Klik button [Request OTP]
37. Ketik 3 kali kode yang salah (`000000`) pada kotak digit
38. Verifikasi setiap percobaan ditolak dengan caption error di bawah kotak digit: "Invalid code"
39. Tunggu countdown 60 detik selesai
40. Klik [Resend code]
41. Ketik 3 kali kode yang salah (`000000`) pada kode baru
42. Verifikasi setiap percobaan ditolak dengan caption error di bawah kotak digit: "Invalid code"
43. Ketik 6 digit kode OTP dari email pada kotak digit (kode kedua dari email)
44. Verifikasi kode kedua yang benar diterima walau total percobaan salah di sesi ini 6 kali
45. Verifikasi browser dialihkan ke Portal — Product Hub
46. Verifikasi sesi aktif untuk `Intan Damayanti`

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Pengecualian P-3 (user berurutan, `docs/e2e-conventions.md` §3): TC-77, 78, 52, 53 di sumber memakai empat user berbeda (`Wulan Lubis`, `Galih Suryani`, `Kartika Harahap`, `Budi Kusuma`) tetapi urutan aksinya satu alur sesi email-request yang sama (Request OTP, Resend, kode lama ditolak, kode baru diterima). Spec memakai satu user (`Wulan Lubis`) supaya hanya ada satu kali tunggu countdown per aksi; `Intan Damayanti` (TC-67) tetap user terpisah karena membutuhkan kode yang belum terpakai.
- Langkah penghubung (S-03): langkah 16 (mencatat kode pertama di akhir TC-77, setelah asersi countdown dan sebelum Resend, karena di TC-52 kode itu baru dibaca setelah Resend; pencatatan tidak ditempatkan di awal supaya asersi "(00:59)" langsung mengikuti tampilnya halaman Verify OTP), langkah 33 (logout dan membuka konteks bersih setelah login sukses di TC-53).
- Langkah 21 sampai 23 mengikuti TC-78 langkah 8 dan Expected e: mail-catcher dihitung setelah Resend; asersi layar (langkah 18 sampai 20) ditempatkan sebelum mail-catcher dibuka (S-14).
- Toast Resend pada TC-53 a (sumber TC-53 menulis Resend sendiri) sudah diasersi pada langkah 18 karena aksi Resend-nya sama dengan TC-78.
- Asersi absence: Expected d TC-78 ("tidak ada entri log baru" di `Global Settings > Activity Log > Session` dan `User Log`) dipindah ke spec absence E2E-047 (kelas g, S-05).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Temuan untuk QA:
  - TC-52 Expected a dan TC-67 hanya menulis "ditolak"; caption "Invalid code" diambil dari TC-52 Expected b dan NC-01, dan dipakai juga untuk percobaan salah di TC-67.
  - TC-77, 78, 52, 53 tidak menyebut cara melewati countdown 60 detik; spec menulisnya sebagai "Tunggu countdown" dengan kemampuan percepatan jam server dan jam browser di Prerequisites.
  - TC-77, 78, 52, 53 di sumber berdiri sendiri dengan empat user, dan TC tidak menyatakan bahwa Resend, penolakan kode lama, dan penerimaan kode baru dijalankan berurutan pada satu sesi email-request; spec mengasumsikan urutan itu (P-3).
  - TC-78 Post Condition b ("Kode sebelumnya tidak dapat dipakai lagi") tidak punya langkah observasi di TC-78; spec tidak mengasersinya di blok TC-AUTH-OTP-78, sedangkan penolakan kode pertama diasersi di blok TC-AUTH-OTP-52 (langkah 24 sampai 28).
  - Post Condition TC-52 a (Failed `Incorrect OTP`, detail pada TC Logging) tidak punya langkah observasi di TC, sehingga tidak diasersi di spec ini; pencatatan itu diuji di spec pencatatan Verify OTP.
