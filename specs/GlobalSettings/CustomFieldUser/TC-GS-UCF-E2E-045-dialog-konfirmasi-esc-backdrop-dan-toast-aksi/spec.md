---
id: TC-GS-UCF-E2E-045-dialog-konfirmasi-esc-backdrop-dan-toast-aksi
title: "Dialog Konfirmasi Aksi: Esc, Klik Backdrop, dan Perilaku Toast (Posisi, Auto-dismiss, Error Persist, Penggantian)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-410
  - TC-GS-UCF-411
  - TC-GS-UCF-488
  - TC-GS-UCF-489
  - TC-GS-UCF-490
  - TC-GS-UCF-491
coverage:
  web: automated
---

# Dialog Konfirmasi Aksi: Esc, Klik Backdrop, dan Perilaku Toast (Posisi, Auto-dismiss, Error Persist, Penggantian)

## Prerequisites

- Mode: FE+BE (backend nyata). Intercept jaringan parsial di atas backend nyata dipakai hanya sebagai pemicu pada blok TC-GS-UCF-490 (P-2).
- Suite serial (`parallel: false`): spec ini mengubah status Custom Field milik sendiri dan bergantung pada toast global yang tidak boleh bertumpuk dengan spec lain.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; langkah tidak mengulang pembukaan layar.
- Akun aktor: Total Control Client A `Sari Dewi` (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (hanya dibaca; semua dialog atasnya ditutup tanpa konfirmasi sehingga record dan Last Updated tidak berubah, pengecualian S-06): `Cost Center` (Active), `Bonus` (Active), dan `Joining Date` (Inactive) dari 14 Custom Field yang di-seed idempotent oleh hook `before` lewat API (disediakan tim FE/BE; dilewati bila sudah ada).
- Data Dinamis (di-seed lewat API di hook `before`, bersuffix per run; fixture baru `Fixture.customFieldUser.dialogToast045`):
  - `Toast Probe {runId}-045`: Text; Active (TC-GS-UCF-489).
  - `Toast Err Probe {runId}-045`: Text; Active (TC-GS-UCF-490).
  - `Toast Seq A {runId}-045` dan `Toast Seq B {runId}-045`: Text; Active (TC-GS-UCF-491).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): lepas intercept yang masih terpasang; hapus lewat API semua Custom Field bersuffix `{runId}-045`; reset sort tabel; dismiss toast yang tersisa.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: penekanan tombol `Esc`; klik di area backdrop di luar dialog; pengamatan posisi toast (kanan bawah layar) dan jumlah toast; `Spectra.intercept()` untuk memaksa respons 500 pada request ubah status Custom Field (PATCH status) milik `Toast Err Probe {runId}-045` (TC-GS-UCF-490) lalu melepasnya; menunggu 4 detik (TC-GS-UCF-489), 2 detik (TC-GS-UCF-491), dan 10 detik (TC-GS-UCF-490) nyata (jeda pendek, kurang dari 30 detik, sesuai TC).
- State global: sort tabel diatur pada langkah 1 dan dipulihkan pada langkah akhir; flag Guided Tooltip diatur hook suite.

## Test Steps

### TC-GS-UCF-488: Esc pada dialog konfirmasi (single dan bulk) menutup dialog setara [Cancel]

1. Urutkan tabel berdasarkan Field Name ascending
2. Matikan switch Active baris `Cost Center`
3. Verifikasi dialog `Deactivate Custom Field` tampil
4. Tekan Esc
5. Verifikasi tidak ada toast
6. Verifikasi dialog tertutup
7. Verifikasi switch `Cost Center` kembali On
8. Nyalakan switch Active baris `Joining Date`
9. Verifikasi dialog `Activate Custom Field` tampil
10. Tekan Esc
11. Verifikasi tidak ada toast
12. Verifikasi dialog tertutup
13. Verifikasi switch `Joining Date` tetap Off
14. Klik `⋯` pada baris `Cost Center`, pilih `Delete`
15. Verifikasi dialog `Delete Custom Field` tampil
16. Tekan Esc
17. Verifikasi tidak ada toast
18. Verifikasi dialog tertutup
19. Verifikasi baris `Cost Center` tetap ada di tabel
20. Centang `Cost Center` dan `Joining Date`, klik `Bulk Action` > `Deactivate`
21. Verifikasi dialog `Deactivate Custom Fields` tampil
22. Tekan Esc
23. Verifikasi tidak ada toast
24. Verifikasi dialog tertutup
25. Verifikasi seleksi 2 baris tetap
26. Verifikasi Bulk Action Bar tetap tampil
27. Klik `Bulk Action` > `Activate`
28. Verifikasi dialog `Activate Custom Fields` tampil
29. Tekan Esc
30. Verifikasi tidak ada toast
31. Verifikasi dialog tertutup
32. Verifikasi seleksi 2 baris tetap
33. Verifikasi Bulk Action Bar tetap tampil
34. Klik `Bulk Action` > `Delete`
35. Verifikasi dialog `Delete Custom Fields` tampil
36. Tekan Esc
37. Verifikasi tidak ada toast
38. Verifikasi dialog tertutup
39. Verifikasi `Cost Center` berstatus Active dan tetap ada di tabel
40. Verifikasi `Joining Date` berstatus Inactive dan tetap ada di tabel
41. Klik `(✕)` pada Bulk Action Bar

### TC-GS-UCF-410: Klik backdrop tidak menutup dialog Deactivate, Activate, dan Delete single

42. Matikan switch Active baris `Cost Center`
43. Klik backdrop di luar dialog
44. Verifikasi dialog `Deactivate Custom Field` tetap tampil
45. Klik `[Cancel]`
46. Verifikasi dialog tertutup
47. Verifikasi switch `Cost Center` tetap On
48. Nyalakan switch Active baris `Joining Date`
49. Klik backdrop di luar dialog
50. Verifikasi dialog `Activate Custom Field` tetap tampil
51. Klik `[Cancel]`
52. Verifikasi dialog tertutup
53. Verifikasi switch `Joining Date` tetap Off
54. Klik `⋯` pada baris `Cost Center`, pilih `Delete`
55. Klik backdrop di luar dialog
56. Verifikasi dialog `Delete Custom Field` tetap tampil
57. Klik `[Cancel]`
58. Verifikasi dialog tertutup
59. Verifikasi baris `Cost Center` tetap ada di tabel

### TC-GS-UCF-411: Klik backdrop tidak menutup dialog Deactivate, Activate, dan Delete bulk

60. Centang baris `Cost Center` dan `Bonus`, klik `Bulk Action` > `Deactivate`
61. Klik backdrop di luar dialog
62. Verifikasi dialog `Deactivate Custom Fields` tetap tampil
63. Klik `[Cancel]`
64. Verifikasi dialog tertutup
65. Verifikasi `Cost Center` dan `Bonus` tetap Active
66. Hapus centang `Bonus` dan centang `Joining Date` (seleksi: `Cost Center` dan `Joining Date`), klik `Bulk Action` > `Activate`
67. Klik backdrop di luar dialog
68. Verifikasi dialog `Activate Custom Fields` tetap tampil
69. Klik `[Cancel]`
70. Verifikasi dialog tertutup
71. Verifikasi `Joining Date` tetap Inactive
72. Klik `Bulk Action` > `Delete`
73. Klik backdrop di luar dialog
74. Verifikasi dialog `Delete Custom Fields` dengan bullet `Cost Center` dan `Joining Date` tetap tampil
75. Klik `[Cancel]`
76. Verifikasi dialog tertutup
77. Verifikasi `Cost Center` dan `Joining Date` tetap ada di tabel
78. Klik `(✕)` pada Bulk Action Bar

### TC-GS-UCF-489: Toast sukses Deactivate tampil di kanan bawah dan hilang otomatis setelah 4 detik

79. Ketik Search `Toast Probe {runId}-045`, tekan Enter
80. Matikan switch Active baris `Toast Probe {runId}-045`, klik `[Deactivate]`
81. Verifikasi toast "Success, custom field has been deactivated." tampil
82. Verifikasi toast tampil di kanan bawah layar
83. Tunggu 4 detik sejak toast muncul tanpa menutupnya
84. Verifikasi toast hilang otomatis tanpa dismiss manual

### TC-GS-UCF-491: Toast baru menggantikan toast sebelumnya tanpa bertumpuk

85. Ganti isi kotak search dengan `Toast Seq`, tekan Enter
86. Matikan switch Active baris `Toast Seq A {runId}-045`, klik `[Deactivate]`
87. Verifikasi 1 toast "Success, custom field has been deactivated." tampil di kanan bawah layar
88. Dalam 2 detik sejak toast pertama muncul, matikan switch Active baris `Toast Seq B {runId}-045`, klik `[Deactivate]`
89. Verifikasi hanya 1 toast "Success, custom field has been deactivated." tampil; toast baru menggantikan toast sebelumnya dan tidak bertumpuk
90. Verifikasi `Toast Seq A {runId}-045` berstatus Inactive
91. Verifikasi `Toast Seq B {runId}-045` berstatus Inactive

### TC-GS-UCF-490: Toast error aksi tulis tidak hilang otomatis

92. Ganti isi kotak search dengan `Toast Err Probe {runId}-045`, tekan Enter
93. Pasang intercept pada request ubah status Custom Field (PATCH status): respons 500
94. Matikan switch Active baris `Toast Err Probe {runId}-045`, klik `[Deactivate]`
95. Verifikasi toast error "Error, failed to deactivate custom field." tampil di kanan bawah layar
96. Lepas intercept pada request ubah status Custom Field
97. Tunggu 10 detik tanpa menutup toast
98. Verifikasi toast masih tampil dan tidak hilang otomatis
99. Dismiss toast, klik `(←)` pada kotak Search, lalu pulihkan sort tabel ke default (klik menu sidebar Global Settings > User > Custom Field)

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (99 langkah). Seluruhnya satu topik (perilaku dialog konfirmasi dan toast aksi tulis pada tabel yang sama dengan akun yang sama). Blok TC-GS-UCF-488, 410, dan 411 hanya membaca `Cost Center`, `Bonus`, dan `Joining Date` (dialog dibatalkan) dan blok TC-GS-UCF-489, 491, dan 490 memakai field milik sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain. Jumlah langkah muncul dari satu `Verifikasi` per klausa Expected pada enam skenario dialog di TC-GS-UCF-488 dan dari TC-GS-UCF-410 dan 411.
- P-2 (pemicu bukan objek uji): respons 500 yang dipaksa pada TC-GS-UCF-490 (langkah 93) hanya memicu toast error yang diuji (tidak hilang otomatis); objek uji adalah perilaku toast, bukan kegagalan server. Intercept dilepas segera sesudah toast error tampil (langkah 96, S-09).
- Urutan TC dalam spec: 488, 410, 411 (tanpa mutasi), lalu 489, 491, 490. Urutan menyimpang dari urutan TC sumber (410, 411, 488, 489, 490, 491). Urutan 491 sebelum 490 mengikuti kebutuhan field; keduanya tidak berpengaruh satu sama lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Sort Field Name ascending agar `Cost Center`, `Bonus`, dan `Joining Date` berada pada halaman 1; lihat Temuan untuk QA), langkah 41 dan 78 (membersihkan seleksi), langkah 79, 85, dan 92 (Search agar baris target tampil), langkah 83 dan 97 (menunggu), langkah 93 dan 96 (memasang dan melepas intercept), dan langkah 99 (dismiss toast dan memulihkan state tabel).
- Absence toast: langkah 5, 11, 17, 23, 30, 37 diletakkan segera sesudah `Esc` dan sebelum asersi dialog tertutup karena toast adalah state sementara (butir 5 dan 11 konvensi 8b); dialog yang tampil pada langkah 3, 9, 15, 21, 28, 35 menjadi anchor positif.
- Temuan untuk QA:
  - TC-GS-UCF-410, 411, 488 mengandalkan `Cost Center`, `Bonus`, dan `Joining Date` berada pada halaman 1 tanpa menyebut urutan default; spec mengurutkan Field Name ascending (langkah 1).
  - TC-GS-UCF-488 butir f menyebut `Cost Center` berstatus Active dan `Joining Date` Inactive "tetap ada di tabel" tanpa Search; spec mengasersi keduanya pada langkah 39 dan 40.
  - TC-GS-UCF-489, 490, dan 491 memakai durasi 4 detik, 10 detik, dan 2 detik yang ditandai `PRD?` (tidak ditemukan verbatim di PRD); spec mengikuti nilai TC.
  - TC-GS-UCF-489, 491 memakai Post Condition "efek ke User, Non-Login User, My Profile, FA > Settings > User, AC > Settings > User, AC > Settings > Group popup Total User Detail, Import" tanpa langkah observasi; tidak diasersi.
  - TC-GS-UCF-490 memaksa respons 500 pada backend nyata (intercept parsial) sehingga tetap `FE+BE` (bukan `Mode: mock`); TC tidak menyebut endpoint, spec menyebutnya "request ubah status Custom Field (PATCH status)" mengikuti teks Langkah TC "respons PATCH status 500".
  - TC-GS-UCF-410 dan 411 tidak menyebut cara mengklik backdrop (area spesifik); spec menulis "klik backdrop di luar dialog" sesuai TC.
