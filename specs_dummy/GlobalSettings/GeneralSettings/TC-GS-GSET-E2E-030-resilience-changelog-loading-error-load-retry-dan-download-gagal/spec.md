---
id: TC-GS-GSET-E2E-030-resilience-changelog-loading-error-load-retry-dan-download-gagal
title: "Resilience Modal Changelog: loading riwayat, error load + Try Again, dan kegagalan Download"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-62
  - TC-GS-GSET-64
  - TC-GS-GSET-101
coverage:
  web: automated
---

# Resilience Modal Changelog: loading riwayat, error load + Try Again, dan kegagalan Download

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Changelog General Settings berisi baris riwayat (dinamis)
- Spectra.intercept() dikonfigurasi untuk menahan respons GET changelog, memaksa error HTTP 500 pada GET changelog, dan memaksa error HTTP 500 pada request download

## Test Steps

### Loading Riwayat

1. Aktifkan penundaan (delay 5 detik) respons GET changelog
2. Klik icon Changelog dan amati modal sebelum respons
3. Verifikasi Loading component tampil di dalam modal
4. Setelah respons diterima, verifikasi tabel terisi

### Error Load dan Try Again

5. Paksa GET changelog gagal (5xx)
6. Klik icon Changelog
7. Verifikasi tampil "Unable to load this data." dan tombol `[Try Again]` (bukan empty state)
8. Lepas intercept 500, lalu klik `[Try Again]`
9. Verifikasi tabel riwayat termuat

### Kegagalan Download

10. Paksa request download gagal (5xx)
11. Klik Download, lalu pilih `Download as CSV`
12. Verifikasi toast error "Error, failed to download Changelog-General-Settings."

## Notes

- Mode: mock untuk memaksa loading, error 500, dan kegagalan download secara terkontrol (TC-GS-GSET-62, 64, 101).
