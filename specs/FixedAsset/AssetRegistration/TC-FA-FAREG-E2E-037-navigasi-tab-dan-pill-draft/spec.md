---
id: TC-FA-FAREG-E2E-037-navigasi-tab-dan-pill-draft
title: "Tab Registration: jumlah pada pill Draft mengikuti data"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1#p3"]
smoke: []
dependsOn: []
trace:
  "§4.1#p3": [4, 5, 10, 11]
anchor: [2]
coverage:
  web: automated
---

# Tab Registration: jumlah pada pill Draft mengikuti data

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft.
- Data:
  - DU-037-1: Batch Draft dengan Group `Gudang Kemang {runId}`, Origin `—`, Total Asset `8`, Progress `50%`, Requested By `Rina W`, Last Updated `T0 − 1 hari`, ada di entitas aktor.
  - DU-037-2: Batch Draft dengan Group `Gudang Tebet {runId}`, Origin `—`, Total Asset `15`, Progress `100%`, Requested By `Agus P`, Last Updated `T0 − 2 hari`, ada di entitas aktor.
  - Rina W dan Agus P adalah pengguna aktif dengan role Manage asset & TAG pada Group batch masing-masing.

## Test Steps

### Jumlah pada pill Draft tidak mengikuti Search
1. Catat jumlah pada judul pill `Draft` sebagai jumlah awal
2. Verifikasi tabel sub tab Draft memuat baris `Gudang Kemang {runId}` dan baris `Gudang Tebet {runId}`
3. Ketik Search `Gudang Kemang {runId}`, tekan Enter
4. Verifikasi tabel sub tab Draft hanya memuat baris `Gudang Kemang {runId}` dan tidak memuat baris `Gudang Tebet {runId}`
5. Verifikasi jumlah pada judul pill `Draft` sama dengan jumlah awal
6. Klik `(←)` pada kotak Search

### Jumlah pada pill Draft tidak mengikuti Filter
7. Klik ikon Filter
8. Pilih Group `Gudang Tebet {runId}` pada field `Group`
9. Klik `[Apply]`
10. Verifikasi tabel sub tab Draft memuat baris `Gudang Tebet {runId}` dan tidak memuat baris `Gudang Kemang {runId}`
11. Verifikasi jumlah pada judul pill `Draft` sama dengan jumlah awal
