---
id: TC-AC-SU-E2E-031-tab-role-global-role-crud-autosave-error-5xx-rollback-resilience
title: "Resiliensi Autosave CRUD Global Role Terhadap Error Jaringan 5xx dan Visual Rollback"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-176
  - TC-AC-SU-252
coverage:
  web: automated
---

# Resiliensi Autosave CRUD Global Role Terhadap Error Jaringan 5xx dan Visual Rollback

## Prerequisites

- Mode: mock
- Login sebagai Administrator Total Control
- Berada di halaman Detail User > Tab Role > Sub-tab Global Role
- Interceptor mock disiapkan untuk merespons 500 pada endpoint PATCH /users/{id}/permissions/global

## Test Steps

### Simulasi Autosave Error dan Visual Rollback
1. Buka Detail User > tab `Role` > sub-tab `Global Role`
2. Temukan baris Global Role aktif yang memiliki izin CRUD
3. Atur mock interceptor untuk mengembalikan status `500 Internal Server Error` pada request mutasi permission
4. Klik checkbox izin `Update` yang sebelumnya belum tercentang
5. Verifikasi indikator loading autosave muncul seketika
6. Verifikasi setelah kegagalan respons 500 diterima, checkbox izin `Update` secara otomatis me-rollback statusnya kembali ke unchecked (tidak tercentang)
7. Verifikasi toast error muncul: `"Failed to update permission. Please try again."`
8. Refresh halaman (F5) dan pastikan di database status izin `Update` memang tidak berubah

## Notes

Memastikan ketahanan UI saat terjadi kegagalan autosave tanpa tombol simpan manual.
