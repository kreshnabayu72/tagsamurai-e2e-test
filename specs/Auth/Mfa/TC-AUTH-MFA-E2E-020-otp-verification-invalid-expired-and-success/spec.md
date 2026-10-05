---
id: TC-AUTH-MFA-E2E-020-otp-verification-invalid-expired-and-success
title: Verifikasi OTP kode salah expired lalu kode benar memicu auto-submit sukses
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-34
  - TC-AUTH-MFA-35
  - TC-AUTH-MFA-36
coverage:
  web: automated
---

# Verifikasi OTP kode salah expired lalu kode benar memicu auto-submit sukses

## Prerequisites

- Mode: FE+BE
- Halaman Verifikasi OTP (MFA) terbuka dengan kode OTP terkirim ke email

## Test Steps

### Kode OTP Salah
1. Masukkan 6 digit kode salah (misalnya "999999")
2. Verifikasi sistem menampilkan caption error "Invalid code"
3. Verifikasi field OTP dibersihkan dan kursor kembali ke kotak digit pertama
4. Verifikasi entri kegagalan tercatat di Activity Log Session dengan Status "Failed" dan Note "Incorrect OTP"

### Kode OTP Kedaluwarsa (>5 Menit)
5. Simulasikan kode yang telah melampaui masa berlaku 5 menit
6. Masukkan 6 digit kode tersebut
7. Verifikasi caption error menampilkan pesan "OTP expired"
8. Verifikasi tercatat di log audit dengan Status "Failed" dan Note "OTP expired"

### Kode OTP Benar (Auto-Submit)
9. Masukkan 6 digit kode OTP valid yang aktif
10. Verifikasi sistem melakukan auto-submit seketika saat digit ke-6 selesai diketik (tanpa tombol Verify)
11. Verifikasi `mfa_session` berhasil di-consume (`is_consumed = true`) dan pengguna berhasil login ke aplikasi

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-20`
- Merepresentasikan `TC-AUTH-MFA-34`, `35`, `36` (FE Ref: `TC-AUTH-MFA-FE-20`).
