---
id: TC-FA-ASSIGN-E2E-067-aksi-asset-list-level-none-dep-asset-list
title: "Asset List pada level None: aksi Assign dan Add to Assignment Draft tidak tampil, Mark as Unassigned untuk aset Assigned"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.10#r18", "§9.10#r22", "§9.10#r23", "ASSIGN-LOGIC-18f"]
smoke: []
dependsOn: ["Asset List: aksi baris Assign, Add to Assignment Draft, dan Mark as Unassigned"]
trace:
  "§9.10#r18": [3, 12, 13, 14, 20, 21, 22, 26]
  "§9.10#r22": 3
  "§9.10#r23": 7
  "ASSIGN-LOGIC-18f": [3, 12, 13, 14, 20, 21, 22]
anchor: [11, 25]
coverage:
  web: automated
---

# Asset List pada level None: aksi Assign dan Add to Assignment Draft tidak tampil, Mark as Unassigned untuk aset Assigned

## Prerequisites
- Aktor: Total Control `Rina Wahyuni {runId}` (DU-067-2) di entitas khusus DU-067-1 yang tidak dipakai spec lain
- Layar awal: Asset List
- Data:
  - DU-067-1: Entitas (Entitas khusus dengan Feature Suite Assignment level None), Name `Entitas None Asset List {runId}`, Level Feature Suite Assignment `None`, Level sebelumnya `Full`
  - DU-067-2: User (Aktor Total Control), Name `Rina Wahyuni {runId}`, Role `Total Control`, Cakupan `Seluruh client`
  - DU-067-3: User (Assignee Employee), Name `Hasan Basri {runId}`, Role `tanpa role Assignment`
  - DU-067-4: Group (Group aset), Name `Head Office {runId}`
  - DU-067-5: Asset (Aset Assigned untuk aksi baris dan bulk), Name `Kamera Fujifilm X-T4 {runId}`, Group `Head Office {runId}`, Custody `Assigned`, Assignee `Hasan Basri {runId}`
  - DU-067-6: Asset (Aset Assigned kedua untuk aksi bulk), Name `Lensa Canon RF 24-70 {runId}`, Group `Head Office {runId}`, Custody `Assigned`, Assignee `Hasan Basri {runId}`
  - DU-067-7: Asset (Aset Available untuk pembanding), Name `Scanner Epson DS-530 {runId}`, Group `Head Office {runId}`, Custody `Available`
- Kondisi:
  - Feature Suite Assignment pada entitas berada pada level `None` setelah turun dari `Full` pada T-0
  - Penugasan `Assigned` yang dibuat saat level `Full` tetap berjalan untuk aset `Kamera Fujifilm X-T4 {runId}` dan `Lensa Canon RF 24-70 {runId}`

## Test Steps

### Mark as Unassigned tampil pada baris aset Assigned
1. Ketik Search `Kamera Fujifilm X-T4 {runId}`, tekan Enter
2. Buka menu ⋯ pada baris aset `Kamera Fujifilm X-T4 {runId}`
3. Verifikasi aksi `Mark as Unassigned` tampil dan aktif pada baris aset yang Assigned
4. Tutup menu ⋯

### Pilihan hasil Mark as Unassigned untuk aset Assigned
5. Buka menu ⋯ pada baris aset `Kamera Fujifilm X-T4 {runId}`
6. Klik `Mark as Unassigned`
7. Verifikasi pilihan hasil `Unassigned`, `Missing`, dan `Damaged` tersedia untuk aset `Kamera Fujifilm X-T4 {runId}` pada dialog `Mark as Unassigned`
8. Klik `[Cancel]` pada dialog

### Aksi baris aset Available pada level None
9. Ganti isi kotak Search dengan `Scanner Epson DS-530 {runId}`, tekan Enter
10. Buka menu ⋯ pada baris aset `Scanner Epson DS-530 {runId}`
11. Verifikasi aksi `Detail` tampil pada baris aset `Scanner Epson DS-530 {runId}`
12. Verifikasi aksi `Assign` tidak tampil pada baris aset `Scanner Epson DS-530 {runId}`
13. Verifikasi aksi `Add to Assignment Draft` tidak tampil pada baris aset `Scanner Epson DS-530 {runId}`
14. Verifikasi aksi `Mark as Unassigned` tidak tampil pada baris aset `Scanner Epson DS-530 {runId}` yang bukan Assigned
15. Tutup menu ⋯

### Aksi bulk pada level None
16. Ganti isi kotak Search dengan `{runId}`, tekan Enter
17. Centang baris `Kamera Fujifilm X-T4 {runId}`
18. Centang baris `Lensa Canon RF 24-70 {runId}`
19. Centang baris `Scanner Epson DS-530 {runId}`
20. Verifikasi aksi `Mark as Unassigned` tampil pada menu aksi bulk
21. Verifikasi aksi `Assign` tidak tampil pada menu aksi bulk
22. Verifikasi aksi `Add to Assignment Draft` tidak tampil pada menu aksi bulk

### Aksi bulk tanpa aset Assigned pada level None
23. Hapus centang baris `Kamera Fujifilm X-T4 {runId}`
24. Hapus centang baris `Lensa Canon RF 24-70 {runId}`
25. Verifikasi baris `Scanner Epson DS-530 {runId}` tetap tercentang
26. Verifikasi aksi `Mark as Unassigned` tidak tampil pada menu aksi bulk saat hanya baris `Scanner Epson DS-530 {runId}` yang dicentang
