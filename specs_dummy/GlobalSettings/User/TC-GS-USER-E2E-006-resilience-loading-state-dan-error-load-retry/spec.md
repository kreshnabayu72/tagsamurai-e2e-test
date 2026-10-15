---
id: TC-GS-USER-E2E-006-resilience-loading-state-dan-error-load-retry
title: "Resilience: Loading skeleton dan penanganan error load via Try Again"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-8
  - TC-GS-USER-23
  - TC-GS-USER-994
  - TC-GS-USER-995
coverage:
  web: automated
---

# Resilience: Loading skeleton dan penanganan error load via Try Again

## Prerequisites

- Mode: mock
- Mode: mock
- Login sebagai Role: Total Control
- Intercept HTTP GET endpoint user list dan modal changelog

## Test Steps

### Skeleton Loader

1. Aktifkan penundaan respons (throttle) pada endpoint pengambilan list user
2. Buka Global Settings > User > User List
3. Verifikasi area tabel menampilkan skeleton loading dan tidak menampilkan ilustrasi empty/error state

### Error Load User List

4. Konfigurasikan intersep respons error HTTP 500 pada endpoint user list
5. Refresh halaman User List
6. Verifikasi tabel menampilkan pesan error 'Unable to load this data.' beserta tombol '[Try Again]'
7. Lepas simulasi error 500 dan kembalikan koneksi normal
8. Klik tombol '[Try Again]'
9. Verifikasi data tabel berhasil dimuat ulang dan skeleton digantikan oleh baris data riil

### Error Load Modal Changelog dan Detail Tab

10. Konfigurasikan intersep respons error HTTP 500 pada endpoint changelog
11. Buka Modal Changelog User List, verifikasi area modal menampilkan pesan error dengan tombol '[Try Again]'
12. Buka halaman User Detail tab System Log dengan simulasi error, verifikasi tampilan pesan error dengan tombol '[Try Again]'

## Notes

- Menggabungkan 4 test case granular (TC-GS-USER-8 s.d. TC-GS-USER-995).
