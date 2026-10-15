---
id: TC-GS-GSET-E2E-010-role-matrix-total-control-dan-read-only
title: "Role Matrix: akses penuh Total Control dan field Disabled/hidden pada Read Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-22
  - TC-GS-GSET-23
coverage:
  web: automated
---

# Role Matrix: akses penuh Total Control dan field Disabled/hidden pada Read Only

## Prerequisites

- Akun Role Total Control dan akun Role Read Only pada entitas yang sama
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`

## Test Steps

### Total Control — Akses Penuh

1. Login sebagai Role Total Control, lalu amati sidebar Global Settings
2. Verifikasi menu General Settings tampil (Show) di sidebar
3. Buka General Settings dan amati field form, Button "Save", icon Changelog, dan ikon info label
4. Verifikasi kelima Select (Currency Code, Date Format, Time Format, Time Zone, Session Idle Timeout) tampil dan enabled
5. Verifikasi Button "Save" tampil (disabled sampai ada perubahan)
6. Verifikasi icon Changelog tampil dan ikon info label tampil

### Read Only — Disabled, Tooltip, dan Save Hidden

7. Ganti login sebagai Role Read Only, lalu amati sidebar Global Settings
8. Verifikasi menu General Settings tetap tampil (Show) di sidebar
9. Buka General Settings dan verifikasi kelima Select tetap tampil (visible) namun disabled dengan nilai tersimpan terbaca penuh
10. Hover tiap Select satu per satu (Currency Code, Date Format, Time Format, Time Zone, Session Idle Timeout)
11. Verifikasi tiap Select disabled menampilkan tooltip "You don't have permission to edit"
12. Verifikasi Button "Save" Hidden (tidak dirender)
13. Klik icon Changelog, verifikasi modal terbuka dan tabel riwayat terbaca
14. Hover ikon info label Currency Code, verifikasi tooltip tetap tampil

## Notes

- Menggabungkan TC-GS-GSET-22 (Total Control akses penuh) dan TC-GS-GSET-23 (Read Only field disabled, tooltip, Save hidden, Changelog tetap tampil).
