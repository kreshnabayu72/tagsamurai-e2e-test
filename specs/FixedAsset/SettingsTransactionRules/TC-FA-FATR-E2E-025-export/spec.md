---
id: TC-FA-FATR-E2E-025-export
title: "Export rules mengunduh berkas aturan node terpilih"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: [§4.4#r9, §7#r10, §9.2#b309, §9.2#b315, §9.2#b322, §9.4.2#r49, §9.4.2#r50, §9.4.4#r41, §9.6#r4, §9.11#r4, EB-FB-2@export-rules, §9.2#b310]
smoke: [§9.2#b310]
dependsOn: []
trace:
  §4.4#r9: [4, 5]
  §7#r10: [6]
  §9.2#b309: [4, 5]
  §9.2#b315: [12, 13]
  §9.2#b322: [5]
  §9.4.2#r49: [4, 6, 7]
  §9.4.2#r50: [16]
  §9.4.4#r41: [16]
  §9.6#r4: [5, 6]
  §9.11#r4: [8, 17]
  EB-FB-2@export-rules: [6]
  §9.2#b310: [8]
anchor: []
coverage:
  web: automated
---

# Export rules mengunduh berkas aturan node terpilih

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-025-1: Category leaf `Vehicle > Pool car {runId}` (nama node `Pool car {runId}`) dengan aturan Borrow Field `Max duration` bernilai sendiri `30 days` yang sudah tersimpan; di berkas export nilainya `30` dengan Unit `days`.
  - DU-025-2: nilai draft Field `Max duration` `45` pada Category `Vehicle > Pool car {runId}`, yang diketik tetapi tidak disimpan.
- Kondisi: cakupan Export rules pada node `All categories` menghasilkan lebih dari `5.000` baris di sheet `Rules`.

## Test Steps

### Export rules pada Category leaf mengunduh berkas tanpa dialog
1. Ketik Search Sidebar Category Tree `{runId}`, tekan Enter
2. Klik Category leaf `Pool car {runId}` di Sidebar Category Tree
3. Klik `[Export rules]`
4. Verifikasi tidak ada dialog yang terbuka
5. Verifikasi berkas Excel bernama `Transaction-Rules` terunduh
6. Verifikasi tidak ada toast sukses
7. Verifikasi berkas memuat sheet `Rules`, `Overrides`, dan `Info`
8. Verifikasi sheet `Info` baris `Category` bernilai `Vehicle > Pool car {runId}`

### Draft yang belum disimpan tidak ikut berkas
9. Klik tab `Borrow`
10. Ganti isi field `Max duration` dengan `45`
11. Klik `[Export rules]`
12. Verifikasi sheet `Rules` memuat baris Category `Vehicle > Pool car {runId}`, Transaction `Borrow`, Field `Max duration`, Value `30`
13. Verifikasi tidak ada baris Field `Max duration` bernilai `45` pada sheet `Rules`

### Export rules pada All categories dengan lebih dari 5.000 baris
14. Klik `All categories` di Sidebar Category Tree
15. Klik `[Export rules]`
16. Verifikasi berkas terunduh langsung setelah berkas siap
17. Verifikasi sheet `Info` baris `Category` bernilai `All categories`
