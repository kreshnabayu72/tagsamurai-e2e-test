---
id: TC-GS-ROLE-E2E-010-assign-total-control-happy-path-shortcut-bulk-write
title: "Penugasan Total Control Sukses, Shortcut Bulk-Write 6 Role, dan Kenaikan Counter Users"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-16
  - TC-GS-ROLE-17
  - TC-GS-ROLE-82
  - TC-GS-ROLE-353
coverage:
  web: automated
---

# Penugasan Total Control Sukses, Shortcut Bulk-Write 6 Role, dan Kenaikan Counter Users

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia user target baru eligible (mis. userTargetTCBaru) tanpa role
- Tersedia user target Doni Pratama yang sudah memiliki 2 role parsial (Import data dan Manage TAG)

## Test Steps

1. Buka Global Settings > Role & Permission > Tab System
2. Catat angka counter pada kolom Users untuk keenam role sistem
3. Buka Tab Total Control dan klik tombol [+ Assign]
4. Cari userTargetTCBaru pada picker, centang checkbox barisnya, lalu klik [Assign]
5. Verifikasi toast sukses muncul: "Success, Total Control has been assigned."
6. Verifikasi userTargetTCBaru kini tampil di tabel Tab Total Control
7. Buka Tab System dan periksa halaman Detail untuk keenam role sistem
8. Verifikasi userTargetTCBaru memiliki centang CRUD penuh aktif di semua role
9. Verifikasi angka counter Users pada Tab System bertambah 1 untuk keenam role sekaligus
10. Buka kembali Tab Total Control, klik [+ Assign], pilih Doni Pratama, lalu klik [Assign]
11. Verifikasi toast "Success, Total Control has been assigned."
12. Buka Tab System > Changelog modal pada Tab System
13. Verifikasi supresi log: tidak ada entri per-role yang dibuat untuk aksi bulk-write penugasan Total Control ini di Changelog System

## Notes

- Assign Total Control adalah shortcut bulk-write 6 role yang mengecualikan pencatatan per-role pada Changelog System (role.md §8.3, §8.7).
