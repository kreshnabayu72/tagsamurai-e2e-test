---
id: TC-FA-ASSIGN-UI-117-tabel-transactions-filter-panel
title: "Tabel Transactions: mekanik Filter Panel"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-FLT-2@tabel-transactions", "EB-FLT-6@tabel-transactions"]
smoke: []
dependsOn: []
trace:
  "EB-FLT-2@tabel-transactions": [3, 7, 9, 15, 17, 21, 22, 27, 28, 30, 32, 33, 37, 39, 40, 45, 46, 48, 52, 56, 60, 61, 63, 65, 69, 70]
  "EB-FLT-6@tabel-transactions": [75, 78, 79, 80, 82, 83]
coverage:
  web: automated
---

# Tabel Transactions: mekanik Filter Panel

## Prerequisites
- Aktor: Aktor Assignment.
- Layar awal: Transactions > Assignment, tab Transactions.
- Komponen: Tabel Transactions
- Data:
  - DU-117-1: Assignment `ASG-2026-0071`, Status `Waiting for Handover`, Group `Head Office`, Assignee `Budi S`, Assignee Type `Employee`, Total Asset `3`, Requested By `Rina W`, Request Date `09 Nov 2026, 19:00`, Last Updated `09 Nov 2026, 20:40`.
  - DU-117-2: Assignment `ASG-2026-0070`, Status `Waiting for Approval`, Group `Head Office`, Assignee `Sari D`, Assignee Type `Employee`, Total Asset `2`, Requested By `Agus P`, Request Date `09 Nov 2026, 14:00`, Last Updated `09 Nov 2026, 14:00`.
  - DU-117-3: Assignment `ASG-2026-0069`, Status `Assigned`, Group `Branch Surabaya`, Assignee `Finance`, Assignee Type `Division`, Total Asset `4`, Requested By `Agus P`, Request Date `05 Nov 2026, 11:00`, Last Updated `06 Nov 2026, 09:20`.
  - DU-117-4: 8 Assignment dengan pola `ASG-2026-00{n}`, Status `Assigned`, Group `Head Office`, Assignee `Petugas Lapangan {n}`, Assignee Type `Employee`, Total Asset `1`, Requested By `Rina W`, Request Date `04 Nov 2026, 09:00`, Last Updated `04 Nov 2026, 09:30`.
  - DU-117-5: kata kunci cari di dalam dropdown yang cocok dengan satu opsi `Finance`.
  - DU-117-6: kata kunci cari di dalam dropdown yang tidak cocok dengan opsi mana pun `Kalimantan`.
- Kondisi:
  - K1: daftar berisi DU-117-1 sampai DU-117-3.
  - K2: daftar berisi DU-117-4.
  - K3: daftar kosong, tanpa baris.

## Test Steps

### Menutup panel dengan klik ulang ikon Filter membuang draft
1. Tampilkan Tabel Transactions dengan kondisi K1
2. Klik ikon Filter
3. Verifikasi Filter Panel tampil
4. Pilih opsi `Assigned` pada field `Status`
5. Klik field `Status` untuk menutup daftar opsi
6. Klik ikon Filter
7. Verifikasi tabel masih memuat baris `ASG-2026-0071` dan `ASG-2026-0070`
8. Klik ikon Filter
9. Verifikasi field `Status` menampilkan placeholder `All statuses`

### Menutup panel dengan klik di luar panel membuang draft
10. Tampilkan Tabel Transactions dengan kondisi K1
11. Klik ikon Filter
12. Pilih opsi `Assigned` pada field `Status`
13. Klik field `Status` untuk menutup daftar opsi
14. Klik di luar Filter Panel
15. Verifikasi tabel tetap memuat baris `ASG-2026-0071` dan `ASG-2026-0070`
16. Klik ikon Filter
17. Verifikasi field `Status` kembali menampilkan placeholder `All statuses`

### Chip tampil untuk setiap opsi terpilih
18. Tampilkan Tabel Transactions dengan kondisi K1
19. Klik ikon Filter
20. Pilih opsi `Waiting for Handover` dan `Waiting for Approval` pada field `Status`
21. Verifikasi chip `Waiting for Handover` tampil pada field `Status`
22. Verifikasi chip `Waiting for Approval` tampil pada field `Status`

### Hapus chip lalu Apply menyaring dengan opsi tersisa
23. Tampilkan Tabel Transactions dengan kondisi K1
24. Klik ikon Filter
25. Pilih opsi `Waiting for Handover` dan `Waiting for Approval` pada field `Status`
26. Klik `(✕)` pada chip `Waiting for Approval`
27. Verifikasi chip `Waiting for Handover` tetap tampil pada field `Status`
28. Verifikasi chip `Waiting for Approval` tidak tampil pada field `Status`
29. Klik field `Status` untuk membuka daftar opsi
30. Verifikasi opsi `Waiting for Approval` tidak tercentang
31. Klik `[Apply]`
32. Verifikasi tabel memuat baris `ASG-2026-0071`
33. Verifikasi tabel tidak memuat baris `ASG-2026-0070`

### Uncheck opsi menghapus chip-nya
34. Tampilkan Tabel Transactions dengan kondisi K1
35. Klik ikon Filter
36. Pilih opsi `Assigned` pada field `Status`
37. Verifikasi chip `Assigned` tampil pada field `Status`
38. Klik opsi `Assigned` pada daftar opsi `Status` untuk menghapus centangnya
39. Verifikasi field `Status` menampilkan placeholder `All statuses`
40. Verifikasi chip `Assigned` tidak tampil pada field `Status`

### Search di dalam dropdown menyaring opsi
41. Tampilkan Tabel Transactions dengan kondisi K1
42. Klik ikon Filter
43. Klik field `Assignee` untuk membuka daftar opsi
44. Ketik `Finance` pada kotak cari di dalam daftar opsi
45. Verifikasi opsi `Finance` tampil
46. Verifikasi opsi `Budi S` tidak tampil
47. Ganti isi kotak cari di dalam daftar opsi dengan `Kalimantan`
48. Verifikasi daftar opsi menampilkan `No results found`

### Sumber opsi kosong
49. Tampilkan Tabel Transactions dengan kondisi K3
50. Klik ikon Filter
51. Klik field `Status` untuk membuka daftar opsi
52. Verifikasi daftar opsi menampilkan `No options available`

### Chip berlebih diringkas menjadi satu chip jumlah
53. Tampilkan Tabel Transactions dengan kondisi K2
54. Klik ikon Filter
55. Pilih opsi `Petugas Lapangan 1` sampai `Petugas Lapangan 8` pada field `Assignee`
56. Verifikasi ringkasan `+N more` tampil pada field `Assignee`

### Indikator titik pada ikon Filter mengikuti filter yang ter-Apply
57. Tampilkan Tabel Transactions dengan kondisi K1
58. Klik ikon Filter
59. Pilih opsi `Assigned` pada field `Status`
60. Verifikasi tabel masih memuat baris `ASG-2026-0071`
61. Verifikasi indikator titik pada ikon Filter belum tampil
62. Klik `[Apply]`
63. Verifikasi indikator titik tampil pada ikon Filter
64. Klik ikon Filter
65. Verifikasi indikator titik tetap tampil pada ikon Filter
66. Klik ikon Filter
67. Klik `[Clear Field]`
68. Klik `[Apply]`
69. Verifikasi tabel memuat baris `ASG-2026-0071`
70. Verifikasi indikator titik pada ikon Filter hilang

### Menyembunyikan kolom tidak menghapus field filter dan tidak membatalkan filter yang ter-Apply
71. Tampilkan Tabel Transactions dengan kondisi K1
72. Klik ikon Filter
73. Pilih opsi `Assigned` pada field `Status`
74. Klik `[Apply]`
75. Verifikasi tabel memuat baris `ASG-2026-0069`
76. Klik header kolom aksi baris
77. Hilangkan centang kolom `Status` pada panel Column Visibility
78. Verifikasi kolom `Transaction ID` tetap tampil pada tabel
79. Verifikasi kolom `Status` tidak tampil pada tabel
80. Verifikasi tabel tidak memuat baris `ASG-2026-0071`
81. Klik ikon Filter
82. Verifikasi field `Status` tetap tampil pada Filter Panel
83. Verifikasi chip `Assigned` tetap tampil pada field `Status`
