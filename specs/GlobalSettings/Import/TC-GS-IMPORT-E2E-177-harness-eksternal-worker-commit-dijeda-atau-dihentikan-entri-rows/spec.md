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
2. Buka Global Settings > Import, pilih Sub-Tab Brand
3. Klik `[Changelog]` di header halaman, terapkan Filter Action = `Import Brand`, catat angka total pada teks Pagination (Showing [From] - [To] of [N] items; 0 bila yang tampil adalah empty state) sebagai baseline, lalu tutup modal Changelog
4. Aktifkan kontrol worker commit mode 6 (dihentikan sebelum batch pertama selesai; tidak dijalankan lagi) dan pencatat jumlah percobaan pelanjutan job
5. Klik `[Import (250)]`
6. Mundurkan penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
7. Baca jumlah percobaan pelanjutan pada kontrol worker commit setiap 5 detik sampai bernilai 1 (batas tunggu 5 menit)
8. Verifikasi jumlah percobaan pelanjutan pada kontrol worker commit bernilai 1
9. Mundurkan lagi penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
10. Muat ulang halaman Import > Brand setiap 5 detik sampai `[Discard]` Enabled (batas tunggu 5 menit)
11. Verifikasi `[Discard]` Enabled (job kembali `draft`)
12. Verifikasi kartu Total Rows tetap 250 (tidak ada baris terkomit)
13. Klik `[Changelog]` di header halaman, terapkan Filter Action = `Import Brand`, dan baca angka total pada teks Pagination
14. Verifikasi total pada Pagination Changelog Import dengan Filter Action `Import Brand` sama dengan baseline langkah 3

### TC-GS-IMPORT-426: Entri commit yang berhenti dengan sebagian baris terkomit memakai format rows remaining

15. Tutup modal Changelog, lalu reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
16. Muat ulang halaman Import > Brand
17. Klik `[Changelog]` di header halaman, terapkan Filter Action = `Import Brand`, catat angka total pada teks Pagination sebagai baseline, lalu tutup modal Changelog
18. Aktifkan kontrol worker commit mode 3 (dijeda setelah batch pertama selesai; tidak dijalankan lagi) dan pencatat jumlah percobaan pelanjutan job
19. Klik `[Import (250)]`
20. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
21. Verifikasi kartu Total Rows menampilkan 150
22. Mundurkan penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
23. Baca jumlah percobaan pelanjutan pada kontrol worker commit setiap 5 detik sampai bernilai 1 (batas tunggu 5 menit)
24. Verifikasi jumlah percobaan pelanjutan pada kontrol worker commit bernilai 1
25. Mundurkan lagi penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
26. Muat ulang halaman Import > Brand setiap 5 detik sampai `[Discard]` Enabled (batas tunggu 5 menit)
27. Verifikasi `[Discard]` Enabled (job kembali `draft`)
28. Klik `[Changelog]` di header halaman, terapkan Filter Action = `Import Brand`, dan baca angka total pada teks Pagination
29. Verifikasi total pada Pagination Changelog Import dengan Filter Action `Import Brand` bertambah tepat satu dibanding baseline langkah 17
30. Verifikasi baris pertama tabel (sort default Date descending) memiliki Action `Import Brand`
31. Verifikasi baris pertama tabel memiliki Data "100 records imported, 0 duplicates ignored, 150 rows remaining"
32. Verifikasi baris pertama tabel memiliki Modified By `Yoga P`

### TC-GS-IMPORT-553: Job committing tanpa kemajuan tidak terkunci permanen

33. Tutup modal Changelog, lalu reset Client E (D-47) dan seed draft Brand D-34 (250 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
34. Muat ulang halaman Import > Brand
35. Aktifkan kontrol worker commit mode 3 (dijeda setelah batch pertama selesai; tidak dijalankan lagi)
36. Klik `[Import (250)]`
37. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
38. Mundurkan waktu kemajuan terakhir job 16 menit lewat fixture timestamp
39. Tunggu pelanjutan otomatis oleh sistem sampai hook D-47 melaporkan jumlah percobaan pelanjutan job bernilai 1 (batas tunggu 5 menit)
40. Verifikasi hook D-47 melaporkan jumlah percobaan pelanjutan job = 1
41. Muat ulang halaman Import > Brand
42. Verifikasi `[Discard]` Disabled (job masih `committing`)
43. Verifikasi tooltip pada `[Discard]` "Can't discard while an import is in progress."
44. Verifikasi kartu Total Rows 150
45. Mundurkan waktu kemajuan terakhir job 16 menit lagi lewat fixture timestamp
46. Muat ulang halaman Import > Brand setiap 5 detik sampai `[Discard]` Enabled (batas tunggu 5 menit)
47. Verifikasi `[Discard]` Enabled (job kembali `draft`)
48. Verifikasi `[Upload File]` Enabled
49. Verifikasi `[Import (150)]` Enabled
50. Baca jumlah percobaan pelanjutan job lewat hook D-47
51. Verifikasi jumlah percobaan pelanjutan job tetap 1
52. Klik `[Discard]` pada Unsaved Banner
53. Klik `[Discard Draft]` pada Dialog Discard Draft
54. Verifikasi toast sukses: "Success, draft has been discarded."
55. Verifikasi halaman kembali ke Dropzone

### TC-GS-IMPORT-532: Upload File langsung saat committing ditolak 409

56. Reset Client E (D-47) dan seed draft Brand D-34 (250 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
57. Muat ulang halaman Import > Brand
58. Aktifkan kontrol worker commit mode 3 (dijeda setelah batch pertama selesai; tidak dijalankan lagi)
59. Klik `[Import (250)]`
60. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
61. Kirim permintaan Upload File langsung ke server dengan token akun Total Control Client E dan berkas `brand-6.csv`
62. Verifikasi server menolak permintaan dengan 409 Conflict
63. Muat ulang halaman Import > Brand
64. Verifikasi kartu Total Rows tetap 150 (tidak bertambah 6 baris)
65. Verifikasi Unsaved Banner tetap tampil

### TC-GS-IMPORT-809: Discard Draft langsung saat committing ditolak 409

66. Reset Client E (D-47) dan seed draft Brand D-34 (250 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
67. Muat ulang halaman Import > Brand
68. Aktifkan kontrol worker commit mode 3 (dijeda setelah batch pertama selesai; tidak dijalankan lagi)
69. Klik `[Import (250)]`
70. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
71. Kirim permintaan Discard Draft langsung ke server dengan token akun Total Control Client E
72. Verifikasi server menolak permintaan dengan 409 Conflict
73. Muat ulang halaman Import > Brand
74. Verifikasi Unsaved Banner tampil
75. Verifikasi kartu Total Rows 150
76. Verifikasi `[Discard]` Disabled

### TC-GS-IMPORT-518: Tulis-balik tidak dijalankan saat job committing

77. Reset Client E (D-47) dan seed draft User Login D-54 (8 baris `pending`, Shift `Siang` pada Row # 1 dan 2) dengan hook umur draft D-76 varian 1 lewat skrip fixture
78. Buka Global Settings > Import, pilih Sub-Tab User Login
79. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
80. Klik `[Import (8)]`
81. Hapus opsi `Siang` dari Custom Field `Shift` di Custom Field User atas nama Admin kedua Client E lewat sesi API
82. Muat ulang halaman Import > User Login
83. Verifikasi Row # 1 tampil berstatus `error` sebagai hasil hitung read-only untuk tampilan
84. Verifikasi Row # 2 tampil berstatus `error` sebagai hasil hitung read-only untuk tampilan
85. Verifikasi Staging Metric Cards Ready to Import 6
86. Verifikasi Staging Metric Cards Errors 2
87. Arahkan kursor ke `[Discard]` pada Unsaved Banner
88. Verifikasi `[Discard]` Disabled dengan tooltip "Can't discard while an import is in progress." (job masih `committing`)
89. Baca status tersimpan Row # 1 dan 2 lewat skrip fixture inspeksi data
90. Verifikasi status tersimpan Row # 1 dan 2 masih `pending`
91. Pulihkan opsi `Siang` pada Custom Field `Shift` Client E

### TC-GS-IMPORT-947: Tulis-balik evaluasi Required tidak dijalankan saat job committing

92. Reset Client E (D-47) dan seed draft User Login D-54 (8 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture; pastikan `Shift Notes` opsional dan kosong pada seluruh baris
93. Muat ulang halaman Import > User Login
94. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
95. Klik `[Import (8)]`
96. Jadikan Custom Field `Shift Notes` Required di Custom Field User atas nama Admin kedua Client E lewat sesi API
97. Muat ulang halaman Import > User Login
98. Verifikasi Row # 1 tampil berstatus `error` sebagai hasil hitung read-only untuk tampilan
99. Verifikasi Row # 2 tampil berstatus `error` sebagai hasil hitung read-only untuk tampilan
100. Baca status tersimpan Row # 1 dan 2 lewat skrip fixture inspeksi data
101. Verifikasi status tersimpan Row # 1 dan 2 masih `pending`
102. Pulihkan `Shift Notes` ke opsional

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (d); objek uji adalah perilaku job `committing` yang dijeda atau dihentikan (kontrol worker D-47, penanda kemajuan job 15 menit sebagai batas yang diuji). Admin kedua hanya memicu perubahan Custom Field lewat sesi API (P-2).
- Alasan melewati sekitar 35 langkah (102 langkah nominal): tujuh blok homogen (satu job `committing` per blok), semua satu kelas harness dan berdiri sendiri dengan reset Client E di awal tiap blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok User Login (TC-518, 947) diletakkan terakhir karena mengubah Custom Field dan dipulihkan setelahnya.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan blok mengikuti kebutuhan state: tanpa commit sebagian (TC-755), commit sebagian dengan entri Changelog (TC-426), pelanjutan dan Discard (TC-553), request langsung (TC-532, 809), dan tulis-balik (TC-518, 947).
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 15, 33, 56, 66, 77, 92), pembukaan halaman dan Sub-Tab, pencatatan baseline (langkah 3, 17), aktivasi kontrol worker, penyetelan penanda kemajuan (langkah 6, 9, 22, 25, 38, 45), polling job, pembukaan Changelog dan penerapan filter, pemicu Admin kedua (langkah 81 dan 96), dan pemulihan Custom Field (langkah 91 dan 102).
- Langkah 14, 29 memakai baseline jumlah entri Changelog dengan Filter Action `Import Brand`; penanda kemajuan tidak menggeser jam server sehingga posisi baris pertama tidak terdampak (S-12).
- Langkah 10 dan 11 adalah `Verifikasi` yang terhubung ke pemicu sebelum asersi jumlah entri Changelog tidak berubah (TC-755 Expected c).
- Temuan untuk QA:
  - TC-GS-IMPORT-426, 553, 532, 809, 755 menulis "menghentikan worker commit setelah batch pertama selesai"; D-47 mendefinisikan "dijeda setelah batch pertama selesai" (mode 3) dan "dihentikan sebelum batch pertama selesai" (mode 6). Spec memakai mode 3 untuk TC-426, 532, 553, 809 dan mode 6 untuk TC-755.
  - TC-GS-IMPORT-426, 755, 553 memakai D-56/D-34 dan jam 16 menit untuk perilaku sama (job `committing` tanpa kemajuan); TC-GS-IMPORT-553 (Must NOT) dan TC-GS-IMPORT-755 tumpang tindih sebagian pada asersi "job kembali `draft` setelah 16 menit"; bukan kontradiksi, tetapi duplikasi asersi. TC-GS-IMPORT-426 dan TC-GS-IMPORT-385 (spec 158) juga beririsan.
  - TC-GS-IMPORT-426 dan TC-GS-IMPORT-755 asersi langkah 7 dan 9 bergantung pada hook "jumlah percobaan pelanjutan" D-47 yang tidak menyebut nomor mode untuk TC ini.
  - TC-GS-IMPORT-518 dan TC-GS-IMPORT-947 menyebut Admin kedua Client E mengubah Custom Field User lewat UI; spec memakai sesi API (P-2) karena hasil di sesi itu tidak diasersi. Mekanisme dan skrip fixture inspeksi data disediakan tim FE/BE.
  - TC-GS-IMPORT-532 dan TC-GS-IMPORT-809 memakai D-34 (`Brand nnn`), sedangkan TC commit Client E lain memakai D-56 (`Brand Impor nnn`); Post Condition menyebut 100 Brand hasil batch pertama dihapus kembali (R2), dikerjakan reset dan hook `after`.
  - Post Condition TC-GS-IMPORT-426 (draft 150 baris; satu entri ringkasan), TC-GS-IMPORT-755 (draft 250 baris; tidak ada record), dan TC-GS-IMPORT-532, 809, 553, 518, 947 tidak punya langkah observasi tersendiri selain Expected dan tidak diasersi tambahan (S-01).
