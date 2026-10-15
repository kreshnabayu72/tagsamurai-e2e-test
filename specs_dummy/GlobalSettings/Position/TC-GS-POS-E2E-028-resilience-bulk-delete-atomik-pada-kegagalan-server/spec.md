---
id: TC-GS-POS-E2E-028-resilience-bulk-delete-atomik-pada-kegagalan-server
title: "Resilience: Bulk Delete atomik all-or-nothing tidak menghapus record saat kegagalan server 5xx"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-149
coverage:
  web: automated
---

# Resilience: Bulk Delete atomik all-or-nothing tidak menghapus record saat kegagalan server 5xx

## Prerequisites

- Mode: mock
- Login sebagai Total Control
- 3 record Position bebas relasi dipilih
- Spectra.intercept() dikonfigurasi mengembalikan 500 pada permintaan bulk-delete

## Test Steps

### Kegagalan Server Atomik All-or-Nothing

1. Centang 3 baris record Position bebas relasi
2. Klik tombol "[Delete]" pada Bulk Action Bar
3. Aktifkan intersep error 500 Internal Server Error
4. Klik tombol konfirmasi "[Delete]" pada dialog
5. Verifikasi toast error server muncul
6. Verifikasi sifat atomik berlaku: ketiga record tetap ada di tabel (tidak ada record yang terhapus sebagian)

## Notes

- Mode: mock untuk simulasi kegagalan atomik bulk delete (TC-GS-POS-149 per keputusan NC-03).
