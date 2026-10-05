---
id: TC-AUTH-OTP-E2E-036-agreement-gate-screening-and-consent
title: Layar Agreement "Confirm to Continue" pasca verifikasi OTP, validasi uncheck, dan submit persetujuan
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-15
  - TC-AUTH-OTP-19
  - TC-AUTH-OTP-20
  - TC-AUTH-OTP-108
coverage:
  web: automated
---

# Layar Agreement "Confirm to Continue" pasca verifikasi OTP, validasi uncheck, dan submit persetujuan

## Prerequisites

- User baru teraktivasi yang belum pernah login (`first_login_at IS NULL`) disiapkan di fixture (`Fixture.auth.firstLoginUser`)
- Layanan pengiriman email testing aktif

## Test Steps

### Screening Layar "Confirm to Continue"

1. Buka halaman Login with OTP dan masukkan email `Fixture.auth.firstLoginUser`
2. Selesaikan reCAPTCHA, minta OTP, dan masukkan kode OTP yang benar pada halaman Input OTP
3. Verifikasi kode OTP ter-consume (`used = true`), namun sesi penuh belum dibuat (hanya token sementara `preAuthToken`)
4. Verifikasi browser berpindah ke layar "Confirm to Continue"
5. Verifikasi judul halaman menampilkan teks "Confirm to Continue"
6. Verifikasi terdapat checkbox dengan label "I agree to the Privacy Policy" dan link "Privacy Policy" dapat diklik menuju dokumen kebijakan
7. Verifikasi checkbox dalam status unchecked secara default
8. Verifikasi terdapat tombol `[Continue]` dalam status enabled

### Validasi Penolakan Klik Tanpa Centang

9. Klik tombol `[Continue]` tanpa mencentang checkbox
10. Verifikasi submit diblokir di sisi client dan pesan error inline "You need to agree to the Privacy Policy to continue" muncul di bawah checkbox
11. Verifikasi tidak ada entri audit log baru yang dibuat

### Persetujuan Consent Sukses

12. Centang checkbox "I agree to the Privacy Policy"
13. Klik tombol `[Continue]`
14. Verifikasi consent tersimpan di database (`user_privacy_consent`), sesi autentikasi resmi dibuat, dan browser di-redirect ke Product Hub

## Notes

- Agreement gate dievaluasi setelah verifikasi OTP sukses dan sebelum MFA handoff atau pembentukan sesi.
- Kasus pembatalan sesi (tutup tab / keluar halaman) dipisahkan ke `TC-AUTH-OTP-E2E-037`.
- Pengujian kondisi pemicu agreement lainnya (idle >=30d, policy version update) dipisahkan ke `TC-AUTH-OTP-E2E-038`.
