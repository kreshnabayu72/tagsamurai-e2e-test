---
id: TC-FA-FAREG-BE-137-cancel-dan-auto-cancel
title: "Cancel registration dan auto-cancel sistem"
layer: be-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: [F-FAREG-08.k1, FAREG-LOGIC-05k, "§8.3#r6", "§9.4.2#r19", "§9.6#r5", "§9.7#r18"]
smoke: []
dependsOn: []
owner: BE
trace:
  F-FAREG-08.k1: [3, 4, 15]
  FAREG-LOGIC-05k: [4, 5, 6, 7, 8, 9, 15, 16]
  "§8.3#r6": [9, 10, 16, 17]
  "§9.4.2#r19": [3, 4, 6, 7, 12, 15]
  "§9.6#r5": [8, 20, 22, 24, 26]
  "§9.7#r18": [3, 4, 8, 9, 13]
---

# Cancel registration dan auto-cancel sistem

## Prerequisites
- Aktor:
  - Rina W (Manage asset & TAG, Group terkelola `Gudang Bogor {runId}`) sebagai pengaju seluruh pengajuan.
  - Budi (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Bogor {runId}`) sebagai approver.
  - Operator Admin Console yang mengubah plan entitas aktor.
- Data:
  - DU-137-1: Group `Gudang Bogor {runId}`, ber-toggle `Require Approval for Registration` ON, ada di entitas aktor.
  - DU-137-2: Asset Name `Laptop {runId}`, Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID`, Status `Active`.
  - DU-137-3: pengajuan `Waiting for Approval` milik Rina W berisi `2` aset `Laptop {runId}` ber-Tag `E280-1370-0001 {runId}` dan `E280-1370-0002 {runId}`, Tag berstatus `Reserved`.
  - DU-137-4: pengajuan `Waiting for Approval` milik Rina W berisi `2` aset `Laptop {runId}` ber-Tag `E280-1370-0003 {runId}` dan `E280-1370-0004 {runId}`, Tag berstatus `Reserved`.
  - DU-137-5: pengajuan `Waiting for Approval` milik Rina W berisi `2` aset `Laptop {runId}` ber-Tag `E280-1370-0005 {runId}` dan `E280-1370-0006 {runId}`.
  - DU-137-6: pengajuan `Waiting for Approval` milik Rina W berisi `2` aset `Laptop {runId}` ber-Tag `E280-1370-0007 {runId}` dan `E280-1370-0008 {runId}`.
  - DU-137-7: pengajuan berstatus `Approved` milik Rina W berisi `2` aset `Laptop {runId}`.
- Kondisi:
  - kuota Group `Gudang Bogor {runId}` dan kuota tenant cukup untuk seluruh pengajuan di atas.
  - Approval Timeout platform bernilai [N] hari dan background job pemeriksa timeout berjalan berkala.

## Test Steps

### Auto-cancel karena Approval Timeout
1. Catat jumlah slot Reserved Group `Gudang Bogor {runId}` serta Asset Code dan increment kedua aset pengajuan DU-137-3
2. Waktu berlalu sampai Approval Timeout platform terlampaui sejak pengajuan DU-137-3 diajukan
3. Verifikasi pengajuan DU-137-3 berstatus `Canceled` tanpa aktor manusia sebagai pembatalnya
4. Verifikasi kedua aset kembali ke Draft sebagai satu batch Draft baru milik Rina W dengan Origin berisi Registration ID pengajuan DU-137-3
5. Verifikasi Asset Code dan increment kedua aset sama dengan catatan
6. Verifikasi Tag `E280-1370-0001 {runId}` dan `E280-1370-0002 {runId}` tetap `Reserved`
7. Verifikasi batch Draft baru tidak memiliki Alert
8. Verifikasi slot Reserved Group berkurang `2` dibanding catatan
9. Verifikasi Registration Log pengajuan memuat node `Canceled by system (approval timeout — no decision within [N] days)` dengan [N] sama dengan nilai Approval Timeout dalam hari
10. Verifikasi node itu memuat dampak `Assets: Returned to Draft`
11. Budi mengirim keputusan `Approve` untuk kedua aset pengajuan DU-137-3
12. Verifikasi keputusan ditolak server dan pengajuan DU-137-3 tetap `Canceled`
13. Verifikasi pengajuan DU-137-3 tidak tampil di sub tab Waiting for Approval maupun di antrean Approvals tab Active, tampil di sub tab History berstatus `Canceled`, dan batch Draft baru tampil di sub tab Draft

### Auto-cancel karena plan kehilangan Approval Workflow
14. Operator Admin Console mengubah plan entitas aktor sehingga kehilangan Approval Workflow, sementara pengajuan DU-137-4 berstatus `Waiting for Approval`
15. Verifikasi pengajuan DU-137-4 berstatus `Canceled` dan kedua aset kembali ke Draft sebagai batch Draft baru milik Rina W dengan Origin berisi Registration ID pengajuan DU-137-4
16. Verifikasi Registration Log pengajuan memuat node `Canceled by system (plan changed)`
17. Verifikasi node itu memuat dampak `Assets: Returned to Draft`

### Cancel registration oleh pengaju
18. Catat jumlah slot Reserved Group `Gudang Bogor {runId}`
19. Rina W membatalkan pengajuan DU-137-5 dengan `Save as Draft to edit` tercentang
20. Verifikasi pengajuan DU-137-5 berstatus `Canceled`, kedua aset kembali ke Draft, dan slot Reserved berkurang `2` dibanding catatan dalam satu transaksi
21. Rina W membatalkan pengajuan DU-137-6 dengan `Save as Draft to edit` tidak tercentang
22. Verifikasi kedua aset pengajuan DU-137-6 dibuang dan slot Reserved berkurang `4` dibanding catatan
23. Rina W membatalkan pengajuan DU-137-5 sekali lagi
24. Verifikasi pembatalan ditolak karena pengajuan tidak lagi menunggu approval dan slot Reserved tidak berubah dibanding sebelum pembatalan kedua
25. Rina W membatalkan pengajuan DU-137-7 yang sudah `Approved`
26. Verifikasi pembatalan ditolak dan pengajuan DU-137-7 tetap `Approved`
