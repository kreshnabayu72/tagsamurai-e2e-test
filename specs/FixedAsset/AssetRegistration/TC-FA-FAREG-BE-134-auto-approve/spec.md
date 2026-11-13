---
id: TC-FA-FAREG-BE-134-auto-approve
title: "Auto-approve: Kondisi A dan Kondisi B"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-06l]
smoke: []
dependsOn: []
owner: BE
trace:
  FAREG-LOGIC-06l: [2, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 17, 18, 19, 20, 22, 23]
---

# Auto-approve: Kondisi A dan Kondisi B

## Prerequisites
- Aktor:
  - Hana T (Total Control, seluruh client).
  - Agus P (Group Manager Group `Gudang Pusat {runId}`).
  - Dewi S (Group Manager Group `Cabang Induk {runId}`, menaungi sub-group `Gudang Anak {runId}`).
  - Rina W (Manage asset & TAG dengan capability Update pada node Group `Gudang Selatan {runId}` dan `Gudang Timur {runId}`).
  - Budi (Manage asset & TAG dengan capability Update pada node Group `Gudang Timur {runId}`).
- Data:
  - DU-134-1: Group `Gudang Pusat {runId}`, Group Manager `Agus P`, ber-toggle `Require Approval for Registration` ON.
  - DU-134-2: Group `Cabang Induk {runId}`, Group Manager `Dewi S`, ber-toggle `Require Approval for Registration` ON.
  - DU-134-3: Group `Gudang Anak {runId}`, sub-group dari `Cabang Induk {runId}` tanpa Group Manager sendiri, ber-toggle `Require Approval for Registration` ON.
  - DU-134-4: Group `Gudang Selatan {runId}`, ber-toggle `Require Approval for Registration` ON.
  - DU-134-5: Group `Gudang Timur {runId}`, ber-toggle `Require Approval for Registration` ON.
  - DU-134-6: Asset Name `Router {runId}`, Brand `Mikrotik`, Model `RB-134`, TAG Type `Non-TAG`, Status `Active`.
  - DU-134-7: batch Draft milik Hana T di Group `Gudang Pusat {runId}`, Item Asset Name `Router {runId}`, Quantity `2`, Condition `Normal`.
  - DU-134-8: batch Draft milik Agus P di Group `Gudang Pusat {runId}`, Item Asset Name `Router {runId}`, Quantity `3`, Condition `Normal`.
  - DU-134-9: batch Draft milik Dewi S di Group `Gudang Anak {runId}`, Item Asset Name `Router {runId}`, Quantity `2`, Condition `Normal`.
  - DU-134-10: batch Draft milik Rina W di Group `Gudang Selatan {runId}`, Item Asset Name `Router {runId}`, Quantity `4`, Condition `Normal`.
  - DU-134-11: batch Draft milik Rina W di Group `Gudang Timur {runId}`, Item Asset Name `Router {runId}`, Quantity `2`, Condition `Normal`.
- Kondisi:
  - seluruh batch memenuhi Tingkat 2 dan kuota Group cukup untuk jumlah aset masing-masing.
  - himpunan approver eligible pada node Group `Gudang Selatan {runId}` berisi Rina W dan Hana T (Total Control).
  - himpunan approver eligible pada node Group `Gudang Timur {runId}` berisi Rina W, Budi, dan Hana T (Total Control).

## Test Steps

### Kondisi A: pengaju Total Control
1. Hana T mengirim Submit for Approval atas batch Draft Group `Gudang Pusat {runId}` berisi `2` aset
2. Verifikasi pengajuan langsung berstatus `Approved`
3. Verifikasi pengajuan itu tidak masuk antrean Approvals
4. Verifikasi kedua aset berstatus `Active` dan slot kuota Group berstatus Used tanpa pernah Reserved
5. Verifikasi Registration Log pengajuan memuat node `Approved by Hana T (Total Control — requester)`

### Kondisi A: pengaju Group Manager Group aset
6. Agus P mengirim Submit for Approval atas batch Draft Group `Gudang Pusat {runId}` berisi `3` aset
7. Verifikasi pengajuan langsung berstatus `Approved`
8. Verifikasi pengajuan itu tidak masuk antrean Approvals
9. Verifikasi ketiga aset berstatus `Active` dan slot kuota Group berstatus Used tanpa pernah Reserved
10. Verifikasi Registration Log pengajuan memuat node `Approved by Agus P (Group Manager — requester)`

### Kondisi A: pengaju Group Manager ancestor Group aset
11. Dewi S mengirim Submit for Approval atas batch Draft Group `Gudang Anak {runId}` berisi `2` aset
12. Verifikasi pengajuan langsung berstatus `Approved`
13. Verifikasi pengajuan itu tidak masuk antrean Approvals
14. Verifikasi kedua aset berstatus `Active` dan slot kuota Group berstatus Used tanpa pernah Reserved
15. Verifikasi Registration Log pengajuan memuat node `Approved by Dewi S (Group Manager — requester)`

### Kondisi B tidak terpenuhi bila Total Control yang eligible adalah approver independen
16. Rina W mengirim Submit for Approval atas batch Draft Group `Gudang Selatan {runId}` berisi `4` aset
17. Verifikasi pengajuan berstatus `Waiting for Approval`
18. Verifikasi pengajuan itu masuk antrean Approvals milik Hana T karena Total Control yang eligible dihitung sebagai approver independen
19. Verifikasi entri Rina W pada Level 1 berstatus `Not Involved` dan Level 1 tetap aktif untuk Hana T
20. Verifikasi Registration Log pengajuan tidak memuat node `Approved by system (no independent approver)`

### Kondisi B tidak terpenuhi bila ada approver independen lain
21. Rina W mengirim Submit for Approval atas batch Draft Group `Gudang Timur {runId}` berisi `2` aset
22. Verifikasi pengajuan berstatus `Waiting for Approval` dan masuk antrean Approvals milik Budi
23. Verifikasi entri Rina W pada Level 1 berstatus `Not Involved` dan Level 1 tetap aktif untuk Budi
