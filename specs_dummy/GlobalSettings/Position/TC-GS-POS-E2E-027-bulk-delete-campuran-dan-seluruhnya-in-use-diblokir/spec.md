---
id: TC-GS-POS-E2E-027-bulk-delete-campuran-dan-seluruhnya-in-use-diblokir
title: "Bulk Delete campuran (sebagian in-use warn lalu continue) dan blokir total seluruhnya in-use"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-142
  - TC-GS-POS-143
  - TC-GS-POS-144
  - TC-GS-POS-145
  - TC-GS-POS-302
  - TC-GS-POS-303
coverage:
  web: automated
---

# Bulk Delete campuran (sebagian in-use warn lalu continue) dan blokir total seluruhnya in-use

## Prerequisites

- Login sebagai Total Control
- Record in-use: Warehouse Supervisor & Customer Success Manager
- Record bebas relasi: 2 record Position dummy

## Test Steps

### Blokir Total (Seluruh Item Terpilih In-Use)

1. Centang hanya record "Warehouse Supervisor" dan "Customer Success Manager" (keduanya in-use)
2. Klik tombol "[Delete]" pada Bulk Action Bar
3. Verifikasi dialog "Cannot Delete Data" muncul menampilkan daftar kedua nama jabatan tersebut
4. Verifikasi hanya ada tombol "[OK]" dan tidak ada opsi untuk melanjutkan penghapusan
5. Klik "[OK]", verifikasi tidak ada data yang terhapus

### Bulk Delete Campuran (Sebagian In-Use)

6. Centang 2 record bebas relasi DITAMBAH 1 record "Warehouse Supervisor"
7. Klik tombol "[Delete]" pada Bulk Action Bar
8. Verifikasi dialog peringatan muncul menginformasikan bahwa sebagian item sedang digunakan dan akan dilewati
9. Verifikasi daftar nama item yang akan dilewati dan yang akan dihapus tampil lengkap
10. Klik tombol "[Cancel]", verifikasi seleksi tetap terjaga
11. Klik kembali tombol "[Delete]" lalu klik "[Continue]" pada dialog
12. Verifikasi toast sukses parsial muncul: "Success, position has been deleted. Some items were skipped."
13. Verifikasi record bebas relasi terhapus, sedangkan "Warehouse Supervisor" tetap ada di tabel

## Notes

- Menggabungkan TC-GS-POS-142, 143, 144, 145, 302, dan 303 sesuai konvensi partial bulk delete.
