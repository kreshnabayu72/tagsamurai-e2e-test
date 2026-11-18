---
id: TC-FA-ASTL-E2E-010-navigasi-asset-detail
title: "Navigasi ke Asset Detail dan kembali ke daftar"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ASTL-LOGIC-18, "§4.4#b1", "§4.4#b2"]
smoke: []
dependsOn: []
trace:
  ASTL-LOGIC-18: [13, 21]
  "§4.4#b1": [15, 16, 17, 19, 21, 23, 24, 27, 28, 44, 45, 46, 48, 52, 53, 54, 56, 59, 60, 61, 63, 67, 68, 69, 71]
  "§4.4#b2": [29, 31, 32, 33, 76, 78, 80]
anchor: [11, 42]
coverage:
  web: automated
---

# Navigasi ke Asset Detail dan kembali ke daftar

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets (tab `Assets`).
- Data:
  - DU-010-1: Group `Kantor Pusat {runId}` dengan anak `Operasional {runId}`.
  - DU-010-2: 12 aset `Laptop Operasional - {n} {runId}` dengan `n` dari 1 sampai 12, Brand `Lenovo`, Group `Operasional {runId}`, berstatus `Borrowed`.
  - DU-010-3: Aset `Meja Kerja - 1 {runId}`, Brand `Ikea`, Group `Kantor Pusat {runId}`, berstatus `Available`.

## Test Steps

### Halaman detail aset dibuka dari kolom Name pada daftar yang sudah disetel
1. Ketik Search `{runId}`, tekan Enter
2. Klik kartu `In Transaction`
3. Klik node `Operasional {runId}` pada sidebar Group
4. Klik ikon Filter
5. Pilih Brand `Lenovo` pada Filter Panel
6. Klik `[Apply]`
7. Klik ikon Filter
8. Klik header kolom `Name`
9. Klik header kolom `Name`
10. Klik tombol halaman `2`
11. Verifikasi baris `Laptop Operasional - 2 {runId}` dan `Laptop Operasional - 1 {runId}` tampil pada halaman 2
12. Klik `Laptop Operasional - 2 {runId}` pada kolom `Name`
13. Verifikasi halaman detail aset `Laptop Operasional - 2 {runId}` terbuka

### State daftar dipertahankan saat kembali dari halaman detail aset
14. Klik `Back`
15. Verifikasi kotak Search berisi `{runId}`
16. Verifikasi kartu `In Transaction` aktif
17. Verifikasi node `Operasional {runId}` terpilih pada sidebar Group
18. Klik ikon Filter
19. Verifikasi field Brand pada Filter Panel berisi `Lenovo`
20. Klik ikon Filter
21. Verifikasi halaman 2 memuat `Laptop Operasional - 2 {runId}` lalu `Laptop Operasional - 1 {runId}` dengan urutan tersebut

### State daftar dipertahankan saat halaman dimuat ulang dan saat kembali lewat sidebar
22. Muat ulang halaman
23. Verifikasi kotak Search berisi `{runId}`
24. Verifikasi halaman 2 memuat `Laptop Operasional - 2 {runId}` lalu `Laptop Operasional - 1 {runId}` dengan urutan tersebut
25. Klik `Laptop Operasional - 2 {runId}` pada kolom `Name`
26. Klik menu `Fixed Asset > Assets` pada sidebar
27. Verifikasi kotak Search berisi `{runId}`
28. Verifikasi halaman 2 memuat `Laptop Operasional - 2 {runId}` lalu `Laptop Operasional - 1 {runId}` dengan urutan tersebut

### Klik menu saat berada di tab Assets mengatur ulang daftar ke default
29. Verifikasi tab `Assets` sedang aktif
30. Klik menu `Fixed Asset > Assets` pada sidebar
31. Verifikasi kartu `All` aktif
32. Verifikasi node `All Groups` terpilih pada sidebar Group
33. Verifikasi tombol halaman `1` aktif pada Paginator tabel

### Daftar dipertahankan saat kembali lewat breadcrumb dari halaman detail aset
34. Ketik Search `{runId}`, tekan Enter
35. Klik kartu `In Transaction`
36. Klik node `Operasional {runId}` pada sidebar Group
37. Klik ikon Filter
38. Pilih Brand `Lenovo` pada Filter Panel
39. Klik `[Apply]`
40. Klik ikon Filter
41. Klik `Laptop Operasional - 2 {runId}` pada kolom `Name`
42. Verifikasi halaman detail aset `Laptop Operasional - 2 {runId}` terbuka
43. Klik breadcrumb `Assets` pada halaman detail aset
44. Verifikasi kotak Search berisi `{runId}`
45. Verifikasi kartu `In Transaction` aktif
46. Verifikasi node `Operasional {runId}` terpilih pada sidebar Group
47. Klik ikon Filter
48. Verifikasi field Brand pada Filter Panel berisi `Lenovo`
49. Klik ikon Filter

### Daftar dipertahankan saat kembali lewat sidebar dari menu lain
50. Klik menu lain pada sidebar selain `Fixed Asset > Assets`
51. Klik menu `Fixed Asset > Assets` pada sidebar
52. Verifikasi kotak Search berisi `{runId}`
53. Verifikasi kartu `In Transaction` aktif
54. Verifikasi node `Operasional {runId}` terpilih pada sidebar Group
55. Klik ikon Filter
56. Verifikasi field Brand pada Filter Panel berisi `Lenovo`
57. Klik ikon Filter

### Kartu, node, dan filter dipertahankan sesudah muat ulang dan kembali lewat sidebar dari halaman detail aset
58. Muat ulang halaman
59. Verifikasi kotak Search berisi `{runId}`
60. Verifikasi kartu `In Transaction` aktif
61. Verifikasi node `Operasional {runId}` terpilih pada sidebar Group
62. Klik ikon Filter
63. Verifikasi field Brand pada Filter Panel berisi `Lenovo`
64. Klik ikon Filter
65. Klik `Laptop Operasional - 2 {runId}` pada kolom `Name`
66. Klik menu `Fixed Asset > Assets` pada sidebar
67. Verifikasi kotak Search berisi `{runId}`
68. Verifikasi kartu `In Transaction` aktif
69. Verifikasi node `Operasional {runId}` terpilih pada sidebar Group
70. Klik ikon Filter
71. Verifikasi field Brand pada Filter Panel berisi `Lenovo`
72. Klik ikon Filter

### Klik menu saat di tab Assets mengatur ulang Search, filter, dan sort
73. Klik header kolom `Name`
74. Klik header kolom `Name`
75. Klik menu `Fixed Asset > Assets` pada sidebar
76. Verifikasi kotak Search kosong
77. Klik ikon Filter
78. Verifikasi field Brand pada Filter Panel kosong dengan placeholder `All brands`
79. Klik ikon Filter
80. Verifikasi header kolom `Name` tidak menampilkan indikator sort aktif karena sort kembali ke default
