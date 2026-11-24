---
id: TC-FA-DISP-BE-003-edit-execution-penanda-harga
title: "Edit Execution yang menurunkan Final price melebihi batas memberi penanda Price changed after approval tanpa persetujuan ulang"
layer: be-e2e
priority: High
caseType: Positive
status: draft
owner: BE
sourceRules: ["FLD-43", "FLD-43e", "DISP-LOGIC-21", "DISP-LOGIC-09", "EC-DISP-159"]
smoke: []
dependsOn:
  - "Disposal: pengajuan, approval, dan Execute"
trace:
  "FLD-43e": [3, 4, 5, 6, 7, 8, 12]
  "DISP-LOGIC-21": [3, 4, 5, 6, 7, 8, 9, 12]
  "DISP-LOGIC-09": [2, 6, 7]
  "EC-DISP-159": [5, 6, 7, 8, 9]
anchor: []
---

# Edit Execution yang menurunkan Final price melebihi batas memberi penanda Price changed after approval tanpa persetujuan ulang

## Prerequisites
- Aktor: Aktor Disposal `Dian Pratama {runId}` (DU-003-1) yang melakukan Execute dan Edit Execution; Approver `Agus Salim {runId}` (DU-003-2) yang sudah menyetujui.
- Data:
  - DU-003-1: User, Aktor Disposal: Name `Dian Pratama {runId}`; Role Transaksi `Aktor Disposal`; Cakupan Group `Gudang Harga {runId}`; Status `Aktif`.
  - DU-003-2: User, Approver Disposal: Name `Agus Salim {runId}`; Role Transaksi `Approver` Disposal; Cakupan Group `Gudang Harga {runId}`; Status `Aktif`.
  - DU-003-3: Group, Group asal aset: Name `Gudang Harga {runId}`.
  - DU-003-4: Category: Name `Mesin Harga {runId}`; Require approval `ON`; Approval type `Any one approver`; Max price drop from approved price nilai sendiri `10`.
  - DU-003-5: Asset: Name `Mesin Koreksi A {runId}`; Category `Mesin Harga {runId}`; Group `Gudang Harga {runId}`; Tag `Ber-tag`; Disposal `Sell` berstatus `Executed` dengan Proposed price `10.000.000` (disetujui) dan Final price `10.000.000`.
  - DU-003-6: Asset: Name `Mesin Koreksi B {runId}`; sama dengan DU-003-5 tetapi jenis `Trade-in`.
- Kondisi:
  - Nilai FLD-43 `10` di-snapshot di baris saat Submit; batas bawah Final price adalah `9.000.000`.
  - Entitas memiliki lisensi Accounting & Depreciation (FA-7) aktif; baris yang di-Execute berstatus `Executed` dan belum di-Post.
  - Akun `Dian Pratama {runId}` aktif dan kredensialnya disediakan fase 2.
  - Spec ini belum pernah dijalankan; status `draft` sampai dijalankan.

## Test Steps

### Penurunan dalam batas tidak diberi penanda
1. `Dian Pratama {runId}` membuka halaman Waiting to Post dan memilih baris Sell aset `Mesin Koreksi A {runId}`
2. `Dian Pratama {runId}` memilih Edit Execution dan mengubah Final price menjadi `9.500.000` dengan Reason `Koreksi nominal` lalu Save
3. Verifikasi Final price baris menjadi `9.500.000` dan baris tidak memuat penanda `Price changed after approval`, karena penurunan 5% masih dalam batas 10%

### Penurunan melebihi batas diberi penanda tanpa persetujuan ulang
4. `Dian Pratama {runId}` memilih Edit Execution baris yang sama dan mengubah Final price menjadi `8.000.000` dengan Reason `Harga akhir disepakati lebih rendah` lalu Save
5. Verifikasi perubahan tersimpan dan Final price baris menjadi `8.000.000`
6. Verifikasi baris tetap berstatus `Executed`, tidak kembali ke `Waiting for Approval`, dan Disposal Log tidak memuat node permintaan persetujuan baru
7. Verifikasi Disposal Log memuat perubahan Final price `9.500.000` menjadi `8.000.000` beserta Reason `Harga akhir disepakati lebih rendah`
8. Verifikasi penanda `Price changed after approval` tampil pada baris di Waiting to Post dan pada Disposal Detail aset `Mesin Koreksi A {runId}`
9. Verifikasi tidak ada notifikasi `disposal_waiting_approval` yang dikirim ke `Agus Salim {runId}` untuk perubahan itu

### Trade-in mengikuti aturan yang sama
10. `Dian Pratama {runId}` memilih Edit Execution baris Trade-in aset `Mesin Koreksi B {runId}` dan mengubah Final price menjadi `7.000.000` dengan Reason `Nilai tukar turun` lalu Save
11. Verifikasi perubahan tersimpan dan baris tetap berstatus `Executed`
12. Verifikasi penanda `Price changed after approval` tampil pada baris aset `Mesin Koreksi B {runId}` di Waiting to Post
