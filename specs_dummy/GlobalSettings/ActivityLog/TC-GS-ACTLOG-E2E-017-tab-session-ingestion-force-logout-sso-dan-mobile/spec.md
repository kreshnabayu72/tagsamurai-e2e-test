---
id: TC-GS-ACTLOG-E2E-017-tab-session-ingestion-force-logout-sso-dan-mobile
title: "Tab Session: Ingestion Sesi Force-Logout oleh Admin, Login SSO SAML/OIDC, dan Mobile Device"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-48
  - TC-GS-ACTLOG-49
  - TC-GS-ACTLOG-50
coverage:
  web: automated
---

# Tab Session: Ingestion Sesi Force-Logout oleh Admin, Login SSO SAML/OIDC, dan Mobile Device

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat event Force-Logout dari modul Concurrent License, sesi login via SSO IdP, dan sesi dari aplikasi mobile native

## Test Steps

### Force Logout oleh Admin (Concurrent License)
1. Buka Tab Session di menu Global Settings > Activity Log.
2. Cari entri pengguna yang sesi aktifnya diputus paksa oleh administrator dari modul lisensi / sesi concurrent.
3. Verifikasi kolom Activity menampilkan 'Force Logout' atau 'Logout (Admin)', dan kolom Note mencatat alasan pemutusan sesi oleh admin.
### Ingestion Sesi SSO SAML / OIDC
4. Cari entri sesi pengguna yang masuk menggunakan Single Sign-On (SSO / SAML / OIDC).
5. Verifikasi kolom Activity menampilkan 'Login (SSO)', Status 'Success', dan kolom Device/Browser memuat identitas peramban.
### Ingestion Sesi Mobile Device
6. Cari entri sesi pengguna yang masuk melalui aplikasi mobile native TAG Samurai (Android / iOS).
7. Verifikasi kolom Device / Browser menampilkan informasi model gawai dan versi OS mobile (misal: 'Android 14 / TAG Samurai Mobile').

## Notes

- Tab Session mengidentifikasi asal platform dan metode otentikasi secara transparan.
