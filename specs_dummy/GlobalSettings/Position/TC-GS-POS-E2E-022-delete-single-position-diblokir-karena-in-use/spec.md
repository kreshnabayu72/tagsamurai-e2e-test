---
id: TC-GS-POS-E2E-022-delete-single-position-diblokir-karena-in-use
title: "Blokir Delete single karena Position dipakai user Login aktif, Non-Login, atau user non-aktif"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-114
  - TC-GS-POS-115
  - TC-GS-POS-116
  - TC-GS-POS-117
coverage:
  web: automated
---

# Blokir Delete single karena Position dipakai user Login aktif, Non-Login, atau user non-aktif

## Prerequisites

- Login sebagai Role: Total Control
- Record "Warehouse Supervisor" dipakai user Login aktif (Rina Wulandari)
- Record "Customer Success Manager" dipakai user Non-Login (Agus Pratama)
- Record "Procurement Officer" dipakai user Login non-aktif (Dewi Lestari)

## Test Steps

### Blokir Dipakai User Login Aktif

1. Buka menu ⋯ pada baris "Warehouse Supervisor", klik "Delete"
2. Verifikasi dialog "Cannot Delete Data" muncul dengan pesan bahwa jabatan masih digunakan oleh user
3. Verifikasi dialog hanya menyediakan tombol "[OK]" (tanpa tombol konfirmasi hapus)
4. Klik tombol "[OK]", verifikasi dialog tertutup dan record tetap ada

### Blokir Dipakai User Non-Login

5. Buka menu ⋯ pada baris "Customer Success Manager", klik "Delete"
6. Verifikasi dialog "Cannot Delete Data" muncul
7. Klik "[OK]", verifikasi penghapusan diblokir

### Blokir Dipakai User Non-Aktif (NC-02)

8. Buka menu ⋯ pada baris "Procurement Officer", klik "Delete"
9. Verifikasi dialog "Cannot Delete Data" muncul (user non-aktif tetap dihitung in-use)
10. Klik "[OK]" dan verifikasi record tidak terhapus

## Notes

- Menggabungkan kasus data condition blocked untuk single delete (TC-GS-POS-114, 115, 116, 117) sesuai keputusan NC-02.
