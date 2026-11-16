---
id: TC-FA-FATR-E2E-012-overrides-tabel
title: "Tabel Overrides menampilkan override per node dan tab"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§4.1#r90, §4.1#p43, §4.1#p50, §11#r10, EB-TBL-7@tabel-overrides]
smoke: []
dependsOn: []
trace:
  §4.1#r90: [16, 17]
  §4.1#p43: [3, 4, 6, 7, 9, 10, 12, 13, 16, 17, 18, 19, 24, 25, 26, 27]
  §4.1#p50: [38, 41, 42, 43, 44, 46, 48, 52, 53, 63, 67, 68, 69, 70, 72]
  §11#r10: 5
  EB-TBL-7@tabel-overrides: [75, 79, 80, 81, 82]
anchor: [3, 16]
coverage:
  web: automated
---

# Tabel Overrides menampilkan override per node dan tab

## Prerequisites
- Aktor: Total Control `Rina Wulandari` pada entitas khusus `Entitas Tabel Overrides {runId}` (DU-012-1), yang tidak dipakai spec lain.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-012-1: entitas khusus `Entitas Tabel Overrides {runId}` dengan aktor bernama Rina Wulandari, Total Control.
  - DU-012-2: Category leaf `Machinery {runId}`.
  - DU-012-3: Category leaf `Laptop {runId}`.
  - DU-012-4: 10 Group tingkat atas `Cabang {n} {runId}` dengan n dari 1 sampai 10.
  - DU-012-5: Group tingkat atas `Workshop {runId}`.
  - DU-012-6: Group tingkat atas `Proyek Karawang {runId}`.
  - DU-012-7: 10 override Group `Cabang {n} {runId}` di Category `Machinery {runId}` transaksi `Borrow`, masing-masing Overridden `Max duration (7 days)`, dibuat berurutan dari n=1 paling awal sampai n=10 oleh `Rina Wulandari`.
  - DU-012-8: override Group `Workshop {runId}` di Category `Laptop {runId}` transaksi `Borrow`, Overridden `Max duration (12 hours), Auto-approve when duration ≤ (4 hours)`, dibuat sesudah DU-012-7.
  - DU-012-9: override Group `Proyek Karawang {runId}` di All categories transaksi `Borrow`, Overridden `Max duration (30 days), Max extensions (1), Auto-approve when duration ≤ (3 days)`, dibuat paling akhir oleh `Rina Wulandari`, sehingga Created By baris itu tampil `Rina W`.
  - DU-012-10: override Group `Workshop {runId}` di Category `Machinery {runId}` transaksi `Assign`, Overridden `Recipient acceptance (Optional)`.
- Kondisi:
  - Company default menyimpan Duration unit `Days`, dan Category `Laptop {runId}` menyimpan Duration unit `Hours`; level Feature Suite Borrowing `Full`.
  - Ukuran halaman tabel Overrides bernilai `10`.

## Test Steps

### Category leaf menampilkan override Category itu dan override All categories pada tab aktif
1. Klik node `Machinery {runId}` di Sidebar Category Tree
2. Klik tab `Borrow`
3. Verifikasi baris dengan Target `Proyek Karawang {runId}` dan Overridden `Max duration (30 days), Max extensions (1), Auto-approve when duration ≤ (3 days)` tampil di tabel Overrides sebagai override All categories
4. Verifikasi baris dengan Target `Cabang 10 {runId}` dan Overridden `Max duration (7 days)` tampil di tabel Overrides
5. Verifikasi baris `Proyek Karawang {runId}` memiliki Created By `Rina W`
6. Verifikasi laporan paginasi `Showing 1 to 10 of 11` tampil di bawah tabel Overrides
7. Verifikasi tidak ada baris dengan Target `Workshop {runId}` di tabel Overrides node `Machinery {runId}` tab `Borrow`
8. Klik tombol `Next Page` pada paginasi tabel Overrides
9. Verifikasi laporan paginasi `Showing 11 to 11 of 11` tampil di bawah tabel Overrides
10. Verifikasi baris dengan Target `Cabang 1 {runId}` tampil sebagai baris di halaman 2 tabel Overrides
11. Klik tab `Assign`
12. Verifikasi baris dengan Target `Workshop {runId}` dan Overridden `Recipient acceptance (Optional)` tampil di tabel Overrides
13. Verifikasi tidak ada baris dengan Target `Cabang 1 {runId}` di tabel Overrides pada tab `Assign`

### Angka kolom Overridden memakai satuan Duration unit tempat nilai disimpan
14. Klik node `Laptop {runId}` di Sidebar Category Tree
15. Klik tab `Borrow`
16. Verifikasi baris dengan Target `Workshop {runId}` dan Overridden `Max duration (12 hours), Auto-approve when duration ≤ (4 hours)` tampil di tabel Overrides
17. Verifikasi baris dengan Target `Proyek Karawang {runId}` dan Overridden `Max duration (30 days), Max extensions (1), Auto-approve when duration ≤ (3 days)` tampil di tabel Overrides Category `Laptop {runId}` dengan satuan `days`
18. Verifikasi tidak ada baris dengan Target `Cabang 1 {runId}` di tabel Overrides Category `Laptop {runId}`
19. Verifikasi laporan paginasi `Showing 1 to 2 of 2` tampil di bawah tabel Overrides Category `Laptop {runId}`

### All categories menampilkan override semua Category dengan kolom Category
20. Klik node `All categories` di Sidebar Category Tree
21. Klik tab `Borrow`
22. Klik header kolom Actions pada tabel Overrides
23. Centang kolom `Category`
24. Verifikasi baris dengan Target `Workshop {runId}` dan Category `Laptop {runId}` tampil di tabel Overrides
25. Verifikasi baris dengan Target `Cabang 10 {runId}` dan Category `Machinery {runId}` tampil di tabel Overrides
26. Verifikasi baris dengan Target `Proyek Karawang {runId}` dan Category `All categories` tampil di tabel Overrides
27. Verifikasi laporan paginasi `Showing 1 to 10 of 12` tampil di bawah tabel Overrides pada node `All categories`

### Berpindah tab mengembalikan Search, Filter, Sort, halaman, dan seleksi ke bawaan
28. Klik node `Machinery {runId}` di Sidebar Category Tree
29. Klik tab `Borrow`
30. Ketik Search `{runId}`, tekan Enter
31. Klik ikon filter pada toolbar tabel Overrides
32. Klik field `Scope` pada panel filter
33. Pilih opsi `Group`
34. Klik `[Apply]`
35. Klik header kolom Target pada tabel Overrides
36. Klik tombol `Next Page` pada paginasi tabel Overrides
37. Centang baris `Proyek Karawang {runId}`
38. Verifikasi `Bulk Action` tampil pada toolbar tabel Overrides dengan baris `Proyek Karawang {runId}` terpilih di halaman 2
39. Klik tab `Assign`
40. Klik tab `Borrow`
41. Verifikasi laporan paginasi `Showing 1 to 10 of 11` tampil kembali di halaman 1 tabel Overrides
42. Verifikasi baris pertama tabel Overrides memiliki Target `Proyek Karawang {runId}` sebagai urutan bawaan Created At Newest First
43. Verifikasi kotak Search pada tabel Overrides kosong dengan placeholder `Search by target or overridden...`
44. Verifikasi `Bulk Action` tidak tampil pada toolbar tabel Overrides
45. Klik ikon filter pada toolbar tabel Overrides
46. Verifikasi field `Scope` pada panel filter menampilkan placeholder `All scopes`
47. Klik field `Overridden` pada panel filter
48. Verifikasi opsi `Max duration` dan opsi `Max extensions` tampil pada field `Overridden`
49. Klik tab `Assign`
50. Klik ikon filter pada toolbar tabel Overrides
51. Klik field `Overridden` pada panel filter
52. Verifikasi opsi `Recipient acceptance` tampil pada field `Overridden`
53. Verifikasi opsi `Max duration` tidak tampil pada field `Overridden`

### Berpindah node mengembalikan Search, Filter, Sort, halaman, dan seleksi ke bawaan
54. Klik tab `Borrow`
55. Ketik Search `{runId}`, tekan Enter
56. Klik ikon filter pada toolbar tabel Overrides
57. Klik field `Scope` pada panel filter
58. Pilih opsi `Group`
59. Klik `[Apply]`
60. Klik header kolom Target pada tabel Overrides
61. Klik tombol `Next Page` pada paginasi tabel Overrides
62. Centang baris `Proyek Karawang {runId}`
63. Verifikasi `Bulk Action` tampil pada toolbar tabel Overrides sebelum berpindah node dengan baris `Proyek Karawang {runId}` terpilih di halaman 2
64. Klik node `Laptop {runId}` di Sidebar Category Tree
65. Klik node `Machinery {runId}` di Sidebar Category Tree
66. Klik tab `Borrow`
67. Verifikasi laporan paginasi `Showing 1 to 10 of 11` tampil di halaman 1 tabel Overrides sesudah berpindah node
68. Verifikasi baris pertama tabel Overrides memiliki Target `Proyek Karawang {runId}` sebagai urutan bawaan Created At Newest First sesudah berpindah node
69. Verifikasi kotak Search pada tabel Overrides kosong sesudah berpindah node
70. Verifikasi `Bulk Action` tidak tampil pada toolbar tabel Overrides sesudah berpindah node
71. Klik ikon filter pada toolbar tabel Overrides
72. Verifikasi field `Scope` pada panel filter menampilkan placeholder `All scopes` sesudah berpindah node

### Menghapus baris terakhir di halaman terakhir memindahkan tabel ke halaman terakhir yang masih ada
73. Klik tab `Borrow`
74. Klik tombol `Next Page` pada paginasi tabel Overrides
75. Verifikasi laporan paginasi `Showing 11 to 11 of 11` tampil dengan baris `Cabang 1 {runId}` sebagai satu-satunya baris halaman 2
76. Klik `⋯` pada baris `Cabang 1 {runId}`
77. Klik `Delete`
78. Klik `[Delete]`
79. Verifikasi toast `Success, override has been deleted.` tampil untuk override `Cabang 1 {runId}`
80. Verifikasi laporan paginasi `Showing 1 to 10 of 10` tampil di halaman 1 tabel Overrides
81. Verifikasi baris dengan Target `Cabang 10 {runId}` dan Overridden `Max duration (7 days)` tampil di halaman 1 tabel Overrides
82. Verifikasi tidak ada baris dengan Target `Cabang 1 {runId}` di tabel Overrides
