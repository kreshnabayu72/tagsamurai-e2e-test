---
id: TC-FA-ASSIGN-E2E-024-cancel-assignment-per-baris
title: "Cancel Assignment per baris"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EC-ASG-86"]
smoke: []
dependsOn: []
trace:
  "EC-ASG-86": [6, 10, 17, 21]
anchor: []
coverage:
  web: automated
---

# Cancel Assignment per baris

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office`.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-024-1: ASG Assignee Employee `Budi Setiawan`, Group `Head Office`, berisi dua baris: `Laptop Dell Latitude 5420 {runId}` berstatus `Unassigned` dan `Monitor LG 24 {runId}` berstatus `Waiting for Handover`.
  - DU-024-2: ASG Assignee Employee `Budi Setiawan`, Group `Head Office`, berisi satu baris `Printer HP M404 {runId}` berstatus `Waiting for Handover`.
  - DU-024-3: Assignee Employee `Budi Setiawan` (email `budi.setiawan@example.com`, Position `Analyst`, Division `Finance`, Home Group `Branch Surabaya`), karyawan aktif dengan akun login.
- Kondisi:
  - Feature Suite Assignment bernilai `Full`.

## Test Steps

### Cancel baris terakhir yang belum selesai menyisakan baris Unassigned
1. Ketik Search `Monitor LG 24 {runId}`, tekan Enter
2. Klik Transaction ID pada baris ASG hasil
3. Klik `⋯` pada baris `Monitor LG 24 {runId}`
4. Klik `Cancel Assignment`
5. Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
6. Verifikasi status header ASG `Unassigned`
7. Buka `Transactions > Assignment`
8. Klik tab `History`
9. Ketik Search `Monitor LG 24 {runId}`, tekan Enter
10. Verifikasi ASG dengan aset `Monitor LG 24 {runId}` tampil di tab History berstatus `Unassigned`

### Cancel baris terakhir menjadikan semua baris Canceled
11. Klik tab `Transactions`
12. Ganti isi kotak search dengan `Printer HP M404 {runId}`, tekan Enter
13. Klik Transaction ID pada baris ASG hasil
14. Klik `⋯` pada baris `Printer HP M404 {runId}`
15. Klik `Cancel Assignment`
16. Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
17. Verifikasi status header ASG `Canceled`
18. Buka `Transactions > Assignment`
19. Klik tab `History`
20. Ganti isi kotak search dengan `Printer HP M404 {runId}`, tekan Enter
21. Verifikasi ASG dengan aset `Printer HP M404 {runId}` tampil di tab History berstatus `Canceled` setelah satu-satunya barisnya dibatalkan per baris
