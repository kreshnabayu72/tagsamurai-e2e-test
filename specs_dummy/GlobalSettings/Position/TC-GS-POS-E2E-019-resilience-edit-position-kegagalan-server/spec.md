---
id: TC-GS-POS-E2E-019-resilience-edit-position-kegagalan-server
title: "Resilience: Form Edit mempertahankan form saat kegagalan server 5xx, timeout, dan retry No-Op"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-106
  - TC-GS-POS-107
  - TC-GS-POS-108
coverage:
  web: automated
---

# Resilience: Form Edit mempertahankan form saat kegagalan server 5xx, timeout, dan retry No-Op

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Modal Edit terbuka dengan teks perubahan

## Test Steps

### Kegagalan Server 500

1. Intersep PUT/PATCH /positions/:id dengan error 500
2. Klik tombol "[Save]"
3. Verifikasi toast error server muncul dan modal Edit tetap terbuka bersama input perubahannya

### Timeout Jaringan & Retry No-Op

4. Intersep PUT/PATCH /positions/:id dengan network timeout
5. Klik tombol "[Save]"
6. Verifikasi toast error timeout muncul dan form tetap terbuka
7. Lepas intersep (anggap data di server ternyata sudah ter-commit)
8. Klik kembali tombol "[Save]"
9. Verifikasi server memperlakukan simpan ulang sebagai No-Op dan modal tertutup sukses tanpa duplikasi log

## Notes

- Mode: mock untuk simulasi error 500, timeout, dan idempotency retry (TC-GS-POS-106, 107, 108).
