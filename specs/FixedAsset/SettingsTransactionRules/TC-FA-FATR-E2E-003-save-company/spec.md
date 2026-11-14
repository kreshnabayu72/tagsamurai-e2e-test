---
id: TC-FA-FATR-E2E-003-save-company
title: "Save Changes di All categories mengubah Company default"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§9.2#b22", "§9.2#b34", "§9.4.2#r12", "§9.4.2#r13", "§9.4.2#r81", "§9.4.2#r83", "§9.2#p6"]
smoke: ["§9.2#p6"]
dependsOn: []
trace:
  "§9.2#b22": [9, 28]
  "§9.2#b34": [19, 28]
  "§9.4.2#r12": 9
  "§9.4.2#r13": 28
  "§9.4.2#r81": [32, 34]
  "§9.4.2#r83": 30
  "§9.2#p6": [38, 40]
anchor: [18]
coverage:
  web: automated
---

# Save Changes di All categories mengubah Company default

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-003-1: Entitas `Citra Logistik {runId}`, entitas khusus yang hanya dipakai spec ini dan tidak dipakai spec lain. Plan-nya menyediakan transaksi Borrow, Assign, Transfer, dan Disposal.
  - DU-003-2: Category leaf `Forklift {runId}`, tanpa sub-Category, ada di entitas DU-003-1. Di tab Borrow: Max duration bernilai sendiri `14`. Field lain Inherit.
- Kondisi:
  - Company default entitas DU-003-1 bernilai bawaan: Allow Borrow, Allow Assign, Allow Transfer, dan Allow Disposal `Allow`, Require approval Disposal `ON`, Max duration `14`.

## Test Steps

### Konfirmasi tampil bila semua transaksi di Company default Deny
1. Pilih `Deny` pada field `Allow Borrow`
2. Klik tab `Assign`
3. Pilih `Deny` pada field `Allow Assign`
4. Klik tab `Transfer`
5. Pilih `Deny` pada field `Allow Transfer`
6. Klik tab `Disposal`
7. Pilih `Deny` pada field `Allow Disposal`
8. Klik `[Save]`
9. Verifikasi konfirmasi `No transactions will be possible for any asset.` tampil pada dialog Save Changes
10. Klik `[Cancel]` pada dialog Save Changes
11. Muat ulang halaman dan setujui konfirmasi bawaan browser untuk meninggalkan halaman

### Draft Category tidak memicu peringatan Disposal tanpa approval
12. Ketik Search Sidebar Category Tree `Forklift {runId}`, tekan Enter
13. Klik Category leaf `Forklift {runId}`
14. Klik tab `Disposal`
15. Klik `[Set own value]` pada field `Require approval`
16. Klik switch `Require approval` sehingga bernilai `OFF`
17. Klik `[Save]`
18. Verifikasi paragraf `The changes apply to new transactions.` tampil pada dialog Save Changes
19. Verifikasi peringatan `Disposal will run without approval. The same person can request and execute it, so there is no separation of duties.` tidak tampil
20. Klik `[Cancel]` pada dialog Save Changes

### Peringatan Disposal tanpa approval tampil bila draft Company default membuat Require approval OFF
21. Kosongkan kotak Search Sidebar Category Tree, tekan Enter
22. Klik `All categories`
23. Klik tab `Disposal`
24. Klik switch `Require approval` sehingga bernilai `OFF`
25. Klik tab `Borrow`
26. Isi `Max duration` `21`
27. Klik `[Save]`
28. Verifikasi peringatan `Disposal will run without approval. The same person can request and execute it, so there is no separation of duties.` tampil
29. Klik `[Save]` pada dialog Save Changes
30. Verifikasi toast `Success, settings have been saved.`

### Perubahan Company default tersimpan sesudah muat ulang
31. Muat ulang halaman
32. Verifikasi field `Max duration` bernilai `21`
33. Klik tab `Disposal`
34. Verifikasi field `Require approval` bernilai `OFF`

### Nilai sendiri Category yang sama dengan Company default tidak ikut berubah
35. Ketik Search Sidebar Category Tree `Forklift {runId}`, tekan Enter
36. Klik Category leaf `Forklift {runId}`
37. Klik tab `Borrow`
38. Verifikasi field `Max duration` bernilai `14` sebagai nilai sendiri, dengan tombol `[Reset to inherit]` tampil
39. Klik `[Reset to inherit]` pada field `Max duration`
40. Verifikasi field `Max duration` menampilkan teks `Inherit — 21 days (from Company default)`
