---
id: TC-GS-DIV-E2E-050-bulk-delete-resilience-double-submit-dan-server-500
title: "Ketahanan Bulk Delete: Guard Double Submit dan Kegagalan Server 500 All-or-Nothing Tanpa Item Terhapus"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-139
  - TC-GS-DIV-140
coverage:
  web: automated
---

# Ketahanan Bulk Delete: Guard Double Submit dan Kegagalan Server 500 All-or-Nothing Tanpa Item Terhapus

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Mode: mock (Spectra.intercept())
- Kebutuhan mock: intercept DELETE batch divisions untuk simulasi 500
- User berada di Global Settings > User > Division
- Division `Research and Development` dan `Internal Control` bebas relasi (TC-GS-DIV-30)
- Division `Quality Assurance` dan `Product Management` bebas relasi (TC-GS-DIV-30)

## Test Steps

### Item berubah in-use setelah pre-check di-skip diam-diam ke ringkasan (TC-GS-DIV-139)

1. Centang baris `Research and Development` dan `Internal Control`
2. Klik aksi `[Delete]` hingga Dialog homogen tampil
3. Admin lain menugaskan Division `Internal Control` ke sebuah user
4. Klik `[Delete]` pada dialog
5. Verifikasi `Research and Development` terhapus dan `Internal Control` tetap ada
6. Verifikasi Item yang berubah in-use di-skip tanpa error dan tanpa meng-crash batch
7. Verifikasi Muncul toast sukses: `Success, division has been deleted. Some items were skipped.`

### Bulk Delete gagal 5xx tidak menghapus satu pun Division (TC-GS-DIV-140)

8. Centang baris `Quality Assurance` dan `Product Management`
9. Klik aksi `[Delete]` lalu paksa respons hapus 5xx
10. Klik `[Delete]` pada dialog
11. Verifikasi Muncul toast error: `Error, failed to delete division.`
12. Verifikasi Kedua Division tetap ada (all-or-nothing)
13. Verifikasi Dialog tetap terbuka dan `[Delete]` enabled kembali untuk retry

## Notes

- Memvalidasi guard double submit pada dialog bulk delete dan transaksi all-or-nothing: kegagalan 500 tidak menghapus satu pun item di database (PRD §9.6).
- Sumber pemetaan test case granular: TC-GS-DIV-139, TC-GS-DIV-140.
