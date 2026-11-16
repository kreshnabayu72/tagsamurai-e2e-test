---
id: TC-FA-FATR-E2E-029-plan-transfer-disposal
title: "Level Feature Suite Transfer dan Disposal None"
layer: ui-e2e
priority: High
caseType: Negative
status: ready-for-automation
sourceRules: [§9.4.2#r16, §9.4.2#r25, §9.4.4#r2, §9.4.4#r58, §9.10.4#b1, §4.3#r15]
smoke: [§4.3#r15]
dependsOn: []
trace:
  §9.4.2#r16: [16, 18, 19, 21, 22, 24, 25, 27]
  §9.4.2#r25: [3, 6, 9]
  §9.4.4#r2: [16, 18, 19, 22, 24, 25]
  §9.4.4#r58: 11
  §9.10.4#b1: [16, 18, 19, 21, 22, 24, 25, 27]
  §4.3#r15: [16, 18, 19, 22, 24, 25]
anchor: [15]
coverage:
  web: automated
---

# Level Feature Suite Transfer dan Disposal None

## Prerequisites
- Aktor: Total Control (Rina Wulandari {runId}). Operator Admin Console memicu perubahan level plan entitas.
- Layar awal: Fixed Asset > Settings > Transaction Settings.
- Data:
  - DU-029-1: Entitas `Entitas Plan Transfer Disposal {runId}`, entitas khusus yang tidak dipakai spec lain, dengan level Feature Suite Transfer `Basic`, Disposal `Basic`, dan Assignment `Basic`.

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

### Level Assignment Basic mengunci Direct handover between holders
10. Klik tab `Assign`
11. Verifikasi kontrol `Direct handover between holders` tidak dapat diubah karena disabled

### Level None: tab Transfer dan Disposal tidak dapat dibuka
12. Operator mengubah level Feature Suite Transfer entitas menjadi `None`
13. Operator mengubah level Feature Suite Disposal entitas menjadi `None`
14. Muat ulang halaman
15. Verifikasi header halaman memuat tombol `Export rules`
16. Verifikasi tab `Transfer` disabled
17. Arahkan pointer ke tab `Transfer`
18. Verifikasi alasan `Not available on your current plan` tersampaikan pada tab `Transfer` yang disabled
19. Verifikasi chip `Upgrade` pada tab `Transfer`
20. Klik tab `Transfer`
21. Verifikasi tab `Transfer` tidak menjadi tab aktif
22. Verifikasi tab `Disposal` disabled
23. Arahkan pointer ke tab `Disposal`
24. Verifikasi alasan `Not available on your current plan` tersampaikan pada tab `Disposal` yang disabled
25. Verifikasi chip `Upgrade` pada tab `Disposal`
26. Klik tab `Disposal`
27. Verifikasi tab `Disposal` tidak menjadi tab aktif
