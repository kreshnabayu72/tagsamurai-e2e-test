---
id: TC-FA-FATR-BE-129-plan-addon-audit-dep-audit
title: "Task Audit pada plan tanpa Approval Workflow"
layer: be-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.4.2#r70", "§9.2#b565", "§9.10.1#r9", "§9.2#b555"]
smoke: []
dependsOn:
  - "Audit: task Audit, Finish Audit, dan perekaman lokasi"
owner: BE
trace:
  "§9.4.2#r70": [3, 4]
  "§9.2#b565": [3, 4]
  "§9.10.1#r9": [3, 4]
  "§9.2#b555": [3, 4]
anchor: []
---

# Task Audit pada plan tanpa Approval Workflow

## Prerequisites
- Aktor: Admin `Bimo Santoso {runId}` (Total Control entitas khusus; membuat task Audit); Auditor `Wulan Anggraini {runId}` (ditugaskan pada task Audit di spec ini; menjalankan Finish Audit).
- Data:
  - DU-129-1: Entitas `Citra Plan Audit {runId}`, entitas khusus yang hanya dipakai spec ini dan tidak dipakai spec lain. Plan-nya tidak menyediakan Approval Workflow. Subscription FAMS-nya memiliki alokasi lisensi addon Audit, sehingga addon aktif.
  - DU-129-2: User `Bimo Santoso {runId}`, Role `Total Control entitas`; Admin yang membuat task Audit.
  - DU-129-3: User `Wulan Anggraini {runId}`, Role `Employee`; Auditor yang ditugaskan pada task Audit.
  - DU-129-4: Pengaturan Company default tab Audit: Require approval `ON`, tersimpan sejak plan entitas masih menyediakan Approval Workflow.
  - DU-129-5: Asset `Rak Besi Gudang {runId}`; aset task Audit pada plan tanpa Approval Workflow.
  - DU-129-6: Task Audit `Audit Rak Gudang {runId}`, aset `Rak Besi Gudang {runId}`, durasi `1` hari.
- Kondisi:
  - Akun Admin `Bimo Santoso {runId}` dan Auditor `Wulan Anggraini {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Approval Workflow tidak tersedia: Require approval Audit tersimpan ON berlaku sebagai OFF saat Finish Audit
1. Admin `Bimo Santoso {runId}` membuat task Audit `Audit Rak Gudang {runId}` untuk aset `Rak Besi Gudang {runId}` dengan durasi `1` hari
2. Auditor `Wulan Anggraini {runId}` menjalankan Finish Audit pada task `Audit Rak Gudang {runId}`
3. Verifikasi nilai efektif Require approval Audit saat Finish Audit adalah `OFF`, karena plan entitas tidak menyediakan Approval Workflow, walau nilai tersimpan `ON`
4. Verifikasi task `Audit Rak Gudang {runId}` langsung berstatus `Completed`
