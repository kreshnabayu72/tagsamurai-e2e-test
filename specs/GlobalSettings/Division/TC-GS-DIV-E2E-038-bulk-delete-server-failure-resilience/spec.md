---
id: TC-GS-DIV-E2E-038-bulk-delete-server-failure-resilience
title: "Ketahanan Eksekusi Bulk Delete Terhadap Kegagalan Server 5xx/Timeout"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-53
coverage:
  web: automated
---

# Ketahanan Eksekusi Bulk Delete Terhadap Kegagalan Server 5xx/Timeout

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Mock intercept request DELETE /v2/iam/divisions disimulasikan error 500 / timeout

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Centang beberapa baris divisi lalu klik '[Delete]' pada Bulk Action Bar
3. Kondisikan interceptor mengembalikan status 500 saat dialog konfirmasi di-submit
4. Klik tombol '[Delete]' pada dialog
5. Verifikasi toast error muncul: 'Error, failed to delete division.'
6. Verifikasi dialog menutup dan data yang dipilih TIDAK terhapus dari tabel utama

## Notes

- Menguji ketahanan aksi destruktif massal terhadap kegagalan jaringan (division.md §7 dan §9.6).
