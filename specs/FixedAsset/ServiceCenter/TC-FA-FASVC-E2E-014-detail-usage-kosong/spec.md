---
id: TC-FA-FASVC-E2E-014-detail-usage-kosong
title: "Tab Usage Tanpa Pemakaian: Not used yet"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["S-FASVC-04"]
smoke: []
dependsOn: []
trace:
  "S-FASVC-04": [2, 5]
anchor: []
coverage:
  web: automated
---

# Tab Usage Tanpa Pemakaian: Not used yet

## Prerequisites
- Aktor: Total Control.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-014-1: Service Center `Usage Nol {runId}`, Status `Active`, Service type `Routine`, Available to `All groups`, Country `Malaysia`, City `Batu Pahat {runId}`, Company phone `+60 7555090909`, Usage `0`.

## Test Steps

### Tab Usage Service Center yang belum dipakai
1. Ketik Search `Usage Nol {runId}`, tekan Enter
2. Verifikasi baris `Usage Nol {runId}` tampil dengan kolom Usage `0`
3. Klik Name `Usage Nol {runId}`
4. Klik tab `Usage`
5. Verifikasi tab Usage menampilkan `Not used yet.`
