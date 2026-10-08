---
id: TC-GS-POS-E2E-023-resilience-delete-single-kegagalan-server
title: "Resilience: Dialog Delete single saat kegagalan server 5xx menampilkan toast error dan record tetap ada"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-121
coverage:
  web: automated
---

# Resilience: Dialog Delete single saat kegagalan server 5xx menampilkan toast error dan record tetap ada

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Intersep DELETE /positions/:id dikonfigurasi untuk mengembalikan 500

## Test Steps

### Simulasi Server 500 Saat Delete Single

1. Buka dialog Delete pada salah satu record Position bebas relasi
2. Aktifkan intersep respons 500 Internal Server Error
3. Klik tombol "[Delete]" pada dialog
4. Verifikasi dialog tertutup, toast error "Unable to delete position." muncul
5. Verifikasi record Position tetap utuh di tabel dan tidak terhapus

## Notes

- Mode: mock untuk simulasi kegagalan server 5xx (TC-GS-POS-121).
