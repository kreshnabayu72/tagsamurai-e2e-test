---
id: TC-AUTH-OTP-E2E-044-login-otp-plan-gating-all-tiers
title: Fitur Login with OTP tersedia identik di seluruh tier lisensi plan tanpa batasan
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-105
coverage:
  web: automated
---

# Fitur Login with OTP tersedia identik di seluruh tier lisensi plan tanpa batasan

## Prerequisites

- Akun uji aktif yang mewakili masing-masing tier langganan plan TAG Samurai:
  - Starter (`Fixture.auth.tierStarterUser`)
  - Business (`Fixture.auth.tierBusinessUser`)
  - Enterprise (`Fixture.auth.tierEnterpriseUser`)

## Test Steps

1. Lakukan pengujian alur Login with OTP untuk akun pada tier Starter (`Fixture.auth.tierStarterUser`)
2. Verifikasi link "Log in with OTP" tersedia, proses permintaan dan verifikasi kode berjalan lancar tanpa pembatasan paywall/plan gating
3. Ulangi alur Login with OTP untuk akun pada tier Business (`Fixture.auth.tierBusinessUser`)
4. Verifikasi seluruh fungsionalitas OTP bekerja secara identik
5. Ulangi alur Login with OTP untuk akun pada tier Enterprise (`Fixture.auth.tierEnterpriseUser`)
6. Verifikasi alur bekerja identik di seluruh tier

## Notes

- Fitur Login with OTP adalah fungsionalitas autentikasi dasar tingkat platform TAG Samurai dan tersedia secara merata di semua tier tanpa diskriminasi lisensi.
