---
id: TC-GS-USER-E2E-020-create-user-validasi-duplikat-dan-guard-double-submit
title: "Create User: Validasi duplikat email dan employee ID serta guard double submit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-118
  - TC-GS-USER-119
  - TC-GS-USER-120
  - TC-GS-USER-121
  - TC-GS-USER-122
  - TC-GS-USER-123
  - TC-GS-USER-124
  - TC-GS-USER-1006
  - TC-GS-USER-1031
  - TC-GS-USER-1032
  - TC-GS-USER-1033
coverage:
  web: automated
---

# Create User: Validasi duplikat email dan employee ID serta guard double submit

## Prerequisites

- Login sebagai Role: Total Control
- Data user existing (email budisantoso@qwertysystem.net dan employee ID EMP-0001) sudah ada

## Test Steps

### Validasi Duplikat

1. Buka modal '[+ User]'
2. Ketik email existing 'budisantoso@qwertysystem.net', verifikasi muncul error inline 'Email already exists' via debounce
3. Ketik email dengan variasi huruf kapital dan spasi tepi '  BUDISANTOSO@QWERTYSYSTEM.NET  ', verifikasi tetap ditolak sebagai duplikat
4. Ketik Employee ID existing dengan spasi tepi ' EMP-0001 ', verifikasi ditolak duplikat
5. Ketik Employee ID dengan variasi case 'emp-0001', verifikasi diterima (case-sensitive) bila kebijakan sistem mengizinkan

### Guard Double Submit

6. Isi data lengkap yang valid, klik tombol '[Submit]' berkali-kali secara cepat
7. Verifikasi tombol '[Submit]' masuk state loading disabled dan hanya satu request pembuatan user yang diproses

## Notes

- Menggabungkan 11 test case granular (TC-GS-USER-118 s.d. TC-GS-USER-1033).
