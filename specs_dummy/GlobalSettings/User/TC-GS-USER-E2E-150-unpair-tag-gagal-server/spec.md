---
id: TC-GS-USER-E2E-150-unpair-tag-gagal-server
title: Unpair TAG di User Detail gagal karena server
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-609
coverage:
  web: automated
---

# Unpair TAG di User Detail gagal karena server

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Target "Edwin Saputra" punya TAG terpasang (badge "Verified")
- Respons server pada permintaan Unpair dipaksa gagal 5xx

## Test Steps

1. Buka User Detail "Edwin Saputra"
2. Klik `Unpair`
3. Pada dialog "Unpair TAG from this user?", klik `[Unpair]`
4. Verifikasi toast "Error, failed to unpair TAG." muncul
5. Verifikasi badge tetap "Verified" dan TAG ID masih tampil
6. Buka Tab Changelog dan verifikasi tidak ada entri "Unpair TAG" baru

## Notes

- Pasangan kegagalan dari `TC-GS-USER-E2E-031`.
- Mode mock dipakai karena kegagalan server tidak bisa dipicu dengan data nyata.
