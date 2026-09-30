---
id: TC-GS-USER-E2E-124-toggle-active-gagal-server
title: 'Toggle Active gagal karena error server dan dialog tetap terbuka'
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-48
coverage:
  web: automated
---

# Toggle Active gagal karena error server dan dialog tetap terbuka

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Kebutuhan mock: respons `500` dipaksa pada permintaan Activate dan Deactivate
- User "Budi Santoso" berstatus Active dan "Irfan Nonaktif" berstatus Inactive

## Test Steps

### Deactivate

1. Klik toggle Active OFF pada "Budi Santoso" lalu klik konfirmasi di dialog saat server membalas `500`
2. Verifikasi toast "Error, failed to deactivate user." muncul
3. Verifikasi dialog tetap terbuka, toggle tidak pernah berubah secara visual, dan tombol konfirmasi kembali aktif dari state loading
4. Klik `[Cancel]`

### Activate

5. Klik toggle Active ON pada "Irfan Nonaktif" lalu klik konfirmasi di dialog saat server membalas `500`
6. Verifikasi toast "Error, failed to activate user." muncul dan dialog tetap terbuka dengan toggle tidak berubah
7. Klik `[Cancel]`

## Notes

- Sumber `user.md` bagian 7 dan 9.6 (Action Resilience: aksi ini pessimistic, UI baru berubah setelah server mengonfirmasi, jadi tidak ada state yang perlu dikembalikan).
- Toggle yang berhasil dicakup `TC-GS-USER-E2E-008-toggle-active-user`.
