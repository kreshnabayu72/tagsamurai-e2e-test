---
id: TC-GS-USER-E2E-167-pindah-tab-state-tidak-reset
title: Pindah antar tab User, Position, Division, dan Custom Field tidak mereset state User List
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-627
coverage:
  web: automated
---

# Pindah antar tab User, Position, Division, dan Custom Field tidak mereset state User List

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Spec ini hanya membaca data

## Test Steps

1. Di tab User List, isi Search "Budi", pilih Filter Division, dan urutkan Name Z-A
2. Pindah ke tab Position
3. Pindah ke tab Division lalu tab Custom Field
4. Kembali ke tab User List
5. Verifikasi Search, Filter Division, dan urutan Name Z-A masih sama
6. Verifikasi breadcrumb tetap `Global Settings > User` di keempat tab

## Notes

- Sumber `user.md` §4.1 ("Pindah tab tidak reset state tab lain").
