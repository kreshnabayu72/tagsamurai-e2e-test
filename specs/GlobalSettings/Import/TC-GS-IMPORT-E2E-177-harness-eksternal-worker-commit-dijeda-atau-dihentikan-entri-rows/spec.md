---
id: TC-GS-IMPORT-E2E-177-harness-eksternal-worker-commit-dijeda-atau-dihentikan-entri-rows
title: "Harness eksternal worker commit: dijeda atau dihentikan (entri rows remaining, tanpa entri bila 0 terkomit, tulis-balik tidak jalan saat committing, 409 saat committing, job tanpa kemajuan 15 menit)"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-426
  - TC-GS-IMPORT-518
  - TC-GS-IMPORT-532
  - TC-GS-IMPORT-553
  - TC-GS-IMPORT-755
  - TC-GS-IMPORT-809
  - TC-GS-IMPORT-947
coverage:
  web: automated
---

# Harness eksternal worker commit: dijeda atau dihentikan (entri rows remaining, tanpa entri bila 0 terkomit, tulis-balik tidak jalan saat committing, 409 saat committing, job tanpa kemajuan 15 menit)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec melakukan commit sebagian nyata di Client E, mengubah state global (kontrol worker commit, penanda kemajuan job) dan Custom Field Client E, serta Changelog Import Client E bersifat permanen sehingga asersi memakai baseline; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client E dibuka hook `beforeEach`.
- Pelaku kedua (pemicu): Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTE_TC2_PASSWORD`, memakai sesi API untuk menghapus opsi `Siang` dari Custom Field `Shift` (TC-518) dan menjadikan `Shift Notes` Required (TC-947); tidak ada sesi UI kedua karena hasil di sesi itu tidak diasersi (P-2).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; TC-426, 518, 532, 553, 755, 809, 947 tidak merujuk D-47 pada beberapa baris kolom D-ref tetapi membutuhkannya):
  - Kontrol worker commit D-47: mode 1 (dijeda sebelum job mulai) untuk TC-518 dan TC-947; mode 3 (dijeda setelah batch pertama selesai, 100 baris terkomit, tidak dijalankan lagi selama blok) untuk TC-426, 532, 553, 809; mode 6 (dihentikan sebelum batch pertama selesai, tidak ada baris terkomit) untuk TC-755; hook membaca jumlah percobaan pelanjutan job.
  - Fixture timestamp kemajuan job: memundurkan penanda kemajuan job 16 menit (dua kali); penanda dihitung di server dan tidak diamati lewat countdown UI sehingga jam browser tidak diubah dan jeda tidak ditunggu secara nyata.
  - Margin jam (8b.3): batas job tanpa kemajuan 15 menit, penanda dimundurkan 16 menit sehingga margin 1 menit. Cara hitung: penanda kemajuan baru = penanda kemajuan semula dikurangi 16 menit, dibaca dan ditulis lewat fixture timestamp; usia tanpa kemajuan = 16 menit ditambah waktu nyata yang berjalan sesudah fixture, sehingga usia hanya bertambah dan selalu lebih dari 15 menit. Spec tidak mengasersi keadaan di bawah 15 menit, jadi margin 1 menit tidak dapat menghasilkan lulus semu.
  - Hook umur draft D-76 varian 1 (>=24 jam; `created_at` dimundurkan 25 jam) agar Unsaved Banner dan `[Discard]` tampil.
  - Klien HTTP yang mengirim request langsung ke server dengan token sesi Total Control Client E (Upload File pada TC-532, Discard Draft pada TC-809); asersi hanya respons server dan state data (butir 1 bagian 8b).
  - Skrip fixture inspeksi data: membaca status tersimpan baris draft (TC-518, 947).
  - Skrip fixture reset Client E (D-47: hapus draft, lanjutkan worker, hapus Brand hasil batch pertama, pulihkan Custom Field `Shift` dan `Shift Notes`, reset hasil commit terakhir) dan seeding draft.
  - Jeda nyata: polling "muat ulang setiap 5 detik" menunggu job latar belakang (batas tunggu 2 sampai 5 menit sesuai TC), bukan menunggu jam.
- Baseline log (S-12): total entri Changelog Import dengan Filter Action `Import Brand` dicatat sebelum aksi pemicu (TC-426, 755); asersi memakai selisih terhadap baseline, bukan posisi atau angka absolut.
- Data Dinamis (milik spec ini; draft dibuang dan hasil commit batch pertama dihapus oleh reset):
  - D-56 `brand-250-impor.csv`: `Brand Impor 001` sampai `Brand Impor 250`, semua valid dan unik (TC-426, 755).
  - D-34 `brand-250.csv`: `Brand 001` sampai `Brand 250`, semua valid dan unik (TC-532, 553, 809); `brand-6.csv`: header `Brand Name`; Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp (TC-532).
  - D-54 draft User Login 8 baris `pending` di Client E (Shift `Siang` pada Row # 1 dan 2; TC-518, 947); Custom Field `Shift` (Dropdown: Pagi, Siang, Malam) dan `Shift Notes` (Text Area, opsional dan kosong pada seluruh baris) Pre-setup Client E, dipulihkan oleh reset (Kontrak Fixture R2).
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): lanjutkan worker commit, kembalikan penanda kemajuan job, pulihkan opsi `Siang` dan flag opsional `Shift Notes`, hapus draft Client E, hapus 100 Brand hasil batch pertama, reset hasil commit terakhir, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-755: Commit yang berhenti tanpa satu pun baris terkomit tidak menulis entri ringkasan

1. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
2. Muat ulang halaman Import > Brand
3. Klik `[Changelog]` di header halaman, terapkan Filter Action = `Import Brand`, catat angka total pada teks Pagination (Showing [From] - [To] of [N] items; 0 bila yang tampil adalah empty state) sebagai baseline, lalu tutup modal Changelog
4. Aktifkan kontrol worker commit mode 6 (dihentikan sebelum batch pertama selesai; tidak dijalankan lagi) dan pencatat jumlah percobaan pelanjutan job
5. Klik `[Import (250)]`
6. Tunggu aksi selesai (permintaan mendapat respons)
7. Mundurkan penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
8. Baca jumlah percobaan pelanjutan pada kontrol worker commit setiap 5 detik sampai bernilai 1 (batas tunggu 5 menit)
9. Verifikasi jumlah percobaan pelanjutan pada kontrol worker commit bernilai 1
10. Mundurkan lagi penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
11. Muat ulang halaman Import > Brand setiap 5 detik sampai `[Discard]` Enabled (batas tunggu 5 menit)
12. Verifikasi `[Discard]` Enabled (job kembali `draft`)
13. Verifikasi kartu Total Rows tetap 250 (tidak ada baris terkomit)
14. Klik `[Changelog]` di header halaman, terapkan Filter Action = `Import Brand`, dan baca angka total pada teks Pagination
15. Verifikasi modal `Changelog: Import` terbuka
16. Verifikasi total pada Pagination Changelog Import dengan Filter Action `Import Brand` sama dengan baseline langkah 3

### TC-GS-IMPORT-426: Entri commit yang berhenti dengan sebagian baris terkomit memakai format rows remaining

17. Tutup modal Changelog, lalu reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
18. Muat ulang halaman Import > Brand
19. Klik `[Changelog]` di header halaman, terapkan Filter Action = `Import Brand`, catat angka total pada teks Pagination sebagai baseline, lalu tutup modal Changelog
20. Aktifkan kontrol worker commit mode 3 (dijeda setelah batch pertama selesai; tidak dijalankan lagi) dan pencatat jumlah percobaan pelanjutan job
21. Klik `[Import (250)]`
22. Tunggu aksi selesai (permintaan mendapat respons)
23. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
24. Verifikasi kartu Total Rows menampilkan 150
25. Mundurkan penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
26. Baca jumlah percobaan pelanjutan pada kontrol worker commit setiap 5 detik sampai bernilai 1 (batas tunggu 5 menit)
27. Verifikasi jumlah percobaan pelanjutan pada kontrol worker commit bernilai 1
28. Mundurkan lagi penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
29. Muat ulang halaman Import > Brand setiap 5 detik sampai `[Discard]` Enabled (batas tunggu 5 menit)
30. Verifikasi `[Discard]` Enabled (job kembali `draft`)
31. Klik `[Changelog]` di header halaman, terapkan Filter Action = `Import Brand`, dan baca angka total pada teks Pagination
32. Verifikasi total pada Pagination Changelog Import dengan Filter Action `Import Brand` bertambah tepat satu dibanding baseline langkah 19
33. Verifikasi baris pertama tabel (sort default Date descending) memiliki Action `Import Brand`
34. Verifikasi baris pertama tabel memiliki Data "100 records imported, 0 duplicates ignored, 150 rows remaining"
35. Verifikasi baris pertama tabel memiliki Modified By `Yoga P`

### TC-GS-IMPORT-553: Job committing tanpa kemajuan tidak terkunci permanen

36. Tutup modal Changelog, lalu reset Client E (D-47) dan seed draft Brand D-34 (250 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
37. Muat ulang halaman Import > Brand
38. Aktifkan kontrol worker commit mode 3 (dijeda setelah batch pertama selesai; tidak dijalankan lagi)
39. Klik `[Import (250)]`
40. Tunggu aksi selesai (permintaan mendapat respons)
41. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
42. Mundurkan waktu kemajuan terakhir job 16 menit lewat fixture timestamp
43. Tunggu pelanjutan otomatis oleh sistem sampai hook D-47 melaporkan jumlah percobaan pelanjutan job bernilai 1 (batas tunggu 5 menit)
44. Verifikasi hook D-47 melaporkan jumlah percobaan pelanjutan job = 1
45. Muat ulang halaman Import > Brand
46. Verifikasi `[Discard]` Disabled (job masih `committing`)
47. Arahkan kursor ke `[Discard]` pada Unsaved Banner
48. Verifikasi tooltip pada `[Discard]` "Can't discard while an import is in progress."
49. Verifikasi kartu Total Rows 150
50. Mundurkan waktu kemajuan terakhir job 16 menit lagi lewat fixture timestamp
51. Muat ulang halaman Import > Brand setiap 5 detik sampai `[Discard]` Enabled (batas tunggu 5 menit)
52. Verifikasi `[Discard]` Enabled (job kembali `draft`)
53. Verifikasi `[Upload File]` Enabled
54. Verifikasi `[Import (150)]` Enabled
55. Baca jumlah percobaan pelanjutan job lewat hook D-47
56. Verifikasi jumlah percobaan pelanjutan job tetap 1
57. Klik `[Discard]` pada Unsaved Banner
58. Klik `[Discard Draft]` pada Dialog Discard Draft
59. Verifikasi toast sukses: "Success, draft has been discarded."
60. Verifikasi halaman kembali ke Dropzone

### TC-GS-IMPORT-532: Upload File langsung saat committing ditolak 409

61. Reset Client E (D-47) dan seed draft Brand D-34 (250 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
62. Muat ulang halaman Import > Brand
63. Aktifkan kontrol worker commit mode 3 (dijeda setelah batch pertama selesai; tidak dijalankan lagi)
64. Klik `[Import (250)]`
65. Tunggu aksi selesai (permintaan mendapat respons)
66. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
67. Kirim permintaan Upload File langsung ke server dengan token akun Total Control Client E dan berkas `brand-6.csv`
68. Verifikasi server menolak permintaan dengan 409 Conflict
69. Muat ulang halaman Import > Brand
70. Verifikasi kartu Total Rows tetap 150 (tidak bertambah 6 baris)
71. Verifikasi Unsaved Banner tetap tampil

### TC-GS-IMPORT-809: Discard Draft langsung saat committing ditolak 409

72. Reset Client E (D-47) dan seed draft Brand D-34 (250 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
73. Muat ulang halaman Import > Brand
74. Aktifkan kontrol worker commit mode 3 (dijeda setelah batch pertama selesai; tidak dijalankan lagi)
75. Klik `[Import (250)]`
76. Tunggu aksi selesai (permintaan mendapat respons)
77. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
78. Kirim permintaan Discard Draft langsung ke server dengan token akun Total Control Client E
79. Verifikasi server menolak permintaan dengan 409 Conflict
80. Muat ulang halaman Import > Brand
81. Verifikasi Unsaved Banner tampil
82. Verifikasi kartu Total Rows 150
83. Verifikasi `[Discard]` Disabled

### TC-GS-IMPORT-518: Tulis-balik tidak dijalankan saat job committing

84. Reset Client E (D-47) dan seed draft User Login D-54 (8 baris `pending`, Shift `Siang` pada Row # 1 dan 2) dengan hook umur draft D-76 varian 1 lewat skrip fixture
85. Muat ulang halaman Import > User Login
86. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
87. Klik `[Import (8)]`
88. Tunggu aksi selesai (permintaan mendapat respons)
89. Hapus opsi `Siang` dari Custom Field `Shift` di Custom Field User atas nama Admin kedua Client E lewat sesi API
90. Muat ulang halaman Import > User Login
91. Verifikasi Row # 1 tampil berstatus `error`
92. Verifikasi Row # 2 tampil berstatus `error`
93. Verifikasi Staging Metric Cards Ready to Import 6
94. Verifikasi Staging Metric Cards Errors 2
95. Arahkan kursor ke `[Discard]` pada Unsaved Banner
96. Verifikasi `[Discard]` Disabled dengan tooltip "Can't discard while an import is in progress." (job masih `committing`)
97. Baca status tersimpan Row # 1 dan 2 lewat skrip fixture inspeksi data
98. Verifikasi status tersimpan Row # 1 dan 2 masih `pending`
99. Pulihkan opsi `Siang` pada Custom Field `Shift` Client E

### TC-GS-IMPORT-947: Tulis-balik evaluasi Required tidak dijalankan saat job committing

100. Reset Client E (D-47) dan seed draft User Login D-54 (8 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture; pastikan `Shift Notes` opsional dan kosong pada seluruh baris
101. Muat ulang halaman Import > User Login
102. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
103. Klik `[Import (8)]`
104. Tunggu aksi selesai (permintaan mendapat respons)
105. Jadikan Custom Field `Shift Notes` Required di Custom Field User atas nama Admin kedua Client E lewat sesi API
106. Muat ulang halaman Import > User Login
107. Verifikasi Row # 1 tampil berstatus `error`
108. Verifikasi Row # 2 tampil berstatus `error`
109. Baca status tersimpan Row # 1 dan 2 lewat skrip fixture inspeksi data
110. Verifikasi status tersimpan Row # 1 dan 2 masih `pending`
111. Pulihkan `Shift Notes` ke opsional

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (d); objek uji adalah perilaku job `committing` yang dijeda atau dihentikan (kontrol worker D-47, penanda kemajuan job 15 menit sebagai batas yang diuji). Admin kedua hanya memicu perubahan Custom Field lewat sesi API (P-2).
- Alasan melewati sekitar 35 langkah (111 langkah nominal): tujuh blok homogen (satu job `committing` per blok), semua satu kelas harness dan berdiri sendiri dengan reset Client E di awal tiap blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok User Login (TC-518, 947) diletakkan terakhir karena mengubah Custom Field dan dipulihkan setelahnya.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan blok mengikuti kebutuhan state: tanpa commit sebagian (TC-755), commit sebagian dengan entri Changelog (TC-426), pelanjutan dan Discard (TC-553), request langsung (TC-532, 809), dan tulis-balik (TC-518, 947).
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 17, 36, 61, 72, 84, 100), muat ulang halaman Import > Brand dan Import > User Login (langkah 2, 85), pembukaan halaman dan Sub-Tab, pencatatan baseline (langkah 3, 19), aktivasi kontrol worker, penyetelan penanda kemajuan (langkah 7, 10, 25, 28, 42, 50), polling job, pembukaan Changelog dan penerapan filter, pemicu Admin kedua (langkah 89 dan 105), pemulihan Custom Field (langkah 99 dan 111), hover `[Discard]` sebelum asersi tooltip (langkah 47), dan Tunggu aksi selesai (langkah 6, 22, 40, 65, 76, 88, 104). Langkah 15 adalah `Verifikasi` modal Changelog Import terbuka sebagai anchor positif sebelum asersi jumlah entri tidak berubah (langkah 16).
- Langkah 16, 32 memakai baseline jumlah entri Changelog dengan Filter Action `Import Brand`; penanda kemajuan tidak menggeser jam server sehingga posisi baris pertama tidak terdampak (S-12).
- Kelas campur: TC-GS-IMPORT-532 dan TC-GS-IMPORT-809 berkelas a (request langsung ke server sebagai objek uji) berada di spec kelas d. Id pengecualian yang paling dekat adalah P-1 (state berat: job `committing` dibangun oleh langkah sebelumnya dan tidak dapat diulang tanpa biaya besar), tetapi P-1 tidak menyebut kelas a sebagai objek uji sehingga kesesuaiannya belum pasti; usulan aturan baru menunggu batch konvensi.
- Langkah 12 dan 13 adalah `Verifikasi` yang terhubung ke pemicu sebelum asersi jumlah entri Changelog tidak berubah (TC-755 Expected c).
- Temuan untuk QA:
  - TC-GS-IMPORT-426, 553, 532, 809, 755 menulis "menghentikan worker commit setelah batch pertama selesai"; D-47 mendefinisikan "dijeda setelah batch pertama selesai" (mode 3) dan "dihentikan sebelum batch pertama selesai" (mode 6). Spec memakai mode 3 untuk TC-426, 532, 553, 809 dan mode 6 untuk TC-755.
  - TC-GS-IMPORT-426, 755, 553 memakai D-56/D-34 dan jam 16 menit untuk perilaku sama (job `committing` tanpa kemajuan); TC-GS-IMPORT-553 (Must NOT) dan TC-GS-IMPORT-755 tumpang tindih sebagian pada asersi "job kembali `draft` setelah 16 menit"; bukan kontradiksi, tetapi duplikasi asersi. TC-GS-IMPORT-426 dan TC-GS-IMPORT-385 (spec 158) juga beririsan.
  - TC-GS-IMPORT-426 dan TC-GS-IMPORT-755 asersi langkah 7 dan 9 bergantung pada hook "jumlah percobaan pelanjutan" D-47 yang tidak menyebut nomor mode untuk TC ini.
  - Status `error` pada Row # 1 dan 2 (langkah 91, 92, 107, 108) adalah hasil hitung read-only untuk tampilan selama job `committing`, bukan nilai tersimpan; nilai tersimpan tetap `pending` dan diasersi lewat skrip fixture inspeksi data (langkah 98 dan 110).
  - TC-GS-IMPORT-518 dan TC-GS-IMPORT-947 menyebut Admin kedua Client E mengubah Custom Field User lewat UI; spec memakai sesi API (P-2) karena hasil di sesi itu tidak diasersi. Mekanisme dan skrip fixture inspeksi data disediakan tim FE/BE.
  - TC-GS-IMPORT-532 dan TC-GS-IMPORT-809 memakai D-34 (`Brand nnn`), sedangkan TC commit Client E lain memakai D-56 (`Brand Impor nnn`); Post Condition menyebut 100 Brand hasil batch pertama dihapus kembali (R2), dikerjakan reset dan hook `after`.
  - Post Condition TC-GS-IMPORT-426 (draft 150 baris; satu entri ringkasan), TC-GS-IMPORT-755 (draft 250 baris; tidak ada record), dan TC-GS-IMPORT-532, 809, 553, 518, 947 tidak punya langkah observasi tersendiri selain Expected dan tidak diasersi tambahan (S-01).
  - Penanda selesai untuk langkah 5, 21, 39, 64, dan 75 (klik `[Import (250)]`) serta langkah 87 dan 103 (klik `[Import (8)]`) tidak disebut di TC, PRD, atau spec ini; langkah "Tunggu aksi selesai" (langkah 6, 22, 40, 65, 76, 88, 104) memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati di halaman Import.
