---
id: TC-AC-SG-E2E-033-delete-single-server-error-dan-retensi-record
title: "Penanganan kegagalan Delete Single saat server error 5xx dan retensi integritas record"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-153
coverage:
  web: automated
---

# Penanganan kegagalan Delete Single saat server error 5xx dan retensi integritas record

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Group kosong yang eligible untuk dihapus
- Mode: mock (Spectra.intercept DELETE /groups/{id})

## Test Steps

### Kegagalan Server saat Delete
1. Klik `[Delete]` pada group target
2. Pasang interceptor mock respons 500 Server Error pada request DELETE
3. Klik tombol konfirmasi `[Delete]` pada dialog
4. Verifikasi toast error `"Error, failed to delete group."` tampil di layar
5. Verifikasi dialog konfirmasi tertutup
6. Verifikasi record group target TIDAK TERHAPUS dan tetap tampil normal di tabel utama

## Notes

- Memastikan integritas visual dan data saat kegagalan transaksi backend terjadi.
