---
id: TC-GS-ROLE-E2E-020-detail-assign-role-happy-path-dan-guard-duplikasi
title: "Penugasan Role ke User Sukses, Baseline Read Otomatis, dan Pengecualian User Ter-assign"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-37
  - TC-GS-ROLE-38
  - TC-GS-ROLE-39
  - TC-GS-ROLE-40
  - TC-GS-ROLE-333
coverage:
  web: automated
---

# Penugasan Role ke User Sukses, Baseline Read Otomatis, dan Pengecualian User Ter-assign

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia user target Budi Santoso yang belum memiliki role Manage master reference

## Test Steps

1. Buka Global Settings > Role & Permission > Tab System
2. Catat angka counter Users pada baris role 'Manage master reference'
3. Buka Detail role 'Manage master reference'
4. Klik tombol [+ Assign]
5. Cari Budi Santoso pada popup picker, centang checkbox barisnya, lalu klik tombol [Assign]
6. Verifikasi toast sukses muncul: "Success, role has been assigned."
7. Verifikasi Budi Santoso kini tampil pada tabel Detail dengan kolom Read otomatis terkunci tercentang dan kolom lainnya tidak tercentang
8. Klik kembali tombol [+ Assign] pada toolbar Detail
9. Cari Budi Santoso pada tabel picker dan verifikasi Budi Santoso tidak muncul lagi (dieksklusi karena sudah ter-assign)
10. Tutup popup picker
11. Kembali ke Tab System dan periksa baris 'Manage master reference'
12. Verifikasi counter Users bertambah tepat 1

## Notes

- User yang sudah memiliki assignment pada suatu role otomatis dieksklusi dari daftar picker role tersebut (F-ROLE-03).
