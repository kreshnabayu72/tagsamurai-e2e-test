---
id: TC-FA-FAREG-E2E-111-toggle-require-approval-dep-settings-role-permission
title: "Toggle Require Approval for Registration menentukan jalur Submit"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-06m, §9.5#r7]
smoke: []
dependsOn: ["Settings Role Permission: toggle Require Approval for Registration"]
trace:
  FAREG-LOGIC-06m: [4, 5, 7, 9, 14, 15, 17, 18, 22]
  §9.5#r7: [4, 14]
anchor: []
coverage:
  web: automated
---

# Toggle Require Approval for Registration menentukan jalur Submit

## Prerequisites
- Aktor:
  - Rina, role Manage asset & TAG dengan Group terkelola `Gudang Setuju OFF {runId}` dan `Gudang Setuju ON {runId}`.
  - Admin, role Total Control (seluruh client), hanya sebagai aktor lain yang mengubah toggle `Require Approval for Registration`.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-111-1: Group `Gudang Setuju OFF {runId}`, toggle `Require Approval for Registration` tidak pernah diubah (nilai bawaan OFF), ada di entitas aktor.
  - DU-111-2: Group `Gudang Setuju ON {runId}`, toggle `Require Approval for Registration` bernilai ON, ada di entitas aktor.
  - DU-111-3: Asset Name `Kursi Setuju {runId}` dengan TAG Type `Non-TAG`, Brand `Ergotec`, Model `No Model`.
  - DU-111-4: batch Draft `Gudang Setuju OFF {runId}` berisi 1 Item Asset Name `Kursi Setuju {runId}`, Brand `Ergotec`, Model `No Model`, Quantity `2`.
  - DU-111-5: batch Draft `Gudang Setuju ON {runId}` berisi 1 Item Asset Name `Kursi Setuju {runId}`, Brand `Ergotec`, Model `No Model`, Quantity `2`.
- Kondisi: sisa kuota Group dan tenant mencukupi untuk 2 aset pada masing-masing Group.

## Test Steps

### Group dengan nilai bawaan OFF langsung mengaktifkan aset
1. Ketik Search `Gudang Setuju OFF {runId}`, tekan Enter
2. Klik row action `Edit` pada baris batch `Gudang Setuju OFF {runId}`
3. Klik `[Submit]`
4. Verifikasi dialog memuat `Are you sure you want to activate it?`
5. Verifikasi tombol konfirmasi `[Activate]` tampil
6. Klik `[Activate]`
7. Verifikasi toast `Success, asset has been activated.`
8. Klik sub tab `History`
9. Verifikasi baris pengajuan `Gudang Setuju OFF {runId}` tampil di sub tab History

### Group dengan toggle ON mengajukan persetujuan
10. Klik sub tab `Draft`
11. Ketik Search `Gudang Setuju ON {runId}`, tekan Enter
12. Klik row action `Edit` pada baris batch `Gudang Setuju ON {runId}`
13. Klik `[Submit]`
14. Verifikasi dialog memuat `Are you sure you want to submit it for approval?`
15. Verifikasi tombol konfirmasi `[Submit for Approval]` tampil
16. Klik `[Submit for Approval]`
17. Verifikasi toast `Success, registration has been submitted.`
18. Verifikasi baris pengajuan `Gudang Setuju ON {runId}` tampil di sub tab Waiting for Approval

### Toggle dimatikan tidak mengubah pengajuan yang sudah menunggu
19. Admin mematikan toggle `Require Approval for Registration` pada node Group `Gudang Setuju ON {runId}`
20. Muat ulang halaman
21. Ketik Search `Gudang Setuju ON {runId}`, tekan Enter
22. Verifikasi baris pengajuan `Gudang Setuju ON {runId}` tetap tampil di sub tab Waiting for Approval
