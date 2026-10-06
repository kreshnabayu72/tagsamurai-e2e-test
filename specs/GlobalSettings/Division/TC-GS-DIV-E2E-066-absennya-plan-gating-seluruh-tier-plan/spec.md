---
id: TC-GS-DIV-E2E-066-absennya-plan-gating-seluruh-tier-plan
title: "Absennya Plan Gating: Seluruh Fitur Division Berlaku Identik di Semua Tier Lisensi"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-203
coverage:
  web: automated
---

# Absennya Plan Gating: Seluruh Fitur Division Berlaku Identik di Semua Tier Lisensi

## Prerequisites

- Tersedia tenant dengan tier lisensi Starter, Business, dan Enterprise

## Test Steps

1. Login pada tenant dengan paket lisensi tier Starter
2. Buka tab Division dan verifikasi seluruh fitur (Create, Edit, Delete, Bulk Delete, Code, Changelog, Download, Setup Column) tersedia penuh tanpa batasan fitur
3. Login pada tenant tier Business dan Enterprise
4. Verifikasi fungsionalitas dan kapabilitas modul Division beroperasi identik di seluruh tier tanpa pembatasan buatan

## Notes

- Division bersifat unlimited di semua plan lisensi tanpa plan gating (division.md §9.10).
