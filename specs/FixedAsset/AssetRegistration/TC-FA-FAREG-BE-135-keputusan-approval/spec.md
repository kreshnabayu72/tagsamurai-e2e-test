---
id: TC-FA-FAREG-BE-135-keputusan-approval
title: "Keputusan approval: status pengajuan, validasi, dan transaksi tunggal"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-06h, FAREG-LOGIC-06i, V-REG-14, V-REG-16, "§4.2.4#r1", "§4.2.4#r2", "§4.2.4#r3", "§4.2.4#b10", "§9.2#p11", "§9.4.2#r20", "§9.6#r4", "§9.9#r19", "§9.9#r21"]
smoke: []
dependsOn: []
owner: BE
trace:
  FAREG-LOGIC-06h: [3, 9, 15]
  FAREG-LOGIC-06i: [3, 17]
  V-REG-14: [29, 30, 33]
  V-REG-16: [19, 22]
  "§4.2.4#r1": [4, 5, 10]
  "§4.2.4#r2": [11, 12]
  "§4.2.4#r3": [12, 13]
  "§4.2.4#b10": [20, 26]
  "§9.2#p11": [9, 41]
  "§9.4.2#r20": [15]
  "§9.6#r4": [20, 35, 37, 39, 41]
  "§9.9#r19": [6, 19, 22, 24, 26]
  "§9.9#r21": [29]
---

# Keputusan approval: status pengajuan, validasi, dan transaksi tunggal

## Prerequisites
- Aktor:
  - Rina W (Manage asset & TAG, Group terkelola `Gudang Kota {runId}`) sebagai pengaju seluruh pengajuan.
  - Budi (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Kota {runId}`) sebagai approver.
  - Citra (Manage asset & TAG dengan capability Update pada node Group registrasi `Gudang Kota {runId}`) sebagai approver lain yang tidak bertindak kecuali disebut.
  - Agus P (Group Manager Group `Gudang Kota {runId}`).
- Data:
  - DU-135-1: Group `Gudang Kota {runId}`, ber-toggle `Require Approval for Registration` ON, ada di entitas aktor.
  - DU-135-2: Asset Name `Meja Kerja {runId}` dengan Brand `Olympic` Model `OL-135` dan Brand `Chitose` Model `Orion`, TAG Type `Non-TAG`, Status `Active`.
  - DU-135-3: Asset Name `Laptop {runId}`, Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID`, Status `Active`.
  - DU-135-4: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Kota {runId}` berisi `3` aset `Meja Kerja {runId}`.
  - DU-135-5: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Kota {runId}` berisi `3` aset `Laptop {runId}` ber-Tag `E280-1350-0001 {runId}`, `E280-1350-0002 {runId}`, dan `E280-1350-0003 {runId}`, urut sebagai aset pertama, kedua, dan ketiga.
  - DU-135-6: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Kota {runId}` berisi `2` aset `Meja Kerja {runId}`.
  - DU-135-7: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Kota {runId}` berisi `2` aset `Meja Kerja {runId}`.
  - DU-135-8: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Kota {runId}` berisi `3` aset `Meja Kerja {runId}`.
  - DU-135-9: pengajuan `Waiting for Approval` milik Rina W di Group `Gudang Kota {runId}` berisi `2` aset `Meja Kerja {runId}` Brand `Olympic` Model `OL-135`.
  - DU-135-10: pengajuan berstatus `Approved` di Group `Gudang Kota {runId}` berisi `2` aset.
  - DU-135-11: pengajuan berstatus `Partially Approved` di Group `Gudang Kota {runId}` berisi `2` aset.
  - DU-135-12: pengajuan berstatus `Rejected` di Group `Gudang Kota {runId}` berisi `2` aset.
  - DU-135-13: pengajuan berstatus `Canceled` di Group `Gudang Kota {runId}` berisi `2` aset.
- Kondisi:
  - kuota Group `Gudang Kota {runId}` dan kuota tenant cukup untuk seluruh pengajuan di atas.

## Test Steps

### Satu approver cukup dan semua Approve menjadi Approved
1. Catat jumlah slot Reserved dan Used Group `Gudang Kota {runId}`
2. Budi mengirim keputusan `Approve` tanpa Reason untuk ketiga aset pengajuan DU-135-4, sementara Citra tidak bertindak
3. Verifikasi pengajuan DU-135-4 berstatus `Approved` walau hanya satu approver yang bertindak
4. Verifikasi ketiga aset pengajuan DU-135-4 berstatus `Active`
5. Verifikasi slot Reserved Group berkurang `3` dan slot Used bertambah `3` dibanding catatan
6. Verifikasi keputusan `Approve` tanpa Reason diterima server

### Keputusan campuran menjadi Partially Approved
7. Catat jumlah slot Reserved dan Used Group `Gudang Kota {runId}`
8. Budi mengirim satu keputusan atas pengajuan DU-135-5: aset pertama `Approve`, aset kedua `Return to Draft` dengan Reason `Foto aset belum jelas`, aset ketiga `Reject` dengan Reason `Aset duplikat dengan pengajuan lain`
9. Verifikasi pengajuan DU-135-5 berstatus `Partially Approved`
10. Verifikasi aset pertama berstatus `Active`
11. Verifikasi aset kedua kembali sebagai batch Draft baru milik Rina W dengan alasan approver `Foto aset belum jelas`
12. Verifikasi slot Reserved Group berkurang `3` dan slot Used bertambah `1` dibanding catatan
13. Verifikasi aset ketiga dibuang, Tag `E280-1350-0003 {runId}` kembali `Available`, dan Asset Code aset ketiga berstatus `Voided`

### Tidak ada Approve menjadi Rejected
14. Budi mengirim satu keputusan atas pengajuan DU-135-6: aset pertama `Return to Draft` dengan Reason `Foto aset belum jelas`, aset kedua `Reject` dengan Reason `Aset duplikat dengan pengajuan lain`
15. Verifikasi pengajuan DU-135-6 berstatus `Rejected` karena tidak ada aset berkeputusan `Approve`

### Override Group Manager memutus langsung
16. Agus P mengirim keputusan `Reject` dengan Reason `Aset duplikat dengan pengajuan lain` untuk kedua aset pengajuan DU-135-7, sementara Budi dan Citra belum bertindak
17. Verifikasi pengajuan DU-135-7 langsung berstatus `Rejected` tanpa menunggu keputusan Budi dan Citra

### Reason wajib untuk Return to Draft dan Reject serta dibatasi 360 karakter
18. Budi mengirim satu keputusan atas pengajuan DU-135-8: aset pertama `Approve`, aset kedua `Return to Draft` tanpa Reason, aset ketiga `Approve`
19. Verifikasi keputusan ditolak server karena Reason aset kedua kosong
20. Verifikasi pengajuan DU-135-8 tetap `Waiting for Approval` dan tidak ada aset yang berubah, termasuk aset pertama dan ketiga yang tidak berstatus `Active`
21. Budi mengirim satu keputusan atas pengajuan DU-135-8: aset pertama `Approve`, aset kedua `Reject` tanpa Reason, aset ketiga `Approve`
22. Verifikasi keputusan ditolak server karena Reason aset kedua kosong
23. Budi mengirim satu keputusan atas pengajuan DU-135-8: aset pertama `Approve`, aset kedua `Return to Draft` dengan Reason `Aset ini perlu difoto ulang karena label serial tidak terbaca dan kondisi fisiknya belum cocok dengan catatan pengajuan. Aset ini perlu difoto ulang karena label serial tidak terbaca dan kondisi fisiknya belum cocok dengan catatan pengajuan. Aset ini perlu difoto ulang karena label serial tidak terbaca dan kondisi fisiknya belum cocok dengan catatan pengaju.x` (361 karakter), aset ketiga `Approve`
24. Verifikasi keputusan ditolak server karena Reason aset kedua melebihi 360 karakter
25. Budi mengirim satu keputusan atas pengajuan DU-135-8: aset pertama `Approve`, aset kedua `Return to Draft` dengan Reason `Aset ini perlu difoto ulang karena label serial tidak terbaca dan kondisi fisiknya belum cocok dengan catatan pengajuan. Aset ini perlu difoto ulang karena label serial tidak terbaca dan kondisi fisiknya belum cocok dengan catatan pengajuan. Aset ini perlu difoto ulang karena label serial tidak terbaca dan kondisi fisiknya belum cocok dengan catatan pengaju.` (360 karakter), aset ketiga `Approve`
26. Verifikasi keputusan diterima server dan pengajuan DU-135-8 berstatus `Partially Approved`

### Pilih ulang Model setelah koreksi Brand
27. Budi menyimpan koreksi Brand aset pertama pengajuan DU-135-9 dari `Olympic` menjadi `Chitose`, sehingga Model aset pertama dikosongkan
28. Budi mengirim keputusan `Approve` untuk kedua aset pengajuan DU-135-9 tanpa memilih ulang Model aset pertama
29. Verifikasi keputusan ditolak server dengan pesan `Select Model again` pada Model aset pertama
30. Verifikasi pengajuan DU-135-9 tetap `Waiting for Approval`
31. Budi menyimpan koreksi Model aset pertama pengajuan DU-135-9 menjadi `Orion`
32. Budi mengirim keputusan `Approve` untuk kedua aset pengajuan DU-135-9
33. Verifikasi keputusan diterima server dan pengajuan DU-135-9 berstatus `Approved`

### Keputusan atas pengajuan yang sudah diputuskan atau dibatalkan ditolak
34. Budi mengirim keputusan `Approve` untuk kedua aset pengajuan DU-135-10 yang sudah `Approved`
35. Verifikasi keputusan ditolak server dan pengajuan DU-135-10 tetap `Approved` tanpa perubahan pada aset dan kuota
36. Budi mengirim keputusan `Approve` untuk kedua aset pengajuan DU-135-11 yang sudah `Partially Approved`
37. Verifikasi keputusan ditolak server dan pengajuan DU-135-11 tetap `Partially Approved`
38. Budi mengirim keputusan `Approve` untuk kedua aset pengajuan DU-135-12 yang sudah `Rejected`
39. Verifikasi keputusan ditolak server dan pengajuan DU-135-12 tetap `Rejected`
40. Budi mengirim keputusan `Approve` untuk kedua aset pengajuan DU-135-13 yang sudah `Canceled`
41. Verifikasi keputusan ditolak server dan pengajuan DU-135-13 tetap `Canceled`
