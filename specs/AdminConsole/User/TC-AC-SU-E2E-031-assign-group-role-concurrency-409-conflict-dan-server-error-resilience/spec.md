---
id: TC-AC-SU-E2E-031-assign-group-role-concurrency-409-conflict-dan-server-error-resilience
title: "Resiliensi error 5xx dan penanganan 409 Conflict pada popup Assign Group Role"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-97
  - TC-AC-SU-98
  - TC-AC-SU-177
coverage:
  web: automated
---

# Resiliensi error 5xx dan penanganan 409 Conflict pada popup Assign Group Role

## Prerequisites

- Mode: mock
- Login sebagai Role: Principal Total Control
- Simulasi mock respons 500 dan 409 pada endpoint PUT group-role assignment

## Test Steps

### Simulasi Server Error 5xx saat Save Group Role

1. Buka popup Assign Group Role dan modifikasi penugasan group
2. Konfigurasikan mock network agar endpoint PUT mengembalikan status 500
3. Klik tombol `[Save]`
4. Verifikasi toast error muncul: `"Error, failed to assign group role."`
5. Verifikasi popup tetap terbuka, isian data dipertahankan, dan tombol `[Save]` tetap enabled untuk retry

### Penanganan Concurrency 409 Conflict saat Save

1. Konfigurasikan mock agar endpoint PUT mengembalikan status `409 Conflict` (penugasan telah diubah oleh admin lain)
2. Klik tombol `[Save]`
3. Verifikasi dialog peringatan muncul: `"This group assignment was changed by someone else. Please review."`
4. Klik tombol konfirmasi pada dialog, verifikasi data popup dimuat ulang sesuai data baseline terbaru dari server

## Notes

- Mekanisme optimistic lock mendeteksi konflik penugasan serentak antar admin.
