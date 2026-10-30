---
id: TC-GS-UCF-E2E-075-perilaku-identik-lintas-plan
title: "Create, Edit, dan Delete Custom Field Berperilaku Identik pada Plan Starter, Growth, Professional, dan Enterprise Tanpa Gating"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-303
  - TC-GS-UCF-417
  - TC-GS-UCF-418
  - TC-GS-UCF-419
  - TC-GS-UCF-420
coverage:
  web: automated
---

# Create, Edit, dan Delete Custom Field Berperilaku Identik pada Plan Starter, Growth, Professional, dan Enterprise Tanpa Gating

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini mengubah plan Client A (state global tenant) yang memengaruhi spec lain; tidak boleh dijalankan paralel dengan spec lain di Client A.
- Akun aktor: Total Control Client A Sari Dewi (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Pengubah plan Client A (Starter, Growth, Professional, Enterprise): TC, PRD modul, dan LLD tidak menyebut akun atau mekanisme pelaku perubahan plan; spec menyatakannya sebagai kemampuan dan akun yang disediakan tim FE. Plan awal Client A dicatat di hook `before` dan dipulihkan di hook `after` walau spec gagal di tengah.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; langkah yang berpindah plan ditulis eksplisit dan diikuti pembukaan ulang halaman itu.
- Data Pre-setup: tidak ada yang dipakai (seluruh target aksi tulis adalah data milik spec).
- Data Dinamis (nama bersuffix `{runId}-075`; fixture baru `Fixture.customFieldUser.plan075`), semuanya dibuat lewat UI oleh spec: `Plan S {runId}-075` (Text; Starter, TC-GS-UCF-303), `Plan E {runId}-075` (Text; Enterprise, TC-GS-UCF-303), `Plan Starter Probe {runId}-075`, `Plan Growth Probe {runId}-075`, `Plan Professional Probe {runId}-075`, dan `Plan Enterprise Probe {runId}-075` (Text; dibuat, diubah Placeholder-nya menjadi `starter hint`, `growth hint`, `professional hint`, dan `enterprise hint`, lalu dihapus oleh spec).
- Cleanup (hook `after`, tidak berasumsi pembuatan berhasil penuh): hapus lewat API Custom Field bersuffix `{runId}-075` yang masih ada (`Plan S`, `Plan E`, dan probe yang gagal terhapus); pulihkan plan Client A ke plan awal.
- Setup Column dan Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: hover untuk tooltip; pengubah plan Client A (di atas).
- State global: plan Client A (diubah dan dipulihkan seperti di atas), flag Guided Tooltip.

## Test Steps

### Plan Starter (TC-GS-UCF-303 bagian pertama dan TC-GS-UCF-417)

1. Atur Client A ke plan Starter (disediakan tim FE)
2. Buka Global Settings > User > Custom Field

### TC-GS-UCF-303 bagian pertama: Create `Plan S` di plan Starter

3. Klik `[+ Custom Field]`
4. Isi Field Name `Plan S {runId}-075`
5. Pilih Data Type `Text`
6. Klik `[Submit]`
7. Ketik Search `Plan S {runId}-075`, tekan Enter
8. Verifikasi baris `Plan S {runId}-075` tampil pada tabel (Create sukses di plan Starter)
9. Verifikasi tidak ada dialog upgrade plan atau limit berbeda

### TC-GS-UCF-417: Create, Edit, dan Delete berhasil pada plan Starter tanpa gating

10. Klik `[+ Custom Field]`
11. Isi Field Name `Plan Starter Probe {runId}-075`
12. Pilih Data Type `Text`
13. Klik `[Submit]`
14. Verifikasi toast sukses: "Success, custom field has been created."
15. Verifikasi tidak ada dialog upgrade plan
16. Hover `[+ Custom Field]`
17. Verifikasi tidak ada tooltip upgrade plan
18. Ketik Search `Plan Starter Probe {runId}-075`, tekan Enter
19. Klik `⋯` pada baris `Plan Starter Probe {runId}-075`, pilih `Edit`
20. Ubah Placeholder menjadi `starter hint`
21. Klik `[Save]`
22. Verifikasi toast sukses: "Success, custom field has been updated."
23. Verifikasi tidak ada dialog upgrade plan
24. Hover `⋯` pada baris `Plan Starter Probe {runId}-075`
25. Verifikasi tidak ada tooltip upgrade plan
26. Klik `⋯` pada baris `Plan Starter Probe {runId}-075`, pilih `Delete`
27. Verifikasi dialog `Delete Custom Field` tampil
28. Klik `[Delete]` pada dialog
29. Verifikasi toast sukses: "Success, custom field has been deleted."
30. Verifikasi baris `Plan Starter Probe {runId}-075` hilang dari tabel

### Plan Growth (TC-GS-UCF-418)

31. Atur Client A ke plan Growth (disediakan tim FE)
32. Buka Global Settings > User > Custom Field

### TC-GS-UCF-418: Create, Edit, dan Delete berhasil pada plan Growth tanpa gating

33. Klik `[+ Custom Field]`
34. Isi Field Name `Plan Growth Probe {runId}-075`
35. Pilih Data Type `Text`
36. Klik `[Submit]`
37. Verifikasi toast sukses: "Success, custom field has been created."
38. Verifikasi tidak ada dialog upgrade plan
39. Hover `[+ Custom Field]`
40. Verifikasi tidak ada tooltip upgrade plan
41. Ketik Search `Plan Growth Probe {runId}-075`, tekan Enter
42. Klik `⋯` pada baris `Plan Growth Probe {runId}-075`, pilih `Edit`
43. Ubah Placeholder menjadi `growth hint`
44. Klik `[Save]`
45. Verifikasi toast sukses: "Success, custom field has been updated."
46. Verifikasi tidak ada dialog upgrade plan
47. Hover `⋯` pada baris `Plan Growth Probe {runId}-075`
48. Verifikasi tidak ada tooltip upgrade plan
49. Klik `⋯` pada baris `Plan Growth Probe {runId}-075`, pilih `Delete`
50. Verifikasi dialog `Delete Custom Field` tampil
51. Klik `[Delete]` pada dialog
52. Verifikasi toast sukses: "Success, custom field has been deleted."
53. Verifikasi baris `Plan Growth Probe {runId}-075` hilang dari tabel

### Plan Professional (TC-GS-UCF-419)

54. Atur Client A ke plan Professional (disediakan tim FE)
55. Buka Global Settings > User > Custom Field

### TC-GS-UCF-419: Create, Edit, dan Delete berhasil pada plan Professional tanpa gating

56. Klik `[+ Custom Field]`
57. Isi Field Name `Plan Professional Probe {runId}-075`
58. Pilih Data Type `Text`
59. Klik `[Submit]`
60. Verifikasi toast sukses: "Success, custom field has been created."
61. Verifikasi tidak ada dialog upgrade plan
62. Hover `[+ Custom Field]`
63. Verifikasi tidak ada tooltip upgrade plan
64. Ketik Search `Plan Professional Probe {runId}-075`, tekan Enter
65. Klik `⋯` pada baris `Plan Professional Probe {runId}-075`, pilih `Edit`
66. Ubah Placeholder menjadi `professional hint`
67. Klik `[Save]`
68. Verifikasi toast sukses: "Success, custom field has been updated."
69. Verifikasi tidak ada dialog upgrade plan
70. Hover `⋯` pada baris `Plan Professional Probe {runId}-075`
71. Verifikasi tidak ada tooltip upgrade plan
72. Klik `⋯` pada baris `Plan Professional Probe {runId}-075`, pilih `Delete`
73. Verifikasi dialog `Delete Custom Field` tampil
74. Klik `[Delete]` pada dialog
75. Verifikasi toast sukses: "Success, custom field has been deleted."
76. Verifikasi baris `Plan Professional Probe {runId}-075` hilang dari tabel

### Plan Enterprise (TC-GS-UCF-303 bagian kedua dan TC-GS-UCF-420)

77. Atur Client A ke plan Enterprise (disediakan tim FE)
78. Buka Global Settings > User > Custom Field

### TC-GS-UCF-303 bagian kedua: Create `Plan E` di plan Enterprise

79. Klik `[+ Custom Field]`
80. Isi Field Name `Plan E {runId}-075`
81. Pilih Data Type `Text`
82. Klik `[Submit]`
83. Ketik Search `Plan E {runId}-075`, tekan Enter
84. Verifikasi baris `Plan E {runId}-075` tampil pada tabel (Create sukses di plan Enterprise)
85. Verifikasi tidak ada dialog upgrade plan atau limit berbeda

### TC-GS-UCF-420: Create, Edit, dan Delete berhasil pada plan Enterprise tanpa gating

86. Klik `[+ Custom Field]`
87. Isi Field Name `Plan Enterprise Probe {runId}-075`
88. Pilih Data Type `Text`
89. Klik `[Submit]`
90. Verifikasi toast sukses: "Success, custom field has been created."
91. Verifikasi tidak ada dialog upgrade plan
92. Hover `[+ Custom Field]`
93. Verifikasi tidak ada tooltip upgrade plan
94. Ketik Search `Plan Enterprise Probe {runId}-075`, tekan Enter
95. Klik `⋯` pada baris `Plan Enterprise Probe {runId}-075`, pilih `Edit`
96. Ubah Placeholder menjadi `enterprise hint`
97. Klik `[Save]`
98. Verifikasi toast sukses: "Success, custom field has been updated."
99. Verifikasi tidak ada dialog upgrade plan
100. Hover `⋯` pada baris `Plan Enterprise Probe {runId}-075`
101. Verifikasi tidak ada tooltip upgrade plan
102. Klik `⋯` pada baris `Plan Enterprise Probe {runId}-075`, pilih `Delete`
103. Verifikasi dialog `Delete Custom Field` tampil
104. Klik `[Delete]` pada dialog
105. Verifikasi toast sukses: "Success, custom field has been deleted."
106. Verifikasi baris `Plan Enterprise Probe {runId}-075` hilang dari tabel
107. Atur Client A kembali ke plan awal (pemulihan state, disediakan tim FE)

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah; subjudul tanpa id TC (`Plan Starter`, `Plan Growth`, `Plan Professional`, `Plan Enterprise`) memuat langkah penghubung yang mengatur plan.
- Urutan TC dalam spec: 303 (bagian pertama), 417, 418, 419, 303 (bagian kedua), 420. TC-GS-UCF-303 mengharuskan Create di plan Starter lalu di plan Enterprise; kedua Create disisipkan pada blok plan masing-masing supaya plan hanya berpindah empat kali. Aksi yang menghapus data (Delete probe) berada di akhir tiap blok TC dan `Plan S` dan `Plan E` dihapus oleh hook `after`.
- Langkah penghubung (aksi tanpa `Verifikasi`): mengatur plan Client A, membuka ulang Global Settings > User > Custom Field, pengisian Search tabel, hover pada `[+ Custom Field]` dan `⋯` (pemicu asersi tooltip), dan pemulihan plan di akhir. Absence dialog dan tooltip upgrade plan memakai toast sukses (atau baris tampil pada TC-GS-UCF-303) sebagai anchor positif yang terhubung ke pemicu (bagian 8b butir 2).
- Spec melewati sekitar 35 langkah (107 langkah). Seluruhnya satu kelas h (perilaku modul per plan tenant) dengan empat blok plan yang identik; satu blok plan berdiri sendiri karena mengatur plan, membuat data, dan menghapusnya sendiri. Langkah yang diulang per plan berparameter pada nama probe, nilai Placeholder, dan plan, ditulis eksplisit (bukan iterasi) karena Expected tiap plan punya `Verifikasi` sendiri.
- Temuan untuk QA:
  - Pelaku dan mekanisme perubahan plan Client A (Starter, Growth, Professional, Enterprise) tidak ditulis di TC; spec menyatakannya sebagai disediakan tim FE (S-13). TC-GS-UCF-303 juga tidak menyebut apakah halaman dimuat ulang sesudah perubahan plan; spec menambahkan pembukaan ulang Global Settings > User > Custom Field sebagai langkah penghubung.
  - TC-GS-UCF-303 hanya menyebut "keduanya sukses tanpa upsell atau limit berbeda" tanpa menyebut toast; spec mengasersi baris tampil pada tabel dan tidak ada dialog upgrade plan atau limit. Toast sukses diasersi pada TC-GS-UCF-417 sampai 420.
  - TC-GS-UCF-417 sampai 420 menyebut "tanpa tooltip upgrade plan" tanpa elemen yang di-hover; spec menambahkan hover pada `[+ Custom Field]` dan pada `⋯` baris sebagai pemicu asersi, tercatat sebagai langkah penghubung.
  - TC-GS-UCF-303 tumpang tindih dengan TC-GS-UCF-417 dan 420 (Create pada plan Starter dan Enterprise); keduanya tetap dipertahankan sesuai TC.
  - Tidak ada Post Condition pada kelima TC.
