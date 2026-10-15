---
id: TC-AUTH-RST-E2E-001-screening-request-page
title: "Screening Halaman Reset Password (Request), State Awal, dan Urutan Tab"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-01
  - TC-AUTH-RST-02
  - TC-AUTH-RST-03
coverage:
  web: automated
---

# Screening Halaman Reset Password (Request), State Awal, dan Urutan Tab

## Prerequisites

- Mode: FE+BE. Halaman publik; tidak ada data yang di-seed dan tidak ada akun yang login.
- Kemampuan teknis: jendela privat tanpa sesi login; tombol Tab keyboard; reload halaman (F5).
- TC-AUTH-RST-01, TC-AUTH-RST-02, TC-AUTH-RST-03: User belum login (guest); browser web; halaman Reset Password belum pernah diisi pada sesi browser ini.

## Test Steps

### TC-AUTH-RST-01: Screening halaman Reset Password (Request) di web

1. Buka jendela privat baru (tanpa sesi login) lalu buka halaman Reset Password (Request)
2. Susuri halaman dari atas ke bawah tanpa klik apa pun
3. Verifikasi **Header**: Logo TAG Samurai di tengah atas
4. Verifikasi **Header**: Title "Reset Password"
5. Verifikasi **Header**: Subtitle "Enter your email and we'll send you a link to reset your password."
6. Verifikasi **Body**: field Email (wajib) berlabel "Email" dengan placeholder "Enter your email"
7. Verifikasi **Body**: widget Google reCAPTCHA v2 belum diselesaikan
8. Verifikasi **Footer**: Button [Reset Password] (solid, primary, lebar penuh) tampil
9. Verifikasi **Footer**: link "Log in with password" (text, di tengah, di bawah button) tampil
10. Verifikasi **Must NOT**: tombol [Clear Field], tombol tutup [✕], dialog Unsaved Changes, link "Login with OTP", dan pilihan masa berlaku token tidak ada (anchor: Button [Reset Password] tampil)

### TC-AUTH-RST-02: State awal form Reset Password (Request) di web

11. Muat ulang halaman Reset Password (F5) sehingga form kembali ke state awal
12. Amati field Email, widget reCAPTCHA, Button [Reset Password], dan slot caption
13. Verifikasi field Email kosong menampilkan placeholder "Enter your email"
14. Verifikasi widget reCAPTCHA berstatus belum diselesaikan
15. Verifikasi caption "Please verify that you are not a robot" tidak tampil
16. Verifikasi Button [Reset Password] enabled
17. Verifikasi Button [Reset Password] tanpa spinner
18. Verifikasi tidak ada caption error pada field Email

### TC-AUTH-RST-03: Urutan Tab keyboard pada halaman Reset Password (Request)

19. Klik field Email
20. Tekan Tab berulang kali sambil mencatat elemen yang fokus
21. Verifikasi urutan fokus: field Email, widget reCAPTCHA, Button [Reset Password]

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`. Screening di awal, lalu state awal, lalu urutan Tab; tanpa aksi yang mengubah data.
- Langkah "muat ulang halaman" sebelum TC-AUTH-RST-02 adalah langkah penghubung untuk mengembalikan state awal (S-03).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
