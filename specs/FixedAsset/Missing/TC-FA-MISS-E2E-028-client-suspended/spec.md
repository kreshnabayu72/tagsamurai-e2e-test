---
id: TC-FA-MISS-E2E-028-client-suspended
title: "Client Suspended: aksi tulis Missing ditolak dengan toast suspended, data tetap terbaca"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["EB-AKS-7", "§9.2#b21", "§9.4.1#r1", "§9.4.2#r30", "§9.4.4#r8"]
smoke: []
dependsOn: []
trace:
  "EB-AKS-7": [10, 11]
  "§9.2#b21": [3, 5, 10]
  "§9.4.1#r1": [3, 5, 10]
  "§9.4.2#r30": [3, 5, 10, 13]
  "§9.4.4#r8": [3, 10, 13]
anchor: []
coverage:
  web: automated
---

# Client Suspended: aksi tulis Missing ditolak dengan toast suspended, data tetap terbaca

## Prerequisites
- Aktor: Total Control pada Client `Klien Suspended {runId}`.
- Layar awal: halaman Assets.
- Data:
  - DU-028-1: Client, Name `Klien Suspended {runId}`, Status `Suspended`; entitas khusus yang tidak dipakai spec lain.
  - DU-028-2: Missing record, Name `Laptop Dell Latitude 5420 {runId} - 22`, Asset ID `LPT-0022 {runId}`, Group `Finance Room {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`.
  - DU-028-3: Missing record, Name `Monitor LG 27UL500 {runId} - 11`, Asset ID `MON-0011 {runId}`, Group `Finance Room {runId}`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Sari Dewi {runId}` (pemegang aset tanpa hak Aktor Missing).

## Test Steps

### Data tetap terbaca pada Client Suspended
1. Klik tab `Missing`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris `Laptop Dell Latitude 5420 {runId} - 22` dengan Status `Missing` tampil
4. Klik nama `Laptop Dell Latitude 5420 {runId} - 22`
5. Verifikasi dialog `Missing Log` untuk record `Laptop Dell Latitude 5420 {runId} - 22` terbuka
6. Klik `✕` pada dialog Missing Log

### Aksi tulis ditolak dengan toast suspended
7. Klik menu ⋯ pada baris `Monitor LG 27UL500 {runId} - 11`
8. Klik `Review`
9. Klik `[Confirm]`
10. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
11. Verifikasi toast `You don't have permission to do this.` tidak tampil
12. Klik `✕` pada dialog Missing Log
13. Verifikasi baris `Monitor LG 27UL500 {runId} - 11` dengan Status `Waiting for Confirmation` tampil
