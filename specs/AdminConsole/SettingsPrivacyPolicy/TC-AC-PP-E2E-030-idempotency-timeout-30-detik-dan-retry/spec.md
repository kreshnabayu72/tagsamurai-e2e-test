---
id: TC-AC-PP-E2E-030-idempotency-timeout-30-detik-dan-retry
title: "Idempotency Publish: Timeout 30 Detik, Respons Dibuang atau Ditahan, dan Pengiriman Ulang"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PP-91
  - TC-AC-PP-203
  - TC-AC-PP-206
  - TC-AC-PP-213
  - TC-AC-PP-214
coverage:
  web: automated
---

# Idempotency Publish: Timeout 30 Detik, Respons Dibuang atau Ditahan, dan Pengiriman Ulang

## Prerequisites

- Mode: FE+BE (kelas b, fault injection: intercept parsial di atas backend nyata dan asersi state backend).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Andi Wijaya), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat A (Version 3 Active `John Doe` 10 Aug 2026 20:30 UTC, Version 2 `John Doe` 02 Jul 2026, Version 1 `Jane Smith` 15 Jan 2026 akun sudah dihapus). Hook `before` men-seed lewat Fixture BE; hook `after` mengembalikan ke Riwayat A. Riwayat versi append-only dan tidak dapat dihapus lewat UI, sehingga Fixture BE dipakai juga untuk mengembalikan dataset di antara blok TC (langkah penghubung).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC. Spec tidak mengubahnya.
- Kemampuan teknis:
  - Fixture BE untuk membuat ulang dataset Riwayat A.
  - `Spectra.intercept()` pada permintaan Publish dengan empat mode: (1) diteruskan ke server tetapi respons dibuang (TC-AC-PP-91, 203, 213, 214); (2) diteruskan ke server tetapi respons ditahan lebih dari 30 detik lalu dilepas (TC-AC-PP-206); (3) dijawab 500 tanpa diteruskan ke server (TC-AC-PP-214); (4) pengamatan isi permintaan keluar (idempotency key dan konten) tanpa mengubahnya. Intercept dilepas di langkah spec dan dipulihkan di hook `after` bila spec gagal di tengah.
  - Menunggu waktu nyata 30 detik (batas waktu FE) sebanyak 5 kali, satu per TC. Jam server dan jam browser tidak diatur.
  - Activity Log Admin Console dapat dibaca untuk menghitung entri `Publish`.
- Baseline log: sebelum aksi Publish tiap TC, spec mencatat jumlah entri `Publish` (Object `Privacy Policy`) dengan Name `Version 4` di Activity Log. Entri log tidak dihapus oleh Fixture BE, sehingga asersi memakai selisih terhadap baseline.
- Suite berjalan serial (`parallel: false`): dokumen Privacy Policy bersifat tunggal platform-wide dan spec ini mem-publish versi baru. Hook `after` memulihkan dataset ke Riwayat A.
- Tidak ada fixture file yang dibutuhkan; halaman dibuka lewat menu Settings > Privacy Policy.

## Test Steps

### TC-AC-PP-91: Retry Publish dengan idempotency key yang sama setelah timeout padahal publikasi pertama sudah tersimpan

1. Buka Admin Console > Activity Log dan catat jumlah entri dengan Action `Publish`, Object `Privacy Policy`, Name `Version 4` sebagai baseline B-91
2. Buka Settings > Privacy Policy
3. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`, tunggu konten termuat
4. Klik di akhir konten editor lalu ketik " Idempotent."
5. Klik `[Publish New Version]`
6. Pasang intercept pada permintaan Publish: permintaan diteruskan ke server, respons dibuang
7. Klik `[Publish]`
8. Tunggu batas waktu 30 detik tanpa respons sampai toast "Connection problem. Please try again." tampil dan Dialog Publish Confirm tertutup
9. Verifikasi toast "Connection problem. Please try again." tampil
10. Verifikasi toast tersebut tidak memuat tombol aksi
11. Verifikasi modal tetap di state Edit
12. Lepas intercept
13. Klik `[Publish New Version]`
14. Klik `[Publish]`
15. Verifikasi permintaan Publish kedua memakai idempotency key yang sama dengan permintaan pertama (diamati pada permintaan keluar yang tertangkap intercept)
16. Verifikasi permintaan Publish kedua memakai konten yang sama dengan permintaan pertama (diamati pada permintaan keluar yang tertangkap intercept)
17. Verifikasi server menjawab sukses seperti permintaan pertama
18. Verifikasi toast sukses "Success, Privacy Policy has been published." tampil
19. Verifikasi Dialog Publish Confirm tertutup
20. Verifikasi modal tertutup
21. Verifikasi tabel menampilkan `Version 4` berbadge `Active`
22. Verifikasi tidak ada `Version 5` di tabel
23. Buka Admin Console > Activity Log dan hitung entri `Publish`, Object `Privacy Policy`, Name `Version 4`
24. Verifikasi jumlah entri `Publish` untuk `Version 4` bertambah tepat 1 dari B-91

### TC-AC-PP-203: Mengubah konten setelah Publish pertama yang tidak diketahui hasilnya membuat permintaan baru dan versi tambahan

25. Kembalikan dataset ke Riwayat A lewat Fixture BE, lalu buka Settings > Privacy Policy
26. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`, tunggu konten termuat
27. Klik di akhir konten editor lalu ketik " First body."
28. Klik `[Publish New Version]`
29. Pasang intercept pada permintaan Publish: permintaan diteruskan ke server (Version 4 tersimpan), respons dibuang
30. Klik `[Publish]`
31. Tunggu batas waktu 30 detik sampai toast "Connection problem. Please try again." tampil tanpa tombol aksi, Dialog Publish Confirm tertutup, dan modal tetap di state Edit
32. Lepas intercept
33. Klik di akhir konten editor lalu ketik " Second body."
34. Klik `[Publish New Version]`
35. Klik `[Publish]`
36. Verifikasi toast sukses "Success, Privacy Policy has been published." tampil
37. Verifikasi tidak ada Dialog konteks konflik
38. Verifikasi tabel menampilkan `Version 5` (Active) dan `Version 4`
39. Klik teks tautan `Version 5`
40. Verifikasi konten `Version 5` memuat ` First body. Second body.`
41. Tutup modal View dengan `[✕]`
42. Klik teks tautan `Version 4`
43. Verifikasi konten `Version 4` memuat ` First body.` saja (tanpa ` Second body.`)
44. Tutup modal View dengan `[✕]`

### TC-AC-PP-206: Publish tanpa respons selama 30 detik menampilkan toast timeout tanpa tombol aksi, dan pengiriman ulang lewat [Publish New Version] memakai key yang sama

45. Kembalikan dataset ke Riwayat A lewat Fixture BE
46. Buka Admin Console > Activity Log dan catat jumlah entri `Publish`, Object `Privacy Policy`, Name `Version 4` sebagai baseline B-206
47. Buka Settings > Privacy Policy
48. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`, tunggu konten termuat
49. Klik di akhir konten editor lalu ketik " Slow network."
50. Klik `[Publish New Version]`
51. Pasang intercept pada permintaan Publish: permintaan diteruskan ke server, respons ditahan lebih dari 30 detik
52. Klik `[Publish]`
53. Verifikasi Dialog Publish Confirm tetap terbuka sebelum 30 detik
54. Verifikasi `[Publish]` disabled sebelum 30 detik
55. Verifikasi spinner tampil pada `[Publish]` sebelum 30 detik
56. Tunggu sampai lewat 30 detik tanpa respons
57. Verifikasi toast "Connection problem. Please try again." tampil
58. Verifikasi toast tersebut tidak memuat tombol aksi
59. Verifikasi toast "Error, failed to publish Privacy Policy." tidak tampil
60. Verifikasi Dialog Publish Confirm tertutup
61. Verifikasi modal tetap di state Edit
62. Verifikasi teks ` Slow network.` dipertahankan di editor
63. Lepas intercept sehingga respons yang tertahan dilepas
64. Verifikasi tidak ada toast baru yang tampil
65. Verifikasi tabel di belakang modal tidak berubah (tetap 3 baris Riwayat A)
66. Klik `[Publish New Version]` tanpa mengubah konten
67. Klik `[Publish]`
68. Verifikasi permintaan Publish memakai idempotency key yang sama dengan permintaan pertama (diamati pada permintaan keluar yang tertangkap intercept)
69. Verifikasi server menjawab sukses seperti permintaan pertama
70. Verifikasi toast sukses "Success, Privacy Policy has been published." tampil
71. Verifikasi Dialog Publish Confirm tertutup
72. Verifikasi modal tertutup
73. Verifikasi tabel menampilkan `Version 4` berbadge `Active`
74. Verifikasi tidak ada `Version 5` di tabel
75. Buka Admin Console > Activity Log dan hitung entri `Publish`, Object `Privacy Policy`, Name `Version 4`
76. Verifikasi jumlah entri `Publish` untuk `Version 4` bertambah tepat 1 dari B-206

### TC-AC-PP-213: Menutup modal setelah toast timeout tanpa kirim ulang me-refresh tabel yang kini memuat versi hasil publikasi pertama

77. Kembalikan dataset ke Riwayat A lewat Fixture BE, lalu buka Settings > Privacy Policy
78. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`, tunggu konten termuat
79. Klik di akhir konten editor lalu ketik " Closed after timeout."
80. Klik `[Publish New Version]`
81. Pasang intercept pada permintaan Publish: permintaan diteruskan ke server (Version 4 tersimpan), respons dibuang
82. Klik `[Publish]`
83. Tunggu batas waktu 30 detik sampai toast "Connection problem. Please try again." tampil dan Dialog Publish Confirm tertutup
84. Verifikasi toast "Connection problem. Please try again." tampil
85. Verifikasi toast tersebut tidak memuat tombol aksi
86. Verifikasi tabel di belakang modal belum menampilkan `Version 4`
87. Lepas intercept tanpa mengirim ulang
88. Klik `[✕]` di header modal
89. Verifikasi Dialog "Unsaved Changes" tampil
90. Klik `[Leave]`
91. Verifikasi modal tertutup
92. Verifikasi tabel Version History di-refresh menampilkan `Version 4` berbadge `Active` di baris teratas
93. Verifikasi tidak ada toast tambahan
94. Verifikasi tidak ada `Version 5` di tabel

### TC-AC-PP-214: Menutup modal setelah toast timeout dan pengiriman ulang yang gagal lagi tetap me-refresh tabel

95. Kembalikan dataset ke Riwayat A lewat Fixture BE, lalu buka Settings > Privacy Policy
96. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`, tunggu konten termuat
97. Klik di akhir konten editor lalu ketik " Resend failed."
98. Klik `[Publish New Version]`
99. Pasang intercept pada permintaan Publish: permintaan diteruskan ke server (Version 4 tersimpan), respons dibuang
100. Klik `[Publish]`
101. Tunggu batas waktu 30 detik sampai toast "Connection problem. Please try again." tampil dan Dialog Publish Confirm tertutup
102. Verifikasi toast "Connection problem. Please try again." tampil
103. Verifikasi toast tersebut tidak memuat tombol aksi
104. Verifikasi tabel di belakang modal belum menampilkan `Version 4`
105. Ganti intercept: permintaan Publish berikutnya dijawab 500 tanpa diteruskan ke server
106. Klik `[Publish New Version]`
107. Klik `[Publish]`
108. Verifikasi toast "Error, failed to publish Privacy Policy." tampil
109. Verifikasi Dialog Publish Confirm tertutup
110. Verifikasi modal tetap di state Edit
111. Verifikasi teks ` Resend failed.` dipertahankan di editor
112. Lepas intercept
113. Klik `[✕]` di header modal
114. Verifikasi Dialog "Unsaved Changes" tampil
115. Klik `[Leave]`
116. Verifikasi modal tertutup
117. Verifikasi tabel Version History di-refresh menampilkan `Version 4` berbadge `Active` di baris teratas
118. Verifikasi tidak ada `Version 5` di tabel

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`. Kelas harness: b (fault injection, timeout) dengan asersi state backend (versi dan log).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa awalan Verifikasi): langkah pembuka tiap blok TC-AC-PP-203, 206, 213, 214 (kembalikan dataset ke Riwayat A lewat Fixture BE, karena TC menetapkan dataset Riwayat A di awal tiap TC dan riwayat append-only); langkah menutup modal View bersih lewat `[✕]` di blok TC-AC-PP-203; langkah mencatat baseline Activity Log lalu kembali ke Settings > Privacy Policy di blok TC-AC-PP-91 dan 206. Penutupan modal dirty di blok TC-AC-PP-213 dan 214 mengikuti butir S-08: `✕`, verifikasi dialog `Unsaved Changes`, lalu `[Leave]` (TC hanya menulis "klik `[✕]` lalu klik `[Leave]`").
- Ukuran spec melewati sekitar 35 langkah karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Lima blok TC tidak saling bergantung karena dataset dikembalikan ke Riwayat A di awal tiap blok, sehingga kegagalan satu blok tidak membuat blok berikutnya tidak bermakna. Seluruh blok satu kelas (b) dan satu topik (idempotency key pada timeout); spec tidak dipecah.
- Urutan blok TC mengikuti urutan di sumber (91, 203, 206, 213, 214); tidak ada penyimpangan urutan.
- TC-AC-PP-92, 93, 202 (key bentrok 409) ada di spec `TC-AC-PP-E2E-031`; TC-AC-PP-94, 212 (masa berlaku key 24 jam) ada di spec `TC-AC-PP-E2E-032`.
- Temuan untuk QA:
  - Pengamatan "idempotency key yang sama" (TC-AC-PP-91 Expected b, TC-AC-PP-206 Expected d) tidak dapat dilihat lewat UI; TC dan `openapi.yaml` tidak menyebut nama header atau field key (NC-02 mencatat openapi belum memuat key). Spec mengasersi lewat permintaan keluar yang tertangkap intercept tanpa menulis nama header.
  - Post Condition TC-AC-PP-91, 203, 206, 213, 214 ("hanya satu record audit") sebagian punya padanan Expected (Activity Log di TC-AC-PP-91 dan 206) dan sebagian tidak (TC-AC-PP-203, 213, 214 hanya menyebut dua atau satu record audit tanpa langkah observasi di log); yang tanpa langkah observasi tidak diasersi.
  - TC-AC-PP-203 langkah 2 menyebut kondisi (toast, dialog tertutup, modal tetap di Edit) hanya di langkah, bukan di Expected; spec memperlakukannya sebagai syarat tunggu, bukan asersi.
  - Menunggu 30 detik nyata dilakukan 5 kali (±2,5 menit); TC tidak menyatakan cara mempersingkat batas waktu FE.
