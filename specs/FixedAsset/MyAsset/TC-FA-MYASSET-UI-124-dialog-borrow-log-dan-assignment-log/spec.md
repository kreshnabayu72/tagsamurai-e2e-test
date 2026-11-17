---
id: TC-FA-MYASSET-UI-124-dialog-borrow-log-dan-assignment-log
title: "Dialog Borrow Log dan Assignment Log di My Asset: node keputusan approver tanpa pelaku dan pelaku atas nama"
layer: ui-client
priority: Medium
caseType: Negative
status: draft
sourceRules: ["§1.2#r89", "§2.2#r4", "§Dialog aksi baris (tab Borrowed dan Assigned)#r5", "§Dialog aksi baris (tab Borrowed dan Assigned)#r7", "§9.4.3#b2"]
smoke: []
dependsOn: []
trace:
  "§1.2#r89": [6, 7, 13, 19, 29, 35]
  "§2.2#r4": [8, 14, 20, 30, 36]
  "§Dialog aksi baris (tab Borrowed dan Assigned)#r5": [4, 5, 6, 7, 13, 19, 24, 29, 35]
  "§Dialog aksi baris (tab Borrowed dan Assigned)#r7": [40, 44]
  "§9.4.3#b2": [8, 14, 20, 30, 36]
anchor: [12, 18, 28, 34]
coverage:
  web: automated
---

# Dialog Borrow Log dan Assignment Log di My Asset: node keputusan approver tanpa pelaku dan pelaku atas nama

## Prerequisites
- Aktor: Borrower `Budi Santoso` pada kondisi K1 sampai K4, Assignee Employee `Budi Santoso` pada kondisi K5 dan K6, dan PIC `Budi Santoso` pada kondisi K7 dan K8.
- Layar awal: My Asset > Borrowed untuk kondisi K1 sampai K4 dan K7, dan My Asset > Assigned untuk kondisi K5, K6, dan K8.
- Komponen: Dialog Borrow Log (T-BRW-23)
- Data:
  - DU-124-1: baris Borrowed dengan Name `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Status `Borrowed`, Borrower `Me`, Transaction ID `BRW-2026-0149`. Borrow Log baris ini memuat node `Approved` oleh approver `Hendra Wijaya`, node `Extension forwarded` oleh Aktor Borrow `Rina W`, node `Extension approved` oleh approver `Hendra Wijaya`, dan node `Extension applied` oleh Aktor Borrow `Rina W`.
  - DU-124-2: baris History dengan Name `Projector Epson EB-X06 - 12`, Asset ID `PRJ-2026-0012`, Status `Rejected`, Borrower `Me`, Transaction ID `BRW-2026-0152`. Borrow Log baris ini memuat node `Rejected` oleh approver `Hendra Wijaya`.
  - DU-124-3: baris Borrowed dengan Name `Laptop Dell Latitude 5420 - 2`, Asset ID `LPT-2026-0002`, Status `Borrowed`, Borrower `Me`, Transaction ID `BRW-2026-0147`. Borrow Log baris ini memuat node `Extension rejected` oleh approver `Hendra Wijaya`.
  - DU-124-4: baris Borrowed dengan Name `Laptop Dell Latitude 5420 - 51`, Asset ID `LPT-2026-0051`, Status `Borrowed`, Borrower `Me`, Transaction ID `BRW-2026-0164`. Borrow Log baris ini memuat node `Extension rejected` hasil review oleh Aktor Borrow `Rina W`.
  - DU-124-5: baris Assigned dengan Name `Meeting Mic Set - 7`, Asset ID `MIC-2026-0007`, Status `Waiting for Handover`, Assignee `Budi Santoso`, Transaction ID `ASG-2026-0071`. Assignment Log baris ini memuat node `Approved` oleh approver `Hendra Wijaya`.
  - DU-124-6: baris History dengan Name `Projector Epson EB-X06 - 15`, Asset ID `PRJ-2026-0015`, Status `Rejected`, Assignee `Budi Santoso`, Transaction ID `ASG-2026-0073`. Assignment Log baris ini memuat node `Rejected` oleh approver `Hendra Wijaya`.
  - DU-124-7: baris Borrowed dengan Name `Laptop Dell Latitude 5420 - 33`, Asset ID `LPT-2026-0033`, Status `Borrowed`, Borrower `Dewi Lestari` tanpa akun, Transaction ID `BRW-2026-0160`. Borrow Log baris ini memuat node `Handed over` dengan pelaku PIC `Budi Santoso` atas nama Borrower `Dewi Lestari`.
  - DU-124-8: baris Assigned dengan Name `Projector Epson EB-X06 - 12`, Asset ID `PRJ-2026-0012`, Status `Assigned`, Assignee Division `Finance`, Transaction ID `ASG-2026-0072`. Assignment Log baris ini memuat node konfirmasi Handover dengan pelaku PIC `Budi Santoso` atas nama Division `Finance`.
- Kondisi:
  - K1: Borrow Log baris DU-124-1 dibuka.
  - K2: Borrow Log baris DU-124-2 dibuka.
  - K3: Borrow Log baris DU-124-3 dibuka.
  - K4: Borrow Log baris DU-124-4 dibuka.
  - K5: Assignment Log baris DU-124-5 dibuka.
  - K6: Assignment Log baris DU-124-6 dibuka.
  - K7: Borrow Log baris DU-124-7 dibuka.
  - K8: Assignment Log baris DU-124-8 dibuka.

## Test Steps

### Borrow Log menampilkan pelaku Aktor Borrow tetapi node approver tanpa pelaku
1. Tampilkan Dialog Borrow Log dengan kondisi K1
2. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 10`
3. Klik `Borrow Log`
4. Verifikasi node `Extension forwarded` menampilkan pelaku Aktor Borrow `Rina W`
5. Verifikasi node `Extension applied` menampilkan pelaku Aktor Borrow `Rina W`
6. Verifikasi node `Approved` tampil tanpa nama pelaku
7. Verifikasi node `Extension approved` tampil tanpa nama pelaku
8. Verifikasi nama approver `Hendra Wijaya` tidak tampil di Borrow Log

### Node Rejected oleh approver tanpa pelaku
9. Tampilkan Dialog Borrow Log dengan kondisi K2
10. Klik `⋯` pada baris `Projector Epson EB-X06 - 12`
11. Klik `Borrow Log`
12. Verifikasi node `Rejected` tampil
13. Verifikasi node `Rejected` tampil tanpa nama pelaku
14. Verifikasi nama approver `Hendra Wijaya` tidak tampil di Borrow Log

### Node Extension rejected oleh approver tanpa pelaku
15. Tampilkan Dialog Borrow Log dengan kondisi K3
16. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 2`
17. Klik `Borrow Log`
18. Verifikasi node `Extension rejected` tampil
19. Verifikasi node `Extension rejected` tampil tanpa nama pelaku
20. Verifikasi nama approver `Hendra Wijaya` tidak tampil di Borrow Log

### Node Extension rejected hasil review Aktor Borrow menampilkan pelaku
21. Tampilkan Dialog Borrow Log dengan kondisi K4
22. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 51`
23. Klik `Borrow Log`
24. Verifikasi node `Extension rejected` menampilkan pelaku Aktor Borrow `Rina W`

### Assignment Log node Approved tanpa pelaku
25. Tampilkan Dialog Borrow Log dengan kondisi K5
26. Klik `⋯` pada baris `Meeting Mic Set - 7`
27. Klik `Assignment Log`
28. Verifikasi node `Approved` tampil
29. Verifikasi node `Approved` tampil tanpa nama pelaku
30. Verifikasi nama approver `Hendra Wijaya` tidak tampil di Assignment Log

### Assignment Log node Rejected tanpa pelaku
31. Tampilkan Dialog Borrow Log dengan kondisi K6
32. Klik `⋯` pada baris `Projector Epson EB-X06 - 15`
33. Klik `Assignment Log`
34. Verifikasi node `Rejected` tampil
35. Verifikasi node `Rejected` tampil tanpa nama pelaku
36. Verifikasi nama approver `Hendra Wijaya` tidak tampil di Assignment Log

### Pelaku atas nama PIC pada Borrow Log
37. Tampilkan Dialog Borrow Log dengan kondisi K7
38. Klik `⋯` pada baris `Laptop Dell Latitude 5420 - 33`
39. Klik `Borrow Log`
40. Verifikasi pelaku pada node `Handed over` ditulis `Budi Santoso on behalf of Dewi Lestari`

### Pelaku atas nama PIC pada Assignment Log
41. Tampilkan Dialog Borrow Log dengan kondisi K8
42. Klik `⋯` pada baris `Projector Epson EB-X06 - 12`
43. Klik `Assignment Log`
44. Verifikasi pelaku pada node konfirmasi Handover ditulis `Budi Santoso on behalf of Finance`
