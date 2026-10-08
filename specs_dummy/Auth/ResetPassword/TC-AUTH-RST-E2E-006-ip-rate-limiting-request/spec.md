---
id: TC-AUTH-RST-E2E-006-ip-rate-limiting-request
title: "Rate limiting per alamat IP pada halaman Request: penolakan 429 dan pemulihan jendela waktu"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-35
  - TC-AUTH-RST-36
  - TC-AUTH-RST-37
coverage:
  web: automated
---

# Rate limiting per alamat IP pada halaman Request: penolakan 429 dan pemulihan jendela waktu

## Prerequisites

- User belum login (guest); browser web berada di halaman `/reset-password`.
- Environment uji terisolasi dengan kemampuan penyetelan counter IP atau simulasi header IP client (`Mode: mock`).
- Batas rate limit IP terkonfigurasi maksimal 20 request per jam per IP.
- Akun uji terdaftar `budisantoso@qwertysystem.net` dan email tidak terdaftar `belumterdaftar@qwertysystem.net`.

## Test Steps

### Kenaikan counter per IP untuk berbagai jenis Request

1. Lakukan request reset ke-1 s/d ke-10 menggunakan email terdaftar `budisantoso@qwertysystem.net` dengan reCAPTCHA valid
2. Verifikasi counter request per IP bertambah 10 kali
3. Lakukan request reset ke-11 s/d ke-15 menggunakan email tidak terdaftar `belumterdaftar@qwertysystem.net` dengan reCAPTCHA valid
4. Verifikasi counter request per IP bertambah 5 kali (total 15), membuktikan email tidak terdaftar tetap menaikkan counter IP
5. Lakukan request reset ke-16 s/d ke-20 menggunakan email akun Inactive `tonokurniawan@qwertysystem.net` dengan reCAPTCHA valid
6. Verifikasi counter request per IP bertambah 5 kali (mencapai batas kuota 20 dalam 1 jam)

### Penolakan HTTP 429 pada request ke-21 dari IP yang sama

7. Buka halaman Reset Password di browser web
8. Masukkan email "budisantoso@qwertysystem.net" pada field Email
9. Selesaikan verifikasi reCAPTCHA
10. Klik tombol [Reset Password] untuk mengirimkan request ke-21 dalam jendela 1 jam yang sama
11. Verifikasi server mengembalikan status HTTP 429 Too Many Requests
12. Verifikasi Alert Danger tampil tepat di atas tombol [Reset Password] dengan teks "Too many requests. Please try again later."
13. Verifikasi input pada field Email tetap dipertahankan ("budisantoso@qwertysystem.net")
14. Verifikasi tombol [Reset Password] tetap dalam keadaan enabled (tidak disabled)
15. Verifikasi widget Google reCAPTCHA v2 di-reset kembali ke status belum dicentang
16. Buka Activity Log Session dan User Log menggunakan sesi admin
17. Verifikasi penolakan rate limit per IP tidak dicatat di kedua surface log (zero-logging)

### Penolakan 429 identik untuk email terdaftar maupun tidak terdaftar

18. Pada halaman yang sama yang masih terkena batas IP, ganti isi field Email dengan "belumterdaftar@qwertysystem.net"
19. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Reset Password]
20. Verifikasi respon server dan UI tetap identik: Alert Danger "Too many requests. Please try again later." tampil, tanpa membocorkan ada atau tidaknya akun di database

### Pemulihan setelah jendela 1 jam berakhir

21. Simulasikan jendela waktu bergulir 1 jam telah berlalu (waktu server dimajukan >60 menit)
22. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Reset Password]
23. Verifikasi request berhasil diproses kembali dan diarahkan ke halaman Email Sent!

## Notes

- Sesuai PRD §9.2 F-AUTHRST-06 Operasional, `RSTPWD-LOGIC-04d`, `RSTPWD-LOGIC-04e`, dan `auth-foundation.md` §3.2, penolakan 429 per IP pada form pra-autentikasi berupa Alert Danger inline di atas tombol submit dengan teks "Too many requests. Please try again later.".
- Pengecekan batas IP dilakukan sebelum lookup email di database sehingga penolakan 429 tidak membocorkan status registrasi email.
