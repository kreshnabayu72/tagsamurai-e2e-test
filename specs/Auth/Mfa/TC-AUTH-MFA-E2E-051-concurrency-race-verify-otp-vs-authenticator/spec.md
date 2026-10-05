---
id: TC-AUTH-MFA-E2E-051-concurrency-race-verify-otp-vs-authenticator
title: Kondisi balapan simultan verifikasi OTP Tab A vs verifikasi Authenticator Tab B
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-121
coverage:
  web: automated
---

# Kondisi balapan simultan verifikasi OTP Tab A vs verifikasi Authenticator Tab B

## Prerequisites

- Mode: FE+BE
- User membuka dua tab dari sesi MFA yang sama: Tab A membuka OTP, Tab B membuka Authenticator

## Test Steps

1. Siapkan kode valid pada form OTP di Tab A dan kode valid pada form Authenticator di Tab B
2. Lakukan submit pada kedua tab secara bersamaan
3. Verifikasi atomic guard pada backend memutuskan tepat satu transaksi sebagai pemenang
4. Verifikasi tab pemenang berhasil login ke Portal
5. Verifikasi tab yang kalah ditolak karena sesi sudah di-consume (bukan error "Invalid code")
6. Verifikasi tidak ada sesi ganda maupun log ganda yang tercatat

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-51`
- Merepresentasikan `TC-AUTH-MFA-121` (FE Ref: `TC-AUTH-MFA-FE-51`).
