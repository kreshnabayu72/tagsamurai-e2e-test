---
id: TC-GS-POS-E2E-043-sinkronisasi-position-dropdown-user
title: Sinkronisasi Position ke Dropdown Form User
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-47
  - TC-GS-POS-98
  - TC-GS-POS-197
coverage:
  web: automated
---

# Sinkronisasi Position ke Dropdown Form User

## Prerequisites

- Aktor `Fixture.globalSettingsPosition.actors.totalControl`.
- Tersedia modul/form User (Create/Edit User) yang memiliki dropdown Position.
- Position master bisa berubah (create/edit/delete) dan harus tersinkron ke dropdown User.

## Test Steps

### A. Create Position muncul di dropdown User

1. Buka form Create/Edit User (atau modal assign Position di User).
2. Catat opsi dropdown Position saat ini.
3. Kembali ke `Global Settings > User > Position`, buat Position baru `P-Test-Sync`.
4. Kembali ke form User, buka dropdown Position.
5. Verifikasi `P-Test-Sync` muncul di daftar opsi dropdown Position (sinkron tanpa reload halaman penuh jika real-time).

### B. Edit nama Position ter-update di dropdown User

6. Edit nama `P-Test-Sync` menjadi `P-Test-Sync-Edited` di tab Position.
7. Buka kembali dropdown Position di form User.
8. Verifikasi opsi lama tidak ada, opsi baru `P-Test-Sync-Edited` muncul dengan label ter-update.

### C. Delete Position hilang dari dropdown User (dan tidak meninggalkan opsi stale)

9. Hapus `P-Test-Sync-Edited` dari tab Position.
10. Buka dropdown Position di form User.
11. Verifikasi opsi tersebut tidak lagi muncul di dropdown User.
12. Verifikasi tidak ada opsi stale/invalid yang tertinggal.

## Notes

- Sinkronisasi wajib ke dropdown form User (master data Position bersifat shared). Opsi dropdown harus selalu mencerminkan master data terkini.
