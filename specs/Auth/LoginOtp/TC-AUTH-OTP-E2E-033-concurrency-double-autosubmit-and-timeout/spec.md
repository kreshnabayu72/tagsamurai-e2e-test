---
id: TC-AUTH-OTP-E2E-033-concurrency-double-autosubmit-and-timeout
title: Penanganan balapan auto-submit ganda pada re-render cepat dan timeout client
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-75
  - TC-AUTH-OTP-77
coverage:
  web: automated
---

# Penanganan balapan auto-submit ganda pada re-render cepat dan timeout client

## Prerequisites

- Akun aktif terdaftar siap menerima verifikasi kode OTP (`Fixture.auth.standardUserEmail`)
- Halaman Input OTP telah terbuka dengan kode OTP 6 digit valid

## Test Steps

### Race Auto-Submit Ganda pada Re-render Cepat

1. Pada halaman Input OTP dengan kode benar yang aktif, picu event auto-submit sebanyak 2 kali secara simultan (misalnya re-render cepat saat digit ke-6 dimasukkan)
2. Verifikasi auto-submit guard pada frontend dan mekanisme atomic check-and-consume pada server mencegah terjadinya double evaluation
3. Verifikasi hanya 1 sesi yang dibuat dan 1 entri audit log yang tercatat

### Client Timeout & Retry Verifikasi pada Kode Ter-consume

4. Simulasikan skenario di mana request verify pertama berhasil diproses server (`used = true`), namun response mengalami timeout pada client
5. Lakukan retry verifikasi dari client dengan kode yang sama
6. Verifikasi server menolak dengan respons kode telah digunakan ("OTP_INVALID") dan tidak menghasilkan sesi kedua

## Notes

- Kasus request OTP paralel pada dua tab browser dipisahkan ke `TC-AUTH-OTP-E2E-015`.
- Kasus cross-action race antar-aksi yang saling bertentangan (Verify vs Resend, Verify vs Edit Email) dipisahkan ke `TC-AUTH-OTP-E2E-034` dan `TC-AUTH-OTP-E2E-035`.
