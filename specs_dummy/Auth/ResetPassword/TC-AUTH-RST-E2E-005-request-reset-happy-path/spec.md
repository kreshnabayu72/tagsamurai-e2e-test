---
id: TC-AUTH-RST-E2E-005-request-reset-happy-path
title: "Request Reset Password sukses: loading spinner, penerbitan token baru, pengiriman email, dan navigasi ke Email Sent!"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-12
  - TC-AUTH-RST-14
  - TC-AUTH-RST-28
  - TC-AUTH-RST-118
coverage:
  web: automated
---

# Request Reset Password sukses: loading spinner, penerbitan token baru, pengiriman email, dan navigasi ke Email Sent!

## Prerequisites

- User belum login (guest); browser web berada di halaman `/reset-password`.
- Environment uji terisolasi dengan akses mail-catcher untuk menangkap email reset.
- Akun uji `budisantoso@qwertysystem.net` berstatus aktif dan terdaftar di database.
- Database reset token bersih dari token aktif sebelumnya untuk akun ini.

## Test Steps

### State loading saat submit diproses

1. Buka halaman Reset Password di browser web
2. Masukkan email "budisantoso@qwertysystem.net" pada field Email
3. Selesaikan verifikasi Google reCAPTCHA v2
4. Klik tombol [Reset Password]
5. Verifikasi tombol [Reset Password] seketika beralih ke state disabled dan menampilkan spinner loading
6. Verifikasi field Email menjadi non-editable selama permintaan dikirim ke server

### Penerbitan token dan navigasi ke halaman Email Sent!

7. Tunggu respons sukses dari server
8. Verifikasi browser secara otomatis berpindah ke halaman Email Sent! (`/email-sent`)
9. Verifikasi title halaman adalah "Email Sent!"
10. Verifikasi subtitle halaman memuat alamat email yang dituju: "We've sent a link to budisantoso@qwertysystem.net to reset your password."
11. Verifikasi di database terbit sebuah record token reset baru dengan `status = 'active'`, masa berlaku 24 jam (`expires_at = created_at + 24 hours`), dan terikat ke user Budi Santoso

### Verifikasi pengiriman email dan struktur tautan reset

12. Buka layanan mail-catcher pengujian
13. Verifikasi terdapat email masuk baru yang ditujukan ke `budisantoso@qwertysystem.net`
14. Verifikasi email memuat button `[Confirm Email]` dan tautan teks fallback dengan parameter token unik
15. Klik tautan reset dari email tersebut pada tab browser baru
16. Verifikasi tautan membuka halaman Setup New Password (`/setup-new-password?token=...`)

### Request dengan format email huruf besar (Case-Insensitive)

17. Buka kembali halaman Reset Password sebagai guest
18. Masukkan email dengan huruf kapital "BUDISANTOSO@QWERTYSYSTEM.NET" pada field Email
19. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Reset Password]
20. Verifikasi pencarian user berhasil menemukan akun Budi Santoso secara case-insensitive
21. Verifikasi browser diarahkan ke halaman Email Sent! dan teks pesan menampilkan email persis seperti yang diketik "BUDISANTOSO@QWERTYSYSTEM.NET"

## Notes

- Sesuai PRD §9.2 F-AUTHRST-01/02 dan `tc-reset-password-tambahan-2.md`, alur happy path Request menerbitkan token kriptografis berdurasi 24 jam, mengirim email reset tanpa toast sukses di halaman Request, dan langsung mengarahkan pengguna ke halaman Email Sent!.
- Sesuai keputusan NC-13, pencarian email di database bersifat case-insensitive, namun pesan di UI Email Sent! mempertahankan casing yang diketik pengguna setelah trim.
