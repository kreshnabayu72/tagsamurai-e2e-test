---
id: TC-FA-FACO-E2E-070-create-dari-shortcut-dep-asset-class
title: "Create Account dari shortcut `+ Create account` pada Select akun Asset Class"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FACO-LOGIC-12a, FACO-LOGIC-12b, FACO-LOGIC-12c, FACO-LOGIC-12d, FACO-LOGIC-12e, "§9.5#r6"]
smoke: []
dependsOn: ["Asset Class: Select akun dengan shortcut `+ Create account`"]
trace:
  FACO-LOGIC-12a: 3
  FACO-LOGIC-12b: [4, 5]
  FACO-LOGIC-12c: 6
  FACO-LOGIC-12d: [10, 11]
  FACO-LOGIC-12e: 12
  "§9.5#r6": 4
anchor: []
coverage:
  web: automated
---

# Create Account dari shortcut `+ Create account` pada Select akun Asset Class

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Asset Class, dengan form Asset Class `Shortcut Class {runId}` terbuka.
- Data:
  - DU-070-1: Asset Class `Shortcut Class {runId}`, belum memakai akun yang dibuat spec ini pada field Asset Cost.
  - Akun yang dibuat spec ini: Account Code `SCT-{runId}`, Account Name `Peralatan Kantor {runId}`, Account Function `Asset Cost` (DU-070-2), nilai Account Function ditentukan field Asset Cost pada form Asset Class.

## Test Steps

### Create Account dari shortcut pada Select akun Asset Class
1. Buka Select akun Asset Cost pada form Asset Class
2. Klik `+ Create account`
3. Verifikasi modal `Add Account` tampil
4. Verifikasi Account Function pada modal terisi `Asset Cost`, sesuai field asal
5. Verifikasi Account Function pada modal Disabled
6. Verifikasi checkbox `Stay on this form after submitting` tidak tampil pada modal
7. Isi Account Code `SCT-{runId}`
8. Isi Account Name `Peralatan Kantor {runId}`
9. Klik `[Submit]`
10. Verifikasi modal `Add Account` tertutup
11. Verifikasi field Asset Cost pada form Asset Class langsung memilih akun `SCT-{runId}`
12. Verifikasi layar tetap pada form Asset Class `Shortcut Class {runId}`, tidak berpindah ke tab Chart of Accounts
