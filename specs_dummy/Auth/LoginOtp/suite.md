---
name: Auth Login with OTP
id: suite-auth-login-otp
description: Test cases derived from tc-login-otp.md for Auth > Login with OTP
executionOrder: 2.0
parallel: false
---

# Suite: Auth Login with OTP

Suite ini mencakup alur autentikasi kata sandi sekali pakai (Login with OTP) pra-autentikasi:
mulai dari halaman Request OTP (web dan mobile), pengiriman email kode 6 digit, halaman Verify OTP
dengan verifikasi otomatis (auto-submit) dan fallback, siklus Resend (countdown 60 detik, kuota 5 kali,
cooldown 10 menit, state Exhausted), alur Edit email, proteksi reCAPTCHA v2 (web), proteksi IP rate limit,
layar kondisional Agreement Gate ("Confirm to Continue"), handoff MFA (TOTP), sinkronisasi status akun
Global Settings, hingga validasi keamanan (bypass UI, tampering token, konkurensi tab).

`parallel: false` ditetapkan karena beberapa kondisi data bersama dan pembatas sistemik:

- Spec 008, 015, dan 018 menguji rate limit per alamat IP dan kuota per alamat email; pengujian paralel dapat saling mencemari counter dan memicu penolakan 429 tak terduga.
- Spec 012 dan 023 mengubah status user di Global Settings > User (Active/Inactive, Delete, Deactivate saat proses berjalan) yang berdampak langsung pada data user bersama.
- Runner otomasi membutuhkan kepastian isolasi status sesi dan counter server-side antar skenario.

Setiap spec menyiapkan data ujinya sendiri melalui hook dan fixture terstandarisasi, sehingga dapat dieksekusi secara independen.
