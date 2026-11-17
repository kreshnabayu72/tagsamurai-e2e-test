---
id: TC-FA-FATR-E2E-004-deny
title: "Allow bernilai Deny menyembunyikan bagian lain tanpa menghapus nilainya"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r28", "§9.2#b17", "§9.4.2#r108", "§9.4.2#r109", "§9.4.2#r111", "§9.4.3#b3", "§9.4.2#r110"]
smoke: ["§9.4.2#r110"]
dependsOn: []
trace:
  "§Aturan Logika Modul#r28": [17, 18, 19]
  "§9.2#b17": [17, 18, 19]
  "§9.4.2#r108": 6
  "§9.4.2#r109": [17, 18, 19]
  "§9.4.2#r111": [7, 8, 9]
  "§9.4.3#b3": [17, 18, 19]
  "§9.4.2#r110": 15
anchor: [3, 5]
coverage:
  web: automated
---

# Allow bernilai Deny menyembunyikan bagian lain tanpa menghapus nilainya

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-004-1: Category leaf `Skid Steer {runId}`, tanpa sub-Category, ada di entitas aktor. Di tab Borrow: Allow Borrow bernilai sendiri `Allow`, Max duration bernilai sendiri `30`, Max extensions bernilai sendiri `4`, Approval type bernilai sendiri `All approvers (AND)`. Field lain Inherit.
- Kondisi:
  - Plan entitas aktor menyediakan Approval Workflow dan tab Borrow.

## Test Steps

### Deny pada Category menyembunyikan bagian selain Eligibility
1. Ketik Search Sidebar Category Tree `Skid Steer {runId}`, tekan Enter
2. Klik Category leaf `Skid Steer {runId}`
3. Verifikasi field `Max duration` bernilai `30`
4. Pilih `Deny` pada field `Allow Borrow`
5. Verifikasi field `Allow Borrow` bernilai `Deny` pada bagian Eligibility
6. Verifikasi bagian `Limits`, `Evidence`, `Approval`, `Reminders`, dan `Notifications` tidak tampil
7. Verifikasi bagian `Overrides` tampil dengan tombol `[+ Override]` aktif
8. Verifikasi tombol `[Reset to Default]` aktif
9. Verifikasi tombol `[Save]` aktif
10. Klik `[Save]`
11. Klik `[Save]` pada dialog Save Changes

### Nilai bagian yang disembunyikan tetap tersimpan sesudah muat ulang
12. Muat ulang halaman
13. Ketik Search Sidebar Category Tree `Skid Steer {runId}`, tekan Enter
14. Klik Category leaf `Skid Steer {runId}`
15. Verifikasi field `Allow Borrow` bernilai `Deny`
16. Pilih `Allow` pada field `Allow Borrow`
17. Verifikasi field `Max duration` bernilai `30`
18. Verifikasi field `Max extensions` bernilai `4`
19. Verifikasi field `Approval type` bernilai `All approvers (AND)`
