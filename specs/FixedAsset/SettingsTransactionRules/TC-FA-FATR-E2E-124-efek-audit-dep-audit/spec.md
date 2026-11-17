---
id: TC-FA-FATR-E2E-124-efek-audit-dep-audit
title: "Require approval Audit berlaku pada Finish Audit"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-XM-2@audit", "§4.1#r198", "§11#r19"]
smoke: ["§4.1#r198", "§11#r19"]
dependsOn:
  - "Audit: task Audit, Finish Audit, dan perekaman lokasi"
trace:
  "EB-XM-2@audit": 3
  "§4.1#r198": 3
  "§11#r19": 3
anchor: []
coverage:
  android: automated
---

# Require approval Audit berlaku pada Finish Audit

## Prerequisites
- Aktor: Auditor yang ditugaskan pada task Audit DU-124-2, masuk di aplikasi Android.
- Layar awal: daftar task Audit di aplikasi Android.
- Data:
  - DU-124-1: Entitas `Citra Efek Audit {runId}`, entitas khusus yang hanya dipakai spec ini dan tidak dipakai spec lain. Plan-nya menyediakan Approval Workflow, dan addon Audit aktif pada subscription FAMS-nya.
  - DU-124-2: Task Audit `Audit Gudang Cikarang {runId}`, ada di entitas DU-124-1 dan siap di-Finish Audit.
- Kondisi:
  - Require approval Audit di Company default entitas DU-124-1 bernilai `ON`.

## Test Steps

### Require approval Audit ON membuat Finish Audit menunggu approval
1. Buka task Audit `Audit Gudang Cikarang {runId}`
2. Lakukan Finish Audit pada task `Audit Gudang Cikarang {runId}`
3. Verifikasi status task Audit `Audit Gudang Cikarang {runId}` adalah `Waiting for Approval`, bukan `Completed`
