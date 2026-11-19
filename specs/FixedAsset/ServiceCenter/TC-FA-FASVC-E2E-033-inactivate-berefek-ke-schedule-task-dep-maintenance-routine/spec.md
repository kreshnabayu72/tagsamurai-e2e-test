---
id: TC-FA-FASVC-E2E-033-inactivate-berefek-ke-schedule-task-dep-maintenance-routine
title: "Inactivate Saat Dipakai: Pemilih, Task In Progress, Schedule, dan Task Berikutnya"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [FASVC-LOGIC-05a, FASVC-LOGIC-05b, FASVC-LOGIC-05c, FASVC-LOGIC-05g, EC-FASVC-05, EC-FASVC-06, EC-FASVC-07, F-FASVC-03.k2, F-FASVC-03.k3, "§9.2#p6", "§9.2#p12", "§9.7#r2", "§9.7#r10", "§9.4.3#b2", "§Aturan Logika Modul#p2", "§9.2#p1"]
smoke: []
dependsOn: ["Maintenance Routine: Schedule dan Task"]
trace:
  FASVC-LOGIC-05a: 13
  FASVC-LOGIC-05b: [15, 16, 18, 22, 23, 24, 26, 28, 27]
  FASVC-LOGIC-05c: [18, 19, 31, 32]
  FASVC-LOGIC-05g: 51
  EC-FASVC-05: [15, 16]
  EC-FASVC-06: [31, 32, 34]
  EC-FASVC-07: [49, 51]
  F-FASVC-03.k2: [38, 40]
  F-FASVC-03.k3: [34, 35, 38, 40]
  "§9.2#p6": [64, 67, 68, 70, 72]
  "§9.2#p12": [22, 23, 24, 26, 28, 27]
  "§9.7#r2": [13, 22, 23, 31, 32, 24, 26, 28, 27]
  "§9.7#r10": [49, 51]
  "§9.4.3#b2": [15, 19]
  "§Aturan Logika Modul#p2": 7
  "§9.2#p1": [16, 18, 22]
anchor: [12]
coverage:
  web: automated
---

# Inactivate Saat Dipakai: Pemilih, Task In Progress, Schedule, dan Task Berikutnya

## Prerequisites
- Aktor: Total Control. Aktor kedua: Asset Admin `Dian Pratama {runId}` (Role Transaksi Maintenance Routine, cakupan Group `Cabang Tengah {runId}` dan `Cabang Sementara {runId}`).
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-033-1: Group `Cabang Tengah {runId}`.
  - DU-033-2: Group `Cabang Sementara {runId}`.
  - DU-033-3: User `Dian Pratama {runId}`, Role Asset Admin dengan Role Transaksi Maintenance Routine, cakupan Group `Cabang Tengah {runId}` dan `Cabang Sementara {runId}`.
  - DU-033-4: Aset `Mesin Pendingin Tengah {runId}`, Group `Cabang Tengah {runId}`.
  - DU-033-24: Aset `Pompa Sementara {runId}`, Group `Cabang Tengah {runId}`. Group `Cabang Sementara {runId}` tidak berisi aset.
  - DU-033-5: Service Center `Servis Terpadu Tengah {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Tengah {runId}`, City `Semarang`.
  - DU-033-6: Service Center `Mitra Aktif Tengah {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Tengah {runId}`, City `Semarang`.
  - DU-033-7: Service Center `Servis Sementara Otomatis {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Tengah {runId}` dan `Cabang Sementara {runId}`, City `Semarang`, dibuat oleh Total Control. Cakupannya dipersempit spec ini menjadi `Cabang Sementara {runId}` saja.
  - DU-033-8: Schedule `Servis Atrium Bulanan {runId}`, Status `Active`, pelaksana default `Servis Terpadu Tengah {runId}`, Asset Admin `Dian Pratama {runId}`.
  - DU-033-9: Schedule `Inspeksi Atrium Paused {runId}`, Status `Paused`, pelaksana default `Servis Terpadu Tengah {runId}`.
  - DU-033-10: Schedule `Servis Sementara Bulanan {runId}`, Status `Active`, pelaksana default `Servis Sementara Otomatis {runId}` (disimpan saat Available to-nya masih mencakup `Cabang Tengah {runId}`), aset `Pompa Sementara {runId}`, Asset Admin `Dian Pratama {runId}`.
  - DU-033-11: Task aset `Chiller Atrium {runId}`, Status `In Progress`, pelaksana `Servis Terpadu Tengah {runId}`.
  - DU-033-12: Task aset `Penggantian Filter Atrium {runId}`, Status `To Do`, Start date `T0 + 1 hari`, satu-satunya pelaksana `Servis Terpadu Tengah {runId}`.
  - DU-033-13: Task aset `Kalibrasi Atrium {runId}`, Status `Completed`, pelaksana `Servis Terpadu Tengah {runId}`.
  - DU-033-16: User `Teknisi Atrium {runId}`, Role Staff.
  - DU-033-17: Task aset `Pemeriksaan Panel Atrium {runId}`, Status `To Do`, Start date `T0 + 1 hari`, dua pelaksana: `Servis Terpadu Tengah {runId}` dan `Teknisi Atrium {runId}`.
  - DU-033-18: Schedule `Inspeksi Atrium Berakhir {runId}`, Status `Ended`, pelaksana default `Servis Terpadu Tengah {runId}`.
  - DU-033-19: Task aset `Pengecekan Genset Atrium {runId}`, Status `On Schedule`, Start date `T0 + 7 hari`, pelaksana `Servis Terpadu Tengah {runId}`.
  - DU-033-20: Task aset `Persetujuan Hasil Atrium {runId}`, Status `Waiting for Approval`, pelaksana `Servis Terpadu Tengah {runId}`.
  - DU-033-21: Task aset `Pelumasan Atrium {runId}`, Status `Skipped`, pelaksana `Servis Terpadu Tengah {runId}`.
  - DU-033-22: Task aset `Pembersihan Atrium {runId}`, Status `Canceled`, pelaksana `Servis Terpadu Tengah {runId}`.
  - DU-033-23: Task aset `Uji Beban Atrium {runId}`, Status `Missed`, pelaksana `Servis Terpadu Tengah {runId}`.
- Kondisi:
  - Lisensi addon Maintenance aktif.

## Test Steps

### Inactivate Service Center yang dipakai Schedule aktif dan Task terbuka
1. Catat entri teratas System Log aktor
2. Asset Admin `Dian Pratama {runId}` mencatat jumlah notifikasi Unread di Notification Center
3. Buka Add-ons > Service Center
4. Ketik Search `Servis Terpadu Tengah {runId}`, tekan Enter
5. Klik `⋯` pada baris `Servis Terpadu Tengah {runId}`
6. Klik `Inactivate`
7. Verifikasi dialog `Inactivate Service Center` menyebut `1` active schedules dan `5` open tasks yang memakainya (Schedule `Paused` dan `Ended`, serta Task `Completed`, `Skipped`, `Canceled`, dan `Missed` tidak dihitung)
8. Klik `[Inactivate]`

### Service Center Inactive tidak lagi muncul di pemilih
9. Buka form Create Schedule di Maintenance Routine
10. Pilih aset `Mesin Pendingin Tengah {runId}` saja
11. Klik pemilih `Select service center`
12. Verifikasi opsi `Mitra Aktif Tengah {runId}` tampil
13. Verifikasi `Servis Terpadu Tengah {runId}` yang berstatus `Inactive` tidak ada di opsi

### Task In Progress dan Schedule tetap memakai Service Center Inactive
14. Buka Task aset `Chiller Atrium {runId}` di Maintenance Routine
15. Verifikasi Task berstatus `In Progress` dan tetap berjalan
16. Verifikasi pelaksana `Servis Terpadu Tengah {runId}` tetap tampil dengan badge `Inactive`
17. Buka Schedule `Servis Atrium Bulanan {runId}` di Maintenance Routine
18. Verifikasi pelaksana default `Servis Terpadu Tengah {runId}` tetap tampil dengan badge `Inactive`
19. Verifikasi Schedule berstatus `Active` dan tetap berjalan

### Task yang belum In Progress dilepas pada Start date
20. Waktu berlalu sampai Start date Task aset `Penggantian Filter Atrium {runId}` dan Task aset `Pemeriksaan Panel Atrium {runId}` (`T0 + 1 hari`)
21. Buka Task aset `Penggantian Filter Atrium {runId}` di Maintenance Routine
22. Verifikasi Task berstatus `Waiting for Assignment`
23. Verifikasi Task bertanda `Service center inactive`
24. Verifikasi pelaksana `Servis Terpadu Tengah {runId}` tidak lagi tampil pada Task itu
25. Buka Task aset `Pemeriksaan Panel Atrium {runId}` di Maintenance Routine
26. Verifikasi Task tetap berstatus `To Do`
27. Verifikasi pelaksana `Teknisi Atrium {runId}` tetap tampil pada Task itu
28. Verifikasi pelaksana `Servis Terpadu Tengah {runId}` tidak lagi tampil pada Task itu

### Task periode berikutnya dan notifikasi ke Asset Admin Schedule
29. Job pembuatan Task periode berikutnya Schedule `Servis Atrium Bulanan {runId}` berjalan
30. Buka Task periode berikutnya Schedule `Servis Atrium Bulanan {runId}` di Maintenance Routine
31. Verifikasi Task berstatus `Waiting for Assignment`
32. Verifikasi Task bertanda `Service center inactive`
33. Asset Admin `Dian Pratama {runId}` membuka Notification Center
34. Verifikasi notifikasi untuk event `service_center_inactive_in_schedule` dengan Schedule `Servis Atrium Bulanan {runId}` tampil
35. Verifikasi jumlah notifikasi Unread Asset Admin `Dian Pratama {runId}` bertambah `1` dari yang dicatat

### Inactivate tercatat di Changelog dan System Log
36. Buka Add-ons > Service Center
37. Klik `[Changelog]`
38. Verifikasi baris Changelog dengan Action `Inactivated`, Service Center Name `Servis Terpadu Tengah {runId}`, Field `Status`, Old Value `Active`, dan New Value `Inactive` tampil
39. Buka System Log aktor
40. Verifikasi entri teratas System Log berAction `Inactivated` dan berbeda dari entri teratas yang dicatat sebelumnya

### Activate mengembalikan ke pemilih tanpa menugaskan ulang Task
41. Buka Add-ons > Service Center
42. Ketik Search `Servis Terpadu Tengah {runId}`, tekan Enter
43. Klik `⋯` pada baris `Servis Terpadu Tengah {runId}`
44. Klik `Activate`
45. Klik `[Activate]` pada dialog `Activate Service Center`
46. Buka form Create Schedule di Maintenance Routine
47. Pilih aset `Mesin Pendingin Tengah {runId}` saja
48. Klik pemilih `Select service center`
49. Verifikasi opsi `Servis Terpadu Tengah {runId}` tampil lagi
50. Buka Task aset `Penggantian Filter Atrium {runId}` di Maintenance Routine
51. Verifikasi Task tetap berstatus `Waiting for Assignment` dan tanpa pelaksana `Servis Terpadu Tengah {runId}`

### Service Center otomatis Inactive karena cakupan habis berefek sama pada Schedule dan Task
52. Buka Add-ons > Service Center
53. Ketik Search `Servis Sementara Otomatis {runId}`, tekan Enter
54. Klik `⋯` pada baris `Servis Sementara Otomatis {runId}`
55. Klik `Edit`
56. Lepas Available to `Cabang Tengah {runId}` sehingga hanya tersisa `Cabang Sementara {runId}`
57. Klik `[Save]`
58. Klik `[Save]` pada dialog `Narrow Coverage`
59. Asset Admin `Dian Pratama {runId}` mencatat jumlah notifikasi Unread di Notification Center
60. Total Control mencatat jumlah notifikasi Unread di Notification Center
61. Grup `Cabang Sementara {runId}` dihapus dari master sehingga Available to `Servis Sementara Otomatis {runId}` habis
62. Buka Add-ons > Service Center
63. Ketik Search `Servis Sementara Otomatis {runId}`, tekan Enter
64. Verifikasi `Servis Sementara Otomatis {runId}` berstatus `Inactive`
65. Job pembuatan Task periode berikutnya Schedule `Servis Sementara Bulanan {runId}` berjalan
66. Buka Task periode berikutnya Schedule `Servis Sementara Bulanan {runId}` di Maintenance Routine
67. Verifikasi Task berstatus `Waiting for Assignment`
68. Verifikasi Task bertanda `Service center inactive`
69. Asset Admin `Dian Pratama {runId}` membuka Notification Center
70. Verifikasi jumlah notifikasi Unread Asset Admin `Dian Pratama {runId}` bertambah `1` untuk event `service_center_inactive_in_schedule`
71. Total Control membuka Notification Center
72. Verifikasi jumlah notifikasi Unread Total Control bertambah `1` untuk event `service_center_auto_inactivated`
