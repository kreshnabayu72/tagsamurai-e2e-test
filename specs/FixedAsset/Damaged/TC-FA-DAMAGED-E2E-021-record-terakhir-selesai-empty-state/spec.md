---
id: TC-FA-DAMAGED-E2E-021-record-terakhir-selesai-empty-state
title: "Menyelesaikan record berjalan terakhir mengosongkan sub-tab Active ke empty state No damaged assets"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EB-EDG-2, §7.1#r1, §Aturan Logika Modul#r58]
smoke: []
dependsOn: []
trace:
  EB-EDG-2: [1, 2, 8, 12]
  §7.1#r1: [8, 9, 10]
  §Aturan Logika Modul#r58: [7, 12]
anchor: []
coverage:
  web: automated
---

# Menyelesaikan record berjalan terakhir mengosongkan sub-tab Active ke empty state No damaged assets

## Prerequisites
- Aktor: Total Control (DU-021-2), pada entitas khusus yang tidak dipakai spec lain.
- Layar awal: halaman Assets, tab Damaged, sub-tab Active.
- Data:
  - DU-021-1: satu-satunya Damage record berjalan di entitas khusus, aset `Projector Epson EB-X06 {runId}` tanpa TAG di Group `Head Office {runId}`, status `Damaged`, Source `Manual`, dilaporkan DU-021-2.
  - DU-021-2: User `Agus Pratama {runId}`, role Total Control; cakupan: seluruh client pada entitas khusus.

## Test Steps

### Record terakhir adalah satu-satunya baris di sub-tab Active
1. Verifikasi baris aset `Projector Epson EB-X06 {runId}` tampil di tabel dengan status `Damaged`
2. Verifikasi tabel sub-tab Active memuat satu baris

### Mark as Repaired atas record terakhir mengosongkan sub-tab Active
3. Klik `⋯` pada baris `Projector Epson EB-X06 {runId}`
4. Klik `Mark as Repaired`
5. Isi Repair note `Lampu proyektor diganti dan unit sudah diuji menyala normal`
6. Klik `[Mark as Repaired]` pada dialog `Mark as Repaired`
7. Verifikasi toast `Success, [Asset Name] has been marked as repaired.` tampil dengan `[Asset Name]` berisi nama aset `Projector Epson EB-X06 {runId}`
8. Verifikasi sub-tab Active menampilkan `No damaged assets`
9. Verifikasi sub-tab Active menampilkan teks `Assets reported damaged will appear here until they're resolved.`
10. Verifikasi sub-tab Active tidak menampilkan `No results found`

### Record selesai tampil di History
11. Klik sub-tab `History`
12. Verifikasi baris aset `Projector Epson EB-X06 {runId}` tampil di tabel History dengan status `Repaired`
