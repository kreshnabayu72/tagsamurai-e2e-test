---
id: TC-FA-FATR-E2E-029-plan-transfer-disposal
title: "Level Feature Suite Transfer dan Disposal None"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [§9.4.2#r16, §9.4.2#r25, §9.4.4#r2, §9.10.4#b1, §11#r2, §4.3#r14]
smoke: [§4.3#r14]
dependsOn: []
trace:
  §9.4.2#r16: [14, 16, 17, 19, 20, 22, 23, 25]
  §9.4.2#r25: [3, 6, 9]
  §9.4.4#r2: [14, 16, 17, 20, 22, 23]
  §9.10.4#b1: [14, 16, 17, 19, 20, 22, 23, 25]
  §4.3#r14: [14, 16, 17, 20, 22, 23]
  §11#r2: [14, 20]
anchor: [13]
coverage:
  web: automated
---

# Level Feature Suite Transfer dan Disposal None

## Prerequisites
- Aktor: Total Control (Rina Wulandari {runId}). Operator Admin Console memicu perubahan level plan entitas.
- Layar awal: Fixed Asset > Settings > Transaction Settings.
- Data:
  - DU-029-1: Entitas `Entitas Plan Transfer Disposal {runId}`, entitas khusus yang tidak dipakai spec lain, dengan level Feature Suite Transfer `Basic` dan Disposal `Basic`.

## Test Steps

### Level Basic: tidak ada field Transfer dan Disposal yang bergerbang
1. Klik `All categories` pada Sidebar Category Tree
2. Klik tab `Transfer`
3. Verifikasi kontrol `Destination scope` aktif
4. Klik `[+ Override]`
5. Klik select Field pada baris Field + Value pertama
6. Verifikasi opsi `Destination scope` tidak disabled
7. Klik `✕` pada dialog Add override, form belum diubah
8. Klik tab `Disposal`
9. Verifikasi kontrol `Min asset age warning` aktif

### Level None: tab Transfer dan Disposal tidak dapat dibuka
10. Operator mengubah level Feature Suite Transfer entitas menjadi `None`
11. Operator mengubah level Feature Suite Disposal entitas menjadi `None`
12. Muat ulang halaman
13. Verifikasi header halaman memuat tombol `Export rules`
14. Verifikasi tab `Transfer` disabled
15. Arahkan pointer ke tab `Transfer`
16. Verifikasi alasan `Not available on your current plan.` tersampaikan pada tab `Transfer` yang disabled
17. Verifikasi chip `Upgrade` pada tab `Transfer`
18. Klik tab `Transfer`
19. Verifikasi tab `Transfer` tidak menjadi tab aktif
20. Verifikasi tab `Disposal` disabled
21. Arahkan pointer ke tab `Disposal`
22. Verifikasi alasan `Not available on your current plan.` tersampaikan pada tab `Disposal` yang disabled
23. Verifikasi chip `Upgrade` pada tab `Disposal`
24. Klik tab `Disposal`
25. Verifikasi tab `Disposal` tidak menjadi tab aktif
