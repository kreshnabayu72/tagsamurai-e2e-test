---
id: suite-auth-mfa
title: "Auth MFA E2E Test Suite"
parallel: false
specs:
  - TC-AUTH-MFA-E2E-001-screening-choose-verification-method
  - TC-AUTH-MFA-E2E-002-screening-halaman-otp-verification
  - TC-AUTH-MFA-E2E-003-screening-authenticator-verification
  - TC-AUTH-MFA-E2E-004-screening-enrollment-authenticator
  - TC-AUTH-MFA-E2E-005-mobile-native-layout-responsif
  - TC-AUTH-MFA-E2E-006-akses-publik-dan-direct-url
  - TC-AUTH-MFA-E2E-007-evaluasi-single-step-tanpa-mfa
  - TC-AUTH-MFA-E2E-008-pemicu-mfa-login-pertama
  - TC-AUTH-MFA-E2E-009-pemicu-mfa-idle-dan-independensi-platform
  - TC-AUTH-MFA-E2E-010-deteksi-device-baru-dan-reset-storage
  - TC-AUTH-MFA-E2E-011-deteksi-lokasi-jarak-dan-baseline-user
  - TC-AUTH-MFA-E2E-012-deteksi-beda-negara-dan-tumbling-window
  - TC-AUTH-MFA-E2E-013-decay-pasangan-negara-dan-single-step-refresh
  - TC-AUTH-MFA-E2E-014-fail-open-geo-ip-dan-kombinasi-alert
  - TC-AUTH-MFA-E2E-015-sekuensialitas-agreement-gate-dan-mfa
  - TC-AUTH-MFA-E2E-016-verifikasi-otp-auto-submit-dan-paste
  - TC-AUTH-MFA-E2E-017-validasi-input-otp-error-dan-expiry
  - TC-AUTH-MFA-E2E-018-siklus-resend-otp-cooldown-dan-kuota
  - TC-AUTH-MFA-E2E-019-verifikasi-authenticator-drift-dan-anti-replay
  - TC-AUTH-MFA-E2E-020-validasi-input-authenticator-dan-paste
  - TC-AUTH-MFA-E2E-021-enrollment-authenticator-lengkap
  - TC-AUTH-MFA-E2E-022-validasi-input-enrollment-authenticator
  - TC-AUTH-MFA-E2E-023-batas-percobaan-salah-lintas-metode
  - TC-AUTH-MFA-E2E-024-ttl-sesi-pre-auth-dan-navigasi-browser
  - TC-AUTH-MFA-E2E-025-pembatalan-sesi-user-deactivated-dan-deleted
  - TC-AUTH-MFA-E2E-026-pembentukan-trust-device-dan-pasca-login
  - TC-AUTH-MFA-E2E-027-email-alert-login-tak-biasa-dan-reset-password
  - TC-AUTH-MFA-E2E-028-audit-log-mutasi-status-sukses-dan-gagal
  - TC-AUTH-MFA-E2E-029-audit-log-whitelist-policy-dan-ip-proxy-hop
  - TC-AUTH-MFA-E2E-030-mfa-recovery-dan-admin-reset-authenticator
  - TC-AUTH-MFA-E2E-031-session-management-dan-paritas-subscription-plan
  - TC-AUTH-MFA-E2E-032-verifikasi-isi-qr-code-dan-secret-key
  - TC-AUTH-MFA-E2E-033-konkurensi-multi-tab-dan-guard-double-submit
  - TC-AUTH-MFA-E2E-034-security-defense-token-tampering
  - TC-AUTH-MFA-E2E-035-rate-limiting-resilience-dan-toast-sticky
  - TC-AUTH-MFA-E2E-036-mobile-biometric-relogin-trigger
---

# Auth MFA E2E Test Suite

Suite ini menguji seluruh fungsionalitas Multi-Factor Authentication (MFA) pada sistem TAG Samurai:
- Screening dan tata letak halaman MFA (Choose Verification Method, OTP Verification, Authenticator Verification, Enrollment Authenticator)
- Evaluasi pemicu MFA (login pertama, idle ≥30 hari, device baru, lokasi jarak jauh >100 km, beda negara, dan decay 180 hari)
- Verifikasi faktor kedua via OTP Email dan Authenticator App (RFC 6238 TOTP)
- Verifikasi kriptografis dan decoding QR Code serta format parameter URI
- Penanganan batas keamanan (5 percobaan salah akumulatif, TTL sesi pre-auth 10 menit, IP rate limit 429)
- Ketahanan terhadap konkurensi, balapan multi-device / multi-tab, dan double-submit guards
- Integrasi audit log multi-surface (Activity Log Session dan User Log) serta paritas lintas modul
