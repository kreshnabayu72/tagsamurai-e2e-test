---
id: TC-FA-ASSIGN-E2E-039-scan-tag-handover-dan-unassign
title: "Scan TAG saat Handover dan Unassign: penolakan dan verifikasi"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [FI-ASG-18, FI-ASG-24, FI-ASG-47, FI-ASG-48, FI-ASG-49, FI-ASG-50, FI-ASG-51, FI-ASG-52, FI-ASG-53, FI-ASG-54, FI-ASG-55, FI-ASG-56, V-ASG-17, V-ASG-18, V-ASG-24, V-ASG-25, "§4.4#r10", "§4.4#r11", "§4.4#r12"]
smoke: []
dependsOn: []
trace:
  FI-ASG-18: 7
  FI-ASG-24: [5, 7, 9, 11, 12, 47, 48]
  FI-ASG-47: 19
  FI-ASG-48: [18, 24, 26, 28]
  FI-ASG-49: 40
  FI-ASG-50: 17
  FI-ASG-51: 38
  FI-ASG-52: 31
  FI-ASG-53: 33
  FI-ASG-54: 35
  FI-ASG-55: 37
  FI-ASG-56: 29
  V-ASG-17: [5, 7, 9, 11]
  V-ASG-18: 14
  V-ASG-24: 35
  V-ASG-25: [31, 33]
  "§4.4#r10": 5
  "§4.4#r11": 7
  "§4.4#r12": 31
anchor: [3]
coverage:
  web: manual
---

# Scan TAG saat Handover dan Unassign: penolakan dan verifikasi

## Prerequisites
- Aktor: Asset Admin `Hendra Kusuma {runId}` (Aktor Assignment) dengan cakupan Group `Head Office`, juga Assignee pada ASG DU-039-19 dan PIC pada ASG Division DU-039-26.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-039-1: User `Budi Santoso {runId}`, tampil sebagai `Budi S`, karyawan aktif dengan akun login.
  - DU-039-2: User `Sari Dewi {runId}`, tampil sebagai `Sari D`, karyawan aktif dengan akun login.
  - DU-039-3: User `Hendra Kusuma {runId}`, Asset Admin dengan cakupan Group `Head Office`, anggota aktif Division `Procurement` dengan akun login.
  - DU-039-4: User `Rina Wijaya {runId}`, Approver dengan cakupan Group `Head Office`, karyawan aktif dengan akun login.
  - DU-039-5: Aset `Laptop HP ProBook {runId}`, Group `Head Office`, TAG `RFID`, berstatus `Waiting for Handover`, TAG dapat dibaca.
  - DU-039-6: Aset `Monitor Dell P2422H {runId}`, Group `Head Office`, TAG `RFID`, berstatus `Waiting for Handover`, TAG tidak dapat dibaca.
  - DU-039-7: Aset `Toyota Avanza {runId}`, Group `Head Office`, TAG `RFID`, berstatus `Waiting for Approval` dengan approver `Rina Wijaya {runId}`.
  - DU-039-8: Aset `Printer Canon G3010 {runId}`, Group `Head Office`, TAG `RFID`, berstatus `Available`, tidak ada di ASG manapun.
  - DU-039-9: Aset `Genset Honda 5KVA {runId}`, Group `Branch Surabaya`, TAG `RFID`, berstatus `Available`.
  - DU-039-10: Aset `Meja Lipat {runId}`, Group `Head Office`, TAG `RFID`, berstatus `Waiting for Handover` pada ASG DU-039-19.
  - DU-039-11: Aset `Kursi Lipat {runId}`, Group `Head Office`, TAG `RFID`, berstatus `Assigned` pada ASG DU-039-19.
  - DU-039-12: Aset `Kamera Canon EOS {runId}`, Group `Head Office`, TAG `RFID`, berstatus `Assigned` pada ASG DU-039-20.
  - DU-039-13: Aset `Lensa Canon 50mm {runId}`, Group `Head Office`, TAG `RFID`, berstatus `Assigned` pada ASG DU-039-20.
  - DU-039-14: Aset `Tripod Manfrotto {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Assigned` pada ASG DU-039-20.
  - DU-039-15: Aset `Rak Server {runId}`, Group `Head Office`, TAG `RFID`, berstatus `Available`.
  - DU-039-16: Aset `Flash Godox {runId}`, Group `Head Office`, TAG `RFID`, berstatus `Assigned` pada ASG DU-039-21.
  - DU-039-17: Aset `Kompresor Udara {runId}`, Group `Branch Surabaya`, TAG `RFID`, berstatus `Assigned` pada ASG DU-039-22.
  - DU-039-18: ASG dengan Assignee `Sari Dewi {runId}` (Employee, tampil `Sari D`), Group `Head Office`, memuat DU-039-5 dan DU-039-6 berstatus `Waiting for Handover` dan DU-039-7 berstatus `Waiting for Approval`, dengan Purpose `Peralatan kantor proyek baru {runId}`.
  - DU-039-19: ASG dengan Assignee `Hendra Kusuma {runId}` (Employee), Group `Head Office`, memuat DU-039-10 berstatus `Waiting for Handover` dan DU-039-11 berstatus `Assigned`, dengan Purpose `Perlengkapan kerja pribadi {runId}`.
  - DU-039-20: ASG dengan Assignee `Budi Santoso {runId}` (Employee, tampil `Budi S`), Group `Head Office`, memuat DU-039-12, DU-039-13, DU-039-14, dan DU-039-23, semuanya `Assigned`, dengan Purpose `Peralatan dokumentasi {runId}`.
  - DU-039-21: ASG dengan Assignee `Sari Dewi {runId}` (Employee, tampil `Sari D`), Group `Head Office`, memuat DU-039-16 berstatus `Assigned`, dengan Purpose `Pencahayaan studio {runId}`.
  - DU-039-22: ASG dengan Assignee `Budi Santoso {runId}` (Employee, tampil `Budi S`), Group `Branch Surabaya`, memuat DU-039-17 berstatus `Assigned`, dengan Purpose `Perawatan mesin cabang {runId}`.
  - DU-039-23: Aset `Drone DJI Mavic {runId}`, Group `Head Office`, TAG `RFID`, berstatus `Assigned` pada ASG DU-039-20, belum dimasukkan ke daftar Unassign.
  - DU-039-24: Aset `Helm Proyek Safety {runId}`, Group `Head Office`, TAG `RFID`, berstatus `Waiting for Handover` pada ASG DU-039-26.
  - DU-039-25: Division `Procurement`.
  - DU-039-26: ASG dengan Assignee Division `Procurement`, PIC `Hendra Kusuma {runId}` aktif, Group `Head Office`, memuat DU-039-24 berstatus `Waiting for Handover`, dengan Purpose `Pengadaan perlengkapan proyek {runId}`.
- Kondisi:
  - Need recipient confirmation efektif bernilai `Yes` untuk DU-039-5, DU-039-6, dan DU-039-7.
  - Photo at start dan Photo at end bernilai `OFF`.
  - Cakupan Group Aktor tidak meliputi `Branch Surabaya`.
  - Feature Suite Assignment pada level `Full`.

## Test Steps

### Scan TAG yang ditolak pada halaman Handover
1. Ketik Search `Laptop HP ProBook {runId}`, tekan Enter
2. Klik `Hand Over` pada menu ⋯ baris ASG DU-039-18
3. Verifikasi kolom Verification DU-039-5 dan DU-039-6 menampilkan `Unverified`
4. Pindai TAG aset DU-039-8 lewat `[Verify Asset]`
5. Verifikasi toast `Error, this TAG belongs to [Asset Code], not in this assignment.` tampil dengan Asset Code milik DU-039-8
6. Pindai TAG aset DU-039-7 lewat `[Verify Asset]`
7. Verifikasi toast `Error, this asset is still waiting for approval from [Names].` tampil dengan Approver DU-039-4 pada posisi `[Names]`
8. Pindai TAG aset DU-039-9 lewat `[Verify Asset]`
9. Verifikasi toast `Error, this asset belongs to Branch Surabaya.` tampil
10. Pindai TAG aset DU-039-10 lewat `[Verify Asset]`
11. Verifikasi toast `Error, you can't hand over or receive your own assignment.` tampil
12. Verifikasi kolom Verification DU-039-5 dan DU-039-6 tetap menampilkan `Unverified`

### TAG yang tidak terbaca pada halaman Handover
13. Pindai TAG aset DU-039-6 lewat `[Verify Asset]`
14. Verifikasi toast `Error, this TAG can't be read. Report the TAG and use another asset.` tampil

### Verify Asset menerapkan hasil pindai pada halaman Unassign
15. Buka halaman Unassign lewat row action `Unassign` pada baris `Kamera Canon EOS {runId}` di tabel Assets Assignment Detail ASG DU-039-20
16. Pindai TAG aset DU-039-12 lewat `[Verify Asset]`
17. Verifikasi field Assignee sudah terisi dari titik masuk tanpa dipilih manual
18. Verifikasi DU-039-12 tampil di daftar dengan Verification `Verified`
19. Verifikasi tidak ada dialog yang terbuka setelah pemindaian
20. Klik `[+ Asset]`
21. Centang baris `Lensa Canon 50mm {runId}`
22. Centang baris `Tripod Manfrotto {runId}`
23. Klik `[Select]`
24. Verifikasi kolom Verification DU-039-13 menampilkan `Unverified`
25. Pindai TAG aset DU-039-13 lewat `[Verify Asset]`
26. Verifikasi kolom Verification DU-039-13 menampilkan `Verified`
27. Pindai ulang TAG aset DU-039-13 lewat `[Verify Asset]`
28. Verifikasi daftar memuat satu baris DU-039-13 dengan Verification `Verified`
29. Verifikasi kolom Verification DU-039-14 menampilkan `Non TAG`

### Scan TAG yang ditolak pada halaman Unassign
30. Pindai TAG aset DU-039-15 lewat `[Verify Asset]`
31. Verifikasi toast `Error, this asset isn't assigned.` tampil
32. Pindai TAG aset DU-039-16 lewat `[Verify Asset]`
33. Verifikasi toast `Error, this asset isn't assigned to Budi S.` tampil
34. Pindai TAG aset DU-039-17 lewat `[Verify Asset]`
35. Verifikasi toast `Error, unassign this asset in Branch Surabaya.` tampil
36. Pindai TAG aset DU-039-11 lewat `[Verify Asset]`
37. Verifikasi toast `Error, you can't hand over or receive your own assignment.` tampil
38. Verifikasi daftar tetap memuat DU-039-12, DU-039-13, dan DU-039-14 tanpa baris tambahan

### Scan TAG aset milik Assignee terpilih yang belum ada di daftar ditambahkan langsung
39. Pindai TAG aset DU-039-23 lewat `[Verify Asset]`
40. Verifikasi DU-039-23 tampil di daftar dengan Verification `Verified`

### Scan TAG aset ASG Division dengan Aktor sebagai PIC ditolak pada halaman Handover
41. Klik `[Cancel]` pada halaman Unassign
42. Klik `[Leave]` pada dialog Unsaved Changes
43. Buka halaman Transactions > Assignment, tab Transactions
44. Ketik Search `Laptop HP ProBook {runId}`, tekan Enter
45. Klik `Hand Over` pada menu ⋯ baris ASG DU-039-18
46. Pindai TAG aset DU-039-24 lewat `[Verify Asset]`
47. Verifikasi toast `Error, you can't hand over or receive your own assignment.` tampil
48. Verifikasi kolom Verification DU-039-5 dan DU-039-6 tetap menampilkan `Unverified`
