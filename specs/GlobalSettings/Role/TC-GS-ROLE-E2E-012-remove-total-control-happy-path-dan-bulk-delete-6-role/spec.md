---
id: TC-GS-ROLE-E2E-012-remove-total-control-happy-path-dan-bulk-delete-6-role
title: "Pencabutan Total Control Sukses, Reset Akses Menjadi Null, Bulk-Delete 6 Role, dan Penurunan Counter"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-22
  - TC-GS-ROLE-25
  - TC-GS-ROLE-28
  - TC-GS-ROLE-83
coverage:
  web: automated
---

# Pencabutan Total Control Sukses, Reset Akses Menjadi Null, Bulk-Delete 6 Role, dan Penurunan Counter

## Prerequisites

- Login sebagai Role: Total Control (Default User)
- Tersedia target Siti Rahmawati ter-assign Total Control

## Test Steps

1. Buka Global Settings > Role & Permission > Tab System dan catat angka counter Users keenam role
2. Buka Tab Total Control
3. Klik row action [⋯] pada baris Siti Rahmawati lalu pilih 'Remove'
4. Pada dialog konfirmasi, klik tombol [Remove]
5. Verifikasi toast sukses muncul: "Success, Total Control has been removed."
6. Verifikasi Siti Rahmawati langsung hilang dari tabel Tab Total Control
7. Buka Tab System dan periksa halaman Detail role sistem
8. Verifikasi Siti Rahmawati tidak lagi memiliki baris assignment role (seluruh 6 role terhapus)
9. Verifikasi angka counter Users pada Tab System berkurang 1 untuk keenam role sekaligus
10. Buka Changelog modal Tab System
11. Verifikasi tidak ada entri log penghapusan per-role di Changelog System (bulk-delete disupres)

## Notes

- Pencabutan Total Control mereset access_level menjadi null dan menghapus 6 baris role sekaligus (role.md §9.2 [F-ROLE-05]).
