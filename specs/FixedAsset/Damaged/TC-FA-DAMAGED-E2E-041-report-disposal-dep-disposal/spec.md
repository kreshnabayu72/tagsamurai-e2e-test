---
id: TC-FA-DAMAGED-E2E-041-report-disposal-dep-disposal
title: "Report Disposal dari baris record membuka D-DISP-13 dan mengubah record menjadi Reported Disposal dengan node Disposal reported by; aset Borrowed atau Assigned tampil Report Disposal Disabled"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, "§4.1#r7", TS-DISP-15, D-DISP-13, "§4.4#r9", S-DMG-05, "§8.1#r13", "§8.3#r4", "§Aturan Logika Modul#r63", "§Aturan Logika Modul#r64", "§Aturan Logika Modul#r20", "§9.7#r10", TS-DISP-12, "§9.2#b26", F-DMG-06, "§2.1#r8", "§4.8#r10", S-DMG-01, "§4.2.4#r17", "§3#p7", "§9.2#r3"]
smoke: []
dependsOn: ["Disposal: dialog Report Disposal (D-DISP-13)"]
trace:
  T-DMG-01: [2, 5, 15, 17, 29, 31, 33, 36, 38, 40, 43]
  "§4.1#r7": 7
  TS-DISP-15: [10, 11]
  D-DISP-13: [7, 11, 12, 26]
  "§4.4#r9": [7, 12]
  S-DMG-05: 16
  "§8.1#r13": [20, 21, 22]
  "§8.3#r4": 20
  "§Aturan Logika Modul#r63": [7, 26]
  "§Aturan Logika Modul#r64": 12
  "§Aturan Logika Modul#r20": 12
  "§9.7#r10": [12, 13, 26]
  TS-DISP-12: [10, 12, 26]
  "§9.2#b26": [7, 12]
  F-DMG-06: [7, 12]
  "§2.1#r8": 5
  "§4.8#r10": 5
  S-DMG-01: 13
  "§4.2.4#r17": [49, 53]
  "§3#p7": [7, 12]
  "§9.2#r3": [12, 26]
anchor: []
coverage:
  web: automated
---

# Report Disposal dari baris record membuka D-DISP-13 dan mengubah record menjadi Reported Disposal dengan node Disposal reported by; aset Borrowed atau Assigned tampil Report Disposal Disabled

## Prerequisites
- Aktor: Total Control; `Admin B {runId}` (Total Control, seluruh client) hanya memicu perubahan state.
- Layar awal: Assets > Damaged > Active.
- Data:
  - DU-041-1: Damage record `Printer HP LaserJet M404 {runId}`, Group `Head Office`, Status `Damaged`, Source `Manual`, aset tidak sedang Borrowed maupun Assigned (Custody `Available`).
  - DU-041-2: Damage record `Tablet Samsung Tab A8 {runId}`, Group `Head Office`, Status `Damaged`, Source `Manual`, aset sedang Borrowed (Custody `Borrowed`).
  - DU-041-3: Damage record `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, Status `Damaged`, Source `Manual`, aset sedang Assigned (Custody `Assigned`).
  - DU-041-4: Input Report Disposal atas `Printer HP LaserJet M404 {runId}`: Reason `Unit rusak berat dan biaya perbaikan melebihi nilai buku`.
  - DU-041-5: Damage record `Monitor Dell P2422H {runId}`, Group `Head Office`, Status `Damaged`, Source `Manual`, aset tidak sedang Borrowed maupun Assigned (Custody `Available`).
  - DU-041-6: User `Admin B {runId}`, role Total Control, cakupan seluruh client.
  - DU-041-7: Input Report Disposal atas `Monitor Dell P2422H {runId}`: Reason `Unit rusak berat dan sudah tidak layak pakai`.
  - DU-041-8: Input Mark as Repaired `Admin B {runId}` atas `Monitor Dell P2422H {runId}`: Repair note `Panel diganti dan unit sudah diuji normal`.
- Kondisi:
  - Level Feature Suite Disposal bernilai `Full`.

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
22. Verifikasi baris detail node `Disposal reported by` memuat `Reason`
23. Tutup dialog Damage Log

### Disposal Report tercatat di tab Reported
24. Buka Transactions > Disposal, tab Reported
25. Ketik Search `Printer HP LaserJet M404 {runId}`, tekan Enter
26. Verifikasi Disposal Report atas aset `Printer HP LaserJet M404 {runId}` tampil di tab Reported

### Report Disposal Disabled pada aset Borrowed
27. Buka tab Damaged, sub-tab Active
28. Ketik Search `Tablet Samsung Tab A8 {runId}`, tekan Enter
29. Verifikasi baris `Tablet Samsung Tab A8 {runId}` tampil dengan Status `Damaged`
30. Buka menu ⋯ pada baris `Tablet Samsung Tab A8 {runId}`
31. Verifikasi aksi `Report Disposal` Disabled pada menu baris `Tablet Samsung Tab A8 {runId}`
32. Arahkan pointer ke aksi `Report Disposal` pada menu baris `Tablet Samsung Tab A8 {runId}`
33. Verifikasi alasan aksi `Report Disposal` Disabled tersampaikan pada menu baris `Tablet Samsung Tab A8 {runId}`
34. Tutup menu ⋯

### Report Disposal Disabled pada aset Assigned
35. Ganti isi kotak search dengan `Laptop Dell Latitude 5420 {runId}`, tekan Enter
36. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tampil dengan Status `Damaged`
37. Buka menu ⋯ pada baris `Laptop Dell Latitude 5420 {runId}`
38. Verifikasi aksi `Report Disposal` Disabled pada menu baris `Laptop Dell Latitude 5420 {runId}`
39. Arahkan pointer ke aksi `Report Disposal` pada menu baris `Laptop Dell Latitude 5420 {runId}`
40. Verifikasi alasan aksi `Report Disposal` Disabled tersampaikan pada menu baris `Laptop Dell Latitude 5420 {runId}`
41. Tutup menu ⋯

### Status record berubah sebelum Submit Report Disposal memunculkan dialog Already Changed
42. Ganti isi kotak search dengan `Monitor Dell P2422H {runId}`, tekan Enter
43. Verifikasi baris `Monitor Dell P2422H {runId}` berstatus `Damaged`
44. Buka menu ⋯ pada baris `Monitor Dell P2422H {runId}`
45. Klik `Report Disposal`
46. Isi Reason `Unit rusak berat dan sudah tidak layak pakai`
47. `Admin B {runId}` menjalankan Mark as Repaired atas record `Monitor Dell P2422H {runId}` dengan Repair note `Panel diganti dan unit sudah diuji normal` dari sesi lain
48. Kirim dialog Report Disposal
49. Verifikasi dialog `Already Changed` tampil dengan isi `This record was changed by [User Name]. Reload to see the latest status.` dengan `[User Name]` diisi `Admin B {runId}`
50. Klik `Reload`
51. Klik sub-tab `History`
52. Ketik Search `Monitor Dell P2422H {runId}`, tekan Enter
53. Verifikasi baris `Monitor Dell P2422H {runId}` tampil di sub-tab `History` dengan Status `Repaired`
