---
id: TC-FA-FAAC-E2E-167-log-request-api-langsung-tiga-surface
title: "Log Request API Langsung Assign, Move, Unassign, Create, Edit, dan Delete pada Tiga Surface"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-552
  - TC-FA-FAAC-553
  - TC-FA-FAAC-554
  - TC-FA-FAAC-608
  - TC-FA-FAAC-609
  - TC-FA-FAAC-610
sourceRules: ["J-05", "L-06", "§8.2#p1", "§8.2#r1", "§8.3#p1", "L-08", "§8.4#r7", "L-07", "§8.4#r6", "L-01", "§4.1.1#r32", "L-02", "L-04", "L-05"]
smoke: []
dependsOn: []
trace:
  "J-05": [6, 10, 13, 20, 34, 47, 60, 73]
  "L-06": [6, 7, 11, 14]
  "§8.2#p1": [10, 24, 38, 51, 64, 77]
  "§8.2#r1": [11, 25, 39, 52, 65, 78]
  "§8.3#p1": [13, 14, 27, 28, 41, 42, 54, 55, 67, 68, 80, 81]
  "L-08": [20, 21, 25, 28]
  "§8.4#r7": [20, 24, 27]
  "L-07": [34, 35, 39, 42]
  "§8.4#r6": 34
  "L-01": [47, 48, 52, 55]
  "§4.1.1#r32": [48, 61, 74]
  "L-02": [60, 61, 65, 68]
  "L-04": [60, 61, 65, 68]
  "L-05": [73, 74, 78, 81]
coverage:
  web: automated
---

# Log Request API Langsung Assign, Move, Unassign, Create, Edit, dan Delete pada Tiga Surface

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class Active `Light Vehicles` (`LT-VEH`); Asset Name tanpa Asset Class `Hand Truck`, serta `Utility Cart 2` dan `Roller Cart 2` (masing-masing 0 aset aktif); Asset Class Active `Machinery` (`MACHINERY`); `B-FREE15` Active tanpa Asset Name; `B-DEL6` tanpa Asset Name dan belum pernah diposting.
- Keadaan awal `LT-VEH` per blok (fixture BE, diatur oleh langkah penyetel di awal blok): TC-552 tanpa Asset Name dengan `Hand Truck` tanpa Asset Class; TC-553 memiliki `Utility Cart 2`; TC-554 memiliki `Roller Cart 2`.
- Kemampuan baca log yang disediakan tim FE/BE: jumlah entri Changelog, System Log aktor, dan Activity Log FAMS dibaca tepat sebelum aksi pemicu tiap TC (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- Kemampuan teknis: klien HTTP/fixture BE untuk request langsung ke server sebagai pemanggil terotorisasi (Total Control) tanpa melewati browser; akun pemanggil tidak tertulis di TC sehingga memakai akun aktor spec ini.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: Hand Truck, Utility Cart 2, dan Roller Cart 2 kembali ke keadaan seed; B-API1 dihapus; B-FREE15 kembali Active dengan Class Name seed; B-DEL6 dibuat ulang.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-552: Request API langsung Assign dicatat di tiga surface (J-05)

1. Buka Fixed Asset > Settings > Accounting > tab Asset Class
2. Pulihkan lewat fixture BE: `LT-VEH` tanpa Asset Name dan `Hand Truck` tanpa Asset Class (precondition TC-552, tidak diasersi)
3. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
4. Lewat fixture BE kirim permintaan Assign `Hand Truck` ke `LT-VEH` sebagai pemanggil terotorisasi tanpa UI hingga tersimpan
5. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
6. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
7. Verifikasi baris teratas Changelog: Action `Edit`, Field `Asset Names`, Old Value `—`, New Value `Hand Truck`
8. Tutup modal Changelog
9. Buka Global Settings > User > Detail User milik aktor > Tab System Log
10. Verifikasi jumlah entri System Log bertambah tepat 1 dari Ns
11. Verifikasi baris teratas System Log: Action `Edit`, Object `Asset Class`, Name `LT-VEH`, Field `Asset Names`, Old Value `—`, New Value `Hand Truck`
12. Buka Activity Log FAMS
13. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari Na
14. Verifikasi baris teratas Activity Log: Action `Edit`, Object `Asset Class`, Name `LT-VEH`, Field `Asset Names`, Old Value `—`, New Value `Hand Truck`

### TC-FA-FAAC-553: Request API langsung Move dicatat di tiga surface (J-05)

15. Buka Fixed Asset > Settings > Accounting > tab Asset Class
16. Pulihkan lewat fixture BE: `LT-VEH` memiliki Asset Name `Utility Cart 2` (precondition TC-553, tidak diasersi)
17. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
18. Lewat fixture BE kirim permintaan Move `Utility Cart 2` dari `LT-VEH` ke `MACHINERY` sebagai pemanggil terotorisasi tanpa UI hingga tersimpan
19. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
20. Verifikasi jumlah entri Changelog bertambah tepat 2 dari Nc
21. Verifikasi dua entri L-08 pada Changelog: asal `LT-VEH` (Old Value `Utility Cart 2`, New Value `—`) dan tujuan `MACHINERY` (Old Value `—`, New Value `Utility Cart 2`)
22. Tutup modal Changelog
23. Buka Global Settings > User > Detail User milik aktor > Tab System Log
24. Verifikasi jumlah entri System Log bertambah tepat 2 dari Ns
25. Verifikasi dua entri L-08 pada System Log: asal `LT-VEH` dan tujuan `MACHINERY` untuk `Utility Cart 2`
26. Buka Activity Log FAMS
27. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari Na
28. Verifikasi dua entri L-08 pada Activity Log: asal `LT-VEH` dan tujuan `MACHINERY` untuk `Utility Cart 2`

### TC-FA-FAAC-554: Request API langsung Unassign dicatat di tiga surface (J-05)

29. Buka Fixed Asset > Settings > Accounting > tab Asset Class
30. Pulihkan lewat fixture BE: `LT-VEH` memiliki Asset Name `Roller Cart 2` (precondition TC-554, tidak diasersi)
31. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
32. Lewat fixture BE kirim permintaan Unassign `Roller Cart 2` dari `LT-VEH` sebagai pemanggil terotorisasi tanpa UI hingga tersimpan
33. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
34. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
35. Verifikasi baris teratas Changelog: entri L-07 dengan Old Value `Roller Cart 2`, New Value `—`
36. Tutup modal Changelog
37. Buka Global Settings > User > Detail User milik aktor > Tab System Log
38. Verifikasi jumlah entri System Log bertambah tepat 1 dari Ns
39. Verifikasi baris teratas System Log: entri L-07 dengan Old Value `Roller Cart 2`, New Value `—`
40. Buka Activity Log FAMS
41. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari Na
42. Verifikasi baris teratas Activity Log: entri L-07 dengan Old Value `Roller Cart 2`, New Value `—`

### TC-FA-FAAC-608: Request API langsung Create tercatat pada tiga surface

43. Buka Fixed Asset > Settings > Accounting > tab Asset Class
44. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
45. Lewat fixture BE kirim permintaan Create Asset Class `B-API1` sebagai pemanggil terotorisasi tanpa UI hingga tersimpan
46. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
47. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
48. Verifikasi baris teratas Changelog: Action `Create`, Class Code `B-API1`, Field `Class Code`, New Value `B-API1`, Modified By `Rina W`
49. Tutup modal Changelog
50. Buka Global Settings > User > Detail User milik aktor > Tab System Log
51. Verifikasi jumlah entri System Log bertambah tepat 1 dari Ns
52. Verifikasi baris teratas System Log: Action `Create`, Object `Asset Class`, Name `B-API1`
53. Buka Activity Log FAMS
54. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari Na
55. Verifikasi baris teratas Activity Log: Action `Create`, Object `Asset Class`, Name `B-API1`, Modified By `Rina W`

### TC-FA-FAAC-609: Request API langsung Edit dan Deactivate tercatat pada tiga surface

56. Buka Fixed Asset > Settings > Accounting > tab Asset Class
57. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
58. Lewat fixture BE kirim permintaan Edit Class Name dan Deactivate untuk `B-FREE15` sebagai pemanggil terotorisasi tanpa UI hingga tersimpan
59. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
60. Verifikasi jumlah entri Changelog bertambah tepat 2 dari Nc
61. Verifikasi dua baris teratas Changelog untuk `B-FREE15`: Edit Field `Class Name` dan Edit Field `Status` (Old Value `Active`, New Value `Inactive`), Modified By `Rina W`
62. Tutup modal Changelog
63. Buka Global Settings > User > Detail User milik aktor > Tab System Log
64. Verifikasi jumlah entri System Log bertambah tepat 2 dari Ns
65. Verifikasi dua baris teratas System Log untuk `B-FREE15`: Edit Field `Class Name` dan Edit Field `Status`
66. Buka Activity Log FAMS
67. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari Na
68. Verifikasi dua baris teratas Activity Log untuk `B-FREE15`: Edit Field `Class Name` dan Edit Field `Status`, Modified By `Rina W`

### TC-FA-FAAC-610: Request API langsung Delete tercatat pada tiga surface

69. Buka Fixed Asset > Settings > Accounting > tab Asset Class
70. Catat jumlah entri Changelog (Nc), System Log aktor (Ns), dan Activity Log FAMS (Na) sebagai baseline lewat kemampuan baca log
71. Lewat fixture BE kirim permintaan Delete untuk `B-DEL6` sebagai pemanggil terotorisasi tanpa UI hingga tersimpan
72. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
73. Verifikasi jumlah entri Changelog bertambah tepat 1 dari Nc
74. Verifikasi baris teratas Changelog: Action `Delete`, Class Code `B-DEL6`, Field `Class Code`, Old Value `B-DEL6`, New Value `—`, Modified By `Rina W`
75. Tutup modal Changelog
76. Buka Global Settings > User > Detail User milik aktor > Tab System Log
77. Verifikasi jumlah entri System Log bertambah tepat 1 dari Ns
78. Verifikasi baris teratas System Log: Action `Delete`, Object `Asset Class`, Name `B-DEL6`
79. Buka Activity Log FAMS
80. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari Na
81. Verifikasi baris teratas Activity Log: Action `Delete`, Object `Asset Class`, Name `B-DEL6`, Modified By `Rina W`

## Notes

1. K-1: TC kelas a (TC-552 sampai 554 dan 608 sampai 610) yang Expected-nya berupa pencatatan hasil request API langsung tetap masuk spec FE+BE walau tumpang tindih dengan TC backend; TC granular tetap sumber dan satu TC tepat satu spec. Request dikirim lewat klien HTTP/fixture BE (bagian 8b butir 1); yang diasersi UI hanya isi tiga surface log, bukan pengalihan halaman atau toast.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 3 dan awal tiap blok TC (kembali ke layar awal, langkah penyetel keadaan awal `LT-VEH` pada tiga blok pertama, dan baseline log).
3. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC lewat kemampuan baca log. Entri baru dibaca pada baris teratas urutan default Date terbaru sesudah selisih jumlah dari baseline dibuktikan (S-14); bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
4. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
5. Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah karena blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) yang tidak dihitung menurut bagian 3 smell; semua TC satu topik dan tiap blok TC berdiri sendiri dengan seed dan baseline sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
6. Temuan untuk QA: (a) TC-552 sampai 554 dan 608 sampai 610 tidak menyebut status respons permintaan; spec tidak mengasersi status respons karena TC tidak memberinya. (b) TC-608 dan TC-609 tidak menyebut payload Create dan nilai Class Name baru; spec memakai nilai fixture. (c) Pemanggil terotorisasi tidak disebut akunnya; spec memakai akun aktor.
