---
id: TC-FA-FATR-E2E-030-suspended
title: "Entitas Suspended atau Expired memblok Save, Add override, dan Delete override"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§7#r9", "§9.2#b49", "§9.2#b62", "§9.2#b168", "§9.2#b169", "§9.4.2#r24", "§9.4.2#r31", "§9.4.2#r52", "§9.4.2#r85", "§9.4.2#r86", "§9.4.2#r87", "§9.4.3#b1", "§9.4.4#r16", "§9.4.4#r28", "§9.4.4#r43", "EB-AKS-7", "§9.2#b50", "§9.2#b375"]
smoke: ["§9.2#b50", "§9.2#b375"]
dependsOn: []
trace:
  "§7#r9": 6
  "§9.2#b49": [6, 16, 32]
  "§9.2#b62": 6
  "§9.2#b168": [16, 21]
  "§9.2#b169": 32
  "§9.4.2#r24": [16, 17]
  "§9.4.2#r31": [32, 33]
  "§9.4.2#r52": [23, 25]
  "§9.4.2#r85": 6
  "§9.4.2#r86": 7
  "§9.4.2#r87": [23, 25]
  "§9.4.3#b1": [6, 16, 32]
  "§9.4.4#r16": [6, 27]
  "§9.4.4#r28": [16, 27, 32]
  "§9.4.4#r43": [23, 25]
  "EB-AKS-7": [6, 16, 32]
  "§9.2#b50": 25
  "§9.2#b375": 23
anchor: [20, 26]
coverage:
  web: automated
---

# Entitas Suspended atau Expired memblok Save, Add override, dan Delete override

## Prerequisites
- Aktor: Total Control pada entitas khusus yang tidak dipakai spec lain.
- Layar awal: Settings > Transaction Settings
- Data:
  - DU-030-1: entitas khusus `Entitas Suspended {runId}` dengan status `Suspended`.
  - DU-030-2: Category leaf `Laptop {runId}` dengan Max extensions bernilai sendiri `1` pada tab Borrow.
  - DU-030-3: Group `Proyek Karawang {runId}`, ada di entitas aktor.
  - DU-030-4: Group `Workshop {runId}`, ada di entitas aktor.
  - DU-030-5: override Scope `Group`, Target `Proyek Karawang {runId}`, Overridden `Max extensions (2)`, Category `Laptop {runId}`, transaksi `Borrow`.
  - DU-030-8: entri Changelog Category `Laptop {runId}`, Field `Borrow (Max extensions)`, Old Value `Inherit`, New Value `1`, Action `Edit`, Modified By `Rina Wulandari` (tampil `Rina W`), Date `T0 − 1 hari`.
- Kondisi: entitas aktor berstatus Suspended. Changelog entitas itu hanya memuat entri DU-030-8.

## Test Steps

### Save Changes ditolak saat entitas Suspended
1. Pilih Category `Laptop {runId}` pada Sidebar Category Tree
2. Klik tab `Borrow`
3. Ubah Max extensions menjadi `3`
4. Klik `[Save]`
5. Klik `[Save]` pada dialog Save Changes
6. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
7. Verifikasi kontrol Max extensions masih menampilkan `3` sebagai draft

### Add override ditolak saat entitas Suspended
8. Klik `[+ Override]`
9. Pilih Scope `Group`
10. Klik `[Select Group]`
11. Centang `Workshop {runId}` pada dialog Select Group
12. Klik `[Select]`
13. Pilih Field `Max extensions`
14. Isi Value `2`
15. Klik `[Submit]`
16. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
17. Verifikasi dialog `Add override - Borrow` tetap terbuka
18. Klik `✕` pada dialog Add override, lalu klik `[Leave]` pada dialog Unsaved Changes
19. Ketik Search `{runId}`, tekan Enter
20. Verifikasi baris `Proyek Karawang {runId}` tampil di tabel Overrides
21. Verifikasi baris `Workshop {runId}` tidak tampil di tabel Overrides

### Export rules dan Changelog tetap dapat dibaca saat entitas Suspended
22. Klik `[Export rules]`
23. Verifikasi berkas `Transaction-Rules` terunduh
24. Klik ikon Changelog di header
25. Verifikasi dialog `Changelog: Transaction Settings` terbuka
26. Verifikasi baris dengan Category `Laptop {runId}`, Field `Borrow (Max extensions)`, Old Value `Inherit`, dan New Value `1` tampil di tabel Changelog
27. Verifikasi tidak ada baris dengan Field `Borrow (Max extensions)` dan New Value `3` di tabel Changelog
28. Tekan `Esc` untuk menutup dialog Changelog

### Delete override ditolak saat entitas Suspended
29. Klik `⋯` pada baris `Proyek Karawang {runId}`
30. Klik `Delete`
31. Klik `[Delete]` pada dialog Delete Override
32. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
33. Verifikasi baris `Proyek Karawang {runId}` tetap tampil di tabel Overrides
