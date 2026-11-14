---
id: TC-FA-FATR-E2E-028-plan-assignment
title: "Level Feature Suite Assignment Basic dan None"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceRules: [§4.1#r248, §4.1#r249, §9.4.2#r16, §9.4.2#r25, §9.4.2#r38, §9.4.4#r2, §9.4.4#r56, §Aturan Logika Modul#r107, §Aturan Logika Modul#r110, §9.2#b560, §9.10.3#r6, §9.10.3#b2]
smoke: [§Aturan Logika Modul#r107, §Aturan Logika Modul#r110, §9.2#b560, §9.10.3#r6, §9.10.3#b2]
dependsOn: []
trace:
  §4.1#r248: 14
  §4.1#r249: [15, 17]
  §9.4.2#r16: [27, 29, 30, 32]
  §9.4.2#r25: [15, 20, 22]
  §9.4.2#r38: 15
  §9.4.4#r2: [27, 29, 30]
  §9.4.4#r56: 15
  §Aturan Logika Modul#r107: 12
  §Aturan Logika Modul#r110: 32
  §9.2#b560: 15
  §9.10.3#r6: [10, 11]
  §9.10.3#b2: 15
anchor: [3, 5, 26]
coverage:
  web: automated
---

# Level Feature Suite Assignment Basic dan None

## Prerequisites
- Aktor: Total Control (Rina Wulandari {runId}). Operator Admin Console memicu perubahan level plan entitas.
- Layar awal: Fixed Asset > Settings > Transaction Settings.
- Data:
  - DU-028-1: Entitas `Entitas Plan Assignment {runId}`, entitas khusus yang tidak dipakai spec lain, level Feature Suite Assignment `Full`. Company default menyimpan Direct handover between holders `Allow`.
  - DU-028-4: Override dengan Scope `Group`, Target `Proyek Bekasi {runId}`, Overridden `Direct handover between holders (Allow)`, Category `All categories`, Created By `Rina Wulandari {runId}`.
  - DU-028-5: Group `Proyek Bekasi {runId}` ada di entitas ini.

## Test Steps

### Level Full: Direct handover between holders dapat diubah dan override tampil
1. Klik `All categories` pada Sidebar Category Tree
2. Klik tab `Assign`
3. Verifikasi kontrol `Direct handover between holders` aktif
4. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
5. Verifikasi baris override dengan Target `Proyek Bekasi {runId}` memuat Overridden `Direct handover between holders (Allow)`

### Level Basic mengunci Direct handover between holders
6. Operator mengubah level Feature Suite Assignment entitas menjadi `Basic`
7. Muat ulang halaman
8. Klik `All categories` pada Sidebar Category Tree
9. Klik tab `Assign`
10. Verifikasi kontrol `Direct handover between holders` disabled
11. Verifikasi kontrol `Allowed assignee: Division` aktif
12. Verifikasi `Direct handover between holders` tetap bernilai `Allow`

### Override Direct handover between holders tidak berlaku pada Basic
13. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
14. Verifikasi baris override dengan Target `Proyek Bekasi {runId}` tetap memuat Overridden `Direct handover between holders (Allow)`
15. Verifikasi sel Target baris `Proyek Bekasi {runId}` memuat Badge `Not applied`
16. Arahkan pointer ke Badge `Not applied` pada baris `Proyek Bekasi {runId}`
17. Verifikasi alasan `Available on plans with full Assignment` tersampaikan pada Badge `Not applied`

### Opsi Direct handover between holders di Dialog Add override disabled
18. Klik `[+ Override]`
19. Klik select Field pada baris Field + Value pertama
20. Verifikasi opsi `Direct handover between holders` disabled
21. Arahkan pointer ke opsi `Direct handover between holders`
22. Verifikasi alasan `Available on plans with full Assignment` tersampaikan pada opsi `Direct handover between holders` yang disabled
23. Klik `✕` pada dialog Add override, form belum diubah

### Level None: tab Assign tidak dapat dibuka
24. Operator mengubah level Feature Suite Assignment entitas menjadi `None`
25. Muat ulang halaman
26. Verifikasi `Export rules` pada header halaman tampil
27. Verifikasi tab `Assign` disabled
28. Arahkan pointer ke tab `Assign`
29. Verifikasi alasan `Not available on your current plan` tersampaikan pada tab `Assign` yang disabled
30. Verifikasi chip `Upgrade` pada tab `Assign`
31. Klik tab `Assign`
32. Verifikasi tab `Assign` tidak menjadi tab aktif
