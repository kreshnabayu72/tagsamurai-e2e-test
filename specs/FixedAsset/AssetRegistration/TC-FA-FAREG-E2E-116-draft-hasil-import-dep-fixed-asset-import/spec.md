---
id: TC-FA-FAREG-E2E-116-draft-hasil-import-dep-fixed-asset-import
title: "Draft hasil Import: batch per Group dan alur Edit serta Delete"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-01t, FAREG-LOGIC-01u, FAREG-LOGIC-01v, §9.2#p8, EB-XM-2@import, EB-XM-3]
smoke: []
dependsOn: ["Fixed Asset Import: impor aset"]
trace:
  FAREG-LOGIC-01t: [5, 8]
  FAREG-LOGIC-01u: [6]
  FAREG-LOGIC-01v: [2, 10]
  §9.2#p8: [5, 8]
  EB-XM-2@import: [5, 8, 17, 22]
  EB-XM-3: [15, 17, 21, 22]
anchor: []
coverage:
  web: automated
---

# Draft hasil Import: batch per Group dan alur Edit serta Delete

## Prerequisites
- Aktor: Rina, role Manage asset & TAG dengan Group terkelola `Gudang Impor A {runId}` dan `Gudang Impor B {runId}`, tidak mencakup Group `Gudang Luar {runId}`.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-116-1: Group `Gudang Impor A {runId}`, ada di entitas aktor.
  - DU-116-2: Group `Gudang Impor B {runId}`, ada di entitas aktor.
  - DU-116-3: Group `Gudang Luar {runId}`, ada di entitas aktor.
  - DU-116-4: berkas impor `Import-Aset-{runId}.xlsx` berisi 3 aset untuk Group `Gudang Impor A {runId}`, 2 aset untuk Group `Gudang Impor B {runId}`, dan 1 aset untuk Group `Gudang Luar {runId}`, semua Asset Name `Rak Impor {runId}` dengan Brand `Olympic` dan Model `No Model`.
  - DU-116-5: Quantity `4` yang diketik Rina saat mengedit batch hasil impor.

## Test Steps

### Import membentuk satu batch Draft per Group
1. Impor berkas `Import-Aset-{runId}.xlsx` di Fixed Asset Import
2. Verifikasi baris berkas untuk Group `Gudang Luar {runId}` ditolak pada baris itu
3. Buka Fixed Asset > Assets > Registration > Draft
4. Ketik Search `Gudang Impor A {runId}`, tekan Enter
5. Verifikasi tepat satu baris batch `Gudang Impor A {runId}` tampil dengan Total Asset `3`
6. Verifikasi Requested By baris batch `Gudang Impor A {runId}` adalah `Rina W`
7. Ganti isi kotak search dengan `Gudang Impor B {runId}`, tekan Enter
8. Verifikasi tepat satu baris batch `Gudang Impor B {runId}` tampil dengan Total Asset `2`
9. Ganti isi kotak search dengan `Gudang Luar {runId}`, tekan Enter
10. Verifikasi tidak ada baris batch `Gudang Luar {runId}`, empty state `No results found` tampil

### Batch hasil Import menjalani alur Edit
11. Ganti isi kotak search dengan `Gudang Impor A {runId}`, tekan Enter
12. Klik row action `Edit` pada baris batch `Gudang Impor A {runId}`
13. Ganti Quantity Item pertama menjadi `4`
14. Klik `[Save draft]`
15. Verifikasi toast `Success, draft has been saved.`
16. Klik `[Cancel]`
17. Verifikasi baris batch `Gudang Impor A {runId}` tampil dengan Total Asset `4`

### Batch hasil Import menjalani alur Delete
18. Ganti isi kotak search dengan `Gudang Impor B {runId}`, tekan Enter
19. Klik row action `Delete` pada baris batch `Gudang Impor B {runId}`
20. Klik `[Delete]` pada dialog `Delete Draft`
21. Verifikasi toast `Success, draft has been deleted.`
22. Verifikasi tidak ada baris batch `Gudang Impor B {runId}`, empty state `No results found` tampil
