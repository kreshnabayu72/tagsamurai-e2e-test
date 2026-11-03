---
id: TC-AC-ACHA-E2E-017-form-allocate-validasi-field
title: "Form Allocate Device: Validasi Field Wajib, Quantity, Notes, dan Pay From dengan Submit Diblokir"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHA-95
  - TC-AC-ACHA-96
  - TC-AC-ACHA-97
  - TC-AC-ACHA-98
  - TC-AC-ACHA-99
  - TC-AC-ACHA-101
  - TC-AC-ACHA-102
  - TC-AC-ACHA-103
  - TC-AC-ACHA-104
  - TC-AC-ACHA-105
  - TC-AC-ACHA-106
  - TC-AC-ACHA-107
  - TC-AC-ACHA-108
  - TC-AC-ACHA-109
  - TC-AC-ACHA-110
  - TC-AC-ACHA-111
  - TC-AC-ACHA-112
  - TC-AC-ACHA-113
coverage:
  web: automated
---

# Form Allocate Device: Validasi Field Wajib, Quantity, Notes, dan Pay From dengan Submit Diblokir

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji:

| Kode | Role | Pre-setup | Email | Env var password |
|---|---|---|---|---|
| A-01 | Total Control Principal `PT ABC` (Admin Pratama) | #21 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| A-04 | Total Control Partner `CV Karya Mandiri` | #46 | `totalControlPartner2_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_TC_P2_PASSWORD` |

- Login A-01 di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (A-01, `AC_TC_PASSWORD`) dan memulihkan seed lewat fixture Pre-setup #20 (Lampiran A butir A-6). Ganti akun ke A-04 dengan langkah logout dan login eksplisit. Env var `AC_DA_TC_P2_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example` (didaftarkan tahap script); password tidak ditulis di spec.
- Data Pre-setup: Client #10 `PT Manufaktur Unggul` (A-01) dan Pre-setup Client `PT Cipta Kreasi` #9 (A-04); kantong #18 dan #19 CV Karya Mandiri dengan dua kantong sumber (untuk TC-99).
- Data Dinamis: satu alokasi dibuat di TC-112 (Category NFC, Client `PT Manufaktur Unggul`, Quantity 2, Notes `  Batch uji+{runId}-017  ` dengan dua spasi di awal dan akhir). Efek: kuota NFC Client `PT Manufaktur Unggul` bertambah 2; modul tanpa Delete sehingga alokasi tidak dihapus; fixture Pre-setup #20 di hook `after` membatalkan transaksi ber-Notes bersuffix `{runId}` itu dan memulihkan seed 30 baris (Lampiran A butir A-6). Nilai Notes 360 dan 361 karakter berupa huruf `a` diulang.
- Kemampuan baca state BE (disediakan tim FE/BE): jumlah transaksi pengirim dan Reserved kantong, dicatat sebagai baseline di hook `before` dan sebelum tiap submit yang diblokir.
- Kemampuan teknis: mengetik karakter satu per satu dan menempel (paste) teks ke field Quantity; fixture API Pre-setup #20 disediakan tim FE/BE.
- Hook suite: flag Guided Tooltip, sesi API aktor, fixture API Pre-setup #20, pemulihan preferensi Setup Column, dan seed 30 baris dinyatakan di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### Akun A-01 Principal: Field wajib kosong (TC-AC-ACHA-95, TC-AC-ACHA-113, TC-AC-ACHA-96, TC-AC-ACHA-97, TC-AC-ACHA-98)

1. Catat baseline jumlah transaksi pengirim lewat kemampuan baca state BE
2. Klik `[+ Allocation]`
3. Klik `[Submit]` tanpa mengisi apa pun
4. Verifikasi pesan inline "Category must not be empty" tampil
5. Verifikasi pesan inline "Client recipient must not be empty" tampil bersamaan
6. Verifikasi pesan inline "Quantity must not be empty" tampil bersamaan
7. Verifikasi form tetap terbuka
8. Verifikasi tidak ada transaksi baru (jumlah transaksi sama dengan baseline)
9. Verifikasi `[Submit]` tetap enabled
10. Pilih Category `TAG - NFC`
11. Verifikasi pesan "Category must not be empty" hilang
12. Pilih Client `PT Manufaktur Unggul`
13. Verifikasi pesan "Client recipient must not be empty" hilang
14. Verifikasi pesan "Quantity must not be empty" tetap tampil
15. Klik `[Clear Field]`
16. Pilih Client `PT Manufaktur Unggul` dan isi Quantity `5`
17. Klik `[Submit]` tanpa memilih Category
18. Verifikasi pesan "Category must not be empty" tampil di bawah field Category
19. Verifikasi tidak ada pesan error lain pada field Client dan Quantity
20. Verifikasi tidak ada transaksi baru (jumlah transaksi sama dengan baseline)
21. Klik `[Clear Field]`
22. Pilih Category `TAG - NFC` dan isi Quantity `5`
23. Klik `[Submit]` tanpa memilih Client
24. Verifikasi pesan "Client recipient must not be empty" tampil di bawah field Client
25. Verifikasi tidak ada pesan error lain pada field Category dan Quantity
26. Verifikasi tidak ada transaksi baru (jumlah transaksi sama dengan baseline)
27. Klik `[Clear Field]`
28. Pilih Category `TAG - NFC` dan Client `PT Manufaktur Unggul`
29. Klik `[Submit]` tanpa mengisi Quantity
30. Verifikasi pesan "Quantity must not be empty" tampil di bawah field Quantity
31. Verifikasi tidak ada pesan error lain pada field Category dan Client
32. Verifikasi tidak ada transaksi baru (jumlah transaksi sama dengan baseline)

### Quantity: real-time dan batas (TC-AC-ACHA-101 sampai TC-AC-ACHA-108)

33. Isi Quantity `0`, lalu pindah fokus dengan Tab
34. Verifikasi pesan inline real-time "Quantity must be a positive whole number" tampil
35. Verifikasi `[Submit]` disabled
36. Kosongkan field Quantity, ketik `1-2.5e` pada field Quantity
37. Verifikasi nilai field Quantity menjadi `125` (ketikan `-`, `.`, dan `e` diblokir)
38. Kosongkan field Quantity, tempel `12abc3` pada field Quantity
39. Verifikasi nilai yang ditempel dibersihkan dari karakter non-digit sehingga nilai field Quantity menjadi `123`
40. Verifikasi tidak ada pesan error pada Quantity
41. Ganti isi Quantity dengan `1`
42. Verifikasi tidak ada pesan error pada Quantity
43. Verifikasi `[Submit]` enabled
44. Ganti isi Quantity dengan `1000000`
45. Verifikasi tidak ada pesan error pada Quantity (nilai tepat 1.000.000 diterima)
46. Verifikasi `[Submit]` enabled
47. Ganti isi Quantity dengan `1000001`, lalu pindah fokus dengan Tab
48. Verifikasi pesan inline real-time "Quantity must not exceed 1,000,000" tampil
49. Verifikasi `[Submit]` disabled
50. Kosongkan field Quantity, lalu pindah fokus dengan Tab
51. Isi Quantity `999999999999999` (15 digit), lalu pindah fokus dengan Tab
52. Verifikasi pesan inline "Quantity must not exceed 1,000,000" tampil
53. Verifikasi pesan "Max. 15 characters" tidak tampil
54. Verifikasi `[Submit]` disabled
55. Ganti isi Quantity dengan `1000000000000000` (16 digit), lalu pindah fokus dengan Tab
56. Verifikasi pesan inline real-time "Max. 15 characters" tampil menggantikan pesan batas atas
57. Verifikasi `[Submit]` disabled
58. Ganti isi Quantity dengan `0`, lalu pindah fokus dengan Tab
59. Verifikasi pesan "Quantity must be a positive whole number" tampil
60. Ganti isi Quantity dengan `7`
61. Verifikasi pesan error Quantity hilang setelah nilai diperbaiki
62. Verifikasi `[Submit]` kembali enabled

### Notes (TC-AC-ACHA-109, TC-AC-ACHA-110, TC-AC-ACHA-111)

63. Isi Notes dengan 360 karakter, lalu pindah fokus dengan Tab
64. Verifikasi tidak ada pesan error pada Notes
65. Ganti isi Notes dengan 361 karakter, lalu pindah fokus dengan Tab
66. Verifikasi pesan inline real-time "Max. 360 characters" tampil di bawah Notes
67. Ganti isi Notes dengan `Kirim <b>cepat</b> & "uji" 😀`
68. Verifikasi tidak ada pesan error karakter tidak valid pada Notes
69. Verifikasi teks Notes tampil apa adanya di field

### Akun A-04 Partner dua kantong: Pay From wajib dipilih (TC-AC-ACHA-99)

70. Klik `[×]`
71. Verifikasi dialog Unsaved Changes tampil
72. Klik `[Leave]`
73. Logout, lalu login sebagai A-04 (`CV Karya Mandiri`), buka Allocation > Device Allocation
74. Catat baseline jumlah transaksi pengirim dan Reserved kedua kantong lewat kemampuan baca state BE
75. Klik `[+ Allocation]`
76. Pilih Category `TAG - NFC`, Client `PT Cipta Kreasi`, isi Quantity `5`
77. Klik `[Submit]` tanpa memilih Pay From
78. Verifikasi pesan "Pay from must not be empty" tampil di bawah field Pay From
79. Verifikasi tidak ada pesan error lain pada field Category, Client, dan Quantity
80. Verifikasi tidak ada transaksi baru (jumlah transaksi sama dengan baseline)
81. Verifikasi tidak ada Reserve (Reserved kedua kantong sama dengan baseline)
82. Klik `[×]`
83. Verifikasi dialog Unsaved Changes tampil
84. Klik `[Leave]`

### Akun A-01 Principal: Notes di-trim saat disimpan (TC-AC-ACHA-112), submit sukses di akhir

85. Logout, lalu login sebagai A-01, buka Allocation > Device Allocation
86. Klik `[+ Allocation]`
87. Pilih Category `TAG - NFC`, Client `PT Manufaktur Unggul`, isi Quantity `2`
88. Isi Notes `  Batch uji+{runId}-017  ` (dua spasi di awal dan akhir), lalu klik `[Submit]`
89. Tunggu aksi selesai
90. Catat Allocation ID baris teratas List sebagai Dynamic Reference transaksi baru
91. Klik Allocation ID itu untuk membuka modal Allocation Log
92. Verifikasi entri `Allocation created` memuat baris `Notes: Batch uji+{runId}-017` tanpa spasi di tepi
93. Tutup modal Allocation Log

## Notes

- Mode FE+BE; sumber `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan spec di atas sekitar 35 langkah (93 langkah bernomor kontinu 1 sampai 93; blok Notes, Pay From, dan Notes di-trim memakai nomor 63 sampai 93): semua blok satu topik (validasi form Allocate Device) dan satu kelas; semua `Verifikasi` mengikuti S-01 per klausa, dan tiap blok (field wajib, Quantity, Notes, Pay From, Notes di-trim) berdiri sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain. Satu-satunya aksi yang membuat data adalah submit sukses TC-112 di akhir (prinsip 7).
- Penyimpangan urutan (S-10): urutan TC dikelompokkan menurut keadaan form yang berkelanjutan: TC-113 mengikuti TC-95 pada form yang sama (tiga pesan error masih tampil); TC-96, TC-97, dan TC-98 memakai `[Clear Field]` di antaranya (S-09) sehingga status validasi direset; TC-101 sampai TC-108 memakai satu form dengan Category dan Client terisi dari TC-98; TC-99 (akun A-04) dan TC-112 (submit sukses, akun A-01) dipisah di akhir karena beda akun (prinsip "ganti akun eksplisit").
- Langkah penghubung (S-03): `[Clear Field]` di antara TC, pemakaian Tab untuk "pindah fokus", pengosongan field Quantity sebelum ketik atau tempel (termasuk pengosongan dan Tab antara TC-105 dan TC-106 pada langkah 50 supaya pesan batas atas dari TC-105 tidak tersisa saat TC-106 diasersi, R-12), penutupan form dirty lewat `[×]`, dialog Unsaved Changes, `[Leave]`, logout dan login ganti akun, serta "Tunggu aksi selesai" sebelum membuka Allocation Log. Asersi tambahan "pesan Quantity 0 tampil" sebelum memperbaiki nilai (TC-108) memberi anchor positif untuk asersi hilangnya pesan.
- Langkah 90 menangkap Allocation ID baris teratas List (urutan Last Updated terbaru) sebagai Dynamic Reference transaksi baru sebelum modal dibuka (S-14); langkah 91 membuka modal lewat ID itu.
- "Tidak ada transaksi baru" diasersi lewat kemampuan baca state BE (baseline jumlah transaksi), bukan dengan menutup form, supaya form tetap terbuka untuk TC berikutnya.
- caseType `Negative` dipertahankan: 17 dari 18 TC sumber adalah validasi yang menolak input dan memblokir Submit; hanya TC-112 di akhir yang berujung submit sukses.
- Pengecualian S-12 nama literal: nama Client Pre-setup literal (sudah ada di environment); Notes TC-112 bersuffix per run.
- Temuan untuk QA:
  - TC-95 Expected b ("kekosongan field wajib dievaluasi saat Submit") adalah penjelasan perilaku, bukan observasi terpisah selain `[Submit]` tetap enabled.
  - TC-101, TC-105, dan TC-106 menulis "pindah fokus" tanpa menyebut target fokus; spec memakai Tab.
  - TC-102 menyebut "tempel" tanpa cara; spec memakai kemampuan tempel teks dari clipboard.
  - TC-109 dan TC-110 menyebut "Notes: 360/361 karakter" tanpa isi; spec memakai huruf `a`.
  - TC-112 Expected b ("Panjang Notes dihitung setelah trim") tidak punya langkah observasi di TC (tidak ada Data Uji panjang batas); tidak diasersi terpisah. Post Condition "Transaksi baru berstatus Completed" tidak punya langkah observasi dan tidak diasersi.
