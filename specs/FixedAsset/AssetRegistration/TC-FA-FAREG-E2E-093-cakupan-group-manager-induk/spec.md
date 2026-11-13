---
id: TC-FA-FAREG-E2E-093-cakupan-group-manager-induk
title: "Cakupan Group: Group Manager induk mengubah lalu menghapus draft sub-group"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["FAREG-LOGIC-02e", "§9.2#p57", "§9.2#p59", "§9.2#p61", "§9.2#p62", "T-REG-04"]
smoke: ["T-REG-04"]
dependsOn: []
trace:
  "FAREG-LOGIC-02e": [3, 10, 14]
  "§9.2#p57": 3
  "§9.2#p59": [5, 8, 13]
  "§9.2#p61": 5
  "§9.2#p62": [5, 8, 10, 13, 14]
  "T-REG-04": 13
coverage:
  web: automated
---

# Cakupan Group: Group Manager induk mengubah lalu menghapus draft sub-group

## Prerequisites
- Aktor: Dewi A (Group Manager Group `Cabang A {runId}`, Group binaan beserta sub-group).
- Layar awal: Fixed Asset > Assets.
- Data:
  - DU-093-1: Batch Draft dengan Group `Gudang 1 {runId}`, Origin `—`, Total Asset `12`, Progress `0%`, Requested By `Rina W`, Last Updated `T0 − 1 hari`, Item `Office Desk` Brand `Kayu Jati` Model `No Model` Quantity `12`.
  - DU-093-2: Quantity Item `Office Desk` sesudah diubah Dewi A menjadi `10`, sehingga Total Asset batch `10`.
  - DU-093-3: Dewi A (Group Manager, Group binaan `Cabang A {runId}` beserta sub-group).
  - DU-093-4: Rina W (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`), pembuat batch DU-093-1.
- Kondisi:
  - Group `Gudang 1 {runId}` adalah sub-group dari Group `Cabang A {runId}`.

## Test Steps

### Group Manager induk mengubah batch Draft sub-group
1. Klik tab `Registration`
2. Ketik Search `Gudang 1 {runId}`, tekan Enter
3. Verifikasi baris Group `Gudang 1 {runId}` dengan Requested By `Rina W` dan Total Asset `12` tampil di sub tab `Draft` bagi Dewi A
4. Klik row action `Edit` pada baris `Gudang 1 {runId}`
5. Verifikasi form `Register Asset` terbuka dalam mode Edit untuk batch `Gudang 1 {runId}` bagi Dewi A
6. Ubah Quantity Item `Office Desk` menjadi `10`
7. Klik `[Save draft]`
8. Verifikasi toast `Success, draft has been saved.` tampil bagi Dewi A
9. Klik `[Cancel]` pada footer form; perubahan sudah disimpan sehingga tanpa dialog Unsaved Changes
10. Verifikasi baris Group `Gudang 1 {runId}` dengan Total Asset `10` tampil di sub tab `Draft`

### Group Manager induk menghapus batch Draft sub-group
11. Klik row action `Delete` pada baris `Gudang 1 {runId}`
12. Klik `[Delete]` pada dialog `Delete Draft`
13. Verifikasi toast `Success, draft has been deleted.` tampil bagi Dewi A
14. Verifikasi baris Group `Gudang 1 {runId}` tidak tampil di sub tab `Draft`
