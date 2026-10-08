---
id: TC-GS-POS-E2E-003-resilience-loading-state-dan-error-try-again
title: "Resilience: Loading skeleton dan pemulihan error load via Try Again"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-6
  - TC-GS-POS-8
coverage:
  web: automated
---

# Resilience: Loading skeleton dan pemulihan error load via Try Again

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Spectra.intercept() dikonfigurasi untuk throttling jaringan dan simulasi error HTTP 500 pada endpoint GET /positions

## Test Steps

### Loading State Skeleton

1. Aktifkan penundaan respons (throttle) pada endpoint GET /positions
2. Buka tab Position
3. Verifikasi area tabel menampilkan skeleton loader komponen Loading, dan tidak menampilkan teks empty state maupun error state saat data sedang diambil

### Error Recovery via Try Again

4. Intersep permintaan GET /positions dengan respons error HTTP 500
5. Refresh atau navigasi ulang ke tab Position
6. Verifikasi area tabel menampilkan pesan error "Unable to load this data." beserta tombol "[Try Again]"
7. Lepas intersep error 500 dan kembalikan respons jaringan normal
8. Klik tombol "[Try Again]"
9. Verifikasi tabel berhasil memuat ulang data dan menampilkan baris data Position secara normal

## Notes

- Mode: mock diperlukan untuk menyimulasikan kegagalan jaringan dan respons 500 secara terkontrol (TC-GS-POS-6 dan TC-GS-POS-8).
