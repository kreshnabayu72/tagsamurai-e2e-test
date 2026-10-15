---
id: TC-AC-SU-E2E-011-user-list-export-failure-resilience-dan-toast-error
title: "Ketahanan ekspor User List: simulasi kegagalan server 500 dan toast error feedback"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-280
coverage:
  web: automated
---

# Ketahanan ekspor User List: simulasi kegagalan server 500 dan toast error feedback

## Prerequisites

- Mode: mock
- Mode: mock
- Login sebagai Role: Total Control
- Mock endpoint `POST /v2/iam/products/admin_console/users/export` untuk mengembalikan error 500

## Test Steps

### Simulasi Error Ekspor 500
1. Intercept request export `POST /v2/iam/products/admin_console/users/export` dan paksa mengembalikan response status 500 Internal Server Error
2. Buka halaman `Settings > User`
3. Klik tombol `[Download]` pada toolbar dan pilih format CSV
4. Verifikasi sistem tidak mengunduh file rusak atau file kosong
5. Verifikasi muncul toast error dengan pesan literal: `"Error, failed to download User."`
6. Hapus interceptor mock error
7. Klik tombol `[Download]` kembali dan verifikasi ekspor berhasil tanpa error

## Notes

- Memisahkan pengujian fault injection ekspor dari validasi integritas binary file.
