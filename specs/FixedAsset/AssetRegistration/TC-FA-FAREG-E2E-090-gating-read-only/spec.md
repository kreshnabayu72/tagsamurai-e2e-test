---
id: TC-FA-FAREG-E2E-090-gating-read-only
title: "Gating Read Only"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["FAREG-LOGIC-06p", "§2.1#r5", "§4.1#r1", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§4.8#r15", "§4.8#r17", "EB-AKS-4"]
smoke: []
dependsOn: []
trace:
  "FAREG-LOGIC-06p": [19, 35]
  "§2.1#r5": [8, 9, 35]
  "§4.1#r1": [2, 3]
  "§4.8#r1": 2
  "§4.8#r2": 5
  "§4.8#r3": 5
  "§4.8#r4": 25
  "§4.8#r5": 5
  "§4.8#r6": 5
  "§4.8#r7": [19, 32]
  "§4.8#r8": 20
  "§4.8#r9": 21
  "§4.8#r10": 35
  "§4.8#r11": 35
  "§4.8#r12": 24
  "§4.8#r13": 28
  "§4.8#r14": 6
  "§4.8#r15": [19, 32]
  "§4.8#r17": [20, 33]
  "EB-AKS-4": [8, 9, 11, 14, 15, 17]
anchor: [4, 23, 27, 34]
coverage:
  web: automated
---

# Gating Read Only

## Prerequisites
- Aktor: Joko R (Read Only, seluruh client).
- Layar awal: Fixed Asset > Assets.
- Data:
  - DU-090-1: Pengajuan Waiting for Approval `REG-20261109-09002` di Group `Gudang 1 {runId}`, diajukan Rina W, Total Asset `12`, Last Updated `T0 − 1 hari` (Item `Laptop` Brand `Dell` Model `Latitude 5440` Quantity `12`, TAG `Verified`).
  - DU-090-2: Pengajuan Waiting for Approval `REG-20261107-09003` di Group `Gudang 1 {runId}`, diajukan Siti N, Total Asset `5`, Last Updated `T0 − 2 hari` (Item `Laptop` Brand `Dell` Model `Latitude 5440` Quantity `5`, TAG `Verified`).
  - DU-090-3: Pengajuan Approved `REG-20261108-09004` di Group `Gudang 1 {runId}`, diajukan Rina W, Approver Budi S, Total Asset `3`, Last Updated `T0 − 3 hari`.
  - DU-090-4: Joko R (Read Only, seluruh client).
  - DU-090-5: Rina W (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`).
  - DU-090-6: Siti N (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`).
  - DU-090-7: Budi S (Manage asset & TAG dengan capability Update pada node Group `Gudang 1 {runId}`).
- Kondisi:
  - Group `Gudang 1 {runId}` ber-toggle `Require Approval for Registration` ON.

## Test Steps

### Read Only membuka sub tab Waiting for Approval dan sub tab Draft tidak tampil
1. Klik tab `Registration`
2. Verifikasi tab `Registration` tampil
3. Verifikasi sub tab `Waiting for Approval` terbuka
4. Verifikasi sub tab `History` tampil di samping sub tab `Waiting for Approval`
5. Verifikasi sub tab `Draft` tidak tampil sehingga `[+ Register Asset]`, `Delete`, dan `Edit` pada sub tab `Draft` tidak dirender
6. Verifikasi `Download` tampil pada toolbar sub tab `Waiting for Approval`

### Search, Filter, Sort, Pagination, dan Setup Column tampil dan aktif bagi Read Only
7. Ketik Search `{runId}`, tekan Enter
8. Verifikasi baris Group `Gudang 1 {runId}` dengan Total Asset `12` dan Requested By `Rina W` tampil di sub tab `Waiting for Approval`
9. Verifikasi baris Group `Gudang 1 {runId}` dengan Total Asset `5` dan Requested By `Siti N` tampil di sub tab `Waiting for Approval`
10. Klik `Filter`
11. Verifikasi Filter Panel terbuka
12. Tutup Filter Panel
13. Klik header kolom `Total Asset`
14. Verifikasi baris Total Asset `5` berada di atas baris Total Asset `12`
15. Verifikasi Pagination tampil di bawah tabel
16. Klik `Setup Column`
17. Verifikasi panel Setup Column terbuka
18. Tutup panel Setup Column

### Detail pengajuan Waiting for Approval hanya baca
19. Verifikasi row action `Detail` tampil pada baris Group `Gudang 1 {runId}` dengan Total Asset `12`
20. Verifikasi row action `Registration Log` tampil pada baris Group `Gudang 1 {runId}` dengan Total Asset `12`
21. Verifikasi row action `Cancel registration` tidak tampil pada baris pengajuan `Rina W`
22. Klik row action `Detail` pada baris Group `Gudang 1 {runId}` dengan Total Asset `12`
23. Verifikasi tombol `[Close]` tampil pada footer halaman Detail pengajuan bagi Joko R
24. Verifikasi tombol `[Cancel Registration]` tidak tampil pada halaman Detail pengajuan
25. Verifikasi tombol `[Submit]` tidak tampil pada footer halaman Detail pengajuan
26. Klik tab `Asset`
27. Verifikasi tabel aset Item `Laptop` tampil pada halaman Detail pengajuan
28. Verifikasi tombol `Bulk Scan` tidak tampil pada Item `Laptop`
29. Klik `[Close]`

### Sub tab History
30. Klik sub tab `History`
31. Ketik Search `{runId}`, tekan Enter
32. Verifikasi row action `Detail` tampil pada baris Group `Gudang 1 {runId}` dengan Total Asset `3`
33. Verifikasi row action `Registration Log` tampil pada baris Group `Gudang 1 {runId}` dengan Total Asset `3`

### Menu Approvals tidak tampil bagi Read Only
34. Verifikasi item sidebar `Assets` tampil bagi Joko R
35. Verifikasi menu `Approvals` > `Registration` tidak tampil pada sidebar bagi Joko R
