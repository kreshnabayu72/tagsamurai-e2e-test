---
id: TC-GS-DIV-E2E-041-delete-single-resilience-double-submit-dan-server-error
title: "Ketahanan Delete Single: Guard Double Submit Tombol Delete dan Kegagalan Server 500"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-122
  - TC-GS-DIV-123
coverage:
  web: automated
---

# Ketahanan Delete Single: Guard Double Submit Tombol Delete dan Kegagalan Server 500

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Mode: mock (Spectra.intercept())
- Kebutuhan mock: intercept DELETE /divisions/:id untuk simulasi 500
- User berada di Global Settings > User > Division
- Division `Strategy` (Code `STR`) bebas relasi (TC-GS-DIV-30)
- Division `Supply Chain` (Code `SC`) bebas relasi (TC-GS-DIV-30)

## Test Steps

### Delete Division yang sudah dihapus pihak lain berhasil tanpa error (TC-GS-DIV-122)

1. Admin A membuka row action baris `Strategy` lalu klik `Delete` hingga dialog konfirmasi tampil
2. Admin B menghapus Division `Strategy`
3. Admin A klik `[Delete]`
4. Verifikasi Tidak ada pesan error
5. Verifikasi Muncul toast sukses: `Success, division has been deleted.`
6. Verifikasi Daftar di-refresh dan baris `Strategy` tidak ada

### Delete gagal 5xx tidak menghapus Division dan dialog tetap terbuka (TC-GS-DIV-123)

7. Buka row action baris `Supply Chain` lalu klik `Delete`
8. Paksa respons hapus 5xx
9. Klik `[Delete]`
10. Verifikasi Muncul toast error: `Error, failed to delete division.`
11. Verifikasi Division `Supply Chain` tidak terhapus dan tetap tampil di tabel
12. Verifikasi Dialog tetap terbuka dan `[Delete]` enabled kembali untuk retry

## Notes

- Memvalidasi guard double submit pada tombol dialog [Delete] dan penanganan error 500 (record tidak terhapus dan toast error generik tampil) (PRD §9.6).
- Sumber pemetaan test case granular: TC-GS-DIV-122, TC-GS-DIV-123.
