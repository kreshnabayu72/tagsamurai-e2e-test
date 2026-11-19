---
id: TC-FA-ASSIGN-E2E-016-submit-multi-group-dipecah
title: "Submit aset dari beberapa Group menghasilkan beberapa ASG"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["TS-ASG-34", "EC-ASG-106"]
smoke: []
dependsOn: []
trace:
  "TS-ASG-34": [19, 20]
  "EC-ASG-106": [12, 13, 22, 24]
anchor: []
coverage:
  web: automated
---

# Submit aset dari beberapa Group menghasilkan beberapa ASG

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office` dan `Branch Surabaya`.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-016-1: Aset `Laptop Dell Latitude 5420 {runId}`, Category `Laptop`, Group `Head Office`, Custody `Available`, Condition `Normal`.
  - DU-016-2: Aset `Projector Epson EB-X49 {runId}`, Category `Projector`, Group `Head Office`, Custody `Available`, Condition `Normal`.
  - DU-016-3: Aset `Printer HP M404 {runId}`, Category `Printer`, Group `Branch Surabaya`, Custody `Available`, Condition `Normal`.
  - DU-016-4: Assignee Employee `Sari Dewi` (email `sari.dewi@example.com`, Position `Analyst`, Division `Finance`, Home Group `Head Office`), karyawan aktif dengan akun login.
  - DU-016-5: Purpose baris aset `Kerja harian`, `Presentasi`, dan `Administrasi cabang`.
  - Hasil pemecahan yang diharapkan: ASG Group `Head Office` berisi `2` aset dan ASG Group `Branch Surabaya` berisi `1` aset.
- Kondisi:
  - Feature Suite Assignment bernilai `Full`.
  - Require approval bernilai OFF untuk Category `Laptop`, `Projector`, dan `Printer`.

## Test Steps

### Aset dari dua Group diterima dalam satu form
1. Klik `[+ Assign]`
2. Klik pilihan `Employee`
3. Klik `[Select Assignee]`
4. Pilih baris `Sari Dewi` pada dialog Select Assignee
5. Klik `[Select]`
6. Klik `[+ Asset]`
7. Ketik Search `{runId}`, tekan Enter
8. Centang baris `Laptop Dell Latitude 5420 {runId}`
9. Centang baris `Projector Epson EB-X49 {runId}`
10. Centang baris `Printer HP M404 {runId}`
11. Klik `[Select]`
12. Verifikasi ketiga baris aset tampil di tabel aset dengan kolom Group `Head Office` untuk `Laptop Dell Latitude 5420 {runId}` dan `Projector Epson EB-X49 {runId}`, serta `Branch Surabaya` untuk `Printer HP M404 {runId}`
13. Verifikasi alert pemecahan tampil dan menyebut Group `Head Office` dan `Branch Surabaya`
14. Isi Purpose baris `Laptop Dell Latitude 5420 {runId}` dengan `Kerja harian`
15. Isi Purpose baris `Projector Epson EB-X49 {runId}` dengan `Presentasi`
16. Isi Purpose baris `Printer HP M404 {runId}` dengan `Administrasi cabang`

### Submit memecah menjadi satu ASG per Group
17. Klik `[Submit]`
18. Klik `[Submit]` pada dialog `Submit Assignment`
19. Verifikasi toast `Success, 2 assignments have been submitted.` tampil setelah Submit aset dari dua Group
20. Verifikasi daftar tab Transactions yang terbuka setelah Submit, bukan halaman Assignment Detail
21. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
22. Verifikasi satu baris ASG dengan Group `Head Office`, Assignee `Sari Dewi`, dan Total Asset `2`
23. Ganti isi kotak search dengan `Printer HP M404 {runId}`, tekan Enter
24. Verifikasi satu baris ASG dengan Group `Branch Surabaya`, Assignee `Sari Dewi`, dan Total Asset `1`
