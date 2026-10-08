---
id: TC-AUTH-ACT-E2E-008-confirm-password-validation
title: Validasi Confirm Password (empty dan mismatch)
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-32
  - TC-AUTH-ACT-33
  - TC-AUTH-ACT-34
coverage:
  web: automated
---

# Validasi Confirm Password (empty dan mismatch)

## Prerequisites

- Token valid `active` tersedia, halaman Set Password `/activate?token={validToken}` terbuka.
- Hook `beforeEach` mengembalikan form ke state kosong/default.

## Test Steps

1. Kosongkan field Password (atau hilangkan nilainya), isi field Confirm Password dengan nilai sembarang. Klik `[Set Password]`.
2. Verifikasi muncul inline error `"Password must not be empty"`. Tetap berada di halaman Set Password. Token tetap `active`, tidak ter-consume.
3. Isi field Password dengan `Abcd1!23`, kosongkan atau hilangkan nilai `confirmPassword`. Klik `[Set Password]`.
4. Verifikasi muncul inline error `"Confirm password must not be empty"`. Tetap berada di halaman Set Password. Token tetap `active`, tidak ter-consume.
5. Isi field Password dengan `Abcd1!23`, isi field Confirm Password dengan `Abcd1!24` (berbeda). Klik `[Set Password]`.
6. Verifikasi muncul inline error `"Passwords do not match"`. Tetap berada di halaman Set Password. Token tetap `active`, tidak ter-consume.

## Notes

- Label tombol sesuai konvensi: `[Set Password]`.
