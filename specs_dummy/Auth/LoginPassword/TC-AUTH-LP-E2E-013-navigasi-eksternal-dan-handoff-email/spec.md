---
id: TC-AUTH-LP-E2E-013-navigasi-eksternal-dan-handoff-email
title: Navigasi ke Login with OTP dan Reset Password dengan prefilled email
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-05
  - TC-AUTH-LP-93
  - TC-AUTH-LP-94
  - TC-AUTH-LP-95
  - TC-AUTH-LP-96
coverage:
  web: automated
---

# Navigasi ke Login with OTP dan Reset Password dengan prefilled email

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- Email `budisantoso@qwertysystem.net` tersedia sebagai data uji prefill.

## Test Steps

### Navigasi ke Login with OTP dengan membawa Email

1. Buka halaman Login with Password di browser web
2. Ketik email `budisantoso@qwertysystem.net` pada field Email
3. Klik link [Log in with OTP] pada footer form login
4. Verifikasi browser membuka halaman Login with OTP
5. Verifikasi field Email pada halaman Login with OTP terisi otomatis dengan `budisantoso@qwertysystem.net`

### Navigasi dengan format Email yang belum lengkap

6. Kembali ke halaman Login with Password
7. Ketik email dengan format belum lengkap `john@` pada field Email
8. Klik link [Log in with OTP]
9. Verifikasi halaman Login with OTP terbuka dengan field Email terisi `john@` apa adanya
10. Verifikasi tidak ada pesan error validasi format yang muncul akibat perpindahan halaman

### Navigasi ke Reset Password dengan membawa Email

11. Kembali ke halaman Login with Password
12. Ketik email `budisantoso@qwertysystem.net` pada field Email
13. Klik link "Forgot your password? " [Reset here]
14. Verifikasi browser membuka halaman Reset Password
15. Verifikasi field Email pada halaman Reset Password terisi otomatis dengan `budisantoso@qwertysystem.net`

### Lifecycle penyimpanan email sementara (Session Storage isolation)

16. Tutup tab browser yang sedang membuka halaman login
17. Buka kembali halaman Login with Password pada tab baru
18. Verifikasi field Email kosong dan menampilkan placeholder default "Enter your email"

### Alur balik dari Login with OTP via tombol Edit email

19. Buka halaman Login with OTP
20. Masukkan email `budisantoso@qwertysystem.net` lalu submit hingga tahap pengisian kode OTP muncul
21. Klik link / tombol "Edit email" pada layar kode OTP
22. Beralih kembali ke halaman Login with Password
23. Verifikasi field Email pada halaman Login with Password otomatis terisi `budisantoso@qwertysystem.net`
24. Verifikasi field Email tetap dapat diedit dan tidak berstatus read-only

## Notes

- Mekanisme pembawaan email antar layar auth pra-login menggunakan state in-memory atau sessionStorage terisolasi sehingga tidak bocor setelah tab ditutup (`auth-foundation.md` §4.0).
