---
id: TC-GS-DIV-E2E-018-create-division-server-failure-resilience
title: "Ketahanan Form Create Terhadap Kegagalan Server 5xx/Timeout"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-29
coverage:
  web: automated
---

# Ketahanan Form Create Terhadap Kegagalan Server 5xx/Timeout

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Mock intercept request POST /v2/iam/divisions disimulasikan error 500 / timeout

## Test Steps

1. Buka modal Create Division melalui tombol '[+ Division]'
2. Ketik Division Name: 'Resilience Unit'
3. Kondisikan interceptor mengembalikan status 500 Internal Server Error
4. Klik tombol '[Submit]'
5. Verifikasi toast error persisten muncul: 'Error, failed to create division.'
6. Verifikasi modal Create Division TETAP terbuka dan input 'Resilience Unit' tidak hilang
7. Verifikasi tombol '[Submit]' kembali aktif untuk memberikan kesempatan pengguna melakukan retry
8. Kondisikan interceptor kembali normal (201 Created) lalu klik kembali '[Submit]'
9. Verifikasi toast sukses muncul dan modal berhasil menutup

## Notes

- Mengikuti protokol Dialog Lifecycle on Error Response Protocol division.md §7.2 item 4.
