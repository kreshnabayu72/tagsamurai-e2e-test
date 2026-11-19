---
id: TC-FA-ASSIGN-E2E-041-unassign-partial
title: "Partial unassign: aset yang tidak dimasukkan tetap Assigned"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EC-ASG-24, FI-ASG-88]
smoke: []
dependsOn: []
trace:
  EC-ASG-24: [9, 10, 11]
  FI-ASG-88: [10, 11, 17]
anchor: []
coverage:
  web: automated
---

# Partial unassign: aset yang tidak dimasukkan tetap Assigned

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office`, bukan Assignee maupun PIC pada ASG di bawah.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-041-1: User `Budi Santoso`, tampil sebagai `Budi S`, karyawan aktif dengan akun login.
  - DU-041-2: Aset `Kursi Rapat {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Assigned`.
  - DU-041-3: Aset `Meja Rapat Oval {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Assigned`.
  - DU-041-4: Aset `Lemari Arsip Besi {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Assigned`.
  - DU-041-5: ASG dengan Assignee `Budi S` (Employee), Group `Head Office`, memuat DU-041-2, DU-041-3, dan DU-041-4, ketiganya `Assigned`, dengan Purpose `Perlengkapan ruang rapat lantai dua {runId}`.
- Kondisi:
  - Photo at end bernilai `OFF`.

## Test Steps

### Unassign sebagian aset dan sisanya tetap Assigned
1. Ketik Search `{runId}`, tekan Enter
2. Klik Transaction ID pada baris hasil pencarian
3. Klik tombol `[Unassign]` di bawah tabel Assets
4. Klik `Remove from List` pada menu ⋯ baris DU-041-4
5. Klik `[Submit]`
6. Buka halaman Transactions > Assignment, tab Transactions
7. Ketik Search `{runId}`, tekan Enter
8. Klik Transaction ID pada baris hasil pencarian
9. Verifikasi kolom Status DU-041-2 dan DU-041-3 menampilkan `Unassigned`
10. Verifikasi kolom Status DU-041-4 menampilkan `Assigned`
11. Verifikasi badge status header menampilkan `Assigned`

### Unassign aset terakhir menyelesaikan ASG
12. Klik tombol `[Unassign]` di bawah tabel Assets
13. Klik `[Submit]`
14. Buka halaman Transactions > Assignment, tab Transactions
15. Ketik Search `{runId}`, tekan Enter
16. Klik Transaction ID pada baris hasil pencarian
17. Verifikasi badge status header menampilkan `Unassigned`
