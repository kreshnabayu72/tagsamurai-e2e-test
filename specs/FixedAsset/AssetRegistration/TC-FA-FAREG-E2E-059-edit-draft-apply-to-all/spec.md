---
id: TC-FA-FAREG-E2E-059-edit-draft-apply-to-all
title: "Edit draft: Apply to all menerapkan nilai ke semua aset Item"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-01r, §9.7#r19, T-REG-16, FI-REG-13]
smoke: [T-REG-16, FI-REG-13]
dependsOn: []
trace:
  FAREG-LOGIC-01r: [8, 9, 15]
  §9.7#r19: [11, 16]
  T-REG-16: 6
  FI-REG-13: [11, 12, 16]
anchor: []
coverage:
  web: automated
---

# Edit draft: Apply to all menerapkan nilai ke semua aset Item

## Prerequisites
- Aktor: `Rina W` (Manage asset & TAG, Group terkelola `Gudang Terapkan {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > sub tab Draft.
- Data:
  - DU-059-1: Draft tersimpan milik `Rina W` untuk Group `Gudang Terapkan {runId}`. Item 1 `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `3`. Aset 1: Alias Name `Laptop Kepala Cabang`, Photo `2`. Aset 2: Alias Name `Laptop Magang`, Photo `1`. Aset 3: tanpa Alias Name dan tanpa Photo.

## Test Steps

### Apply to all Alias Name menggantikan nilai semua aset Item
1. Ketik Search `Gudang Terapkan {runId}`, tekan Enter
2. Klik Group `Gudang Terapkan {runId}` pada baris untuk membuka form Edit
3. Klik tab `Asset`
4. Klik row option `Detail` pada aset 1
5. Klik `Apply to all` pada bagian Alias Name di panel samping aset
6. Verifikasi toast `Success, the value has been applied to all assets in the item.` tampil
7. Klik row option `Detail` pada aset 2
8. Verifikasi Alias Name aset 2 menampilkan `Laptop Kepala Cabang`
9. Verifikasi nilai `Laptop Magang` tidak lagi tampil pada Alias Name aset 2, karena nilai sumber menggantikan dan tidak digabung
10. Klik row option `Detail` pada aset 3
11. Verifikasi Alias Name aset 3 menampilkan `Laptop Kepala Cabang`
12. Verifikasi kolom Photo aset 3 tetap `—`, karena `Apply to all` hanya menerapkan data Alias Name

### Apply to all Photo menggantikan foto semua aset Item
13. Klik row option `Detail` pada aset 1
14. Klik `Apply to all` pada bagian Photo di panel samping aset
15. Verifikasi kolom Photo aset 2 menampilkan `2`, bukan `3`, karena foto sumber menggantikan foto semula
16. Verifikasi kolom Photo aset 3 menampilkan `2`
