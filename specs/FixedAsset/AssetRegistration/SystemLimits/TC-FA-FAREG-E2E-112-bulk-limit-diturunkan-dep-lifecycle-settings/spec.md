---
id: TC-FA-FAREG-E2E-112-bulk-limit-diturunkan-dep-lifecycle-settings
title: "Register Asset Bulk Limit diturunkan: draft di atas limit baru"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [FAREG-LOGIC-03w, S-REG-21]
smoke: [S-REG-21]
dependsOn: ["Lifecycle Settings: tab System Limits"]
trace:
  FAREG-LOGIC-03w: [4, 8, 11, 14, 17, 21, 24, 29, 30]
  S-REG-21: [4, 5, 6]
anchor: [16]
coverage:
  web: automated
---

# Register Asset Bulk Limit diturunkan: draft di atas limit baru

## Prerequisites
- Aktor:
  - Rina, role Manage asset & TAG dengan Group terkelola `Gudang Limit {runId}` `Gudang Limit Submit {runId}`, dan capability Update pada node Group `Gudang Limit Approval {runId}`, sehingga berhak memutuskan pengajuan Siti pada Group itu.
  - Admin, role Total Control (seluruh client), hanya sebagai aktor lain yang mengubah Register Asset Bulk Limit di tab System Limits.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-112-1: Group `Gudang Limit {runId}`, ada di entitas aktor.
  - DU-112-2: Group `Gudang Limit Approval {runId}`, ada di entitas aktor.
  - DU-112-3: batch Draft `Gudang Limit {runId}` berisi 1 Item Asset Name `Kursi Limit {runId}` dengan TAG Type `Non-TAG`, Brand `Ergotec`, Model `No Model`, Quantity `8`.
  - DU-112-4: pengajuan berstatus Waiting for Approval milik Siti (Manage asset & TAG) di Group `Gudang Limit Approval {runId}`, berisi 8 aset Asset Name `Kursi Limit {runId}`.
  - DU-112-5: Register Asset Bulk Limit `100` saat spec dimulai, diturunkan menjadi `5` oleh langkah 1, dan dikembalikan menjadi `100` oleh langkah 31.
  - DU-112-7: batch Draft `Gudang Limit Submit {runId}` berisi 1 Item Asset Name `Kursi Limit {runId}` dengan TAG Type `Non-TAG`, Brand `Ergotec`, Model `No Model`, Quantity `8`.
  - DU-112-6: Quantity `5` yang diketik Rina untuk mengurangi total aset.
- Kondisi: Register Asset Bulk Limit bernilai `100` saat spec dimulai.

## Test Steps

### Draft di atas limit baru tetap dapat dibuka dengan Alert
1. Admin menurunkan Register Asset Bulk Limit di tab System Limits menjadi `5`
2. Ketik Search `Gudang Limit {runId}`, tekan Enter
3. Klik row action `Edit` pada baris batch `Gudang Limit {runId}`
4. Verifikasi `Alert` Warning `For more than 5 assets, use Import.` tampil di atas form
5. Verifikasi tautan ke Import tampil pada `Alert` itu
6. Verifikasi tidak ada error inline pada Quantity selama `Alert` tampil

### Save draft diblokir sampai total aset dikurangi
7. Klik `[Save draft]`
8. Verifikasi error pada Quantity `For more than 5 assets, use Import.`
9. Ganti Quantity menjadi `5`
10. Klik `[Save draft]`
11. Verifikasi toast `Success, draft has been saved.`

### Pengajuan Waiting for Approval tidak dievaluasi ulang
12. Buka Fixed Asset > Assets > Registration > Waiting for Approval
13. Ketik Search `Gudang Limit Approval {runId}`, tekan Enter
14. Verifikasi baris pengajuan `Gudang Limit Approval {runId}` tetap tampil dengan Total Asset `8`
15. Klik row action `Detail` pada baris pengajuan `Gudang Limit Approval {runId}`
16. Verifikasi Badge status `Waiting for Approval` tampil pada header Detail pengajuan
17. Verifikasi `Alert` `For more than 5 assets, use Import.` tidak tampil pada Detail pengajuan
18. Buka Approvals > Registration > Active
19. Ketik Search `Gudang Limit Approval {runId}`, tekan Enter
20. Klik row action `Review` pada baris pengajuan `Gudang Limit Approval {runId}`
21. Verifikasi Total Asset `8` tampil pada halaman Approval, di atas limit `5`
22. Klik `[Submit]` dengan Decision semua aset tetap `Approve`
23. Klik `[Submit]` pada dialog `Submit Approval`
24. Verifikasi toast `Success, registration request has been decided.`

### Submit diblokir pada draft di atas limit baru
25. Buka Fixed Asset > Assets > Registration > Draft
26. Ketik Search `Gudang Limit Submit {runId}`, tekan Enter
27. Klik row action `Edit` pada baris batch `Gudang Limit Submit {runId}`
28. Klik `[Submit]`
29. Verifikasi error pada Quantity `For more than 5 assets, use Import.`
30. Verifikasi dialog dengan `Are you sure you want to activate it?` tidak tampil
31. Admin mengembalikan Register Asset Bulk Limit di tab System Limits menjadi `100`
