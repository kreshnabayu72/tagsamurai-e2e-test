---
id: TC-FA-FATR-E2E-042-efek-transfer-dep-transfer
title: "Setting Transfer berlaku pada transaksi Transfer"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceRules: ["§9.2#b166", "§9.4.2#r123", "§9.7#r28", "EB-XM-2@transfer", "§9.2#b277", "§9.2#p28", "§9.4.2#r61", "§9.4.2#r62"]
smoke: ["§9.2#b277", "§9.2#p28", "§9.4.2#r61", "§9.4.2#r62"]
dependsOn:
  - "Transfer: pengajuan, Send, dan Receive"
trace:
  "§9.2#b166": 48
  "§9.4.2#r123": [29, 31]
  "§9.7#r28": 37
  "EB-XM-2@transfer": [48, 55, 62]
  "§9.2#b277": [34, 35]
  "§9.2#p28": [21, 25]
  "§9.4.2#r61": [4, 9, 11]
  "§9.4.2#r62": 17
anchor: [7, 40]
coverage:
  web: automated
---

# Setting Transfer berlaku pada transaksi Transfer

## Prerequisites
- Aktor: Default User yang memegang Manage transaction settings (Update); aktor lain yang masuk sebagai pengguna: `Tika Maharani {runId}`, `Bambang Setiawan {runId}`, `Citra Dewanti {runId}`.
- Layar awal: Fixed Asset > Transfer.
- Data:
  - DU-042-1: Group Name `Operations {runId}`; Group induk.
  - DU-042-2: Group Name `Plant North {runId}`, Parent `Operations {runId}`; Group dengan induk langsung Operations.
  - DU-042-3: Group Name `Plant South {runId}`, Parent `Operations {runId}`; Group dengan induk langsung Operations.
  - DU-042-4: Group Name `Plant East {runId}`, Group quota `1`; Group dengan kuota 1 yang sudah terpakai.
  - DU-042-5: Category Name `Production Machinery {runId}`, Allow Transfer `Allow`; Category leaf dengan Allow Transfer nilai sendiri.
  - DU-042-6: User Name `Tika Maharani {runId}`, Role `Employee`, Group `Plant North {runId}`; akun aktif.
  - DU-042-7: User Name `Bambang Setiawan {runId}`, Role `Employee`, Group `Plant North {runId}`, Role Transaksi `Approver`; akun aktif.
  - DU-042-8: User Name `Citra Dewanti {runId}`, Role `Employee`, Group `Plant South {runId}`, Role Transaksi `Approver`; akun aktif.
  - DU-042-9: Asset Name `Furnace FN05 {runId}`, Category `Production Machinery {runId}`, Group `Plant East {runId}`, Status `Available`; aset yang menempati kuota Group tujuan.
  - DU-042-10: Asset Name `Lathe Machine LM300 {runId}`, Category `Production Machinery {runId}`, Group `Plant North {runId}`, Status `Available`; aset.
  - DU-042-11: Asset Name `Milling Machine MM450 {runId}`, Category `Production Machinery {runId}`, Group `Plant North {runId}`, Status `Available`; aset.
  - DU-042-12: Asset Name `Packing Line PL20 {runId}`, Category `Production Machinery {runId}`, Group `Plant North {runId}`, Status `Available`; aset.
  - DU-042-13: Asset Name `Boiler BL15 {runId}`, Category `Production Machinery {runId}`, Group `Plant North {runId}`, Status `Waiting for Approval`; aset.
  - DU-042-14: Asset Name `Air Dryer AD40 {runId}`, Category `Production Machinery {runId}`, Group `Plant North {runId}`, Status `Available, kondisi Damaged`; aset berkondisi Damaged.
  - DU-042-15: Asset Name `Conveyor CV90 {runId}`, Category `Production Machinery {runId}`, Group `Plant North {runId}`, Status `Waiting for Approval`; aset.
  - DU-042-16: Asset Name `Press Brake PB60 {runId}`, Category `Production Machinery {runId}`, Group `Plant North {runId}`, Status `Waiting for Send`; aset.
  - DU-042-17: Asset Name `Cooling Tower CT10 {runId}`, Category `Production Machinery {runId}`, Group `Plant North {runId}`, Status `Available`; aset.
  - DU-042-18: Override Target `Lathe Machine LM300 {runId}`, Scope `Asset`, Transaction `Transfer`, Destination quota check `ON`; override Asset untuk Transfer.
  - DU-042-19: Override Target `Milling Machine MM450 {runId}`, Scope `Asset`, Transaction `Transfer`, Destination quota check `ON`; override Asset untuk Transfer.
  - DU-042-20: Override Target `Packing Line PL20 {runId}`, Scope `Asset`, Transaction `Transfer`, Require approval `ON`, Auto-approve `ON`, Auto-approve when destination in same parent Group `ON`; override Asset untuk Transfer.
  - DU-042-21: Override Target `Boiler BL15 {runId}`, Scope `Asset`, Transaction `Transfer`, Require approval `ON`, Auto-approve `OFF`, Approval scope `Both`; override Asset untuk Transfer.
  - DU-042-22: Transfer Asset `Boiler BL15 {runId}`, Requester `Tika Maharani {runId}`, From `Plant North {runId}`, To `Plant South {runId}`, Status `Waiting for Approval`; pengajuan menunggu approval kedua sisi.
  - DU-042-23: Transfer Asset `Conveyor CV90 {runId}`, Requester `Tika Maharani {runId}`, From `Plant North {runId}`, To `Plant South {runId}`, Status `Waiting for Approval`, Diajukan `T0 − 30 hari`; pengajuan yang sudah melewati batas Transaction timeout.
  - DU-042-24: Transfer Asset `Press Brake PB60 {runId}`, Requester `Tika Maharani {runId}`, From `Plant North {runId}`, To `Plant South {runId}`, Status `Waiting for Send`, Disetujui `T0 − 30 hari`; pengajuan yang sudah melewati batas Transaction timeout.
  - DU-042-25: Override Target `Conveyor CV90 {runId}`, Scope `Asset`, Transaction `Transfer`, Require approval `ON`, Auto-approve `OFF`; override Asset untuk Transfer yang membuat pengajuan Transfer aset itu menunggu approval.
- Kondisi:
  - Akun semua aktor di atas aktif dan kredensialnya tersedia untuk login.
  - Alokasi kuota per Group aktif, dan Group `Plant East {runId}` berkuota `1` dengan aset `Furnace FN05 {runId}` sudah menempati kuota itu.
  - Role Transaksi `Approver` untuk Group `Plant North {runId}` hanya dipegang `Bambang Setiawan {runId}`, dan untuk Group `Plant South {runId}` hanya dipegang `Citra Dewanti {runId}`.
  - Pengajuan Transfer aset `Conveyor CV90 {runId}` dan `Press Brake PB60 {runId}` sudah melewati batas Transaction timeout statusnya masing-masing.

## Test Steps
### Submit Transfer ke Group tujuan yang kuotanya terlampaui diblokir seluruhnya
1. Mulai pengajuan Transfer baru untuk aset `Lathe Machine LM300 {runId}` dan `Milling Machine MM450 {runId}`
2. Pilih Group tujuan `Plant East {runId}`
3. Klik `[Submit]`
4. Verifikasi Submit diblokir seluruhnya karena kuota Group tujuan `Plant East {runId}` terlampaui
5. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
6. Ketik Search `Boiler BL15 {runId}`, tekan Enter
7. Verifikasi pengajuan Transfer aset `Boiler BL15 {runId}` berstatus `Waiting for Approval`
8. Ganti isi kotak search dengan `Lathe Machine LM300 {runId}`, tekan Enter
9. Verifikasi tidak ada pengajuan Transfer untuk aset `Lathe Machine LM300 {runId}`
10. Ganti isi kotak search dengan `Milling Machine MM450 {runId}`, tekan Enter
11. Verifikasi tidak ada pengajuan Transfer untuk aset `Milling Machine MM450 {runId}`
12. Klik `(←)` pada kotak Search

### Auto-approve melewati approval bila Group tujuan berinduk langsung sama
13. Masuk sebagai `Tika Maharani {runId}`
14. Mulai pengajuan Transfer baru untuk aset `Packing Line PL20 {runId}`
15. Pilih Group tujuan `Plant South {runId}`
16. Klik `[Submit]`
17. Verifikasi pengajuan Transfer aset `Packing Line PL20 {runId}` langsung `Approved` tanpa permintaan approval di sisi asal maupun sisi tujuan

### Approval scope Both menyetujui Transfer hanya bila kedua sisi menyetujui
18. Masuk sebagai `Bambang Setiawan {runId}`
19. Buka permintaan approval Transfer aset `Boiler BL15 {runId}`
20. Setujui permintaan approval sisi asal
21. Verifikasi pengajuan Transfer aset `Boiler BL15 {runId}` masih `Waiting for Approval` karena sisi tujuan belum menyetujui
22. Masuk sebagai `Citra Dewanti {runId}`
23. Buka permintaan approval Transfer aset `Boiler BL15 {runId}`
24. Setujui permintaan approval sisi tujuan
25. Verifikasi pengajuan Transfer aset `Boiler BL15 {runId}` `Approved` karena kedua sisi menyetujui

### Aset yang kondisinya rusak dapat di-Transfer dengan peringatan
26. Masuk sebagai Default User
27. Mulai pengajuan Transfer baru untuk aset `Air Dryer AD40 {runId}`
28. Pilih Group tujuan `Plant South {runId}`
29. Verifikasi peringatan tampil karena kondisi aset `Air Dryer AD40 {runId}`
30. Klik `[Submit]`
31. Verifikasi pengajuan Transfer aset `Air Dryer AD40 {runId}` dibuat dan tidak diblokir

### Transaksi yang melewati Transaction timeout berakhir Canceled oleh System
32. Job Transaction timeout berjalan
33. Buka daftar Transfer
34. Verifikasi pengajuan Transfer aset `Conveyor CV90 {runId}` yang menunggu approval berstatus `Canceled` oleh `System` dengan alasan `Timed out (Waiting for Approval)`
35. Verifikasi pengajuan Transfer aset `Press Brake PB60 {runId}` yang menunggu kirim berstatus `Canceled` oleh `System` dengan alasan `Not sent`, dan bukan `Expired`
36. Buka detail pengajuan Transfer aset `Conveyor CV90 {runId}` di daftar Transfer
37. Verifikasi daftar dan detail transaksi Transfer aset `Conveyor CV90 {runId}` sama-sama menampilkan status `Canceled`

### Override Allow Transfer Deny dan penghapusannya tercermin di Transfer
38. Buka Fixed Asset > Transfer
39. Ketik Search `Cooling Tower CT10 {runId}` pada daftar aset di Fixed Asset > Transfer, tekan Enter
40. Verifikasi aksi Transfer pada baris aset `Cooling Tower CT10 {runId}` aktif
41. Buka tab Transfer pada node Category `Production Machinery {runId}` di Fixed Asset > Settings > Transaction Settings
42. Klik `[+ Override]` pada bagian Overrides
43. Isi Scope `Asset` dengan Target `Cooling Tower CT10 {runId}`
44. Pilih Field `Allow Transfer` dengan Value `Deny`
45. Klik `[Submit]`
46. Buka Fixed Asset > Transfer
47. Ketik Search `Cooling Tower CT10 {runId}` pada daftar aset di Fixed Asset > Transfer, tekan Enter
48. Verifikasi aksi Transfer pada baris aset `Cooling Tower CT10 {runId}` disabled, dengan alasan dan kontak tersampaikan pada aksi itu
49. Buka tab Transfer pada node Category `Production Machinery {runId}` di Fixed Asset > Settings > Transaction Settings
50. Buka menu ⋯ pada baris override untuk `Cooling Tower CT10 {runId}`
51. Klik `Delete`
52. Klik `[Delete]` pada dialog Delete Override
53. Buka Fixed Asset > Transfer
54. Ketik Search `Cooling Tower CT10 {runId}` pada daftar aset di Fixed Asset > Transfer, tekan Enter
55. Verifikasi aksi Transfer pada baris aset `Cooling Tower CT10 {runId}` aktif lagi

### Perubahan nilai Category berlaku untuk pengajuan Transfer baru
56. Buka tab Transfer pada node Category `Production Machinery {runId}` di Fixed Asset > Settings > Transaction Settings
57. Pilih nilai `Deny` pada field Allow Transfer
58. Klik `[Save]`
59. Klik `[Save]` pada dialog Save Changes
60. Buka Fixed Asset > Transfer
61. Ketik Search `Cooling Tower CT10 {runId}` pada daftar aset di Fixed Asset > Transfer, tekan Enter
62. Verifikasi aksi Transfer pada baris aset `Cooling Tower CT10 {runId}` disabled sesuai nilai baru Category `Production Machinery {runId}`
