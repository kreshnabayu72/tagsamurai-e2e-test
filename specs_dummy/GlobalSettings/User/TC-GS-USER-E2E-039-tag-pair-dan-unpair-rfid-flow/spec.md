---
id: TC-GS-USER-E2E-039-tag-pair-dan-unpair-rfid-flow
title: "TAG Management: Pasang (Pair) dan lepas (Unpair) TAG RFID dari User Detail"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-313
  - TC-GS-USER-314
  - TC-GS-USER-315
  - TC-GS-USER-316
  - TC-GS-USER-317
  - TC-GS-USER-318
  - TC-GS-USER-319
  - TC-GS-USER-320
  - TC-GS-USER-321
  - TC-GS-USER-322
  - TC-GS-USER-323
  - TC-GS-USER-324
coverage:
  web: automated
---

# TAG Management: Pasang (Pair) dan lepas (Unpair) TAG RFID dari User Detail

## Prerequisites

- Login sebagai Role: Total Control
- User John Doe dan RFID TAG simulator tersedia di environment

## Test Steps

### Pairing TAG RFID

1. Buka User Detail John Doe
2. Klik tombol '[Pair TAG]'
3. Simulasikan pemindaian RFID TAG valid 'TAG-USR-0001'
4. Verifikasi TAG terdeteksi dan status pairing tersimpan
5. Verifikasi identitas TAG tampil pada header User Detail

### Unpairing TAG RFID

6. Klik opsi '[Unpair TAG]' pada Detail John Doe
7. Konfirmasi pelepasan TAG pada dialog
8. Verifikasi TAG berhasil dilepas dan status kembali kosong

## Notes

- Menggabungkan 12 test case granular (TC-GS-USER-313 s.d. TC-GS-USER-324).
