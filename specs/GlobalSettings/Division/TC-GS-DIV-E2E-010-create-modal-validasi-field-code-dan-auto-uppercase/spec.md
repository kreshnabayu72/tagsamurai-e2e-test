---
id: TC-GS-DIV-E2E-010-create-modal-validasi-field-code-dan-auto-uppercase
title: "Validasi Field Code: Batas 15 Karakter, Whitelist Karakter, Duplikat Debounce, dan Auto-Uppercase"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-261
  - TC-GS-DIV-262
  - TC-GS-DIV-263
  - TC-GS-DIV-264
coverage:
  web: automated
---

# Validasi Field Code: Batas 15 Karakter, Whitelist Karakter, Duplikat Debounce, dan Auto-Uppercase

## Prerequisites

- Login sebagai Role: Total Control
- Telah terdapat data divisi dengan Code 'LOG' di sistem

## Test Steps

1. Buka modal Create Division melalui tombol '[+ Division]'
2. Ketik nama valid pada Division Name
3. Ketik string 16 karakter pada field Code dan verifikasi muncul pesan error inline 'Max. 15 characters'
4. Ketik kode dengan karakter non-whitelist seperti 'LOG@ISTIC' pada field Code
5. Verifikasi muncul pesan error inline 'Code contains invalid characters' (hanya huruf, angka, tanda hubung, garis bawah, dan titik yang diizinkan)
6. Ketik kode dengan huruf kecil 'mkt' pada field Code
7. Verifikasi teks otomatis terkonversi menjadi huruf kapital 'MKT' saat mengetik (auto-uppercase)
8. Ketik kode 'log' (huruf kecil dari Code 'LOG' yang sudah ada) dan tunggu debounce ~500ms
9. Verifikasi muncul pesan error inline 'Code already exists'

## Notes

- Aturan format kode divisi mengacu pada DIV-LOGIC-04 dan division.md §9.9.
