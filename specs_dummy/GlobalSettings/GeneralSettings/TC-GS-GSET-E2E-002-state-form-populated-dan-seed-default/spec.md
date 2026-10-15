---
id: TC-GS-GSET-E2E-002-state-form-populated-dan-seed-default
title: "State form: nilai record tersimpan, seed default entitas baru, dan default Time Zone lintas negara"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-02
  - TC-GS-GSET-11
  - TC-GS-GSET-12
coverage:
  web: automated
---

# State form: nilai record tersimpan, seed default entitas baru, dan default Time Zone lintas negara

## Prerequisites

- Login sebagai Role: Total Control
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
- Entitas `Client Baru` (negara Indonesia) dibuat dari Admin Console tanpa Save General Settings
- Entitas `Client Negara Lain` (negara bukan Indonesia) dibuat tanpa Save General Settings

## Test Steps

### Record Tersimpan (Populated)

1. Buka Global Settings > General Settings
2. Verifikasi form terisi nilai tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
3. Verifikasi tombol "Save" disabled (state Unchanged)

### Entitas Baru (Seed Default)

4. Login sebagai staff entitas `Client Baru` lalu buka Global Settings > General Settings
5. Verifikasi form terisi seed default: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
6. Verifikasi tombol "Save" disabled
7. Klik icon Changelog dan verifikasi tidak ada baris di Modal Changelog (record lahir bersama entitas, tanpa entri log)

### Default Time Zone untuk Negara Bukan Indonesia

8. Login sebagai staff entitas `Client Negara Lain` lalu buka Global Settings > General Settings
9. Verifikasi field Time Zone terpilih `Asia/Jakarta` tanpa pemetaan negara

## Notes

- Menggabungkan TC-GS-GSET-02, TC-GS-GSET-11, dan TC-GS-GSET-12 (state form populated dan seed default). Ganti akun eksplisit dipakai antar entitas.
