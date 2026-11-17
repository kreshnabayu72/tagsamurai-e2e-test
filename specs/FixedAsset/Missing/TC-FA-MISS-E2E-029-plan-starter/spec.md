---
id: TC-FA-MISS-E2E-029-plan-starter
title: "Plan Starter: Report Disposal dan Cancel Disposal Report terkunci Upgrade to unlock, kolom TAG hanya tipe terbuka; aksi inti tetap sama"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.10#p1", "EB-AKS-8", "§9.4.1#r2", "§9.4.2#r31"]
smoke: []
dependsOn: []
trace:
  "§9.10#p1": [4, 6, 9, 11, 14, 16, 21, 22, 23, 26, 27, 37, 39, 41, 43, 45, 46, 47]
  "EB-AKS-8": 34
  "§9.4.1#r2": 34
  "§9.4.2#r31": 34
anchor: []
coverage:
  web: automated
---

# Plan Starter: Report Disposal dan Cancel Disposal Report terkunci Upgrade to unlock, kolom TAG hanya tipe terbuka; aksi inti tetap sama

## Prerequisites
- Aktor: Total Control pada Client `Klien Starter {runId}`.
- Layar awal: halaman Assets.
- Data:
  - DU-029-1: Client, Name `Klien Starter {runId}`, Plan `Starter`; entitas khusus yang tidak dipakai spec lain.
  - DU-029-2: Missing record, Name `Laptop Dell Latitude 5420 {runId} - 22`, Asset ID `LPT-0022 {runId}`, Group `Finance Room {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`, TAG `QR`.
  - DU-029-3: Missing record, Name `Hand Pallet Truck {runId} - 3`, Asset ID `HPT-0003 {runId}`, Group `Warehouse {runId}`, Status `Missing`, Source `Manual`, Last Holder `—`, TAG `RFID, NFC, BLE, GPS, QR` (pairing lama dari plan sebelumnya).
  - DU-029-4: Missing record, Name `Projector Epson EB-X06 {runId} - 7`, Asset ID `PRJ-0007 {runId}`, Group `Branch Surabaya {runId}`, Status `Reported Disposal`, Source `Stock opname`, Last Holder `—`, TAG `RFID`.

## Test Steps

### Report Disposal dan Cancel Disposal Report terkunci di plan Starter
1. Klik tab `Missing`
2. Ketik Search `{runId}`, tekan Enter
3. Klik menu ⋯ pada baris `Laptop Dell Latitude 5420 {runId} - 22`
4. Verifikasi aksi `Report Disposal` disabled
5. Arahkan pointer ke aksi `Report Disposal`
6. Verifikasi alasan `Upgrade to unlock` tersampaikan pada aksi `Report Disposal` yang disabled
7. Tekan `Esc`
8. Klik menu ⋯ pada baris `Projector Epson EB-X06 {runId} - 7`
9. Verifikasi aksi `Cancel Disposal Report` disabled
10. Arahkan pointer ke aksi `Cancel Disposal Report`
11. Verifikasi alasan `Upgrade to unlock` tersampaikan pada aksi `Cancel Disposal Report` yang disabled
12. Tekan `Esc`
13. Centang baris `Laptop Dell Latitude 5420 {runId} - 22`
14. Verifikasi tombol bulk `Report Disposal` disabled
15. Arahkan pointer ke tombol bulk `Report Disposal`
16. Verifikasi alasan `Upgrade to unlock` tersampaikan pada tombol bulk `Report Disposal` yang disabled
17. Lepas centang baris `Laptop Dell Latitude 5420 {runId} - 22`

### Kolom TAG dan filter TAG hanya memuat tipe terbuka
18. Klik tombol `Column Visibility` pada header tabel
19. Centang `TAG`
20. Tekan `Esc`
21. Verifikasi sel TAG baris `Laptop Dell Latitude 5420 {runId} - 22` memuat ikon tipe `QR`
22. Verifikasi sel TAG baris `Hand Pallet Truck {runId} - 3` hanya memuat ikon tipe `QR`
23. Verifikasi sel TAG baris `Projector Epson EB-X06 {runId} - 7` tampil `—`
24. Klik `Filter`
25. Klik field `TAG`
26. Verifikasi opsi `QR` tampil pada field `TAG`
27. Verifikasi opsi `RFID` tidak tampil pada field `TAG`
28. Tekan `Esc`
29. Klik `Filter`

### Aksi inti tetap tersedia di plan Starter
30. Klik menu ⋯ pada baris `Laptop Dell Latitude 5420 {runId} - 22`
31. Klik `Add Update`
32. Isi Update `Terakhir terlihat di lobi cabang {runId}`
33. Klik `[Add Update]`
34. Verifikasi toast `Success, update has been added.` tampil

### Scan TAG tipe terkunci di plan Starter
35. Klik menu ⋯ pada baris `Hand Pallet Truck {runId} - 3`
36. Klik `Mark as Found`
37. Verifikasi scan TAG tipe `RFID`, `NFC`, `BLE`, dan `GPS` pada isian Scan TAG terkunci (disabled)
38. Arahkan pointer ke scan TAG tipe `RFID`
39. Verifikasi alasan `Upgrade to unlock` tersampaikan pada scan TAG tipe `RFID` yang terkunci
40. Arahkan pointer ke scan TAG tipe `NFC`
41. Verifikasi alasan `Upgrade to unlock` tersampaikan pada scan TAG tipe `NFC` yang terkunci
42. Arahkan pointer ke scan TAG tipe `BLE`
43. Verifikasi alasan `Upgrade to unlock` tersampaikan pada scan TAG tipe `BLE` yang terkunci
44. Arahkan pointer ke scan TAG tipe `GPS`
45. Verifikasi alasan `Upgrade to unlock` tersampaikan pada scan TAG tipe `GPS` yang terkunci
46. Verifikasi scan TAG tipe `QR` pada isian Scan TAG aktif
47. Verifikasi tautan `I Can't Scan the TAG` tersedia pada isian Scan TAG
48. Klik `[Cancel]` pada dialog Mark as Found (form belum diubah)
