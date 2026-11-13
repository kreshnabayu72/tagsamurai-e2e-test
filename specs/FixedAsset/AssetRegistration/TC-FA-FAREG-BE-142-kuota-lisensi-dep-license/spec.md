---
id: TC-FA-FAREG-BE-142-kuota-lisensi-dep-license
title: "Kuota lisensi: Reserved, Used, dan perebutan slot terakhir"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-05a, FAREG-LOGIC-05b, FAREG-LOGIC-05c, FAREG-LOGIC-05d, FAREG-LOGIC-05e, FAREG-LOGIC-05f, FAREG-LOGIC-05h, FAREG-LOGIC-05j, FAREG-LOGIC-05l, "§9.4.2#r10", "§9.4.3#b5", "§9.4.3#b6", EB-CON-4]
smoke: []
dependsOn:
  - "License: kuota Group dan tenant"
owner: BE
trace:
  FAREG-LOGIC-05a: [3, 14, 19]
  FAREG-LOGIC-05b: [3, 4]
  FAREG-LOGIC-05c: [14, 15]
  FAREG-LOGIC-05d: [6, 11]
  FAREG-LOGIC-05e: [27, 29, 31]
  FAREG-LOGIC-05f: 24
  FAREG-LOGIC-05h: [4, 20, 35]
  FAREG-LOGIC-05j: [19, 20]
  FAREG-LOGIC-05l: 16
  "§9.4.2#r10": [34, 35]
  "§9.4.3#b5": 24
  "§9.4.3#b6": 11
  EB-CON-4: [34, 35]
---

# Kuota lisensi: Reserved, Used, dan perebutan slot terakhir

## Prerequisites
- Aktor:
  - Rina W (Manage asset & TAG, Group terkelola `Gudang Kuota A {runId}` sampai `Gudang Kuota F {runId}`) sebagai pengaju.
  - Lina (Manage asset & TAG, Group terkelola `Gudang Kuota D {runId}`).
  - Budi (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Kuota A {runId}` sampai `Gudang Kuota F {runId}`) sebagai approver.
  - Hana T (Total Control, termasuk akses mengubah kuota Group di License).
- Data:
  - DU-142-1: Group `Gudang Kuota A {runId}`, ber-toggle `Require Approval for Registration` ON, kuota Group `10`, slot terpakai `0`.
  - DU-142-2: Group `Gudang Kuota B {runId}`, ber-toggle `Require Approval for Registration` OFF, kuota Group `10`, slot terpakai `0`.
  - DU-142-3: Group `Gudang Kuota C {runId}`, ber-toggle `Require Approval for Registration` OFF, kuota Group `10`, slot terpakai `0`.
  - DU-142-4: Group `Gudang Kuota D {runId}`, ber-toggle `Require Approval for Registration` OFF, kuota Group `10`, slot terpakai `9`.
  - DU-142-5: Group `Gudang Kuota E {runId}`, ber-toggle `Require Approval for Registration` ON, kuota Group `10`, slot terpakai `0`.
  - DU-142-6: Group `Gudang Kuota F {runId}`, ber-toggle `Require Approval for Registration` ON, kuota Group `10`, slot terpakai `0`.
  - DU-142-7: Asset Name `Meja Kerja {runId}`, Brand `Olympic`, Model `OL-142`, TAG Type `Non-TAG`, Status `Active`.
  - DU-142-8: batch Draft milik Rina W di Group `Gudang Kuota A {runId}`, Item `Meja Kerja {runId}` Quantity `9`, memenuhi Tingkat 2.
  - DU-142-9: batch Draft milik Rina W di Group `Gudang Kuota B {runId}`, Item `Meja Kerja {runId}` Quantity `10`, memenuhi Tingkat 2; aset kesepuluh Condition `Damaged` dengan Damage note `Layar retak di sudut kiri`.
  - DU-142-10: batch Draft milik Rina W di Group `Gudang Kuota C {runId}`, Item `Meja Kerja {runId}` Quantity `11`, memenuhi Tingkat 2.
  - DU-142-11: batch Draft milik Rina W di Group `Gudang Kuota D {runId}`, Item `Meja Kerja {runId}` Quantity `1`, memenuhi Tingkat 2.
  - DU-142-12: batch Draft milik Lina di Group `Gudang Kuota D {runId}`, Item `Meja Kerja {runId}` Quantity `1`, memenuhi Tingkat 2.
  - DU-142-13: batch Draft milik Rina W di Group `Gudang Kuota E {runId}`, Item `Meja Kerja {runId}` Quantity `6`, memenuhi Tingkat 2.
  - DU-142-14: batch Draft milik Rina W di Group `Gudang Kuota A {runId}`, Item `Meja Kerja {runId}` Quantity `5`.
  - DU-142-15: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Kuota F {runId}` berisi `2` aset `Meja Kerja {runId}`, slot kuotanya Reserved.
  - DU-142-16: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Kuota F {runId}` berisi `2` aset `Meja Kerja {runId}`, slot kuotanya Reserved.
  - DU-142-17: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Kuota F {runId}` berisi `2` aset `Meja Kerja {runId}`, slot kuotanya Reserved.
- Kondisi:
  - kuota tenant cukup untuk seluruh aset di atas, sehingga hanya kuota Group yang menentukan hasil.

## Test Steps

### Approval ON: slot Reserved selama menunggu lalu Used saat Approve
1. Catat jumlah slot Reserved dan Used Group `Gudang Kuota A {runId}`
2. Rina W mengirim Submit for Approval atas batch DU-142-8 berisi `9` aset
3. Verifikasi pengajuan diterima karena `9` aset berada satu di bawah kuota Group `10`
4. Verifikasi slot Reserved Group bertambah `9` dan slot Used tidak berubah dibanding catatan
5. Budi mengirim keputusan `Approve` untuk kesembilan aset pengajuan dari batch DU-142-8
6. Verifikasi slot Reserved Group kembali ke jumlah pada catatan dan slot Used bertambah `9` dibanding catatan

### Approve tidak mengecek ulang kuota
7. Catat jumlah slot Reserved dan Used Group `Gudang Kuota E {runId}`
8. Rina W mengirim Submit for Approval atas batch DU-142-13 berisi `6` aset
9. Hana T menurunkan kuota Group `Gudang Kuota E {runId}` menjadi `4` di License
10. Budi mengirim keputusan `Approve` untuk keenam aset pengajuan dari batch DU-142-13
11. Verifikasi keputusan diterima server walau slot Used melebihi kuota Group yang sudah diturunkan, dan slot Used bertambah `6` dibanding catatan

### Approval OFF: langsung Used dan aset Damaged tetap dihitung Used
12. Catat jumlah slot Reserved dan Used Group `Gudang Kuota B {runId}`
13. Rina W mengirim Activate atas batch DU-142-9 berisi `10` aset, tepat sebesar kuota Group
14. Verifikasi Activate diterima server dan kesepuluh aset berstatus `Active`
15. Verifikasi slot Used Group bertambah `10` dan slot Reserved tidak berubah dibanding catatan
16. Verifikasi aset kesepuluh ber-Condition `Damaged` termasuk dalam `10` slot Used seperti aset Active lain

### Kuota terlampaui menolak seluruh pengajuan
17. Catat jumlah slot Reserved dan Used Group `Gudang Kuota C {runId}`
18. Rina W mengirim Activate atas batch DU-142-10 berisi `11` aset, satu di atas kuota Group
19. Verifikasi Activate ditolak seluruhnya karena kuota dievaluasi atas total `11` aset dalam satu pengajuan
20. Verifikasi tidak ada aset yang diproses sebagian: seluruh aset batch tetap Draft dan slot Reserved serta Used Group sama dengan catatan

### Draft tidak menyentuh kuota
21. Catat jumlah slot Reserved dan Used Group `Gudang Kuota A {runId}`
22. Rina W menyimpan batch DU-142-14 dengan Quantity `6`
23. Rina W menghapus batch DU-142-14
24. Verifikasi slot Reserved dan Used Group sama dengan catatan setelah Save dan Delete draft

### Return, Reject, Cancel, dan auto-cancel melepas Reserved
25. Catat jumlah slot Reserved dan Used Group `Gudang Kuota F {runId}`
26. Budi mengirim satu keputusan atas pengajuan DU-142-15: aset pertama `Return to Draft` dengan Reason `Foto aset belum jelas`, aset kedua `Reject` dengan Reason `Aset duplikat dengan pengajuan lain`
27. Verifikasi slot Reserved Group berkurang `2` dan slot Used tidak berubah dibanding catatan
28. Rina W membatalkan pengajuan DU-142-16
29. Verifikasi slot Reserved Group berkurang `4` dibanding catatan awal grup ini dan slot Used tidak berubah
30. Waktu berlalu sampai Approval Timeout platform terlampaui sejak pengajuan DU-142-17 diajukan
31. Verifikasi slot Reserved Group berkurang `6` dibanding catatan awal grup ini dan slot Used tidak berubah

### Dua aktor berebut slot terakhir
32. Catat jumlah slot Used Group `Gudang Kuota D {runId}`
33. Rina W dan Lina mengirim Activate pada saat yang sama, Rina W atas batch DU-142-11 dan Lina atas batch DU-142-12, sementara Group `Gudang Kuota D {runId}` hanya menyisakan `1` slot
34. Verifikasi tepat satu Activate diterima server dan yang lain ditolak karena kuota
35. Verifikasi slot Used Group bertambah `1` dibanding catatan sehingga tidak melebihi kuota Group `10`
