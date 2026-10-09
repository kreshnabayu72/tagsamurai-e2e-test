---
id: TC-GS-GSET-E2E-003-resilience-loading-skeleton-error-load-dan-retry
title: "Resilience: Loading skeleton halaman, error load, dan pemulihan via Try Again"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-03
  - TC-GS-GSET-04
  - TC-GS-GSET-05
coverage:
  web: automated
---

# Resilience: Loading skeleton halaman, error load, dan pemulihan via Try Again

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
- Spectra.intercept() dikonfigurasi untuk menahan respons GET general settings (delay) dan memaksa error HTTP 500 pada endpoint yang sama

## Test Steps

### Loading Skeleton

1. Aktifkan penundaan (delay 5 detik) pada respons GET general settings
2. Buka Global Settings > General Settings
3. Verifikasi halaman menampilkan Loading component berupa shimmer skeleton yang mempertahankan proporsi grid form sebelum respons diterima
4. Verifikasi setelah respons diterima skeleton diganti form terisi nilai tersimpan

### Error Load

5. Intersep GET general settings dengan respons error HTTP 500
6. Buka Global Settings > General Settings
7. Verifikasi tampil teks "Unable to load this data." beserta tombol `[Try Again]`, bukan empty state dan bukan form kosong

### Pemulihan via Try Again

8. Lepas intersep 500 dan kembalikan respons jaringan normal
9. Klik `[Try Again]`
10. Verifikasi form terisi nilai tersimpan: `IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`
11. Verifikasi teks "Unable to load this data." hilang

## Notes

- Mode: mock dipakai karena skenario menangkap tampilan loading dan simulasi kegagalan baca yang butuh kontrol penuh atas respons (TC-GS-GSET-03, TC-GS-GSET-04, TC-GS-GSET-05).
