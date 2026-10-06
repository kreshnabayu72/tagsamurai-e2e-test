---
id: TC-GS-ROLE-E2E-023-detail-remove-single-happy-path-dan-penurunan-counter
title: "Pencabutan Role Assignment Tunggal Sukses dan Refleksi Penurunan Counter Users"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-42
  - TC-GS-ROLE-327
coverage:
  web: automated
---

# Pencabutan Role Assignment Tunggal Sukses dan Refleksi Penurunan Counter Users

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia user Budi Santoso ter-assign pada Detail role Manage master reference

## Test Steps

1. Buka Global Settings > Role & Permission > Tab System > Detail role 'Manage master reference'
2. Klik row action [⋯] pada baris Budi Santoso lalu pilih 'Remove'
3. Pada dialog konfirmasi, klik tombol [Remove]
4. Verifikasi toast sukses muncul: "Success, user has been removed."
5. Verifikasi baris Budi Santoso langsung hilang dari tabel Detail
6. Kembali ke Tab System dan periksa baris 'Manage master reference'
7. Verifikasi counter Users berkurang tepat 1

## Notes

- Pencabutan assignment role tunggal mengurangi counter Users pada Tab System secara instan (role.md §9.2 [F-ROLE-08]).
