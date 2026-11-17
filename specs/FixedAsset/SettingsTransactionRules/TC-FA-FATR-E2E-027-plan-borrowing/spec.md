---
id: TC-FA-FATR-E2E-027-plan-borrowing
title: "Level Feature Suite Borrowing Basic dan None"
layer: ui-e2e
priority: High
caseType: Negative
status: ready-for-automation
sourceRules: [§4.1#r275, §4.1#r276, §9.4.2#r16, §9.4.2#r25, §9.4.2#r38, §9.4.4#r2, §9.4.4#r56, §Aturan Logika Modul#r89, §Aturan Logika Modul#r92, §4.3#r13, §9.2#b557, §9.10.2#r6, §9.10.2#b3, §9.10.2#r10]
smoke: [§Aturan Logika Modul#r89, §Aturan Logika Modul#r92, §4.3#r13, §9.2#b557, §9.10.2#r6, §9.10.2#b3, §9.10.2#r10]
dependsOn: []
trace:
  §4.1#r275: 17
  §4.1#r276: [18, 20]
  §9.4.2#r16: [31, 33, 34, 36]
  §9.4.2#r25: [18, 23, 24, 26]
  §9.4.2#r38: 18
  §9.4.4#r2: [31, 33, 34]
  §9.4.4#r56: 18
  §Aturan Logika Modul#r89: [14, 15]
  §Aturan Logika Modul#r92: 36
  §4.3#r13: [33, 34, 36]
  §9.2#b557: 18
  §9.10.2#r6: [11, 12, 13]
  §9.10.2#b3: 11
  §9.10.2#r10: 18
anchor: [3, 4, 6, 30]
coverage:
  web: automated
---

# Level Feature Suite Borrowing Basic dan None

## Prerequisites
- Aktor: Total Control (Rina Wulandari {runId}). Operator Admin Console memicu perubahan level plan entitas.
- Layar awal: Fixed Asset > Settings > Transaction Settings.
- Data:
  - DU-027-1: Entitas `Entitas Plan Borrowing {runId}`, entitas khusus yang tidak dipakai spec lain, level Feature Suite Borrowing `Full`. Company default menyimpan Self service `ON` dan Duration unit `Hours`.
  - DU-027-4: Override dengan Scope `Group`, Target `Workshop {runId}`, Overridden `Self service (ON), Duration unit (Hours)`, Category `All categories`, Created By `Rina Wulandari {runId}`.
  - DU-027-5: Group `Workshop {runId}` ada di entitas ini.

## Test Steps

### Level Full: field Borrow dapat diubah dan override tampil
1. Klik `All categories` pada Sidebar Category Tree
2. Klik tab `Borrow`
3. Verifikasi kontrol `Self service` aktif
4. Verifikasi kontrol `Duration unit` aktif
5. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
6. Verifikasi baris override dengan Target `Workshop {runId}` memuat Overridden `Self service (ON), Duration unit (Hours)`

### Level Basic mengunci Self service dan Duration unit
7. Operator mengubah level Feature Suite Borrowing entitas menjadi `Basic`
8. Muat ulang halaman
9. Klik `All categories` pada Sidebar Category Tree
10. Klik tab `Borrow`
11. Verifikasi kontrol `Self service` disabled
12. Verifikasi kontrol `Duration unit` disabled
13. Verifikasi kontrol `Max duration` aktif
14. Verifikasi `Self service` tetap bernilai `ON`
15. Verifikasi `Duration unit` tetap bernilai `Hours`

### Override Self service dan Duration unit tidak berlaku pada Basic
16. Ketik Search `{runId}` pada tabel Overrides, tekan Enter
17. Verifikasi baris override dengan Target `Workshop {runId}` tetap memuat Overridden `Self service (ON), Duration unit (Hours)`
18. Verifikasi sel Target baris `Workshop {runId}` memuat Badge `Not applied`
19. Arahkan pointer ke Badge `Not applied` pada baris `Workshop {runId}`
20. Verifikasi alasan `Available on plans with full Borrowing.` tersampaikan pada Badge `Not applied`

### Opsi field bergerbang di Dialog Add override disabled
21. Klik `[+ Override]`
22. Klik select Field pada baris Field + Value pertama
23. Verifikasi opsi `Self service` disabled
24. Verifikasi opsi `Duration unit` disabled
25. Arahkan pointer ke opsi `Self service`
26. Verifikasi alasan `Available on plans with full Borrowing.` tersampaikan pada opsi `Self service` yang disabled
27. Klik `✕` pada dialog Add override, form belum diubah

### Level None: tab Borrow tidak dapat dibuka
28. Operator mengubah level Feature Suite Borrowing entitas menjadi `None`
29. Muat ulang halaman
30. Verifikasi tombol `Export rules` tampil
31. Verifikasi tab `Borrow` disabled
32. Arahkan pointer ke tab `Borrow`
33. Verifikasi alasan `Not available on your current plan.` tersampaikan pada tab `Borrow` yang disabled
34. Verifikasi chip `Upgrade` pada tab `Borrow`
35. Klik tab `Borrow`
36. Verifikasi tab `Borrow` tidak menjadi tab aktif
