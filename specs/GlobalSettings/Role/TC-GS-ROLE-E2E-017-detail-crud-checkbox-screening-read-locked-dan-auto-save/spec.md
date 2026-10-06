---
id: TC-GS-ROLE-E2E-017-detail-crud-checkbox-screening-read-locked-dan-auto-save
title: "Screening Checkbox CRUD Detail Role, Kunci Permanen Kolom Read, dan Auto-Save Per-Cell"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-32
  - TC-GS-ROLE-33
  - TC-GS-ROLE-326
  - TC-GS-ROLE-328
coverage:
  web: automated
---

# Screening Checkbox CRUD Detail Role, Kunci Permanen Kolom Read, dan Auto-Save Per-Cell

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia user target reguler Doni Pratama pada Detail role Manage user and role

## Test Steps

1. Buka Global Settings > Role & Permission > Tab System
2. Klik Detail pada role 'Manage user and role'
3. Amati baris user Doni Pratama pada kolom Read
4. Verifikasi checkbox kolom Read selalu checked (tercentang) dan disabled (terkunci permanen) serta tidak dapat diklik untuk di-uncheck
5. Klik checkbox kolom Create pada baris Doni Pratama untuk mengaktifkannya
6. Verifikasi toast sukses auto-save langsung muncul: "Success, permissions have been updated."
7. Klik checkbox kolom Delete pada baris Doni Pratama untuk mengaktifkannya
8. Verifikasi toast sukses auto-save langsung muncul: "Success, permissions have been updated."
9. Refresh halaman browser (F5) dan kembali ke baris Doni Pratama
10. Verifikasi kedua checkbox Create dan Delete tetap tersimpan dalam kondisi tercentang

## Notes

- Read adalah baseline minimum izin yang terkunci permanen (ROLE-LOGIC-05). Perubahan izin di auto-save per cell (role.md §3, §6.4).
