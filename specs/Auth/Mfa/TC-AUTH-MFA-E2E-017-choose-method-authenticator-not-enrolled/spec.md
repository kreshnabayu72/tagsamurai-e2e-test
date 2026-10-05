---
id: TC-AUTH-MFA-E2E-017-choose-method-authenticator-not-enrolled
title: Pemilihan metode Authenticator pada user belum enroll diarahkan ke layar pendaftaran
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-31
coverage:
  web: automated
---

# Pemilihan metode Authenticator pada user belum enroll diarahkan ke layar pendaftaran

## Prerequisites

- Mode: FE+BE
- Akun user belum pernah melakukan setup Authenticator (`authenticator_enrollment` kosong atau tidak aktif)
- Halaman Choose Verification Method terbuka

## Test Steps

1. Klik pada kartu opsi "Authenticator app"
2. Klik tombol CTA `[Login]`
3. Verifikasi sistem mendeteksi bahwa user belum pernah melakukan setup
4. Verifikasi pengguna dinavigasikan ke halaman Setup Authenticator dengan heading "Set up authenticator app" (bukan langsung ke halaman verifikasi)

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-17`
- Merepresentasikan `TC-AUTH-MFA-31` (FE Ref: `TC-AUTH-MFA-FE-17`).
