---
id: TC-GS-GSET-E2E-036-parity-tanpa-plan-gating-di-semua-paket
title: "Parity: General Settings tersedia dan identik di semua plan (Starter, Growth, Professional, Enterprise) tanpa gating"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-123
coverage:
  web: automated
---

# Parity: General Settings tersedia dan identik di semua plan (Starter, Growth, Professional, Enterprise) tanpa gating

## Prerequisites

- Akun Total Control pada entitas `Client Starter`, `Client Growth`, `Client Professional`, dan `Client Enterprise`
- Record General Settings tiap entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`

## Test Steps

1. Pada entitas `Client Starter`: buka General Settings, verifikasi kelima field tersedia, lalu pilih Session Idle Timeout `1 hour` dan klik `[Save]`
2. Verifikasi Save berhasil dengan toast "Success, general settings has been saved."
3. Pada entitas `Client Growth`: ulangi langkah 1 dan 2
4. Pada entitas `Client Professional`: ulangi langkah 1 dan 2
5. Pada entitas `Client Enterprise`: ulangi langkah 1 dan 2
6. Verifikasi tidak ada upsell atau limit berbeda pada keempat plan

## Notes

- TC-GS-GSET-123 (parity lintas plan tanpa plan gating).
