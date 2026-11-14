---
id: TC-FA-DAMAGED-E2E-041-report-disposal-dep-disposal
title: "Report Disposal dari baris record membuka D-DISP-13 dan mengubah record menjadi Reported Disposal dengan node Disposal reported by; aset Borrowed ditolak"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, "§4.1#r7", "§4.2.4#p11", "§4.2.4#r7", "§4.4#r9", S-DMG-05, "§8.1#r13", "§8.3#r4", "§Aturan Logika Modul#r61", "§Aturan Logika Modul#r62", "§Aturan Logika Modul#r19", "§9.7#r10", "§9.6#r6", "§9.2#b23", "§9.1#r6", "§2.1#r8", "§4.8#r8", S-DMG-01]
smoke: []
dependsOn: ["Disposal: dialog Report Disposal (D-DISP-13)"]
trace:
  T-DMG-01: [2, 5, 15, 17, 29, 32, 34, 36, 39, 41]
  "§4.1#r7": 7
  "§4.2.4#p11": [10, 11]
  "§4.2.4#r7": [7, 12]
  "§4.4#r9": [7, 12]
  S-DMG-05: 16
  "§8.1#r13": [20, 21, 22]
  "§8.3#r4": 20
  "§Aturan Logika Modul#r61": [7, 26]
  "§Aturan Logika Modul#r62": 12
  "§Aturan Logika Modul#r19": 12
  "§9.7#r10": [12, 13, 26]
  "§9.6#r6": [10, 12, 26]
  "§9.2#b23": [7, 12]
  "§9.1#r6": 12
  "§2.1#r8": 5
  "§4.8#r8": 5
  S-DMG-01: 13
anchor: []
coverage:
  web: automated
---

# Report Disposal dari baris record membuka D-DISP-13 dan mengubah record menjadi Reported Disposal dengan node Disposal reported by; aset Borrowed ditolak

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Damaged > Active.
- Data:
  - DU-041-1: Damage record `Printer HP LaserJet M404 {runId}`, Group `Head Office`, Status `Damaged`, Source `Manual`, aset tidak sedang Borrowed maupun Assigned (Custody `Available`).
  - DU-041-2: Damage record `Tablet Samsung Tab A8 {runId}`, Group `Head Office`, Status `Damaged`, Source `Manual`, aset sedang Borrowed; Transaction ID milik transaksi Borrow aset itu.
  - DU-041-3: Damage record `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, Status `Damaged`, Source `Manual`, aset sedang Assigned; Transaction ID milik transaksi Assignment aset itu.
  - DU-041-4: Input Report Disposal atas `Printer HP LaserJet M404 {runId}`: Reason `Unit rusak berat dan biaya perbaikan melebihi nilai buku`.
- Kondisi:
  - Level Feature Suite Disposal bernilai `Basic`.

## Test Steps

### Report Disposal atas record Damaged membuka dialog Reason dan mengubah record menjadi Reported Disposal
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Printer HP LaserJet M404 {runId}` berstatus `Damaged`
3. Catat jumlah pada badge tab Damaged
4. Buka menu ⋯ pada baris `Printer HP LaserJet M404 {runId}`
5. Verifikasi menu baris `Printer HP LaserJet M404 {runId}` memuat aksi `Report Disposal`
6. Klik `Report Disposal`
7. Verifikasi dialog Report Disposal terbuka dengan isian `Reason`
8. Isi Reason `Unit rusak berat dan biaya perbaikan melebihi nilai buku`
9. Kirim dialog Report Disposal
10. Verifikasi toast sukses Report Disposal tampil
11. Verifikasi tampilan kembali ke sub-tab Active
12. Verifikasi baris `Printer HP LaserJet M404 {runId}` berstatus `Reported Disposal`
13. Verifikasi jumlah pada badge tab Damaged berkurang `1` dari jumlah yang dicatat
14. Buka menu ⋯ pada baris `Printer HP LaserJet M404 {runId}`
15. Verifikasi menu baris `Printer HP LaserJet M404 {runId}` memuat aksi `Cancel Disposal Report`
16. Verifikasi aksi `Mark as Repaired` Hidden pada menu baris `Printer HP LaserJet M404 {runId}`
17. Verifikasi aksi `Report Disposal` Hidden pada menu baris `Printer HP LaserJet M404 {runId}`
18. Tutup menu ⋯

### Node Disposal reported by di Damage Log
19. Klik nama aset `Printer HP LaserJet M404 {runId}` di kolom Name
20. Verifikasi dialog Damage Log memuat node `Disposal reported by` dengan pelaku aktor yang menjalankan Report Disposal
21. Verifikasi baris detail node `Disposal reported by` memuat Reason `Unit rusak berat dan biaya perbaikan melebihi nilai buku`
22. Verifikasi baris detail node `Disposal reported by` memuat `Report ID`
23. Tutup dialog Damage Log

### Disposal Report tercatat di tab Reported
24. Buka Transactions > Disposal, tab Reported
25. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
26. Verifikasi Disposal Report atas aset `Printer HP LaserJet M404 {runId}` tampil di tab Reported

### Aset Borrowed ditolak Report Disposal
27. Buka tab Damaged, sub-tab Active
28. Ketik Search `Tablet Samsung Tab A8 {runId}`, tekan Enter
29. Verifikasi baris `Tablet Samsung Tab A8 {runId}` tampil dengan Status `Damaged`
30. Buka menu ⋯ pada baris `Tablet Samsung Tab A8 {runId}`
31. Klik `Report Disposal`
32. Verifikasi pesan `This asset is in [Transaction ID]. Return it first.` tampil dengan `[Transaction ID]` diisi nomor transaksi milik DU-041-2
33. Tutup pesan penolakan
34. Verifikasi baris `Tablet Samsung Tab A8 {runId}` tetap berstatus `Damaged`

### Aset Assigned ditolak Report Disposal
35. Ganti isi kotak search dengan `Laptop Dell Latitude 5420 {runId}`, tekan Enter
36. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil dengan Status `Damaged`
37. Buka menu ⋯ pada baris `Laptop Dell Latitude 5420 {runId}`
38. Klik `Report Disposal`
39. Verifikasi pesan `This asset is in [Transaction ID]. Return it first.` tampil dengan `[Transaction ID]` diisi nomor transaksi milik DU-041-3
40. Tutup pesan penolakan
41. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tetap berstatus `Damaged`
