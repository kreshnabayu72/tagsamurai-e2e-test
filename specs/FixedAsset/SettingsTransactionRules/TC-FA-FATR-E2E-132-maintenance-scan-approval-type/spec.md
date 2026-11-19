---
id: TC-FA-FATR-E2E-132-maintenance-scan-approval-type
title: "Tab Maintenance: Require scan to start dan Approval type tersimpan, tersembunyi, dan diwarisi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FATR-LOGIC-17a, FLD-42, FLD-42c, FLD-29e, FLD-29f, FLD-29g, FLD-41]
smoke: []
dependsOn: []
trace:
  FATR-LOGIC-17a: [3, 7]
  FLD-42: [3, 14, 31]
  FLD-42c: [31]
  FLD-29e: [7, 15]
  FLD-29f: [4, 7, 23, 25]
  FLD-29g: [32, 39, 40]
  FLD-41: [22, 27]
anchor: []
coverage:
  web: automated
---

# Tab Maintenance: Require scan to start dan Approval type tersimpan, tersembunyi, dan diwarisi

## Prerequisites
- Aktor: Total Control, berwenang atas seluruh Group di entitas DU-132-4.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-132-4: Entitas `Grafika Scan {runId}`, entitas khusus yang hanya dipakai spec ini dan tidak dipakai spec lain. Plan-nya menyediakan Approval Workflow, dan addon Maintenance aktif pada subscription FAMS-nya.
  - DU-132-1: Category `Mesin Cetak Scan {runId}`, Category leaf tingkat teratas tanpa sub-Category, ada di entitas DU-132-4; semua field tab Maintenance Inherit.
  - DU-132-2: Company default tab Maintenance entitas DU-132-4 pada All categories saat spec dimulai bernilai bawaan: Require scan to start `OFF`, Require approval to close `OFF`, Approval type `Any one approver`.
  - DU-132-5: Company default tab Maintenance yang disimpan spec ini pada All categories: Require scan to start `ON`, Require approval to close `ON`, Approval type `All approvers (AND)`.
  - DU-132-3: Perubahan Category `Mesin Cetak Scan {runId}` tab Maintenance: Approval type `Any one approver`.
- Kondisi:
  - Plan entitas DU-132-4 menyediakan Approval Workflow, sehingga Require approval to close dan Approval type bisa diubah.
  - Company default tab Maintenance entitas DU-132-4 bernilai bawaan sesuai DU-132-2.

## Test Steps

### Bawaan: Approval type tersembunyi sampai Require approval to close ON, lalu tersimpan di Company default
1. Klik `All categories` pada Sidebar Category Tree
2. Klik tab `Maintenance`
3. Verifikasi bagian `Routine` memuat `Require scan to start` bernilai `OFF`
4. Verifikasi `Approval type` tidak tampil pada bagian `Routine`
5. Klik switch `Require scan to start` sehingga bernilai `ON`
6. Klik switch `Require approval to close` sehingga bernilai `ON`
7. Verifikasi bagian `Routine` memuat `Approval type` bernilai `Any one approver`
8. Pilih `All approvers (AND)` pada `Approval type`
9. Klik `[Save]`
10. Klik `[Save]` pada dialog Save Changes
11. Muat ulang halaman
12. Klik `All categories` pada Sidebar Category Tree
13. Klik tab `Maintenance`
14. Verifikasi `Require scan to start` bernilai `ON`
15. Verifikasi `Approval type` bernilai `All approvers (AND)`

### Require approval to close OFF menyembunyikan Approval type dan nilai tersimpan dipertahankan
16. Klik switch `Require approval to close` sehingga bernilai `OFF`
17. Klik `[Save]`
18. Klik `[Save]` pada dialog Save Changes
19. Muat ulang halaman
20. Klik `All categories` pada Sidebar Category Tree
21. Klik tab `Maintenance`
22. Verifikasi `Require approval to close` bernilai `OFF`
23. Verifikasi `Approval type` tidak tampil pada bagian `Routine`
24. Klik switch `Require approval to close` sehingga bernilai `ON`
25. Verifikasi `Approval type` bernilai `All approvers (AND)`
26. Klik `[Save]`
27. Verifikasi dialog Save Changes tampil dan memuat perubahan `Require approval to close`
28. Klik `[Save]` pada dialog Save Changes

### Category leaf tanpa nilai sendiri mewarisi Require scan to start dan Approval type
29. Ketik Search Sidebar Category Tree `Mesin Cetak Scan {runId}`, tekan Enter
30. Klik Category leaf `Mesin Cetak Scan {runId}`
31. Verifikasi `Require scan to start` menampilkan teks Inherit dengan nilai `ON` dan sumber `Company default`
32. Verifikasi `Approval type` menampilkan teks Inherit dengan nilai `All approvers (AND)` dan sumber `Company default`

### Perubahan Approval type pada Category leaf tercatat di Changelog
33. Klik `[Set own value]` pada field `Approval type`
34. Pilih `Any one approver` pada `Approval type`
35. Klik `[Save]`
36. Klik `[Save]` pada dialog Save Changes
37. Klik ikon Changelog di header
38. Ketik Search `Mesin Cetak Scan {runId}`, tekan Enter
39. Verifikasi tabel Changelog memuat baris dengan Field `Maintenance (Approval type)`
40. Verifikasi baris Changelog itu memuat Category `Mesin Cetak Scan {runId}`
41. Tekan `Esc` untuk menutup dialog Changelog
