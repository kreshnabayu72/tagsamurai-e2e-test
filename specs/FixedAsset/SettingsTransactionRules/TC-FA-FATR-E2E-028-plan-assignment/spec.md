---
id: TC-FA-FATR-E2E-028-plan-assignment
title: "Level Feature Suite Assignment None"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [§9.4.2#r16, §9.4.4#r2, §Aturan Logika Modul#r106, §9.10.3#r6]
smoke: [§Aturan Logika Modul#r106, §9.10.3#r6]
dependsOn: []
trace:
  §9.4.2#r16: [4, 6]
  §9.4.4#r2: [4, 6]
  §Aturan Logika Modul#r106: 6
  §9.10.3#r6: [4, 6]
anchor: [3]
coverage:
  web: automated
---

# Level Feature Suite Assignment None

## Prerequisites
- Aktor: Total Control. Operator Admin Console memicu perubahan level plan entitas.
- Layar awal: Fixed Asset > Settings > Transaction Settings.
- Data:
  - DU-028-1: Entitas `Entitas Plan Assignment {runId}`, entitas khusus yang tidak dipakai spec lain, level Feature Suite Assignment `Full`.

## Test Steps

### Level None: tab Assign tidak tampil
1. Operator mengubah level Feature Suite Assignment entitas menjadi `None`
2. Muat ulang halaman
3. Verifikasi `Export rules` pada header halaman tampil
4. Verifikasi tab `Assign` tidak tampil pada daftar tab
5. Buka langsung URL Transaction Settings dengan tab `Assign`
6. Verifikasi tab `Assign` tetap tidak tampil dan tidak menjadi tab aktif
