---
id: TC-GS-POS-E2E-020-security-edit-position-pencabutan-capability-di-tengah-sesi
title: "Security: Save Edit setelah capability Update dicabut di tengah sesi ditolak 403"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-294
coverage:
  web: automated
---

# Security: Save Edit setelah capability Update dicabut di tengah sesi ditolak 403

## Prerequisites

- Dua sesi: Sesi 1 Aktor U-Only membuka modal Edit; Sesi 2 Admin mencabut capability Update dari role aktor

## Test Steps

### Pencabutan Izin di Tengah Sesi

1. Pada Sesi 1, Aktor U-Only membuka form Edit Position
2. Pada Sesi 2, Admin mencabut izin Update dari role aktor tersebut
3. Kembali ke Sesi 1, lakukan perubahan nama Position lalu klik tombol "[Save]"
4. Verifikasi permintaan ditolak oleh server dengan status 403 Forbidden
5. Verifikasi toast error izin muncul dan perubahan tidak tersimpan ke database

## Notes

- Menguji defense-in-depth penegakan izin dinamis (TC-GS-POS-294).
