---
id: TC-AUTH-RST-E2E-006-ip-rate-limiting-request
title: "Rate limiting per alamat IP pada halaman Request: penolakan 429, cooldown menambah counter, dan sliding window"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-35
  - TC-AUTH-RST-36
  - TC-AUTH-RST-37
  - TC-AUTH-RST-138
  - TC-AUTH-RST-142
coverage:
  web: automated
---

# Rate limiting per alamat IP pada halaman Request: penolakan 429, cooldown menambah counter, dan sliding window

## Prerequisites

- User belum login (guest); browser web berada di halaman `/reset-password`.
- Environment uji terisolasi dengan kemampuan penyetelan counter IP atau simulasi header IP client (`Mode: mock`).
- Batas rate limit IP terkonfigurasi maksimal 20 request per jam per IP.
- Akun uji terdaftar `budisantoso@qwertysystem.net`, email tidak terdaftar `belumterdaftar@qwertysystem.net`, dan email akun Inactive `tonokurniawan@qwertysystem.net`.

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

### Request di dalam cooldown tetap menambah counter per IP (TC-142)

21. Setel counter per IP tercatat 19 request dalam 1 jam terakhir; user `budisantoso@qwertysystem.net` baru saja melakukan Request berhasil kurang dari 60 detik lalu sehingga cooldown 60 detik masih berjalan (fixture BE)
22. Buka halaman Reset Password, masukkan "budisantoso@qwertysystem.net", selesaikan reCAPTCHA, lalu klik [Reset Password] (Request berada di dalam cooldown)
23. Verifikasi halaman Email Sent! tampil tanpa toast dan tidak ada email reset baru di mail-catcher (no-op cooldown, Request tetap dihitung ke counter per IP)
24. Ganti field Email dengan "dewilestari@qwertysystem.net", selesaikan reCAPTCHA, lalu klik [Reset Password]
25. Verifikasi Request ini menjadi Request ke-21 yang ditolak dengan Alert Danger "Too many requests. Please try again later."
26. Verifikasi counter per email Budi tidak bertambah oleh Request di dalam cooldown

### Pemulihan sliding window per IP saat Request tertua melewati 1 jam (TC-138)

27. Simulasikan kondisi counter per IP 20 request dengan Request tertua pada T0 dan 19 request lainnya pada T0+59 menit (fixture BE)
28. Majukan waktu server ke T0+1 jam 1 menit sehingga Request tertua keluar dari jendela bergulir 1 jam
29. Buka halaman Reset Password, masukkan "budisantoso@qwertysystem.net", selesaikan reCAPTCHA, lalu klik [Reset Password]
30. Verifikasi request tidak ditolak 429 karena jendela bergulir dan Request tertua sudah keluar, diproses sukses menuju halaman Email Sent!, dan email reset baru terbit untuk Budi

## Notes

- Sesuai PRD §9.2 F-AUTHRST-06 Operasional, `RSTPWD-LOGIC-04d`, `RSTPWD-LOGIC-04e`, dan `auth-foundation.md` §3.2, penolakan 429 per IP pada form pra-autentikasi berupa Alert Danger inline di atas tombol submit dengan teks "Too many requests. Please try again later.".
- Pengecekan batas IP dilakukan sebelum lookup email di database sehingga penolakan 429 tidak membocorkan status registrasi email.
- Request di dalam cooldown 60 detik tetap dihitung ke counter per IP (`TC-AUTH-RST-142`), namun tidak menambah counter per email (NC-01). Pemulihan memakai jendela bergulir 1 jam (`TC-AUTH-RST-138`), di mana Request tertua keluar begitu melewati 1 jam.