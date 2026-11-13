---
id: TC-FA-FAREG-E2E-117-draft-hasil-physical-count-dep-physical-count
title: "Draft hasil Physical Count: batch per Group"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-01t, FAREG-LOGIC-01u, §9.2#p8, EB-XM-2@audit]
smoke: []
dependsOn: ["Physical Count: Register as asset"]
trace:
  FAREG-LOGIC-01t: [6, 8]
  FAREG-LOGIC-01u: [6, 8]
  §9.2#p8: [6, 8]
  EB-XM-2@audit: [6, 8]
anchor: []
coverage:
  web: automated
---

# Draft hasil Physical Count: batch per Group

## Prerequisites
- Aktor: Rina, role Manage asset & TAG dengan Group terkelola `Gudang Fisik A {runId}` dan `Gudang Fisik B {runId}`.
- Layar awal: Physical Count.
- Data:
  - DU-117-1: Group `Gudang Fisik A {runId}`, ada di entitas aktor.
  - DU-117-2: Group `Gudang Fisik B {runId}`, ada di entitas aktor.
  - DU-117-3: sesi Physical Count `Hitung Fisik {runId}` dengan 3 aset temuan tanpa catatan untuk Group `Gudang Fisik A {runId}` dan 2 aset temuan tanpa catatan untuk Group `Gudang Fisik B {runId}`, semua Asset Name `Rak Fisik {runId}` dengan Brand `Olympic` dan Model `No Model`.

## Test Steps

### Register as asset membentuk satu batch Draft per Group
1. Buka sesi Physical Count `Hitung Fisik {runId}`
2. Centang baris aset temuan `Rak Fisik {runId}` untuk Group `Gudang Fisik A {runId}` dan `Gudang Fisik B {runId}`
3. Klik `Register as asset`
4. Buka Fixed Asset > Assets > Registration > Draft
5. Ketik Search `Gudang Fisik A {runId}`, tekan Enter
6. Verifikasi tepat satu baris batch `Gudang Fisik A {runId}` tampil dengan Total Asset `3` dan Requested By `Rina W`
7. Ganti isi kotak search dengan `Gudang Fisik B {runId}`, tekan Enter
8. Verifikasi tepat satu baris batch `Gudang Fisik B {runId}` tampil dengan Total Asset `2` dan Requested By `Rina W`
