---
id: TC-AUTH-OTP-E2E-039-agreement-gate-skip-routine-user-and-shared-consent
title: Peniadaan (skip) layar Agreement untuk user rutin dan pengakuan shared consent lintas Login Password ke Login OTP
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-18
  - TC-AUTH-OTP-22
coverage:
  web: automated
---

# Peniadaan (skip) layar Agreement untuk user rutin dan pengakuan shared consent lintas Login Password ke Login OTP

## Prerequisites

- User rutin normal yang telah menyetujui versi Privacy Policy terbaru dan idle < 30 hari (`Fixture.auth.routineUserEmail`)
- User yang baru saja menyetujui privacy policy terbaru lewat jalur Login with Password (`Fixture.auth.consentGivenViaPasswordUser`)

## Test Steps

### Skip Layar Agreement untuk User Rutin

1. Buka halaman Login with OTP dan masukkan email `Fixture.auth.routineUserEmail`
2. Minta OTP dan masukkan 6 digit kode yang benar pada halaman Input OTP
3. Verifikasi auto-submit terpicu
4. Verifikasi layar Agreement "Confirm to Continue" di-skip total (tidak pernah muncul)
5. Verifikasi browser langsung di-redirect ke halaman utama Product Hub

### Shared Consent Lintas Jalur (Password ke OTP)

6. Lakukan alur Login with OTP untuk user `Fixture.auth.consentGivenViaPasswordUser` (user yang telah menandatangani consent terbaru melalui sesi Login with Password)
7. Masukkan 6 digit kode OTP yang benar pada halaman Input OTP
8. Verifikasi auto-submit terpicu
9. Verifikasi layar Agreement "Confirm to Continue" di-skip secara total
10. Verifikasi browser langsung diarahkan ke Product Hub tanpa meminta persetujuan ulang
11. Verifikasi entitas `user_privacy_consent` pada database tetap berstatus valid dan tidak mengalami duplikasi record

## Notes

- Entitas persetujuan `user_privacy_consent` bersifat global per user, berlaku lintas metode login (Password dan OTP) tanpa memerlukan persetujuan berulang.
