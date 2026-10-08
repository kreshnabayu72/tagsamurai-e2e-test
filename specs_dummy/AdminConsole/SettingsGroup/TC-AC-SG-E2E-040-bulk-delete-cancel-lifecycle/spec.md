---
id: TC-AC-SG-E2E-040-bulk-delete-cancel-lifecycle
title: "Pembatalan dialog Bulk Delete pada varian homogen dan varian campuran"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-77
coverage:
  web: automated
---

# Pembatalan dialog Bulk Delete pada varian homogen dan varian campuran

## Prerequisites

- Login sebagai Role: Total Control
- Multiple group terpilih

## Test Steps

### Pembatalan Dialog Bulk Homogen
1. Centang 2 group kosong yang aman
2. Klik `[Delete]` pada Bulk Action Bar
3. Pada dialog konfirmasi homogen `"Delete Groups"`, klik tombol `[Cancel]`
4. Verifikasi dialog tertutup, seleksi checkbox tetap utuh, dan tidak ada data terhapus
### Pembatalan Dialog Bulk Campuran
5. Tambahkan centang pada 1 group yang memiliki member (kondisi campuran)
6. Klik `[Delete]` pada Bulk Action Bar
7. Pada dialog campuran 2 kelompok bullet, klik tombol `[Cancel]`
8. Verifikasi dialog tertutup dan seluruh data tetap utuh

## Notes

- Memverifikasi integritas pembatalan aksi destruktif massal.
