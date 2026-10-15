---
id: TC-GS-USER-E2E-037-bulk-delete-dialog-dan-eksekusi-seleksi-campuran
title: "Bulk Delete: Dialog konfirmasi, cancel path, skip item terproteksi, dan eksekusi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-1028
  - TC-GS-USER-1037
  - TC-GS-USER-1038
coverage:
  web: automated
---

# Bulk Delete: Dialog konfirmasi, cancel path, skip item terproteksi, dan eksekusi

## Prerequisites

- Login sebagai Role: Total Control
- User dinamis untuk bulk delete (Tono Wijaya, Rani Lestari) tersedia

## Test Steps

### Dialog Konfirmasi dan Cancel Path

1. Pilih user Tono Wijaya dan Rani Lestari via checkbox
2. Klik 'Delete' pada Bulk Bar
3. Verifikasi dialog konfirmasi Bulk Delete muncul dengan daftar nama user yang akan dihapus
4. Klik '[Cancel]', verifikasi dialog tertutup dan tidak ada user yang terhapus

### Eksekusi Bulk Delete

5. Klik 'Delete' kembali pada Bulk Bar, lalu klik tombol konfirmasi '[Delete]'
6. Verifikasi toast sukses muncul dan kedua user terhapus dari User List

## Notes

- Menggabungkan 3 test case granular (TC-GS-USER-1028 s.d. TC-GS-USER-1038).
