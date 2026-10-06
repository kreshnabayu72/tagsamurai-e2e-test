---
id: TC-AC-ACAL-E2E-002-loading-skeleton-dan-error-recovery
title: "Loading state, simulasi error fetch 500, dan pemulihan tabel via tombol Try Again"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-06
  - TC-AC-ACAL-07
  - TC-AC-ACAL-12
  - TC-AC-ACAL-13
  - TC-AC-ACAL-14
  - TC-AC-ACAL-15
coverage:
  web: automated
---

# Loading state, simulasi error fetch 500, dan pemulihan tabel via tombol Try Again

## Prerequisites

- Mode: mock
- Login sebagai Role: Principal Total Control
- Mock response delay dan mock error 500 pada endpoint `/v2/analytics-reporting/session-logs/list` dan `/v2/analytics-reporting/change-logs/list`

## Test Steps

### Loading State & Error Load Tab Session

1. Intercept endpoint `/v2/analytics-reporting/session-logs/list` dengan delay response
2. Buka menu `Admin Console > Activity Log`
3. Verifikasi komponen loading skeleton tampil saat data sedang dimuat di Tab Session
4. Ubah mock endpoint `/v2/analytics-reporting/session-logs/list` mengembalikan status 500 (Internal Server Error)
5. Refresh halaman atau trigger reload Tab Session
6. Verifikasi state error tampil dengan pesan `"Unable to load this data."` dan tombol `[Try Again]`

### Recovery Tab Session

7. Kembalikan mock endpoint `/v2/analytics-reporting/session-logs/list` ke respons normal 200 OK
8. Klik tombol `[Try Again]`
9. Verifikasi re-fetch berhasil dan tabel Tab Session kembali tampil normal dengan data

### Loading State & Error Load Tab User Action

10. Klik tab `"User Action"` dengan kondisi intercept delay pada endpoint `/v2/analytics-reporting/change-logs/list`
11. Verifikasi komponen loading skeleton tampil pada Tab User Action
12. Ubah mock endpoint `/v2/analytics-reporting/change-logs/list` mengembalikan status 500
13. Trigger reload atau tab switch kembali ke Tab User Action
14. Verifikasi state error tampil dengan pesan `"Unable to load this data."` dan tombol `[Try Again]`

### Recovery Tab User Action

15. Kembalikan mock endpoint `/v2/analytics-reporting/change-logs/list` ke respons normal 200 OK
16. Klik tombol `[Try Again]`
17. Verifikasi re-fetch berhasil dan tabel Tab User Action kembali tampil normal

## Notes

- Pengujian error handling server 500 dan loading delay menggunakan network interception (mock).
