---
id: TC-AUTH-OTP-E2E-045-login-otp-happy-path-success-and-logging
title: Login OTP happy path sukses, pembuatan sesi aktif, dan pencatatan identik di 2 surface log
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-38
  - TC-AUTH-OTP-62
  - TC-AUTH-OTP-68
  - TC-AUTH-OTP-74
  - TC-AUTH-OTP-113
coverage:
  web: automated
---

# Login OTP happy path sukses, pembuatan sesi aktif, dan pencatatan identik di 2 surface log

## Prerequisites

- User rutin aktif (`Fixture.auth.routineUserEmail`): bukan login pertama kali, idle <30 hari, dan telah menyetujui versi Privacy Policy terbaru
- Layanan pengiriman email testing aktif

## Test Steps

### Happy Path Login Sukses & Pembentukan Sesi

1. Buka halaman Input Email Login with OTP
2. Masukkan email user rutin `Fixture.auth.routineUserEmail`
3. Selesaikan verifikasi reCAPTCHA lalu klik `[Request OTP]`
4. Ambil 6 digit kode OTP yang dikirimkan ke email user
5. Pada halaman Input OTP, masukkan ke-6 digit kode yang benar
6. Verifikasi auto-submit terpicu secara otomatis pada pengetikan digit ke-6
7. Verifikasi kode OTP ditandai telah digunakan (`otp_code.used = true`)
8. Verifikasi sesi login aktif terbentuk (cookie autentikasi disematkan di browser)
9. Verifikasi browser langsung di-redirect ke halaman Portal (Product Hub) tanpa terhalang layar Agreement atau MFA

### Verifikasi Pencatatan pada 2 Surface Log

10. Menggunakan sesi admin, periksa data pada Activity Log Session dan User Log
11. Verifikasi kedua surface log mencatat entri login baru yang identik:
    - Status: "Success"
    - Note / Activity: "Login with OTP"
    - Date & Timestamp sama
    - IP Address sesuai IP client pengirim
    - Kolom "Device / Browser" berformat kanonikal `[Browser] on [OS]` (contoh: "Chrome on Windows", tanpa versi numerik, sesuai GAP-178)

## Notes

- User rutin yang tidak memenuhi kondisi pemicu Agreement atau MFA langsung diarahkan ke Product Hub.
- Kolom Device / Browser pada log dicatat dengan format Browser-first tanpa nomor versi (`[Browser] on [OS]`).
- Kasus akun terkunci password dipisahkan ke `TC-AUTH-OTP-E2E-025` dan plan gating dipisahkan ke `TC-AUTH-OTP-E2E-044`.
