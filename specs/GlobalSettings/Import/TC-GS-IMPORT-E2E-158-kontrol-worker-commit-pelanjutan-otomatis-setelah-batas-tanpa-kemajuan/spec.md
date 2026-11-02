---
id: TC-GS-IMPORT-E2E-158-kontrol-worker-commit-pelanjutan-otomatis-setelah-batas-tanpa-kemajuan
title: "Kontrol worker commit: pelanjutan otomatis setelah batas tanpa kemajuan tanpa memproses ulang baris terkomit; di bawah batas tidak"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-385
  - TC-GS-IMPORT-386
  - TC-GS-IMPORT-749
  - TC-GS-IMPORT-822
coverage:
  web: automated
---

# Kontrol worker commit: pelanjutan otomatis setelah batas tanpa kemajuan tanpa memproses ulang baris terkomit; di bawah batas tidak

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah state global (kontrol worker commit, penanda kemajuan job) dan melakukan commit nyata di Client E yang dipakai bersama spec commit lain; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client E dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE):
  - Kontrol worker commit D-47: mode 3 (dijeda setelah batch pertama selesai, 100 baris terkomit, tidak dijalankan lagi selama blok) untuk TC-385, 749, 822; mode 5 (dihentikan setelah batch kedua, 200 baris terkomit) untuk TC-386, dengan pelepasan jeda; hook membaca jumlah percobaan pelanjutan job.
  - Fixture timestamp kemajuan job: memundurkan penanda kemajuan job secara relatif (16 menit, 8 menit, tambahan 2 menit, tambahan 1 menit) dan mengaturnya absolut tepat 15 menit sebelum waktu server saat ini (TC-822, batas eksak). Penanda dihitung di server dan tidak diamati lewat countdown UI, sehingga jam browser tidak diubah dan jeda tidak ditunggu secara nyata.
  - Margin terhadap batas 15 menit (kurang dari 5 menit; 8b.3): usia tanpa kemajuan = pergeseran fixture + waktu nyata sejak kemajuan terakhir, dan titik uji dihitung dari pergeseran sebagai berikut. TC-749 di bawah batas: 8 + 2 = 10 menit pada langkah 8 sampai 14 (margin 15 − 10 = 5 menit) dan 10 + 1 = 11 menit pada langkah 15 sampai 20 (margin 15 − 11 = 4 menit); waktu nyata mengurangi margin (arah tidak aman), sehingga langkah 9 sampai 20 diselesaikan tanpa jeda sengaja. TC-385 dan TC-386: 16 menit, margin 16 − 15 = 1 menit di atas batas; waktu nyata hanya menambah usia (arah aman). TC-822: penanda diatur absolut tepat 15 menit sebelum waktu server (margin 0, batas eksak yang diuji); waktu nyata hanya menambah usia sehingga "sudah terlampaui" tetap benar.
  - Hook umur draft D-76 varian 1 (>=24 jam; `created_at` dimundurkan 25 jam) untuk TC-385, 749, 822.
  - Skrip fixture reset Client E (D-47: hapus draft, lanjutkan worker, hapus Brand hasil commit, reset hasil commit terakhir) dan seeding draft.
  - Jeda nyata: polling "muat ulang setiap 5 detik" menunggu job latar belakang (batas tunggu 2 sampai 7 menit sesuai TC), bukan menunggu jam.
- Data Dinamis (milik spec ini; hasil commit dihapus oleh reset): D-56 `brand-250-impor.csv`, `Brand Impor 001` (#1) sampai `Brand Impor 250` (#250), semua valid dan unik.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): lanjutkan worker commit, kembalikan penanda kemajuan job, hapus draft Client E, hapus Brand hasil commit (`Brand Impor nnn`), reset hasil commit terakhir, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-749: Di bawah batas 15 menit tidak dilanjutkan

1. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
2. Muat ulang halaman Import > Brand
3. Aktifkan kontrol worker commit mode 3 (dijeda setelah batch pertama selesai; tidak dijalankan lagi) dan pencatat jumlah percobaan pelanjutan job
4. Klik `[Import (250)]`
5. Tunggu aksi selesai (permintaan mendapat respons)
6. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
7. Verifikasi kartu Total Rows menampilkan 150
8. Mundurkan penanda kemajuan job sebesar 8 menit lewat fixture timestamp kemajuan job
9. Mundurkan penanda kemajuan job tambahan 2 menit (setara jeda 2 menit pada TC)
10. Muat ulang halaman Import > Brand
11. Verifikasi `[Discard]` Disabled
12. Verifikasi tooltip pada `[Discard]` "Can't discard while an import is in progress."
13. Verifikasi kartu Total Rows tetap 150
14. Verifikasi jumlah percobaan pelanjutan pada kontrol worker commit bernilai 0
15. Mundurkan penanda kemajuan job tambahan 1 menit (setara jeda 1 menit pada TC)
16. Muat ulang halaman Import > Brand
17. Verifikasi `[Discard]` Disabled
18. Verifikasi tooltip pada `[Discard]` "Can't discard while an import is in progress."
19. Verifikasi kartu Total Rows tetap 150
20. Verifikasi jumlah percobaan pelanjutan pada kontrol worker commit bernilai 0

### TC-GS-IMPORT-822: Tepat 15 menit sudah terlampaui dan dilanjutkan otomatis

21. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
22. Muat ulang halaman Import > Brand
23. Aktifkan kontrol worker commit mode 3 (dijeda setelah batch pertama selesai; tidak dijalankan lagi)
24. Klik `[Import (250)]`
25. Tunggu aksi selesai (permintaan mendapat respons)
26. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
27. Verifikasi kartu Total Rows menampilkan 150
28. Atur penanda kemajuan job menjadi tepat 15 menit sebelum waktu server saat ini (fixture timestamp kemajuan job, nilai absolut)
29. Baca jumlah percobaan pelanjutan pada kontrol worker commit setiap 5 detik sampai bernilai 1 (batas tunggu 5 menit)
30. Verifikasi jumlah percobaan pelanjutan pada kontrol worker commit bernilai 1
31. Muat ulang halaman Import > Brand
32. Verifikasi `[Discard]` Disabled
33. Verifikasi kartu Total Rows tetap 150

### TC-GS-IMPORT-385: Pelanjutan otomatis lalu kembali ke draft bila pelanjutan juga tanpa kemajuan

34. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
35. Muat ulang halaman Import > Brand
36. Aktifkan kontrol worker commit mode 3 (dijeda setelah batch pertama selesai; tidak dijalankan lagi) dan pencatat jumlah percobaan pelanjutan job
37. Klik `[Import (250)]`
38. Tunggu aksi selesai (permintaan mendapat respons)
39. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
40. Mundurkan penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
41. Baca jumlah percobaan pelanjutan pada kontrol worker commit setiap 5 detik sampai bernilai 1 (batas tunggu 5 menit)
42. Verifikasi jumlah percobaan pelanjutan pada kontrol worker commit bernilai 1
43. Muat ulang halaman Import > Brand
44. Verifikasi `[Discard]` Disabled (job masih `committing`)
45. Verifikasi kartu Total Rows tetap 150
46. Mundurkan lagi penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
47. Muat ulang halaman Import > Brand setiap 5 detik sampai `[Discard]` Enabled (batas tunggu 5 menit)
48. Verifikasi `[Discard]` Enabled (job kembali `draft`)
49. Verifikasi `[Upload File]` Enabled
50. Verifikasi `[Import (150)]` Enabled
51. Verifikasi toggle "Edit this page" Enabled
52. Verifikasi kartu Total Rows 150 (baris yang sudah terkomit tidak diproses ulang)
53. Buka halaman Master Reference > Brand
54. Ketik Search `Brand Impor`, tekan Enter
55. Verifikasi Pagination tabel Brand Client E menampilkan "Showing 1 - 10 of 100 items"

### TC-GS-IMPORT-386: Pelanjutan otomatis tidak memproses ulang baris yang sudah terkomit

56. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) lewat skrip fixture
57. Buka Global Settings > Import, pilih Sub-Tab Brand
58. Aktifkan kontrol worker commit mode 5 (dihentikan setelah batch kedua, 200 baris terkomit) dan jangan jalankan lagi selama blok ini
59. Klik `[Import (250)]`
60. Tunggu aksi selesai (permintaan mendapat respons)
61. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 50 (batas tunggu 2 menit)
62. Nonaktifkan kontrol penghenti worker commit
63. Mundurkan penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
64. Tunggu commit selesai: muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 7 menit)
65. Verifikasi Dropzone tampil
66. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil
67. Buka halaman Master Reference > Brand
68. Ketik Search `Brand Impor`, tekan Enter
69. Verifikasi Pagination tabel Brand Client E menampilkan "Showing 1 - 10 of 250 items"

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (d); objek uji adalah TTL kemajuan job 15 menit (sebagai batas yang diuji) pada job `committing`. Penanda kemajuan job dan kontrol worker D-47 adalah harness; spec tidak menunggu waktu nyata untuk batas 15 menit.
- Alasan melewati sekitar 35 langkah (69 langkah nominal): empat blok homogen (satu kelas harness, satu job `committing` per blok), tiap blok berdiri sendiri dengan reset Client E di awal sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Urutan blok: TC-749 dan TC-822 (tanpa pelanjutan atau pelanjutan sekali, tanpa commit selesai), lalu TC-385 (pelanjutan kedua kembali ke draft), lalu TC-386 (commit selesai).
- Subjudul `###` memetakan langkah ke id TC granular.
- Penggantian jeda nyata: TC-GS-IMPORT-749 Langkah 5 "Tunggu 2 menit" dan Langkah 8 "Tunggu 1 menit" diganti memundurkan penanda kemajuan job tambahan 2 menit dan 1 menit (langkah 9 dan 15), karena menunggu waktu nyata di atas ±30 detik tidak diizinkan konvensi (bagian 6) dan penanda dihitung di server. Batas yang diuji tidak berubah: usia tanpa kemajuan total 10 menit dan 11 menit, tetap di bawah 15 menit.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 21, 34, 56), aktivasi dan penonaktifan kontrol worker (langkah 3, 23, 36, 59, 62), muat ulang halaman Import > Brand sesudah reset (langkah 2, 22, dan 35), pembukaan halaman dan Sub-Tab lain, penyetelan penanda kemajuan (langkah 8, 9, 15, 28, 40, 46, 63), "Tunggu aksi selesai (permintaan mendapat respons)" persis sesudah klik `[Import (250)]` dan sebelum polling (langkah 5, 25, 38, 60; bagian 8b butir 8), dan polling job (langkah 6, 26, 29, 39, 41, 47, 61, 64) yang menunggu job latar belakang dan bukan menunggu jam.
- Langkah 7, 27 (Total Rows 150) dan TC-GS-IMPORT-749 Expected a diasersi sebelum penyetelan penanda sebagai anchor bahwa batch pertama terkomit. Langkah 14 dan 20 (jumlah percobaan pelanjutan 0) diasersi sesudah muat ulang.
- Temuan untuk QA:
  - Penanda selesai untuk klik `[Import (250)]` (langkah 5, 25, 38, 60) tidak disebut di TC atau PRD; langkah "Tunggu aksi selesai" memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati.
  - TC-GS-IMPORT-385 dan TC-GS-IMPORT-749 menulis "menghentikan worker commit setelah batch pertama selesai"; D-47 mendefinisikan "dijeda setelah batch pertama selesai" (mode 3) dan "dihentikan setelah batch kedua" (mode 5). Spec memakai mode 3 untuk TC-385, 749, 822 dan mode 5 untuk TC-386.
  - TC-GS-IMPORT-426, 755, 553 (spec 177) memakai nilai jam 16 menit yang sama untuk perilaku serupa; TC-GS-IMPORT-385 juga menyangkut "kembali ke draft bila pelanjutan juga tanpa kemajuan" yang beririsan dengan TC-GS-IMPORT-426.
  - TC-GS-IMPORT-822 menyebut "mode (3)" pada Precondition dan Langkah 1 tetapi kolom D-ref TC-GS-IMPORT-385, 386, 749 tidak merujuk D-47; kontrol worker ditulis di Prerequisites.
  - TC-GS-IMPORT-822 Post Condition a ("draft berisi 150 baris dengan job berstatus committing") bertentangan ringan dengan Expected c yang hanya mengasersi `[Discard]` Disabled dan Total Rows 150; spec mengasersi Expected.
  - Post Condition TC-GS-IMPORT-385 (draft 150 baris, 100 record Brand), TC-GS-IMPORT-386 (draft dihapus; 250 record), TC-GS-IMPORT-749 ("job committing; draft 150 baris"), dan TC-GS-IMPORT-822 tidak punya langkah observasi tersendiri selain Expected dan tidak diasersi tambahan (S-01).
