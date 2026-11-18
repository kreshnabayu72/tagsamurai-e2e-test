---
id: TC-FA-ASSIGN-E2E-040-unassign-penuh
title: "Unassign semua aset satu Assignee"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [TS-ASG-08, FI-ASG-74, FI-ASG-75, FI-ASG-76, FI-ASG-77, FI-ASG-83, FI-ASG-86, FI-ASG-62]
smoke: []
dependsOn: []
trace:
  TS-ASG-08: [11, 27, 34]
  FI-ASG-74: 13
  FI-ASG-75: 9
  FI-ASG-76: [4, 5, 6, 7]
  FI-ASG-77: 14
  FI-ASG-83: [13, 14]
  FI-ASG-86: [13, 16]
  FI-ASG-62: [11, 12, 27, 28]
anchor: [8]
coverage:
  web: automated
---

# Unassign semua aset satu Assignee

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office`, bukan Assignee maupun PIC pada ASG di bawah.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-040-1: User `Budi Santoso {runId}`, tampil sebagai `Budi S`, karyawan aktif dengan akun login.
  - DU-040-2: Aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Assigned`.
  - DU-040-3: Aset `Printer HP M404 {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Assigned` dengan laporan Damaged dari Assignee yang masih `Waiting for Confirmation`.
  - DU-040-4: Aset `Proyektor Epson EB-X49 {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Assigned` dengan laporan Missing dari Assignee yang masih `Waiting for Confirmation`.
  - DU-040-5: ASG dengan Assignee `Budi Santoso {runId}` (Employee, tampil `Budi S`), Group `Head Office`, memuat DU-040-2, DU-040-3, DU-040-4, dan DU-040-12, semuanya `Assigned`, dengan Purpose `Pemakaian divisi pemasaran {runId}`.
  - DU-040-6: Aset `Tablet Samsung Tab S8 {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Assigned`.
  - DU-040-7: ASG dengan Assignee `Sari Dewi {runId}` (Employee, tampil `Sari D`), Group `Head Office`, memuat DU-040-6 berstatus `Assigned`, dengan Purpose `Pemakaian tim lapangan {runId}`.
  - DU-040-8: Aset `Camera Sony A7 {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Assigned`.
  - DU-040-9: ASG dengan Assignee `Sari Dewi {runId}` (Employee, tampil `Sari D`), Group `Head Office`, memuat DU-040-8 berstatus `Assigned`, dengan Purpose `Dokumentasi acara kantor {runId}`.
  - DU-040-10: Aset `Kamera CCTV Hikvision {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Assigned`.
  - DU-040-11: ASG dengan Assignee `Budi Santoso {runId}` (Employee, tampil `Budi S`), Group `Head Office`, memuat DU-040-10 berstatus `Assigned`, dengan Purpose `Pengawasan gudang {runId}`.
  - DU-040-12: Aset `Mesin Fotokopi Canon {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Assigned` dengan laporan Damaged yang sudah dikonfirmasi (badge `Damaged`).
  - DU-040-13: User `Sari Dewi {runId}`, tampil sebagai `Sari D`, karyawan aktif dengan akun login.
- Kondisi:
  - Photo at end bernilai `OFF`.

## Test Steps

### Unassign semua aset ASG dari Assignment Detail
1. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
2. Klik Transaction ID pada baris hasil pencarian
3. Klik tombol `[Unassign]` di bawah tabel Assets
4. Verifikasi kolom Status DU-040-2 menampilkan `Assigned`
5. Verifikasi kolom Status DU-040-3 menampilkan `Reported Damaged`
6. Verifikasi kolom Status DU-040-4 menampilkan `Reported Missing`
7. Verifikasi kolom Status DU-040-12 menampilkan `Damaged`
8. Verifikasi kolom `Status` dan `Verification` tampil pada daftar aset
9. Verifikasi kolom `Assess`, `Compare`, dan `Damage` tidak tampil pada daftar aset
10. Klik `[Submit]`
11. Verifikasi toast `Success, 4 assets have been unassigned.` tampil
12. Verifikasi halaman Assignment Detail tampil dengan Assignee `Budi S`
13. Verifikasi kolom Status DU-040-2 menampilkan `Unassigned`
14. Verifikasi kolom Status DU-040-3, DU-040-4, dan DU-040-12 menampilkan `Unassigned`
15. Klik `Assignment Log` pada menu ⋯ baris DU-040-2
16. Verifikasi Assignment Log memuat node `Unassigned by [Receiver]` dengan Assignee `Budi S`
17. Tutup dialog Assignment Log

### Unassign aset dari dua ASG berbeda
18. Buka halaman Transactions > Assignment, tab Transactions
19. Ketik Search `Tablet Samsung Tab S8 {runId}`, tekan Enter
20. Klik Transaction ID pada baris hasil pencarian
21. Klik tombol `[Unassign]` di bawah tabel Assets
22. Klik `[+ Asset]`
23. Ketik Search `Camera Sony A7 {runId}` pada dialog Select Asset, tekan Enter
24. Centang baris `Camera Sony A7 {runId}`
25. Klik `[Select]`
26. Klik `[Submit]`
27. Verifikasi toast `Success, 2 assets have been unassigned.` tampil
28. Verifikasi tab `Assigned Assets` terbuka

### Unassign satu aset
29. Buka halaman Transactions > Assignment, tab Transactions
30. Ketik Search `Kamera CCTV Hikvision {runId}`, tekan Enter
31. Klik Transaction ID pada baris hasil pencarian
32. Klik tombol `[Unassign]` di bawah tabel Assets
33. Klik `[Submit]`
34. Verifikasi toast `Success, 1 asset has been unassigned.` tampil
