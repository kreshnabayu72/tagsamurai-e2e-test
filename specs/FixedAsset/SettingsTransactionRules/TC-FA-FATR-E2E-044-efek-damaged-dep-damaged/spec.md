---
id: TC-FA-FATR-E2E-044-efek-damaged-dep-damaged
title: "After photo required berlaku di Damaged"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["EB-XM-2@damaged", "§11#r16"]
smoke: ["§11#r16"]
dependsOn:
  - "Damaged: Mark as Repaired"
trace:
  "EB-XM-2@damaged": 10
  "§11#r16": 10
anchor: [3]
coverage:
  web: automated
---

# After photo required berlaku di Damaged

## Prerequisites
- Aktor: Default User yang memegang Manage transaction settings (Update), di entitas khusus yang tidak dipakai spec lain.
- Layar awal: Fixed Asset > Damaged
- Data:
  - DU-044-1: Entitas Name `Entitas Damaged {runId}`, After photo required `OFF`; entitas khusus spec ini dengan After photo required bernilai OFF.
  - DU-044-2: Asset Name `Compressor CP90 {runId}`, Condition `Damaged`, Status `Available`; aset berkondisi Damaged di entitas khusus.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Damaged {runId}` yang tidak dipakai spec lain, karena yang diubah adalah setting tingkat entitas.
  - After photo required bernilai `OFF` di entitas khusus ini.

## Test Steps

### After photo required berubah dari OFF ke ON mengubah dialog Mark as Repaired
1. Masuk sebagai Default User
2. Buka dialog Mark as Repaired untuk aset `Compressor CP90 {runId}`
3. Verifikasi After photo tidak wajib di dialog Mark as Repaired karena After photo required bernilai `OFF`
4. Tutup dialog Mark as Repaired yang belum diisi
5. Buka tab yang memuat field After photo required pada node All categories di Fixed Asset > Settings > Transaction Settings
6. Pilih nilai `ON` pada field After photo required
7. Klik `[Save]`
8. Klik `[Save]` pada dialog Save Changes
9. Buka dialog Mark as Repaired untuk aset `Compressor CP90 {runId}`
10. Verifikasi After photo wajib di dialog Mark as Repaired sesuai nilai baru After photo required `ON`
