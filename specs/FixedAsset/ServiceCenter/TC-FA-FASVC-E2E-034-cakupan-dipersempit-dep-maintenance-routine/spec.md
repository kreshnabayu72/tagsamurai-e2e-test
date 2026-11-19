---
id: TC-FA-FASVC-E2E-034-cakupan-dipersempit-dep-maintenance-routine
title: "Cakupan Dipersempit Saat Dipakai: Rujukan Tetap, Pemilih Baru, dan Task Sesudahnya"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FASVC-LOGIC-07a, FASVC-LOGIC-07b, FASVC-LOGIC-07c, FASVC-LOGIC-07d, EC-FASVC-10b, EC-FASVC-10c, EC-FASVC-10d, "§9.7#r3", "§9.7#r12", "§Aturan Logika Modul#p15", "§Aturan Logika Modul#p17", "§Aturan Logika Modul#p18", "§Aturan Logika Modul#p19", "§Aturan Logika Modul#p20"]
smoke: []
dependsOn: ["Maintenance Routine: Schedule dan Task"]
trace:
  FASVC-LOGIC-07a: [11, 31, 51]
  FASVC-LOGIC-07b: [13, 33, 53]
  FASVC-LOGIC-07c: [18, 38, 58]
  FASVC-LOGIC-07d: [21, 22, 41, 42, 61, 62]
  EC-FASVC-10b: [11, 13]
  EC-FASVC-10c: [21, 22]
  EC-FASVC-10d: 18
  "§9.7#r3": [11, 18]
  "§9.7#r12": [31, 38, 51, 58, 73]
  "§Aturan Logika Modul#p15": 11
  "§Aturan Logika Modul#p17": 11
  "§Aturan Logika Modul#p18": [7, 8]
  "§Aturan Logika Modul#p19": [11, 13]
  "§Aturan Logika Modul#p20": [21, 22]
anchor: [17, 37, 57, 72]
coverage:
  web: automated
---

# Cakupan Dipersempit Saat Dipakai: Rujukan Tetap, Pemilih Baru, dan Task Sesudahnya

## Prerequisites
- Aktor: Total Control.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-034-1: Group `Branch Surabaya {runId}`.
  - DU-034-2: Group `Branch Malang {runId}`.
  - DU-034-3: Category `Pendingin Udara {runId}`.
  - DU-034-4: Category `Pendingin Industri {runId}`.
  - DU-034-5: Category `Generator {runId}`.
  - DU-034-6: Brand `Daikin {runId}`.
  - DU-034-7: Brand `LG {runId}`.
  - DU-034-8: Service Center `CV Genset Prima {runId}`, Service type `Routine`, Status `Active`, Available to Branch Surabaya {runId}, Branch Malang {runId}, Specialization All categories, Brands All brands, City `Surabaya`.
  - DU-034-9: Service Center `Mitra Genset Malang {runId}`, Service type `Routine`, Status `Active`, Available to Branch Malang {runId}, Specialization All categories, Brands All brands, City `Surabaya`.
  - DU-034-10: Aset `Genset Pabrik Malang {runId}`, Group Branch Malang {runId}, Category Generator {runId}, Brand —.
  - DU-034-11: Schedule `Servis Genset Malang {runId}`, Status `Active`, pelaksana default `CV Genset Prima {runId}`, aset `Genset Pabrik Malang {runId}`.
  - DU-034-12: Task `Cek Genset Malang {runId}` pada aset `Genset Pabrik Malang {runId}`, Status `In Progress`, Assignee `CV Genset Prima {runId}`.
  - DU-034-27: Schedule `Inspeksi Genset Malang Paused {runId}`, Status `Paused`, pelaksana default `CV Genset Prima {runId}`, aset `Genset Pabrik Malang {runId}`.
  - DU-034-28: Task `Cek Genset Malang Selesai {runId}` pada aset `Genset Pabrik Malang {runId}`, Status `Completed`, Assignee `CV Genset Prima {runId}`.
  - DU-034-14: Service Center `Servis Pendingin Spesialis {runId}`, Service type `Routine`, Status `Active`, Available to Branch Surabaya {runId}, Specialization Pendingin Udara {runId}, Pendingin Industri {runId}, Brands All brands, City `Surabaya`.
  - DU-034-15: Service Center `Mitra Pendingin Surabaya {runId}`, Service type `Routine`, Status `Active`, Available to Branch Surabaya {runId}, Specialization All categories, Brands All brands, City `Surabaya`.
  - DU-034-16: Aset `Chiller Industri Surabaya {runId}`, Group Branch Surabaya {runId}, Category Pendingin Industri {runId}, Brand —.
  - DU-034-17: Schedule `Servis Chiller Industri {runId}`, Status `Active`, pelaksana default `Servis Pendingin Spesialis {runId}`, aset `Chiller Industri Surabaya {runId}`.
  - DU-034-18: Task `Cek Chiller Industri {runId}` pada aset `Chiller Industri Surabaya {runId}`, Status `In Progress`, Assignee `Servis Pendingin Spesialis {runId}`.
  - DU-034-20: Service Center `Teknik Brand Khusus {runId}`, Service type `Routine`, Status `Active`, Available to Branch Surabaya {runId}, Specialization All categories, Brands Daikin {runId}, LG {runId}, City `Surabaya`.
  - DU-034-21: Service Center `Mitra Brand Umum {runId}`, Service type `Routine`, Status `Active`, Available to Branch Surabaya {runId}, Specialization All categories, Brands All brands, City `Surabaya`.
  - DU-034-22: Aset `AC Lobi LG {runId}`, Group Branch Surabaya {runId}, Category Pendingin Udara {runId}, Brand LG {runId}.
  - DU-034-23: Schedule `Servis AC Lobi {runId}`, Status `Active`, pelaksana default `Teknik Brand Khusus {runId}`, aset `AC Lobi LG {runId}`.
  - DU-034-24: Task `Cek AC Lobi {runId}` pada aset `AC Lobi LG {runId}`, Status `In Progress`, Assignee `Teknik Brand Khusus {runId}`.
  - DU-034-26: Service Center `Servis Dua Jenis Kerja {runId}`, Service type `Routine` dan `Repair`, Status `Active`, Available to Branch Surabaya {runId}, Specialization All categories, Brands All brands, City `Surabaya`. Belum dirujuk Schedule, Task, atau Work Order apa pun.
- Kondisi:
  - Lisensi addon Maintenance aktif.

## Test Steps

### Available to dipersempit saat dipakai
1. Buka Add-ons > Service Center
2. Ketik Search `CV Genset Prima {runId}`, tekan Enter
3. Klik `⋯` pada baris `CV Genset Prima {runId}`
4. Klik `Edit`
5. Lepas Available to `Branch Malang {runId}`
6. Klik `[Save]`
7. Verifikasi dialog `Narrow Coverage` tampil
8. Verifikasi dialog `Narrow Coverage` menyebut `1` active schedules dan `1` open tasks yang memakai `CV Genset Prima {runId}` untuk aset di `Branch Malang {runId}` (Schedule `Paused` dan Task `Completed` tidak dihitung)
9. Klik `[Save]` pada dialog `Narrow Coverage`
10. Buka Schedule `Servis Genset Malang {runId}` di Maintenance Routine
11. Verifikasi pelaksana default `CV Genset Prima {runId}` tetap tampil dan Schedule berstatus `Active`
12. Buka Task `Cek Genset Malang {runId}` di Maintenance Routine
13. Verifikasi Task berstatus `In Progress` dengan Assignee `CV Genset Prima {runId}` tidak berubah
14. Buka form Create Schedule di Maintenance Routine
15. Pilih aset `Genset Pabrik Malang {runId}` saja
16. Klik pemilih `Select service center`
17. Verifikasi opsi `Mitra Genset Malang {runId}` tampil
18. Verifikasi `CV Genset Prima {runId}` yang cakupannya sudah dipersempit tidak ada di opsi
19. Job pembuatan Task periode berikutnya Schedule `Servis Genset Malang {runId}` berjalan
20. Buka Task periode berikutnya Schedule `Servis Genset Malang {runId}` untuk aset `Genset Pabrik Malang {runId}` di Maintenance Routine
21. Verifikasi Task berstatus `Waiting for Assignment`
22. Verifikasi Task bertanda `Service center doesn't cover this asset`

### Specialization dipersempit saat dipakai
23. Buka Add-ons > Service Center
24. Ketik Search `Servis Pendingin Spesialis {runId}`, tekan Enter
25. Klik `⋯` pada baris `Servis Pendingin Spesialis {runId}`
26. Klik `Edit`
27. Lepas Specialization `Pendingin Industri {runId}`
28. Klik `[Save]`
29. Klik `[Save]` pada dialog `Narrow Coverage`
30. Buka Schedule `Servis Chiller Industri {runId}` di Maintenance Routine
31. Verifikasi pelaksana default `Servis Pendingin Spesialis {runId}` tetap tampil dan Schedule berstatus `Active`
32. Buka Task `Cek Chiller Industri {runId}` di Maintenance Routine
33. Verifikasi Task berstatus `In Progress` dengan Assignee `Servis Pendingin Spesialis {runId}` tidak berubah
34. Buka form Create Schedule di Maintenance Routine
35. Pilih aset `Chiller Industri Surabaya {runId}` saja
36. Klik pemilih `Select service center`
37. Verifikasi opsi `Mitra Pendingin Surabaya {runId}` tampil
38. Verifikasi `Servis Pendingin Spesialis {runId}` yang cakupannya sudah dipersempit tidak ada di opsi
39. Job pembuatan Task periode berikutnya Schedule `Servis Chiller Industri {runId}` berjalan
40. Buka Task periode berikutnya Schedule `Servis Chiller Industri {runId}` untuk aset `Chiller Industri Surabaya {runId}` di Maintenance Routine
41. Verifikasi Task berstatus `Waiting for Assignment`
42. Verifikasi Task bertanda `Service center doesn't cover this asset`

### Brands dipersempit saat dipakai
43. Buka Add-ons > Service Center
44. Ketik Search `Teknik Brand Khusus {runId}`, tekan Enter
45. Klik `⋯` pada baris `Teknik Brand Khusus {runId}`
46. Klik `Edit`
47. Lepas Brands `LG {runId}`
48. Klik `[Save]`
49. Klik `[Save]` pada dialog `Narrow Coverage`
50. Buka Schedule `Servis AC Lobi {runId}` di Maintenance Routine
51. Verifikasi pelaksana default `Teknik Brand Khusus {runId}` tetap tampil dan Schedule berstatus `Active`
52. Buka Task `Cek AC Lobi {runId}` di Maintenance Routine
53. Verifikasi Task berstatus `In Progress` dengan Assignee `Teknik Brand Khusus {runId}` tidak berubah
54. Buka form Create Schedule di Maintenance Routine
55. Pilih aset `AC Lobi LG {runId}` saja
56. Klik pemilih `Select service center`
57. Verifikasi opsi `Mitra Brand Umum {runId}` tampil
58. Verifikasi `Teknik Brand Khusus {runId}` yang cakupannya sudah dipersempit tidak ada di opsi
59. Job pembuatan Task periode berikutnya Schedule `Servis AC Lobi {runId}` berjalan
60. Buka Task periode berikutnya Schedule `Servis AC Lobi {runId}` untuk aset `AC Lobi LG {runId}` di Maintenance Routine
61. Verifikasi Task berstatus `Waiting for Assignment`
62. Verifikasi Task bertanda `Service center doesn't cover this asset`

### Service type dilepas dari Service Center yang belum dipakai
63. Buka Add-ons > Service Center
64. Ketik Search `Servis Dua Jenis Kerja {runId}`, tekan Enter
65. Klik `⋯` pada baris `Servis Dua Jenis Kerja {runId}`
66. Klik `Edit`
67. Lepas Service type `Routine`
68. Klik `[Save]`
69. Buka form Create Schedule di Maintenance Routine
70. Pilih aset `Chiller Industri Surabaya {runId}` saja
71. Klik pemilih `Select service center`
72. Verifikasi opsi `Mitra Pendingin Surabaya {runId}` tampil
73. Verifikasi `Servis Dua Jenis Kerja {runId}` yang Service type-nya tidak lagi memuat `Routine` tidak ada di opsi
