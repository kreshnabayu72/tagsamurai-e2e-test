---
id: TC-FA-FATR-UI-076-add-mekanik
title: "Dialog Add override: footer, Clear Field, penutupan, dan reaksi atas respons Submit"
layer: ui-client
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules:
  - "§4.1#r330"
  - "§4.1#r331"
  - "§4.1#r332"
  - "§4.1#r333"
  - "§4.1#r334"
  - "§4.1#r335"
  - "§4.1#r336"
  - "§4.1#r337"
  - "§4.1#r338"
  - "§4.1#r339"
  - "§4.5#b4"
  - "§7#r3"
  - "§7#r4"
  - "§9.2#b103"
  - "§9.2#b104"
  - "§9.2#b105"
  - "§9.2#b178"
  - "§9.2#b179"
  - "§9.4.2#r111"
  - "§9.4.2#r112"
  - "§9.4.2#r113"
  - "§9.4.4#r31"
  - "§9.6#r23"
  - "§9.6#r24"
  - "§9.6#r25"
  - "EB-FB-1@add-override"
  - "EB-FB-2@add-override"
  - "EB-FRM-1@add-override"
  - "EB-FRM-2@add-override"
  - "EB-FRM-3@add-override"
  - "EB-ERR-1@add-override"
smoke: []
dependsOn: []
trace:
  §4.1#r330: 2
  §4.1#r331: 3
  §4.1#r332: [4, 5]
  §4.1#r333: 17
  §4.1#r334: 17
  §4.1#r335: 18
  §4.1#r336: 19
  §4.1#r337: 20
  §4.1#r338: 24
  §4.1#r339: [34, 40]
  §4.5#b4: [27, 30, 40, 44]
  §7#r3: [56, 57]
  §7#r4: 89
  §9.2#b103: 114
  §9.2#b104: 115
  §9.2#b105: 116
  §9.2#b178: [89, 104]
  §9.2#b179: [91, 93]
  §9.4.2#r111: [89, 104]
  §9.4.2#r112: [90, 105]
  §9.4.2#r113: [91, 105]
  §9.4.4#r31: 93
  §9.6#r23: [89, 104]
  §9.6#r24: [90, 105]
  §9.6#r25: [91, 105]
  EB-FB-1@add-override: [56, 67, 68, 89]
  EB-FB-2@add-override: [21, 38]
  EB-FRM-1@add-override: [77, 78, 80]
  EB-FRM-2@add-override: [24, 27, 30, 34, 35, 37, 42, 44, 47]
  EB-FRM-3@add-override: [16, 20]
  EB-ERR-1@add-override: [89, 92, 95, 104, 105]
anchor: []
coverage:
  web: automated
---

# Dialog Add override: footer, Clear Field, penutupan, dan reaksi atas respons Submit

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings, tab Borrow, dengan Dialog Add override dibuka dari tombol `[+ Override]`.
- Komponen: Dialog Add override
- Data:
  - DU-076-1: Group `Proyek Karawang` (hierarki `Region Jawa > Proyek Karawang`).
  - DU-076-2: Group `Proyek Bekasi` (hierarki `Region Jawa > Proyek Bekasi`).
  - DU-076-3: Value `5`.
- Kondisi:
  - K1: Dialog Add override - Borrow dibuka dari Category leaf `Vehicle > Pool car`; tree Group memuat DU-076-1 dan DU-076-2; server menerima permintaan Submit yang valid.
  - K2: sama dengan K1; permintaan Submit pertama gagal karena error server, dan permintaan Submit berikutnya diterima.
  - K3: sama dengan K1; permintaan Submit tidak mendapat respons (timeout).
  - K4: sama dengan K1; Group `Proyek Bekasi` (DU-076-2) sudah dihapus antara pemilihan dan Submit, sehingga server menolak permintaan Submit.
  - K5: sama dengan K1; server belum merespons permintaan Submit sampai pengujian selesai.

## Test Steps

### Footer dialog
1. Tampilkan Dialog Add override dengan kondisi K1
2. Verifikasi footer memuat checkbox `Stay on this form after submitting` yang tidak tercentang
3. Verifikasi footer memuat tombol `[Clear Field]` bergaya teks primary
4. Verifikasi footer memuat tombol `[Submit]`
5. Verifikasi footer tidak memuat tombol `[Cancel]`

### Clear Field mengosongkan isian dan mempertahankan checkbox
6. Tampilkan Dialog Add override dengan kondisi K1
7. Pilih Scope `Group`
8. Klik `[Select Group]`
9. Centang node `Proyek Karawang`
10. Klik `[Select]`
11. Pilih Field `Max duration` pada baris pertama
12. Isi Value `5` pada baris pertama
13. Klik `[+ Add field]`
14. Centang checkbox `Stay on this form after submitting`
15. Klik `[Clear Field]`
16. Verifikasi dialog Add override tetap terbuka tanpa dialog konfirmasi apa pun
17. Verifikasi Scope kembali belum terpilih dengan placeholder `Select scope`
18. Verifikasi tidak ada badge target terpilih
19. Verifikasi hanya ada satu baris Field + Value, dengan Field dan Value kosong
20. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
21. Verifikasi tidak ada toast yang tampil

### Menutup dialog yang bersih
22. Tampilkan Dialog Add override dengan kondisi K1
23. Klik `✕` pada dialog
24. Verifikasi dialog Add override tertutup tanpa dialog Unsaved Changes
25. Tampilkan Dialog Add override dengan kondisi K1
26. Tekan `Esc`
27. Verifikasi dialog Add override tertutup tanpa dialog Unsaved Changes
28. Tampilkan Dialog Add override dengan kondisi K1
29. Klik backdrop di luar dialog
30. Verifikasi dialog Add override tetap terbuka

### Menutup dialog yang sudah terisi
31. Tampilkan Dialog Add override dengan kondisi K1
32. Pilih Scope `Group`
33. Klik `✕` pada dialog
34. Verifikasi dialog `Unsaved Changes` tampil dengan teks `You have unsaved changes. Are you sure you want to leave?`
35. Verifikasi dialog `Unsaved Changes` memuat tombol `[Leave]` dan `[Cancel]`
36. Klik `[Cancel]`
37. Verifikasi dialog `Unsaved Changes` tertutup dan Dialog Add override tetap terbuka dengan Scope `Group`
38. Verifikasi tidak ada toast yang tampil
39. Tekan `Esc`
40. Verifikasi dialog `Unsaved Changes` tampil
41. Tekan `Esc`
42. Verifikasi dialog `Unsaved Changes` tertutup dan Dialog Add override tetap terbuka
43. Klik backdrop di luar dialog
44. Verifikasi Dialog Add override tetap terbuka dengan Scope `Group` dan dialog `Unsaved Changes` tidak tampil
45. Klik `✕` pada dialog
46. Klik `[Leave]`
47. Verifikasi Dialog Add override tertutup

### Submit berhasil
48. Tampilkan Dialog Add override dengan kondisi K1
49. Pilih Scope `Group`
50. Klik `[Select Group]`
51. Centang node `Proyek Karawang`
52. Klik `[Select]`
53. Pilih Field `Max duration` pada baris pertama
54. Isi Value `5` pada baris pertama
55. Klik `[Submit]`
56. Verifikasi toast sukses `Success, override has been added.` tampil
57. Verifikasi Dialog Add override tertutup

### Submit berhasil dengan checkbox Stay on this form
58. Tampilkan Dialog Add override dengan kondisi K1
59. Pilih Scope `Group`
60. Klik `[Select Group]`
61. Centang node `Proyek Karawang`
62. Klik `[Select]`
63. Pilih Field `Max duration` pada baris pertama
64. Isi Value `5` pada baris pertama
65. Centang checkbox `Stay on this form after submitting`
66. Klik `[Submit]`
67. Verifikasi toast sukses `Success, override has been added.` tampil
68. Verifikasi Dialog Add override tetap terbuka dengan Scope belum terpilih dan tanpa badge target

### Keadaan saving: satu permintaan
69. Tampilkan Dialog Add override dengan kondisi K5
70. Pilih Scope `Group`
71. Klik `[Select Group]`
72. Centang node `Proyek Karawang`
73. Klik `[Select]`
74. Pilih Field `Max duration` pada baris pertama
75. Isi Value `5` pada baris pertama
76. Klik `[Submit]`
77. Verifikasi tombol `[Submit]` menampilkan indikator loading dan disabled
78. Verifikasi `[Clear Field]`, `✕`, Scope, Target, kontrol Field + Value, `[+ Add field]`, dan checkbox `Stay on this form after submitting` disabled
79. Klik `[Submit]` yang disabled
80. Verifikasi hanya satu permintaan Submit yang terkirim

### Submit gagal karena error server
81. Tampilkan Dialog Add override dengan kondisi K2
82. Pilih Scope `Group`
83. Klik `[Select Group]`
84. Centang node `Proyek Karawang`
85. Klik `[Select]`
86. Pilih Field `Max duration` pada baris pertama
87. Isi Value `5` pada baris pertama
88. Klik `[Submit]`
89. Verifikasi toast error `Error, failed to add override.` tampil
90. Verifikasi Dialog Add override tetap terbuka
91. Verifikasi Scope `Group`, badge `Proyek Karawang`, Field `Max duration`, dan Value `5` dipertahankan
92. Verifikasi tombol `[Submit]` aktif lagi
93. Verifikasi toast `Success, override has been added.` tidak tampil
94. Klik `[Submit]`
95. Verifikasi toast sukses `Success, override has been added.` tampil satu kali dan dialog tertutup

### Submit tanpa respons
96. Tampilkan Dialog Add override dengan kondisi K3
97. Pilih Scope `Group`
98. Klik `[Select Group]`
99. Centang node `Proyek Karawang`
100. Klik `[Select]`
101. Pilih Field `Max duration` pada baris pertama
102. Isi Value `5` pada baris pertama
103. Klik `[Submit]`
104. Verifikasi toast error `Connection problem. Please try again.` tampil[^drift-1]
105. Verifikasi Dialog Add override tetap terbuka dengan seluruh isian dipertahankan dan tombol `[Submit]` aktif lagi

### Target dihapus antara pemilihan dan Submit
106. Tampilkan Dialog Add override dengan kondisi K4
107. Pilih Scope `Group`
108. Klik `[Select Group]`
109. Centang node `Proyek Bekasi`
110. Klik `[Select]`
111. Pilih Field `Max duration` pada baris pertama
112. Isi Value `5` pada baris pertama
113. Klik `[Submit]`
114. Verifikasi toast error `Error, failed to add override.` tampil
115. Verifikasi Dialog Add override tetap terbuka
116. Verifikasi Scope `Group`, badge `Proyek Bekasi`, Field `Max duration`, dan Value `5` dipertahankan

[^drift-1]: Drift PRD vs foundation. PRD §7 T-04 dan §9.4.2 EC-27a: Add gagal karena 5xx atau timeout menampilkan toast T-04. Foundation `error-handling-convention.md` §2: timeout menampilkan toast `Connection problem. Please try again.`. Diasersi: foundation (SB-4).
