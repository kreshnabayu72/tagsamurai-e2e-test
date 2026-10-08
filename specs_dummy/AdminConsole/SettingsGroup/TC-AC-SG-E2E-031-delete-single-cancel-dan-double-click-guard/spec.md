---
id: TC-AC-SG-E2E-031-delete-single-cancel-dan-double-click-guard
title: "Pembatalan dialog Delete dan perlindungan double-click pada tombol konfirmasi Delete"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-65
  - TC-AC-SG-111
coverage:
  web: automated
---

# Pembatalan dialog Delete dan perlindungan double-click pada tombol konfirmasi Delete

## Prerequisites

- Login sebagai Role: Total Control
- Group temporer yang lolos guard member (Total Member = 0)

## Test Steps

### Pembatalan Dialog Delete
1. Klik elipsis `[⋯]` pada group target lalu pilih `[Delete]`
2. Verifikasi dialog konfirmasi delete muncul
3. Klik tombol `[Cancel]` pada dialog
4. Verifikasi dialog tertutup, tidak ada toast yang muncul, dan data group tidak terhapus
### Perlindungan Double-Click Delete
5. Buka kembali dialog `[Delete]` pada group target
6. Lakukan klik ganda secara cepat pada tombol konfirmasi `[Delete]`
7. Verifikasi tombol seketika disabled loading pada klik pertama
8. Verifikasi hanya tepat 1 eksekusi commit penghapusan yang diproses sistem

## Notes

- Mencegah race condition double submit penghapusan di level browser.
