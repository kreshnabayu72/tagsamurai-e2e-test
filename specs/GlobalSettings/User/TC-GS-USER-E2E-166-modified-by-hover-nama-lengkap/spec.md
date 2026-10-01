---
id: TC-GS-USER-E2E-166-modified-by-hover-nama-lengkap
title: Kolom Modified By tampil singkat dan hover menampilkan nama lengkap
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-626
coverage:
  web: automated
---

# Kolom Modified By tampil singkat dan hover menampilkan nama lengkap

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Baris "Quentin Edit" terakhir diubah oleh aktor "Siti Nurhaliza"
- Spec ini hanya membaca data

## Test Steps

1. Cari "Quentin Edit" di User List
2. Verifikasi sel Modified By menampilkan "Siti N"
3. Hover sel itu dan verifikasi tooltip menampilkan "Siti Nurhaliza"

## Notes

- Sumber `user.md` §4.1 dan §4.2a (kolom Modified By). Sort berdasar nama lengkap diuji di `TC-GS-USER-224`.
