---
id: TC-GS-ACTLOG-E2E-002-loading-skeleton-dan-read-failure-resilience
title: "Loading Skeleton dan Ketahanan Kegagalan Load Tabel di Kedua Tab"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-04
  - TC-GS-ACTLOG-08
  - TC-GS-ACTLOG-09
coverage:
  web: automated
---

# Loading Skeleton dan Ketahanan Kegagalan Load Tabel di Kedua Tab

## Prerequisites

Mode: mock
- Login sebagai Role: Total Control Global Settings
- Mock/intercept endpoint list log dengan network throttle dan fault injection HTTP 500

## Test Steps

### Skeleton Loading State
1. Aktifkan simulasi penundaan respons jaringan (network throttle) pada endpoint daftar log.
2. Buka halaman Global Settings > Activity Log > Session.
3. Verifikasi skeleton loader tampil pada area tabel Tab Session selama data sedang diambil.
4. Klik tab 'User Action'.
5. Verifikasi skeleton loader tampil pada area tabel Tab User Action selama data sedang diambil.
6. Lepas penahanan respons dan verifikasi tabel normal beserta data dan paginasi muncul di kedua tab.
### Error Load State & Recovery
7. Simulasikan kegagalan server HTTP 5xx pada endpoint daftar log Tab Session.
8. Buka Tab Session dan amati tampilan area tabel.
9. Verifikasi alert error 'Unable to load this data.' tampil dengan tombol [Try Again], dan komponen empty state tidak muncul.
10. Simulasikan kegagalan server HTTP 5xx pada endpoint daftar log Tab User Action.
11. Klik tab 'User Action' dan verifikasi alert error 'Unable to load this data.' beserta tombol [Try Again] tampil.
12. Kembalikan respons endpoint ke kondisi normal (sukses 200).
13. Klik tombol [Try Again] pada Tab User Action.
14. Verifikasi alert error hilang dan tabel normal beserta paginasi kembali dimuat.
15. Kembali ke Tab Session dan klik tombol [Try Again], verifikasi tabel normal kembali dimuat.

## Notes

- Ketahanan kegagalan baca data memastikan pengguna mendapatkan umpan balik yang jelas dan tombol pemulihan [Try Again].
