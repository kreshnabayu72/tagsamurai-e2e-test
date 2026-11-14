---
id: TC-FA-DAMAGED-E2E-054-stock-opname-dep-stock-opname
title: "Pemilik sesi Stock Opname melaporkan kondisi rusak: record langsung Damaged Source Stock opname dan Damage Log dapat dibuka pelapornya"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#b1", "§2.1#b2", "§2#b6", "§4.8#r3", "§Aturan Logika Modul#r42", "§Aturan Logika Modul#r45", "§8.3#r2", "§3#p2", "§9.4.2#r19", "§9.11#r1", "T-DMG-01"]
smoke: []
dependsOn:
  - "Stock Opname: dialog Report Condition"
trace:
  "§2.1#b1": [10]
  "§2.1#b2": [10, 14, 20, 21]
  "§2#b6": [10, 12]
  "§4.8#r3": [10]
  "§Aturan Logika Modul#r42": [10]
  "§Aturan Logika Modul#r45": [16]
  "§8.3#r2": [11, 15]
  "§3#p2": [7, 10, 15]
  "§9.4.2#r19": [14, 15]
  "§9.11#r1": [14, 15]
  "T-DMG-01": [10, 11, 12, 19, 20, 21]
anchor: []
coverage:
  web: automated
---

# Pemilik sesi Stock Opname melaporkan kondisi rusak: record langsung Damaged Source Stock opname dan Damage Log dapat dibuka pelapornya

## Prerequisites
- Aktor: Pemilik sesi Stock Opname `Stock Opname Gudang Pusat {runId}`, tanpa hak Update Manage asset & TAG pada Group aset, yang juga memegang role Read Only.
- Layar awal: halaman sesi Stock Opname.
- Data:
  - DU-054-1: sesi Stock Opname Name `Stock Opname Gudang Pusat {runId}` untuk Group `Head Office`, berisi aset Name `Rak Besi Heavy Duty {runId}`, Group `Head Office`, tanpa TAG, belum punya record Damage.

## Test Steps

### Report Condition rusak dari sesi Stock Opname membuat record langsung Damaged
1. Buka sesi Stock Opname `Stock Opname Gudang Pusat {runId}`
2. Klik `Report Condition` pada aset `Rak Besi Heavy Duty {runId}`
3. Pilih Condition `Damaged` pada dialog Report Condition
4. Isi catatan kerusakan `Kaki rak bengkok dan tidak stabil saat diberi beban` pada dialog Report Condition
5. Pilih foto kerusakan `rak-kaki-bengkok.jpg` pada dialog Report Condition
6. Klik tombol simpan pada dialog Report Condition
7. Verifikasi dialog `Report Damaged` tidak tampil

### Record langsung Damaged di tab Damaged dan Damage Log dapat dibuka pelapornya
8. Buka halaman Assets, tab `Damaged`
9. Ketik Search `{runId}`, tekan Enter
10. Verifikasi baris aset `Rak Besi Heavy Duty {runId}` tampil di sub-tab `Active` dengan Status `Damaged`, tanpa Confirm
11. Verifikasi kolom Source pada baris itu `Stock opname`
12. Verifikasi kolom Reported By pada baris itu memuat nama pemilik sesi, dalam bentuk nama depan dan inisial nama belakang
13. Klik nama aset pada baris aset `Rak Besi Heavy Duty {runId}`
14. Verifikasi dialog `Damage Log` tampil
15. Verifikasi node `Reported damaged by [Reporter Name]` tampil atas nama pemilik sesi Stock Opname
16. Verifikasi node itu memuat catatan kerusakan `Kaki rak bengkok dan tidak stabil saat diberi beban` dan foto kerusakan `rak-kaki-bengkok.jpg` dari dialog Report Condition
17. Tutup dialog Damage Log

### Pemilik sesi tanpa hak Update hanya dapat membuka Damage Log
18. Klik `⋯` pada baris aset `Rak Besi Heavy Duty {runId}`
19. Verifikasi aksi `Damage Log` tampil pada menu baris
20. Verifikasi aksi `Mark as Repaired` tidak tampil pada menu baris
21. Verifikasi aksi `Report Missing` tidak tampil pada menu baris
