---
id: TC-AUTH-ACT-E2E-017-resend-basic-invalidate-link-flow
title: Resend - buat token baru, invalidate lama, link lama 404, link baru berfungsi
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-61
  - TC-AUTH-ACT-62
  - TC-AUTH-ACT-63
coverage:
  web: automated
---

# Resend - buat token baru, invalidate lama, link lama 404, link baru berfungsi

## Prerequisites

- User dengan status `Pending Activation` dan token `active` tersedia.
- Akses admin untuk melakukan Resend Activation Email (via UI/API).

## Test Steps

1. Siapkan user dengan token `active` (token lama). Catat nilai token lama.
2. Admin melakukan Resend Activation Email untuk user tersebut.
3. Verifikasi token baru dibuat dengan `status=active` dan `expires_at = now + 24 jam`.
4. Verifikasi token lama langsung menjadi `status=superseded`, meski belum expired.
5. Verifikasi hanya ada tepat 1 token `active` untuk user tersebut setelah resend.
6. Buka `/activate?token={tokenLama}` (link sebelum resend). Verifikasi halaman 404 dirender dengan title `"Activation Link Expired"`.
7. Ambil token baru dari email hasil resend (atau dari DB). Buka `/activate?token={tokenBaru}`. Verifikasi halaman Set Password dirender normal dan dapat digunakan.

## Notes

- Link lama pasti 404 (varian "Expired"); link baru berfungsi normal.
