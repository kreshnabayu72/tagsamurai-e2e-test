---
id: TC-FA-MISS-E2E-027-capability-dicabut
title: "Capability dicabut saat halaman terbuka: aksi berikutnya ditolak dan aksi disembunyikan"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["EB-AKS-6"]
smoke: []
dependsOn: []
trace:
  "EB-AKS-6": [4, 6, 9, 12, 15, 16]
anchor: [14]
coverage:
  web: automated
---

# Capability dicabut saat halaman terbuka: aksi berikutnya ditolak dan aksi disembunyikan

## Prerequisites
- Aktor: pemegang Manage asset & TAG dengan Update pada Group `Finance Room {runId}`; Admin lain: Total Control yang mencabut Update pada Group itu sehingga aktor tinggal memegang Read.
- Layar awal: halaman Assets.
- Data:
  - DU-027-1: Missing record, Name `Monitor LG 27UL500 {runId} - 11`, Asset ID `MON-0011 {runId}`, Group `Finance Room {runId}`, Status `Waiting for Confirmation`, Source `Reported by holder`, Last Holder `Sari Dewi {runId}` (pemegang aset tanpa hak Aktor Missing).
  - DU-027-2: Missing record, Name `Laptop Dell Latitude 5420 {runId} - 22`, Asset ID `LPT-0022 {runId}`, Group `Finance Room {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`.

## Test Steps

### Aksi tulis tersedia sebelum capability dicabut
1. Klik tab `Missing`
2. Ketik Search `{runId}`, tekan Enter
3. Klik menu ⋯ pada baris `Monitor LG 27UL500 {runId} - 11`
4. Verifikasi aksi `Review` tampil
5. Klik `Review`
6. Verifikasi tombol `[Confirm]` pada footer dialog Missing Log tampil

### Aksi berikutnya ditolak setelah capability dicabut
7. Admin lain mencabut Update pada Manage asset & TAG dari aktor untuk Group `Finance Room {runId}`
8. Klik `[Confirm]`
9. Verifikasi toast `You don't have permission to do this.` tampil
10. Klik `✕` pada dialog Missing Log
11. Ketik Search `{runId}`, tekan Enter
12. Verifikasi baris `Monitor LG 27UL500 {runId} - 11` dengan Status `Waiting for Confirmation` tampil

### Aksi yang tidak lagi berhak disembunyikan
13. Klik menu ⋯ pada baris `Laptop Dell Latitude 5420 {runId} - 22`
14. Verifikasi aksi `Missing Log` tampil
15. Verifikasi aksi `Add Update` tidak tampil
16. Verifikasi aksi `Mark as Found` tidak tampil
17. Tekan `Esc`
