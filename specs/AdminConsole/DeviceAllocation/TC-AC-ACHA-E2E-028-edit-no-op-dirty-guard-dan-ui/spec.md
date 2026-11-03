---
id: TC-AC-ACHA-E2E-028-edit-no-op-dirty-guard-dan-ui
title: "Form Edit Allocation: Dirty Guard, Save Tanpa Perubahan, Double-submit, Saving State, Clear Field, Hover, dan Accessibility"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-211
  - TC-AC-ACHA-212
  - TC-AC-ACHA-213
  - TC-AC-ACHA-214
  - TC-AC-ACHA-215
  - TC-AC-ACHA-216
  - TC-AC-ACHA-217
  - TC-AC-ACHA-218
  - TC-AC-ACHA-219
  - TC-AC-ACHA-428
  - TC-AC-ACHA-469
coverage:
  web: automated
---

# Form Edit Allocation: Dirty Guard, Save Tanpa Perubahan, Double-submit, Saving State, Clear Field, Hover, dan Accessibility

## Prerequisites

- Mode: FE+BE (satu blok memakai intercept parsial di atas backend nyata: TC-AC-ACHA-217).
- Akun aktor pertama: Group Member Distributor toggle ON (MB_ON, Pre-setup #32) `memberOnDistributor_automated_qaTeam1@qwertysystem.net`, nama pengguna Budi Santoso (PIC pada Allocation Log = Budi Santoso), password `Spectra.env.AC_DA_MB_ON_PASSWORD`. Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun di tengah spec: Group Member Partner CV Karya Mandiri toggle ON (MB_P2, Pre-setup #47) `memberOnPartner2_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_MB_P2_PASSWORD`.
- Hook suite: sesi API aktor, flag Guided Tooltip, pemulihan preferensi Setup Column, seed 30 baris idempotent (Lampiran A butir A-6), dan fixture API Pre-setup #20 dinyatakan di `suite.md`. Hook `after` memulihkan seed lewat fixture Pre-setup #20.
- Data milik spec (dibuat di hook `before` lewat fixture seeding "disediakan tim FE/BE", dibersihkan di hook `after`; Allocation ID dibaca saat seeding sebagai Dynamic Reference dan dipakai sebagai kata kunci Search): (1) T-A, transaksi Waiting for Approval dibuat MB_ON yang mereplikasi Pre-setup #49 (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch uji`, Total Cost $250.00, Reserve $250.00 pada kantong PT Global Distribusi saldo $20,000.00), dipulihkan ke keadaan awal itu lewat fixture sebelum blok TC-AC-ACHA-217 dan TC-AC-ACHA-211; (2) T-P2, transaksi Waiting for Approval dibuat MB_P2 yang mereplikasi Pre-setup #50 (NFC, Quantity 40, Client PT Cipta Kreasi, Pay From `PT Global Distribusi (Distributor)`, Total Cost $60.00, kantong A saldo $1,000.00 Reserved $60.00 dan kantong B saldo $3,000.00, Pre-setup #18 dan #19). Notes `Batch uji` literal karena diasersi TC (pengecualian S-12, Lampiran A butir A-6).
- Kemampuan teknis: (1) mengaktifkan paksa `[Save]` yang disabled lewat DOM (hapus atribut `disabled`) pada blok TC-AC-ACHA-428; (2) intercept parsial di atas backend nyata yang menunda respons Save Edit 3 detik pada blok TC-AC-ACHA-217 (endpoint Edit tidak disebut TC; request diidentifikasi tim FE) dan dilepas segera setelah blok selesai; (3) kemampuan membaca Reserved, jumlah entri Allocation Log transaksi, serta jumlah dokumen Activity Log dan System Log untuk Allocation ID (disediakan tim FE/BE, tanpa endpoint karangan; N dibaca sebelum aksi dan asersi memakai selisih, S-12); (4) jam server dan jam browser sinkron; Last Updated berketelitian menit sehingga asersi Last Updated tidak berubah dibandingkan dengan nilai baseline yang dicatat sebelum aksi.
- State global: preferensi kolom Setup Column akun MB_ON dan MB_P2 (kolom Notes, Cost, dan Paid From untuk MB_ON, Paid From untuk MB_P2; ditampilkan ulang sesudah ganti akun karena cakupan preferensi lintas akun tidak diasumsikan; dipulihkan hook `after`); suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `AC_DA_MB_ON_PASSWORD`, `AC_DA_MB_P2_PASSWORD` (satu nama satu arti).

## Test Steps

1. Buka Setup Column, aktifkan kolom Notes, Cost, dan Paid From, klik `[Save]`
2. Ketik Search Allocation ID transaksi T-A, tekan Enter

### TC-AC-ACHA-212: Tutup form Edit yang belum diubah tanpa dialog

3. Buka menu row action `⋯` transaksi itu, klik `Edit`
4. Tutup form dengan `[×]` tanpa mengubah apa pun
5. Verifikasi form tertutup langsung
6. Verifikasi dialog `Unsaved Changes` tidak muncul
7. Buka menu row action `⋯` transaksi itu, klik `Edit`
8. Tutup form dengan Esc
9. Verifikasi form tertutup langsung
10. Verifikasi dialog `Unsaved Changes` tidak muncul

### TC-AC-ACHA-214: Edit yang dikembalikan identik dianggap bersih

11. Buka menu row action `⋯` transaksi itu, klik `Edit`
12. Ubah Quantity menjadi `101`
13. Ubah Quantity kembali menjadi `100`
14. Klik `[×]`
15. Verifikasi form tertutup karena nilai identik dengan snapshot saat form dibuka
16. Verifikasi dialog `Unsaved Changes` tidak muncul

### TC-AC-ACHA-213: Form Edit dirty ditutup memunculkan dialog Unsaved Changes

17. Buka menu row action `⋯` transaksi itu, klik `Edit`
18. Ubah Notes menjadi `Draf`
19. Klik `[×]`
20. Verifikasi dialog `Unsaved Changes` (severity warning): judul "Unsaved Changes", body "You have unsaved changes. Are you sure you want to leave?", tombol `[Cancel]` dan `[Leave]`
21. Klik `[Leave]`
22. Verifikasi form tertutup tanpa menyimpan
23. Verifikasi kolom Notes transaksi tetap `Batch uji`

### TC-AC-ACHA-469: Cancel pada dialog Unsaved Changes form Edit tetap di form

24. Buka menu row action `⋯` transaksi itu, klik `Edit`
25. Ubah Quantity menjadi `120` dan Notes menjadi `Draf`
26. Klik `[×]`
27. Verifikasi dialog `Unsaved Changes` tampil
28. Klik `[Cancel]` pada dialog
29. Verifikasi dialog `Unsaved Changes` tertutup
30. Verifikasi form Edit tetap terbuka
31. Verifikasi Quantity `120` dipertahankan
32. Verifikasi Notes `Draf` dipertahankan
33. Verifikasi `[Save]` enabled

### TC-AC-ACHA-215: Klik backdrop form Edit adalah no-op

34. Klik area backdrop di luar form
35. Verifikasi form Edit tidak tertutup
36. Verifikasi dialog `Unsaved Changes` tidak muncul
37. Verifikasi Notes `Draf` dipertahankan

### TC-AC-ACHA-218: State hover tombol utama form Edit

38. Ubah Quantity menjadi `101`
39. Arahkan kursor ke `[Save]`
40. Verifikasi `[Save]` (filled, success) menampilkan state hover berbeda dari state normal
41. Arahkan kursor ke `[Clear Field]`
42. Verifikasi `[Clear Field]` (text, primary) menampilkan state hover berbeda dari state normal
43. Klik `[×]`
44. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
45. Klik `[Leave]`
46. Verifikasi baris transaksi di List menampilkan Quantity `100` (transaksi belum berubah, TC-AC-ACHA-469 butir c)

### TC-AC-ACHA-428: Save Edit tanpa perubahan (termasuk hanya kapitalisasi atau spasi tepi) adalah No-Op tanpa log

47. Catat jumlah entri Allocation Log transaksi T-A, jumlah dokumen Activity Log dan System Log untuk Allocation ID itu, serta Quantity, Notes, kolom Paid From, Reserved kantong PT Global Distribusi, dan Last Updated transaksi sebagai baseline
48. Buka menu row action `⋯` transaksi itu, klik `Edit`
49. Aktifkan paksa tombol `[Save]` lewat DOM (hapus atribut disabled) tanpa mengubah nilai
50. Klik `[Save]`
51. Verifikasi toast netral (severity Info) "No changes to save." tampil
52. Verifikasi tidak ada toast sukses
53. Verifikasi Quantity transaksi sama dengan baseline pada langkah 47 (`100`)
54. Verifikasi Notes transaksi sama dengan baseline pada langkah 47 (`Batch uji`)
55. Verifikasi kolom Paid From transaksi sama dengan baseline pada langkah 47 (`PT ABC (Principal)`)
56. Verifikasi Reserved kantong PT Global Distribusi sama dengan baseline pada langkah 47 ($250.00)
57. Verifikasi Last Updated transaksi sama dengan baseline pada langkah 47
58. Verifikasi jumlah entri Allocation Log transaksi sama dengan baseline pada langkah 47
59. Verifikasi jumlah dokumen Activity Log untuk Allocation ID sama dengan baseline pada langkah 47
60. Verifikasi jumlah dokumen System Log untuk Allocation ID sama dengan baseline pada langkah 47
61. Ubah Notes dari `Batch uji` menjadi `BATCH UJI` dan aktifkan paksa tombol `[Save]` lewat DOM
62. Klik `[Save]`
63. Verifikasi toast netral "No changes to save." tampil
64. Verifikasi Notes tersimpan sama dengan baseline pada langkah 47 (`Batch uji`)
65. Ubah Notes menjadi `  Batch uji  ` (dua spasi di awal dan akhir) dan aktifkan paksa tombol `[Save]` lewat DOM
66. Klik `[Save]`
67. Verifikasi toast netral "No changes to save." tampil
68. Verifikasi Notes tersimpan sama dengan baseline pada langkah 47 (`Batch uji`)
69. Verifikasi tidak ada entri log baru: jumlah entri Allocation Log sama dengan baseline pada langkah 47
70. Verifikasi jumlah dokumen Activity Log sama dengan baseline pada langkah 47
71. Verifikasi jumlah dokumen System Log sama dengan baseline pada langkah 47
72. Ubah Notes kembali menjadi `Batch uji`
73. Klik `[×]`

### TC-AC-ACHA-217: Saving state tombol Save

74. Pulihkan transaksi T-A ke keadaan awal lewat fixture hingga tersimpan, muat ulang halaman (F5), lalu ganti isi kotak search dengan Allocation ID transaksi itu, tekan Enter
75. Buka menu row action `⋯` transaksi itu, klik `Edit`
76. Ubah Quantity menjadi `120`
77. Pasang intercept yang menunda respons Save Edit 3 detik
78. Klik `[Save]`
79. Verifikasi `[Save]` menampilkan loading dan disabled
80. Verifikasi `[Clear Field]` disabled
81. Verifikasi `[×]` disabled
82. Verifikasi input form disabled
83. Coba klik `[Save]`, `[Clear Field]`, dan `[×]` selama menunggu
84. Tunggu respons diterima, lalu lepas intercept
85. Verifikasi form tertutup
86. Verifikasi toast sukses: "Success, device allocation has been updated."

### TC-AC-ACHA-211: Double-submit Save hanya memproses satu request

87. Pulihkan transaksi T-A ke keadaan awal lewat fixture hingga tersimpan, muat ulang halaman (F5), lalu ganti isi kotak search dengan Allocation ID transaksi itu, tekan Enter
88. Catat jumlah entri Allocation Log transaksi T-A sebagai baseline
89. Buka menu row action `⋯` transaksi itu, klik `Edit`
90. Ubah Quantity menjadi `120`
91. Klik `[Save]` dua kali cepat
92. Verifikasi `[Save]` masuk Saving state setelah klik pertama
93. Tunggu form Edit tertutup
94. Buka menu row action `⋯` transaksi itu, klik `Allocation Log`
95. Verifikasi jumlah entri bertambah tepat satu dari baseline pada langkah 88
96. Verifikasi entri baru itu `Allocation edited by [PIC]`
97. Tutup modal Allocation Log
98. Verifikasi Wallet kantong PT Global Distribusi: Reserved menjadi $300.00 satu kali

### TC-AC-ACHA-216: Clear Field pada Edit hanya mengosongkan field yang dapat diubah

99. Ganti akun: Logout, login sebagai MB_P2 (Pre-setup #47), buka Allocation > Device Allocation
100. Buka Setup Column, aktifkan kolom Paid From, klik `[Save]`
101. Ketik Search Allocation ID transaksi T-P2, tekan Enter
102. Catat Quantity dan kolom Paid From transaksi T-P2 sebagai baseline
103. Buka menu row action `⋯` transaksi itu, klik `Edit`
104. Klik `[Clear Field]`
105. Verifikasi Quantity dikosongkan (bukan dikembalikan ke nilai tersimpan)
106. Verifikasi Notes dikosongkan (bukan dikembalikan ke nilai tersimpan)
107. Verifikasi Pay From dikosongkan (bukan dikembalikan ke nilai tersimpan)
108. Verifikasi Category, Type, Client, dan From tidak berubah
109. Verifikasi tidak ada dialog konfirmasi
110. Verifikasi form tetap terbuka
111. Verifikasi `[Save]` tidak disabled
112. Klik `[Save]`
113. Verifikasi pesan "Quantity must not be empty" tampil
114. Verifikasi pesan "Pay from must not be empty" tampil
115. Verifikasi Quantity transaksi T-P2 sama dengan baseline pada langkah 102 (`40`)
116. Verifikasi kolom Paid From transaksi T-P2 sama dengan baseline pada langkah 102 (`PT Global Distribusi (Distributor)`)

### TC-AC-ACHA-219: Accessibility form Edit

117. Tekan Tab berulang pada form Edit yang sama
118. Verifikasi field wajib Quantity dan Pay From memiliki `aria-required`
119. Verifikasi fokus terkunci di dalam modal
120. Verifikasi ikon close punya label aksesibel
121. Klik `[Save]` (Quantity masih kosong dari blok sebelumnya)
122. Verifikasi field dengan pesan error memiliki `aria-describedby`
123. Tekan Esc
124. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
125. Klik `[Leave]`
126. Verifikasi modal Edit tertutup

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan TC (S-05, S-10): blok tanpa perubahan data (TC-AC-ACHA-212, 214, 213, 469, 215, 218) berjalan lebih dulu; blok yang mengubah data (TC-AC-ACHA-428 sebagai no-op, 217 dan 211 sebagai Save sukses) di akhir blok MB_ON; blok MB_P2 (TC-AC-ACHA-216, 219) terakhir karena butuh ganti akun satu kali. TC-AC-ACHA-215 dan TC-AC-ACHA-218 melanjutkan form dirty dari TC-AC-ACHA-469 (Notes `Draf`) tanpa membuka ulang (prinsip 8, halaman yang sama dipakai berulang; TC-AC-ACHA-218 mengubah Quantity menjadi `101` pada form yang sama); TC-AC-ACHA-219 melanjutkan form TC-AC-ACHA-216 yang Quantity-nya sudah kosong dan sudah memunculkan pesan error. Form dirty ditutup deterministik (`[×]`, `Verifikasi` dialog `Unsaved Changes`, `[Leave]`, S-08).
- Pembagian TC lintas spec: klausa absence TC-AC-ACHA-428 (Allocation Log, Activity Log, System Log tidak menambah entri) juga dirujuk spec 049 `absence-pencatatan-log-aksi-ditolak`; spec ini tetap memuat `Verifikasi` berbaseline pada langkah 58 sampai 60 dan 69 sampai 71 (S-05, TC terbelah).
- Langkah penghubung (S-03, R-16): langkah 1 dan 100 (Setup Column; kolom Notes, Cost, dan Paid From diperlukan untuk asersi, kolom Paid From ditampilkan ulang sesudah ganti akun ke MB_P2); langkah 2, 74, 87, 101 (Search Allocation ID untuk menemukan baris target; pemulihan transaksi dan muat ulang di langkah 74 dan 87); langkah 47, 88, dan 102 (baseline; langkah 47 mencakup Quantity, Notes, Pay From, Reserved, dan Last Updated sehingga langkah 53 sampai 57, 64, dan 68 membandingkan terhadap baseline, bukan literal, S-12); langkah 49, 61, 65 (mengaktifkan paksa `[Save]` lewat DOM, aksi TC-AC-ACHA-428); langkah 72 dan 73 (mengembalikan Notes dan menutup form sebelum blok berikutnya; bahwa form tertutup tanpa dialog karena nilai identik dengan nilai tersimpan tidak diasersi karena TC-428 tidak memintanya); langkah 77 dan 84 (memasang dan melepas intercept, S-09); langkah 83 (aksi TC-AC-ACHA-217 yang diamati lewat langkah 79 sampai 82); langkah 93 (menunggu form tertutup); langkah 97 (menutup modal Allocation Log); langkah 99 (ganti akun); langkah 43, 45, 123, 125 (menutup form dirty).
- Spec ini melewati sekitar 35 langkah. Alasan: seluruhnya satu topik (perilaku form Edit tanpa aksi sukses bernilai bisnis lain), satu dataset transaksi, tiap blok berdiri sendiri (blok yang mengubah data memulihkan transaksi sendiri) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan `Verifikasi` dipecah per klausa (S-01).
- P-2 (pemicu bukan objek uji): intercept penundaan respons pada TC-AC-ACHA-217 hanya menahan respons untuk mengamati Saving state (bukan kegagalan yang dipaksa, bukan kelas b), dan dilepas segera setelah pengamatan (S-09).
- P-5 (b, objek uji ringan): TC-AC-ACHA-428 memaksa `[Save]` aktif lewat DOM (kelas a) sebagai objek uji ringan tanpa harness eksternal dan tanpa state berat sendiri; ini satu-satunya TC kelas a di spec fungsional ini (intercept TC-AC-ACHA-217 hanya menahan respons untuk mengamati Saving state, lihat P-2).
- Pengecualian S-12: Notes `Batch uji` dan nama entitas Pre-setup bernilai literal karena diasersi TC (Lampiran A butir A-6).
- Temuan untuk QA:
  - TC-AC-ACHA-428 tidak menyatakan apakah form Edit tetap terbuka atau tertutup setelah toast netral "No changes to save."; langkah 61 sampai 73 mengasumsikan form tetap terbuka (tidak ada mutasi). Jika form tertutup, spec perlu disesuaikan.
  - TC-AC-ACHA-428 langkah 3 menyebut "Ulangi langkah 1" (klik `Edit`, aktifkan paksa `[Save]`, klik) untuk kedua variasi Notes; spec memakai satu form yang sama dan hanya mengubah Notes, bukan membuka ulang form.
  - TC-AC-ACHA-219 butir b menyatakan "Esc menutup modal", sedangkan form pada langkah 117 s.d. 122 sudah dirty (Quantity dikosongkan), sehingga Esc memunculkan dialog `Unsaved Changes` (TC-AC-ACHA-213); spec menambahkan `Verifikasi` dialog dan `[Leave]` lalu mengasersi modal tertutup. TC perlu menyatakan kondisi form saat Esc.
  - TC-AC-ACHA-219 butir a ("field wajib memiliki `aria-required`") tidak menyebut Notes dan Pay From untuk Principal; spec hanya mengasersi Quantity dan Pay From (Partner dua kantong).
  - TC-AC-ACHA-216 Expected c menyebut pesan "Pay from must not be empty" (huruf kecil pada "from") berbeda dari label field `Pay From`; spec memakai teks persis TC.
  - TC-AC-ACHA-211, 217 Post Condition ("Wallet Balance dan Wallet Transaction List (Reserve disesuaikan), Approvals Active Tab (data subject terbaru)") tanpa langkah observasi di TC: tidak diasersi; hanya Reserved $300.00 pada TC-AC-ACHA-211 yang punya Expected butir b.
  - Kontrak fixture (seeding transaksi milik spec, pemulihan transaksi, baca Reserved, baca jumlah entri Allocation Log dan dokumen Activity Log dan System Log) tidak tertulis di TC, PRD, atau LLD; ditulis "disediakan tim FE/BE" (R-19, S-13).
