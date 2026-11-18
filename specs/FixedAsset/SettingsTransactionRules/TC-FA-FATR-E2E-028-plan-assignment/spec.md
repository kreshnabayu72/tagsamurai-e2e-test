---
id: TC-FA-FATR-E2E-028-plan-assignment
title: "Level Feature Suite Assignment None dan Basic"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [§9.4.2#r16, §9.4.4#r2, §Aturan Logika Modul#r106, §9.10.3#r6, §9.4.2#r25, FLD-08, FLD-09, FLD-08d, FLD-09a, FATR-LOGIC-14b, FATR-LOGIC-14c, FATR-LOGIC-14d, FATR-LOGIC-14e, FATR-LOGIC-14f, FATR-LOGIC-14h, FATR-LOGIC-14i, S-23c, FLD-36s]
smoke: [§Aturan Logika Modul#r106, §9.10.3#r6]
dependsOn: []
trace:
  §9.4.2#r16: [4, 6]
  §9.4.4#r2: [4, 6]
  §Aturan Logika Modul#r106: 6
  §9.10.3#r6: [4, 6]
  §9.4.2#r25: [22, 23]
  FLD-08: [14, 16, 23, 29]
  FLD-09: [10, 11, 13, 19, 22, 28, 31]
  FLD-08d: [14, 16]
  FLD-09a: [10, 11, 13]
  FATR-LOGIC-14b: [10, 11, 13, 22]
  FATR-LOGIC-14c: [14, 16, 23]
  FATR-LOGIC-14d: [10, 13, 14, 16]
  FATR-LOGIC-14e: [11, 28]
  FATR-LOGIC-14f: [18, 19, 22, 23]
  FATR-LOGIC-14h: [4]
  FATR-LOGIC-14i: [6]
  S-23c: [10, 13, 14, 16]
  FLD-36s: [22, 23]
anchor: [3]
coverage:
  web: automated
---

# Level Feature Suite Assignment None dan Basic

## Prerequisites
- Aktor: Total Control (Rina Wulandari {runId}). Operator Admin Console memicu perubahan level plan entitas.
- Layar awal: Fixed Asset > Settings > Transaction Settings.
- Data:
  - DU-028-1: Entitas `Entitas Plan Assignment {runId}`, entitas khusus yang tidak dipakai spec lain, level Feature Suite Assignment `Full`. Company default tab Assign pada All categories menyimpan Allowed assignee: Employee `ON` dan Allowed assignee: Division `ON`.
  - DU-028-2: Override dengan Scope `Group`, Target `Divisi Plan {runId}`, Overridden `Allowed assignee: Division (OFF)`, Category `All categories`, transaksi `Assign`, Created By `Rina Wulandari {runId}`; Group `Divisi Plan {runId}` ada di entitas ini.

## Test Steps

### Level None: tab Assign tidak tampil
1. Operator mengubah level Feature Suite Assignment entitas menjadi `None`
2. Muat ulang halaman
3. Verifikasi `Export rules` pada toolbar kartu tampil
4. Verifikasi tab `Assign` tidak tampil pada daftar tab
5. Buka langsung URL Transaction Settings dengan tab `Assign`
6. Verifikasi tab `Assign` tetap tidak tampil dan tidak menjadi tab aktif

### Level Basic: Allowed assignee: Division dan Allowed assignee: Employee terkunci
7. Operator mengubah level Feature Suite Assignment entitas menjadi `Basic`
8. Muat ulang halaman
9. Klik `All categories` pada Sidebar Category Tree, lalu klik tab `Assign`
10. Verifikasi kontrol `Allowed assignee: Division` disabled
11. Verifikasi `Allowed assignee: Division` tetap bernilai `ON`
12. Arahkan pointer ke kontrol `Allowed assignee: Division` yang disabled
13. Verifikasi alasan `Available on plans with full Assignment.` tersampaikan pada kontrol `Allowed assignee: Division` yang disabled
14. Verifikasi kontrol `Allowed assignee: Employee` disabled
15. Arahkan pointer ke kontrol `Allowed assignee: Employee` yang disabled
16. Verifikasi alasan `Available on plans with full Assignment.` tersampaikan pada kontrol `Allowed assignee: Employee` yang disabled
17. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
18. Verifikasi baris override dengan Target `Divisi Plan {runId}` tetap memuat Overridden `Allowed assignee: Division (OFF)`
19. Verifikasi sel Target baris `Divisi Plan {runId}` memuat Badge `Not applied`
20. Klik `[+ Override]`
21. Klik select Field pada baris Field + Value pertama
22. Verifikasi opsi `Allowed assignee: Division` disabled
23. Verifikasi opsi `Allowed assignee: Employee` disabled
24. Klik `✕` pada Dialog Add override, form belum diubah

### Upgrade ke Full: Allowed assignee: Division aktif kembali dengan nilai tersimpan
25. Operator mengubah level Feature Suite Assignment entitas menjadi `Full`
26. Muat ulang halaman
27. Klik `All categories` pada Sidebar Category Tree, lalu klik tab `Assign`
28. Verifikasi kontrol `Allowed assignee: Division` aktif dan bernilai `ON`
29. Verifikasi kontrol `Allowed assignee: Employee` aktif
30. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
31. Verifikasi sel Target baris `Divisi Plan {runId}` tidak memuat Badge `Not applied`
