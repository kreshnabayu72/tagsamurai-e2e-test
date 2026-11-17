---
id: TC-FA-FATR-E2E-026-plan-approval
title: "Approval Workflow tidak tersedia di plan"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: [§4.1#r275, §4.1#r276, §9.4.2#r25, §9.10.1#b5, §9.10.1#p7, §9.10.1#p11, §9.10.1#p12, §Aturan Logika Modul#r80, §9.2#b555, §9.4.2#r100, §9.10.1#r5, §9.10.1#r8, §9.10.1#b3, §9.10.1#b4, §9.10.1#r9]
smoke: [§Aturan Logika Modul#r80, §9.2#b555, §9.4.2#r100, §9.10.1#r5, §9.10.1#r8, §9.10.1#b3, §9.10.1#b4, §9.10.1#r9]
dependsOn: []
trace:
  §4.1#r275: [13]
  §4.1#r276: [14]
  §9.4.2#r25: [14, 19, 21]
  §9.10.1#b5: [14, 16, 21]
  §9.10.1#p7: [3, 5, 12]
  §9.10.1#p11: [4, 5]
  §9.10.1#p12: [12]
  §Aturan Logika Modul#r80: [5]
  §9.2#b555: [3]
  §9.4.2#r100: [4]
  §9.10.1#r5: [3]
  §9.10.1#r8: [6]
  §9.10.1#b3: [4]
  §9.10.1#b4: [8, 10]
  §9.10.1#r9: [3]
anchor: []
coverage:
  web: automated
---

# Approval Workflow tidak tersedia di plan

## Prerequisites
- Aktor: Total Control pada entitas khusus `Citra Distribusi {runId}` (DU-026-1), yang tidak dipakai spec lain.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-026-1: entitas `Citra Distribusi {runId}` dengan plan `Growth`.
  - DU-026-2: Company default Require approval Borrow tersimpan `ON`.
  - DU-026-3: Company default Require approval Assign tersimpan `ON`.
  - DU-026-4: Category leaf `Vehicle > Pool car {runId}`.
  - DU-026-5: Group `Workshop {runId}`.
  - DU-026-6: override dengan Scope `Group`, Target `Workshop {runId}`, Overridden `Require approval (OFF)`, Category `Vehicle > Pool car {runId}`, transaksi `Borrow`.
- Kondisi: plan entitas tidak menyertakan Approval Workflow, sedangkan Feature Suite Borrowing dan Assignment bernilai `Basic`.

## Test Steps

### Field bergerbang disabled dan nilai tersimpan dipertahankan
1. Klik `All categories` di Sidebar Category Tree
2. Klik tab `Borrow`
3. Verifikasi Alert `Approval Workflow isn't available on your plan. Transactions run without approval.` tampil di bagian Approval
4. Verifikasi field `Require approval` disabled
5. Verifikasi field `Require approval` bernilai `ON`
6. Verifikasi field `Max duration` aktif

### Reset to Default tidak menyentuh field bergerbang
7. Klik tab `Assign`
8. Verifikasi field `Require approval` pada tab `Assign` bernilai `ON`
9. Klik `[Reset to Default]`
10. Verifikasi field `Require approval` pada tab `Assign` tetap bernilai `ON`

### Override lama tetap tersimpan dan tampil dengan Badge Not applied
11. Klik tab `Borrow`
12. Verifikasi baris override Group `Workshop {runId}` tampil di tabel Overrides
13. Verifikasi kolom Overridden baris itu menampilkan `Require approval (OFF)`
14. Verifikasi sel Target baris itu menampilkan badge `Not applied`
15. Arahkan pointer ke badge `Not applied` pada baris `Workshop {runId}`
16. Verifikasi alasan `Requires Approval Workflow on your plan.` tersampaikan pada badge `Not applied`

### Opsi field bergerbang di Dialog Add override disabled
17. Klik `[+ Override]`
18. Klik Select field pada baris Field + Value pertama
19. Verifikasi opsi `Require approval` disabled
20. Arahkan pointer ke opsi `Require approval` yang disabled
21. Verifikasi alasan `Requires Approval Workflow on your plan.` tersampaikan pada opsi `Require approval` yang disabled
22. Klik `✕` pada Dialog Add override, form belum diubah
