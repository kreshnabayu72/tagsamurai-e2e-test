---
id: TC-GS-DIV-E2E-003-loading-skeleton-dan-read-failure-resilience
title: "Tampilan Loading Skeleton, Kegagalan Fetch Data 500, dan Pemulihan via Tombol Try Again"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-5
  - TC-GS-DIV-8
  - TC-GS-DIV-9
coverage:
  web: automated
---

# Tampilan Loading Skeleton, Kegagalan Fetch Data 500, dan Pemulihan via Tombol Try Again

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Mode: mock (Spectra.intercept())
- Kebutuhan mock: intercept GET /divisions dengan delay 3 detik untuk loading skeleton, dan paksa respons 500 untuk simulasi error fetch
- User berada di Global Settings > User > Division

## Test Steps

### Tampilan Loading saat data tabel diambil (TC-GS-DIV-5)

1. Tahan (delay) respons daftar Division di network
2. Buka Tab Division
3. Perhatikan tabel sebelum respons datang
4. Verifikasi Skeleton loader / Loading component tampil pada area tabel selama menunggu
5. Verifikasi Data tampil dan skeleton hilang setelah respons diterima

### Error Load tabel saat pengambilan data gagal (TC-GS-DIV-8)

6. Paksa respons daftar Division gagal 5xx
7. Buka Tab Division
8. Verifikasi Tabel menampilkan teks `Unable to load this data.`
9. Verifikasi Tombol `[Try Again]` tampil
10. Verifikasi Tampilan bukan empty state `No division yet`

### Klik Try Again memuat ulang data setelah Error Load (TC-GS-DIV-9)

11. Paksa respons daftar Division gagal 5xx
12. Buka Tab Division dan tunggu `Unable to load this data.`
13. Pulihkan respons daftar Division
14. Klik `[Try Again]`
15. Verifikasi Data tabel Division dimuat ulang dan tampil
16. Verifikasi Teks `Unable to load this data.` dan tombol `[Try Again]` hilang

## Notes

- Memvalidasi transisi state loading skeleton (S-01), error state (S-05: "Unable to load this data." + [Try Again]), dan pemulihan data saat tombol Try Again diklik (PRD §7).
- Sumber pemetaan test case granular: TC-GS-DIV-5, TC-GS-DIV-8, TC-GS-DIV-9.
