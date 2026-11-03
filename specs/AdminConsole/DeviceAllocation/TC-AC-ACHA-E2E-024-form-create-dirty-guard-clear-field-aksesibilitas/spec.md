---
id: TC-AC-ACHA-E2E-024-form-create-dirty-guard-clear-field-aksesibilitas
title: "Form Allocate Device: Dirty Guard Unsaved Changes, Clear Field, Saving State, State Tombol, dan Aksesibilitas"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-163
  - TC-AC-ACHA-164
  - TC-AC-ACHA-165
  - TC-AC-ACHA-166
  - TC-AC-ACHA-167
  - TC-AC-ACHA-168
  - TC-AC-ACHA-169
  - TC-AC-ACHA-170
  - TC-AC-ACHA-171
  - TC-AC-ACHA-172
  - TC-AC-ACHA-173
  - TC-AC-ACHA-174
  - TC-AC-ACHA-175
  - TC-AC-ACHA-176
  - TC-AC-ACHA-177
  - TC-AC-ACHA-178
  - TC-AC-ACHA-179
  - TC-AC-ACHA-180
  - TC-AC-ACHA-181
coverage:
  web: automated
---

# Form Allocate Device: Dirty Guard Unsaved Changes, Clear Field, Saving State, State Tombol, dan Aksesibilitas

## Prerequisites

- Mode: FE+BE. TC-179 memakai intercept parsial (tunda respons Submit) di atas backend nyata.
- Akun yang diuji (urutan pemakaian dalam spec):

| Kode | Role | Pre-setup | Email | Env var password |
|---|---|---|---|---|
| A-01 | Total Control Principal `PT ABC` (Admin Pratama) | #21 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| A-02 | Total Control Distributor `PT Global Distribusi` (Hendra Wibowo) | #27 | `totalControlDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_DIST_PASSWORD` |
| A-04 | Total Control Partner `CV Karya Mandiri` | #46 | `totalControlPartner2_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_P2_PASSWORD` |

- Login A-01 di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (A-01, `AC_TC_PASSWORD`). Ganti akun A-02 dan A-04 dengan langkah logout dan login eksplisit. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example` (didaftarkan tahap script); password tidak ditulis di spec.
- Data Pre-setup: Client #7 `PT Sejahtera Logistik`, #9 `PT Cipta Kreasi`, #10 `PT Manufaktur Unggul`; Seed 30 alokasi #48 (precondition TC-167, tidak diasersi); kantong #16, #18, #19. Hook `before` menyetel saldo kantong ke nilai Pre-setup lewat fixture API Pre-setup #20 (disediakan tim FE/BE).
- Data Dinamis: dua alokasi `Completed` dibuat (TC-179 NFC Quantity 2, TC-172 BLE Gateway Quantity 50), keduanya milik Principal sehingga tanpa Reserve atau wallet. Efek: kuota Client `PT Manufaktur Unggul` bertambah; modul tanpa Delete sehingga alokasi tidak dihapus.
- Kemampuan baca state BE (disediakan tim FE/BE): jumlah transaksi pengirim (baseline TC-167).
- Kemampuan teknis: menangani dialog `beforeunload` browser (menerima atau membatalkan) pada muat ulang F5 (TC-172); `Spectra.intercept()` untuk menunda 3 detik respons Submit (TC-179, dilepas segera sesudah dipakai); mengamati state hover dan active tombol (gaya terhitung berbeda dari state normal); membaca atribut `aria-required`, `aria-describedby`, dan label aksesibel ikon close; mengamati fokus keyboard dan fokus terkunci di dalam modal.
- Hook suite (dinyatakan sekali di `suite.md`): flag Guided Tooltip halaman Device Allocation disetel true untuk akun aktor dan dipulihkan di `after`, sesi API aktor, fixture API Pre-setup #20, pemulihan preferensi Setup Column.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Akun A-01 Principal: Tutup form bersih lewat `[×]` dan Esc (TC-AC-ACHA-163)

1. Klik `[+ Allocation]`
2. Klik `[×]`
3. Verifikasi form tertutup langsung
4. Verifikasi dialog Unsaved Changes tidak muncul
5. Klik `[+ Allocation]`
6. Tekan Esc
7. Verifikasi form tertutup langsung
8. Verifikasi dialog Unsaved Changes tidak muncul

### Akun A-01: Klik backdrop, dialog Unsaved Changes, Cancel, dan Esc pada dialog (TC-AC-ACHA-168, TC-AC-ACHA-164, TC-AC-ACHA-166, TC-AC-ACHA-165, TC-AC-ACHA-173)

9. Klik `[+ Allocation]`
10. Klik area backdrop di luar form dalam keadaan bersih
11. Verifikasi form tidak tertutup oleh klik backdrop dalam keadaan bersih
12. Isi Quantity `5`
13. Klik area backdrop di luar form
14. Verifikasi form tidak tertutup oleh klik backdrop dalam keadaan dirty
15. Verifikasi dialog Unsaved Changes tidak muncul
16. Verifikasi input Quantity `5` dipertahankan
17. Isi Notes `Uji`
18. Klik `[×]`
19. Verifikasi dialog Unsaved Changes: judul "Unsaved Changes", body "You have unsaved changes. Are you sure you want to leave?", tombol `[Cancel]` dan `[Leave]` (severity warning)
20. Verifikasi form tetap terbuka di belakang dialog
21. Klik `[Cancel]` pada dialog
22. Verifikasi dialog tertutup
23. Verifikasi form tetap terbuka
24. Verifikasi isian Quantity `5` dan Notes `Uji` dipertahankan
25. Pilih Category `TAG - NFC`
26. Tekan Esc
27. Verifikasi dialog Unsaved Changes: judul "Unsaved Changes", body "You have unsaved changes. Are you sure you want to leave?", tombol `[Cancel]` dan `[Leave]` (severity warning)
28. Tekan Esc sekali lagi
29. Verifikasi dialog tertutup (Esc pada dialog setara `[Cancel]`)
30. Verifikasi user tetap di form dengan input dipertahankan

### Akun A-01: Navigasi internal saat form dirty (TC-AC-ACHA-171)

31. Klik item sidebar menu `Dashboard`
32. Verifikasi perpindahan route dicegat dan dialog Unsaved Changes yang sama tampil
33. Klik `[Cancel]` pada dialog
34. Verifikasi navigasi dibatalkan: form tetap terbuka dengan input dipertahankan
35. Klik item sidebar menu `Dashboard` lagi, lalu klik `[Leave]` pada dialog
36. Verifikasi navigasi dilanjutkan dan form ditutup tanpa menyimpan

### Akun A-01: Leave menutup form tanpa menyimpan (TC-AC-ACHA-167) dan checkbox Stay (TC-AC-ACHA-170)

37. Catat baseline jumlah transaksi pengirim lewat kemampuan baca state BE
38. Buka Allocation > Device Allocation
39. Klik `[+ Allocation]`
40. Isi Quantity `5`
41. Klik `[×]`
42. Verifikasi dialog Unsaved Changes tampil
43. Klik `[Leave]` pada dialog
44. Verifikasi form tertutup tanpa menyimpan
45. Verifikasi dialog tertutup
46. Verifikasi tidak ada transaksi baru pada List (jumlah transaksi sama dengan baseline)
47. Klik `[+ Allocation]`
48. Verifikasi form yang dibuka lagi kosong
49. Centang "Stay on this form after submitting"
50. Klik `[×]`
51. Verifikasi form tertutup
52. Verifikasi dialog Unsaved Changes tidak muncul (checkbox Stay bukan field data)

### Akun A-01: Form yang dikosongkan kembali dianggap bersih (TC-AC-ACHA-174)

53. Klik `[+ Allocation]`
54. Isi Quantity `5`
55. Klik `[Clear Field]`
56. Klik `[×]`
57. Verifikasi form tertutup
58. Verifikasi dialog Unsaved Changes tidak muncul (setelah `[Clear Field]` form kembali sama dengan keadaan awal)

### Akun A-01: Clear Field, reset validasi, dan state tombol (TC-AC-ACHA-175, TC-AC-ACHA-178, TC-AC-ACHA-180)

59. Klik `[+ Allocation]`
60. Centang "Stay on this form after submitting", pilih Category `TAG - RFID`, pilih Type `User TAG`, pilih Client `PT Manufaktur Unggul`, isi Quantity `9` dan Notes `Uji`
61. Klik `[Clear Field]`
62. Verifikasi Category kembali kosong (placeholder tampil)
63. Verifikasi Client kembali kosong (placeholder tampil)
64. Verifikasi Quantity kembali kosong (placeholder tampil)
65. Verifikasi Notes kembali kosong (placeholder tampil)
66. Verifikasi radio Type tersembunyi
67. Verifikasi checkbox "Stay on this form after submitting" tetap tercentang
68. Verifikasi form tetap terbuka
69. Verifikasi tidak ada dialog konfirmasi
70. Verifikasi kursor fokus ke field pertama (Category)
71. Klik `[Submit]`
72. Verifikasi tiga pesan error inline tampil: "Category must not be empty", "Client recipient must not be empty", "Quantity must not be empty"
73. Klik `[Clear Field]`
74. Verifikasi seluruh pesan error inline hilang
75. Verifikasi border merah hilang
76. Verifikasi form kembali pristine
77. Arahkan kursor ke `[Submit]`
78. Verifikasi `[Submit]` (filled, success) menampilkan state hover yang berbeda dari state normal
79. Tekan dan tahan `[Submit]`, lalu geser kursor keluar tombol sebelum melepas
80. Verifikasi `[Submit]` menampilkan state active yang berbeda dari state normal
81. Arahkan kursor ke `[Clear Field]`
82. Verifikasi `[Clear Field]` (text, primary) menampilkan state hover yang berbeda dari state normal
83. Tekan dan tahan `[Clear Field]`
84. Verifikasi `[Clear Field]` menampilkan state active yang berbeda dari state normal
85. Lepas tombol mouse, lalu klik `[×]`

### Akun A-01: Saving state tombol Submit dan kontrol beku (TC-AC-ACHA-179)

86. Klik `[+ Allocation]`
87. Pilih Category `TAG - NFC`, Client `PT Manufaktur Unggul`, isi Quantity `2`
88. Pasang intercept: tunda 3 detik respons Submit
89. Klik `[Submit]`
90. Verifikasi `[Submit]` menampilkan indikator loading dan disabled
91. Coba klik `[Submit]`, `[Clear Field]`, `[×]`, dan ubah Quantity selama menunggu
92. Verifikasi `[Clear Field]`, `[×]`, dan seluruh kontrol input disabled selama request berlangsung
93. Tunggu respons diterima, lalu lepas intercept
94. Verifikasi form tertutup setelah respons diterima (kontrol kembali normal pada sukses)

### Akun A-01: Konfirmasi bawaan browser saat reload (TC-AC-ACHA-172), submit sukses di akhir

95. Klik `[+ Allocation]`
96. Muat ulang halaman (F5) dalam keadaan form bersih
97. Verifikasi reload berjalan tanpa konfirmasi bawaan browser
98. Klik `[+ Allocation]`
99. Isi Quantity `5`, lalu muat ulang halaman (F5)
100. Verifikasi konfirmasi bawaan browser (beforeunload) muncul
101. Batalkan konfirmasi bawaan browser
102. Verifikasi form tetap terbuka
103. Verifikasi input Quantity `5` dipertahankan
104. Pilih Category `Hardware - BLE Gateway`, Client `PT Manufaktur Unggul`, ubah Quantity menjadi `50`, lalu klik `[Submit]`
105. Tunggu toast sukses tampil dan form tertutup
106. Muat ulang halaman (F5)
107. Verifikasi reload tidak memunculkan konfirmasi bawaan browser (guard dilepas setelah Submit sukses)

### Akun A-02 Distributor: Field read-only dan pre-filled (TC-AC-ACHA-169) serta Clear Field tidak mengubah From dan Pay From (TC-AC-ACHA-176)

108. Logout, lalu login sebagai A-02 (`PT Global Distribusi`), buka Allocation > Device Allocation
109. Klik `[+ Allocation]`
110. Klik `[×]` tanpa mengubah apa pun
111. Verifikasi form tertutup
112. Verifikasi dialog Unsaved Changes tidak muncul (From read-only dan Pay From pre-filled disabled tidak dihitung sebagai terisi)
113. Klik `[+ Allocation]`
114. Pilih Category `Hardware - BLE Gateway`, Client `PT Sejahtera Logistik`, isi Quantity `5` sampai Preview tampil
115. Verifikasi Preview tampil
116. Klik `[Clear Field]`
117. Verifikasi Category kosong
118. Verifikasi Client kosong
119. Verifikasi Quantity kosong
120. Verifikasi Preview tidak lagi dirender
121. Verifikasi From tetap `PT Global Distribusi (Distributor)`
122. Verifikasi Pay From pre-filled `PT ABC (Principal)` tetap disabled dan tidak berubah
123. Klik `[×]`

### Akun A-04 Partner dua kantong: Clear Field mengosongkan Pay From (TC-AC-ACHA-177) dan aksesibilitas (TC-AC-ACHA-181)

124. Logout, lalu login sebagai A-04 (`CV Karya Mandiri`), buka Allocation > Device Allocation
125. Klik `[+ Allocation]`
126. Pilih Category `TAG - NFC`, Client `PT Cipta Kreasi`, Quantity `5`, dan Pay From `PT ABC (Principal)`
127. Klik `[Clear Field]`
128. Verifikasi Pay From kembali kosong dengan placeholder "Select source pocket"
129. Verifikasi Category kembali kosong
130. Verifikasi Client kembali kosong
131. Verifikasi Quantity kembali kosong
132. Klik `[×]`
133. Klik `[+ Allocation]`
134. Tekan Tab berulang dari field pertama
135. Verifikasi fokus terkunci di dalam modal selama Tab
136. Klik `[Submit]` kosong
137. Verifikasi field wajib Category, Client, Quantity, dan Pay From memiliki `aria-required`
138. Verifikasi field yang menampilkan pesan error inline memiliki `aria-describedby` yang menunjuk pesan itu
139. Verifikasi ikon close punya label aksesibel
140. Tekan Esc
141. Verifikasi Esc menutup modal

## Notes

- Mode FE+BE; sumber `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat satu kelas ringan (perilaku form di browser) dengan dua TC yang membuat data (TC-179 dan TC-172) di akhir blok akun A-01; satu-satunya state global yang tersentuh adalah flag Guided Tooltip (dinyatakan di `suite.md`).
- Alasan spec di atas sekitar 35 langkah: semua blok satu topik (dirty guard, Clear Field, dan aksesibilitas form Allocate Device) dan satu kelas; tiap blok berdiri sendiri; blok akun A-02 dan A-04 dipisah dengan langkah ganti akun eksplisit sehingga tetap bermakna walau blok A-01 gagal (konvensi bagian 3, pemisah (b)); jumlah langkah berasal dari S-01 serta pembukaan form per kejadian menutup form (prinsip 6).
- Penyimpangan urutan (S-10): TC-168 mendahului TC-164 pada form yang sama (Quantity `5` dari TC-168 dipakai ulang oleh TC-164, dengan Notes `Uji` ditambahkan sebelum `[×]` supaya keadaan form sama dengan precondition TC-166); TC-165 dan TC-173 melanjutkan dialog yang sama (Esc ke dialog, lalu Esc kedua); TC-175, TC-178, dan TC-180 berbagi satu form (TC-178 dan TC-180 melanjutkan setelah `[Clear Field]` TC-175); TC-179 dan TC-172 yang membuat data diletakkan di akhir blok A-01 (prinsip 5).
- Jumlah pembukaan form tidak kurang dari jumlah kejadian menutup form (prinsip 6): kasus menutup bersih (TC-163, TC-170, TC-169) memakai form baru; kasus menutup form setelah `[Clear Field]` (TC-174, TC-175 sampai TC-180, TC-176, TC-177) memakai `[×]` tanpa asersi dialog kecuali pada TC-174.
- Langkah penghubung (S-03): isi Notes `Uji` sebelum `[×]` pada TC-164; buka Allocation > Device Allocation sesudah navigasi sidebar; catat baseline; `[Clear Field]` dan `[×]` untuk membersihkan state; logout dan login ganti akun; tunggu toast sukses; pasang dan lepas intercept; tekan dan tahan tombol lalu geser keluar sebelum melepas supaya tidak memicu klik. Pada TC-176 langkah "Verifikasi Preview tampil" adalah anchor positif untuk asersi Preview tidak dirender sesudah `[Clear Field]` (asersi tambahan, S-03).
- Pengecualian S-12 nama literal: nama entitas dan Client Pre-setup literal (sudah ada di environment); spec ini tidak men-seed data bernama dinamis. Notes `Uji` hanya diketik pada form yang ditutup lewat `[Leave]` atau `[Clear Field]` dan tidak pernah tersimpan.
- Langkah 71 sampai 72 (klik `[Submit]` pada form kosong dan `Verifikasi` tiga pesan error inline) adalah penyiapan dan anchor positif: TC-178 hanya menyebut pesan error "hilang" sesudah `[Clear Field]`, sehingga pesan error harus tampil lebih dulu supaya asersi hilang bermakna (S-03).
- Temuan untuk QA:
  - TC-171 menulis "item sidebar menu lain" tanpa menyebut item; spec memakai item sidebar `Dashboard`.
  - TC-172 butir b tidak menyebut tindakan yang dibatalkan secara rinci (batalkan konfirmasi bawaan browser) selain Expected; kemampuan menangani dialog `beforeunload` ditulis di Prerequisites.
  - TC-175 Expected c ("kursor fokus ke field pertama") tidak menyebut field pertama; spec mengasersi fokus pada field Category (urutan form).
  - TC-179 Expected c ("kontrol kembali normal") ditulis sebagai "form tertutup pada sukses"; spec hanya mengasersi form tertutup. Post Condition (kuota Client, panel Stock Balance Summary) tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-180 tidak menyebut properti visual yang dibandingkan; spec mengasersi bahwa state hover dan active berbeda dari state normal.
  - TC-181 butir c tidak menyebut jumlah tekanan Tab atau urutan fokus; spec mengasersi fokus tidak keluar dari modal.
  - TC-164 Expected a menyebut "severity warning" tanpa penanda visual; diasersi bersama teks dialog.
  - TC-167 Precondition menyebut Seed 30 alokasi tetapi Expected tidak memakainya; seed tidak diasersi.
