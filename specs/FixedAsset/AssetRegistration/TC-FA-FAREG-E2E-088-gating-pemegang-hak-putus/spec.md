---
id: TC-FA-FAREG-E2E-088-gating-pemegang-hak-putus
title: "Gating Manage asset & TAG dengan capability Update pada node Group registrasi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FAREG-LOGIC-06p", "§2.1#r3", "§4.8#r10", "§4.8#r11", "§4.8#r18", "§9.2#p75", "§9.2#p77", "§9.2#p79", "§9.2#p80", "EB-AKS-5@keputusan-approval"]
smoke: []
dependsOn: []
trace:
  "FAREG-LOGIC-06p": [1, 6]
  "§2.1#r3": 1
  "§4.8#r10": 1
  "§4.8#r11": [5, 8, 10, 11, 14]
  "§4.8#r18": 5
  "§9.2#p75": 1
  "§9.2#p77": 1
  "§9.2#p79": 4
  "§9.2#p80": [4, 6]
  "EB-AKS-5@keputusan-approval": [18, 19]
coverage:
  web: automated
---

# Gating Manage asset & TAG dengan capability Update pada node Group registrasi

## Prerequisites
- Aktor: Budi S (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang 1 {runId}`, tanpa capability lain pada node itu).
- Layar awal: Fixed Asset > Assets.
- Data:
  - DU-088-1: Pengajuan Waiting for Approval `REG-20261109-08802` di Group `Gudang 1 {runId}`, diajukan Rina W, Total Asset `2`, Last Updated `T0 − 1 hari` (Item `Proyektor` Brand `Epson` Model `EB-X49` Quantity `2`, TAG `Verified`).
  - DU-088-2: Pengajuan Waiting for Approval `REG-20261108-08803` di Group `Kantor Pusat {runId}`, diajukan Hadi K, Total Asset `3`, Last Updated `T0 − 2 hari` (Item `Laptop` Brand `Dell` Model `Latitude 5440` Quantity `3`, TAG `Verified`).
  - DU-088-3: Budi S (Manage asset & TAG dengan capability Update pada node Group `Gudang 1 {runId}`).
  - DU-088-4: Rina W (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`).
  - DU-088-5: Hadi K (Manage asset & TAG, Group terkelola `Kantor Pusat {runId}`).
- Kondisi:
  - Group `Gudang 1 {runId}` dan Group `Kantor Pusat {runId}` ber-toggle `Require Approval for Registration` ON.
  - Kuota lisensi tenant dan Group `Gudang 1 {runId}` cukup untuk 2 aset.

## Test Steps

### Menu Approvals > Registration tampil bagi pemegang capability Update
1. Verifikasi menu `Approvals` > `Registration` tampil pada sidebar bagi Budi S

### Antrean Active hanya memuat pengajuan dalam cakupan Group hak putus
2. Klik menu `Approvals` > `Registration`
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi baris Group `Gudang 1 {runId}` dengan Total Asset `2` dan Requested By `Rina W` tampil di tab `Active`
5. Verifikasi row action `Review` tampil pada baris Group `Gudang 1 {runId}` dengan Total Asset `2`
6. Verifikasi tidak ada baris Group `Kantor Pusat {runId}` di tab `Active`

### Pemegang capability Update memutuskan pengajuan sampai berhasil
7. Klik row action `Review` pada baris Group `Gudang 1 {runId}` dengan Total Asset `2`
8. Verifikasi kolom Decision tampil dengan nilai `Approve` pada aset ke-1 grup `Proyektor`
9. Centang aset ke-1 pada grup `Proyektor`
10. Verifikasi Bulk Action dengan pilihan `Approve`, `Return to Draft`, dan `Reject` tampil
11. Verifikasi tombol `[Submit]` tampil pada footer halaman Approval
12. Buka row option pada aset ke-1 grup `Proyektor`
13. Klik `Edit`
14. Verifikasi panel koreksi tampil
15. Klik `Close` pada panel koreksi yang belum diubah
16. Klik `[Submit]` pada footer halaman Approval
17. Klik `[Submit]` pada dialog `Submit Approval`
18. Verifikasi toast `Success, registration request has been decided.` tampil setelah Budi S memutuskan hanya dengan capability Update
19. Verifikasi baris Group `Gudang 1 {runId}` dengan Total Asset `2` tidak tampil lagi di tab `Active`
