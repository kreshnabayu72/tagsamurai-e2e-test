---
id: TC-GS-ACTLOG-E2E-002-loading-skeleton-dan-read-failure-resilience
title: "Loading skeleton dan ketahanan terhadap kegagalan pembacaan data di kedua tab"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-04
  - TC-GS-ACTLOG-05
  - TC-GS-ACTLOG-10
  - TC-GS-ACTLOG-11
coverage:
  web: automated
---

# Loading skeleton dan ketahanan terhadap kegagalan pembacaan data di kedua tab

## Prerequisites

Mode: mock
- Login sebagai Role: Total Control
- Mock intercept: Network delay 2000 ms pada request list Tab Session dan Tab User Action
- Mock intercept: Status 500 / Network Error pada endpoint list kedua tab

## Test Steps

### Loading & Error State Tab Session
1. Pasang mock network delay pada request list Tab Session
2. Buka `Global Settings > Activity Log > Tab Session`
3. Verifikasi komponen loading skeleton tampil sebelum data selesai dimuat
4. Pasang mock response error 500 pada endpoint list Tab Session
5. Muat ulang Tab Session
6. Verifikasi pesan error "Unable to load this data." beserta tombol `[Try Again]` tampil di layar (bukan empty state)
7. Lepas mock error 500 dan klik tombol `[Try Again]`
8. Verifikasi tabel Tab Session berhasil memuat data normal
### Loading & Error State Tab User Action
9. Pasang mock network delay pada request list Tab User Action
10. Klik tab "User Action"
11. Verifikasi skeleton 10 baris tampil sesaat sebelum data selesai dimuat
12. Pasang mock response error 500 pada endpoint list Tab User Action
13. Muat ulang Tab User Action
14. Verifikasi pesan error "Unable to load this data." beserta tombol `[Try Again]` tampil di layar
15. Lepas mock error 500 dan klik tombol `[Try Again]`
16. Verifikasi tabel Tab User Action berhasil memuat data normal

## Notes

- Kegagalan fetch data list harus menampilkan state error deskriptif dengan opsi pemulihan manual `[Try Again]` alih-alih keliru menampilkan empty state.
