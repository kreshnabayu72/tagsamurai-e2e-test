---
id: TC-GS-USER-E2E-149-pair-tag-gagal-server
title: Pair TAG di User Detail gagal karena server
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-608
coverage:
  web: automated
---

# Pair TAG di User Detail gagal karena server

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client, plan Growth atau lebih tinggi (Scan TAG tampil)
- Target "Dita Pratiwi" adalah User Basic biasa tanpa TAG terpasang (badge "Unverified")
- Simulasi scan RFID disediakan tim FE
- Respons server pada permintaan Pair dipaksa gagal 5xx

## Test Steps

1. Buka User Detail "Dita Pratiwi"
2. Klik `Scan TAG`, lalu scan TAG yang valid
3. Verifikasi toast "Error, failed to pair TAG." muncul
4. Verifikasi badge tetap "Unverified" dengan teks "No TAG paired" dan tombol `Scan TAG` masih tersedia
5. Buka Tab Changelog dan verifikasi tidak ada entri "Pair TAG" baru

## Notes

- Pasangan kegagalan dari `TC-GS-USER-E2E-031`. Toast Pair TAG di Detail bersifat instan (`user.md` §7, §9.2 [F-USER-08]).
- Mode mock dipakai karena kegagalan server tidak bisa dipicu dengan data nyata.
