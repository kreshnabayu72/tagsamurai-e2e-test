---
id: TC-FA-FAREG-UI-005-draft-filter-panel
title: "Sub tab Draft: mekanik Filter Panel dan field filter"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1#r22", "§4.1#r23", "§4.1#r24", "§4.1#r25", "§4.1#r26", "§4.1#r27", "§9.5#r8", "EB-FLT-2@tabel-draft", "EB-FLT-6@tabel-draft"]
smoke: []
dependsOn: []
trace:
  "§4.1#r22": [3, 4, 5]
  "§4.1#r23": 15
  "§4.1#r24": [6, 7, 8]
  "§4.1#r25": 16
  "§4.1#r26": [9, 10, 11]
  "§4.1#r27": [12, 13, 14]
  "§9.5#r8": 19
  EB-FLT-2@tabel-draft: [23, 25, 27, 28, 32, 38, 44, 46, 47, 51, 53, 54, 59, 60, 62, 66, 71, 73, 78]
  EB-FLT-6@tabel-draft: [84, 88, 89, 90]
anchor: [18, 77, 83]
coverage:
  web: automated
---

# Sub tab Draft: mekanik Filter Panel dan field filter

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft.
- Komponen: Sub tab `Draft` (TBL-REG-01)
- Data:
  - DU-005-1: batch Draft Group `Gudang 1`, Origin `—`, Total Asset `12`, Progress `0%`, Requested By `Budi Santoso`, Last Updated `2026-11-09T08:15:00Z`.
  - DU-005-2: batch Draft Group `Gudang 2`, Origin `—`, Total Asset `5`, Progress `60%`, Requested By `Siti Nurbaya`, Last Updated `2026-11-08T16:40:00Z`.
  - DU-005-3: batch Draft Group `Kantor Pusat`, Origin `—`, Total Asset `30`, Progress `100%`, Requested By `Alexander Graham Bell`, Last Updated `2026-11-07T09:05:00Z`.
  - DU-005-4: batch Draft Group `Gudang 3`, Origin `—`, Total Asset `8`, Progress `25%`, Requested By `Buzzlightyear Sumardi`, Last Updated `2026-11-06T13:10:00Z`.
  - DU-005-5: batch Draft Group `Gudang 4`, Origin `—`, Total Asset `6`, Progress `50%`, Requested By `Dewi Anggraini`, Last Updated `2026-11-05T10:00:00Z`.
  - DU-005-6: batch Draft Group `Gudang 5`, Origin `—`, Total Asset `4`, Progress `75%`, Requested By `Hadi Kusuma`, Last Updated `2026-11-04T14:45:00Z`.
  - DU-005-7: kata kunci pencarian opsi dropdown `Siti` yang cocok dengan satu pengaju.
  - DU-005-8: kata kunci pencarian opsi dropdown `Zulkifli` yang tidak cocok dengan pengaju mana pun.
- Kondisi:
  - K1: daftar berisi DU-005-1 sampai DU-005-6; opsi filter Requested By berisi keenam pengaju pada daftar; tidak ada filter ter-Apply.
  - K2: sama dengan K1; filter Requested By `Siti Nurbaya` hanya menghasilkan DU-005-2; tanpa filter menghasilkan DU-005-1 sampai DU-005-6.
  - K3: daftar Draft kosong, belum ada batch.

## Test Steps

### Field filter tabel Draft: label, tipe, dan placeholder
1. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
2. Klik ikon Filter pada toolbar
3. Verifikasi field berlabel `Group` tampil
4. Verifikasi field `Group` berupa `Tree picker`
5. Verifikasi placeholder field `Group` adalah `All groups`
6. Verifikasi field berlabel `Total Asset` tampil
7. Verifikasi field `Total Asset` berupa rentang `Min/Max`
8. Verifikasi placeholder kedua input field `Total Asset` adalah `Min` dan `Max`
9. Verifikasi field berlabel `Requested By` tampil
10. Verifikasi field `Requested By` berupa `Multi-select searchable`
11. Verifikasi placeholder field `Requested By` adalah `All users`
12. Verifikasi field berlabel `Last Updated` tampil
13. Verifikasi field `Last Updated` berupa `Date range picker`
14. Verifikasi placeholder field `Last Updated` adalah `Select date`
15. Verifikasi field filter `Origin` tidak tampil
16. Verifikasi field filter `Progress` tidak tampil

### Tanpa filter aktif saat pertama dibuka
17. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
18. Verifikasi ikon Filter tampil pada toolbar
19. Verifikasi badge titik pada ikon Filter tidak tampil

### Menutup panel tanpa Apply membuang pilihan
20. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
21. Klik ikon Filter pada toolbar
22. Pilih opsi `Siti Nurbaya` pada field `Requested By`
23. Verifikasi chip `Siti Nurbaya` tampil pada field `Requested By`
24. Klik ikon Filter untuk menutup panel tanpa `[Apply]`
25. Verifikasi baris `Gudang 1` tampil setelah panel ditutup tanpa Apply
26. Klik ikon Filter untuk membuka panel
27. Verifikasi placeholder field `Requested By` adalah `All users`
28. Verifikasi chip `Siti Nurbaya` tidak tampil pada field `Requested By`

### Chip tampil per opsi terpilih dan overflow
29. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
30. Klik ikon Filter pada toolbar
31. Pilih opsi `Budi Santoso` pada field `Requested By`
32. Verifikasi chip `Budi Santoso` tampil pada field `Requested By`
33. Pilih opsi `Siti Nurbaya` pada field `Requested By`
34. Pilih opsi `Alexander Graham Bell` pada field `Requested By`
35. Pilih opsi `Buzzlightyear Sumardi` pada field `Requested By`
36. Pilih opsi `Dewi Anggraini` pada field `Requested By`
37. Pilih opsi `Hadi Kusuma` pada field `Requested By`
38. Verifikasi ringkasan overflow `+N more` tampil pada field `Requested By`

### Hapus chip lalu Apply menyaring dengan opsi tersisa
39. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K2
40. Klik ikon Filter pada toolbar
41. Pilih opsi `Budi Santoso` pada field `Requested By`
42. Pilih opsi `Siti Nurbaya` pada field `Requested By`
43. Klik `✕` pada chip `Budi Santoso`
44. Verifikasi opsi `Budi Santoso` tidak tercentang pada dropdown field `Requested By`
45. Klik `[Apply]`
46. Verifikasi baris `Gudang 2` tampil
47. Verifikasi baris `Gudang 1` tidak tampil setelah Apply dengan satu opsi tersisa

### Hilangkan centang opsi menghapus chip
48. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
49. Klik ikon Filter pada toolbar
50. Pilih opsi `Siti Nurbaya` pada field `Requested By`
51. Verifikasi chip `Siti Nurbaya` tampil pada field `Requested By`
52. Hilangkan centang opsi `Siti Nurbaya` pada field `Requested By`
53. Verifikasi placeholder field `Requested By` adalah `All users`
54. Verifikasi chip `Siti Nurbaya` tidak tampil pada field `Requested By`

### Search di dalam dropdown
55. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
56. Klik ikon Filter pada toolbar
57. Buka dropdown field `Requested By`
58. Ketik `Siti` pada kotak cari di dalam dropdown
59. Verifikasi opsi `Siti Nurbaya` tampil
60. Verifikasi opsi `Budi Santoso` tidak tampil
61. Ganti isi kotak cari di dalam dropdown dengan `Zulkifli`
62. Verifikasi teks `No results found` tampil di dalam dropdown

### Sumber opsi kosong
63. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K3
64. Klik ikon Filter pada toolbar
65. Buka dropdown field `Requested By`
66. Verifikasi teks `No options available` tampil di dalam dropdown

### Indikator filter aktif pada ikon Filter
67. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K2
68. Klik ikon Filter pada toolbar
69. Pilih opsi `Siti Nurbaya` pada field `Requested By`
70. Klik `[Apply]`
71. Verifikasi badge titik pada ikon Filter tampil
72. Klik ikon Filter untuk menutup panel
73. Verifikasi badge titik pada ikon Filter tetap tampil
74. Klik ikon Filter untuk membuka panel
75. Klik `[Clear Field]`
76. Klik `[Apply]`
77. Verifikasi ikon Filter tampil pada toolbar
78. Verifikasi badge titik pada ikon Filter tidak tampil

### Menyembunyikan kolom tidak menghapus field filter dan filter ter-Apply
79. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K2
80. Klik ikon Filter pada toolbar
81. Pilih opsi `Siti Nurbaya` pada field `Requested By`
82. Klik `[Apply]`
83. Verifikasi baris `Gudang 2` tampil
84. Verifikasi baris `Gudang 1` tidak tampil setelah filter Requested By ter-Apply
85. Klik header kolom Actions `⋯`
86. Hilangkan centang kolom `Requested By` pada panel Column Visibility
87. Klik ikon Filter pada toolbar
88. Verifikasi field berlabel `Requested By` tampil
89. Verifikasi chip `Siti Nurbaya` tampil pada field `Requested By`
90. Verifikasi baris `Gudang 1` tetap tidak tampil setelah kolom Requested By disembunyikan
