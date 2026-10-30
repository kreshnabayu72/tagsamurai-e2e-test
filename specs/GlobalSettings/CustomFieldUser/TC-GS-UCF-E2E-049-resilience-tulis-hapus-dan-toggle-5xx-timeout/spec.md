---
id: TC-GS-UCF-E2E-049-resilience-tulis-hapus-dan-toggle-5xx-timeout
title: "Resilience Tulis Aksi: Delete, Bulk Delete, Toggle Active, dan Bulk Toggle saat Kegagalan Server 5xx atau Timeout"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UCF-138
  - TC-GS-UCF-341
  - TC-GS-UCF-154
  - TC-GS-UCF-547
  - TC-GS-UCF-161
  - TC-GS-UCF-162
  - TC-GS-UCF-486
  - TC-GS-UCF-487
  - TC-GS-UCF-172
  - TC-GS-UCF-550
  - TC-GS-UCF-348
  - TC-GS-UCF-549
coverage:
  web: automated
---

# Resilience Tulis Aksi: Delete, Bulk Delete, Toggle Active, dan Bulk Toggle saat Kegagalan Server 5xx atau Timeout

## Prerequisites

- Mode: mock. Seluruh API di-mock (dijalankan tim FE sebagai integration test, tanpa backend nyata); dasar: pengecualian resilience `Mode: mock` di `docs/e2e-conventions.md` bagian 6 (spec hanya mengasersi perilaku FE atas respons mock). Endpoint yang dipanggil halaman pada kondisi tes, rujukan `API/openapi.yaml` dan `API/low-level-design.md` modul (angka = nomor baris berkas), dan respons yang dipaksa:
  - Daftar Custom Field, `POST /v2/iam/user-custom-fields/list` (openapi.yaml:13, low-level-design.md:15): memuat baris Data Dinamis di bawah, ditambah 14 Custom Field Pre-setup dan Population sebagai latar; list selalu memuat seluruh baris karena tidak ada aksi tulis yang berhasil.
  - Request hapus Custom Field, `DELETE /v2/iam/user-custom-fields` dengan body `ids` (openapi.yaml:396, low-level-design.md:456; satu `id` untuk single dan beberapa `id` untuk bulk): respons 500 (TC-GS-UCF-138 dan 154) atau koneksi diputus tanpa respons (TC-GS-UCF-341 dan 547).
  - Request ubah status Custom Field, `PATCH /v2/iam/user-custom-fields/status` dengan body `ids` dan `isActive` (openapi.yaml:533, low-level-design.md:663; satu `id` untuk single dan beberapa `id` untuk bulk): respons 500 (TC-GS-UCF-161, 162, 172, 348) atau koneksi diputus tanpa respons (TC-GS-UCF-486, 487, 550, 549).
  - Endpoint modul lain pada openapi (`POST /v2/iam/user-custom-fields/options` openapi.yaml:89 dan low-level-design.md:93, `GET /v2/iam/user-custom-fields/used` openapi.yaml:243 dan low-level-design.md:274): respons normal bila halaman memanggilnya pada kondisi tes; apakah halaman memanggilnya dikonfirmasi tim FE.
  - SSE perubahan Custom Field: tidak ada di `openapi.yaml` maupun `low-level-design.md`; PRD (`custom-field-user.md:934`) menyatakan modul ini tidak mengirim event SSE, sehingga tidak ada event selama spec ini (stream, bila halaman berlangganan, disediakan tim FE).
  - API pendukung di luar sumber modul (identitas pengguna, menu, payload sesi dan izin Total Control agar switch Active, row action Delete, dan Bulk Action Bar tampil, flag Guided Tooltip, dan Detail User Rahmat Hidayat section Custom Fields untuk TC-GS-UCF-138) disediakan tim FE.
- Akun aktor: Total Control Client A `Sari Dewi` (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1) sebagai identitas sesi; sesi disediakan harness mock, tanpa login nyata dan tanpa password.
- Data Dinamis (hanya sebagai isi respons list mock, tidak ada data yang dibuat di backend; bersuffix per run; fixture baru `Fixture.customFieldUser.resilienceAction049`; seluruhnya Text, Active kecuali dinyatakan lain):
  - `Delete Fail {runId}-049` (nilai User Rahmat Hidayat = `Keep Me`; TC-GS-UCF-138), `Timeout Del {runId}-049` (TC-GS-UCF-341).
  - `Bulk Fail A {runId}-049`, `Bulk Fail B {runId}-049` (TC-GS-UCF-154); `Bulk Timeout Del A {runId}-049`, `Bulk Timeout Del B {runId}-049` (TC-GS-UCF-547).
  - `Toggle Fail {runId}-049` (Active; TC-GS-UCF-161), `Toggle Fail On {runId}-049` (Inactive; TC-GS-UCF-162), `Timeout Off {runId}-049` (Active; TC-GS-UCF-486), `Timeout On {runId}-049` (Inactive; TC-GS-UCF-487).
  - `Bulk 5xx A {runId}-049`, `Bulk 5xx B {runId}-049` (Active; TC-GS-UCF-172); `Bulk Timeout Off A {runId}-049`, `Bulk Timeout Off B {runId}-049` (Active; TC-GS-UCF-550); `Bulk 5xx On A {runId}-049`, `Bulk 5xx On B {runId}-049` (Inactive; TC-GS-UCF-348); `Bulk Timeout On A {runId}-049`, `Bulk Timeout On B {runId}-049` (Inactive; TC-GS-UCF-549).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): lepas semua intercept dan mock yang dipasang spec ini; dismiss toast yang masih ada.
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 500 dan memutus koneksi (request tanpa respons, tanpa perubahan status) pada request hapus dan ubah status, serta untuk melepasnya; muat ulang halaman (F5) tanpa dialog `beforeunload` (tidak ada form terbuka); pengamatan toast error yang tidak hilang otomatis; Search tabel.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`; pada mode mock flag ini termasuk API pendukung yang disediakan tim FE.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.

## Test Steps

### TC-GS-UCF-138: Delete single gagal 5xx mempertahankan data dan memberi toast error

1. Ketik Search `Delete Fail {runId}-049`, tekan Enter
2. Klik `⋯` pada baris `Delete Fail {runId}-049`, pilih `Delete`
3. Pasang intercept pada request hapus Custom Field: respons 500
4. Klik `[Delete]`
5. Verifikasi toast error: "Error, failed to delete custom field."
6. Verifikasi dialog Delete tetap terbuka
7. Verifikasi `[Delete]` kembali enabled untuk coba ulang
8. Lepas intercept, dismiss toast, lalu klik `[Cancel]` pada dialog
9. Verifikasi baris `Delete Fail {runId}-049` tetap ada di tabel
10. Buka Global Settings > User > Detail Rahmat Hidayat, section Custom Fields
11. Verifikasi Detail User Rahmat Hidayat menampilkan nilai `Keep Me` pada `Delete Fail {runId}-049`
12. Buka Global Settings > User > Custom Field

### TC-GS-UCF-341: Delete timeout mempertahankan data dan dialog untuk coba ulang

13. Ketik Search `Timeout Del {runId}-049`, tekan Enter
14. Klik `⋯` pada baris `Timeout Del {runId}-049`, pilih `Delete`
15. Pasang intercept pada request hapus Custom Field: koneksi diputus (tanpa respons)
16. Klik `[Delete]`
17. Verifikasi toast error `Connection problem. Please try again.`
18. Verifikasi toast error memuat tombol `[Try Again]`
19. Verifikasi dialog Delete tetap terbuka
20. Verifikasi `[Delete]` kembali enabled
21. Lepas intercept, dismiss toast, lalu klik `[Cancel]` pada dialog
22. Verifikasi baris `Timeout Del {runId}-049` tetap ada di tabel
23. Klik `(←)` pada kotak Search

### TC-GS-UCF-154: Bulk Delete gagal 5xx mempertahankan bar dan seleksi lalu me-refresh list

24. Ketik Search `Bulk Fail`, tekan Enter
25. Centang `Bulk Fail A {runId}-049` dan `Bulk Fail B {runId}-049`
26. Pasang intercept pada request hapus Custom Field: respons 500
27. Klik `Bulk Action` > `Delete`, klik `[Delete]`
28. Verifikasi toast error: "Error, failed to delete custom field."
29. Verifikasi Bulk Action Bar dipertahankan
30. Verifikasi seleksi dipertahankan
31. Verifikasi list di-refresh dan menampilkan kondisi terkini tiap item dari respons list
32. Lepas intercept, dismiss toast, klik `(✕)` pada Bulk Action Bar, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-547: Bulk Delete timeout mempertahankan bar dan seleksi serta memberi toast koneksi

33. Ketik Search `Bulk Timeout Del`, tekan Enter
34. Centang `Bulk Timeout Del A {runId}-049` dan `Bulk Timeout Del B {runId}-049`
35. Klik `Bulk Action` > `Delete`
36. Pasang intercept pada request hapus Custom Field: koneksi diputus (tanpa respons)
37. Klik `[Delete]` pada dialog
38. Verifikasi toast error `Connection problem. Please try again.`
39. Verifikasi toast error memuat tombol `[Try Again]`
40. Verifikasi Bulk Action Bar dan seleksi dipertahankan: counter `2 custom fields selected`
41. Lepas intercept (pulihkan koneksi), dismiss toast, lalu muat ulang halaman (F5)
42. Ketik Search `Bulk Timeout Del`, tekan Enter
43. Verifikasi `Bulk Timeout Del A {runId}-049` dan `Bulk Timeout Del B {runId}-049` tetap ada di tabel
44. Klik `(←)` pada kotak Search

### TC-GS-UCF-161: Deactivate gagal 5xx mengembalikan switch dan memberi toast error

45. Pasang intercept pada request ubah status Custom Field: respons 500
46. Ketik Search `Toggle Fail {runId}-049`, tekan Enter
47. Matikan switch Active baris `Toggle Fail {runId}-049`, klik `[Deactivate]`
48. Verifikasi toast error: "Error, failed to deactivate custom field."
49. Verifikasi switch `Toggle Fail {runId}-049` kembali On
50. Lepas intercept, dismiss toast

### TC-GS-UCF-162: Activate gagal 5xx mengembalikan switch dan memberi toast error

51. Pasang intercept pada request ubah status Custom Field: respons 500
52. Ganti isi kotak search dengan `Toggle Fail On {runId}-049`, tekan Enter
53. Nyalakan switch Active baris `Toggle Fail On {runId}-049`, klik `[Activate]`
54. Verifikasi toast error: "Error, failed to activate custom field."
55. Verifikasi switch `Toggle Fail On {runId}-049` kembali Off
56. Lepas intercept, dismiss toast

### TC-GS-UCF-486: Deactivate single timeout mengembalikan switch dan memberi toast koneksi

57. Ganti isi kotak search dengan `Timeout Off {runId}-049`, tekan Enter
58. Matikan switch Active baris `Timeout Off {runId}-049`
59. Pasang intercept pada request ubah status Custom Field: koneksi diputus (tanpa respons)
60. Klik `[Deactivate]`
61. Verifikasi toast error `Connection problem. Please try again.`
62. Verifikasi toast error memuat tombol `[Try Again]`
63. Verifikasi switch `Timeout Off {runId}-049` kembali On
64. Lepas intercept (pulihkan koneksi), dismiss toast, lalu muat ulang halaman (F5)
65. Ketik Search `Timeout Off {runId}-049`, tekan Enter
66. Verifikasi `Timeout Off {runId}-049` berstatus Active

### TC-GS-UCF-487: Activate single timeout mengembalikan switch dan memberi toast koneksi

67. Ganti isi kotak search dengan `Timeout On {runId}-049`, tekan Enter
68. Nyalakan switch Active baris `Timeout On {runId}-049`
69. Pasang intercept pada request ubah status Custom Field: koneksi diputus (tanpa respons)
70. Klik `[Activate]`
71. Verifikasi toast error `Connection problem. Please try again.`
72. Verifikasi toast error memuat tombol `[Try Again]`
73. Verifikasi switch `Timeout On {runId}-049` kembali Off
74. Lepas intercept (pulihkan koneksi), dismiss toast, lalu muat ulang halaman (F5)
75. Ketik Search `Timeout On {runId}-049`, tekan Enter
76. Verifikasi `Timeout On {runId}-049` berstatus Inactive
77. Klik `(←)` pada kotak Search

### TC-GS-UCF-172: Bulk Deactivate gagal 5xx mempertahankan bar dan seleksi

78. Ketik Search `Bulk 5xx A`, tekan Enter
79. Centang `Bulk 5xx A {runId}-049`
80. Ganti isi kotak search dengan `Bulk 5xx B`, tekan Enter
81. Centang `Bulk 5xx B {runId}-049`
82. Pasang intercept pada request ubah status Custom Field: respons 500
83. Klik `Bulk Action` > `Deactivate`, klik `[Deactivate]`
84. Verifikasi toast error: "Error, failed to deactivate custom field."
85. Verifikasi Bulk Action Bar dan seleksi dipertahankan
86. Verifikasi list di-refresh
87. Lepas intercept, dismiss toast, klik `(✕)` pada Bulk Action Bar, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-550: Bulk Deactivate timeout mempertahankan bar dan seleksi serta memberi toast koneksi

88. Ketik Search `Bulk Timeout Off`, tekan Enter
89. Centang `Bulk Timeout Off A {runId}-049` dan `Bulk Timeout Off B {runId}-049`
90. Klik `Bulk Action` > `Deactivate`
91. Pasang intercept pada request ubah status Custom Field: koneksi diputus (tanpa respons)
92. Klik `[Deactivate]` pada dialog
93. Verifikasi toast error `Connection problem. Please try again.`
94. Verifikasi toast error memuat tombol `[Try Again]`
95. Verifikasi Bulk Action Bar dan seleksi dipertahankan: counter `2 custom fields selected`
96. Lepas intercept (pulihkan koneksi), dismiss toast, lalu muat ulang halaman (F5)
97. Ketik Search `Bulk Timeout Off`, tekan Enter
98. Verifikasi `Bulk Timeout Off A {runId}-049` dan `Bulk Timeout Off B {runId}-049` tetap berstatus Active
99. Klik `(←)` pada kotak Search

### TC-GS-UCF-348: Bulk Activate gagal 5xx mempertahankan bar dan seleksi

100. Ketik Search `Bulk 5xx On A`, tekan Enter
101. Centang `Bulk 5xx On A {runId}-049`
102. Ganti isi kotak search dengan `Bulk 5xx On B`, tekan Enter
103. Centang `Bulk 5xx On B {runId}-049`
104. Pasang intercept pada request ubah status Custom Field: respons 500
105. Klik `Bulk Action` > `Activate`, klik `[Activate]`
106. Verifikasi toast error: "Error, failed to activate custom field."
107. Verifikasi Bulk Action Bar dan seleksi dipertahankan
108. Verifikasi list di-refresh
109. Lepas intercept, dismiss toast, klik `(✕)` pada Bulk Action Bar, lalu klik `(←)` pada kotak Search

### TC-GS-UCF-549: Bulk Activate timeout mempertahankan bar dan seleksi serta memberi toast koneksi

110. Ketik Search `Bulk Timeout On`, tekan Enter
111. Centang `Bulk Timeout On A {runId}-049` dan `Bulk Timeout On B {runId}-049`
112. Klik `Bulk Action` > `Activate`
113. Pasang intercept pada request ubah status Custom Field: koneksi diputus (tanpa respons)
114. Klik `[Activate]` pada dialog
115. Verifikasi toast error `Connection problem. Please try again.`
116. Verifikasi toast error memuat tombol `[Try Again]`
117. Verifikasi Bulk Action Bar dan seleksi dipertahankan: counter `2 custom fields selected`
118. Lepas intercept (pulihkan koneksi), dismiss toast, lalu muat ulang halaman (F5)
119. Ketik Search `Bulk Timeout On`, tekan Enter
120. Verifikasi `Bulk Timeout On A {runId}-049` dan `Bulk Timeout On B {runId}-049` tetap berstatus Inactive

## Notes

- Mode: mock. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness: fault injection / resilience (prinsip 13b), satu spec untuk seluruh aksi Delete, Bulk Delete, Toggle, dan Bulk Toggle (cara menggabung antar-aksi).
- Spec melewati sekitar 35 langkah (120 langkah). Seluruhnya satu kelas harness (fault injection pada aksi tulis), seluruhnya `Mode: mock` tanpa backend nyata, dan tiap blok memakai baris respons list mock sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain. Dua belas blok berpola sama (pasang intercept, pemicu aksi, asersi toast dan state UI, lepas intercept); jumlah langkah muncul dari satu baris per aksi dan satu `Verifikasi` per klausa Expected (toast dan `[Try Again]` dipecah).
- Urutan TC dalam spec: Delete (138, 341), Bulk Delete (154, 547), Toggle single (161, 162, 486, 487), Bulk Toggle (172, 550, 348, 549). Tidak ada aksi yang menghabisi data karena semua aksi gagal (tidak ada perubahan pada list mock).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search agar baris target tampil dan pembersihan Search lewat `(←)`; memasang dan melepas intercept; dismiss toast error (toast error tidak hilang otomatis sehingga di-dismiss sebelum blok berikutnya, S-09); muat ulang halaman pada blok timeout (hanya agar list mock dibaca ulang); dan langkah 12 (kembali ke tab Custom Field sesudah Detail User).
- Seleksi pada blok 172 dan 348 dilakukan dengan Search berganti per baris (langkah 78 sampai 81 dan 100 sampai 103) karena Search `Bulk 5xx A` dan `Bulk 5xx B` tidak mengelompokkan keduanya; seleksi dipertahankan lintas Search (TC-GS-UCF-144).
- Muat ulang pada blok timeout memenuhi Langkah TC "Pulihkan koneksi dan muat ulang halaman"; pada mode mock list yang dibaca ulang berasal dari respons mock sehingga asersi "tetap ada" atau "tetap berstatus ..." membaca mock, bukan state backend nyata.
- Temuan untuk QA:
  - Spec `Mode: mock` (pengecualian resilience, `docs/e2e-conventions.md` bagian 6) memuat asersi yang pada Expected TC mengasumsikan state backend: TC-GS-UCF-138 butir c (nilai `Keep Me` tetap di Detail User, langkah 10 sampai 12), TC-GS-UCF-154 (langkah 31), 172 (langkah 86), dan 348 (langkah 108) (list di-refresh dan menampilkan kondisi terkini tiap item dari server), serta butir "tetap ada" atau "tetap berstatus" setelah muat ulang di TC-GS-UCF-547 (langkah 43), 486 (66), 487 (76), 550 (98), 549 (120). Bagian 6 menetapkan asersi state server nyata dipecah ke TC FE+BE terpisah; pemecahan TC belum dikerjakan, sehingga langkah itu ditulis sesuai TC. Pada mock hanya perilaku UI terhadap respons mock yang teruji, state backend nyata tidak; langkah-langkah itu pindah ke spec FE+BE setelah QA memecah TC-nya.
  - Rujukan endpoint hapus (`DELETE /v2/iam/user-custom-fields`, bentuk bulk `ids`), ubah status, dan list diambil dari `openapi.yaml` dan `low-level-design.md` modul (S-13); SSE tidak ada di kedua sumber itu dan PRD menyatakan modul tidak mengirim event SSE.
  - TC-GS-UCF-138 dan 154 menyebut "Paksa respons DELETE 500" tanpa endpoint; TC-GS-UCF-161, 162, 172, dan 348 menyebut "respons PATCH status 500". Spec mengikuti istilah TC.
  - TC-GS-UCF-341 dan TC-GS-UCF-486/487 menyebut "Putuskan koneksi/timeout"; spec memakai intercept koneksi diputus tanpa respons. TC-GS-UCF-138 butir d meminta `[Delete]` enabled "diamati sebelum [Cancel]"; spec mengamatinya pada langkah 7 sebelum `[Cancel]` (langkah 8).
  - Post Condition tanpa langkah observasi di TC tidak diasersi, mis. "Delete Fail tetap ada di Detail User" selain yang ada di Expected.
  - TC-GS-UCF-138 sampai 549 memakai nama field tanpa suffix; spec memakai versi bersuffix `{runId}-049`.
  - Toast `Connection problem. Please try again.` dengan `[Try Again]`: spec tidak menekan `[Try Again]` karena tidak ada Expected untuknya.
