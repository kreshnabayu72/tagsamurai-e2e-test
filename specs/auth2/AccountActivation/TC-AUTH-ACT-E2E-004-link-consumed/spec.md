---
id: TC-AUTH-ACT-E2E-004-link-consumed
title: Link consumed mengarah ke 404 "Link Already Used" dengan CTA "Go to Login"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-12
coverage:
  web: automated
---

# Link consumed mengarah ke 404 "Link Already Used" dengan CTA "Go to Login"

## Prerequisites

- Token `consumed` (sudah pernah digunakan untuk aktivasi sukses) tersedia.

## Test Steps

1. Buka `/activate?token={consumedToken}` yang sudah pernah digunakan untuk aktivasi sukses.
2. Verifikasi halaman 404 dirender.
3. Verifikasi title halaman 404 adalah `"Link Already Used"`.
4. Verifikasi body halaman sesuai copy varian Used dan menampilkan CTA `"Go to Login"`.

## Notes

- Hanya varian "Used" yang memiliki CTA Go to Login.
