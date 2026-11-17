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
  §9.4.2#r16: [4, 6, 7, 9]
  §9.4.4#r2: [4, 6, 7]
  §Aturan Logika Modul#r106: 9
  §9.10.3#r6: [4, 9]
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

### Level None: tab Assign tidak dapat dibuka
1. Operator mengubah level Feature Suite Assignment entitas menjadi `None`
2. Muat ulang halaman
3. Verifikasi `Export rules` pada header halaman tampil
4. Verifikasi tab `Assign` disabled
5. Arahkan pointer ke tab `Assign`
6. Verifikasi alasan `Not available on your current plan.` tersampaikan pada tab `Assign` yang disabled
7. Verifikasi chip `Upgrade` pada tab `Assign`
8. Klik tab `Assign`
9. Verifikasi tab `Assign` tidak menjadi tab aktif
