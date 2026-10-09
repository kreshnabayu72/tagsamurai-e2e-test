---
id: TC-GS-GSET-E2E-035-cross-module-timestamp-mengikuti-entitas-staff-yang-login
title: "Cross-Module: timestamp Admin Console mengikuti Time Zone entitas staff yang login, bukan entitas yang dilihat"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-122
coverage:
  web: automated
---

# Cross-Module: timestamp Admin Console mengikuti Time Zone entitas staff yang login, bukan entitas yang dilihat

## Prerequisites

- Staff Distributor `PT Maju Bersama` dengan Time Zone `Asia/Jakarta` (UTC+07:00)
- Client `PT Sentosa Abadi` memakai Time Zone Lain (UTC+08:00)

## Test Steps

1. Login sebagai Role Total Control (staff Distributor `PT Maju Bersama`), buka Admin Console > Client List
2. Amati kolom Last Updated pada baris `PT Sentosa Abadi`
3. Verifikasi timestamp `PT Sentosa Abadi` ditampilkan dalam Time Zone `PT Maju Bersama` (UTC+07:00)
4. Login sebagai staff `PT Sentosa Abadi` dan buka FAMS, amati timestamp
5. Verifikasi timestamp ditampilkan dalam Time Zone `PT Sentosa Abadi` (UTC+08:00)

## Notes

- TC-GS-GSET-122 (format timestamp mengikuti entitas staff yang login, bukan entitas yang dilihat). Butuh dua akun lintas entitas dengan Time Zone berbeda.
