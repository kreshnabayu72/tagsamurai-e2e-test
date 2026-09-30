---
id: TC-GS-USER-E2E-026-edit-access-subscription-tidak-aktif
title: Edit Access untuk produk yang subscription-nya sudah tidak aktif
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-389
  - TC-GS-USER-478
coverage:
  web: automated
---

# Edit Access untuk produk yang subscription-nya sudah tidak aktif

## Prerequisites

- Login sebagai Role: Total Control pada entity yang subscription "FAMS"-nya sudah tidak aktif. Entity ini khusus untuk spec ini, bukan entity yang dipakai spec lain yang butuh FAMS aktif
- User "Tono Wibowo" ada dengan Access ["Global Settings", "FAMS"], dan dicentang "FAMS" saat subscription masih aktif
- Spec ini melepas Access "FAMS" dari "Tono Wibowo", jadi datanya dibuat ulang oleh seeding sebelum run berikutnya

## Test Steps

### Access yang sudah dicentang tetap tampil

1. Klik `Edit` pada baris "Tono Wibowo"
2. Verifikasi checkbox "FAMS" tampil tercentang dan tidak dipaksa hilang, dan bisa di-uncheck secara manual
3. Klik `✕` untuk menutup modal tanpa mengubah apa pun
4. Klik `[+ User]` untuk membuka modal Create
5. Verifikasi opsi "FAMS" tidak muncul sama sekali di daftar checkbox Access
6. Klik `✕` untuk menutup modal Create

### Uncheck lalu terkunci

7. Klik `Edit` pada baris "Tono Wibowo"
8. Uncheck checkbox "FAMS"
9. Verifikasi checkbox "FAMS" otomatis terkunci (disabled) dan tidak bisa dicentang kembali
10. Klik `[Save]`
11. Klik `Edit` pada baris "Tono Wibowo" lagi
12. Verifikasi checkbox "FAMS" tetap terkunci dan tidak tercentang
13. Verifikasi Access "Tono Wibowo" di User List tidak lagi memuat "FAMS"
14. Klik `✕` lalu klik `[+ User]` dan verifikasi opsi "FAMS" tetap tidak muncul di modal Create

## Notes

- Spec ini dipisah dari alur Edit biasa karena butuh entity dengan subscription produk yang tidak aktif (prinsip 12 di `docs/e2e-conventions.md` bagian 3). Kebutuhan entity itu ditulis di Prerequisites untuk tim FE.
- Produk yang sudah tidak disubscribe tidak bisa di-attach kembali setelah dilepas.
- Kasus Access kosong pada Edit (`TC-GS-USER-31`) dicakup `TC-GS-USER-E2E-009-remove-access-user`.
