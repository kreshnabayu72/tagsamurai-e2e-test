---
id: TC-GS-USER-E2E-163-navigasi-ke-user-detail
title: Klik nama user dan row action Detail membuka User Detail
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-623
coverage:
  web: automated
---

# Klik nama user dan row action Detail membuka User Detail

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Target "Putri Anggun" adalah User Basic biasa
- Spec ini hanya membaca data

## Test Steps

1. Klik link nama "Putri Anggun" di kolom Name
2. Verifikasi User Detail "Putri Anggun" terbuka
3. Kembali ke User List
4. Buka `[⋯]` pada baris yang sama lalu klik `Detail`
5. Verifikasi User Detail yang sama terbuka
6. Verifikasi row action `Detail` juga tersedia pada baris Default User dan akun sendiri

## Notes

- Sumber `user.md` §4.1 (Row Actions) dan §4.2a.
