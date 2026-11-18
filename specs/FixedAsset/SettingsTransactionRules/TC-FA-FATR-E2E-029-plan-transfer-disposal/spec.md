---
id: TC-FA-FATR-E2E-029-plan-transfer-disposal
title: "Level Feature Suite Transfer Basic dan Transfer dan Disposal None"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [§9.4.2#r16, §9.4.2#r25, §9.4.4#r2, §9.10.4#b1, §11#r2, §4.3#r14, FATR-LOGIC-18m, FATR-LOGIC-18n, FATR-LOGIC-18p, FATR-LOGIC-18q, FLD-36r, FLD-15, FLD-23, FLD-23e, S-23b, FATR-LOGIC-18a, FATR-LOGIC-18h, FATR-LOGIC-18i, FATR-LOGIC-18j, F-FATR-18.k6]
smoke: [§4.3#r14]
dependsOn: []
trace:
  §9.4.2#r16: [22, 24, 25, 27, 30, 32]
  §9.4.2#r25: [3, 12, 13, 14, 17]
  §9.4.4#r2: [22, 24, 25, 27]
  §9.10.4#b1: [4, 5, 7, 9, 13, 14, 22, 24, 25, 27]
  §4.3#r14: [22, 24, 25, 27]
  §11#r2: [22, 25]
  FATR-LOGIC-18m: [4, 7, 13]
  FATR-LOGIC-18n: [5, 9, 14]
  FATR-LOGIC-18p: [4, 5, 7, 9]
  FATR-LOGIC-18q: [13, 14]
  FLD-36r: [13, 14]
  FLD-15: [4, 7, 13]
  FLD-23: [5, 9, 14]
  FLD-23e: [5, 9, 14]
  S-23b: [4, 5, 7, 9]
  FATR-LOGIC-18a: [17]
  FATR-LOGIC-18h: [22, 24]
  FATR-LOGIC-18i: [25, 27]
  FATR-LOGIC-18j: [24, 27]
  F-FATR-18.k6: [17]
anchor: [21]
coverage:
  web: automated
---

# Level Feature Suite Transfer Basic dan Transfer dan Disposal None

## Prerequisites
- Aktor: Total Control (Rina Wulandari {runId}). Operator Admin Console memicu perubahan level plan entitas.
- Layar awal: Fixed Asset > Settings > Transaction Settings.
- Data:
  - DU-029-1: Entitas `Entitas Plan Transfer Disposal {runId}`, entitas khusus yang tidak dipakai spec lain, dengan level Feature Suite Transfer `Basic` dan Disposal `Full`.

## Test Steps

### Level Transfer Basic: In-transit overdue after dan Photo at end sel Transfer terkunci, Destination scope tetap aktif
1. Klik `All categories` pada Sidebar Category Tree
2. Klik tab `Transfer`
3. Verifikasi kontrol `Destination scope` aktif
4. Verifikasi kontrol `In-transit overdue after` disabled
5. Verifikasi kontrol `Photo at end` disabled
6. Arahkan pointer ke kontrol `In-transit overdue after` yang disabled
7. Verifikasi alasan `Available on plans with full Transfer.` tersampaikan pada kontrol `In-transit overdue after` yang disabled
8. Arahkan pointer ke kontrol `Photo at end` yang disabled
9. Verifikasi alasan `Available on plans with full Transfer.` tersampaikan pada kontrol `Photo at end` yang disabled
10. Klik `[+ Override]`
11. Klik select Field pada baris Field + Value pertama
12. Verifikasi opsi `Destination scope` tidak disabled
13. Verifikasi opsi `In-transit overdue after` disabled
14. Verifikasi opsi `Photo at end` disabled
15. Klik `✕` pada dialog Add override, form belum diubah

### Level Disposal Full: tidak ada field Disposal yang bergerbang
16. Klik tab `Disposal`
17. Verifikasi kontrol `Min asset age warning` aktif

### Level None: tab Transfer dan Disposal tidak tampil dan nilai tersimpan dipertahankan
18. Operator mengubah level Feature Suite Transfer entitas menjadi `None`
19. Operator mengubah level Feature Suite Disposal entitas menjadi `None`
20. Muat ulang halaman
21. Verifikasi toolbar kartu memuat tombol `Export rules`
22. Verifikasi tab `Transfer` tidak tampil pada daftar tab
23. Buka langsung URL Transaction Settings dengan tab `Transfer`
24. Verifikasi tab `Transfer` tetap tidak tampil dan tidak menjadi tab aktif
25. Verifikasi tab `Disposal` tidak tampil pada daftar tab
26. Buka langsung URL Transaction Settings dengan tab `Disposal`
27. Verifikasi tab `Disposal` tetap tidak tampil dan tidak menjadi tab aktif
28. Operator mengubah level Feature Suite Transfer dan Disposal entitas menjadi `Full`
29. Muat ulang halaman, lalu klik tab `Transfer`
30. Verifikasi tab `Transfer` menjadi tab aktif
31. Klik tab `Disposal`
32. Verifikasi tab `Disposal` menjadi tab aktif
