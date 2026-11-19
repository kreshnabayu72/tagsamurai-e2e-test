---
id: TC-FA-ASSIGN-BE-223-validasi-panjang-teks-server
title: "Batas karakter Purpose, Note, Approval Note, Description, dan Reason di server"
layer: be-e2e
priority: Medium
caseType: Edge
status: ready-for-automation
sourceRules: ["EB-FRM-4@purpose", "EB-FRM-4@note", "EB-FRM-4@approval-note", "EB-FRM-4@description-report-damaged", "EB-FRM-4@reason-mark-unassigned"]
smoke: []
dependsOn: []
owner: BE
trace:
  "EB-FRM-4@purpose": [2, 4]
  "EB-FRM-4@note": [6, 8]
  "EB-FRM-4@approval-note": [10, 12]
  "EB-FRM-4@description-report-damaged": [14, 16]
  "EB-FRM-4@reason-mark-unassigned": [18, 20]
---

# Batas karakter Purpose, Note, Approval Note, Description, dan Reason di server

## Prerequisites
- Aktor: Aktor Assignment `Rina Wijaya {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); Approver `Mira Handayani {runId}` (cakupan Group `Head Office {runId}`); Assignee Employee ber-akun login seperti di entri data.
- Data:
  - DU-223-1: User, Aktor Assignment: Nama `Rina Wijaya {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-223-2: User, Approver Group: Nama `Mira Handayani {runId}`, Role `Approver`, Cakupan Group `Head Office {runId}`.
  - DU-223-3: Asset, Dua aset Available untuk Purpose tepat di batas dan di atas batas: Nama aset 1 `Laptop Asus A {runId}`, Nama aset 2 `Laptop Asus B {runId}`, Custody `Available`, Assignee `Budi Santoso {runId}`, Tipe Assignee `Employee`.
  - DU-223-6: Asset, Dua aset Available untuk Note tepat di batas dan di atas batas: Nama aset 1 `Monitor LG 24 {runId}`, Nama aset 2 `Monitor LG 27 {runId}`, Custody `Available`, Assignee `Citra Dewi {runId}`, Tipe Assignee `Employee`.
  - DU-223-9: Assignment, ASG dengan dua baris Waiting for Approval untuk Approval Note: Assignee `Dedi Prasetyo {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Printer Epson L3250 {runId}`, Baris 2 `Printer Canon G3010 {runId}`, Status baris `Waiting for Approval`, Approver `Mira Handayani {runId}`.
  - DU-223-12: Assignment, ASG dengan dua baris Assigned untuk Description Report Damaged: Assignee `Eko Wijaya {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kamera Sony Alpha {runId}`, Baris 2 `Kamera Canon EOS {runId}`, Status baris `Assigned`.
  - DU-223-15: Assignment, ASG dengan dua baris Assigned pada entitas level None untuk Reason Mark as Unassigned: Assignee `Fajar Nugroho {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Tablet iPad {runId}`, Baris 2 `Tablet Samsung Tab {runId}`, Status baris `Assigned`.
- Kondisi:
  - Batas karakter mengikuti PRD: Purpose `120`, Note `360`, Approval Note `120`, Description Report Damaged `360`, dan Reason `360`.
  - Aksi Mark as Unassigned dijalankan pada entitas ber-Feature Suite Assignment level `None`.

## Test Steps

### Purpose melebihi batas ditolak server
1. Rina mengajukan aset `Laptop Asus A {runId}` pada DU-223-3 untuk Assignee `Budi Santoso {runId}` dengan Purpose `Penggunaan perangkat kerja untuk kegiatan operasional harian tim keuangan pusat Penggunaan perangkat kerja untuk kegiata` (120 karakter) pada DU-223-4
2. Verifikasi pengajuan diterima dan Purpose tersimpan utuh tepat di batas
3. Rina mengajukan aset `Laptop Asus B {runId}` untuk Assignee `Budi Santoso {runId}` dengan Purpose `Penggunaan perangkat kerja untuk kegiatan operasional harian tim keuangan pusat Penggunaan perangkat kerja untuk kegiatan` (121 karakter) pada DU-223-5
4. Verifikasi server menolak Purpose yang melebihi batas dengan pesan `Max. 120 characters` dan tidak ada ASG yang terbentuk

### Note melebihi batas ditolak server
5. Rina mengajukan aset `Monitor LG 24 {runId}` pada DU-223-6 untuk Assignee `Citra Dewi {runId}` dengan Note `Catatan pengajuan untuk kebutuhan kerja lapangan dan administrasi kantor cabang Catatan pengajuan untuk kebutuhan kerja lapangan dan administrasi kantor cabang Catatan pengajuan untuk kebutuhan kerja lapangan dan administrasi kantor cabang Catatan pengajuan untuk kebutuhan kerja lapangan dan administrasi kantor cabang Catatan pengajuan untuk kebutuhan kerjax` (360 karakter) pada DU-223-7
6. Verifikasi pengajuan diterima dan Note tersimpan utuh tepat di batas
7. Rina mengajukan aset `Monitor LG 27 {runId}` untuk Assignee `Citra Dewi {runId}` dengan Note `Catatan pengajuan untuk kebutuhan kerja lapangan dan administrasi kantor cabang Catatan pengajuan untuk kebutuhan kerja lapangan dan administrasi kantor cabang Catatan pengajuan untuk kebutuhan kerja lapangan dan administrasi kantor cabang Catatan pengajuan untuk kebutuhan kerja lapangan dan administrasi kantor cabang Catatan pengajuan untuk kebutuhan kerja l` (361 karakter) pada DU-223-8
8. Verifikasi server menolak Note yang melebihi batas dengan pesan `Max. 360 characters` dan tidak ada ASG yang terbentuk

### Approval Note Reject melebihi batas ditolak server
9. Mira me-Reject baris `Printer Epson L3250 {runId}` pada DU-223-9 dengan Approval Note `Penolakan karena aset masih dibutuhkan unit lain pada periode yang sama Penolakan karena aset masih dibutuhkan unit lain` (120 karakter) pada DU-223-10
10. Verifikasi keputusan Reject diterima dan baris `Printer Epson L3250 {runId}` berstatus `Rejected` dengan Approval Note tersimpan utuh
11. Mira me-Reject baris `Printer Canon G3010 {runId}` dengan Approval Note `Penolakan karena aset masih dibutuhkan unit lain pada periode yang sama Penolakan karena aset masih dibutuhkan unit lainx` (121 karakter) pada DU-223-11
12. Verifikasi server menolak Approval Note yang melebihi batas dengan pesan `Max. 120 characters` dan baris `Printer Canon G3010 {runId}` tetap `Waiting for Approval`

### Description Report Damaged pada Unassign melebihi batas ditolak server
13. Rina membuat laporan rusak pada halaman Unassign untuk baris `Kamera Sony Alpha {runId}` pada DU-223-12 dengan satu foto dan Description `Layar retak di sudut kiri atas dan engsel terasa longgar saat perangkat dibuka Layar retak di sudut kiri atas dan engsel terasa longgar saat perangkat dibuka Layar retak di sudut kiri atas dan engsel terasa longgar saat perangkat dibuka Layar retak di sudut kiri atas dan engsel terasa longgar saat perangkat dibuka Layar retak di sudut kiri atas dan engsel te` (360 karakter) pada DU-223-13
14. Verifikasi laporan diterima dan Description tersimpan utuh tepat di batas
15. Rina membuat laporan rusak pada halaman Unassign untuk baris `Kamera Canon EOS {runId}` dengan satu foto dan Description `Layar retak di sudut kiri atas dan engsel terasa longgar saat perangkat dibuka Layar retak di sudut kiri atas dan engsel terasa longgar saat perangkat dibuka Layar retak di sudut kiri atas dan engsel terasa longgar saat perangkat dibuka Layar retak di sudut kiri atas dan engsel terasa longgar saat perangkat dibuka Layar retak di sudut kiri atas dan engsel ter` (361 karakter) pada DU-223-14
16. Verifikasi server menolak Description yang melebihi batas dengan pesan `Max. 360 characters` dan tidak ada laporan yang terbentuk

### Reason Mark as Unassigned melebihi batas ditolak server
17. Rina menjalankan `Mark as Unassigned` untuk baris `Tablet iPad {runId}` pada DU-223-15 dengan Reason `Penugasan diakhiri karena paket langganan turun dan fitur Assignment tidak tersedia Penugasan diakhiri karena paket langganan turun dan fitur Assignment tidak tersedia Penugasan diakhiri karena paket langganan turun dan fitur Assignment tidak tersedia Penugasan diakhiri karena paket langganan turun dan fitur Assignment tidak tersedia Penugasan diakhiri karen` (360 karakter) pada DU-223-16
18. Verifikasi aksi diterima dan Reason tersimpan utuh tepat di batas
19. Rina menjalankan `Mark as Unassigned` untuk baris `Tablet Samsung Tab {runId}` dengan Reason `Penugasan diakhiri karena paket langganan turun dan fitur Assignment tidak tersedia Penugasan diakhiri karena paket langganan turun dan fitur Assignment tidak tersedia Penugasan diakhiri karena paket langganan turun dan fitur Assignment tidak tersedia Penugasan diakhiri karena paket langganan turun dan fitur Assignment tidak tersedia Penugasan diakhiri karena` (361 karakter) pada DU-223-17
20. Verifikasi server menolak Reason yang melebihi batas dan baris `Tablet Samsung Tab {runId}` tetap `Assigned`
