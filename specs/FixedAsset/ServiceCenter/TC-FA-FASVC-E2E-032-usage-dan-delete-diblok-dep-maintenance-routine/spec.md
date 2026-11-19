---
id: TC-FA-FASVC-E2E-032-usage-dan-delete-diblok-dep-maintenance-routine
title: "Usage dari Schedule, Task, dan Work Order: Angka, Hover, Tab Usage, dan Delete Diblok"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: [FASVC-LOGIC-03a, FASVC-LOGIC-03b, FASVC-LOGIC-03c, FASVC-LOGIC-03d, FASVC-LOGIC-06a, FASVC-LOGIC-06b, F-FASVC-06.k1, F-FASVC-04.k2, EC-FASVC-08, EC-FASVC-40, "§9.2#p13", "§9.7#r7", "§4.4#r9", "§9.2#p15", "§9.4.3#b1", "§9.2#r2", "§9.5#r2", "§9.5#r4", "§9.7#p1", "§12#p1"]
smoke: []
dependsOn: ["Maintenance Routine: Schedule dan Task"]
trace:
  FASVC-LOGIC-03a: [3, 7, 8, 9, 10, 11, 42, 45, 47, 51, 55, 58]
  FASVC-LOGIC-03b: [3, 5]
  FASVC-LOGIC-03c: [7, 9, 20, 22, 24, 26, 28, 30, 31, 34, 37, 38, 85]
  FASVC-LOGIC-03d: 64
  FASVC-LOGIC-06a: [42, 47, 51, 55, 60, 64, 66, 72, 78]
  FASVC-LOGIC-06b: [42, 47, 51, 55, 60]
  F-FASVC-06.k1: [3, 5]
  F-FASVC-04.k2: 47
  EC-FASVC-08: [45, 47]
  EC-FASVC-40: [3, 5]
  "§9.2#p13": [78, 80]
  "§9.7#r7": [42, 58, 64, 66, 70, 80]
  "§4.4#r9": 17
  "§9.2#p15": 3
  "§9.4.3#b1": [11, 47]
  "§9.2#r2": [3, 5]
  "§9.5#r2": [14, 15]
  "§9.5#r4": 12
  "§9.7#p1": [64, 70]
  "§12#p1": 5
anchor: [33, 84]
coverage:
  web: automated
---

# Usage dari Schedule, Task, dan Work Order: Angka, Hover, Tab Usage, dan Delete Diblok

## Prerequisites
- Aktor: Total Control. Aktor kedua: `Admin Aset Selatan {runId}` (DU-032-23), Asset Admin pemegang Role Transaksi Maintenance Routine dengan cakupan Group `Cabang Selatan {runId}`.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-032-1: Group `Cabang Selatan {runId}`.
  - DU-032-2: Service Center `Teknik Jaya Mandiri {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Selatan {runId}`, City `Semarang`. Dirujuk 1 Schedule dan 6 Task (DU-032-9, DU-032-11 sampai DU-032-16), sehingga Usage `7`.
  - DU-032-3: Service Center `Bengkel Cabang Selatan {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Selatan {runId}`, City `Semarang`. Hanya dirujuk 1 Task `Canceled` (DU-032-17), sehingga Usage `1`.
  - DU-032-4: Service Center `Vendor Baru Tanpa Rujukan {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Selatan {runId}`, City `Semarang`. Hanya dirujuk 1 Task `To Do` (DU-032-19), sehingga Usage `1`.
  - DU-032-5: Service Center `Teknisi Pengganti Mandiri {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Selatan {runId}`, City `Semarang`. Belum dirujuk, Usage `0`.
  - DU-032-6: Service Center `Vendor Rujukan Bersamaan {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Selatan {runId}`, City `Semarang`. Belum dirujuk, Usage `0`.
  - DU-032-7: Service Center `Servis Paused Utara {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Selatan {runId}`, City `Semarang`. Hanya dirujuk 1 Schedule `Paused` (DU-032-10), sehingga Usage `1`.
  - DU-032-8: Service Center `Biaya Mandiri Teknik {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Selatan {runId}`, City `Semarang`. Hanya menjadi sumber biaya 1 Task `Completed` (DU-032-18), sehingga Usage `1`.
  - DU-032-9: Schedule `Servis Chiller Bulanan {runId}`, Status `Active`, pelaksana default `Teknik Jaya Mandiri {runId}`.
  - DU-032-10: Schedule `Inspeksi Paused {runId}`, Status `Paused`, pelaksana default `Servis Paused Utara {runId}`.
  - DU-032-11: Task aset `Chiller Lantai 2 {runId}`, Status `In Progress`, pelaksana `Teknik Jaya Mandiri {runId}`, belum selesai.
  - DU-032-12: Task aset `Genset Gudang Utara {runId}`, Status `To Do`, pelaksana `Teknik Jaya Mandiri {runId}`, belum selesai.
  - DU-032-13: Task aset `Panel Distribusi Utama {runId}`, Status `Completed`, Result `Normal`, selesai `T0 − 10 hari, pukul 11:20`, pelaksana `Teknik Jaya Mandiri {runId}`.
  - DU-032-14: Task aset `Kompresor Bengkel {runId}`, Status `Completed`, Result `Needs attention`, selesai `T0 − 20 hari, pukul 09:40`, pelaksana `Teknik Jaya Mandiri {runId}`.
  - DU-032-15: Task aset `Forklift Gudang {runId}`, Status `Canceled`, pelaksana `Teknik Jaya Mandiri {runId}`, tanpa waktu selesai.
  - DU-032-16: Task aset `Pompa Hydrant {runId}`, Status `Completed`, Result `Normal`, selesai `T0 − 14 bulan`, pelaksana `Teknik Jaya Mandiri {runId}`.
  - DU-032-17: Task aset `Mesin Bubut Selatan {runId}`, Status `Canceled`, pelaksana `Bengkel Cabang Selatan {runId}`, tanpa waktu selesai.
  - DU-032-18: Task aset `Trafo Gardu Selatan {runId}`, Status `Completed`, Result `Normal`, selesai `T0 − 5 hari, pukul 14:10`, sumber biaya `Biaya Mandiri Teknik {runId}`.
  - DU-032-19: Task `Tugas Pindah Pelaksana {runId}` pada aset `Blower Gudang {runId}`, Status `To Do`, pelaksana `Vendor Baru Tanpa Rujukan {runId}`.
  - DU-032-20: Task `Tugas Rujukan Baru {runId}` pada aset `Pompa Sumur {runId}` (Group `Cabang Selatan {runId}`), Status `Waiting for Assignment`, belum ada pelaksana.
  - DU-032-21: Schedule `Inspeksi Panel Bulanan {runId}`, Status `Active`, tanpa Service Center sebagai pelaksana default; menjadi Schedule Task `Kompresor Bengkel {runId}`.
  - DU-032-23: User `Admin Aset Selatan {runId}`, Asset Admin pemegang Role Transaksi Maintenance Routine, cakupan Group `Cabang Selatan {runId}`, akun aktif.
  - Task DU-032-11, DU-032-12, DU-032-13, DU-032-15, dan DU-032-16 ber-Schedule `Servis Chiller Bulanan {runId}`; Task DU-032-14 ber-Schedule `Inspeksi Panel Bulanan {runId}`.
- Kondisi:
  - Lisensi addon Maintenance aktif.
  - Tidak ada Work Order yang merujuk Service Center di Data.
  - Akun `Admin Aset Selatan {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Usage di daftar menjumlahkan semua rujukan dan hover merinci per konsumen
1. Buka Add-ons > Service Center
2. Ketik Search `Teknik Jaya Mandiri {runId}`, tekan Enter
3. Verifikasi angka Usage pada baris `Teknik Jaya Mandiri {runId}` adalah `7`
4. Arahkan kursor ke angka Usage pada baris itu
5. Verifikasi rincian `Schedules: 1 · Open tasks: 2 · Completed tasks: 3 · Other tasks: 1 · Repair orders: 0` tersampaikan pada angka Usage

### Tab Usage memuat rujukan Task apa pun statusnya
6. Klik angka Usage pada baris `Teknik Jaya Mandiri {runId}`
7. Verifikasi baris Task aset `Chiller Lantai 2 {runId}` berstatus `In Progress` tampil di tab Usage
8. Verifikasi baris Task aset `Genset Gudang Utara {runId}` berstatus `To Do` tampil
9. Verifikasi baris Task aset `Panel Distribusi Utama {runId}` berstatus `Completed` dengan Result `Normal` tampil
10. Verifikasi baris Task aset `Kompresor Bengkel {runId}` berstatus `Completed` dengan Result `Needs attention` tampil
11. Verifikasi baris Task aset `Forklift Gudang {runId}` berstatus `Canceled` tampil
12. Verifikasi baris Task aset `Pompa Hydrant {runId}` yang selesai 14 bulan lalu tidak tampil, karena periode default 12 bulan terakhir
13. Ketik Search `{runId}` pada tab Usage, tekan Enter
14. Verifikasi baris tanpa waktu selesai (`Chiller Lantai 2 {runId}`, `Genset Gudang Utara {runId}`, `Forklift Gudang {runId}`) berada di atas baris `Panel Distribusi Utama {runId}`
15. Verifikasi baris `Panel Distribusi Utama {runId}` (selesai lebih baru) berada di atas baris `Kompresor Bengkel {runId}`
16. Klik Reference pada baris `Panel Distribusi Utama {runId}`
17. Verifikasi popup `Maintenance Routine Log` terbuka bagi aktor yang berhak melihat semua task
18. Tutup popup `Maintenance Routine Log`

### Search di tab Usage mencari kolom yang tampil tanpa membedakan huruf besar-kecil
19. Ganti isi kotak Search dengan `Chiller`, tekan Enter
20. Verifikasi baris `Chiller Lantai 2 {runId}` tampil
21. Ganti isi kotak Search dengan `CHILLER`, tekan Enter
22. Verifikasi baris `Chiller Lantai 2 {runId}` tampil untuk kata kunci huruf besar
23. Ganti isi kotak Search dengan `istribusi`, tekan Enter
24. Verifikasi baris `Panel Distribusi Utama {runId}` tampil untuk kata kunci di tengah nama
25. Ganti isi kotak Search dengan `Canceled`, tekan Enter
26. Verifikasi baris `Forklift Gudang {runId}` berstatus `Canceled` tampil
27. Ganti isi kotak Search dengan Asset ID milik aset `Panel Distribusi Utama {runId}`, tekan Enter
28. Verifikasi baris `Panel Distribusi Utama {runId}` tampil
29. Ganti isi kotak Search dengan `Panel`, tekan Enter
30. Verifikasi baris `Panel Distribusi Utama {runId}` tampil karena cocok pada kolom Name
31. Verifikasi baris `Kompresor Bengkel {runId}` tampil karena cocok pada kolom Schedule `Inspeksi Panel Bulanan {runId}`
32. Sembunyikan kolom `Schedule` lewat Column Visibility
33. Verifikasi baris `Panel Distribusi Utama {runId}` tetap tampil untuk kata kunci `Panel`
34. Verifikasi baris `Kompresor Bengkel {runId}` tidak tampil untuk kata kunci `Panel`, karena kolom Schedule tersembunyi
35. Tampilkan kembali kolom `Schedule` lewat Column Visibility
36. Ganti isi kotak Search dengan `zzzz-tanpa-hasil`, tekan Enter
37. Verifikasi pesan `No results found` tampil
38. Verifikasi petunjuk `Try adjusting your search or filter.` tampil

### Delete disabled bagi Service Center yang dipakai, apa pun jenis dan status pemakainya
39. Buka Add-ons > Service Center
40. Ketik Search `Teknik Jaya Mandiri {runId}`, tekan Enter
41. Klik `⋯` pada baris `Teknik Jaya Mandiri {runId}`
42. Verifikasi alasan `This service center has been used. Inactivate it instead.` tersampaikan pada aksi `Delete` yang disabled (dirujuk Schedule dan Task)
43. Tutup menu `⋯`
44. Ganti isi kotak Search dengan `Bengkel Cabang Selatan {runId}`, tekan Enter
45. Verifikasi angka Usage pada baris `Bengkel Cabang Selatan {runId}` adalah `1`, walau satu-satunya rujukan Task `Canceled`
46. Klik `⋯` pada baris `Bengkel Cabang Selatan {runId}`
47. Verifikasi alasan `This service center has been used. Inactivate it instead.` tersampaikan pada aksi `Delete` yang disabled (hanya dirujuk Task `Canceled`)
48. Tutup menu `⋯`
49. Ganti isi kotak Search dengan `Servis Paused Utara {runId}`, tekan Enter
50. Klik `⋯` pada baris `Servis Paused Utara {runId}`
51. Verifikasi alasan `This service center has been used. Inactivate it instead.` tersampaikan pada aksi `Delete` yang disabled (hanya dirujuk Schedule `Paused`)
52. Tutup menu `⋯`
53. Ganti isi kotak Search dengan `Biaya Mandiri Teknik {runId}`, tekan Enter
54. Klik `⋯` pada baris `Biaya Mandiri Teknik {runId}`
55. Verifikasi alasan `This service center has been used. Inactivate it instead.` tersampaikan pada aksi `Delete` yang disabled (hanya menjadi sumber biaya Task)
56. Tutup menu `⋯`

### Rujukan yang di-Reassign tidak dihitung dan Delete tersedia saat Usage 0
57. Ganti isi kotak Search dengan `Vendor Baru Tanpa Rujukan {runId}`, tekan Enter
58. Verifikasi angka Usage pada baris `Vendor Baru Tanpa Rujukan {runId}` adalah `1`
59. Klik `⋯` pada baris `Vendor Baru Tanpa Rujukan {runId}`
60. Verifikasi alasan `This service center has been used. Inactivate it instead.` tersampaikan pada aksi `Delete` yang disabled (dirujuk 1 Task)
61. Tutup menu `⋯`
62. Task `Tugas Pindah Pelaksana {runId}` di-Reassign dari `Vendor Baru Tanpa Rujukan {runId}` ke `Teknisi Pengganti Mandiri {runId}`
63. Ganti isi kotak Search dengan `Vendor Baru Tanpa Rujukan {runId}`, tekan Enter
64. Verifikasi angka Usage pada baris `Vendor Baru Tanpa Rujukan {runId}` adalah `0` tanpa perubahan apa pun di modul Service Center
65. Klik `⋯` pada baris `Vendor Baru Tanpa Rujukan {runId}`
66. Verifikasi aksi `Delete` tersedia (tidak disabled)
67. Klik `Delete`
68. Klik `[Delete]` pada dialog `Delete Service Center`
69. Ganti isi kotak Search dengan `Teknisi Pengganti Mandiri {runId}`, tekan Enter
70. Verifikasi angka Usage pada baris `Teknisi Pengganti Mandiri {runId}` adalah `1`
71. Ganti isi kotak Search dengan `Vendor Baru Tanpa Rujukan {runId}`, tekan Enter
72. Verifikasi pesan `No results found` tampil karena `Vendor Baru Tanpa Rujukan {runId}` sudah terhapus

### Rujukan yang muncul bersamaan dengan Delete membatalkan Delete
73. Ganti isi kotak Search dengan `Vendor Rujukan Bersamaan {runId}`, tekan Enter
74. Klik `⋯` pada baris `Vendor Rujukan Bersamaan {runId}`
75. Klik `Delete`
76. `Admin Aset Selatan {runId}` menetapkan `Vendor Rujukan Bersamaan {runId}` sebagai pelaksana Task `Tugas Rujukan Baru {runId}`
77. Klik `[Delete]` pada dialog `Delete Service Center`
78. Verifikasi dialog `Cannot Delete Service Center` dengan pesan `This service center has been used and can't be deleted. Inactivate it instead.` tampil
79. Klik `[OK]`
80. Verifikasi baris `Vendor Rujukan Bersamaan {runId}` tetap ada di tabel dengan angka Usage `1`

### Tab Usage hanya memuat baris Task, bukan baris Schedule
81. Buka Add-ons > Service Center
82. Ketik Search `Teknik Jaya Mandiri {runId}`, tekan Enter
83. Klik angka Usage pada baris `Teknik Jaya Mandiri {runId}`
84. Verifikasi baris Task aset `Chiller Lantai 2 {runId}` tampil di tab Usage
85. Verifikasi tab Usage memuat tepat `5` baris (Task `Chiller Lantai 2 {runId}`, `Genset Gudang Utara {runId}`, `Panel Distribusi Utama {runId}`, `Kompresor Bengkel {runId}`, dan `Forklift Gudang {runId}`), dan tidak ada baris untuk Schedule `Servis Chiller Bulanan {runId}` yang ikut dihitung di angka Usage `7`
