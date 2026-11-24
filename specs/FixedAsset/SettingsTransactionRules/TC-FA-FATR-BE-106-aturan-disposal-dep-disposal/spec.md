---
id: TC-FA-FATR-BE-106-aturan-disposal-dep-disposal
title: "Evaluasi dan penegakan aturan pada transaksi Disposal"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules:
  - "§Aturan Logika Modul#r6"
  - "§Aturan Logika Modul#r29"
  - "§4.1#r156"
  - "§4.1#r157"
  - "§4.1#r160"
  - "§4.1#r161"
  - "§4.1#r162"
  - "§4.1#r163"
  - "§4.1#r164"
  - "§4.1#r165"
  - "§9.2#b13"
  - "§9.2#b15"
  - "AU-BAGIAN-asampaiAU-BAGIAN-s,AU-NILAI-asampaiAU-NILAI-l,AU-TOOLTIP-asampaiAU-TOOLTIP-f"
  - "§9.2#b92"
  - "§9.2#b426"
  - "§9.2#b427"
  - "§9.2#b428"
  - "§9.2#b433"
  - "§9.2#b434"
  - "§9.2#b437"
  - "§9.2#b384"
  - "§9.2#b392"
  - "§9.2#b397"
  - "§9.2#b398"
  - "§9.2#b424"
  - "§9.4.2#r35"
  - "§9.4.2#r90"
  - "§9.4.2#r133"
  - "§9.4.2#r136"
  - "§9.4.3#b9"
  - "§9.7#r6"
  - "§9.7#r15"
  - "§9.8#r6"
  - "§9.8#r7"
  - "§11#r6"
  - "§9.2#b269"
  - "§4.1#r154"
  - "§4.1#r155"
  - "§Aturan Logika Modul#r5"
  - "§9.2#b423"
  - "F-FATR-10.p6d"
  - "F-FATR-10.p6e"
  - "F-FATR-10.p6f"
smoke: []
dependsOn:
  - "Disposal: pengajuan, approval, dan Execute"
owner: BE
trace:
  "F-FATR-10.p6d": [55, 56, 57, 58]
  "F-FATR-10.p6e": [59, 60]
  "F-FATR-10.p6f": [40, 42, 96, 97, 98, 99]
  "§Aturan Logika Modul#r6": 46
  "§Aturan Logika Modul#r29": 46
  "§4.1#r156": [8, 82, 84, 86]
  "§4.1#r157": [2, 5]
  "§4.1#r160": 3
  "§4.1#r161": [16, 19, 22, 25, 27, 28]
  "§4.1#r162": [19, 25, 30]
  "§4.1#r163": [16, 17, 20, 22, 23, 31]
  "§4.1#r164": [33, 36]
  "§4.1#r165": [34, 37]
  "§9.2#b13": 41
  "§9.2#b15": 44
  "AU-BAGIAN-asampaiAU-BAGIAN-s,AU-NILAI-asampaiAU-NILAI-l,AU-TOOLTIP-asampaiAU-TOOLTIP-f": [8, 10]
  "§9.2#b92": [50, 52, 54]
  "§9.2#b426": 56
  "§9.2#b427": 58
  "§9.2#b428": [42, 60]
  "§9.2#b433": [46, 48]
  "§9.2#b434": 47
  "§9.2#b437": 63
  "§9.2#b384": 47
  "§9.2#b392": [12, 14]
  "§9.2#b397": [2, 5, 12, 14, 82, 84, 86]
  "§9.2#b398": [8, 10]
  "§9.2#b424": 6
  "§9.4.2#r35": [46, 47]
  "§9.4.2#r90": 65
  "§9.4.2#r133": 39
  "§9.4.2#r136": 63
  "§9.4.3#b9": [87, 88, 89, 93, 94, 95]
  "§9.7#r6": 65
  "§9.7#r15": 68
  "§9.8#r6": 78
  "§9.8#r7": 80
  "§11#r6": [65, 77]
  "§9.2#b269": [77, 78, 79, 80]
  "§4.1#r154": [2, 3]
  "§4.1#r155": [16, 19]
  "§Aturan Logika Modul#r5": [65, 68, 92]
  "§9.2#b423": [69, 71, 73]
---

# Evaluasi dan penegakan aturan pada transaksi Disposal

## Prerequisites
- Aktor: Pengaju Disposal, yaitu user yang berhak mengajukan Disposal pada Group aset dan bukan Total Control maupun Group Manager. Aktor lain: Total Control, yang menyimpan perubahan setting dan menambahkan override pada Category `Mesin Produksi {runId}` dan asetnya, serta Aktor Disposal, yaitu user ber-Role Aktor Disposal dengan cakupan Group `Workshop {runId}`, yang melakukan Execute.
- Data:
  - DU-106-1: Group `Workshop {runId}`
  - DU-106-2: Group `Gudang Terbatas {runId}`, Group override Allow Disposal `Deny`
  - DU-106-3: Category `Alat Berat {runId}`, Allowed disposal types `Sell, Scrap, Donate, Trade-in`, Min asset age warning `12`, Max deviation from book value `30`, Allow Disposal `Allow`, Non TAG `Tidak`
  - DU-106-4: Category `Peralatan Proyek {runId}`, Allowed disposal types `Sell, Scrap, Donate, Trade-in`, Min asset age warning `12`, Max deviation from book value `30`, Allow Disposal `Allow`, Non TAG `Ya`
  - DU-106-5: Category `Mesin Produksi {runId}`, Allowed disposal types `Sell, Scrap, Donate, Trade-in`, Min asset age warning `12`, Min asset age warning setelah Save Changes `24`, Max deviation from book value `30`, Allow Disposal `Allow`, Non TAG `Tidak`
  - DU-106-6: Category `Kendaraan Dinas {runId}`, Allowed disposal types `Sell, Scrap, Donate, Trade-in`, Min asset age warning `12`, Max deviation from book value `30`, Allow Disposal `Deny`, Non TAG `Tidak`
  - DU-106-7: Asset `Excavator PC200 {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 6 bulan`, Register Date `T0 − 6 bulan`, Commercial book value `10.000.000`, Nilai jual yang diajukan `10.000.000`
  - DU-106-8: Asset `Excavator PC300 {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 18 bulan`, Register Date `T0 − 2 bulan`, Commercial book value `10.000.000`, Nilai jual yang diajukan `10.000.000`
  - DU-106-9: Asset `Bulldozer D31 {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `kosong`, Register Date `T0 − 3 bulan`, Commercial book value `10.000.000`
  - DU-106-10: Asset `Bulldozer D41 {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `kosong`, Register Date `T0 − 20 bulan`, Commercial book value `10.000.000`
  - DU-106-11: Asset `Crane RT50 {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 12 bulan` (tanggal kalender zona waktu client), Register Date `T0 − 12 bulan`, Commercial book value `10.000.000`
  - DU-106-12: Asset `Crane RT60 {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 12 bulan + 1 hari` (tanggal kalender zona waktu client), Register Date `T0 − 12 bulan + 1 hari`, Commercial book value `10.000.000`
  - DU-106-13: Asset `Compressor GA37 {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 30 bulan`, Register Date `T0 − 30 bulan`, Commercial book value `10.000.000`, Nilai jual yang diajukan `6.000.000`, Reason `Harga pasar turun`
  - DU-106-14: Asset `Genset 100kVA {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 30 bulan`, Register Date `T0 − 30 bulan`, Commercial book value `10.000.000`, Nilai jual yang diajukan `6.000.000`, Reason `Tukar tambah unit baru`
  - DU-106-15: Asset `Forklift FD18 {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 30 bulan`, Register Date `T0 − 30 bulan`, Commercial book value `10.000.000`
  - DU-106-16: Asset `Pompa Air P50 {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 30 bulan`, Register Date `T0 − 30 bulan`, Commercial book value `10.000.000`, Nilai jual yang diajukan `8.000.000`
  - DU-106-17: Asset `Mesin Bubut {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 30 bulan`, Register Date `T0 − 30 bulan`, Commercial book value `0`, Nilai jual yang diajukan `1.000.000`
  - DU-106-18: Asset `Lemari Besi {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 30 bulan`, Register Date `T0 − 30 bulan`, Commercial book value `tidak tersedia`, Nilai jual yang diajukan `1.000.000`
  - DU-106-19: Asset `Forklift FD25 {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Missing`, Purchase date `T0 − 30 bulan`, Register Date `T0 − 30 bulan`, Commercial book value `10.000.000`
  - DU-106-20: Asset `Forklift FD30 {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Missing`, Purchase date `T0 − 30 bulan`, Register Date `T0 − 30 bulan`, Commercial book value `10.000.000`
  - DU-106-21: Asset `Forklift FD35 {runId}`, Category `Kendaraan Dinas {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Missing`, Purchase date `T0 − 30 bulan`, Register Date `T0 − 30 bulan`, Commercial book value `10.000.000`
  - DU-106-22: Asset `Pickup L300 {runId}`, Category `Kendaraan Dinas {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 30 bulan`, Register Date `T0 − 30 bulan`, Commercial book value `10.000.000`
  - DU-106-23: Asset `Dump Truck HD465 {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 30 bulan`, Register Date `T0 − 30 bulan`, Commercial book value `10.000.000`, Asset override Allow Disposal `Deny`
  - DU-106-24: Asset `Dump Truck HD785 {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 30 bulan`, Register Date `T0 − 30 bulan`, Commercial book value `10.000.000`, Asset Name override Allow Disposal `Deny`, Asset override Allow Disposal `Allow`
  - DU-106-25: Asset `Dump Truck HD325 {runId}`, Category `Alat Berat {runId}`, Group `Gudang Terbatas {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 30 bulan`, Register Date `T0 − 30 bulan`, Commercial book value `10.000.000`, Asset override Allow Disposal `Allow`
  - DU-106-26: Asset `Excavator PC350 {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 30 bulan`, Register Date `T0 − 30 bulan`, Commercial book value `10.000.000`
  - DU-106-27: Asset `Tenda Proyek {runId}`, Category `Peralatan Proyek {runId}`, Group `Workshop {runId}`, Tag `Tidak ber-tag`, Condition `Active`, Purchase date `T0 − 30 bulan`, Register Date `T0 − 30 bulan`, Commercial book value `10.000.000`
  - DU-106-28: Asset `Mesin Press P1 {runId}`, Category `Mesin Produksi {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 18 bulan`, Register Date `T0 − 18 bulan`, Commercial book value `10.000.000`, Nilai jual yang diajukan `10.000.000`
  - DU-106-29: Asset `Mesin Press P2 {runId}`, Category `Mesin Produksi {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 18 bulan`, Register Date `T0 − 18 bulan`, Commercial book value `10.000.000`, Nilai jual yang diajukan `10.000.000`
  - DU-106-30: Asset `Mesin Press P3 {runId}`, Category `Mesin Produksi {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 8 bulan`, Register Date `T0 − 8 bulan`, Commercial book value `10.000.000`, Nilai jual yang diajukan `10.000.000`, Asset override Min asset age warning setelah Add override `6`
  - DU-106-37: Asset `Wheel Loader WL180 {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 6 bulan`, Register Date `T0 − 6 bulan`, Commercial book value `10.000.000`
  - DU-106-38: Asset `Backhoe BH75 {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 6 bulan`, Register Date `T0 − 6 bulan`, Commercial book value `10.000.000`, Nilai jual yang diajukan `10.000.000`
  - DU-106-40: Asset `Scaffolding SC12 {runId}`, Category `Peralatan Proyek {runId}`, Group `Workshop {runId}`, Tag `Tidak ber-tag`, Condition `Active`, Purchase date `T0 − 6 bulan`, Register Date `T0 − 6 bulan`, Commercial book value `10.000.000`
  - DU-106-41: Disposal `Mesin Tunggu Eksekusi {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Status `Waiting for Execution`, Masuk status sejak `T0`
  - DU-106-42: Category `Pompa Industri {runId}`, Allowed disposal types `Sell, Scrap, Donate, Trade-in`, Min asset age warning `12`, Max deviation from book value `30`, Allow Disposal `Allow`, Allow Disposal setelah Save Changes `Deny`, Non TAG `Tidak`
  - DU-106-43: Asset `Pompa Uji {runId}`, Category `Pompa Industri {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 30 bulan`, Register Date `T0 − 30 bulan`, Commercial book value `10.000.000`, Nilai jual yang diajukan `10.000.000`
  - DU-106-44: Disposal `Pompa Draft {runId}`, Category `Pompa Industri {runId}`, Group `Workshop {runId}`, Status `Draft`, Masuk status sejak `T0`
  - DU-106-45: Disposal Report `Pompa Laporan {runId}`, Category `Pompa Industri {runId}`, Group `Workshop {runId}`, Status `Reported`, Masuk status sejak `T0`
  - DU-106-46: Disposal `Pompa Eksekusi {runId}`, Category `Pompa Industri {runId}`, Group `Workshop {runId}`, Status `Executed menunggu posting`, Masuk status sejak `T0`
  - DU-106-47: Asset `Mesin Foto {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Tag `Ber-tag`, Condition `Active`, Purchase date `T0 − 30 bulan`, Register Date `T0 − 30 bulan`, Commercial book value `10.000.000`
  - DU-106-48: Disposal `Mesin Eksekusi Foto {runId}`, Category `Alat Berat {runId}`, Group `Workshop {runId}`, Status `Waiting for Execution`, Masuk status sejak `T0`
  - DU-106-49: User `Indra Pratama {runId}`, Role `Aktor Disposal`, Cakupan `Workshop {runId}`, Status `Aktif`; melakukan Execute pada langkah 57, 59, dan 98
- Kondisi:
  - Zona waktu client bernilai `Asia/Jakarta` (UTC+7), dan T0 adalah pukul `01:00` pada zona waktu itu, yaitu pukul `18:00` pada hari kalender sebelumnya menurut UTC. Purchase date dan Register Date ditulis sebagai tanggal kalender zona waktu client.
  - Transaction timeout Disposal bernilai `7` (days), nilai awal Company default.
  - Require approval Disposal tersimpan `ON` dengan Approval type `Any one approver`, dan setiap Group aset memiliki Approver eligible selain Pengaju.
  - Photo at start dan Photo at end bernilai `ON` di All categories, nilai default Company.

## Test Steps

### Peringatan umur aset dihitung sejak Purchase date dan tidak memblokir
1. Pengaju mengajukan Disposal jenis `Sell` atas `Excavator PC200 {runId}` dengan scan tag aset dan Nilai jual `10.000.000`
2. Verifikasi evaluasi pengajuan memuat peringatan umur aset karena umur aset dari Purchase date kurang dari Min asset age warning `12` bulan kalender penuh
3. Verifikasi pengajuan tidak diblokir oleh peringatan umur aset dan diterima sebagai Disposal berstatus `Waiting for Approval`
4. Pengaju mengajukan Disposal jenis `Sell` atas `Excavator PC300 {runId}` dengan scan tag aset dan Nilai jual `10.000.000`, tanpa Evidence apa pun
5. Verifikasi evaluasi pengajuan tidak memuat peringatan umur aset karena umur dihitung dari Purchase date aset yang lebih dari `12` bulan kalender penuh, walaupun Register Date aset kurang dari `12` bulan
6. Verifikasi pengajuan diterima tanpa Evidence karena Disposal tidak memiliki setting Evidence

### Peringatan umur aset dari Register Date untuk Purchase date kosong dan untuk semua jenis Disposal
7. Pengaju mengajukan Disposal jenis `Donate` atas `Bulldozer D31 {runId}` dengan scan tag aset
8. Verifikasi evaluasi pengajuan memuat peringatan umur aset untuk jenis `Donate`, karena Purchase date kosong dan umur dihitung dari Register Date aset yang kurang dari `12` bulan kalender penuh
9. Pengaju mengajukan Disposal jenis `Donate` atas `Bulldozer D41 {runId}` dengan scan tag aset
10. Verifikasi evaluasi pengajuan tidak memuat peringatan umur aset karena umur dari Register Date aset lebih dari `12` bulan kalender penuh

### Batas bulan kalender penuh dihitung menurut zona waktu client
11. Pengaju mengajukan Disposal jenis `Donate` atas `Crane RT50 {runId}` dengan scan tag aset
12. Verifikasi evaluasi pengajuan tidak memuat peringatan umur aset karena umur aset tepat `12` bulan kalender penuh menurut tanggal kalender zona waktu client `Asia/Jakarta`, walaupun menurut tanggal kalender UTC umurnya kurang dari `12` bulan kalender penuh
13. Pengaju mengajukan Disposal jenis `Donate` atas `Crane RT60 {runId}` dengan scan tag aset
14. Verifikasi evaluasi pengajuan memuat peringatan umur aset karena umur aset kurang dari `12` bulan kalender penuh menurut tanggal kalender zona waktu client `Asia/Jakarta`

### Sell di bawah nilai buku Commercial melebihi batas deviasi mewajibkan alasan dan memunculkan peringatan
15. Pengaju mengajukan Disposal jenis `Sell` atas `Compressor GA37 {runId}` dengan scan tag aset dan Nilai jual `6.000.000`, tanpa Reason
16. Verifikasi pengajuan ditolak karena Reason wajib diisi: Nilai jual di bawah nilai buku Commercial `10.000.000` melebihi Max deviation from book value `30`%
17. Verifikasi aset `Compressor GA37 {runId}` tidak memiliki Disposal aktif baru dibanding sebelum pengajuan tanpa Reason
18. Pengaju mengajukan ulang Disposal jenis `Sell` atas `Compressor GA37 {runId}` dengan Nilai jual `6.000.000` dan Reason `Harga pasar turun`
19. Verifikasi evaluasi pengajuan memuat peringatan deviasi dari nilai buku Commercial
20. Verifikasi pengajuan dengan Reason diterima

### Trade-in di bawah nilai buku Commercial melebihi batas deviasi mewajibkan alasan dan memunculkan peringatan
21. Pengaju mengajukan Disposal jenis `Trade-in` atas `Genset 100kVA {runId}` dengan scan tag aset dan Nilai jual `6.000.000`, tanpa Reason
22. Verifikasi pengajuan ditolak karena Reason wajib diisi untuk deviasi dari nilai buku Commercial `10.000.000`
23. Verifikasi aset `Genset 100kVA {runId}` tidak memiliki Disposal aktif baru dibanding sebelum pengajuan tanpa Reason
24. Pengaju mengajukan ulang Disposal jenis `Trade-in` atas `Genset 100kVA {runId}` dengan Nilai jual `6.000.000` dan Reason `Tukar tambah unit baru`
25. Verifikasi evaluasi pengajuan memuat peringatan deviasi dari nilai buku Commercial

### Deviasi tidak berlaku untuk jenis lain dan tidak berlaku di dalam batas
26. Pengaju mengajukan Disposal jenis `Scrap` atas `Forklift FD18 {runId}` dengan scan tag aset
27. Verifikasi evaluasi pengajuan jenis `Scrap` tidak memuat peringatan deviasi dari nilai buku Commercial
28. Verifikasi pengajuan jenis `Scrap` diterima tanpa Reason
29. Pengaju mengajukan Disposal jenis `Sell` atas `Pompa Air P50 {runId}` dengan scan tag aset dan Nilai jual `8.000.000`, tanpa Reason
30. Verifikasi evaluasi pengajuan tidak memuat peringatan deviasi karena selisih dari nilai buku Commercial `10.000.000` tidak melebihi Max deviation from book value `30`%
31. Verifikasi pengajuan diterima tanpa Reason karena selisih tidak melebihi batas deviasi

### Nilai buku Commercial nol atau tidak tersedia tidak memunculkan peringatan dan tidak mewajibkan alasan
32. Pengaju mengajukan Disposal jenis `Sell` atas `Mesin Bubut {runId}` dengan scan tag aset dan Nilai jual `1.000.000`, tanpa Reason
33. Verifikasi evaluasi pengajuan tidak memuat peringatan deviasi karena nilai buku Commercial aset `0`
34. Verifikasi pengajuan diterima tanpa Reason karena nilai buku Commercial aset `0`
35. Pengaju mengajukan Disposal jenis `Sell` atas `Lemari Besi {runId}` dengan scan tag aset dan Nilai jual `1.000.000`, tanpa Reason
36. Verifikasi evaluasi pengajuan tidak memuat peringatan deviasi karena nilai buku Commercial aset `tidak tersedia`
37. Verifikasi pengajuan diterima tanpa Reason karena nilai buku Commercial aset `tidak tersedia`

### Aset berkondisi Missing hanya dapat di-Disposal jenis Write-off
38. Pengaju mengajukan Disposal jenis `Sell` atas `Forklift FD25 {runId}` dengan scan tag aset
39. Verifikasi pengajuan ditolak karena aset berkondisi `Missing` hanya dapat di-Disposal jenis `Write-off`
40. Pengaju mengajukan Disposal jenis `Write-off` atas `Forklift FD30 {runId}` tanpa scan tag aset
41. Verifikasi pengajuan jenis `Write-off` diterima walaupun `Write-off` tidak ada di Allowed disposal types efektif Category `Alat Berat {runId}`
42. Verifikasi pengajuan jenis `Write-off` tidak ditolak karena tanpa scan tag
43. Pengaju mengajukan Disposal jenis `Write-off` atas `Forklift FD35 {runId}` tanpa scan tag aset
44. Verifikasi pengajuan ditolak karena Allow Disposal bernilai Deny pada nilai efektif aset berkondisi `Missing`

### Deny pada Category dievaluasi ulang di server dan pesan blokir menyebut pihak kontak
45. Pengaju mengirim pengajuan Disposal jenis `Sell` atas `Pickup L300 {runId}` langsung ke server tanpa melalui UI
46. Verifikasi pengajuan ditolak server karena Allow Disposal bernilai Deny pada nilai efektif aset, apa pun keadaan UI
47. Verifikasi pesan penolakan menyebut siapa yang dapat dihubungi
48. Verifikasi aset `Pickup L300 {runId}` tidak memiliki Disposal aktif baru dibanding sebelum pengajuan

### Deny pada override Asset, Asset Name, atau Group mengalahkan nilai lain
49. Pengaju mengajukan Disposal jenis `Sell` atas `Dump Truck HD465 {runId}` dengan scan tag aset
50. Verifikasi pengajuan ditolak karena override pada aset bernilai Deny
51. Pengaju mengajukan Disposal jenis `Sell` atas `Dump Truck HD785 {runId}` dengan scan tag aset
52. Verifikasi pengajuan ditolak karena override Asset Name bernilai Deny walaupun override pada aset yang lebih dekat ke aset bernilai Allow
53. Pengaju mengajukan Disposal jenis `Sell` atas `Dump Truck HD325 {runId}` dengan scan tag aset
54. Verifikasi pengajuan ditolak karena override Group bernilai Deny walaupun override pada aset yang lebih dekat ke aset bernilai Allow

### Scan tag wajib saat Execute untuk aset ber-tag, identifikasi manual diizinkan saat Execute, dengan pengecualian Category Non TAG
55. Pengaju mengajukan Disposal jenis `Sell` atas `Excavator PC350 {runId}` tanpa scan tag aset
56. Verifikasi pengajuan diterima karena langkah mulai Disposal adalah Execute, bukan Request, sehingga scan tag tidak diminta saat Request
57. Aktor Disposal `Indra Pratama {runId}` melakukan Execute atas Disposal `Excavator PC350 {runId}` yang berstatus `Waiting for Execution` tanpa scan tag aset dan tanpa identifikasi manual
58. Verifikasi Execute ditolak karena scan tag wajib saat Execute untuk aset ber-tag
59. Aktor Disposal `Indra Pratama {runId}` melakukan Execute atas Disposal `Excavator PC350 {runId}` dengan mengidentifikasi aset secara manual
60. Verifikasi Execute diterima karena identifikasi manual diizinkan saat Execute (`tag.md` §9.12.3)

### Perubahan setting berlaku untuk transaksi baru dan tidak membatalkan transaksi berjalan
61. Pengaju mengajukan Disposal jenis `Sell` atas `Mesin Press P1 {runId}` dengan scan tag aset dan Nilai jual `10.000.000`, sehingga Disposal berstatus `Waiting for Approval`
62. Total Control mengubah Min asset age warning Category `Mesin Produksi {runId}` di tab Disposal menjadi `24`, lalu Save Changes
63. Verifikasi Disposal `Mesin Press P1 {runId}` tetap berstatus `Waiting for Approval` dan tidak dibatalkan otomatis walaupun umur asetnya kini kurang dari Min asset age warning `24`
64. Pengaju mengajukan Disposal jenis `Sell` atas `Mesin Press P2 {runId}` dengan scan tag aset dan Nilai jual `10.000.000`
65. Verifikasi evaluasi pengajuan baru memuat peringatan umur aset menurut Min asset age warning `24` yang baru disimpan
66. Total Control menambahkan override pada aset untuk `Mesin Press P3 {runId}` pada Category `Mesin Produksi {runId}` dengan Min asset age warning `6`
67. Pengaju mengajukan Disposal jenis `Sell` atas `Mesin Press P3 {runId}` dengan scan tag aset dan Nilai jual `10.000.000`
68. Verifikasi evaluasi pengajuan tidak memuat peringatan umur aset karena evaluasi memakai override pada aset `6`, bukan nilai Category `24`

### Photo at start dan Photo at end tidak berlaku untuk Disposal
69. Verifikasi Photo at start `ON` dan Photo at end `ON` tersimpan di All categories
70. Pengaju mengajukan Disposal jenis `Scrap` atas `Mesin Foto {runId}` dengan scan tag aset, tanpa foto
71. Verifikasi pengajuan diterima dan Disposal berstatus `Waiting for Approval` walaupun Photo at start bernilai `ON` di All categories, karena Disposal tidak memakai Photo at start
72. Aktor Disposal melakukan Execute atas Disposal `Mesin Eksekusi Foto {runId}` tanpa foto
73. Verifikasi Execute diterima dan Disposal menjadi `Executed` walaupun Photo at end bernilai `ON` di All categories, karena Disposal tidak memakai Photo at end

### Disposal Waiting for Approval dan Waiting for Execution yang melewati batas Transaction timeout dibatalkan System
74. Waktu berlalu sampai batas Transaction timeout `7` hari terlampaui sejak Disposal `Mesin Press P1 {runId}` masuk status `Waiting for Approval`
75. Waktu berlalu sampai batas Transaction timeout `7` hari terlampaui sejak Disposal `Mesin Tunggu Eksekusi {runId}` masuk status `Waiting for Execution`
76. Job Transaction timeout berjalan
77. Verifikasi Disposal `Mesin Press P1 {runId}` berstatus `Canceled`, bukan `Expired`, dengan Note `Timed out (Waiting for Approval)`
78. Verifikasi log transaksi Disposal `Mesin Press P1 {runId}` mencatat penutupan itu dengan Modified By `System`
79. Verifikasi Disposal `Mesin Tunggu Eksekusi {runId}` berstatus `Canceled`, bukan `Expired`, dengan Note `Timed out (Waiting for Execution)`
80. Verifikasi log transaksi Disposal `Mesin Tunggu Eksekusi {runId}` mencatat penutupan itu dengan Modified By `System`

### Peringatan umur aset berlaku untuk jenis Scrap, Trade-in, dan Write-off
81. Pengaju mengajukan Disposal jenis `Scrap` atas `Wheel Loader WL180 {runId}` dengan scan tag aset
82. Verifikasi evaluasi pengajuan jenis `Scrap` memuat peringatan umur aset karena umur aset dari Purchase date kurang dari Min asset age warning `12` bulan kalender penuh
83. Pengaju mengajukan Disposal jenis `Trade-in` atas `Backhoe BH75 {runId}` dengan scan tag aset dan Nilai jual `10.000.000`
84. Verifikasi evaluasi pengajuan jenis `Trade-in` memuat peringatan umur aset karena umur aset dari Purchase date kurang dari Min asset age warning `12` bulan kalender penuh
85. Pengaju mengajukan Disposal jenis `Write-off` atas `Scaffolding SC12 {runId}` tanpa scan tag aset
86. Verifikasi evaluasi pengajuan jenis `Write-off` memuat peringatan umur aset karena umur aset dari Purchase date kurang dari Min asset age warning `12` bulan kalender penuh

### Perubahan Allow Disposal tidak menutup otomatis Draft Disposal, Disposal Report, dan Disposal Executed menunggu posting
87. Verifikasi Draft Disposal `Pompa Draft {runId}` berstatus `Draft`
88. Verifikasi Disposal Report `Pompa Laporan {runId}` berstatus `Reported`
89. Verifikasi Disposal `Pompa Eksekusi {runId}` berstatus `Executed menunggu posting`
90. Total Control mengubah Allow Disposal Category `Pompa Industri {runId}` di tab Disposal menjadi `Deny`, lalu Save Changes
91. Pengaju mengajukan Disposal jenis `Sell` atas `Pompa Uji {runId}` dengan scan tag aset dan Nilai jual `10.000.000`
92. Verifikasi pengajuan ditolak karena Allow Disposal Category `Pompa Industri {runId}` kini bernilai `Deny`, sehingga perubahan Allow sudah berlaku untuk transaksi baru
93. Verifikasi Draft Disposal `Pompa Draft {runId}` tetap berstatus `Draft`, tidak ditutup otomatis
94. Verifikasi Disposal Report `Pompa Laporan {runId}` tetap berstatus `Reported`, tidak ditutup otomatis
95. Verifikasi Disposal `Pompa Eksekusi {runId}` yang Executed menunggu posting tetap berstatus `Executed menunggu posting`, tidak ditutup otomatis
96. Pengaju mengajukan Disposal jenis `Sell` atas `Tenda Proyek {runId}` tanpa scan tag aset
97. Verifikasi pengajuan diterima karena Category `Peralatan Proyek {runId}` bertanda Non TAG
98. Aktor Disposal `Indra Pratama {runId}` melakukan Execute atas Disposal `Tenda Proyek {runId}` yang berstatus `Waiting for Execution` tanpa scan tag aset dan tanpa identifikasi manual
99. Verifikasi Execute diterima karena Category `Peralatan Proyek {runId}` bertanda Non TAG
