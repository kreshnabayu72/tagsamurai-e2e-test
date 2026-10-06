---
id: TC-GS-ROLE-E2E-021-detail-table-user-picker-stale-reference-resilience
title: "Penanganan Stale Reference pada Popup Table User Picker Saat User Dihapus / Di-assign Bersamaan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-332
  - TC-GS-ROLE-357
coverage:
  web: automated
---

# Penanganan Stale Reference pada Popup Table User Picker Saat User Dihapus / Di-assign Bersamaan

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Intersept endpoint submit penugasan role disiapkan untuk merespons HTTP 422 stale reference

## Test Steps

1. Buka Global Settings > Role & Permission > Tab System > Detail role 'Manage files'
2. Klik tombol [+ Assign] pada toolbar
3. Pilih 2 user pada tabel picker (User A dan User B)
4. Simulasikan User A telah dihapus atau di-assign oleh admin lain di background sebelum tombol disubmit
5. Klik tombol [Assign]
6. Verifikasi sistem menerima respons 422 dan menampilkan pesan peringatan inline yang menandakan user tidak lagi tersedia
7. Verifikasi centang seleksi pada User A otomatis dibatalkan (uncheck)
8. Verifikasi centang seleksi pada User B tetap dipertahankan dan popup picker tetap terbuka agar admin dapat melanjutkan submit

## Notes

- Penanganan stale reference tidak membatalkan seluruh pilihan, melainkan hanya me-remove item yang stale (error-handling-convention §5.7).
