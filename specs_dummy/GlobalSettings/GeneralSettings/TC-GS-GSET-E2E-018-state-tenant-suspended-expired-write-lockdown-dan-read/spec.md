---
id: TC-GS-GSET-E2E-018-state-tenant-suspended-expired-write-lockdown-dan-read
title: "State Tenant: Save ditolak saat entitas Suspended/Expired namun pembacaan tetap berjalan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-54
  - TC-GS-GSET-55
  - TC-GS-GSET-56
coverage:
  web: automated
---

# State Tenant: Save ditolak saat entitas Suspended/Expired namun pembacaan tetap berjalan

## Prerequisites

- Entitas `Client Suspended` (berstatus suspended) dan `Client Expired` (berstatus expired)
- Akun Role Total Control pada masing-masing entitas
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`

## Test Steps

### Save Ditolak saat Suspended

1. Login sebagai staff `Client Suspended`, buka Global Settings > General Settings
2. Pilih Session Idle Timeout `1 hour` lalu klik `[Save]`
3. Verifikasi Save ditolak server (403) dengan toast "Changes can't be saved while this workspace is suspended or expired."
4. Verifikasi form tetap unsaved dengan Session Idle Timeout `1 hour`; field dan Button "Save" tidak diberi perlakuan UI khusus
5. Refresh halaman (F5) dan verifikasi pembacaan tetap berjalan: Session Idle Timeout `30 minutes` (tidak tersimpan)

### Save Ditolak saat Expired

6. Login sebagai staff `Client Expired`, buka Global Settings > General Settings
7. Pilih Time Format `hh:mm a` lalu klik `[Save]`
8. Verifikasi Save ditolak server (403) dengan toast "Changes can't be saved while this workspace is suspended or expired."
9. Verifikasi form tetap unsaved dengan Time Format `hh:mm a`
10. Refresh halaman (F5) dan verifikasi Time Format `HH:mm` (tidak tersimpan)

### Halaman Tetap Dapat Dibaca saat Suspended

11. Login sebagai staff `Client Suspended`, buka Global Settings > General Settings
12. Verifikasi form terisi nilai tersimpan; tidak ada error dan tidak ada banner/perlakuan UI khusus

## Notes

- Menggabungkan TC-GS-GSET-54 (suspended), 55 (expired), dan 56 (pembacaan tetap berjalan). Langkah 5 dan 10 mengasersi nilai tersimpan di server.
