---
id: TC-GS-UCF-E2E-041-bulk-activate-deactivate-komposisi-seleksi-dan-dialog
title: "Bulk Activate dan Bulk Deactivate: Komposisi Seleksi, Dialog, Cancel, Efek ke User, dan Klik Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-164
  - TC-GS-UCF-165
  - TC-GS-UCF-166
  - TC-GS-UCF-167
  - TC-GS-UCF-168
  - TC-GS-UCF-481
  - TC-GS-UCF-482
  - TC-GS-UCF-483
  - TC-GS-UCF-343
  - TC-GS-UCF-346
  - TC-GS-UCF-347
coverage:
  web: automated
---

# Bulk Activate dan Bulk Deactivate: Komposisi Seleksi, Dialog, Cancel, Efek ke User, dan Klik Ganda

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec ini mengubah status Custom Field milik sendiri, bergantung pada total tepat 14 Custom Field pada blok awal (TC-GS-UCF-168, 164, 167; kebersihan field sisa dijamin butir hook suite "Field sisa Client A" di `suite.md`), dan membaca Changelog yang dibagi suite; tidak berjalan bersamaan dengan spec lain.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; langkah tidak mengulang pembukaan layar kecuali sesudah berpindah halaman.
- Akun aktor: Total Control Client A `Sari Dewi` (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (hanya dibaca, tidak diubah atau dihapus spec ini; seluruh aksi atasnya dibatalkan lewat `[Cancel]` atau hanya membuka overlay, sehingga Last Updated tidak berubah, pengecualian S-06): 14 Custom Field (6 Pre-setup `Cost Center` Active, `Employee Grade`, `Job Description`, `Bonus` Active, `Office Phone`, `Joining Date` Inactive dan 8 Population `Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID`, `Work Notes`, `Annual Target`, `badge number`) di-seed idempotent oleh hook `before` lewat API (disediakan tim FE/BE; dilewati bila sudah ada). User `Rahmat Hidayat` (`rahmatHidayat_automated_qaTeam1@qwertysystem.net`, Pre-setup) dengan nilai `Grade 5` pada `Employee Grade` dipakai sebagai anchor pembanding di Detail User.
- Data Dinamis (bersuffix per run; fixture baru `Fixture.customFieldUser.bulkToggle041`; mekanisme seeding nilai Custom Field pada User disediakan tim FE/BE, lihat Temuan untuk QA). Karena TC-GS-UCF-168 dan 164 mengandalkan total tepat 14 baris pada page size 25, seluruh Data Dinamis di-seed lewat API pada langkah penghubung 31 (disediakan tim FE/BE), bukan di hook `before`:
  - `Bulk One On {runId}-041`: Text; Inactive (TC-GS-UCF-481).
  - `Bulk One Off {runId}-041`: Text; Active (TC-GS-UCF-482).
  - `Bulk Act 01 {runId}-041` sampai `Bulk Act 12 {runId}-041`: 12 field Text; Inactive; bebas nilai User (TC-GS-UCF-483).
  - `Bulk On A {runId}-041` (Inactive; nilai User Rahmat Hidayat = `Back`), `Bulk On B {runId}-041` (Inactive), `Bulk On C {runId}-041` (Active), `Bulk Off D {runId}-041` (Inactive): Text (TC-GS-UCF-165 dan 166; TC-GS-UCF-166 memakai A dan B yang Active hasil TC-GS-UCF-165).
  - `Filt Keep A {runId}-041`, `Filt Keep B {runId}-041`, `Filt Other {runId}-041`: Text; Active (TC-GS-UCF-343).
  - `Bulk Dbl On A {runId}-041`, `Bulk Dbl On B {runId}-041`: Text; Inactive (TC-GS-UCF-346).
  - `Bulk Dbl Off A {runId}-041`, `Bulk Dbl Off B {runId}-041`: Text; Active (TC-GS-UCF-347).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Custom Field bersuffix `{runId}-041` yang masih ada dan nilai Custom Field milik spec pada Rahmat Hidayat; kembalikan page size tabel ke default (10).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: scroll pada container daftar bullet dialog; klik ganda cepat pada `[Activate]` dan `[Deactivate]` (TC-GS-UCF-346 dan 347); Search tabel Custom Field; Changelog Custom Field dengan filter Action dan Search; menunggu toast sukses lama hilang otomatis (jeda pendek, ≤ 4 detik, TC-GS-UCF-489) pada langkah 121. Entri Changelog bersifat permanen; asersi jumlah entri memakai Search `{runId}-041` (suffix berisi digit run saja) sehingga baseline entri milik run ini adalah nol.
- State global: page size tabel (cache browser) diubah ke 25 dan dipulihkan ke 10 pada langkah akhir; flag Guided Tooltip diatur hook suite.

## Test Steps

### TC-GS-UCF-168: Dialog Bulk Deactivate memuat seluruh nama dalam container scrollable

1. Ubah page size menjadi 25
2. Klik checkbox header halaman, lalu uncheck baris `Cost Center` dan `Joining Date` (12 baris Active tersisa terpilih)
3. Klik `Bulk Action` > `Deactivate`
4. Verifikasi dialog `Deactivate Custom Fields` memuat 12 bullet lengkap tanpa diringkas: `Annual Target`, `badge number`, `Birth Date`, `Blood Type`, `Bonus`, `Emergency Phone`, `Employee Grade`, `Job Description`, `Office Phone`, `Shirt Size`, `Tax ID`, `Work Notes`
5. Scroll daftar bullet
6. Verifikasi daftar bullet dapat di-scroll
7. Klik `[Cancel]`
8. Verifikasi tidak ada toast
9. Verifikasi dialog tertutup tanpa perubahan
10. Klik `(✕)` pada Bulk Action Bar

### TC-GS-UCF-164: Aksi Activate dan Deactivate pada Bulk Action Bar mengikuti komposisi seleksi

11. Centang `Cost Center` dan `Bonus` (keduanya Active), klik `Bulk Action`
12. Verifikasi overlay `Bulk Action` menampilkan `Deactivate` dan `Delete`
13. Verifikasi `Activate` disembunyikan (bukan disabled)
14. Tutup overlay `Bulk Action`, uncheck `Cost Center` dan `Bonus`, centang `Joining Date` (Inactive), klik `Bulk Action`
15. Verifikasi overlay `Bulk Action` menampilkan `Activate` dan `Delete`
16. Verifikasi `Deactivate` disembunyikan
17. Tutup overlay `Bulk Action`, centang `Cost Center` (seleksi: `Cost Center` dan `Joining Date`), klik `Bulk Action`
18. Verifikasi overlay `Bulk Action` menampilkan `Activate`, `Deactivate`, dan `Delete`
19. Tutup overlay `Bulk Action`, klik `(✕)` pada Bulk Action Bar

### TC-GS-UCF-167: Cancel dialog Bulk Activate dan Bulk Deactivate mempertahankan seleksi

20. Centang `Cost Center` dan `Bonus`, klik `Bulk Action` > `Deactivate`, klik `[Cancel]`
21. Verifikasi tidak ada toast
22. Verifikasi dialog tertutup
23. Verifikasi seleksi `Cost Center` dan `Bonus` tetap tercentang
24. Verifikasi Bulk Action Bar tetap tampil
25. Klik `(✕)` pada Bulk Action Bar, centang `Joining Date` (Inactive) saja, klik `Bulk Action` > `Activate`, klik `[Cancel]`
26. Verifikasi tidak ada toast
27. Verifikasi dialog tertutup
28. Verifikasi seleksi `Joining Date` tetap tercentang
29. Verifikasi Bulk Action Bar tetap tampil
30. Verifikasi status `Joining Date` tidak berubah (switch Off)
31. Klik `(✕)` pada Bulk Action Bar, seed Data Dinamis spec ini lewat API (disediakan tim FE/BE), lalu muat ulang halaman (F5)

### TC-GS-UCF-481: Bulk Activate dengan 1 baris terpilih memakai dialog single

32. Ketik Search `Bulk One On {runId}-041`, tekan Enter
33. Centang `Bulk One On {runId}-041`
34. Klik `Bulk Action` > `Activate`
35. Verifikasi dialog `Activate Custom Field` (singular) menampilkan 1 bullet `Bulk One On {runId}-041`, body "Activating this field will make it and its data visible in all user forms. Are you sure you want to activate it?" (bukan "...activate them?"), serta tombol `[Cancel]` dan `[Activate]`
36. Klik `[Cancel]`
37. Verifikasi tidak ada toast
38. Verifikasi dialog tertutup
39. Verifikasi `Bulk One On {runId}-041` tetap Inactive
40. Verifikasi seleksi dan Bulk Action Bar tetap tampil
41. Klik `(✕)` pada Bulk Action Bar, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-482: Bulk Deactivate dengan 1 baris terpilih memakai dialog single

42. Ketik Search `Bulk One Off {runId}-041`, tekan Enter
43. Centang `Bulk One Off {runId}-041`
44. Klik `Bulk Action` > `Deactivate`
45. Verifikasi dialog `Deactivate Custom Field` (singular) menampilkan 1 bullet `Bulk One Off {runId}-041`, body "Deactivating this field will hide it and its data from all user forms. You can reactivate it later. Are you sure you want to deactivate it?" (bukan "...deactivate them?"), serta tombol `[Cancel]` dan `[Deactivate]`
46. Klik `[Cancel]`
47. Verifikasi tidak ada toast
48. Verifikasi dialog tertutup
49. Verifikasi `Bulk One Off {runId}-041` tetap Active
50. Verifikasi seleksi dan Bulk Action Bar tetap tampil
51. Klik `(✕)` pada Bulk Action Bar, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-483: Dialog Bulk Activate memuat seluruh nama dalam container scrollable

52. Ubah page size menjadi 25
53. Ketik Search `Bulk Act`, tekan Enter
54. Klik checkbox header
55. Verifikasi counter `12 custom fields selected`
56. Klik `Bulk Action` > `Activate`
57. Verifikasi dialog `Activate Custom Fields` memuat 12 bullet `Bulk Act 01 {runId}-041` sampai `Bulk Act 12 {runId}-041` dalam container scrollable (tidak diringkas), body "Activating these fields will make them and their data visible in all user forms. Are you sure you want to activate them?", serta tombol `[Cancel]` dan `[Activate]`
58. Scroll daftar bullet
59. Verifikasi daftar dapat di-scroll sampai `Bulk Act 12 {runId}-041`
60. Klik `[Cancel]`
61. Verifikasi dialog tertutup
62. Verifikasi seluruh field `Bulk Act 01 {runId}-041` sampai `Bulk Act 12 {runId}-041` tetap Inactive
63. Klik `(✕)` pada Bulk Action Bar, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-165: Bulk Activate hanya mengaktifkan baris Inactive dan mengabaikan baris Active

64. Ketik Search `Bulk On`, tekan Enter
65. Centang `Bulk On A {runId}-041`, `Bulk On B {runId}-041`, dan `Bulk On C {runId}-041`
66. Klik `Bulk Action` > `Activate`
67. Verifikasi dialog `Activate Custom Fields` memuat bullet `Bulk On A {runId}-041`, `Bulk On B {runId}-041`, `Bulk On C {runId}-041` dalam container scrollable, body "Activating these fields will make them and their data visible in all user forms. Are you sure you want to activate them?", serta tombol `[Cancel]` dan `[Activate]`
68. Verifikasi tombol `[Activate]` bergaya primary, bukan danger (merah)
69. Klik `[Activate]`
70. Verifikasi muncul toast sukses: "Success, custom field has been activated."
71. Verifikasi Bulk Action Bar hilang dan seleksi di-reset
72. Verifikasi `Bulk On A {runId}-041` dan `Bulk On B {runId}-041` berstatus Active
73. Verifikasi `Bulk On C {runId}-041` tidak berubah (tetap Active)
74. Klik icon Changelog, pilih filter Action `Activate`, Search `{runId}-041`, tekan Enter
75. Verifikasi Changelog memuat tepat 2 entri Activate (`Bulk On A {runId}-041` dan `Bulk On B {runId}-041`)
76. Verifikasi Changelog tidak memuat entri untuk `Bulk On C {runId}-041`
77. Tutup modal Changelog dengan `[✕]`
78. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
79. Verifikasi Detail User Rahmat Hidayat menampilkan `Bulk On A {runId}-041` dengan nilai `Back`
80. Buka Global Settings > User > Custom Field

### TC-GS-UCF-166: Bulk Deactivate hanya menonaktifkan baris Active dan mengabaikan baris Inactive

81. Ketik Search `Bulk O`, tekan Enter
82. Centang `Bulk On A {runId}-041`, `Bulk On B {runId}-041`, dan `Bulk Off D {runId}-041`
83. Klik `Bulk Action` > `Deactivate`
84. Verifikasi dialog `Deactivate Custom Fields` memuat bullet `Bulk On A {runId}-041`, `Bulk On B {runId}-041`, `Bulk Off D {runId}-041` dalam container scrollable, body "Deactivating these fields will hide them and their data from all user forms. You can reactivate them later. Are you sure you want to deactivate them?", serta tombol `[Cancel]` dan `[Deactivate]`
85. Verifikasi tombol `[Deactivate]` bergaya danger (merah)
86. Klik `[Deactivate]`
87. Verifikasi muncul toast sukses: "Success, custom field has been deactivated."
88. Verifikasi `Bulk On A {runId}-041` dan `Bulk On B {runId}-041` berstatus Inactive
89. Verifikasi `Bulk Off D {runId}-041` tetap Inactive
90. Klik icon Changelog, pilih filter Action `Deactivate`, Search `{runId}-041`, tekan Enter
91. Verifikasi Changelog memuat tepat 2 entri Deactivate (`Bulk On A {runId}-041` dan `Bulk On B {runId}-041`)
92. Tutup modal Changelog dengan `[✕]`
93. Buka Global Settings > User > User List (sub-tab Login User), klik `[+ User]`, perhatikan section Custom Field dinamis
94. Verifikasi section Custom Field dinamis form Create User memuat field `Cost Center`
95. Verifikasi form Create User tidak memuat field `Bulk On A {runId}-041` dan `Bulk On B {runId}-041`
96. Tutup popup lewat `[✕]`
97. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
98. Verifikasi Detail User Rahmat Hidayat menampilkan `Employee Grade` dengan nilai `Grade 5`
99. Verifikasi Detail User Rahmat Hidayat tidak menampilkan field `Bulk On A {runId}-041`
100. Buka Global Settings > User > Custom Field

### TC-GS-UCF-343: Bulk Deactivate beroperasi atas seluruh seleksi termasuk baris yang tersaring keluar

101. Ketik Search `Filt`, tekan Enter
102. Centang `Filt Keep A {runId}-041`, `Filt Keep B {runId}-041`, dan `Filt Other {runId}-041`
103. Ganti isi kotak search dengan `Filt Other`, tekan Enter (hanya satu baris tampil)
104. Verifikasi counter Bulk Action Bar tetap `3 custom fields selected`
105. Klik `Bulk Action` > `Deactivate`
106. Verifikasi dialog `Deactivate Custom Fields` memuat 3 bullet: `Filt Keep A {runId}-041`, `Filt Keep B {runId}-041`, `Filt Other {runId}-041`
107. Klik `[Deactivate]`
108. Klik `(←)` pada kotak Search, lalu ketik Search `Filt`, tekan Enter
109. Verifikasi `Filt Keep A {runId}-041`, `Filt Keep B {runId}-041`, dan `Filt Other {runId}-041` berstatus Inactive
110. Klik icon Changelog, pilih filter Action `Deactivate`, Search `Filt`, tekan Enter
111. Verifikasi Changelog memuat 3 entri Deactivate (`Filt Keep A {runId}-041`, `Filt Keep B {runId}-041`, `Filt Other {runId}-041`)
112. Tutup modal Changelog dengan `[✕]`, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-346: Klik ganda [Activate] pada dialog Bulk Activate hanya memproses satu batch

113. Ketik Search `Bulk Dbl On`, tekan Enter
114. Centang `Bulk Dbl On A {runId}-041` dan `Bulk Dbl On B {runId}-041`
115. Klik `Bulk Action` > `Activate`
116. Klik `[Activate]` dua kali cepat
117. Verifikasi hanya 1 toast sukses yang tampil: "Success, custom field has been activated."
118. Klik icon Changelog, pilih filter Action `Activate`, Search `Bulk Dbl On`, tekan Enter
119. Verifikasi Changelog memuat tepat 1 entri Activate per field (`Bulk Dbl On A {runId}-041` dan `Bulk Dbl On B {runId}-041`)
120. Tutup modal Changelog dengan `[✕]`, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-347: Klik ganda [Deactivate] pada dialog Bulk Deactivate hanya memproses satu batch

121. Tunggu toast dari langkah 117 hilang otomatis
122. Ketik Search `Bulk Dbl Off`, tekan Enter
123. Centang `Bulk Dbl Off A {runId}-041` dan `Bulk Dbl Off B {runId}-041`
124. Klik `Bulk Action` > `Deactivate`
125. Klik `[Deactivate]` dua kali cepat
126. Verifikasi hanya 1 toast sukses yang tampil: "Success, custom field has been deactivated."
127. Klik icon Changelog, pilih filter Action `Deactivate`, Search `Bulk Dbl Off`, tekan Enter
128. Verifikasi Changelog memuat tepat 1 entri Deactivate per field (`Bulk Dbl Off A {runId}-041` dan `Bulk Dbl Off B {runId}-041`)
129. Tutup modal Changelog dengan `[✕]`, klik `(←)` pada kotak Search, lalu ubah page size kembali menjadi 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (129 langkah). Seluruhnya satu kelas (Bulk Activate dan Bulk Deactivate pada satu dataset: Bulk Action Bar dan dialognya). Blok TC-GS-UCF-168, 164, 167 hanya membaca 14 field Pre-setup dan Population; blok sesudahnya memakai field milik sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain, kecuali TC-GS-UCF-166 yang memakai `Bulk On A` dan `Bulk On B` yang diaktifkan TC-GS-UCF-165 (rantai yang disebut TC sumber: "hasil TC sebelumnya"). Jumlah langkah muncul dari satu baris per aksi dan satu `Verifikasi` per klausa Expected, serta dari TC-GS-UCF-165 dan 166 yang memeriksa Changelog, form Create User, dan Detail User.
- Urutan TC dalam spec: 168, 164, 167 (tiga TC yang mengandalkan total tepat 14 baris), seeding Data Dinamis (langkah 31), lalu 481, 482, 483, 165, 166, 343, 346, 347. TC-GS-UCF-343 ditempatkan sesudah 166 supaya `Verifikasi` jumlah entri Deactivate pada TC-GS-UCF-166 (langkah 91) tidak ikut menghitung entri `Filt`. Urutan menyimpang dari urutan TC sumber (164 sampai 168, 481 sampai 483, 343, 346, 347).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 52 (page size 25 untuk TC yang mensyaratkannya; TC-GS-UCF-168 menyebut "Page size 25" pada Precondition), langkah 10, 19, 31, 41, 51, 63, 80, 100, 112, 120, 129 (membersihkan seleksi, Search, atau state, atau kembali ke tab Custom Field), langkah 14 dan 17 (menutup overlay dan mengganti seleksi), langkah 32, 42, 64, 81, 101, 113, 122 (Search agar baris target tampil), langkah 77, 92, 96 (menutup modal atau popup), dan langkah 121 (menunggu toast sukses lama hilang otomatis supaya hitungan toast pada langkah 126 hanya memuat toast hasil klik ganda).
- Asersi tambahan di luar Expected TC (S-03): langkah 8 dan 9 (TC-GS-UCF-168 butir b hanya menyebut "[Cancel] menutup dialog tanpa perubahan"; dipecah menjadi tidak ada toast dan dialog tertutup), langkah 94 dan 98 (anchor pembanding `Cost Center` dan `Employee Grade` untuk asersi absence), langkah 76 (TC-GS-UCF-165 butir d "tidak ada entri untuk C"; anchor positif adalah langkah 75), dan langkah 71 (TC-GS-UCF-165 butir f).
- Changelog memakai filter Action dan Search `{runId}-041` pada langkah 74 dan 90 (bukan `Bulk On` dan `Bulk O` seperti TC) karena entri Changelog bersifat permanen dan nama tanpa suffix cocok dengan run sebelumnya; suffix bernilai digit run saja sehingga baseline nol. Search `Bulk On` pada langkah 64 mencocokkan juga `Bulk One On` dan `Bulk One Off`; baris target dicentang berdasarkan nama lengkap.
- Pembagian TC lintas spec: TC-GS-UCF-143 (Select All) ada di spec 042 dan TC-GS-UCF-147 (dialog Bulk Delete) di spec 044.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi: TC-GS-UCF-165 dan 166 ("efek ke User, Non-Login User, My Profile, FA > Settings > User, AC > Settings > User, AC > Settings > Group popup Total User Detail, Import"; hanya form Create User dan Detail User yang punya Expected) serta "nilai User tersimpan" TC-GS-UCF-166.
  - TC-GS-UCF-164, 167, 168, 481, 482, dan 483 mengasumsikan total tepat 14 baris pada page size 25 atau Search tersendiri, sedangkan Data Dinamis spec yang sama menambah baris; spec men-seed Data Dinamis sesudah blok yang bergantung pada 14 baris (langkah 31). Mekanisme seeding oleh tim FE/BE.
  - TC-GS-UCF-166 menyebut `Bulk On A, B, C` berstatus Active sebagai hasil TC sebelumnya (TC-GS-UCF-165); spec menjalankan keduanya berurutan.
  - TC-GS-UCF-343 menyebut Search `Filt Other` dan nama field tanpa suffix; spec memakai versi bersuffix `{runId}-041` pada bullet dan asersi status.
  - Mekanisme seeding nilai Custom Field pada User (`Back`) tidak didefinisikan di TC, PRD, atau LLD sehingga ditulis sebagai kemampuan tim FE/BE.
  - TC-GS-UCF-483 menyebut "Klik icon Search" sebagai langkah dan Search `Bulk Act`; spec menulisnya atomik "Ketik Search `Bulk Act`, tekan Enter" (langkah 53) karena TC tidak menguji siklus input Search (konvensi bagian 8b butir 9).
