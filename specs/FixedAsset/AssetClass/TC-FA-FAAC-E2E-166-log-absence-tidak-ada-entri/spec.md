---
id: TC-FA-FAAC-E2E-166-log-absence-tidak-ada-entri
title: "Log Absence: Tidak Ada Entri untuk Aksi yang Dilewati, Ditolak, atau Gagal"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-538
  - TC-FA-FAAC-539
  - TC-FA-FAAC-540
  - TC-FA-FAAC-551
  - TC-FA-FAAC-578
sourceRules: ["L-04", "§8.4#r5", "E-FAAC-14", "§8.2#p1", "§8.2#r1", "§8.3#p1", "F-FAAC-02.k2", "E-FAAC-26", "F-FAAC-01.k1", "§4.2f#b2", "R-02", "R-09", "§7.3#b5", "L-06", "§4.1.1#r8", "S-13", "§4.1.3#p1", "§8.4#p3", "L-10", "L-11", "J-01", "J-02"]
smoke: []
dependsOn: []
trace:
  "L-04": [6, 7, 11, 12, 15, 16]
  "§8.4#r5": [6, 8, 13, 17]
  "E-FAAC-14": [8, 13, 17]
  "§8.2#p1": [11, 42, 92]
  "§8.2#r1": 12
  "§8.3#p1": [15, 16, 45, 88]
  "F-FAAC-02.k2": [23, 38, 42, 45]
  "E-FAAC-26": [23, 38]
  "F-FAAC-01.k1": 25
  "§4.2f#b2": 27
  "R-02": 32
  "R-09": 55
  "§7.3#b5": [55, 61]
  "L-06": 61
  "§4.1.1#r8": 73
  "S-13": [73, 77]
  "§4.1.3#p1": 76
  "§8.4#p3": [77, 81]
  "L-10": [88, 89]
  "L-11": [88, 89]
  "J-01": [89, 92]
  "J-02": [89, 92]
anchor: [37, 41, 44, 60, 80, 91]
coverage:
  web: automated
---

# Log Absence: Tidak Ada Entri untuk Aksi yang Dilewati, Ditolak, atau Gagal

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-FREE12` Active tanpa Asset Name dan `B-NAMES` Active dengan Asset Name; `B-ANCHOR` Active; Asset Class Active `Light Vehicles` (`LT-VEH`); Asset Name tanpa Asset Class `Hand Truck` (0 aset aktif), `Old Trailer` (0 aset aktif), dan `City Car`; `B-LOCK` dengan Last Posted Period Mar 2026.
- Keadaan awal `LT-VEH` per blok (fixture BE): blok TC-551 `LT-VEH` Active tanpa Asset Name dengan `Hand Truck` tanpa Asset Class; blok TC-578 `LT-VEH` memiliki `Old Trailer` dan `City Car` (kolom Asset Names = 2). Kedua keadaan diatur oleh langkah penyetel di awal blok masing-masing (langkah 47 dan 64).
- Nilai form Create valid (TC-540 menulis "semua field wajib" tanpa nilai; dipakai Data Uji TC-FA-FAAC-262): Class Code `B-ANCHOR` (duplikat sengaja); Class Name `Truck Equipment`; Method `Straight Line`; Useful Life `96`; Depreciation Start Convention `Full month from in-service date`; Tax Depreciation Class `Bukan bangunan – Kelompok 2`; Tax Method `Declining Balance`; Tax Depreciation Start Rule `Month of expenditure`.
- Kemampuan baca log yang disediakan tim FE/BE: jumlah entri Changelog, System Log aktor, dan Activity Log FAMS dibaca tepat sebelum aksi pemicu tiap TC (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Kemampuan teknis: `Spectra.intercept` parsial di atas backend nyata untuk respons 5xx; fixture BE untuk memicu seed posting dan export periode. Seluruhnya hanya pemicu kondisi yang diasersi tidak tercatat dan bukan objek uji (P-5 butir a).
- Jam server dan jam browser tidak digeser spec ini; bulan berjalan mengikuti zona waktu General Settings (NC-11).
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: B-FREE12 dan B-NAMES kembali Active; Old Trailer dibuat ulang dan ter-assign ke LT-VEH; B-LOCK kembali ke Last Posted Period Mar 2026 tanpa Last Exported Period; intercept respons 5xx dilepas.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-539: Aksi bulk menulis satu kejadian per Asset Class yang berhasil dan tidak mencatat yang dilewati

1. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
2. Centang `B-FREE12` dan `B-NAMES`, lalu pilih Bulk Action `Deactivate`
3. Klik `Continue` pada dialog konfirmasi
4. Tunggu aksi selesai
5. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
6. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
7. Verifikasi baris teratas Changelog tampil: Action `Edit`, Class Code `B-FREE12`, Field `Status`, Old Value `Active`, New Value `Inactive`
8. Verifikasi tidak ada entri baru Changelog untuk `B-NAMES` (satu-satunya entri baru milik `B-FREE12`)
9. Tutup modal Changelog
10. Buka Global Settings > User > Detail User milik aktor > Tab System Log
11. Verifikasi jumlah entri System Log bertambah tepat 1 dari Ns
12. Verifikasi baris teratas System Log tampil: Action `Edit`, Object `Asset Class`, Name `B-FREE12`, Field `Status`
13. Verifikasi tidak ada entri baru System Log untuk `B-NAMES`
14. Buka Activity Log FAMS
15. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari Na
16. Verifikasi baris teratas Activity Log tampil: Action `Edit`, Object `Asset Class`, Name `B-FREE12`, Field `Status`
17. Verifikasi tidak ada entri baru Activity Log untuk `B-NAMES`

### TC-FA-FAAC-540: Tidak ada entri log untuk Edit No-Op, validasi ditolak, dan kegagalan server

18. Buka Fixed Asset > Settings > Accounting > tab Asset Class
19. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
20. Klik link Class Code `B-ANCHOR` di tabel
21. Klik `Save` tanpa mengubah field apa pun
22. Tunggu aksi selesai
23. Verifikasi halaman kembali ke tabel Asset Class (No-Op Save kembali ke tabel, tabel Asset Class dan tombol `+ Asset Class` tampil)
24. Klik `+ Asset Class`, isi semua field wajib dengan nilai form valid (Prerequisites) dan Class Code duplikat `B-ANCHOR`, lalu klik `Submit`
25. Verifikasi error validasi Class Code duplikat tampil pada form
26. Klik breadcrumb `Asset Class` pada form Create
27. Verifikasi dialog `Unsaved Changes` tampil
28. Klik `[Leave]`
29. Klik link Class Code `B-ANCHOR` di tabel
30. Ubah Class Name menjadi `Log Gagal`
31. Siapkan respons 5xx untuk permintaan Save lewat `Spectra.intercept` parsial, lalu klik `Save`
32. Verifikasi toast error kegagalan server tampil
33. Lepas intercept respons 5xx
34. Kembalikan Class Name ke nilai tersimpan
35. Kembali ke tabel Asset Class lewat Breadcrumb
36. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
37. Verifikasi sedikitnya satu entri lain yang sudah ada tampil di Changelog
38. Verifikasi jumlah entri Changelog sama dengan Nc (tidak ada entri baru dari ketiga aksi)
39. Tutup modal Changelog
40. Buka Global Settings > User > Detail User milik aktor > Tab System Log
41. Verifikasi sedikitnya satu entri lain yang sudah ada tampil di System Log aktor
42. Verifikasi jumlah entri System Log sama dengan Ns
43. Buka Activity Log FAMS
44. Verifikasi sedikitnya satu entri lain yang sudah ada tampil di Activity Log FAMS
45. Verifikasi jumlah entri Activity Log sama dengan Na

### TC-FA-FAAC-551: Assign yang gagal karena error server tidak menulis entri log

46. Buka Fixed Asset > Settings > Accounting > tab Asset Class
47. Setel keadaan awal lewat fixture BE: `LT-VEH` Active tanpa Asset Name dan `Hand Truck` tanpa Asset Class (precondition TC-551, tidak diasersi)
48. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
49. Ketik Search `LT-VEH`, tekan Enter
50. Klik link Class Code `LT-VEH` di tabel
51. Klik tab `Asset Names`
52. Klik tombol `+ Assign Asset Names`
53. Centang `Hand Truck`
54. Siapkan respons 5xx untuk permintaan Assign lewat `Spectra.intercept` parsial, lalu klik `[Assign]`
55. Verifikasi toast error `Error, failed to assign asset name.` tampil
56. Lepas intercept respons 5xx
57. Klik `[Cancel]`
58. Klik kembali ke tabel Asset Class
59. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
60. Verifikasi sedikitnya satu entri lain yang sudah ada tampil di Changelog
61. Verifikasi tidak ada entri baru untuk `Hand Truck` (jumlah entri Changelog sama dengan Nc)
62. Tutup modal Changelog

### TC-FA-FAAC-578: Menghapus Asset Name yang ter-assign melepas penugasannya tanpa log Unassign

63. Buka Fixed Asset > Settings > Accounting > tab Asset Class
64. Pulihkan lewat fixture BE: `LT-VEH` memiliki Asset Name `Old Trailer` dan `City Car` (precondition TC-578, tidak diasersi)
65. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
66. Buka Settings > Asset Master > Asset Name
67. Ketik Search `Old Trailer`, tekan Enter
68. Hapus Asset Name `Old Trailer`
69. Klik `Delete` pada dialog konfirmasi
70. Tunggu aksi selesai
71. Kembali ke tabel Asset Class
72. Ketik Search `LT-VEH`, tekan Enter
73. Verifikasi baris `LT-VEH` menampilkan Asset Names = 1
74. Klik link Class Code `LT-VEH` di tabel
75. Klik tab `Asset Names`
76. Verifikasi Asset Name `City Car` tampil pada tab Asset Names
77. Verifikasi tab Asset Names tidak memuat `Old Trailer`
78. Kembali ke tabel Asset Class
79. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
80. Verifikasi sedikitnya satu entri lain yang sudah ada tampil di Changelog
81. Verifikasi tidak ada entri Changelog Unassign (L-07) untuk `Old Trailer` (jumlah entri Changelog sama dengan Nc)
82. Tutup modal Changelog

### TC-FA-FAAC-538: Last Posted dan Last Exported Period tanpa System Log

83. Buka Fixed Asset > Settings > Accounting > tab Asset Class
84. Catat jumlah entri System Log aktor (Ns) dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
85. Picu seed posting periode Apr 2026 dan export periode Mar 2026 untuk `B-LOCK` lewat fixture BE
86. Tunggu aksi selesai
87. Buka Activity Log FAMS
88. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari Na
89. Verifikasi dua baris teratas Activity Log: Field `Last Posted Period` dan Field `Last Exported Period` dengan Modified By `System`
90. Buka Global Settings > User > Detail User milik aktor > Tab System Log
91. Verifikasi sedikitnya satu entri lain yang sudah ada tampil di System Log aktor
92. Verifikasi tidak ada entri System Log baru untuk L-10 maupun L-11 (jumlah entri System Log sama dengan Ns)

## Notes

1. P-5 (butir a): spec absence ini memuat pemicu kelas b (respons 5xx pada TC-540 dan TC-551) dan fixture BE (seed posting dan export pada TC-538) yang hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC punya baseline dan data sendiri (S-12).
2. Pembagian TC lintas spec (S-05): TC-538 ada di spec 175 (entri L-10 dan L-11 pada Changelog dan Activity Log dengan Modified By `System`, aksi nyata dengan baseline sendiri) dan di spec ini (System Log tidak memuat entri L-10 dan L-11). TC-539, 540, 551, dan 578 hanya ada di spec ini. TC-164, 170, dan lain-lain yang menyebut "tanpa log" tidak dirujuk di sini.
3. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, langkah penyetel keadaan awal `LT-VEH` (langkah 47 dan 64), awal tiap blok TC (baseline log), langkah 49 dan 72 (Search kode `LT-VEH` untuk menemukan baris target, R-16: tabel Asset Class memuat lebih dari 25 baris), langkah 67 (Search `Old Trailer` di daftar Asset Name sebelum `Hapus`, R-16), langkah pengembalian Class Name dan langkah kembali ke layar awal (S-09), serta langkah "Tunggu aksi selesai" sesudah aksi tulis tanpa asersi langsung (konfirmasi `Continue`, `Save` tanpa perubahan, `Delete` Asset Name, dan pemicu fixture BE) sebelum membuka surface lain. Langkah 23 adalah `Verifikasi` halaman kembali ke tabel Asset Class: `Save` tanpa perubahan (No-Op) kembali ke tabel menurut TC-172, sehingga tidak ada klik breadcrumb di tabel.
4. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC lewat kemampuan baca log. Entri baru dibaca pada baris teratas urutan default Date terbaru sesudah selisih jumlah dari baseline dibuktikan (S-14); bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
5. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
6. Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah karena blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) yang tidak dihitung menurut bagian 3 smell; semua TC satu topik dan tiap blok TC berdiri sendiri dengan seed dan baseline sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
7. Anchor positif asersi absence (bagian 8b butir 2): baris Changelog, System Log, dan Activity Log yang sudah ada (anchor surface agregat) ditambah baris `B-FREE12` pada TC-539, Verifikasi pesan penolakan dan toast error server pada TC-540 dan TC-551, serta baris Activity Log `System` pada TC-538.
8. Temuan untuk QA: (a) TC-540 tidak menyebut teks error validasi Class Code duplikat atau teks toast kegagalan server; spec hanya mengasersi kemunculannya (S-02). (b) Expected b TC-538 menyebut "System Log setiap user" tetapi LK hanya membuka System Log aktor; spec mengasersi System Log aktor. (c) TC-578 tidak menyebut dialog konfirmasi Delete Asset Name; spec menulis `Delete` pada dialog. (d) TC-539 tidak menyebut Expected b untuk surface mana; spec mengasersi ketiganya.
