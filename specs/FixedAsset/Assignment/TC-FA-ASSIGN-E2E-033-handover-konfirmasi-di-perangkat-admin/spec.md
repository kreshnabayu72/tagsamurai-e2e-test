---
id: TC-FA-ASSIGN-E2E-033-handover-konfirmasi-di-perangkat-admin
title: "Handover dengan Request Confirmation dan Confirm on This Device"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.4#r13", FI-ASG-37, FI-ASG-38, FI-ASG-39, EC-ASG-14, EC-ASG-71]
smoke: []
dependsOn: []
trace:
  "§4.4#r13": 5
  FI-ASG-37: 8
  FI-ASG-38: [10, 11, 14]
  FI-ASG-39: [23, 27]
  EC-ASG-14: [4, 6, 7, 25]
  EC-ASG-71: [16, 17, 22, 24, 27]
anchor: []
coverage:
  web: automated
---

# Handover dengan Request Confirmation dan Confirm on This Device

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office`, bukan Assignee maupun PIC pada ASG di bawah.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-033-1: User `Budi Santoso`, tampil sebagai `Budi S`, karyawan aktif dengan akun login.
  - DU-033-2: Aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), butuh konfirmasi.
  - DU-033-3: Aset `Monitor LG 24 {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), butuh konfirmasi.
  - DU-033-4: Aset `Printer HP M404 {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), butuh konfirmasi.
  - DU-033-5: Aset `Proyektor Epson EB-X49 {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), tanpa konfirmasi.
  - DU-033-6: ASG dengan Assignee `Budi S` (Employee), Group `Head Office`, memuat DU-033-2, DU-033-3, DU-033-4, dan DU-033-5, semuanya berstatus `Waiting for Handover` dengan Approval `Not required` dan Purpose `Pemakaian proyek renovasi {runId}`.
- Kondisi:
  - Need recipient confirmation efektif bernilai `Yes` untuk DU-033-2, DU-033-3, dan DU-033-4, dan bernilai `No` untuk DU-033-5.
  - Photo at start bernilai `OFF`.

## Test Steps

### Request Confirmation pada sesi campuran
1. Ketik Search `{runId}`, tekan Enter
2. Klik `Hand Over` pada menu ⋯ baris ASG DU-033-6
3. Klik `[Request Confirmation]`
4. Verifikasi toast `Success, 1 asset has been assigned to Budi S.` tampil
5. Verifikasi popup `Waiting for Confirmation` tampil
6. Verifikasi daftar aset pada popup memuat DU-033-2, DU-033-3, dan DU-033-4
7. Verifikasi DU-033-5 tidak tampil pada daftar aset popup
8. Verifikasi tombol `[Confirm on This Device]` tampil pada popup

### Confirm on This Device dengan satu aset tidak diterima
9. Klik `[Confirm on This Device]`
10. Verifikasi dialog `Confirm Receipt` tampil dengan checklist aset DU-033-2, DU-033-3, dan DU-033-4
11. Verifikasi tombol `[Confirm]` disabled selama pernyataan belum dicentang
12. Hapus centang aset DU-033-4 pada checklist
13. Centang pernyataan `I confirm that Budi S is here and has received these assets and accepted responsibility for them.`
14. Verifikasi tombol `[Confirm]` aktif
15. Klik `[Confirm]`
16. Verifikasi popup menampilkan `Budi S confirmed 2 assets.`
17. Verifikasi popup menampilkan `1 asset not received.`
18. Klik `[Done]`

### Hasil konfirmasi di Assignment Detail dan Assignment Log
19. Buka halaman Transactions > Assignment, tab Transactions
20. Ketik Search `{runId}`, tekan Enter
21. Klik Transaction ID pada baris hasil pencarian
22. Verifikasi kolom Status DU-033-2 dan DU-033-3 menampilkan `Assigned`
23. Verifikasi kolom Confirmation DU-033-2 dan DU-033-3 menampilkan `Confirmed on admin device`
24. Verifikasi kolom Status DU-033-4 menampilkan `Waiting for Handover`
25. Verifikasi kolom Status DU-033-5 menampilkan `Assigned` dan kolom Confirmation menampilkan `Not required`
26. Klik `Assignment Log` pada menu ⋯ baris DU-033-2
27. Verifikasi baris detail Confirmation pada node `Handed over by [Giver]` bernilai `Confirmed by [Aktor] on behalf of [Assignee]`, dengan Aktor adalah pengguna yang login dan Assignee adalah `Budi Santoso`
