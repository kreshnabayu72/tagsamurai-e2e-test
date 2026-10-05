---
id: TC-AUTH-MFA-E2E-016-choose-method-authenticator-enrolled
title: Pemilihan metode Authenticator pada user yang sudah enroll langsung ke verifikasi
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-30
coverage:
  web: automated
---

# Pemilihan metode Authenticator pada user yang sudah enroll langsung ke verifikasi

## Prerequisites

- Mode: FE+BE
- Akun user sudah pernah melakukan setup Authenticator (`authenticator_enrollment.is_active = true`)
- Halaman Choose Verification Method terbuka

## Test Steps

1. Klik pada kartu opsi "Authenticator app"
2. Klik tombol CTA `[Login]`
3. Verifikasi sistem mengecek status pendaftaran Authenticator user
4. Verifikasi pengguna langsung dinavigasikan ke halaman Authenticator Verification dengan judul "Enter authenticator code" (tanpa diarahkan ke pendaftaran ulang)

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-16`
- Merepresentasikan `TC-AUTH-MFA-30` (FE Ref: `TC-AUTH-MFA-FE-16`).
