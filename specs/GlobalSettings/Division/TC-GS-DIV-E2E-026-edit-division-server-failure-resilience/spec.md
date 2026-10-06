---
id: TC-GS-DIV-E2E-026-edit-division-server-failure-resilience
title: "Ketahanan Form Edit Terhadap Kegagalan Server 5xx/Timeout"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-37
coverage:
  web: automated
---

# Ketahanan Form Edit Terhadap Kegagalan Server 5xx/Timeout

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Mock intercept request PATCH /v2/iam/divisions/{id} disimulasikan error 500 / timeout

## Test Steps

1. Buka modal Edit pada salah satu baris divisi
2. Ubah nama divisi
3. Kondisikan interceptor mengembalikan status error 500
4. Klik tombol '[Save]'
5. Verifikasi toast error persisten muncul: 'Error, failed to update division.'
6. Verifikasi modal Edit TETAP terbuka dan nilai input tidak hilang
7. Verifikasi tombol '[Save]' kembali aktif untuk retry
8. Kondisikan interceptor kembali normal (200 OK) lalu klik '[Save]'
9. Verifikasi toast sukses muncul dan modal berhasil menutup

## Notes

- Menguji ketahanan dialog form edit terhadap server failure sesuai division.md §7.2.
