---
id: TC-AC-SU-E2E-019-activate-deactivate-server-error-optimistic-rollback-dan-409-conflict
title: "Resiliensi error 5xx dengan optimistic rollback dan penanganan 409 Conflict pada Activate/Deactivate"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-41
  - TC-AC-SU-174
  - TC-AC-SU-219
  - TC-AC-SU-263
coverage:
  web: automated
---

# Resiliensi error 5xx dengan optimistic rollback dan penanganan 409 Conflict pada Activate/Deactivate

## Prerequisites

- Mode: mock
- Login sebagai Role: Principal Total Control
- Simulasi mock respons 500 dan 409 pada endpoint PATCH status user

## Test Steps

### Optimistic UI Rollback pada Error 5xx

1. Konfigurasikan mock agar endpoint PATCH active status mengembalikan status 500
2. Klik switch Active pada pengguna Inactive untuk mengaktifkannya dan klik `[Activate]` pada dialog
3. Verifikasi switch tampak beralih visual sesaat lalu otomatis rollback kembali ke posisi awal (OFF)
4. Verifikasi toast error muncul: `"Error, failed to activate user."`
5. Coba nonaktifkan pengguna Active saat endpoint 500, verifikasi switch rollback kembali ke posisi ON dan muncul toast `"Error, failed to deactivate user."`

### Penanganan Concurrency 409 Conflict

1. Konfigurasikan mock agar endpoint PATCH mengembalikan status `409 Conflict` (data telah diubah admin lain)
2. Klik switch Active baris pengguna dan konfirmasi dialog
3. Verifikasi dialog peringatan muncul: `"This user was changed by someone else. Please review."` (bukan silent overwrite)
4. Klik tombol pada dialog, verifikasi data tabel User List otomatis dimuat ulang ke status terkini

## Notes

- Optimistic UI memberikan responsifitas instan dengan jaminan rollback otomatis bila transaksi gagal.
