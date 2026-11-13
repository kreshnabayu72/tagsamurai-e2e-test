---
id: TC-FA-FAREG-E2E-089-gating-manage-purchase
title: "Gating Manage purchase"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["FAREG-LOGIC-02e", "FAREG-LOGIC-06p", "FAREG-LOGIC-20b", "§2.1#r4", "§4.1#r1", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§4.8#r15", "§4.8#r16", "§4.8#r17", "§4.8#r19", "§4.8#r21", "§9.2#p81", "S-REG-26"]
smoke: ["S-REG-26"]
dependsOn: []
trace:
  "FAREG-LOGIC-02e": [8, 28]
  "FAREG-LOGIC-06p": [14, 28]
  "FAREG-LOGIC-20b": [14, 24]
  "§2.1#r4": [5, 7, 10, 11]
  "§4.1#r1": 2
  "§4.8#r1": 2
  "§4.8#r2": 3
  "§4.8#r3": 5
  "§4.8#r4": 16
  "§4.8#r5": 11
  "§4.8#r6": 10
  "§4.8#r7": [28, 37]
  "§4.8#r8": 9
  "§4.8#r9": 30
  "§4.8#r10": 40
  "§4.8#r11": 40
  "§4.8#r12": 33
  "§4.8#r13": [18, 21]
  "§4.8#r14": 4
  "§4.8#r15": 8
  "§4.8#r16": 10
  "§4.8#r17": [9, 29, 38]
  "§4.8#r19": 11
  "§4.8#r21": 12
  "§9.2#p81": [28, 40, 42]
  "S-REG-26": [14, 15, 16]
anchor: [17, 20, 32, 39]
coverage:
  web: automated
---

# Gating Manage purchase

## Prerequisites
- Aktor: Maya L (Manage purchase, Group terkelola `Gudang 1 {runId}`).
- Layar awal: Fixed Asset > Assets.
- Data:
  - DU-089-1: Batch Draft dengan Group `Gudang 1 {runId}`, Origin `—`, Total Asset `12`, Progress `0%`, Requested By `Rina W`, Last Updated `T0 − 1 hari`, Item `Laptop` Brand `Dell` Model `Latitude 5440` Quantity `12`.
  - DU-089-2: Pengajuan Waiting for Approval `REG-20261109-08902` di Group `Gudang 1 {runId}`, diajukan Rina W, Total Asset `5`, Last Updated `T0 − 2 hari` (Item `Laptop` Brand `Dell` Model `Latitude 5440` Quantity `5`, TAG `Verified`).
  - DU-089-3: Pengajuan Approved `REG-20261108-08903` di Group `Gudang 1 {runId}`, diajukan Rina W, Approver Budi S, Total Asset `3`, Last Updated `T0 − 3 hari`.
  - DU-089-4: Maya L (Manage purchase, Group terkelola `Gudang 1 {runId}`).
  - DU-089-5: Rina W (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`).
  - DU-089-6: Budi S (Manage asset & TAG dengan capability Update pada node Group `Gudang 1 {runId}`).
- Kondisi:
  - Group `Gudang 1 {runId}` ber-toggle `Require Approval for Registration` ON.

## Test Steps

### Tab Registration dan sub tab Draft tampil
1. Klik tab `Registration`
2. Verifikasi tab `Registration` tampil
3. Verifikasi sub tab `Draft` tampil
4. Verifikasi `Download` tampil pada toolbar sub tab `Draft`
5. Verifikasi `[+ Register Asset]` tidak tampil pada toolbar sub tab `Draft`

### Manage purchase melihat batch Draft hanya lewat Detail
6. Ketik Search `Gudang 1 {runId}`, tekan Enter
7. Verifikasi baris Group `Gudang 1 {runId}` dengan Requested By `Rina W` tampil di sub tab `Draft` bagi Maya L
8. Verifikasi row action `Detail` tampil pada baris `Gudang 1 {runId}`
9. Verifikasi row action `Registration Log` tampil pada baris `Gudang 1 {runId}`
10. Verifikasi row action `Edit` tidak tampil pada baris `Gudang 1 {runId}`
11. Verifikasi row action `Delete` tidak tampil pada baris `Gudang 1 {runId}`
12. Verifikasi kolom Checkbox dan Bulk Action `Delete` tidak tampil pada tabel sub tab `Draft`

### Detail batch Draft membuka form read-only
13. Klik row action `Detail` pada baris `Gudang 1 {runId}`
14. Verifikasi form `Register Asset` terbuka dalam mode read-only dengan footer `[Close]` bagi Maya L
15. Verifikasi data form tampil sebagai teks atau Badge statis tanpa field yang dapat diisi
16. Verifikasi `[Save draft]` dan `[Submit]` tidak tampil pada footer form read-only
17. Verifikasi baris Item `Laptop` tampil pada tabel Item tab `General Information`
18. Verifikasi row option `Remove from List` tidak tampil pada baris Item `Laptop`
19. Klik tab `Asset`
20. Verifikasi tabel aset Item `Laptop` tampil
21. Verifikasi tombol `Bulk Scan` tidak tampil pada Item `Laptop`
22. Klik `[Close]`

### Klik Group membuka form read-only bagi role tanpa hak ubah
23. Klik Group `Gudang 1 {runId}` pada baris tabel Draft
24. Verifikasi form `Register Asset` terbuka dalam mode read-only untuk batch `Gudang 1 {runId}`
25. Klik `[Close]`

### Sub tab Waiting for Approval dan Detail pengajuan
26. Klik sub tab `Waiting for Approval`
27. Ketik Search `Gudang 1 {runId}`, tekan Enter
28. Verifikasi row action `Detail` tampil pada baris Group `Gudang 1 {runId}` dengan Total Asset `5`
29. Verifikasi row action `Registration Log` tampil pada baris Group `Gudang 1 {runId}` dengan Total Asset `5`
30. Verifikasi row action `Cancel registration` tidak tampil pada baris pengajuan `Rina W`
31. Klik row action `Detail` pada baris Group `Gudang 1 {runId}` dengan Total Asset `5`
32. Verifikasi tombol `[Close]` tampil pada footer halaman Detail pengajuan bagi Maya L
33. Verifikasi tombol `[Cancel Registration]` tidak tampil pada halaman Detail pengajuan
34. Klik `[Close]`

### Sub tab History
35. Klik sub tab `History`
36. Ketik Search `Gudang 1 {runId}`, tekan Enter
37. Verifikasi row action `Detail` tampil pada baris Group `Gudang 1 {runId}` dengan Total Asset `3`
38. Verifikasi row action `Registration Log` tampil pada baris Group `Gudang 1 {runId}` dengan Total Asset `3`

### Menu Approvals tidak tampil dan halaman Approval ditolak
39. Verifikasi item sidebar `Assets` tampil bagi Maya L
40. Verifikasi menu `Approvals` > `Registration` tidak tampil pada sidebar bagi Maya L
41. Buka halaman Approval pengajuan Group `Gudang 1 {runId}` dengan Total Asset `5` lewat alamat langsung (URL)
42. Verifikasi toast `You don't have permission to do this.` tampil untuk halaman Approval yang dibuka Maya L
