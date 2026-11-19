---
id: TC-FA-FASVC-E2E-022-daftar-setup-column-bertahan
title: "Setup Column: Konfigurasi Kolom Bertahan, Search Mengikuti Kolom Tampil, Per Akun"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-KOL-2@tabel-service-center", "EB-SRC-5@tabel-service-center"]
smoke: []
dependsOn: []
trace:
  "EB-KOL-2@tabel-service-center": [6, 19, 20, 23, 25, 27, 29, 31, 41, 42, 43, 44, 46, 50, 55, 63, 68, 72, 79, 85, 92, 97, 100]
  "EB-SRC-5@tabel-service-center": [2, 8, 13]
anchor: []
coverage:
  web: automated
---

# Setup Column: Konfigurasi Kolom Bertahan, Search Mengikuti Kolom Tampil, Per Akun

## Prerequisites
- Aktor: Total Control `Rina Wijaya` (cakupan seluruh Group). Aktor kedua: Total Control `Tika Kolom {runId}`.
- Layar awal: Add-ons > Service Center (halaman daftar).
- Data:
  - DU-022-1: Group `Cabang Kolom {runId}`, anak langsung dari root pohon Group.
  - DU-022-2: User `Tika Kolom {runId}`, role Total Control, Status `Active`; Setup Column memakai konfigurasi bawaan.
  - DU-022-3: Service Center `Bengkel Kolom {runId}`, Service type `Routine`, Available to `Cabang Kolom {runId}`, City `Kota Kolom {runId}`, Usage `0`, Status `Active`, Company email `kolom@bengkelkolom.example`.
  - DU-022-4: Service Center `Cakra Kolom {runId}`, Service type `Routine`, Available to `Cabang Kolom {runId}`, City `Kota Cakra {runId}`, Usage `0`, Status `Active`, Company email `cakra@bengkelkolom.example`.
- Kondisi: client memiliki lisensi addon Maintenance berstatus aktif. Setup Column akun `Rina Wijaya` memakai konfigurasi bawaan saat spec dimulai dan dikembalikan ke bawaan di akhir spec.

## Test Steps

### Search hanya mencocokkan kolom yang tampil
1. Ketik Search `Kota Kolom {runId}` pada daftar, tekan Enter
2. Verifikasi baris `Bengkel Kolom {runId}` tampil karena kata kunci cocok di kolom City
3. Klik header kolom Actions (`⋯`) pada tabel daftar
4. Hilangkan centang `City` pada panel Column Visibility
5. Tekan Esc untuk menutup panel Column Visibility
6. Verifikasi urutan header kolom: `Name`, `Service Type`, `Specialization`, `Available To`, `Brands`, `Usage`, `Status`, `Modified By`, `Last Updated`
7. Tekan Enter pada kotak search daftar
8. Verifikasi empty state dengan judul `No results found` tampil, karena kolom City tersembunyi tidak lagi dicocokkan
9. Klik header kolom Actions (`⋯`) pada tabel daftar
10. Centang `City` pada panel Column Visibility
11. Tekan Esc untuk menutup panel Column Visibility
12. Tekan Enter pada kotak search daftar
13. Verifikasi baris `Bengkel Kolom {runId}` tampil kembali, karena kolom City tampil lagi
14. Klik `(←)` pada kotak Search

### Konfigurasi kolom dari panel Column Visibility bertahan sesudah muat ulang
15. Klik header kolom Actions (`⋯`) pada tabel daftar
16. Hilangkan centang `Usage` pada panel Column Visibility
17. Tekan Esc untuk menutup panel Column Visibility
18. Muat ulang halaman Service Center
19. Verifikasi urutan header kolom: `Name`, `Service Type`, `Specialization`, `Available To`, `City`, `Brands`, `Status`, `Modified By`, `Last Updated`
20. Verifikasi header kolom `Usage` bukan bagian dari tabel dan kolom `City` serta `Status` tetap tampil

### Urutan kolom dari dialog Setup Columns tersimpan sesudah Save dan bertahan sesudah muat ulang
21. Klik header kolom Actions (`⋯`) pada tabel daftar
22. Klik `Setup Columns`
23. Verifikasi dialog `Setup Columns` tampil dengan `Preview`, `Reset to Default`, dan `Save`[^drift-1]
24. Seret baris `Status` ke atas baris `City` pada daftar kolom dialog
25. Verifikasi tabel pada halaman tidak berubah sebelum `Save`: header `City` masih mendahului header `Status`
26. Klik `Save`
27. Verifikasi urutan header kolom: `Name`, `Service Type`, `Specialization`, `Available To`, `Status`, `City`, `Brands`, `Modified By`, `Last Updated`
28. Muat ulang halaman Service Center
29. Verifikasi urutan header kolom tetap `Name`, `Service Type`, `Specialization`, `Available To`, `Status`, `City`, `Brands`, `Modified By`, `Last Updated`

### Konfigurasi kolom bertahan sesudah logout dan login, sedangkan Search, Filter, Sort, dan ukuran halaman tidak ikut tersimpan
30. Ketik Search `Bengkel Kolom {runId}` pada daftar, tekan Enter
31. Verifikasi baris `Bengkel Kolom {runId}` tampil
32. Klik ikon `Filter` pada toolbar daftar
33. Pilih `Active` pada filter `Status`
34. Klik `[Apply]`
35. Klik header kolom `Name`
36. Klik header kolom `Name`
37. Pilih ukuran halaman `25` pada paginasi daftar
38. Keluar dari akun `Rina Wijaya`
39. Masuk sebagai `Rina Wijaya`
40. Buka Add-ons > Service Center
41. Verifikasi urutan header kolom: `Name`, `Service Type`, `Specialization`, `Available To`, `Status`, `City`, `Brands`, `Modified By`, `Last Updated`
42. Verifikasi kotak search daftar kosong dan baris Service Center selain `Bengkel Kolom {runId}` tampil
43. Verifikasi ikon `Filter` tidak menampilkan penanda filter aktif
44. Verifikasi ukuran halaman paginasi daftar bernilai `10`
45. Ketik Search `Kolom {runId}` pada daftar, tekan Enter
46. Verifikasi baris `Bengkel Kolom {runId}` berada di atas baris `Cakra Kolom {runId}`, karena Sort `Name` bawaan A-Z berlaku dan Sort descending sebelum logout tidak tersimpan
47. Klik `(←)` pada kotak Search

### Konfigurasi kolom bertahan di browser lain untuk user yang sama
48. Buka browser lain dan masuk sebagai `Rina Wijaya`
49. Buka Add-ons > Service Center
50. Verifikasi urutan header kolom: `Name`, `Service Type`, `Specialization`, `Available To`, `Status`, `City`, `Brands`, `Modified By`, `Last Updated`
51. Tutup browser lain

### User lain tetap melihat kolom default
52. Keluar dari akun `Rina Wijaya`
53. Masuk sebagai `Tika Kolom {runId}`
54. Buka Add-ons > Service Center
55. Verifikasi urutan header kolom `Name`, `Service Type`, `Specialization`, `Available To`, `City`, `Brands`, `Usage`, `Status`, `Modified By`, `Last Updated`
56. Keluar dari akun `Tika Kolom {runId}`

### Reset to Default mengembalikan tata letak bawaan setelah Save
57. Masuk sebagai `Rina Wijaya`
58. Buka Add-ons > Service Center
59. Klik header kolom Actions (`⋯`) pada tabel daftar
60. Klik `Setup Columns`
61. Klik `Reset to Default`
62. Klik `Save`
63. Verifikasi urutan header kolom `Name`, `Service Type`, `Specialization`, `Available To`, `City`, `Brands`, `Usage`, `Status`, `Modified By`, `Last Updated`

### Pin kolom bertahan sesudah muat ulang, logout lalu login, dan di browser lain
64. Klik header kolom Actions (`⋯`) pada tabel daftar
65. Klik `Setup Columns`
66. Klik tombol pin pada baris `Last Updated` pada daftar kolom dialog
67. Klik `Save`
68. Verifikasi urutan header kolom `Last Updated`, `Name`, `Service Type`, `Specialization`, `Available To`, `City`, `Brands`, `Usage`, `Status`, `Modified By`
69. Muat ulang halaman Service Center
70. Klik header kolom Actions (`⋯`) pada tabel daftar
71. Klik `Setup Columns`
72. Verifikasi tombol pin pada baris `Last Updated` aktif pada daftar kolom dialog `Setup Columns`[^drift-1]
73. Tekan Esc untuk menutup dialog `Setup Columns`[^drift-1]
74. Keluar dari akun `Rina Wijaya`
75. Masuk sebagai `Rina Wijaya`
76. Buka Add-ons > Service Center
77. Klik header kolom Actions (`⋯`) pada tabel daftar
78. Klik `Setup Columns`
79. Verifikasi tombol pin pada baris `Last Updated` aktif pada daftar kolom dialog `Setup Columns`[^drift-1]
80. Tekan Esc untuk menutup dialog `Setup Columns`[^drift-1]
81. Buka browser lain dan masuk sebagai `Rina Wijaya`
82. Buka Add-ons > Service Center
83. Klik header kolom Actions (`⋯`) pada tabel daftar
84. Klik `Setup Columns`
85. Verifikasi tombol pin pada baris `Last Updated` aktif pada daftar kolom dialog `Setup Columns`[^drift-1]
86. Tekan Esc untuk menutup dialog `Setup Columns`[^drift-1]
87. Tutup browser lain
88. Klik header kolom Actions (`⋯`) pada tabel daftar
89. Klik `Setup Columns`
90. Klik `Reset to Default`
91. Klik `Save`
92. Verifikasi urutan header kolom `Name`, `Service Type`, `Specialization`, `Available To`, `City`, `Brands`, `Usage`, `Status`, `Modified By`, `Last Updated`

### Tabel di dalam dialog tidak menyimpan konfigurasi kolom
93. Klik ikon `Changelog` pada toolbar daftar
94. Klik header kolom Actions (`⋯`) pada tabel modal
95. Hilangkan centang `New Value` pada panel Column Visibility
96. Tekan Esc untuk menutup panel Column Visibility
97. Verifikasi urutan header kolom tabel modal `Date`, `Action`, `Service Center Name`, `Field`, `Old Value`, `Modified By`
98. Tutup modal Changelog lewat icon close
99. Klik ikon `Changelog` pada toolbar daftar
100. Verifikasi urutan header kolom tabel modal `Date`, `Action`, `Service Center Name`, `Field`, `Old Value`, `New Value`, `Modified By`
101. Tutup modal Changelog lewat icon close

[^drift-1]: Drift foundation vs kontrak komponen. PRD §4.1a (Setup Column mengikuti foundation, tanpa judul sendiri) dan foundation `prd-conventions.md` §9.3: modal berjudul `"Setup Column"`. Kontrak `DataTable#76`: dialog daftar kolom berjudul `Setup Columns`. Diasersi: kontrak, karena judul dialog adalah teks bawaan komponen DataTable (SB-7).
