---
id: TC-FA-FAREG-E2E-046-waiting-for-approval-tabel
title: "Sub tab Waiting for Approval: isi tabel, Search, Filter, sort, dan aksi baris"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#r38", "§4.1#r39", "§4.1#r40", "§4.1#r41", "§4.1#r42", "§4.1#p12", "§5#r3", "§5#r4", "§9.5#r5", "EB-SRC-5@tabel-waiting-for-approval"]
smoke: []
dependsOn: []
trace:
  "§4.1#r39": [2, 11, 19, 23, 45]
  "§4.1#r38": [3, 9, 19, 43, 70]
  "§4.1#r40": [4, 13, 19, 29, 47]
  "§4.1#r41": [5, 15, 19, 34, 49]
  "§4.1#r42": [6, 7, 17, 19, 39, 51]
  "§5#r4": [7]
  "§9.5#r5": [7]
  "§5#r3": [9]
  "EB-SRC-5@tabel-waiting-for-approval": [53, 57, 60]
  "§4.1#p12": [62, 63, 64, 66, 74, 77]
coverage:
  web: automated
---

# Sub tab Waiting for Approval: isi tabel, Search, Filter, sort, dan aksi baris

## Prerequisites
- Aktor: Manage asset & TAG `Maya L`, Group terkelola `Gudang Mangga {runId}`, `Gudang Jati {runId}`, dan `Gudang Akasia {runId}`, pengaju DU-046-1.
- Layar awal: Assets > Registration > Waiting for Approval.
- Data:
  - DU-046-1: Pengajuan Waiting for Approval dengan Registration ID yang dibentuk server saat Submit, Group `Gudang Mangga {runId}`, Total Asset `12`, Requested By `Maya L.`, Last Updated `T0 − 1 hari`.
  - DU-046-2: Pengajuan Waiting for Approval dengan Registration ID yang dibentuk server saat Submit, Group `Gudang Jati {runId}`, Total Asset `30`, Requested By `Hadi K`, Last Updated `T0 − 2 hari`.
  - DU-046-3: Pengajuan Waiting for Approval dengan Registration ID yang dibentuk server saat Submit, Group `Gudang Akasia {runId}`, Total Asset `5`, Requested By `Siti N`, Last Updated `T0 − 3 hari`.
  - Pengajuan DU-046-3 diajukan lebih dulu daripada DU-046-2, dan DU-046-2 lebih dulu daripada DU-046-1.
  - Maya L, Hadi K, dan Siti N adalah pengguna aktif dengan role Manage asset & TAG pada Group pengajuan masing-masing; ada approver independen selain Maya L sehingga DU-046-1 menunggu keputusan.
- Kondisi: format tanggal General Settings `dd/MM/yy` dan format waktu 24 jam; kolom Requested By tampil.

## Test Steps

### Nilai sel tabel Waiting for Approval
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi tabel sub tab Waiting for Approval memuat baris `Gudang Mangga {runId}`, `Gudang Jati {runId}`, `Gudang Akasia {runId}` dengan Group tampil sebagai Badge
3. Verifikasi Registration ID baris `Gudang Mangga {runId}` berformat `REG-YYYYMMDD-NNNNN` dan sama dengan Registration ID milik DU-046-1
4. Verifikasi Total Asset baris `Gudang Mangga {runId}` bernilai `12`
5. Verifikasi Requested By baris `Gudang Mangga {runId}` bernilai `Maya L.`[^drift-1]
6. Verifikasi Last Updated baris `Gudang Mangga {runId}` tampil dengan Date Format `dd/MM/yy` diikuti Time Format 24 jam

### Urutan awal Last Updated terbaru di atas
7. Verifikasi baris `Gudang Mangga {runId}` tampil di atas baris `Gudang Jati {runId}`, dan baris `Gudang Jati {runId}` tampil di atas baris `Gudang Akasia {runId}` (Last Updated terbaru di atas)

### Search pada kolom Searchable
8. Ganti isi kotak search dengan Registration ID milik DU-046-2, tekan Enter
9. Verifikasi tabel sub tab Waiting for Approval memuat baris `Gudang Jati {runId}` dan tidak memuat baris `Gudang Mangga {runId}`
10. Ganti isi kotak search dengan `Gudang Akasia {runId}`, tekan Enter
11. Verifikasi tabel sub tab Waiting for Approval memuat baris `Gudang Akasia {runId}` dan tidak memuat baris `Gudang Jati {runId}`
12. Ganti isi kotak search dengan `30`, tekan Enter
13. Verifikasi tabel sub tab Waiting for Approval memuat baris `Gudang Jati {runId}` dan tidak memuat baris `Gudang Mangga {runId}`
14. Ganti isi kotak search dengan `Hadi K`, tekan Enter
15. Verifikasi tabel sub tab Waiting for Approval memuat baris `Gudang Jati {runId}` dan tidak memuat baris `Gudang Mangga {runId}`
16. Ganti isi kotak search dengan tanggal Last Updated baris `Gudang Jati {runId}` dalam Date Format `dd/MM/yy`, dari `T0 − 2 hari`, tekan Enter
17. Verifikasi baris `Gudang Jati {runId}` tidak tampil karena kolom Last Updated tidak dicari

### Filter pada kolom Filterable
18. Klik ikon Filter
19. Verifikasi panel Filter memuat field `Group`, `Total Asset`, `Requested By`, dan `Last Updated` dan tidak memuat field `Registration ID`
20. Ganti isi kotak search dengan `{runId}`, tekan Enter
21. Pilih Group `Gudang Jati {runId}` pada field `Group`
22. Klik `[Apply]`
23. Verifikasi tabel sub tab Waiting for Approval memuat baris `Gudang Jati {runId}` dan tidak memuat baris `Gudang Mangga {runId}`
24. Klik `[Clear Field]`
25. Klik `[Apply]`
26. Isi Min `12` pada field `Total Asset`
27. Isi Max `30` pada field `Total Asset`
28. Klik `[Apply]`
29. Verifikasi tabel sub tab Waiting for Approval memuat baris `Gudang Mangga {runId}`, `Gudang Jati {runId}` dan tidak memuat baris `Gudang Akasia {runId}`
30. Klik `[Clear Field]`
31. Klik `[Apply]`
32. Pilih opsi `Maya L.` pada field `Requested By`[^drift-1]
33. Klik `[Apply]`
34. Verifikasi tabel sub tab Waiting for Approval memuat baris `Gudang Mangga {runId}` dan tidak memuat baris `Gudang Jati {runId}`
35. Klik `[Clear Field]`
36. Klik `[Apply]`
37. Pilih rentang tanggal `T0 − 2 hari` sampai `T0 − 1 hari` pada field `Last Updated`
38. Klik `[Apply]`
39. Verifikasi tabel sub tab Waiting for Approval memuat baris `Gudang Mangga {runId}`, `Gudang Jati {runId}` dan tidak memuat baris `Gudang Akasia {runId}`
40. Klik `[Clear Field]`
41. Klik `[Apply]`

### Sort pada kolom Sortable
42. Klik ikon sort pada header kolom `Registration ID`
43. Verifikasi urutan baris kolom `Registration ID` naik: `Gudang Akasia {runId}`, `Gudang Jati {runId}`, `Gudang Mangga {runId}`
44. Klik ikon sort pada header kolom `Group`
45. Verifikasi urutan baris kolom `Group` naik: `Gudang Akasia {runId}`, `Gudang Jati {runId}`, `Gudang Mangga {runId}`
46. Klik ikon sort pada header kolom `Total Asset`
47. Verifikasi urutan baris kolom `Total Asset` naik: `Gudang Akasia {runId}`, `Gudang Mangga {runId}`, `Gudang Jati {runId}`
48. Klik ikon sort pada header kolom `Requested By`
49. Verifikasi urutan baris kolom `Requested By` naik: `Gudang Jati {runId}`, `Gudang Mangga {runId}`, `Gudang Akasia {runId}`
50. Klik ikon sort pada header kolom `Last Updated`
51. Verifikasi urutan baris kolom `Last Updated` naik (Oldest First): `Gudang Akasia {runId}`, `Gudang Jati {runId}`, `Gudang Mangga {runId}`

### Kolom yang disembunyikan tidak dicari
52. Ganti isi kotak search dengan `Hadi K`, tekan Enter
53. Verifikasi tabel sub tab Waiting for Approval memuat baris `Gudang Jati {runId}`
54. Klik header kolom Actions `⋯`
55. Hilangkan centang `Requested By` pada panel Column Visibility
56. Ganti isi kotak search dengan `Hadi K`, tekan Enter
57. Verifikasi baris `Gudang Jati {runId}` tidak tampil di tabel sub tab Waiting for Approval
58. Centang kembali `Requested By` pada panel Column Visibility
59. Ganti isi kotak search dengan `Hadi K`, tekan Enter
60. Verifikasi tabel sub tab Waiting for Approval memuat baris `Gudang Jati {runId}`

### Aksi baris sesuai pengaju
61. Ganti isi kotak search dengan `{runId}`, tekan Enter
62. Verifikasi kolom `Actions` adalah kolom terakhir tabel sub tab Waiting for Approval, sesudah kolom `Last Updated`
63. Verifikasi baris `Gudang Mangga {runId}` milik pengaju menampilkan ikon aksi `Detail`, `Registration Log`, dan `Cancel registration`
64. Verifikasi baris `Gudang Jati {runId}` milik pengguna lain menampilkan ikon aksi `Detail` dan `Registration Log` dan tidak menampilkan `Cancel registration`

### Aksi Detail membuka Detail pengajuan
65. Klik ikon `Detail` pada baris `Gudang Mangga {runId}`
66. Verifikasi halaman Detail pengajuan terbuka dengan Registration ID milik DU-046-1
67. Klik tautan breadcrumb `Waiting for Approval`

### Klik Registration ID membuka Detail pengajuan
68. Ganti isi kotak search dengan `{runId}`, tekan Enter
69. Klik Registration ID milik DU-046-2
70. Verifikasi halaman Detail pengajuan terbuka dengan Registration ID milik DU-046-2
71. Klik tautan breadcrumb `Waiting for Approval`

### Aksi Registration Log membuka dialog
72. Ganti isi kotak search dengan `{runId}`, tekan Enter
73. Klik ikon `Registration Log` pada baris `Gudang Jati {runId}`
74. Verifikasi dialog `Registration Log` tampil di atas halaman Waiting for Approval
75. Klik ikon X pada dialog `Registration Log`

### Aksi Cancel registration membuka dialog konfirmasi
76. Klik ikon `Cancel registration` pada baris `Gudang Mangga {runId}`
77. Verifikasi dialog `Cancel Registration` tampil
78. Klik `[Go Back]` pada dialog `Cancel Registration`

[^drift-1]: Drift PRD vs foundation vs override. PRD §4.1 kolom Requested By: `Nama singkat`. foundation `prd-conventions.md` §9.13: nama singkat `[First Name] [Last Initial]`, contoh tanpa titik (`John L`, `Alexander G`). Override O-4: nama singkat mengakhiri inisial dengan titik (`John L.`, `Alexander G.`). Diasersi: O-4, karena override menang atas foundation (SB-6).
