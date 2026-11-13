---
id: TC-FA-FAREG-E2E-054-buat-draft-item-tanpa-asset-name
title: "Register Asset: draft dengan Item tanpa Asset Name"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-03d, FAREG-LOGIC-03t]
smoke: []
dependsOn: []
trace:
  FAREG-LOGIC-03d: 7
  FAREG-LOGIC-03t: [10, 11, 12]
anchor: [6]
coverage:
  web: automated
---

# Register Asset: draft dengan Item tanpa Asset Name

## Prerequisites
- Aktor: `Rina W` (Manage asset & TAG, Group terkelola `Gudang Tanpa Aset {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > sub tab Draft.
- Data:
  - DU-054-1: Group `Gudang Tanpa Aset {runId}`, node Assignable dan bukan Excess, belum memiliki batch Draft.

## Test Steps

### Item tanpa Asset Name belum membentuk aset
1. Klik `[+ Register Asset]`
2. Pilih Group `Gudang Tanpa Aset {runId}`
3. Isi Quantity Item 1 dengan `4`, tanpa memilih Asset Name
4. Klik `[Save draft]`
5. Klik tab `Asset`
6. Verifikasi subjudul form menampilkan `Saved`
7. Verifikasi tab Asset belum memuat aset untuk Item 1, sehingga belum ada Name sementara maupun data aset
8. Klik `[Cancel]` pada form (form belum diubah sejak Save draft)

### Draft tampil dengan Total Asset 0 dan Progress 0%
9. Ketik Search `Gudang Tanpa Aset {runId}`, tekan Enter
10. Verifikasi baris Group `Gudang Tanpa Aset {runId}` tampil di sub tab Draft
11. Verifikasi Total Asset batch `0`
12. Verifikasi Progress batch `0%`
