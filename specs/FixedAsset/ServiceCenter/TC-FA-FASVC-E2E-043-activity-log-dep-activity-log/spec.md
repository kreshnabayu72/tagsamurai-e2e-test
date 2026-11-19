---
id: TC-FA-FASVC-E2E-043-activity-log-dep-activity-log
title: "Activity Log: Entri Created, Updated, Inactivated, Activated, Deleted untuk Service Center"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FASVC-LOGIC-09c, "§8#r7"]
smoke: []
dependsOn: ["Activity Log: halaman Activity Log"]
trace:
  FASVC-LOGIC-09c: [19, 20, 21, 22, 23]
  "§8#r7": [19, 20, 21, 22, 23]
anchor: []
coverage:
  web: automated
---
# Activity Log: Entri Created, Updated, Inactivated, Activated, Deleted untuk Service Center

## Prerequisites
- Aktor: Total Control `Rina Wulandari {runId}` (cakupan seluruh Group).
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-043-1: Service Center `Bengkel Mitra Aktivitas {runId}` yang dibuat aktor, Service type `Routine`, Available to `All groups` (nilai awal Create), Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia` (nilai awal Create), City `Semarang` lalu diubah lewat Edit menjadi `Surabaya`, Company email `aktivitas@mitraaktivitas.example`, Usage `0`, dan pada akhirnya dihapus.
  - DU-043-2: User Total Control `Rina Wulandari {runId}`, cakupan seluruh Group.

## Test Steps

### Activity Log mencatat setiap aksi tulis dan Delete dengan Object Service Center dan nama snapshot
1. Klik `[+ Service Center]`
2. Isi Name `Bengkel Mitra Aktivitas {runId}`
3. Centang Service type `Routine`
4. Isi City `Semarang`
5. Isi Company email `aktivitas@mitraaktivitas.example`
6. Klik `[Submit]`
7. Ketik Search `Bengkel Mitra Aktivitas {runId}`, tekan Enter
8. Klik `⋯` pada baris `Bengkel Mitra Aktivitas {runId}`, lalu klik `Edit`
9. Ganti isi field City dengan `Surabaya`
10. Klik `[Save]`
11. Klik `⋯` pada baris `Bengkel Mitra Aktivitas {runId}`, lalu klik `Inactivate`
12. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
13. Klik `⋯` pada baris `Bengkel Mitra Aktivitas {runId}`, lalu klik `Activate`
14. Klik `[Activate]` pada dialog `Activate Service Center`
15. Klik `⋯` pada baris `Bengkel Mitra Aktivitas {runId}`, lalu klik `Delete`
16. Klik `[Delete]` pada dialog `Delete Service Center`
17. Buka halaman Activity Log
18. Ketik Search `Bengkel Mitra Aktivitas {runId}`, tekan Enter
19. Verifikasi entri Activity Log dengan Action `Created`, Object `Service Center`, dan Name `Bengkel Mitra Aktivitas {runId}` tampil
20. Verifikasi entri Activity Log dengan Action `Updated`, Object `Service Center`, dan Name `Bengkel Mitra Aktivitas {runId}` tampil
21. Verifikasi entri Activity Log dengan Action `Inactivated`, Object `Service Center`, dan Name `Bengkel Mitra Aktivitas {runId}` tampil
22. Verifikasi entri Activity Log dengan Action `Activated`, Object `Service Center`, dan Name `Bengkel Mitra Aktivitas {runId}` tampil
23. Verifikasi entri Activity Log dengan Action `Deleted`, Object `Service Center`, dan Name `Bengkel Mitra Aktivitas {runId}` tampil
