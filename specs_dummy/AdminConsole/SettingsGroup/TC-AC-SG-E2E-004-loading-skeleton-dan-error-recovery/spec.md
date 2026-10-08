---
id: TC-AC-SG-E2E-004-loading-skeleton-dan-error-recovery
title: "Loading skeleton dan pemulihan error load data via tombol Try Again"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-5
  - TC-AC-SG-6
coverage:
  web: automated
---

# Loading skeleton dan pemulihan error load data via tombol Try Again

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Mode: mock (Spectra.intercept pada endpoint GET/POST /groups/list)

## Test Steps

### Loading Skeleton State
1. Pasang interceptor network delay (3000ms) pada endpoint list group
2. Buka halaman `Settings > Group` dan amati state tabel sesaat setelah navigasi
3. Verifikasi komponen loading skeleton tabel dan sidebar dirender selama proses fetch data berlangsung
### Error Recovery State
4. Pasang interceptor HTTP 500 Server Error pada endpoint list group
5. Lakukan reload halaman `Settings > Group`
6. Verifikasi tabel menampilkan pesan error `"Unable to load this data."` dan tombol `[Try Again]`
7. Hapus interceptor HTTP 500 (kembalikan ke respons normal 200 OK)
8. Klik tombol `[Try Again]`
9. Verifikasi state error hilang dan tabel berhasil me-render daftar data group secara normal

## Notes

- Membutuhkan Network Mock Interceptor untuk simulasi latency dan response code 500.
