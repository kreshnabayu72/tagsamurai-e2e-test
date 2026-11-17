---
id: TC-FA-FATR-E2E-122-tab-maintenance
title: "Tab Maintenance: Category leaf mewarisi Company default dan perubahannya tercatat di Changelog"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.4.2#r71", "§Aturan Logika Modul#r121", "§4.1#r58", "§9.2#b566"]
smoke: []
dependsOn: []
trace:
  "§9.4.2#r71": [12, 13, 14, 18, 19, 20]
  "§Aturan Logika Modul#r121": [11, 17, 18, 19, 20]
  "§4.1#r58": [27, 28]
  "§9.2#b566": [18, 19, 20, 27, 28]
anchor: []
coverage:
  web: automated
---

# Tab Maintenance: Category leaf mewarisi Company default dan perubahannya tercatat di Changelog

## Prerequisites
- Aktor: Total Control, berwenang atas seluruh Group di entitas DU-122-4.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-122-4: Entitas `Grafika Nusantara {runId}`, entitas khusus yang hanya dipakai spec ini dan tidak dipakai spec lain. Plan-nya menyediakan Approval Workflow, dan addon Maintenance aktif pada subscription FAMS-nya.
  - DU-122-1: Category `Mesin Cetak {runId}`, Category leaf tingkat teratas tanpa sub-Category, ada di entitas DU-122-4; semua field tab Maintenance Inherit.
  - DU-122-2: Company default tab Maintenance entitas DU-122-4 pada All categories saat spec dimulai bernilai bawaan: Reminder before due `3`, Photo after `ON`, Require approval to close `OFF`.
  - DU-122-5: Company default tab Maintenance yang disimpan spec ini pada All categories: Reminder before due `9`, Photo after `OFF`, Require approval to close `ON`. Teks warisan Reminder before due yang diharapkan `9 days`, dari Reminder before due `9` (days) di Company default.
  - DU-122-3: Perubahan Category `Mesin Cetak {runId}` tab Maintenance: Reminder before due `5`.
- Kondisi:
  - Plan entitas DU-122-4 menyediakan Approval Workflow, sehingga Require approval to close bisa diubah.
  - Company default tab Maintenance entitas DU-122-4 bernilai bawaan sesuai DU-122-2.

## Test Steps

### Company default tab Maintenance disimpan dengan nilai selain bawaan
1. Klik `All categories` pada Sidebar Category Tree
2. Klik tab `Maintenance`
3. Isi `Reminder before due` `9`
4. Klik switch `Photo after` sehingga bernilai `OFF`
5. Klik switch `Require approval to close` sehingga bernilai `ON`
6. Klik `[Save]`
7. Klik `[Save]` pada dialog Save Changes
8. Muat ulang halaman
9. Klik `All categories` pada Sidebar Category Tree
10. Klik tab `Maintenance`
11. Verifikasi Sidebar Category Tree tampil pada tab `Maintenance` dengan node `All categories` terpilih
12. Verifikasi field `Reminder before due` bernilai `9`
13. Verifikasi field `Photo after` bernilai `OFF`
14. Verifikasi field `Require approval to close` bernilai `ON`

### Category leaf tanpa nilai sendiri mewarisi nilai Company default tersimpan
15. Ketik Search Sidebar Category Tree `Mesin Cetak {runId}`, tekan Enter
16. Klik Category leaf `Mesin Cetak {runId}`
17. Verifikasi Sidebar Category Tree tampil pada tab `Maintenance` dengan node `Mesin Cetak {runId}` terpilih
18. Verifikasi `Reminder before due` menampilkan teks Inherit dengan nilai `9 days` dan sumber `Company default`
19. Verifikasi `Photo after` menampilkan teks Inherit dengan nilai `OFF` dan sumber `Company default`
20. Verifikasi `Require approval to close` menampilkan teks Inherit dengan nilai `ON` dan sumber `Company default`

### Perubahan nilai Category leaf tercatat di Changelog dengan Category yang diubah
21. Klik `[Set own value]` pada field `Reminder before due`
22. Isi `Reminder before due` `5`
23. Klik `[Save]`
24. Klik `[Save]` pada dialog Save Changes
25. Klik ikon Changelog di header
26. Ketik Search `Mesin Cetak {runId}`, tekan Enter
27. Verifikasi tabel Changelog memuat baris dengan Field `Maintenance (Reminder before due)`
28. Verifikasi baris Changelog itu memuat Category `Mesin Cetak {runId}`
29. Tekan `Esc` untuk menutup dialog Changelog
