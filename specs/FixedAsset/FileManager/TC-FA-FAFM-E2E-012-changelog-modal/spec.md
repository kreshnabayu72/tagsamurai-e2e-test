---
id: TC-FA-FAFM-E2E-012-changelog-modal
title: "Modal Changelog: entri Delete dan Permanently Delete terbaca"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["INV-09b", "INV-09d", "INV-09e", "INV-09f", "INV-09g", "INV-11f", "T-FAFM-04", "TBL-03a", "TBL-04d", "TBL-05d", "TBL-07a", "§4.1#p19", "§8.1#r1", "§8.1#r4", "EB-SRC-5@tabel-changelog", "EB-LOG-1"]
smoke: []
dependsOn: []
trace:
  "INV-09b": 2
  "INV-09d": [14, 28, 36]
  "INV-09e": [14, 68]
  "INV-09f": [14, 16]
  "INV-09g": [18, 19, 20]
  "INV-11f": 18
  "T-FAFM-04": [4, 5, 6, 7, 8, 9, 10, 22, 24, 28, 29, 30, 32, 36, 37, 41, 45, 46, 50, 54, 55, 60, 61, 64, 68]
  "TBL-03a": [28, 29]
  "TBL-04d": 22
  "TBL-05d": 20
  "TBL-07a": 2
  "§4.1#p19": 19
  "§8.1#r1": [5, 6]
  "§8.1#r4": [5, 6]
  "EB-SRC-5@tabel-changelog": [73, 75, 81]
  "EB-LOG-1": 12
anchor: [4, 12, 14, 28, 32, 36, 41, 45, 50, 54, 60, 68]
coverage:
  web: automated
---

# Modal Changelog: entri Delete dan Permanently Delete terbaca

## Prerequisites
- Aktor: Total Control, user `Dimas Anggoro {runId}` (tampil `Dimas A`), akun aktif dengan kredensial disediakan fase 2.
- Layar awal: halaman Settings > File Manager.
- Data:
  - User `Wahyu Pratama {runId}` (DU-012-1, tampil `Wahyu P`) dan `Nadia Rahayu {runId}` (DU-012-2, tampil `Nadia R`) ada di entitas aktor.
  - DU-012-3: Entri Changelog Date `T0 − 10 hari, pukul 10:00`, Action `Delete`, File Name `laporan-bulanan-{runId}.pdf`, Field `File Name`, Old Value `laporan-bulanan-{runId}.pdf`, New Value `—`, Modified By `Wahyu P`.
  - DU-012-4: Entri Changelog Date `T0 − 9 hari, pukul 11:30`, Action `Permanently Delete`, File Name `laporan-bulanan-{runId}.pdf`, Field `File Name`, Old Value `laporan-bulanan-{runId}.pdf`, New Value `—`, Modified By `Wahyu P`.
  - DU-012-5: Entri Changelog Date `T0 − 5 hari, pukul 14:00`, Action `Delete`, File Name `kontrak-vendor-{runId}.pdf`, Field `File Name`, Old Value `kontrak-vendor-{runId}.pdf`, New Value `—`, Modified By `Nadia R`.
  - DU-012-6: Entri Changelog Date `T0 − 3 hari, pukul 08:15`, Action `Delete`, File Name `foto-lama-{runId}.jpg`, Field `File Name`, Old Value `foto-lama-{runId}.jpg`, New Value `—`, Modified By `System`, dari auto-transition modul sumber.
  - DU-012-7: Entri Changelog Date `T0 − 2 hari, pukul 02:00`, Action `Permanently Delete`, File Name `arsip-lama-{runId}.png`, Field `File Name`, Old Value `arsip-lama-{runId}.png`, New Value `—`, Modified By `System`, dari job auto-purge.
  - Himpunan entri Changelog ber-runId seluruhnya berjumlah 5: DU-012-3 sampai DU-012-7.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `HH:mm`.

## Test Steps

### Changelog dibuka dari header kartu Storage Usage dan memuat entri Delete dan Permanently Delete
1. Klik `Changelog` pada header kartu `Storage Usage`
2. Verifikasi modal `Changelog: File Manager` tampil
3. Ketik Search `{runId}`, tekan Enter
4. Verifikasi tabel Changelog menampilkan `5` entri
5. Verifikasi entri dengan Action `Delete` untuk File Name `laporan-bulanan-{runId}.pdf` memuat Field `File Name`, Old Value `laporan-bulanan-{runId}.pdf`, New Value `—`, dan Modified By `Wahyu P`
6. Verifikasi entri dengan Action `Permanently Delete` untuk File Name `laporan-bulanan-{runId}.pdf` memuat Field `File Name`, Old Value `laporan-bulanan-{runId}.pdf`, New Value `—`, dan Modified By `Wahyu P`
7. Verifikasi entri dengan Action `Permanently Delete` untuk File Name `arsip-lama-{runId}.png` memuat Modified By `System`
8. Verifikasi entri dengan Action `Delete` untuk File Name `foto-lama-{runId}.jpg` memuat Modified By `System`
9. Verifikasi entri dengan Action `Delete` untuk File Name `kontrak-vendor-{runId}.pdf` memuat Modified By `Nadia R`
10. Verifikasi Date entri File Name `laporan-bulanan-{runId}.pdf` dengan Action `Delete` tampil dalam format `dd/MM/yy HH:mm`
11. Ganti isi kotak search dengan `laporan-bulanan-{runId}`, tekan Enter
12. Verifikasi hanya dua entri untuk File Name `laporan-bulanan-{runId}.pdf` yang tampil, yaitu Action `Delete` dan Action `Permanently Delete`
13. Klik `(←)` pada kotak Search

### Changelog read-only dengan toolbar Search, Filter, dan Download
14. Verifikasi toolbar modal `Changelog` memuat ikon Search, Filter, dan Download
15. Klik ikon Download pada modal `Changelog`
16. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil pada modal `Changelog`
17. Tutup pilihan Download
18. Verifikasi tidak ada kotak centang pada header tabel maupun pada entri File Name `laporan-bulanan-{runId}.pdf`
19. Verifikasi tidak ada aksi baris pada entri File Name `laporan-bulanan-{runId}.pdf`
20. Verifikasi tidak ada bar aksi bulk pada modal `Changelog`

### Urutan default Date terbaru dan sort Date
21. Ketik Search `{runId}`, tekan Enter
22. Verifikasi urutan Action dan File Name dari atas ke bawah: `Permanently Delete` `arsip-lama-{runId}.png`, `Delete` `foto-lama-{runId}.jpg`, `Delete` `kontrak-vendor-{runId}.pdf`, `Permanently Delete` `laporan-bulanan-{runId}.pdf`, `Delete` `laporan-bulanan-{runId}.pdf`
23. Klik ikon sort pada header kolom `Date`
24. Verifikasi entri pertama adalah Action `Delete` untuk File Name `laporan-bulanan-{runId}.pdf`
25. Klik ikon sort pada header kolom `Date` sekali lagi
26. Klik ikon sort pada header kolom `Date` untuk ketiga kalinya

### Panel Filter memuat field menurut kolom filterable
27. Klik ikon Filter
28. Verifikasi panel Filter tampil dengan field `Date`, `Action`, `File Name`, dan `Modified By`
29. Verifikasi tidak ada field filter untuk `Field`, `Old Value`, dan `New Value`
30. Verifikasi placeholder field `Select date`, `All actions`, `All files`, dan `All users`

### Filter Action memuat opsi dari nilai yang tercatat dan menyaring entri
31. Buka dropdown field `Action`
32. Verifikasi opsi `Delete` dan `Permanently Delete` tampil
33. Pilih Action `Permanently Delete`
34. Tutup dropdown field `Action`
35. Klik `[Apply]`
36. Verifikasi entri File Name `arsip-lama-{runId}.png` dan entri `Permanently Delete` File Name `laporan-bulanan-{runId}.pdf` tampil
37. Verifikasi entri dengan Action `Delete` untuk File Name `kontrak-vendor-{runId}.pdf` tidak tampil
38. Klik `[Clear Field]`
39. Klik `[Apply]`

### Filter File Name dan Modified By
40. Buka dropdown field `File Name`
41. Verifikasi opsi `laporan-bulanan-{runId}.pdf`, `kontrak-vendor-{runId}.pdf`, `arsip-lama-{runId}.png`, dan `foto-lama-{runId}.jpg` tampil
42. Pilih File Name `arsip-lama-{runId}.png`
43. Tutup dropdown field `File Name`
44. Klik `[Apply]`
45. Verifikasi entri File Name `arsip-lama-{runId}.png` tampil
46. Verifikasi entri File Name `laporan-bulanan-{runId}.pdf` tidak tampil
47. Klik `[Clear Field]`
48. Klik `[Apply]`
49. Buka dropdown field `Modified By`
50. Verifikasi opsi `Wahyu Pratama {runId}` dan `Nadia Rahayu {runId}` tampil dengan nama lengkap, serta opsi `System`
51. Pilih Modified By `Nadia Rahayu {runId}`
52. Tutup dropdown field `Modified By`
53. Klik `[Apply]`
54. Verifikasi entri File Name `kontrak-vendor-{runId}.pdf` tampil
55. Verifikasi entri File Name `laporan-bulanan-{runId}.pdf` tidak tampil
56. Klik `[Clear Field]`
57. Klik `[Apply]`

### Filter rentang Date
58. Pilih rentang tanggal dari T0 − 11 hari sampai T0 − 9 hari pada field `Date`
59. Klik `[Apply]`
60. Verifikasi entri File Name `laporan-bulanan-{runId}.pdf` tampil
61. Verifikasi entri File Name `arsip-lama-{runId}.png` tidak tampil
62. Pilih rentang tanggal dari T0 − 60 hari sampai T0 − 40 hari pada field `Date`
63. Klik `[Apply]`
64. Verifikasi pesan `No results found` tampil
65. Klik `[Clear Field]`
66. Klik `[Apply]`

### Kolom searchable yang disembunyikan tidak lagi cocok dan cocok lagi saat ditampilkan
67. Ganti isi kotak search dengan `arsip-lama-{runId}`, tekan Enter
68. Verifikasi entri File Name `arsip-lama-{runId}.png` tampil
69. Klik header kolom `Actions` (`⋯`) pada tabel
70. Hilangkan centang kolom `File Name` pada panel Column Visibility
71. Hilangkan centang kolom `Old Value` pada panel Column Visibility
72. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility
73. Verifikasi header kolom `File Name` dan `Old Value` tidak ada lagi di tabel
74. Ganti isi kotak search dengan `arsip-lama-{runId}`, tekan Enter
75. Verifikasi pesan `No results found` tampil di modal `Changelog`
76. Klik header kolom `Actions` (`⋯`) pada tabel
77. Centang kolom `File Name` pada panel Column Visibility
78. Centang kolom `Old Value` pada panel Column Visibility
79. Klik header kolom `Actions` (`⋯`) sekali lagi untuk menutup panel Column Visibility
80. Ganti isi kotak search dengan `arsip-lama-{runId}`, tekan Enter
81. Verifikasi entri File Name `arsip-lama-{runId}.png` tampil
82. Klik `(←)` pada kotak Search
