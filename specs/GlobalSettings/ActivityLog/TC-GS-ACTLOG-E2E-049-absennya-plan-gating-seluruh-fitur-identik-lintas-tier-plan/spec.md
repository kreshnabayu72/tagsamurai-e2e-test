---
id: TC-GS-ACTLOG-E2E-049-absennya-plan-gating-seluruh-fitur-identik-lintas-tier-plan
title: "8d-1 Seluruh fitur dan perilaku Activity Log berlaku identik di seluruh tier lisensi plan"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-239
coverage:
  web: automated
---

# 8d-1 Seluruh fitur dan perilaku Activity Log berlaku identik di seluruh tier lisensi plan

## Prerequisites

- Akun Total Control pada tenant dengan tier Starter, Growth, Professional, Enterprise, dan Custom

## Test Steps

1. Login sebagai Total Control pada tenant bertier Starter
2. Buka Activity Log, verifikasi kedua tab, seluruh table tools, export, dan filter dapat diakses tanpa batasan
3. Login sebagai Total Control pada tenant bertier Enterprise
4. Buka Activity Log, verifikasi perilaku dan tampilan UI identik tanpa batasan retention tiering
5. Verifikasi tidak ada batasan kuota retensi atau banner upsell lisensi di tier mana pun

## Notes

- Batas retensi bertingkat telah dihapus total sejak 2026-08-17 sehingga semua plan mendapat kapabilitas identik.
