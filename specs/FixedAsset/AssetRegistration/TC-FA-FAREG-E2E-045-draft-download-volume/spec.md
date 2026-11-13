---
id: TC-FA-FAREG-E2E-045-draft-download-volume
title: "Sub tab Draft: Download lebih dari 5.000 baris"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-DL-5"]
smoke: []
dependsOn: []
trace:
  "EB-DL-5": [5, 6, 7]
anchor: [2]
coverage:
  web: automated
---

# Sub tab Draft: Download lebih dari 5.000 baris

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft.
- Data:
  - DU-045-1: 5001 batch Draft dengan Group `Gudang Volume {n} {runId}` (n = 1 sampai 5001), Origin `—`, Total Asset `2`, Progress `0%`, Requested By `Rina W`, Last Updated `T0 − {n} menit`.
  - Rina W adalah pengguna aktif dengan role Manage asset & TAG pada Group batch.
  - Seluruh baris yang namanya memuat {runId} berjumlah 5001, melebihi ambang 5.000 baris.

## Test Steps

### Download di atas 5.000 baris memakai loading screen
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi tabel sub tab Draft memuat baris `Gudang Volume 1 {runId}`
3. Klik `[Download]`
4. Pilih `Download as CSV`
5. Verifikasi loading screen tampil sampai berkas siap
6. Verifikasi tidak ada toast informasional dan tidak ada notifikasi in-app selama berkas disiapkan
7. Verifikasi berkas `Registration-Drafts` dengan ekstensi `.csv` langsung terunduh sesudah loading screen selesai dan memuat baris `Gudang Volume 5001 {runId}`
