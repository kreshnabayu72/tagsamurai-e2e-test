---
id: TC-AC-PP-E2E-020-editor-insert-link
title: "Editor Insert Link: Screening Popover, Validasi URL, Penyisipan, Cancel, Esc, dan Tautan Existing"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-54
  - TC-AC-PP-55
  - TC-AC-PP-56
  - TC-AC-PP-57
  - TC-AC-PP-58
  - TC-AC-PP-209
coverage:
  web: automated
---

# Editor Insert Link: Screening Popover, Validasi URL, Penyisipan, Cancel, Esc, dan Tautan Existing

## Prerequisites

- Mode: mock. Seluruh API dijawab dari mock tanpa mengubah backend: endpoint daftar riwayat versi dijawab Riwayat A (Version 3 Active, Version 2, Version 1) dan endpoint konten versi dijawab konten Version 3 (H1 `Privacy Policy`, paragraf `This Privacy Policy describes how we collect, use, and protect your information.`, H3 `1. Information We Collect`). Sesi dan payload izin akun Total Control (capability "Manage privacy policy" Read dan Update) juga dijawab dari mock agar row action `Edit` dan footer `[Publish New Version]` tampil. Tidak ada request Publish yang dikirim spec ini (tidak ada langkah Publish).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login nyata dengan akun ini di hook `before` hanya untuk run non-mock; pada run mock sesi dan payload izin disediakan harness. Hook `before` lalu membuka Settings > Privacy Policy; hook `after` mengembalikan sesi ke akun default suite yang sama. Nama env `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Dataset: Riwayat A (lewat mock, tidak ada seeding backend sehingga tidak ada pemulihan dataset).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Kemampuan teknis: pembacaan DOM editor (jumlah, href, dan teks tampil elemen tautan di konten editor); tombol keyboard Esc dan klik di area editor.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-PP-54: Screening popover Insert Link dari tombol Link di toolbar editor

1. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
2. Tunggu konten editor termuat
3. Klik tombol Link pada toolbar
4. Verifikasi popover kecil tampil menempel pada tombol Link
5. Verifikasi popover berada di dalam Modal state Edit
6. Verifikasi popover berisi 1 field URL
7. Verifikasi popover berisi tombol `[Insert]`
8. Verifikasi popover berisi tombol `[Cancel]`
9. Verifikasi field URL berlabel "URL"
10. Verifikasi field URL memiliki placeholder "https://"

### TC-AC-PP-56: Insert Link dengan URL tidak valid menampilkan error inline V-04 dan tautan tidak disisipkan

11. Isi field URL dengan `javascript:alert(1)`
12. Klik `[Insert]`
13. Verifikasi error inline "Enter a valid URL starting with http://, https://, or mailto:" tampil di bawah field URL
14. Verifikasi popover tetap terbuka
15. Verifikasi tidak ada tautan yang disisipkan ke konten editor
16. Kosongkan field URL
17. Isi field URL dengan `ftp://example.com`
18. Klik `[Insert]`
19. Verifikasi error inline "Enter a valid URL starting with http://, https://, or mailto:" tampil di bawah field URL
20. Verifikasi popover tetap terbuka
21. Verifikasi tidak ada tautan yang disisipkan ke konten editor
22. Kosongkan field URL
23. Isi field URL dengan `http://`
24. Klik `[Insert]`
25. Verifikasi error inline "Enter a valid URL starting with http://, https://, or mailto:" tampil di bawah field URL
26. Verifikasi popover tetap terbuka
27. Verifikasi tidak ada tautan yang disisipkan ke konten editor
28. Kosongkan field URL
29. Isi field URL dengan `mailto:`
30. Klik `[Insert]`
31. Verifikasi error inline "Enter a valid URL starting with http://, https://, or mailto:" tampil di bawah field URL
32. Verifikasi popover tetap terbuka
33. Verifikasi tidak ada tautan yang disisipkan ke konten editor
34. Verifikasi tidak ada dialog yang tampil pada keempat URL
35. Verifikasi tidak ada toast yang tampil pada keempat URL
36. Klik `[Cancel]` pada popover untuk menutupnya

### TC-AC-PP-55: Insert Link dengan URL bersekema http, https, dan mailto menyisipkan tautan

37. Klik di akhir konten editor tanpa menyeleksi teks
38. Klik tombol Link pada toolbar
39. Isi field URL dengan `http://example.com`
40. Klik `[Insert]`
41. Verifikasi popover tertutup
42. Verifikasi tidak ada error inline di popover
43. Verifikasi tautan dengan href `http://example.com` ada di konten editor
44. Verifikasi teks tampil tautan adalah `http://example.com` (URL itu sendiri)
45. Klik tombol Link pada toolbar
46. Isi field URL dengan `https://example.com/privacy`
47. Klik `[Insert]`
48. Verifikasi popover tertutup
49. Verifikasi tidak ada error inline di popover
50. Verifikasi tautan dengan href `https://example.com/privacy` ada di konten editor
51. Verifikasi teks tampil tautan adalah `https://example.com/privacy` (URL itu sendiri)
52. Klik tombol Link pada toolbar
53. Isi field URL dengan `mailto:privacy@example.com`
54. Klik `[Insert]`
55. Verifikasi popover tertutup
56. Verifikasi tidak ada error inline di popover
57. Verifikasi tautan dengan href `mailto:privacy@example.com` ada di konten editor
58. Verifikasi teks tampil tautan adalah `mailto:privacy@example.com` (URL itu sendiri)
59. Ketik " privacy terms" di akhir konten editor
60. Seleksi teks `privacy terms`
61. Klik tombol Link pada toolbar
62. Isi field URL dengan `https://example.com/terms`
63. Klik `[Insert]`
64. Verifikasi teks tampil tautan adalah `privacy terms`
65. Verifikasi tautan tersebut berhref `https://example.com/terms`

### TC-AC-PP-57: Tombol [Cancel] pada popover Insert Link menutup popover tanpa menyisipkan tautan

66. Catat jumlah tautan di konten editor sebagai baseline
67. Klik tombol Link pada toolbar
68. Isi field URL dengan `https://example.com`
69. Klik `[Cancel]`
70. Verifikasi popover tertutup
71. Verifikasi jumlah tautan di konten editor sama dengan baseline (tidak ada tautan baru)
72. Verifikasi Modal tetap terbuka di state Edit
73. Verifikasi tidak ada dialog yang tampil

### TC-AC-PP-58: Esc dan klik di luar popover Insert Link hanya menutup popover dan tidak memicu guard penutupan modal

74. Klik di akhir konten editor lalu ketik " Extra."
75. Catat jumlah tautan di konten editor sebagai baseline
76. Klik tombol Link pada toolbar
77. Tekan Esc
78. Verifikasi hanya popover yang tertutup
79. Verifikasi Dialog Unsaved Changes tidak tampil
80. Verifikasi Modal tetap terbuka
81. Klik tombol Link pada toolbar
82. Klik area di dalam editor (di luar popover)
83. Verifikasi hanya popover yang tertutup
84. Verifikasi Dialog Unsaved Changes tidak tampil
85. Verifikasi tautan tidak disisipkan (jumlah tautan sama dengan baseline)
86. Tekan Esc sekali lagi
87. Verifikasi Dialog "Unsaved Changes" tampil karena konten berbeda dari snapshot
88. Klik `[Leave]`

### TC-AC-PP-209: Tombol Link pada tautan existing hanya menyisipkan tautan baru

89. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
90. Tunggu konten editor termuat
91. Klik `[Clear Field]`
92. Ketik "terms"
93. Seleksi teks `terms`
94. Klik tombol Link pada toolbar
95. Isi field URL dengan `https://example.com/a`
96. Klik `[Insert]`
97. Seleksi teks `terms` (di dalam tautan)
98. Klik tombol Link pada toolbar
99. Isi field URL dengan `https://example.com/b`
100. Klik `[Insert]`
101. Verifikasi teks `terms` tampil satu kali sebagai tautan dengan href `https://example.com/b`
102. Verifikasi tidak ada tautan bersarang
103. Verifikasi href `https://example.com/a` tidak ada lagi
104. Letakkan kursor di dalam teks `terms` tanpa seleksi
105. Klik tombol Link pada toolbar
106. Isi field URL dengan `https://example.com/c`
107. Klik `[Insert]`
108. Verifikasi tautan baru dengan teks tampil `https://example.com/c` disisipkan sesudah tautan `terms`
109. Verifikasi teks tampil tautan baru adalah URL itu sendiri walau kursor berada di dalam tautan `terms`
110. Verifikasi tautan `terms` tetap berhref `https://example.com/b`
111. Verifikasi tautan `terms` tidak berisi tautan lain
112. Tekan `[↶]` sampai tautan `https://example.com/c` hilang
113. Verifikasi tautan `https://example.com/c` hilang
114. Verifikasi tautan `terms` tetap ada
115. Verifikasi tidak ada tombol Unlink atau ubah tautan di toolbar
116. Klik di akhir tautan `terms`
117. Tekan Enter
118. Ketik "alpha beta"
119. Seleksi `alpha`
120. Klik tombol Link pada toolbar
121. Isi field URL dengan `https://example.com/d`
122. Klik `[Insert]`
123. Seleksi `ha be` (sebagian tautan `alpha` dan sebagian teks biasa)
124. Klik tombol Link pada toolbar
125. Isi field URL dengan `https://example.com/e`
126. Klik `[Insert]`
127. Verifikasi satu tautan berhref `https://example.com/e` dengan teks `alpha be` (seluruh teks tautan lama `alpha` ditambah bagian terseleksi `be`)
128. Verifikasi sisa teks `ta` tetap teks biasa tanpa tautan
129. Verifikasi href `https://example.com/d` tidak ada lagi
130. Letakkan kursor tepat setelah huruf `e` terakhir pada tautan `alpha be` (tepi akhir, tanpa seleksi)
131. Klik tombol Link pada toolbar
132. Isi field URL dengan `https://example.com/f`
133. Klik `[Insert]`
134. Verifikasi tautan baru berhref `https://example.com/f` dengan teks tampil `https://example.com/f` berdiri sendiri (kursor di tepi akhir dianggap di luar tautan)
135. Verifikasi tautan `alpha be` tetap berhref `https://example.com/e` tanpa perubahan
136. Klik `✕` di header
137. Verifikasi Dialog "Unsaved Changes" tampil
138. Klik `[Leave]`

## Notes

- Mode: mock. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC berubah dari urutan nomor: TC-AC-PP-56 (validasi diblokir) ditaruh sebelum TC-AC-PP-55 (penyisipan sukses) mengikuti prinsip 3 konvensi (validasi diblokir sebelum aksi sukses) dan TC-AC-PP-54, 56, 55, 57, 58 berbagi satu sesi modal Edit (satu kali buka) sehingga jumlah buka form (2) tidak melebihi jumlah kejadian menutup (2: `[Leave]` di langkah 88 dan 138). TC-AC-PP-209 membuka sesi kedua karena butuh editor yang dikosongkan (`[Clear Field]`).
- Langkah penghubung (tanpa awalan Verifikasi): langkah 16, 22, 28 (mengosongkan field URL), 36 (`[Cancel]` menutup popover), 37 (menaruh kursor di akhir konten tanpa seleksi), 66 dan 75 (mencatat baseline jumlah tautan), 88 dan 138 (`[Leave]` menutup modal dirty), serta langkah penambah tiga `Verifikasi` "tidak ada error inline di popover" (langkah 42, 49, 56) yang memecah klausa "popover tertutup tanpa error" (S-01).
- Asersi tambahan yang dicatat: langkah 137 (Dialog "Unsaved Changes" sebelum `[Leave]`) tidak ada di Expected TC-AC-PP-209; ditulis agar penutupan modal dirty deterministik (S-08). Langkah 66/75 membuat "tidak ada tautan baru" dapat diasersi walau tautan hasil TC-AC-PP-55 sudah ada di editor.
- Pada TC-AC-PP-58 langkah 74 konten sudah berbeda dari snapshot sejak TC-AC-PP-55, tetapi ketikan " Extra." tetap ditulis sesuai TC.
- Jumlah langkah (138) jauh di atas smell 35 langkah karena satu `Verifikasi` per klausa Expected (S-01) dan enam TC satu topik (popover Insert Link) dan satu kelas harness berbagi sesi modal; tiap blok `###` tetap bermakna walau blok sebelumnya gagal (soft assertion) kecuali kegagalan keras membuka modal Edit.
- Post Condition TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Temuan untuk QA:
  - TC-AC-PP-209 langkah 5 menyebut tombol `[↶]` sedangkan tooltip dan `aria-label` toolbar di TC-AC-PP-34 dan NC-15 adalah "Undo"; spec mengikuti penulisan TC.
  - TC-AC-PP-209 Expected e diurutkan menurut langkah 4 (sesudah Expected b) agar `Verifikasi` ditaruh langsung setelah aksi; urutan abjad Expected di TC (a, b, c, d, e, f) tidak sama dengan urutan langkah.
  - TC-AC-PP-55 dan TC-AC-PP-57 tidak menyebut posisi kursor sebelum `[Link]` diklik; spec menambah langkah menaruh kursor di akhir konten (langkah 37) agar tautan tanpa seleksi punya posisi sisip yang pasti.
