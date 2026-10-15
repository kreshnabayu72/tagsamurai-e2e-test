---
id: TC-AUTH-OTP-E2E-044-defense-in-depth-kuota-resend
title: "Defense-in-Depth setelah Kuota Resend Habis: Resend Langsung, Request Tanpa Entry, Hapus Data Browser, dan Entry edit_email"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-163
  - TC-AUTH-OTP-171
  - TC-AUTH-OTP-162
  - TC-AUTH-OTP-178
coverage:
  web: automated
---

# Defense-in-Depth setelah Kuota Resend Habis: Resend Langsung, Request Tanpa Entry, Hapus Data Browser, dan Entry edit_email

## Prerequisites

- Mode: FE+BE.
- Password user uji dari `Spectra.env.OTP_PASSWORD` (hanya dipakai saat seeding user lewat API). Tidak ada password atau token di spec atau fixture.
- Environment variable: `OTP_PASSWORD`.
- Kemampuan teknis: klien HTTP untuk mengirim request langsung ke endpoint Request OTP dan Resend modul ini sesuai kontrak di `auth/login-otp/API/openapi.yaml` (melewati UI yang menonaktifkan tombol), termasuk token reCAPTCHA valid mode uji dan atribut `entry`; percepatan jam server untuk melewati countdown Resend 60 detik (lima kali) dan cooldown 10 menit; kemampuan menghapus cookie dan local storage jendela privat; mail-catcher lingkungan uji untuk membaca kode OTP dan memeriksa tidak ada email baru; reCAPTCHA mode uji. Jam server dipulihkan di hook `after`.
- Jam yang diatur (konvensi bagian 6): jam server dan jam browser (klien) dimajukan bersama, karena countdown Resend di UI berjalan di jam klien sehingga memajukan jam server saja tidak mengaktifkan [Resend code]. Hook `after` memulihkan kedua jam. Suite berjalan serial (`parallel: false`) karena jam server digeser.
- Hook `before` (seeding API) membuat satu user profil BASE (Activated, Active ON, sudah login web di device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru sudah ada) dengan suffix per run `+{runId}-044`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian): `Rafi Pratama` (`rafipratama+{runId}-044@qwertysystem.net`). Satu user dan satu sesi email-request dengan kuota Resend habis dipakai bersama oleh keempat blok TC, karena menghabiskan kuota butuh lima kali Resend; ini mengubah TC sumber yang masing-masing memakai user sendiri (lihat Notes).
- Tanpa login pada semua langkah uji: halaman Login with OTP adalah halaman publik, tidak ada sesi aktif di jendela privat.

## Test Steps

### Persiapan: menghabiskan kuota Resend dan melewati cooldown 10 menit (langkah 1 sampai 15 TC-AUTH-OTP-163, 171, 162, dan 178)

1. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
2. Ketik `rafipratama+{runId}-044@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Majukan jam server dan jam browser 60 detik sehingga countdown Resend selesai
6. Klik [Resend code] (Resend ke-1)
7. Majukan jam server dan jam browser 60 detik sehingga countdown Resend selesai
8. Klik [Resend code] (Resend ke-2)
9. Majukan jam server dan jam browser 60 detik sehingga countdown Resend selesai
10. Klik [Resend code] (Resend ke-3)
11. Majukan jam server dan jam browser 60 detik sehingga countdown Resend selesai
12. Klik [Resend code] (Resend ke-4)
13. Majukan jam server dan jam browser 60 detik sehingga countdown Resend selesai
14. Klik [Resend code] (Resend ke-5)
15. Majukan jam server dan jam browser 10 menit sehingga cooldown selesai

### TC-AUTH-OTP-163: Resend yang dikirim langsung ke server setelah kuota habis ditolak

16. Kirim permintaan Resend langsung ke server untuk sesi yang sama (melewati UI yang menonaktifkan tombol)
17. Verifikasi permintaan ditolak server
18. Verifikasi tidak ada email OTP baru terkirim di mail-catcher untuk `rafipratama+{runId}-044@qwertysystem.net`
19. Verifikasi area Resend tetap pada state Exhausted: button [Resend code] disabled
20. Verifikasi area Resend tetap pada state Exhausted: teks "You've used all your resend attempts for this code. Edit your email to request a new one."

### TC-AUTH-OTP-171: Request OTP langsung ke server tanpa atribut entry setelah kuota habis ditolak

21. Kirim Request OTP langsung ke server untuk email `rafipratama+{runId}-044@qwertysystem.net` tanpa atribut `entry` (dengan token reCAPTCHA valid)
22. Verifikasi permintaan diperlakukan sebagai `login_password`
23. Verifikasi permintaan ditolak: respons berisi penolakan batas permintaan
24. Verifikasi tidak ada email OTP baru terkirim di mail-catcher untuk `rafipratama+{runId}-044@qwertysystem.net`
25. Verifikasi kuota resend tidak ter-reset: area Resend pada layar Verify OTP tetap pada state Exhausted

### TC-AUTH-OTP-162: Menghapus data browser tidak mereset kuota resend

26. Hapus cookie dan local storage jendela privat
27. Buka kembali halaman Request OTP, ketik `rafipratama+{runId}-044@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", klik button [Request OTP]
28. Verifikasi Request OTP ditolak dengan Alert inline di atas button [Request OTP]: "Too many requests. Please try again later."
29. Verifikasi tidak ada email OTP baru di mail-catcher untuk `rafipratama+{runId}-044@qwertysystem.net`
30. Verifikasi kuota resend email yang sama tidak ter-reset

### TC-AUTH-OTP-178: Request OTP langsung dengan entry edit_email tanpa Edit email sungguhan diterima apa adanya dan memulai sesi baru

31. Kirim Request OTP langsung ke server untuk email `rafipratama+{runId}-044@qwertysystem.net` dengan atribut `entry` = `edit_email` tanpa melewati alur Edit email (dengan token reCAPTCHA valid)
32. Verifikasi permintaan diterima apa adanya (atribut `entry` tidak diverifikasi terhadap riwayat Edit email)
33. Verifikasi email OTP baru terkirim di mail-catcher untuk `rafipratama+{runId}-044@qwertysystem.net`
34. Verifikasi kuota resend ter-reset sebagai sesi baru: respons memuat cooldown awal 60 detik (`resendCooldownSeconds`), bukan state Exhausted
35. Verifikasi IP rate limit tetap berlaku
36. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Kelas harness a (defense-in-depth: request langsung ke server). Keempat TC sumber masing-masing memakai user sendiri dengan 14 langkah persiapan yang sama (lima kali Resend lalu cooldown 10 menit). Spec ini menyatukan persiapan itu pada satu user supaya sesi kuota habis hanya dibangun sekali, sehingga langkah 1 sampai 15 mewakili langkah 1 sampai 15 keempat TC (S-04). Ini pengecualian P-3 (user berurutan): kuota Resend habis dan cooldown 10 menit tidak bisa diulang tanpa biaya besar. Akibatnya urutan TC di dalam spec berbeda dari nomor TC: TC-AUTH-OTP-163, 171, 162, lalu 178; TC-AUTH-OTP-178 terakhir karena menghancurkan sesi kuota habis dengan memulai sesi baru (S-05, S-10, prinsip 5 konvensi: aksi yang merusak state ditaruh di akhir).
- TC-AUTH-OTP-162 dan 171 memeriksa penolakan yang tidak mengubah state, sehingga boleh dijalankan berurutan di sesi kuota yang sama; TC-AUTH-OTP-162 menghapus cookie dan local storage setelah TC-AUTH-OTP-171 dan sebelum TC-AUTH-OTP-178.
- Langkah penghubung (S-03): memajukan jam server dan jam browser serta mengklik Resend pada persiapan, serta menghapus cookie dan local storage pada langkah 26 dan memulihkan jam pada langkah 36, ditulis sebagai aksi tanpa `Verifikasi`.
- Spec ini 36 langkah, di atas batas smell sekitar 35 langkah, dan butuh jam server dan jam browser dimajukan total 15 menit; keduanya dipulihkan ke waktu nyata pada langkah 36 (hook `after` tetap menjadi cadangan) karena seluruh TC memerlukan state Exhausted yang bergantung pada jam yang sudah maju.
- Temuan untuk QA: (1) Expected TC-AUTH-OTP-171 menyebut "respons berisi penolakan batas permintaan" tanpa menyebut kode error atau pesan; spec mengasersi penolakan sebagaimana tertulis. (2) Expected TC-AUTH-OTP-178 "kuota resend ter-reset (sesi baru)" tidak punya indikator yang terlihat di UI karena request dikirim langsung; spec membaca indikatornya dari respons berupa cooldown awal 60 detik (`resendCooldownSeconds`, disebut di `auth/login-otp/API/openapi.yaml`), dan "IP rate limit tetap berlaku" tidak memuat langkah pemicu limit; spec hanya mengasersinya apa adanya tanpa memicu flood (flood dicakup di spec rate limit IP); akibatnya langkah "IP rate limit tetap berlaku" tidak punya langkah menuju keadaannya (S-14) karena TC tidak menyebut pemicunya. (3) TC-AUTH-OTP-171 menyatakan "kuota resend tidak ter-reset" tanpa observable; spec menafsirkannya sebagai area Resend pada layar Verify OTP tetap pada state Exhausted (langkah 25), padahal request dikirim langsung ke server dan layar Verify OTP yang dipakai berasal dari sesi UI sebelumnya. (4) TC-AUTH-OTP-162 Expected b "kuota resend email yang sama tidak ter-reset" (langkah 30) tidak menyebut observable; spec hanya mengikuti kalimat TC tanpa mekanisme pengamatan sendiri, sehingga langkah 30 baru bisa diverifikasi bila QA menetapkan indikatornya (misalnya state Exhausted pada respons atau layar). (5) Asumsi urutan P-3: TC-AUTH-OTP-163, 171, 162, dan 178 masing-masing memakai user dan sesi sendiri di TC, tetapi spec menjalankannya berurutan pada satu user dan satu sesi kuota habis; TC tidak menyatakan bahwa 163, 171, dan 162 tidak mengubah state sesi (penolakan tidak menambah hitungan), dan bahwa 178 sengaja terakhir. (6) TC-AUTH-OTP-162 langkah 16 menghapus data browser setelah halaman Verify OTP terbuka; TC tidak menyebut apakah layar Verify OTP masih ada, spec membuka kembali halaman Request OTP seperti pada langkah 17 TC.
