---
id: TC-FA-FAREG-BE-136-koreksi-approver
title: "Koreksi approver: staged, validasi, dan penerapan"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-07d, FAREG-LOGIC-07e, FAREG-LOGIC-07i, FAREG-LOGIC-07j, "§9.4.2#r62", "§9.4.3#b7", "§9.6#r11", EB-CON-1]
smoke: []
dependsOn: []
owner: BE
trace:
  FAREG-LOGIC-07d: [3, 11, 12, 21]
  FAREG-LOGIC-07e: [17, 18]
  FAREG-LOGIC-07i: [24, 26, 28, 30, 32, 34]
  FAREG-LOGIC-07j: [2, 4, 9, 13, 22, 36, 38, 44, 45]
  "§9.4.2#r62": [8, 9]
  "§9.4.3#b7": [3, 21]
  "§9.6#r11": [6, 21]
  EB-CON-1: [8, 9, 42, 43]
---

# Koreksi approver: staged, validasi, dan penerapan

## Prerequisites
- Aktor:
  - Rina W (Manage asset & TAG, Group terkelola `Gudang Medan {runId}`) sebagai pengaju seluruh pengajuan.
  - Budi (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Medan {runId}`) sebagai approver.
  - Citra (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Medan {runId}`) sebagai approver lain pada pengajuan yang sama.
- Data:
  - DU-136-1: Group `Gudang Medan {runId}`, ber-toggle `Require Approval for Registration` ON, ada di entitas aktor.
  - DU-136-2: Asset Name `Laptop {runId}`, TAG Type `Non-TAG`, Status `Active`, dengan pasangan Brand dan Model `Dell` / `Latitude 5440`, `Lenovo` / `ThinkPad E14`, dan `HP` / `ProBook 450`, serta Custom field wajib `Nomor Inventaris` dengan Scope `General` dan Value Type `Specific` (nilai per aset).
  - DU-136-3: pengajuan `Waiting for Approval` milik Rina W berisi `2` aset `Laptop {runId}` Brand `Dell` Model `Latitude 5440` Condition `Normal`, Nomor Inventaris `INV-136-001 {runId}` dan `INV-136-002 {runId}`.
  - DU-136-4: pengajuan `Waiting for Approval` milik Rina W berisi `2` aset `Laptop {runId}` Brand `Dell` Model `Latitude 5440` Condition `Normal`.
  - DU-136-5: pengajuan `Waiting for Approval` milik Rina W berisi `3` aset `Laptop {runId}` Brand `Dell` Model `Latitude 5440`: aset pertama Condition `Normal` Nomor Inventaris `INV-136-011 {runId}`, aset kedua Condition `Normal`, aset ketiga Condition `Damaged` dengan Damage note `Casing retak di sisi kanan`.
  - DU-136-6: pengajuan `Waiting for Approval` milik Rina W berisi `2` aset `Laptop {runId}` Brand `Dell` Model `Latitude 5440` Condition `Normal`.
  - DU-136-17: pengajuan `Waiting for Approval` milik Rina W berisi `2` aset `Laptop {runId}` Brand `Dell` Model `Latitude 5440` Condition `Normal`.
  - DU-136-18: aset `Active` `Laptop {runId}` di Group `Gudang Medan {runId}`, Brand `Dell`, Model `Latitude 5440`, Alias Name `Laptop Staf {runId}`.
- Kondisi:
  - kuota Group `Gudang Medan {runId}` dan kuota tenant cukup untuk seluruh pengajuan di atas.

## Test Steps

### Koreksi staged tersimpan di server dan terlihat approver lain
1. Budi menyimpan koreksi Brand aset pertama pengajuan DU-136-3 dari `Dell` menjadi `Lenovo` dengan Model `ThinkPad E14`
2. Verifikasi koreksi aset pertama tersimpan staged di server per aset
3. Verifikasi Brand aset pertama pada data aset tetap `Dell` karena koreksi belum diterapkan sebelum Approve
4. Verifikasi Citra membaca koreksi Brand `Lenovo` pada aset pertama pengajuan yang sama
5. Budi menyimpan koreksi Brand aset pertama pengajuan DU-136-3 dengan nilai yang sama, `Lenovo` dengan Model `ThinkPad E14`
6. Verifikasi aset pertama hanya memiliki satu koreksi staged dengan Brand `Lenovo`

### Dua approver mengoreksi aset yang sama menerapkan last-write-wins
7. Citra menyimpan koreksi Brand aset pertama pengajuan DU-136-3 menjadi `HP` dengan Model `ProBook 450`
8. Verifikasi kedua penyimpanan koreksi sukses dan koreksi staged aset pertama bernilai `HP` dari penyimpanan terakhir, tanpa dialog konflik
9. Verifikasi Budi membaca koreksi staged `HP` pada aset pertama

### Approve menerapkan koreksi secara atomik
10. Budi mengirim keputusan `Approve` untuk kedua aset pengajuan DU-136-3
11. Verifikasi aset pertama berstatus `Active` dengan Brand `HP` dan Model `ProBook 450`
12. Verifikasi aset kedua berstatus `Active` dengan Brand `Dell` dan Model `Latitude 5440` karena tidak dikoreksi
13. Verifikasi Registration Log pengajuan memuat satu entri `Draft edited by Budi`

### Return to Draft dan Reject membuang seluruh koreksi
14. Budi menyimpan koreksi Brand aset pertama pengajuan DU-136-4 menjadi `Lenovo` dengan Model `ThinkPad E14`
15. Budi menyimpan koreksi Brand aset kedua pengajuan DU-136-4 menjadi `HP` dengan Model `ProBook 450`
16. Budi mengirim satu keputusan atas pengajuan DU-136-4: aset pertama `Return to Draft` dengan Reason `Foto aset belum jelas`, aset kedua `Reject` dengan Reason `Aset duplikat dengan pengajuan lain`
17. Verifikasi aset pertama kembali ke Draft dengan Brand `Dell` dan Model `Latitude 5440` tanpa koreksi
18. Verifikasi tidak ada koreksi staged yang tersisa untuk kedua aset pengajuan DU-136-4

### Koreksi tidak diterapkan bila keputusan ditolak
19. Budi menyimpan koreksi Brand aset pertama pengajuan DU-136-6 menjadi `Lenovo` dengan Model `ThinkPad E14`
20. Budi mengirim satu keputusan atas pengajuan DU-136-6: aset pertama `Approve`, aset kedua `Return to Draft` tanpa Reason
21. Verifikasi keputusan ditolak server dan Brand aset pertama pada data aset tetap `Dell` karena koreksi tidak diterapkan
22. Verifikasi koreksi staged aset pertama masih bernilai `Lenovo` dan terbaca oleh Citra

### Server menolak koreksi yang mengosongkan field Tingkat 2
23. Budi menyimpan koreksi Brand aset pertama pengajuan DU-136-5 menjadi kosong
24. Verifikasi koreksi ditolak server dan aset pertama tidak memiliki koreksi staged Brand
25. Budi menyimpan koreksi Custom field `Nomor Inventaris` aset pertama pengajuan DU-136-5 menjadi kosong
26. Verifikasi koreksi ditolak server dan Nomor Inventaris aset pertama tetap `INV-136-011 {runId}`
27. Budi menyimpan koreksi Condition aset kedua pengajuan DU-136-5 menjadi `Damaged` tanpa Damage note
28. Verifikasi koreksi ditolak server dengan pesan `Damage note must not be empty`
29. Budi menyimpan koreksi Condition aset kedua pengajuan DU-136-5 menjadi `Damaged` dengan Damage note `Layar retak di sudut kiri`
30. Verifikasi koreksi aset kedua diterima dan tersimpan staged dengan Condition `Damaged` serta Damage note `Layar retak di sudut kiri`
31. Budi menyimpan koreksi Condition aset ketiga pengajuan DU-136-5 menjadi `Normal`
32. Verifikasi koreksi staged aset ketiga bernilai Condition `Normal` tanpa Damage note
33. Budi menyimpan koreksi Brand aset pertama pengajuan DU-136-5 menjadi `Lenovo` tanpa Model
34. Verifikasi koreksi diterima dan tersimpan staged walau Model dikosongkan oleh koreksi Brand

### Pembatalan pengajuan membuang koreksi staged
35. Budi menyimpan koreksi Brand aset pertama pengajuan DU-136-17 menjadi `Lenovo` dengan Model `ThinkPad E14`
36. Verifikasi Citra membaca koreksi Brand `Lenovo` pada aset pertama pengajuan DU-136-17
37. Rina W membatalkan pengajuan DU-136-17
38. Verifikasi tidak ada koreksi staged yang tersisa untuk kedua aset pengajuan DU-136-17 sesudah pembatalan

### Dua user mengedit aset Active yang sama menerapkan last-write-wins
39. Budi dan Citra sama-sama membaca aset DU-136-18 dengan Alias Name `Laptop Staf {runId}`
40. Budi menyimpan Edit Active atas aset DU-136-18 dengan Alias Name `Laptop Budi {runId}`
41. Citra menyimpan Edit Active atas aset DU-136-18 dari keadaan yang ia baca sebelum Save Budi, dengan Alias Name `Laptop Citra {runId}`
42. Verifikasi kedua Save Edit Active diterima server tanpa penanda versi dan tanpa penolakan karena konflik
43. Verifikasi Alias Name aset DU-136-18 bernilai `Laptop Citra {runId}` dari Save yang terakhir diterima server

### Koreksi pada aset yang tidak disetujui tidak dicatat sebagai Draft edited by
44. Verifikasi Registration Log pengajuan DU-136-4 memuat node `Submitted by Rina W`
45. Verifikasi Registration Log pengajuan DU-136-4 tidak memuat node `Draft edited by Budi` karena koreksi Budi hanya ada pada aset yang dikembalikan ke Draft dan aset yang ditolak
