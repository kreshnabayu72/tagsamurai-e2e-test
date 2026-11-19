---
id: TC-FA-FASVC-E2E-004-gating-monitoring-report
title: "Gating Monitoring & Report: Lihat, Download, Changelog; Tanpa Aksi Tulis"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "RA-FASVC-01", "RA-FASVC-02", "RA-FASVC-03", "RA-FASVC-04", "RA-FASVC-05", "FASVC-LOGIC-08a", "FASVC-LOGIC-08d", "FASVC-LOGIC-08g", "FASVC-LOGIC-08h", "FASVC-LOGIC-08i", "§2.1#b4"]
smoke: []
dependsOn: []
trace:
  "§2.1#r1": [44, 55, 64, 75]
  "§2.1#r2": 47
  "§2.1#r3": [60, 61, 71]
  "§2.1#r4": [62, 73]
  "§2.1#r5": 49
  "§4.8#r1": 42
  "§4.8#r2": [59, 70]
  "§4.8#r3": 47
  "§4.8#r4": [60, 61, 72]
  "§4.8#r5": 71
  "§4.8#r6": [62, 73]
  "§4.8#r7": 45
  "§4.8#r8": [46, 52]
  "RA-FASVC-01": [59, 70]
  "RA-FASVC-02": [60, 72]
  "RA-FASVC-03": [68, 71]
  "RA-FASVC-04": 61
  "RA-FASVC-05": [62, 73]
  "FASVC-LOGIC-08a": [55, 56, 57, 64, 90]
  "FASVC-LOGIC-08d": 47
  "FASVC-LOGIC-08g": [60, 61, 62, 71, 72, 73]
  "FASVC-LOGIC-08h": [59, 60, 61, 62, 70, 71, 72, 73]
  "FASVC-LOGIC-08i": [65, 76]
  "§2.1#b4": [93, 95]
anchor: [39, 92]
coverage:
  web: automated
---

# Gating Monitoring & Report: Lihat, Download, Changelog; Tanpa Aksi Tulis

## Prerequisites
- Aktor: Monitoring & Report `Maya Monitoring {runId}` (Role Transaksi `Maintenance Routine` pada `Branch Surabaya`) Monitoring & Report `Mira Tanpa Transaksi {runId}` (hanya Role Transaksi `Assignment` pada `Branch Surabaya`), dan Total Control `Tania Control {runId}` sebagai pemicu.
- Layar awal: Dashboard Fixed Asset.
- Data:
  - DU-004-1: Group `Head Office`, node root pohon Group entitas aktor.
  - DU-004-2: Group `Branch Surabaya`, anak dari `Head Office`.
  - DU-004-3: Group `Branch Malang`, anak dari `Head Office`.
  - DU-004-4: Aktor `Maya Monitoring {runId}` dengan Role `Monitoring & Report`, Role Transaksi `Maintenance Routine`, cakupan `Branch Surabaya`.
  - DU-004-5: Aktor `Tania Control {runId}` dengan Role `Total Control`.
  - DU-004-6: Service Center `Servis Monitoring {runId}`, Service type `Routine`, Available to `Branch Surabaya` dan `Branch Malang`, City `Surabaya`, Company email `layanan@servismonitoring.co.id`, dibuat oleh `Tania Control {runId}`. Usage `0`.
  - DU-004-7: Service Center `Servis Malang Saja {runId}`, Service type `Routine`, Available to `Branch Malang`, City `Malang`, Company email `info@malangsaja.co.id`, dibuat oleh `Tania Control {runId}`. Usage `0`.
  - DU-004-8: Service Center `Servis Nonaktif {runId}`, Service type `Routine`, Available to `Branch Surabaya`, City `Surabaya`, Company email `kontak@servisnonaktif.co.id`, dibuat oleh `Tania Control {runId}` lalu di-Inactivate oleh `Tania Control {runId}`. Status `Inactive`. Usage `0`.
  - DU-004-9: Service Center `Servis Semua Group {runId}`, Service type `Routine`, Available to `All groups`, City `Jakarta Selatan`, Company email `layanan@semuagroupmr.co.id`, dibuat oleh `Tania Control {runId}`. Usage `0`.
  - DU-004-10: Aktor `Mira Tanpa Transaksi {runId}` dengan Role `Monitoring & Report`, hanya Role Transaksi `Assignment` (modul lain), cakupan `Branch Surabaya`.
- Kondisi:
  - Lisensi addon Maintenance aktif untuk entitas aktor.
  - Akun `Maya Monitoring {runId}`, `Mira Tanpa Transaksi {runId}`, dan `Tania Control {runId}` aktif dan kredensialnya disediakan fase 2.
  - Master Data Count Limit bernilai `1000` dan entitas aktor berisi kurang dari 1.000 Service Center.

## Test Steps

### Total Control menyiapkan tiga Service Center sebagai pemicu
1. Masuk sebagai `Tania Control {runId}`
2. Buka menu `Add-ons` pada sidebar
3. Klik `Service Center`
4. Klik `[+ Service Center]`
5. Isi Name `Servis Monitoring {runId}`
6. Centang Service type `Routine`
7. Klik field Available to
8. Hapus centang node `All groups`
9. Centang node `Branch Surabaya`
10. Centang node `Branch Malang`
11. Klik `[Select]`
12. Isi City `Surabaya`
13. Isi Company email `layanan@servismonitoring.co.id`
14. Klik `[Submit]`
15. Klik `[+ Service Center]`
16. Isi Name `Servis Malang Saja {runId}`
17. Centang Service type `Routine`
18. Klik field Available to
19. Hapus centang node `All groups`
20. Centang node `Branch Malang`
21. Klik `[Select]`
22. Isi City `Malang`
23. Isi Company email `info@malangsaja.co.id`
24. Klik `[Submit]`
25. Klik `[+ Service Center]`
26. Isi Name `Servis Nonaktif {runId}`
27. Centang Service type `Routine`
28. Klik field Available to
29. Hapus centang node `All groups`
30. Centang node `Branch Surabaya`
31. Klik `[Select]`
32. Isi City `Surabaya`
33. Isi Company email `kontak@servisnonaktif.co.id`
34. Klik `[Submit]`
35. Ketik Search `Servis Nonaktif {runId}`, tekan Enter
36. Klik `⋯` pada baris `Servis Nonaktif {runId}`
37. Klik `Inactivate`
38. Klik `[Inactivate]`
39. Verifikasi kolom Status pada baris `Servis Nonaktif {runId}` menampilkan `Inactive`

### Menu dan toolbar bagi Monitoring & Report
40. Masuk sebagai `Maya Monitoring {runId}`
41. Buka menu `Add-ons` pada sidebar
42. Verifikasi menu `Service Center` tampil di bawah `Add-ons`
43. Klik `Service Center`
44. Verifikasi halaman daftar Service Center terbuka dengan breadcrumb `Add-ons > Service Center`
45. Verifikasi tombol `[Download]` tampil
46. Verifikasi tombol `[Changelog]` tampil
47. Verifikasi tombol `[+ Service Center]` tidak tampil

### Download menyediakan pilihan unduhan
48. Klik `[Download]`
49. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil
50. Tutup popover Download

### Changelog gabungan terbuka
51. Klik `[Changelog]`
52. Verifikasi modal `Changelog: Service Center` terbuka
53. Klik ikon close pada modal Changelog

### Cakupan baca Monitoring & Report mengikuti irisan Available to
54. Ketik Search `{runId}`, tekan Enter
55. Verifikasi baris `Servis Monitoring {runId}` tampil di tabel
56. Verifikasi baris `Servis Nonaktif {runId}` tampil di tabel
57. Verifikasi baris `Servis Malang Saja {runId}` tidak tampil di tabel

### Service Center sebagian di luar cakupan hanya punya aksi Detail bagi Monitoring & Report
58. Klik `⋯` pada baris `Servis Monitoring {runId}`
59. Verifikasi aksi `Detail` tampil
60. Verifikasi aksi `Edit` tidak tampil
61. Verifikasi aksi `Inactivate` tidak tampil
62. Verifikasi aksi `Delete` tidak tampil
63. Klik `Detail`
64. Verifikasi halaman Detail menampilkan nama `Servis Monitoring {runId}`
65. Verifikasi info `This service center also serves groups outside your access. Ask an admin who manages all of them.` tidak tampil
66. Klik breadcrumb `Service Center`

### Service Center Inactive dalam cakupan penuh tetap tanpa aksi kelola bagi Monitoring & Report
67. Ganti isi kotak search dengan `Servis Nonaktif {runId}`, tekan Enter
68. Verifikasi kolom Status pada baris `Servis Nonaktif {runId}` menampilkan `Inactive`
69. Klik `⋯` pada baris `Servis Nonaktif {runId}`
70. Verifikasi aksi `Detail` tampil
71. Verifikasi aksi `Activate` tidak tampil
72. Verifikasi aksi `Edit` tidak tampil
73. Verifikasi aksi `Delete` tidak tampil
74. Klik `Detail`
75. Verifikasi halaman Detail menampilkan nama `Servis Nonaktif {runId}`
76. Verifikasi info `This service center also serves groups outside your access. Ask an admin who manages all of them.` tidak tampil

### Service Center All groups terlihat bagi Monitoring & Report
77. Masuk sebagai `Tania Control {runId}`
78. Buka menu `Add-ons` pada sidebar
79. Klik `Service Center`
80. Klik `[+ Service Center]`
81. Isi Name `Servis Semua Group {runId}`
82. Centang Service type `Routine`
83. Isi City `Jakarta Selatan`
84. Isi Company email `layanan@semuagroupmr.co.id`
85. Klik `[Submit]`
86. Masuk sebagai `Maya Monitoring {runId}`
87. Buka menu `Add-ons` pada sidebar
88. Klik `Service Center`
89. Ketik Search `Servis Semua Group {runId}`, tekan Enter
90. Verifikasi baris `Servis Semua Group {runId}` tampil di tabel

### Monitoring & Report tanpa Role Transaksi Maintenance Routine atau Repair tidak punya akses
91. Masuk sebagai `Mira Tanpa Transaksi {runId}`
92. Verifikasi menu `Dashboard` tampil pada sidebar
93. Verifikasi menu `Service Center` tidak tampil pada sidebar
94. Buka halaman daftar Service Center lewat alamat langsung
95. Verifikasi empty state `You do not have access to Service Center.` tampil
