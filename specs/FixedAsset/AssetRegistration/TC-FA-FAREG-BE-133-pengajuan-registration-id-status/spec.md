---
id: TC-FA-FAREG-BE-133-pengajuan-registration-id-status
title: "Pengajuan: Registration ID, status aset, dan satu pengajuan terbuka"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-06a, FAREG-LOGIC-06b, "§9.2#r15", "§9.2#r16", "§10#b1"]
smoke: []
dependsOn: []
owner: BE
trace:
  FAREG-LOGIC-06a: [2, 3, 4, 7, 10, 18, 19, 20, 23]
  FAREG-LOGIC-06b: [14, 15]
  "§9.2#r15": [7, 8, 9, 12]
  "§9.2#r16": [5, 17]
  "§10#b1": [14, 15]
---

# Pengajuan: Registration ID, status aset, dan satu pengajuan terbuka

## Prerequisites
- Aktor: Rina W (Manage asset & TAG, Group terkelola `Gudang Bekasi {runId}` dan `Gudang Cikarang {runId}`) sebagai pengaju; Budi (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Cikarang {runId}`, bukan pengaju) sebagai approver.
- Data:
  - DU-133-1: Group `Gudang Bekasi {runId}`, ber-toggle `Require Approval for Registration` OFF, ada di entitas aktor.
  - DU-133-2: Group `Gudang Cikarang {runId}`, ber-toggle `Require Approval for Registration` ON, ada di entitas aktor.
  - DU-133-3: Asset Name `Meja Kerja {runId}`, Brand `Olympic`, Model `OL-133`, TAG Type `Non-TAG`, Status `Active`.
  - DU-133-4: batch Draft milik Rina W di Group `Gudang Bekasi {runId}`, Item Asset Name `Meja Kerja {runId}`, Brand `Olympic`, Model `OL-133`, Quantity `3`, Condition `Normal`; seluruh aset memenuhi Tingkat 2.
  - DU-133-5: batch Draft milik Rina W di Group `Gudang Cikarang {runId}`, Item Asset Name `Meja Kerja {runId}`, Brand `Olympic`, Model `OL-133`, Quantity `2`, Condition `Normal`; seluruh aset memenuhi Tingkat 2.
  - DU-133-7: batch Draft milik Rina W di Group `Gudang Bekasi {runId}`, Item Asset Name `Meja Kerja {runId}`, Brand `Olympic`, Model `OL-133`, Quantity `1`, Condition `Normal`; seluruh aset memenuhi Tingkat 2.
- Kondisi:
  - kuota Group `Gudang Bekasi {runId}` dan `Gudang Cikarang {runId}` cukup untuk seluruh aset yang diaktifkan.

## Test Steps

### Activate tanpa Approval Workflow membentuk pengajuan ber-Registration ID
1. Rina W mengirim Activate atas batch Draft Group `Gudang Bekasi {runId}` berisi `3` aset
2. Verifikasi Activate membentuk satu pengajuan yang berisi `3` aset
3. Verifikasi pengajuan itu mendapat Registration ID berformat `REG-YYYYMMDD-NNNNN`
4. Verifikasi bagian `YYYYMMDD` pada Registration ID adalah tanggal Activate menurut waktu server
5. Verifikasi ketiga aset pengajuan itu berstatus `Active`

### Submit dengan Approval Workflow membentuk pengajuan Waiting for Approval
6. Rina W mengirim Submit for Approval atas batch Draft Group `Gudang Cikarang {runId}` berisi `2` aset
7. Verifikasi pengajuan baru berstatus `Waiting for Approval` dan berisi `2` aset
8. Verifikasi pengajuan itu terbentuk dari batch dengan Approval Workflow ON, Tingkat 2 lengkap, tanpa error, dan kuota lolos
9. Verifikasi pengaju pengajuan itu adalah `Rina W`
10. Verifikasi Registration ID pengajuan itu berformat `REG-YYYYMMDD-NNNNN` dan berbeda dari Registration ID pengajuan Group `Gudang Bekasi {runId}`
11. Rina W mengubah Alias Name salah satu aset pada pengajuan itu menjadi `Meja Rapat {runId}`
12. Verifikasi perubahan itu ditolak dan Alias Name aset tidak berubah karena field aset terkunci bagi pengaju selama pengajuan Waiting for Approval

### Satu aset hanya berada di satu pengajuan terbuka
13. Rina W mengirim Submit for Approval sekali lagi atas batch yang sama, Group `Gudang Cikarang {runId}`
14. Verifikasi Submit kedua ditolak tanpa membentuk pengajuan baru
15. Verifikasi jumlah pengajuan terbuka yang memuat aset batch Group `Gudang Cikarang {runId}` tetap `1`

### Approval terakhir mengaktifkan aset
16. Budi memutuskan `Approve` untuk kedua aset pengajuan Group `Gudang Cikarang {runId}`
17. Verifikasi kedua aset pengajuan itu berstatus `Active` setelah approval terakhir

### Nomor urut Registration ID berurutan pada hari yang sama
18. Verifikasi bagian `NNNNN` Registration ID pengajuan Group `Gudang Bekasi {runId}` terdiri dari 5 digit dengan angka nol di depan
19. Verifikasi bagian `NNNNN` Registration ID pengajuan Group `Gudang Cikarang {runId}` terdiri dari 5 digit dengan angka nol di depan
20. Verifikasi bagian `NNNNN` pengajuan Group `Gudang Cikarang {runId}`, yang dibentuk sesudah pengajuan Group `Gudang Bekasi {runId}` pada tanggal server yang sama, lebih besar daripada bagian `NNNNN` pengajuan Group `Gudang Bekasi {runId}`

### Nomor urut Registration ID kembali ke 00001 pada tanggal server baru
21. Tanggal server berganti ke tanggal baru dan belum ada pengajuan registrasi yang terbentuk pada tanggal itu
22. Rina W mengirim Activate atas batch Draft Group `Gudang Bekasi {runId}` berisi `1` aset
23. Verifikasi bagian `NNNNN` Registration ID pengajuan itu adalah `00001`
