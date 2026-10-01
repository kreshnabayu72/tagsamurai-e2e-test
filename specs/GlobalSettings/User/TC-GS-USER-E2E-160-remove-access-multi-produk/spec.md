---
id: TC-GS-USER-E2E-160-remove-access-multi-produk
title: Remove Access beberapa produk sekaligus memakai satu dialog gabungan dan satu entri Changelog per produk
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-619
  - TC-GS-USER-620
coverage:
  web: automated
---

# Remove Access beberapa produk sekaligus memakai satu dialog gabungan dan satu entri Changelog per produk

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Target "Kirana Dewi" punya Access `[Global Settings, Fixed Asset, SIEM]`
- Fixed Asset dan SIEM masing-masing punya aset atau approval terkait milik target
- Spec ini mengubah Access target, jadi target di-seed ulang setelah run

## Test Steps

1. Buka Modal Edit "Kirana Dewi"
2. Hilangkan centang `Fixed Asset` dan `SIEM`
3. Klik `[Save]`
4. Verifikasi hanya satu dialog warn muncul, memuat bullet nama user, satu baris dampak untuk Fixed Asset dan satu baris untuk SIEM, ditutup "Are you sure you want to remove them?"
5. Konfirmasi dialog
6. Verifikasi toast "Success, user has been updated." dan Access target menjadi `[Global Settings]`
7. Buka Tab Changelog dan verifikasi ada dua baris terpisah dengan Action "Remove Access" pada Field "App Access", satu untuk Fixed Asset dan satu untuk SIEM, tanpa baris Action "Edit"

## Notes

- Satu produk diuji di `TC-GS-USER-E2E-009`. Sumber `user.md` §9.2 [F-USER-03] dan §8.2.
