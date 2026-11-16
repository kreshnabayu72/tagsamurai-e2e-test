---
id: TC-FA-FATR-E2E-053-efek-activity-log-dep-activity-log
title: "Perubahan Settings dan override tercatat di Activity Log"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["§8.2#r2", "§9.4.2#r49", "§8.2#p1", "§9.2#b372", "§9.7#r10"]
smoke: ["§8.2#p1", "§9.2#b372", "§9.7#r10"]
dependsOn:
  - "Activity Log: daftar entri"
trace:
  "§8.2#r2": [17, 18, 19, 20, 21]
  "§9.4.2#r49": 21
  "§8.2#p1": [17, 18, 19, 20, 21]
  "§9.2#b372": 21
  "§9.7#r10": 17
anchor: []
coverage:
  web: automated
---

# Perubahan Settings dan override tercatat di Activity Log

## Prerequisites
- Aktor: `Dian Pratiwi {runId}` sebagai Default User yang memegang Manage transaction settings (Update).
- Layar awal: Fixed Asset > Settings > Transaction Settings
- Data:
  - DU-053-1: Category Name `Plant Lighting {runId}`, Max duration `14 Days`, Max extensions `2`; Category leaf dengan Max duration Borrow nilai sendiri.
  - DU-053-2: Group Name `Plant Lighting Team {runId}`; Group target override.
  - DU-053-3: User Name `Dian Pratiwi {runId}`, Role `Default User`; Default User pengubah setting yang namanya tampil di Activity Log.
- Kondisi:
  - Akun `Dian Pratiwi {runId}` aktif dan kredensialnya tersedia untuk login.

## Test Steps

### Save Changes, Add override, Delete override, dan Export rules tercatat di Activity Log
1. Masuk sebagai `Dian Pratiwi {runId}`
2. Buka tab `Borrow` pada node Category `Plant Lighting {runId}` di Fixed Asset > Settings > Transaction Settings
3. Isi Max duration dengan `7`
4. Klik `[Reset to inherit]` pada field Max extensions
5. Klik `[Save]`
6. Klik `[Save]` pada dialog Save Changes
7. Klik `[+ Override]` pada bagian Overrides
8. Isi Scope `Group` dengan Target `Plant Lighting Team {runId}`
9. Pilih Field `Max duration` dengan Value `10`
10. Klik `[Submit]`
11. Buka menu ⋯ pada baris override untuk `Plant Lighting Team {runId}`
12. Klik `Delete`
13. Klik `[Delete]` pada dialog Delete Override
14. Klik `[Export rules]` pada header halaman
15. Buka daftar Activity Log
16. Ketik Search `Plant Lighting {runId}`, tekan Enter
17. Verifikasi satu entri berformat `[Name] changed [Field] of [Transaction] for [Category] from [Old] to [New]` tampil di Activity Log dengan [Name] `Dian Pratiwi {runId}`, [Field] `Max duration`, [Transaction] `Borrow`, [Category] `Plant Lighting {runId}`, [Old] `14`, dan [New] `7 days`
18. Verifikasi satu entri berformat `[Name] changed [Field] of [Transaction] for [Category] from [Old] to [New]` tampil di Activity Log dengan [Name] `Dian Pratiwi {runId}`, [Field] `Max extensions`, [Transaction] `Borrow`, [Category] `Plant Lighting {runId}`, [Old] `2`, dan [New] `Inherit`
19. Verifikasi satu entri berformat `[Name] added an override on [Transaction] for [Target] in [Category]: [field] ([value])` tampil di Activity Log dengan [Name] `Dian Pratiwi {runId}`, [Transaction] `Borrow`, [Target] `Plant Lighting Team {runId}`, [Category] `Plant Lighting {runId}`, [field] `Max duration`, dan [value] `10`
20. Verifikasi satu entri berformat `[Name] deleted an override on [Transaction] for [Target] in [Category]` tampil di Activity Log dengan [Name] `Dian Pratiwi {runId}`, [Transaction] `Borrow`, [Target] `Plant Lighting Team {runId}`, dan [Category] `Plant Lighting {runId}`
21. Verifikasi satu entri berformat `[Name] exported transaction rules for [Category]` tampil di Activity Log dengan [Name] `Dian Pratiwi {runId}` dan [Category] `Plant Lighting {runId}`
