---
id: TC-GS-POS-E2E-042-resilience-download-popup-changelog-gagal
title: "Resilience: Download Popup Changelog saat gagal menampilkan toast error"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-240
coverage:
  web: automated
---

# Resilience: Download Popup Changelog saat gagal menampilkan toast error

## Prerequisites

- Mode: mock
- Login sebagai Total Control
- Intersep permintaan ekspor changelog ke error 500

## Test Steps

### Kegagalan Download Changelog

1. Buka Popup Changelog
2. Aktifkan intersep error 500 pada endpoint export changelog
3. Klik "Download as CSV"
4. Verifikasi toast error "Unable to download file." muncul
5. Verifikasi popup Changelog tidak crash dan tetap terbuka

## Notes

- Mode: mock untuk simulasi kegagalan download changelog (TC-GS-POS-240).
