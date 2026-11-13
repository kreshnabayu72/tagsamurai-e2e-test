---
id: TC-FA-FAREG-UI-006-draft-setup-column
title: "Sub tab Draft: mekanik Setup Column"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1#p4", "EB-KOL-1@tabel-draft"]
smoke: []
dependsOn: []
trace:
  "§4.1#p4": [4, 9]
  EB-KOL-1@tabel-draft: [4, 5, 6, 7, 8, 9, 10, 11, 17, 19, 20, 25, 30, 32, 39, 40, 42, 44, 49, 51, 57, 59, 65, 67, 76, 78, 80, 85, 87]
anchor: [16, 56, 64]
coverage:
  web: automated
---

# Sub tab Draft: mekanik Setup Column

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft.
- Komponen: Sub tab `Draft` (TBL-REG-01)
- Data:
  - DU-006-1: batch Draft Group `Gudang 1`, Origin `—`, Total Asset `12`, Progress `0%`, Requested By `Rina Wulandari`, Last Updated `2026-11-09T08:15:00Z`.
  - DU-006-2: batch Draft Group `Gudang 2`, Origin `REG-20261105-00007`, Total Asset `5`, Progress `60%`, Requested By `Siti Nurbaya`, Last Updated `2026-11-08T16:40:00Z`.
- Kondisi:
  - K1: daftar berisi DU-006-1 dan DU-006-2; belum ada konfigurasi kolom tersimpan, sehingga keenam kolom tampil menurut default.
  - K2: sama dengan K1, dengan konfigurasi kolom tersimpan yang menyembunyikan kolom `Origin`.

## Test Steps

### Setup Column dibuka dari panel Column Visibility dan anatominya
1. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
2. Klik header kolom Actions `⋯`
3. Klik `Setup Column...`
4. Verifikasi modal `Setup Column` tampil
5. Verifikasi deskripsi modal `Drag and drop to rearrange the order and click the pin to freeze up to 3 columns.`
6. Verifikasi ikon `✕` tampil pada modal
7. Verifikasi footer modal memuat `[Reset to Default]` dan `[Save]`
8. Verifikasi footer modal tidak memuat tombol `[Cancel]`
9. Verifikasi daftar kolom pada modal memuat `Group`, `Origin`, `Total Asset`, `Progress`, `Requested By`, dan `Last Updated`
10. Verifikasi keenam kolom pada modal tercentang
11. Verifikasi daftar kolom pada modal tidak memuat baris `Checkbox` dan `Actions`

### Hilangkan centang kolom dipratinjau lalu tersimpan dengan Save
12. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
13. Klik header kolom Actions `⋯`
14. Klik `Setup Column...`
15. Hilangkan centang kolom `Origin` pada modal Setup Column
16. Verifikasi kolom `Group` tampil pada Live Preview di modal Setup Column[^drift-1]
17. Verifikasi kolom `Origin` tidak tampil pada Live Preview di modal Setup Column[^drift-1]
18. Klik `[Save]`
19. Verifikasi modal `Setup Column` tertutup
20. Verifikasi kolom `Origin` tidak tampil pada tabel

### Centang kembali kolom yang tersembunyi
21. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K2
22. Klik header kolom Actions `⋯`
23. Klik `Setup Column...`
24. Centang kolom `Origin` pada modal Setup Column
25. Verifikasi kolom `Origin` tampil pada Live Preview di modal Setup Column[^drift-1]

### Urutan kolom dipratinjau lalu tersimpan
26. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
27. Klik header kolom Actions `⋯`
28. Klik `Setup Column...`
29. Seret kolom `Last Updated` ke atas kolom `Group` pada modal Setup Column
30. Verifikasi kolom `Last Updated` berada sebelum kolom `Group` pada Live Preview di modal Setup Column[^drift-1]
31. Klik `[Save]`
32. Verifikasi kolom `Last Updated` berada sebelum kolom `Group` pada tabel

### Pin kolom dengan batas tiga kolom
33. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
34. Klik header kolom Actions `⋯`
35. Klik `Setup Column...`
36. Klik ikon pin kolom `Group`
37. Klik ikon pin kolom `Origin`
38. Klik ikon pin kolom `Total Asset`
39. Verifikasi ikon pin kolom `Group`, `Origin`, dan `Total Asset` tertanda ter-pin
40. Verifikasi ikon pin kolom `Progress` disabled
41. Arahkan kursor ke ikon pin kolom `Progress`
42. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
43. Klik ikon pin kolom `Origin`
44. Verifikasi ikon pin kolom `Progress` enabled

### Reset to Default mengembalikan konfigurasi default
45. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K2
46. Klik header kolom Actions `⋯`
47. Klik `Setup Column...`
48. Klik `[Reset to Default]`
49. Verifikasi kolom `Origin` tampil pada Live Preview di modal Setup Column[^drift-1]
50. Klik `[Save]`
51. Verifikasi kolom `Origin` tampil pada tabel

### Menutup dengan ikon close membuang perubahan
52. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
53. Klik header kolom Actions `⋯`
54. Klik `Setup Column...`
55. Hilangkan centang kolom `Origin` pada modal Setup Column
56. Verifikasi kolom `Group` tampil pada Live Preview di modal Setup Column[^drift-1]
57. Verifikasi kolom `Origin` tidak tampil pada Live Preview di modal Setup Column[^drift-1]
58. Klik `✕` pada modal Setup Column
59. Verifikasi kolom `Origin` tampil pada tabel

### Menutup dengan Esc membuang perubahan
60. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
61. Klik header kolom Actions `⋯`
62. Klik `Setup Column...`
63. Hilangkan centang kolom `Origin` pada modal Setup Column
64. Verifikasi kolom `Group` tampil pada Live Preview di modal Setup Column[^drift-1]
65. Verifikasi kolom `Origin` tidak tampil pada Live Preview di modal Setup Column[^drift-1]
66. Tekan `Esc`
67. Verifikasi kolom `Origin` tampil pada tabel

### Kolom terakhir tidak bisa disembunyikan
68. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
69. Klik header kolom Actions `⋯`
70. Klik `Setup Column...`
71. Hilangkan centang kolom `Origin` pada modal Setup Column
72. Hilangkan centang kolom `Total Asset` pada modal Setup Column
73. Hilangkan centang kolom `Progress` pada modal Setup Column
74. Hilangkan centang kolom `Requested By` pada modal Setup Column
75. Hilangkan centang kolom `Last Updated` pada modal Setup Column
76. Verifikasi checkbox kolom `Group` disabled
77. Arahkan kursor ke checkbox kolom `Group`
78. Verifikasi tooltip `At least one column must remain visible.`
79. Centang kolom `Origin` pada modal Setup Column
80. Verifikasi checkbox kolom `Group` enabled

### Tabel di balik modal tidak berubah sebelum Save
81. Tampilkan Sub tab `Draft` (TBL-REG-01) dengan kondisi K1
82. Klik header kolom Actions `⋯`
83. Klik `Setup Column...`
84. Hilangkan centang kolom `Origin` pada modal Setup Column
85. Verifikasi kolom `Origin` tetap tampil pada tabel di balik modal[^drift-1]
86. Seret kolom `Last Updated` ke atas kolom `Group` pada modal Setup Column
87. Verifikasi kolom `Group` tetap berada sebelum kolom `Last Updated` pada tabel di balik modal[^drift-1]

[^drift-1]: Drift foundation vs override. PRD §4.1 (Deviasi) menunjuk `prd-conventions.md` §9.3 tanpa aturan preview sendiri; foundation `prd-conventions.md` §9.3: perubahan di modal Setup Column di-preview langsung di tabel di balik modal. Override O-20: dialog punya Live Preview sendiri, dan tabel berubah hanya sesudah `[Save]`; langkah yang mengharapkan tabel di balik modal berubah selama dialog terbuka diabaikan. Diasersi: O-20, karena override menang atas foundation (SB-6).
