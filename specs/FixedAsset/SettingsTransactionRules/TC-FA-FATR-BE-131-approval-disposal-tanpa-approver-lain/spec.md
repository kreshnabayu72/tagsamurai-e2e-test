---
id: TC-FA-FATR-BE-131-approval-disposal-tanpa-approver-lain
title: "Approval Disposal ketika pengaju satu-satunya orang yang dapat menyetujui"
layer: be-e2e
priority: High
caseType: Positive
status: draft
owner: BE
sourceRules: ["F-FATR-11.p4a", "F-FATR-11.p5d", "EC-40", "EC-63", "DISP-LOGIC-06"]
smoke: []
dependsOn:
  - "Disposal: pengajuan, approval, dan Execute"
trace:
  "F-FATR-11.p4a": [7, 10]
  "F-FATR-11.p5d": [9, 10]
  "EC-40": [3, 4, 5, 6, 9, 14, 15]
  "EC-63": [7, 10]
  "DISP-LOGIC-06": [3, 4, 5, 6, 9, 14, 15]
anchor: []
---

# Approval Disposal ketika pengaju satu-satunya orang yang dapat menyetujui

## Prerequisites
- Aktor: Pengaju Disposal `Wahyu Prakoso {runId}` (Total Control, satu-satunya Total Control entitas) dan Group Manager `Lestari Kusuma {runId}`.
- Data:
  - DU-131-1: Entitas, entitas khusus spec ini, tidak dipakai spec lain: Name `Entitas Approver Tunggal {runId}`; hanya ada satu Total Control; tidak ada Role Transaksi `Approver` Disposal yang ditugaskan.
  - DU-131-2: User, Total Control: Name `Wahyu Prakoso {runId}`; Access Level `Total Control`; Cakupan `seluruh Group`; Status `Aktif`.
  - DU-131-3: Group, Group asal aset tanpa Group Manager: Name `Gudang Tunggal {runId}`.
  - DU-131-4: Group, Group asal aset dengan satu Group Manager: Name `Gudang Manajer {runId}`.
  - DU-131-5: User, Group Manager: Name `Lestari Kusuma {runId}`; Role `Group Manager tanpa penugasan Approver`; Cakupan `Gudang Manajer {runId}`; Status `Aktif`; memiliki hak mengajukan Disposal.
  - DU-131-6: Category: Name `Mesin Tunggal {runId}`; Require approval `ON`; Approval type `Any one approver`; Allowed disposal types `Scrap`.
  - DU-131-7: Asset, tanpa Group Manager: Name `Mesin Tunggal M1 {runId}`; Category `Mesin Tunggal {runId}`; Group `Gudang Tunggal {runId}`; Tag `Ber-tag`; Condition `Active`.
  - DU-131-8: Asset, tanpa Group Manager: Name `Mesin Tunggal M2 {runId}`; Category `Mesin Tunggal {runId}`; Group `Gudang Tunggal {runId}`; Tag `Ber-tag`; Condition `Active`.
  - DU-131-9: Asset, Group dengan satu Group Manager: Name `Mesin Manajer M3 {runId}`; Category `Mesin Tunggal {runId}`; Group `Gudang Manajer {runId}`; Tag `Ber-tag`; Condition `Active`.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Approver Tunggal {runId}` (DU-131-1) karena skenario mensyaratkan tidak ada approver lain sama sekali, termasuk Total Control lain.
  - Require approval Disposal bernilai `ON` pada Category uji dan Approval Workflow tersedia di plan entitas.
  - Aturan Disposal: Kondisi A tidak berlaku, tidak ada auto-approve oleh pengaju, dan approval dialihkan dengan urutan Approver eligible, Group Manager yang menaungi Group aset, lalu Total Control, selalu bukan pengaju (`disposal.md` `DISP-LOGIC-06`).
  - Status `draft` karena spec ini belum pernah dijalankan dan fixture entitas khusus belum disediakan fase 2.

## Test Steps

### Tidak ada approver lain sama sekali: baris lanjut tanpa approval dan ditandai
1. Catat bahwa `Wahyu Prakoso {runId}` adalah satu-satunya Total Control dan tidak ada Approver eligible maupun Group Manager yang menaungi `Gudang Tunggal {runId}`
2. `Wahyu Prakoso {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Tunggal M1 {runId}` dengan scan tag aset
3. Verifikasi Disposal berstatus `Waiting for Execution`, karena tidak ada approver lain sama sekali selain pengaju
4. Verifikasi log transaksi mencatat node `Approved by system (no independent approver)` dengan Modified By `System`
5. Verifikasi baris Disposal memuat penanda `No independent approver`
6. Verifikasi `Wahyu Prakoso {runId}` tidak tercatat sebagai approver transaksinya sendiri
7. Verifikasi log transaksi tidak memuat `Approved by Wahyu Prakoso {runId} (Total Control — requester)`, karena Kondisi A tidak berlaku untuk Disposal

### Group Manager sebagai pengaju: approval dialihkan ke Total Control, bukan auto-approve
8. `Lestari Kusuma {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Manajer M3 {runId}` dengan scan tag aset
9. Verifikasi Disposal berstatus `Waiting for Approval` dan log transaksi mencatat node `Approval rerouted` dengan Reason `Requester is the only approver` ke `Wahyu Prakoso {runId}`, karena tidak ada Approver eligible dan satu-satunya Group Manager yang menaungi adalah pengaju
10. Verifikasi log transaksi tidak memuat `Approved by Lestari Kusuma {runId} (Group Manager — requester)`
11. `Wahyu Prakoso {runId}` menyetujui Disposal atas `Mesin Manajer M3 {runId}`
12. Verifikasi Disposal berstatus `Waiting for Execution` sesudah persetujuan `Wahyu Prakoso {runId}`

### Pengaju Total Control tanpa approver lain tidak dapat menyetujui sendiri
13. `Wahyu Prakoso {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Tunggal M2 {runId}` dengan scan tag aset
14. Verifikasi Disposal berstatus `Waiting for Execution` dengan penanda `No independent approver`, bukan `Waiting for Approval`
15. Verifikasi daftar approver baris itu kosong dan tidak memuat `Wahyu Prakoso {runId}`
