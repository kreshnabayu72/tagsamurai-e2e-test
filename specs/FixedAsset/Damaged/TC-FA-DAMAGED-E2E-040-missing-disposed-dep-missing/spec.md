---
id: TC-FA-DAMAGED-E2E-040-missing-disposed-dep-missing
title: "Aset Missing yang di-Dispose menyelesaikan Damage record sebagai Disposed di History dengan node Disposed oleh System"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r76", "§8.1#r16", "§8.3#r3", EC-DMG-34, "§9.4.4#r33", "§9.7#r16"]
smoke: []
dependsOn: ["Missing: Missing → Disposed"]
trace:
  "§Aturan Logika Modul#r76": [8, 9]
  "§8.1#r16": [11, 12]
  "§8.3#r3": 11
  EC-DMG-34: [5, 8, 9, 11]
  "§9.4.4#r33": [9, 11]
  "§9.7#r16": [5, 8, 9]
anchor: []
coverage:
  web: automated
---

# Aset Missing yang di-Dispose menyelesaikan Damage record sebagai Disposed di History dengan node Disposed oleh System

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Missing.
- Data:
  - DU-040-1: Damage record `Camera Canon EOS {runId}`, Group `Head Office`, Status `Damaged`, Source `Manual`, berpenanda `Missing`.
- Kondisi:
  - Aset `Camera Canon EOS {runId}` berstatus Missing.

## Test Steps

### Missing → Disposed menyelesaikan Damage record sebagai Disposed
1. Ketik Search `Camera Canon EOS {runId}`, tekan Enter
2. Dispose aset Missing `Camera Canon EOS {runId}` lewat Missing → Disposed
3. Buka tab Damaged, sub-tab Active
4. Ketik Search `Camera Canon EOS {runId}`, tekan Enter
5. Verifikasi hasil Search sub-tab Active menampilkan `No results found`
6. Buka sub-tab History
7. Ketik Search `Camera Canon EOS {runId}`, tekan Enter
8. Verifikasi baris `Camera Canon EOS {runId}` tampil di sub-tab History

### Node Disposed oleh System di Damage Log
9. Verifikasi baris `Camera Canon EOS {runId}` berstatus `Disposed`
10. Klik nama aset `Camera Canon EOS {runId}` di kolom Name
11. Verifikasi dialog Damage Log memuat node `Disposed` dengan pelaku `System`
12. Verifikasi baris detail node `Disposed` memuat `Disposal No.`
13. Tutup dialog Damage Log
