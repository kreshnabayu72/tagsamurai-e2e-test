---
id: TC-FA-MISS-E2E-026-aktor-tanpa-akses
title: "Aktor tanpa capability: tab Missing tidak tampil dan alamat langsung ditolak"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["EB-AKS-1", "EB-AKS-2", "§4.8#r1"]
smoke: []
dependsOn: []
trace:
  "EB-AKS-1": 2
  "EB-AKS-2": [4, 5, 6]
  "§4.8#r1": 2
anchor: [1]
coverage:
  web: automated
---

# Aktor tanpa capability: tab Missing tidak tampil dan alamat langsung ditolak

## Prerequisites
- Aktor: pengguna dengan role tanpa capability apa pun pada modul Missing dan tanpa Group yang ditugaskan.
- Layar awal: halaman Assets.
- Data:
  - DU-026-1: Missing record, Name `Laptop Dell Latitude 5420 {runId} - 22`, Asset ID `LPT-0022 {runId}`, Group `Finance Room {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`.

## Test Steps

### Tab Missing tidak tampil
1. Verifikasi tab `Assets` tampil pada halaman Assets
2. Verifikasi tab `Missing` tidak tampil pada halaman Assets

### Alamat langsung tab Missing ditolak
3. Buka alamat langsung tab `Missing` pada halaman Assets
4. Verifikasi toast `You don't have permission to do this.` tampil
5. Verifikasi record `Laptop Dell Latitude 5420 {runId} - 22` tidak tampil
6. Verifikasi halaman tidak berpindah ke halaman lain dari alamat yang dibuka
