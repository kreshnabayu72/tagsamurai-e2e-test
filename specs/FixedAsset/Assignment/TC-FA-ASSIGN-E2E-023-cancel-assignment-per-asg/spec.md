---
id: TC-FA-ASSIGN-E2E-023-cancel-assignment-per-asg
title: "Cancel Assignment per ASG sebelum handover"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§3#p11", "TS-ASG-11", "D-ASG-09"]
smoke: []
dependsOn: []
trace:
  "§3#p11": [8, 14]
  "TS-ASG-11": 6
  "D-ASG-09": [22, 23, 27]
anchor: [2, 26]
coverage:
  web: automated
---

# Cancel Assignment per ASG sebelum handover

## Prerequisites
- Aktor:
  - Aktor A: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office`.
  - Aktor B: Group Manager dengan cakupan Group `Head Office`, hanya memicu pembatalan oleh aktor lain.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-023-1: ASG Assignee Employee `Nadia Pratama {runId}`, Group `Head Office`, berstatus Waiting for Handover, berisi aset `Printer HP M404 {runId}` dengan Purpose `Kerja harian`.
  - DU-023-2: ASG Assignee Employee `Nadia Pratama {runId}`, Group `Head Office`, berstatus Waiting for Handover, berisi aset `Laptop Dell Latitude 5420 {runId}` dengan Purpose `Kerja harian`.
  - DU-023-3: ASG Assignee Employee `Nadia Pratama {runId}`, Group `Head Office`, berstatus Waiting for Handover, berisi aset `Monitor LG 24 {runId}` dengan Purpose `Kerja harian`, tidak dibatalkan.
  - DU-023-4: Assignee Employee `Nadia Pratama {runId}` (email `nadia.pratama.{runId}@example.com`, Position `Accountant`, Division `Finance`, Home Group `Branch Surabaya`), karyawan aktif dengan akun login.
- Kondisi:
  - Feature Suite Assignment bernilai `Full`.
  - Akun Aktor B aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Cancel Assignment per ASG sebelum handover
1. Ketik Search `Printer HP M404 {runId}`, tekan Enter
2. Verifikasi baris ASG Assignee `Nadia Pratama {runId}` berstatus `Waiting for Handover` tampil
3. Klik `⋯` pada baris ASG
4. Klik `Cancel Assignment`
5. Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
6. Verifikasi toast `Success, assignment has been canceled.` tampil
7. Klik tab `History`
8. Verifikasi ASG dengan aset `Printer HP M404 {runId}` tampil di tab History berstatus `Canceled`

### Aset ASG yang dibatalkan kembali tersedia
9. Klik tab `Transactions`
10. Klik `[+ Assign]`
11. Klik pilihan `Employee`
12. Klik `[+ Asset]`
13. Ketik Search `Printer HP M404 {runId}`, tekan Enter
14. Verifikasi baris `Printer HP M404 {runId}` tampil lagi pada dialog Select Asset karena Custody kembali `Available`
15. Klik `[Cancel]` pada dialog Select Asset
16. Klik `[Cancel]` pada form (form belum diubah, tanpa dialog Unsaved Changes)

### ASG yang sudah dibatalkan pihak lain saat dialog dikonfirmasi
17. Ganti isi kotak search dengan `Laptop Dell Latitude 5420 {runId}`, tekan Enter
18. Klik `⋯` pada baris ASG
19. Klik `Cancel Assignment`
20. Aktor B membatalkan ASG dengan aset `Laptop Dell Latitude 5420 {runId}` lewat `Cancel Assignment`
21. Klik `[Cancel Assignment]` pada dialog `Cancel Assignment`
22. Verifikasi dialog `Assignment Canceled` tampil dengan teks `This assignment was canceled by [Name].`
23. Verifikasi dialog `Assignment Canceled` menyediakan tombol `[Close]`
24. Klik `[Close]`
25. Ganti isi kotak search dengan `{runId}`, tekan Enter
26. Verifikasi baris ASG dengan aset `Monitor LG 24 {runId}` tetap tampil di tab Transactions
27. Verifikasi ASG dengan aset `Laptop Dell Latitude 5420 {runId}` tidak tampil lagi di tab Transactions setelah daftar dimuat ulang
