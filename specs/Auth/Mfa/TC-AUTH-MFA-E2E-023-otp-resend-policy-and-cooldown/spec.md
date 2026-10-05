---
id: TC-AUTH-MFA-E2E-023-otp-resend-policy-and-cooldown
title: Kebijakan resend kode OTP pada MFA dengan cooldown dan batas kuota sesi
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-39
coverage:
  web: automated
---

# Kebijakan resend kode OTP pada MFA dengan cooldown dan batas kuota sesi

## Prerequisites

- Mode: FE+BE
- Halaman Verifikasi OTP (MFA) terbuka

## Test Steps

1. Amati tombol resend kode di bagian bawah form OTP
2. Verifikasi tombol memiliki label "Resend code" dan dalam keadaan nonaktif (disabled) selama cooldown 60 detik awal
3. Tunggu hingga timer 60 detik selesai
4. Verifikasi tombol "Resend code" menjadi aktif
5. Lakukan pengiriman ulang hingga mencapai kuota maksimum 5 kali dalam satu sesi MFA
6. Pada resend ke-5, verifikasi sistem memicu cooldown panjang selama 10 menit
7. Verifikasi aksi resend kode OTP ini TIDAK dicatat sebagai entri di Activity Log Session

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-23`
- Merepresentasikan `TC-AUTH-MFA-39` (FE Ref: `TC-AUTH-MFA-FE-23`).
- Kebijakan resend MFA identik dengan aturan baku Login with OTP.
