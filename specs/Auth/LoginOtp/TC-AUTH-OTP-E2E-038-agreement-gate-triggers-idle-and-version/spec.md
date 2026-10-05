---
id: TC-AUTH-OTP-E2E-038-agreement-gate-triggers-idle-and-version
title: Pemicu layar Agreement pasca OTP: user idle >=30 hari dan pembaruan versi Privacy Policy
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-16
  - TC-AUTH-OTP-17
coverage:
  web: automated
---

# Pemicu layar Agreement pasca OTP: user idle >=30 hari dan pembaruan versi Privacy Policy

## Prerequisites

- User yang telah idle logout >= 30 hari (`Fixture.auth.idle30DaysUser`)
- User dengan versi persetujuan privacy policy lama/stale (`Fixture.auth.policyUpdatedUser`)

## Test Steps

### Pemicu Idle >= 30 Hari

1. Buka halaman Login with OTP dan masukkan email user idle `Fixture.auth.idle30DaysUser`
2. Minta OTP dan masukkan kode yang benar pada halaman Input OTP
3. Verifikasi auto-submit mengarahkan browser ke layar "Confirm to Continue"
4. Centang persetujuan dan klik `[Continue]`
5. Verifikasi proses berhasil masuk ke Product Hub

### Pemicu Pembaruan Versi Privacy Policy

6. Lakukan alur Login OTP untuk `Fixture.auth.policyUpdatedUser` (versi aktif sistem > versi persetujuan user)
7. Masukkan kode OTP yang benar
8. Verifikasi layar "Confirm to Continue" muncul karena adanya pembaruan versi dokumen kebijakan
9. Selesaikan persetujuan hingga berhasil login

## Notes

- Evaluasi kebutuhan agreement dilakukan secara dinamis pasca verifikasi OTP sukses.
- Peniadaan (skip) untuk user rutin dan shared consent lintas Login Password ke Login OTP dipisahkan ke `TC-AUTH-OTP-E2E-039`.
