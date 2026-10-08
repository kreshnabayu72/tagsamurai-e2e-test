---
id: TC-AUTH-RST-E2E-009-email-sent-tanpa-konteks
title: "Halaman Email Sent! tanpa konteks email: fallback teks generik, section Resend tersembunyi, dan navigasi Back to Reset"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-RST-46
coverage:
  web: automated
---

# Halaman Email Sent! tanpa konteks email: fallback teks generik, section Resend tersembunyi, dan navigasi Back to Reset

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/email-sent` tanpa state sesi atau query parameter email.
- Environment uji terisolasi khusus pengujian otomatis.

## Test Steps

### Akses halaman Email Sent! via refresh browser atau direct URL

1. Buka tab browser baru lalu akses langsung URL `/email-sent` tanpa melalui alur submit form Request Reset
2. Verifikasi halaman merender layout Email Sent!
3. Verifikasi teks subtitle menggunakan fallback generik: "We've sent a password reset link to your email. Please check your inbox and follow the instructions." (kata "your email" menggantikan alamat email spesifik)
4. Verifikasi seluruh section Resend ("Didn't receive the email?" dan tombol [Resend email]) disembunyikan dari layar
5. Verifikasi timer countdown tidak dipulihkan
6. Verifikasi tampil link navigasi "Back to Reset Password" atau tombol kembali yang mengarahkan ke form Request
7. Klik link "Back to Reset Password"
8. Verifikasi browser diarahkan kembali ke halaman Reset Password (`/reset-password`) dengan field Email dalam keadaan kosong

## Notes

- Sesuai keputusan NC-09, FI-AUTHRST-07, FI-AUTHRST-08, dan PRD §9.5, konteks email tidak bertahan saat halaman dimuat ulang (refresh) atau diakses via direct URL.
- Tanpa konteks email yang jelas, fitur Resend disembunyikan untuk menghindari pengiriman email ke tujuan yang tidak terdefinisi, dan pengguna difasilitasi untuk mengulang input email lewat tautan kembali.
