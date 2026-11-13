---
id: TC-FA-FAREG-E2E-058-edit-draft-autosave
title: "Edit draft: autosave menyimpan perubahan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§9.5#r2, S-REG-12]
smoke: [S-REG-12]
dependsOn: []
trace:
  §9.5#r2: [7, 17]
  S-REG-12: [7, 8, 10]
anchor: []
coverage:
  web: automated
---

# Edit draft: autosave menyimpan perubahan

## Prerequisites
- Aktor: `Rina W` (Manage asset & TAG, Group terkelola `Gudang Autosave {runId}`).
- Layar awal: Fixed Asset > Assets > Registration > sub tab Draft.
- Data:
  - DU-058-1: Draft tersimpan milik `Rina W` untuk Group `Gudang Autosave {runId}`. Item 1 `Laptop`, `Dell`, `Latitude 5440` dengan Quantity `1`; aset 1 belum memiliki Alias Name.

## Test Steps

### Autosave berjalan 20 detik sesudah perubahan
1. Ketik Search `Gudang Autosave {runId}`, tekan Enter
2. Klik Group `Gudang Autosave {runId}` pada baris untuk membuka form Edit
3. Klik tab `Asset`
4. Klik row option `Detail` pada aset 1
5. Isi Alias Name `Laptop Autosave` pada panel samping aset
6. Waktu berlalu sampai 20 detik sejak perubahan
7. Verifikasi subjudul form menampilkan `Saving...`
8. Verifikasi subjudul form kemudian menampilkan `Saved`
9. Klik tab `General Information`
10. Verifikasi subjudul form pada tab `General Information` juga menampilkan `Saved`

### Perubahan hasil autosave tersimpan
11. Klik `[Cancel]` pada form (perubahan sudah disimpan autosave dan form belum diubah sesudahnya)
12. Muat ulang halaman
13. Ketik Search `Gudang Autosave {runId}`, tekan Enter
14. Klik Group `Gudang Autosave {runId}` pada baris untuk membuka form Edit
15. Klik tab `Asset`
16. Klik row option `Detail` pada aset 1
17. Verifikasi Alias Name aset 1 menampilkan `Laptop Autosave`
