---
id: TC-GS-ROLE-E2E-014-assign-read-only-happy-path-screening-dan-filter-kelayakan
title: "Screening Table User Picker Assign Read Only, Filter Kelayakan, dan Penugasan Sukses Bulk-Write"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-29
  - TC-GS-ROLE-30
  - TC-GS-ROLE-329
coverage:
  web: automated
---

# Screening Table User Picker Assign Read Only, Filter Kelayakan, dan Penugasan Sukses Bulk-Write

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia user eligible baru (userTargetROBaru)
- Tersedia user yang sedang Total Control (totalControl2)

## Test Steps

1. Buka Global Settings > Role & Permission > Tab Read Only
2. Klik tombol [+ Assign] pada toolbar
3. Verifikasi popup Table User Picker terbuka
4. Cari totalControl2 pada picker dan verifikasi user Total Control tidak muncul (harus di-remove dari TC terlebih dahulu)
5. Cari userTargetROBaru pada picker, centang checkbox barisnya, lalu klik tombol [Assign]
6. Verifikasi toast sukses muncul: "Success, Read Only has been assigned."
7. Verifikasi userTargetROBaru muncul pada tabel Tab Read Only
8. Buka Tab System dan periksa halaman Detail pada role sistem
9. Verifikasi userTargetROBaru memiliki baris aktif dengan kolom Read tercentang dan kolom C/U/D tidak tercentang
10. Buka Changelog modal Tab System dan verifikasi 0 entri log per-role untuk aksi penugasan Read Only ini

## Notes

- Assign Read Only mengaktifkan keenam role dengan hak akses Read-only (C/U/D unchecked) (role.md §9.2 [F-ROLE-04]).
