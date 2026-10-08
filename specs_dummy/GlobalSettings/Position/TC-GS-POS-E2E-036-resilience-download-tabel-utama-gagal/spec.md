---
id: TC-GS-POS-E2E-036-resilience-download-tabel-utama-gagal
title: "Resilience: Download tabel utama saat gagal menghasilkan toast error"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-199
coverage:
  web: automated
---

# Resilience: Download tabel utama saat gagal menghasilkan toast error

## Prerequisites

- Mode: mock
- Login sebagai Total Control
- Intersep permintaan ekspor file ke error 500

## Test Steps

### Simulasi Kegagalan Download

1. Buka overlay Download pada tabel Position
2. Aktifkan intersep error 500 pada endpoint download
3. Klik "Download as CSV"
4. Verifikasi toast error "Unable to download file." muncul
5. Verifikasi halaman tabel tidak crash dan tetap dapat digunakan secara normal

## Notes

- Mode: mock untuk simulasi kegagalan unduhan file (TC-GS-POS-199).
