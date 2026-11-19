---
id: TC-FA-FASVC-E2E-048-service-type-dipakai-tidak-bisa-dilepas-dep-maintenance-routine
title: "Service Type yang Dipakai Schedule Aktif atau Task Terbuka: Checkbox Disabled dan Tidak Bisa Dilepas"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: [FASVC-LOGIC-07h, F-FASVC-02.k5]
smoke: []
dependsOn: ["Maintenance Routine: Schedule dan Task"]
trace:
  FASVC-LOGIC-07h: [5, 6, 8, 14, 15, 21, 23, 25]
  F-FASVC-02.k5: [6, 8, 15]
anchor: []
coverage:
  web: automated
---

# Service Type yang Dipakai Schedule Aktif atau Task Terbuka: Checkbox Disabled dan Tidak Bisa Dilepas

## Prerequisites
- Aktor: Total Control.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-048-1: Group `Cabang Tipe {runId}`.
  - DU-048-2: Service Center `Teknik Tipe Satu {runId}`, Service type `Routine` dan `Repair`, Status `Active`, Available to `Cabang Tipe {runId}`, Country `Indonesia`, City `Palembang`, Company phone `+62 711550401`.
  - DU-048-3: Service Center `Teknik Tipe Dua {runId}`, Service type `Routine` dan `Repair`, Status `Active`, Available to `Cabang Tipe {runId}`, Country `Indonesia`, City `Palembang`, Company phone `+62 711550402`.
  - DU-048-4: Service Center `Teknik Tipe Ketiga {runId}`, Service type `Routine` dan `Repair`, Status `Active`, Available to `Cabang Tipe {runId}`, Country `Indonesia`, City `Palembang`, Company phone `+62 711550403`.
  - DU-048-5: Schedule `Servis Tipe Satu {runId}`, Status `Active`, pelaksana default `Teknik Tipe Satu {runId}`.
  - DU-048-6: Schedule `Servis Tipe Dua {runId}`, Status `Active`, pelaksana default `Teknik Tipe Dua {runId}`.
  - DU-048-7: Task aset `Pompa Tipe Dua {runId}`, Status `To Do`, pelaksana `Teknik Tipe Dua {runId}`.
  - DU-048-8: Schedule `Inspeksi Tipe Ketiga {runId}`, Status `Paused`, pelaksana default `Teknik Tipe Ketiga {runId}`.
  - DU-048-9: Task aset `Mesin Tipe Ketiga {runId}`, Status `Completed`, pelaksana `Teknik Tipe Ketiga {runId}`.
- Kondisi:
  - Lisensi addon Maintenance aktif.
  - Tidak ada Work Order yang merujuk Service Center di Data.

## Test Steps

### Type yang dipakai satu Schedule aktif tidak bisa dilepas
1. Buka Add-ons > Service Center
2. Ketik Search `Teknik Tipe Satu {runId}`, tekan Enter
3. Klik `⋯` pada baris `Teknik Tipe Satu {runId}`
4. Klik `Edit`
5. Verifikasi checkbox Service type `Repair` tidak disabled
6. Verifikasi alasan `Used by 1 active schedule or open task.` tersampaikan pada checkbox Service type `Routine` yang disabled
7. Klik checkbox Service type `Routine`
8. Verifikasi checkbox Service type `Routine` tetap tercentang
9. Klik `✕` pada form (isian belum diubah)

### Hitungan pemakai jamak: Schedule aktif dan Task terbuka
10. Buka Add-ons > Service Center
11. Ketik Search `Teknik Tipe Dua {runId}`, tekan Enter
12. Klik `⋯` pada baris `Teknik Tipe Dua {runId}`
13. Klik `Edit`
14. Verifikasi checkbox Service type `Repair` tidak disabled
15. Verifikasi alasan `Used by 2 active schedules or open tasks.` tersampaikan pada checkbox Service type `Routine` yang disabled
16. Klik `✕` pada form (isian belum diubah)

### Schedule Paused dan Task Completed tidak menahan type
17. Buka Add-ons > Service Center
18. Ketik Search `Teknik Tipe Ketiga {runId}`, tekan Enter
19. Klik `⋯` pada baris `Teknik Tipe Ketiga {runId}`
20. Klik `Edit`
21. Verifikasi checkbox Service type `Routine` tidak disabled
22. Klik checkbox Service type `Routine`
23. Verifikasi checkbox Service type `Routine` tidak tercentang
24. Klik `[Save]`
25. Verifikasi baris `Teknik Tipe Ketiga {runId}` menampilkan Service Type `Repair`
