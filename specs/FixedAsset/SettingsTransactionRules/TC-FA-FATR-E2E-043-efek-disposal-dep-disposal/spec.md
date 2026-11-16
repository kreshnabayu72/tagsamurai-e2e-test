---
id: TC-FA-FATR-E2E-043-efek-disposal-dep-disposal
title: "Setting Disposal berlaku pada transaksi Disposal"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§4.1#r149", "§4.1#r187", "§9.2#b16", "§9.2#b166", "§9.2#b525", "§9.2#b526", "§9.2#b529", "§9.2#b532", "§9.4.2#r137", "§9.7#r28", "EB-XM-2@disposal", "§4.1#r152", "§9.2#b269", "§9.2#b397", "§9.2#b527", "§9.2#b528", "§9.4.2#r136"]
smoke: ["§4.1#r152", "§9.2#b269", "§9.2#b397", "§9.2#b527", "§9.2#b528", "§9.4.2#r136"]
dependsOn:
  - "Disposal: pengajuan, approval, dan Execute"
trace:
  "§4.1#r149": [7, 24]
  "§4.1#r187": 16
  "§9.2#b16": [42, 60]
  "§9.2#b166": 42
  "§9.2#b525": [4, 5]
  "§9.2#b526": 6
  "§9.2#b529": 16
  "§9.2#b532": 10
  "§9.4.2#r137": 16
  "§9.7#r28": 31
  "EB-XM-2@disposal": [42, 49, 56]
  "§4.1#r152": 9
  "§9.2#b269": [28, 29]
  "§9.2#b397": 7
  "§9.2#b527": 12
  "§9.2#b528": 15
  "§9.4.2#r136": 15
anchor: [34, 59]
coverage:
  web: automated
---

# Setting Disposal berlaku pada transaksi Disposal

## Prerequisites
- Aktor: Default User yang memegang Manage transaction settings (Update); aktor lain yang masuk sebagai pengguna: `Fajar Ramadhan {runId}`, `Eko Prasetyo {runId}`.
- Layar awal: Fixed Asset > Disposal.
- Data:
  - DU-043-1: Group Name `Maintenance {runId}`; Group tanpa Division.
  - DU-043-2: Category Name `Plant Equipment {runId}`, Allow Disposal `Allow`; Category leaf dengan Allow Disposal nilai sendiri.
  - DU-043-3: User Name `Fajar Ramadhan {runId}`, Role `Employee`, Group `Maintenance {runId}`, Role Transaksi `Aktor Disposal`; akun aktif.
  - DU-043-4: User Name `Eko Prasetyo {runId}`, Role `Employee`, Group `Maintenance {runId}`, Role Transaksi `Approver`; akun aktif.
  - DU-043-5: Asset Name `Server Rack SR40 {runId}`, Category `Plant Equipment {runId}`, Group `Maintenance {runId}`, Status `Available`, Purchase date `T0 − 3 bulan`, Book value (Commercial) `10000000`; aset yang dibeli 3 bulan lalu.
  - DU-043-6: Asset Name `Server Rack SR60 {runId}`, Category `Plant Equipment {runId}`, Group `Maintenance {runId}`, Status `Available`, Purchase date `T0 − 3 bulan`, Book value (Commercial) `10000000`; aset yang dibeli 3 bulan lalu.
  - DU-043-7: Asset Name `Lathe Machine LM90 {runId}`, Category `Plant Equipment {runId}`, Group `Maintenance {runId}`, Status `Waiting for Approval`; aset.
  - DU-043-8: Asset Name `Forklift FL40 {runId}`, Category `Plant Equipment {runId}`, Group `Maintenance {runId}`, Status `Waiting for Execution`; aset.
  - DU-043-9: Asset Name `Welding Station WS20 {runId}`, Category `Plant Equipment {runId}`, Group `Maintenance {runId}`, Status `Available`; aset.
  - DU-043-10: Override Target `Server Rack SR40 {runId}`, Scope `Asset`, Transaction `Disposal`, Require approval `OFF`, Min asset age warning `12`, Max deviation from book value `30`; override Asset untuk Disposal.
  - DU-043-11: Override Target `Server Rack SR60 {runId}`, Scope `Asset`, Transaction `Disposal`, Require approval `ON`, Min asset age warning `12`; override Asset untuk Disposal.
  - DU-043-12: Disposal Asset `Lathe Machine LM90 {runId}`, Type `Sell`, Status `Waiting for Approval`, Diajukan `T0 − 30 hari`; pengajuan yang sudah melewati batas Transaction timeout.
  - DU-043-13: Disposal Asset `Forklift FL40 {runId}`, Type `Scrap`, Status `Waiting for Execution`, Disetujui `T0 − 30 hari`; pengajuan yang sudah melewati batas Transaction timeout.
  - DU-043-16: Asset Name `Welding Unit WU25 {runId}`, Category `Plant Equipment {runId}`, Group `Maintenance {runId}`, Status `Available, kondisi Missing`; aset berkondisi Missing.
  - DU-043-17: Override Target `Welding Unit WU25 {runId}`, Scope `Asset`, Transaction `Disposal`, Allow Disposal `Deny`; override Asset untuk Disposal yang melarang Disposal aset itu.
- Kondisi:
  - Akun semua aktor di atas aktif dan kredensialnya tersedia untuk login.
  - Role Transaksi `Approver` untuk Group `Maintenance {runId}` hanya dipegang `Eko Prasetyo {runId}`.
  - `Fajar Ramadhan {runId}` berhak mengajukan Disposal dan membuka halaman Execute karena memegang Role Transaksi `Aktor Disposal` untuk Group `Maintenance {runId}`.
  - Pengajuan Disposal aset `Lathe Machine LM90 {runId}` dan `Forklift FL40 {runId}` sudah melewati batas Transaction timeout statusnya masing-masing.

## Test Steps
### Disposal dengan Require approval OFF langsung menunggu Execute
1. Masuk sebagai `Fajar Ramadhan {runId}`
2. Mulai pengajuan Disposal baru untuk aset `Server Rack SR40 {runId}`
3. Pilih jenis Disposal `Sell`
4. Verifikasi judul form pengajuan Disposal bertuliskan `Dispose`
5. Verifikasi tombol `[Dispose]` tampil pada form
6. Verifikasi peringatan `Disposal without approval. This action can't be undone.` tampil
7. Verifikasi peringatan severity danger tampil karena umur aset `Server Rack SR40 {runId}` kurang dari `12` bulan kalender penuh sejak Purchase date
8. Isi nilai jual `6000000`
9. Verifikasi peringatan deviasi tampil karena nilai jual `6000000` di bawah nilai buku Commercial `10000000` dengan selisih melebihi Max deviation from book value `30`
10. Verifikasi peringatan aset muda dan peringatan below book value tetap tampil walau Require approval OFF
11. Klik `[Dispose]` tanpa mengisi reason
12. Verifikasi pengajuan tidak dapat diajukan karena reason wajib diisi
13. Isi reason `Unit diganti dengan model baru`
14. Klik `[Dispose]`
15. Verifikasi baris Disposal aset `Server Rack SR40 {runId}` langsung berstatus `Waiting for Execution`, tanpa melalui `Waiting for Approval`
16. Verifikasi pengaju diarahkan ke halaman Execute dalam sesi yang sama

### Peringatan aset muda tampil pada approval
17. Mulai pengajuan Disposal baru untuk aset `Server Rack SR60 {runId}`
18. Pilih jenis Disposal `Sell`
19. Isi nilai jual `6000000`
20. Isi reason `Unit diganti dengan model baru`
21. Klik `[Submit]`
22. Masuk sebagai `Eko Prasetyo {runId}`
23. Buka permintaan approval Disposal aset `Server Rack SR60 {runId}`
24. Verifikasi peringatan severity danger tampil pada permintaan approval karena aset `Server Rack SR60 {runId}` lebih muda dari Min asset age warning

### Transaksi yang melewati Transaction timeout berakhir Canceled oleh System
25. Masuk sebagai Default User
26. Job Transaction timeout berjalan
27. Buka daftar Disposal
28. Verifikasi pengajuan Disposal aset `Lathe Machine LM90 {runId}` yang menunggu approval berstatus `Canceled` oleh `System`, bukan `Expired`
29. Verifikasi pengajuan Disposal aset `Forklift FL40 {runId}` yang menunggu eksekusi berstatus `Canceled` oleh `System`, bukan `Expired`
30. Buka detail pengajuan Disposal aset `Lathe Machine LM90 {runId}` di daftar Disposal
31. Verifikasi daftar dan detail transaksi Disposal aset `Lathe Machine LM90 {runId}` sama-sama menampilkan status `Canceled`

### Override Allow Disposal Deny dan penghapusannya tercermin di Disposal
32. Buka Fixed Asset > Disposal
33. Ketik Search `Welding Station WS20 {runId}` pada daftar aset di Fixed Asset > Disposal, tekan Enter
34. Verifikasi aksi Disposal pada baris aset `Welding Station WS20 {runId}` aktif
35. Buka tab Disposal pada node Category `Plant Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
36. Klik `[+ Override]` pada bagian Overrides
37. Isi Scope `Asset` dengan Target `Welding Station WS20 {runId}`
38. Pilih Field `Allow Disposal` dengan Value `Deny`
39. Klik `[Submit]`
40. Buka Fixed Asset > Disposal
41. Ketik Search `Welding Station WS20 {runId}` pada daftar aset di Fixed Asset > Disposal, tekan Enter
42. Verifikasi aksi Disposal pada baris aset `Welding Station WS20 {runId}` disabled, dengan alasan dan kontak tersampaikan pada aksi itu
43. Buka tab Disposal pada node Category `Plant Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
44. Buka menu ⋯ pada baris override untuk `Welding Station WS20 {runId}`
45. Klik `Delete`
46. Klik `[Delete]` pada dialog Delete Override
47. Buka Fixed Asset > Disposal
48. Ketik Search `Welding Station WS20 {runId}` pada daftar aset di Fixed Asset > Disposal, tekan Enter
49. Verifikasi aksi Disposal pada baris aset `Welding Station WS20 {runId}` aktif lagi

### Perubahan nilai Category berlaku untuk pengajuan Disposal baru
50. Buka tab Disposal pada node Category `Plant Equipment {runId}` di Fixed Asset > Settings > Transaction Settings
51. Pilih nilai `Deny` pada field Allow Disposal
52. Klik `[Save]`
53. Klik `[Save]` pada dialog Save Changes
54. Buka Fixed Asset > Disposal
55. Ketik Search `Welding Station WS20 {runId}` pada daftar aset di Fixed Asset > Disposal, tekan Enter
56. Verifikasi aksi Disposal pada baris aset `Welding Station WS20 {runId}` disabled sesuai nilai baru Category `Plant Equipment {runId}`

### Aset Missing dengan Allow Disposal Deny memblokir Disposal
57. Buka Fixed Asset > Disposal
58. Ketik Search `Welding Unit WU25 {runId}` pada daftar aset di Fixed Asset > Disposal, tekan Enter
59. Verifikasi baris aset `Welding Unit WU25 {runId}` tampil di daftar aset
60. Verifikasi aksi Disposal pada baris aset `Welding Unit WU25 {runId}` yang ditandai hilang disabled karena Allow Disposal bernilai `Deny` pada override, dengan pesan blokir yang menyebut siapa yang dapat dihubungi
