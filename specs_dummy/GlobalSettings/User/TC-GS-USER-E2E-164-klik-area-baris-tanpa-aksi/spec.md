---
id: TC-GS-USER-E2E-164-klik-area-baris-tanpa-aksi
title: Klik area baris di luar link dan kontrol tidak melakukan apa pun
priority: Low
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-624
coverage:
  web: automated
---

# Klik area baris di luar link dan kontrol tidak melakukan apa pun

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User List terisi
- Spec ini hanya membaca data

## Test Steps

1. Klik area sel Division pada sebuah baris
2. Klik area sel Last Update pada baris yang sama
3. Verifikasi URL tidak berubah, tidak ada dialog, dan tidak ada checkbox yang berubah

## Notes

- Sumber `user.md` §5 ("Akses data existing: hanya dari row action").
