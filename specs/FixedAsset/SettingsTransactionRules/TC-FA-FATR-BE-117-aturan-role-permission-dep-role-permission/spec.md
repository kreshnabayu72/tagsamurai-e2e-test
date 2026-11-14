---
id: TC-FA-FATR-BE-117-aturan-role-permission-dep-role-permission
title: "Penugasan Approver di Role Permission"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
owner: BE
sourceRules: ["§11#r1"]
smoke: []
dependsOn:
  - "Role Permission: penugasan Role Transaksi Approver dan perubahan role"
trace:
  "§11#r1": [4, 6, 8, 10, 12]
---

# Penugasan Approver di Role Permission

## Prerequisites
- Aktor: Total Control. Pengaju: `Rudi Hartono {runId}`, bukan Group Manager dan bukan Total Control.
- Data:
  - DU-117-1: Group `Divisi Operasional {runId}`.
  - DU-117-2: Group `Seksi Lapangan {runId}`, sub-Group dari `Divisi Operasional {runId}`.
  - DU-117-3: Group `Divisi Keuangan {runId}`, tanpa penugasan Role Transaksi `Approver`.
  - DU-117-4: Group `Divisi Gudang {runId}`.
  - DU-117-5: user `Agus Prasetyo {runId}`, aktif, bukan Read Only, cakupan `Divisi Operasional {runId}`.
  - DU-117-6: user `Bima Santoso {runId}`, nonaktif, cakupan `Divisi Gudang {runId}`.
  - DU-117-7: user `Rudi Hartono {runId}`, aktif, pengaju transaksi, bukan Group Manager dan bukan Total Control.
  - DU-117-8: aset `Truk Boks Unit 1 {runId}` di Group `Divisi Operasional {runId}`.
  - DU-117-9: aset `Forklift Mini Unit 1 {runId}` di Group `Seksi Lapangan {runId}`.
  - DU-117-10: aset `Printer Keuangan Unit 1 {runId}` di Group `Divisi Keuangan {runId}`.
  - DU-117-11: aset `Rak Roda Unit 1 {runId}` di Group `Divisi Gudang {runId}`.
  - DU-117-12: aset `Truk Boks Unit 2 {runId}` di Group `Divisi Operasional {runId}`.
- Kondisi:
  - Approval Workflow tersedia pada paket entitas.
  - Require approval bernilai `ON` untuk transaksi pinjam dan transaksi serah terima aset pada Company default.

## Test Steps

### Penugasan Approver per jenis transaksi pada Group dan turunannya
1. Total Control menugaskan Role Transaksi `Approver` untuk transaksi pinjam pada Group `Divisi Operasional {runId}` kepada user `Agus Prasetyo {runId}`
2. Total Control menugaskan Role Transaksi `Approver` untuk transaksi pinjam pada Group `Divisi Gudang {runId}` kepada user `Bima Santoso {runId}`
3. `Rudi Hartono {runId}` mengajukan peminjaman aset `Truk Boks Unit 1 {runId}` di Group `Divisi Operasional {runId}`
4. Verifikasi approval peminjaman aset `Truk Boks Unit 1 {runId}` menunggu keputusan `Agus Prasetyo {runId}`, user yang ditugaskan Role Transaksi `Approver` untuk transaksi pinjam pada Group aset
5. `Rudi Hartono {runId}` mengajukan peminjaman aset `Forklift Mini Unit 1 {runId}` di Group `Seksi Lapangan {runId}`
6. Verifikasi approval peminjaman aset `Forklift Mini Unit 1 {runId}` menunggu keputusan `Agus Prasetyo {runId}` karena penugasan pada Group `Divisi Operasional {runId}` mencakup descendant-nya
7. `Rudi Hartono {runId}` mengajukan serah terima aset `Truk Boks Unit 2 {runId}` di Group `Divisi Operasional {runId}`
8. Verifikasi approval serah terima aset `Truk Boks Unit 2 {runId}` tidak menunggu `Agus Prasetyo {runId}` karena penugasan Role Transaksi `Approver` berlaku per jenis transaksi dan hanya untuk transaksi pinjam
9. `Rudi Hartono {runId}` mengajukan peminjaman aset `Printer Keuangan Unit 1 {runId}` di Group `Divisi Keuangan {runId}`
10. Verifikasi approval peminjaman aset `Printer Keuangan Unit 1 {runId}` tidak menunggu `Agus Prasetyo {runId}` karena penugasan berlaku per Group dan tidak mencakup `Divisi Keuangan {runId}`
11. `Rudi Hartono {runId}` mengajukan peminjaman aset `Rak Roda Unit 1 {runId}` di Group `Divisi Gudang {runId}`
12. Verifikasi approval peminjaman aset `Rak Roda Unit 1 {runId}` tidak menunggu `Bima Santoso {runId}` karena user nonaktif tidak eligible, dan jatuh ke Group Manager yang menaungi lalu Total Control
