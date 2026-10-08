---
id: TC-AC-ACAL-E2E-042-absennya-plan-gating-lintas-tier
title: "Plan Gating — Ketiadaan plan gating dan fungsionalitas identik lintas seluruh tier langganan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-242
coverage:
  web: automated
---

# Plan Gating — Ketiadaan plan gating dan fungsionalitas identik lintas seluruh tier langganan

## Prerequisites

- Akun Principal pada entitas dengan tier Starter
- Akun Principal pada entitas dengan tier Pro
- Akun Principal pada entitas dengan tier Enterprise

## Test Steps

1. Login sebagai Principal pada akun tier Starter
2. Buka menu `Admin Console > Activity Log`
3. Verifikasi seluruh kontrol (Tab Session, Tab User Action, Search, Filter, Setup Column, Download CSV/XLSX) tersedia lengkap tanpa banner upgrade atau kunci plan gating
4. Logout dan login sebagai Principal pada akun tier Pro
5. Verifikasi seluruh fitur Activity Log tersedia identik
6. Logout dan login sebagai Principal pada akun tier Enterprise
7. Verifikasi seluruh fitur Activity Log tersedia identik tanpa batasan

## Notes

- Modul Activity Log di Admin Console tersedia penuh sebagai fitur core compliance tanpa segmentasi tier langganan (no plan gating).
