---
id: TC-GS-POS-E2E-013-resilience-create-position-kegagalan-server
title: "Resilience: Form Create mempertahankan input saat kegagalan server 5xx dan timeout jaringan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-67
  - TC-GS-POS-68
coverage:
  web: automated
---

# Resilience: Form Create mempertahankan input saat kegagalan server 5xx dan timeout jaringan

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Form Create Position dibuka
- Spectra.intercept() dikonfigurasi untuk menangani permintaan POST /positions

## Test Steps

### Respons Server 500

1. Buka form Create Position dan isi Position Name "DevOps Specialist"
2. Konfigurasikan intersep POST /positions agar mengembalikan error HTTP 500 Internal Server Error
3. Klik tombol "[Submit]"
4. Verifikasi toast error server muncul
5. Verifikasi modal Create tetap terbuka dan input "DevOps Specialist" tidak hilang sehingga user tidak perlu mengetik ulang

### Timeout Jaringan

6. Konfigurasikan intersep POST /positions agar mengalami network timeout
7. Klik kembali tombol "[Submit]"
8. Verifikasi toast error timeout atau koneksi muncul
9. Verifikasi modal tetap terbuka dan input tetap terjaga

## Notes

- Mode: mock untuk simulasi kegagalan server 5xx dan network timeout (TC-GS-POS-67 dan 68).
