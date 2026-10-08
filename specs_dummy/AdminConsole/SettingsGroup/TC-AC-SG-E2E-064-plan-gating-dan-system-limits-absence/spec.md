---
id: TC-AC-SG-E2E-064-plan-gating-dan-system-limits-absence
title: "Ketiadaan plan gating atau upsell pada seluruh alur fitur Settings > Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-145
coverage:
  web: automated
---

# Ketiadaan plan gating atau upsell pada seluruh alur fitur Settings > Group

## Prerequisites

- Login sebagai Role: Total Control pada entitas entitas apa pun (tanpa memandang plan tier konsumen)

## Test Steps

### Verifikasi Ketiadaan Plan Gating
1. Buka `Settings > Group`
2. Jalankan alur pembuatan group level 1 dan subgroup
3. Jalankan alur edit dan delete group
4. Verifikasi seluruh operasi berjalan bebas tanpa pemblokiran tier langganan (Starter/Pro/Enterprise) dan tanpa modal upsell FAMS/SAMS
5. Verifikasi Admin Console beroperasi sebagai tooling internal platform vendor tanpa restriksi paket lisensi

## Notes

- TC-AC-SG-146 (unlimited node count) dan TC-AC-SG-147 (depth ceiling) divalidasi di backend.
