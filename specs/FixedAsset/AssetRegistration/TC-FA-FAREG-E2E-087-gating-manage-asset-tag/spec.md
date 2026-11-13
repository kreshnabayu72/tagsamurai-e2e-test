---
id: TC-FA-FAREG-E2E-087-gating-manage-asset-tag
title: "Gating Manage asset & TAG tanpa hak putus"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: ["FAREG-LOGIC-06p", "§2.1#r3", "§4.1#r1", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§4.8#r15", "§4.8#r16", "§4.8#r17", "§4.8#r18", "§4.8#r19", "§4.8#r20", "§4.8#r23", "§9.2#p82", "T-REG-07"]
smoke: ["T-REG-07"]
dependsOn: []
trace:
  "FAREG-LOGIC-06p": 42
  "§2.1#r3": [7, 21, 42]
  "§4.1#r1": 2
  "§4.8#r1": 2
  "§4.8#r2": 3
  "§4.8#r3": 4
  "§4.8#r4": 27
  "§4.8#r5": [11, 13]
  "§4.8#r6": 8
  "§4.8#r7": [31, 39]
  "§4.8#r8": 10
  "§4.8#r9": 33
  "§4.8#r10": 42
  "§4.8#r11": 42
  "§4.8#r12": 35
  "§4.8#r13": [19, 23, 26]
  "§4.8#r14": 5
  "§4.8#r15": 9
  "§4.8#r16": 8
  "§4.8#r17": [16, 32, 40]
  "§4.8#r18": 42
  "§4.8#r19": 11
  "§4.8#r20": 33
  "§4.8#r23": 35
  "§9.2#p82": 42
  "T-REG-07": 44
anchor: [41]
coverage:
  web: automated
---

# Gating Manage asset & TAG tanpa hak putus

## Prerequisites
- Aktor: Siti N (Manage asset & TAG tanpa capability Update pada node Group registrasi `Gudang 1 {runId}`), pengaju pengajuan DU-087-2.
- Layar awal: Fixed Asset > Assets.
- Data:
  - DU-087-1: Batch Draft dengan Group `Gudang 1 {runId}`, Origin `—`, Total Asset `12`, Progress `0%`, Requested By `Rina W`, Last Updated `T0 − 1 hari`, Item `Laptop` Brand `Dell` Model `Latitude 5440` Quantity `12`.
  - DU-087-2: Pengajuan Waiting for Approval `REG-20261109-08702` di Group `Gudang 1 {runId}`, diajukan Siti N, Total Asset `5`, Last Updated `T0 − 2 hari` (Item `Laptop` Brand `Dell` Model `Latitude 5440` Quantity `5`, TAG `Verified`).
  - DU-087-3: Pengajuan Approved `REG-20261108-08703` di Group `Gudang 1 {runId}`, diajukan Siti N, Approver Budi S, Total Asset `3`, Last Updated `T0 − 3 hari`.
  - DU-087-4: Siti N (Manage asset & TAG tanpa capability Update, Group terkelola `Gudang 1 {runId}`).
  - DU-087-5: Rina W (Manage asset & TAG, Group terkelola `Gudang 1 {runId}`).
  - DU-087-6: Budi S (Manage asset & TAG dengan capability Update pada node Group `Gudang 1 {runId}`).
- Kondisi:
  - Group `Gudang 1 {runId}` ber-toggle `Require Approval for Registration` ON.
  - Kunci sesi edit batch DU-087-1 sedang dipegang Rina W.

## Test Steps

### Tab Registration dan sub tab Draft tampil
1. Klik tab `Registration`
2. Verifikasi tab `Registration` tampil
3. Verifikasi sub tab `Draft` tampil
4. Verifikasi `[+ Register Asset]` tampil pada toolbar sub tab `Draft`
5. Verifikasi `Download` tampil pada toolbar sub tab `Draft`

### Siti N melihat dan menindak batch Draft
6. Ketik Search `Gudang 1 {runId}`, tekan Enter
7. Verifikasi baris Group `Gudang 1 {runId}` dengan Requested By `Rina W` tampil di sub tab `Draft` bagi Siti N
8. Verifikasi row action `Edit` tampil pada baris `Gudang 1 {runId}`
9. Verifikasi row action `Detail` tidak tampil pada baris `Gudang 1 {runId}`
10. Verifikasi row action `Registration Log` tampil pada baris `Gudang 1 {runId}`
11. Verifikasi row action `Delete` tampil pada baris `Gudang 1 {runId}`
12. Centang baris `Gudang 1 {runId}`
13. Verifikasi Bulk Action `Delete` tampil
14. Hilangkan centang baris `Gudang 1 {runId}`

### Registration Log terbuka sebagai dialog read-only
15. Klik row action `Registration Log` pada baris `Gudang 1 {runId}`
16. Verifikasi dialog `Registration Log` terbuka
17. Tutup dialog lewat ikon X

### Edit batch Draft: Take over, Remove from List, Bulk Scan, dan Submit tampil
18. Klik row action `Edit` pada baris `Gudang 1 {runId}`
19. Verifikasi dialog `Draft Is Being Edited` tampil dengan tombol `[Take over]`
20. Klik `[Take over]`
21. Verifikasi form `Register Asset` terbuka dalam mode Edit untuk batch `Gudang 1 {runId}` bagi Siti N
22. Buka row option pada baris Item `Laptop` di tab `General Information`
23. Verifikasi row option `Remove from List` tampil
24. Tutup menu row option
25. Klik tab `Asset`
26. Verifikasi tombol `Bulk Scan` tampil pada Item `Laptop`
27. Verifikasi tombol `[Submit]` tampil pada footer form
28. Klik `[Cancel]` pada footer form yang belum diubah, tanpa dialog Unsaved Changes

### Sub tab Waiting for Approval: pengaju melihat Cancel registration
29. Klik sub tab `Waiting for Approval`
30. Ketik Search `Gudang 1 {runId}`, tekan Enter
31. Verifikasi row action `Detail` tampil pada baris Group `Gudang 1 {runId}` dengan Total Asset `5`
32. Verifikasi row action `Registration Log` tampil pada baris Group `Gudang 1 {runId}` dengan Total Asset `5`
33. Verifikasi row action `Cancel registration` tampil pada baris pengajuan `Siti N`
34. Klik row action `Detail` pada baris Group `Gudang 1 {runId}` dengan Total Asset `5`
35. Verifikasi tombol `[Cancel Registration]` tampil pada halaman Detail pengajuan `Siti N`
36. Klik `[Close]`

### Sub tab History
37. Klik sub tab `History`
38. Ketik Search `Gudang 1 {runId}`, tekan Enter
39. Verifikasi row action `Detail` tampil pada baris Group `Gudang 1 {runId}` dengan Total Asset `3`
40. Verifikasi row action `Registration Log` tampil pada baris Group `Gudang 1 {runId}` dengan Total Asset `3`

### Menu Approvals tidak tampil bagi pemegang Manage asset & TAG tanpa capability Update
41. Verifikasi item sidebar `Assets` tampil bagi Siti N
42. Verifikasi menu `Approvals` > `Registration` tidak tampil pada sidebar bagi Siti N

### Halaman Approval ditolak lewat alamat langsung
43. Buka halaman Approval pengajuan Group `Gudang 1 {runId}` dengan Total Asset `5` lewat alamat langsung (URL)
44. Verifikasi toast `You don't have permission to do this.` tampil tanpa pengalihan halaman bagi Siti N
