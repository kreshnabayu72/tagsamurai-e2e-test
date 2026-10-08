---
id: TC-AC-SU-E2E-022-resilience-error-5xx-optimistic-rollback-dan-conflict-409
title: "Resiliensi Error 5xx Optimistic Rollback dan Penanganan 409 Conflict pada Switch Active"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-41
  - TC-AC-SU-174
  - TC-AC-SU-219
  - TC-AC-SU-263
coverage:
  web: automated
---

# Resiliensi Error 5xx Optimistic Rollback dan Penanganan 409 Conflict pada Switch Active

## Prerequisites

- Mode: mock
- Login sebagai Total Control
- Mock network interceptor terpasang untuk endpoint status pengguna

## Test Steps

### Resiliensi HTTP 500 dan Optimistic Rollback
1. Buka `Admin Console > Settings > User`
2. Atur interceptor jaringan agar mengembalikan respons `500 Internal Server Error` saat toggle status dikirim
3. Klik switch Active pada baris user aktif untuk mengubahnya ke posisi OFF
4. Verifikasi animasi toggle bergerak sementara ke posisi OFF
5. Verifikasi setelah respons 500 diterima, switch Active secara otomatis melakukan rollback visual kembali ke posisi ON
6. Verifikasi toast error muncul: `"Failed to change user status. Please try again."`

### Penanganan Race Condition 409 Conflict
7. Atur interceptor agar mengembalikan respons `409 Conflict` dengan pesan bahwa status telah dimutasi oleh sesi lain
8. Lakukan toggle switch Active kembali
9. Verifikasi muncul toast peringatan: `"User status has been updated by another user."`
10. Verifikasi tabel User List secara otomatis memicu re-fetch data untuk menyelaraskan status terkini

## Notes

Mencegah inkonsistensi status antara state UI lokal dan kondisi riil di database.
