---
id: TC-GS-IMPORT-E2E-160-notifikasi-progres-commit-awal-pembaruan-in-place-per-batch-selesai
title: "Notifikasi progres commit: awal, pembaruan in-place per batch, selesai dengan Detail, selesai dengan error, dan stopped"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-411
  - TC-GS-IMPORT-412
  - TC-GS-IMPORT-413
  - TC-GS-IMPORT-414
  - TC-GS-IMPORT-415
coverage:
  web: automated
---

# Notifikasi progres commit: awal, pembaruan in-place per batch, selesai dengan Detail, selesai dengan error, dan stopped

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec melakukan commit nyata di Client E, mengubah state global (kontrol worker commit, penanda kemajuan job), dan notifikasi lonceng bersifat permanen sehingga asersi memakai baseline; lihat `suite.md`.
- Dua konteks browser, ditandai `[Sesi A]` dan `[Sesi B]` (hanya TC-411 memakai Sesi B, yang mengasersi notifikasi di lonceng Admin kedua). Langkah tanpa tanda dijalankan di Sesi A:
  - Sesi A (aktor): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Login di hook `before`; layar awal Global Settings > Import dibuka hook `beforeEach`.
  - Sesi B (penerima notifikasi): Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTE_TC2_PASSWORD`. Login di hook `before` pada konteks browser terpisah.
  - Password tidak ditulis di spec atau fixture.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk kedua akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; TC-411 sampai TC-415 tidak merujuk D-47 pada kolom D-ref pada sebagian baris tetapi membutuhkannya):
  - Kontrol worker commit D-47: mode 1 (dijeda sebelum job mulai) untuk TC-411; mode 7 (dijeda sebelum tiap batch, satu batch per perintah lepas) untuk TC-412; mode 3 (dijeda setelah batch pertama selesai, tidak dijalankan lagi) dan hook jumlah percobaan pelanjutan untuk TC-415; worker normal untuk TC-413 dan TC-414.
  - Fixture timestamp kemajuan job (memundurkan penanda 16 menit, dua kali) untuk TC-415; dihitung di server dan tidak diamati lewat countdown UI.
  - Margin TC-415 terhadap batas 15 menit (kurang dari 5 menit; 8b.3): tiap pergeseran 16 menit (langkah 53 dan 56) memberi margin 16 − 15 = 1 menit (60 detik) di atas batas; usia tanpa kemajuan = pergeseran + waktu nyata sejak kemajuan terakhir, sehingga waktu nyata hanya menambah usia (arah aman: batas tetap terlampaui). Nilai 16 menit mengikuti TC dan tidak dinaikkan.
  - Hook umur draft D-76 varian 1 (>=24 jam; `created_at` dimundurkan 25 jam) untuk TC-414 dan TC-415.
  - Notifikasi lonceng diperbarui via SSE (tanpa muat ulang halaman); skrip fixture reset Client E (D-47: hapus draft, lanjutkan worker, hapus Brand hasil commit, reset hasil commit terakhir) dan seeding draft.
  - Jendela amat SSE 5 detik (langkah 44) adalah pilihan spec (bukan nilai TC atau PRD) sampai TC menyatakan durasinya.
  - Jeda nyata: polling "muat ulang setiap 5 detik" menunggu job latar belakang (bukan menunggu jam).
- Baseline notifikasi (S-12): jumlah notifikasi lonceng dengan judul yang diasersi dicatat sebelum aksi pemicu pertama tiap blok; asersi "notifikasi baru" memakai selisih terhadap baseline, bukan posisi atau angka absolut.
- Data Dinamis (milik spec ini; draft dibuang dan hasil commit dihapus oleh reset):
  - D-56 `brand-250-impor.csv`: `Brand Impor 001` sampai `Brand Impor 250`, semua valid dan unik (TC-411, 412, 413, 415).
  - D-59 `brand-250-err5.csv`: 245 `pending` (`Brand Impor nnn`) dan 5 `error` (baris #10, #60, #110, #160, #210 dengan Brand Name 121 karakter huruf `A`, `B`, `C`, `D`, `E` diulang 121 kali) (TC-414).
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): lanjutkan worker commit, kembalikan penanda kemajuan job, hapus draft Client E, hapus Brand hasil commit (`Brand Impor nnn`), reset hasil commit terakhir, tutup konteks Sesi B, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-413: Penyelesaian, notifikasi completed dengan tombol Detail

1. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) lewat skrip fixture
2. Buka Global Settings > Import, pilih Sub-Tab Brand
3. Buka notifikasi lonceng, catat jumlah notifikasi "Import Brand completed" sebagai baseline, lalu tutup lonceng
4. Klik `[Import (250)]`
5. Tunggu aksi selesai (permintaan mendapat respons)
6. Tunggu commit selesai: muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
7. Buka notifikasi lonceng
8. Verifikasi jumlah notifikasi "Import Brand completed" bertambah tepat 1 dari baseline langkah 3
9. Verifikasi notifikasi terbaru memuat judul "Import Brand completed"
10. Verifikasi notifikasi terbaru memuat isi "250 records imported."
11. Verifikasi notifikasi terbaru memuat tombol `[Detail]`
12. Klik `[Detail]` pada notifikasi
13. Verifikasi halaman Import > Brand terbuka dengan Breadcrumb "Import > Brand"

### TC-GS-IMPORT-414: Penyelesaian dengan baris error tersisa

14. Reset Client E (D-47) dan seed draft Brand D-59 (245 `pending`, 5 `error`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
15. Buka Global Settings > Import, pilih Sub-Tab Brand
16. Buka notifikasi lonceng, catat jumlah notifikasi "Import Brand completed" sebagai baseline, lalu tutup lonceng
17. Klik `[Import (245)]`
18. Tunggu aksi selesai (permintaan mendapat respons)
19. Tunggu commit selesai: muat ulang halaman Import > Brand setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
20. Buka notifikasi lonceng
21. Verifikasi jumlah notifikasi "Import Brand completed" bertambah tepat 1 dari baseline langkah 16
22. Verifikasi notifikasi terbaru memuat judul "Import Brand completed"
23. Verifikasi notifikasi terbaru memuat isi "245 records imported. 5 errors remain."
24. Verifikasi notifikasi terbaru memuat tombol `[Detail]`
25. Tutup lonceng
26. Verifikasi Unsaved Banner tampil
27. Verifikasi kartu Errors menampilkan 5

### TC-GS-IMPORT-412: Notifikasi diperbarui in-place per batch

28. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) lewat skrip fixture
29. Buka Global Settings > Import, pilih Sub-Tab Brand
30. Buka notifikasi lonceng, catat jumlah rekaman "Importing Brand..." sebagai baseline, lalu tutup lonceng
31. Aktifkan kontrol worker commit mode 7 (dijeda sebelum tiap batch; satu batch per perintah lepas)
32. Klik `[Import (250)]`
33. Buka notifikasi lonceng
34. Verifikasi notifikasi "Importing Brand..." berisi "0 of 250 records processed."
35. Verifikasi notifikasi "Importing Brand..." tanpa tombol aksi
36. Lepaskan batch pertama lewat kontrol worker commit
37. Baca isi notifikasi tanpa memuat ulang halaman
38. Verifikasi rekaman yang sama berisi "100 of 250 records processed."
39. Verifikasi rekaman yang sama tanpa tombol aksi
40. Lepaskan batch kedua lewat kontrol worker commit
41. Baca isi notifikasi tanpa memuat ulang halaman
42. Verifikasi rekaman yang sama berisi "200 of 250 records processed."
43. Verifikasi rekaman yang sama tanpa tombol aksi
44. Tunggu 5 detik tanpa memuat ulang halaman
45. Verifikasi jumlah rekaman "Importing Brand..." bertambah tepat 1 dari baseline langkah 30 (tidak ada rekaman baru per batch)

### TC-GS-IMPORT-415: Notifikasi stopped saat job kembali ke draft

46. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
47. Buka Global Settings > Import, pilih Sub-Tab Brand
48. Buka notifikasi lonceng, catat jumlah notifikasi "Import Brand stopped" sebagai baseline, lalu tutup lonceng
49. Aktifkan kontrol worker commit mode 3 (dijeda setelah batch pertama selesai; tidak dijalankan lagi) dan pencatat jumlah percobaan pelanjutan job
50. Klik `[Import (250)]`
51. Tunggu aksi selesai (permintaan mendapat respons)
52. Muat ulang halaman Import > Brand setiap 5 detik sampai kartu Total Rows menampilkan 150 (batas tunggu 2 menit)
53. Mundurkan penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
54. Baca jumlah percobaan pelanjutan pada kontrol worker commit setiap 5 detik sampai bernilai 1 (batas tunggu 5 menit)
55. Verifikasi jumlah percobaan pelanjutan pada kontrol worker commit bernilai 1
56. Mundurkan lagi penanda kemajuan job sebesar 16 menit lewat fixture timestamp kemajuan job
57. Muat ulang halaman Import > Brand setiap 5 detik sampai `[Discard]` Enabled (batas tunggu 5 menit)
58. Verifikasi `[Discard]` Enabled (job kembali `draft`)
59. Buka notifikasi lonceng
60. Verifikasi jumlah notifikasi "Import Brand stopped" bertambah tepat 1 dari baseline langkah 48
61. Verifikasi notifikasi terbaru memuat judul "Import Brand stopped"
62. Verifikasi notifikasi terbaru memuat isi "100 records imported. 150 rows remain."
63. Verifikasi notifikasi terbaru memuat tombol `[Detail]`

### TC-GS-IMPORT-411: Notifikasi awal diterima Total Control dan Admin kedua

64. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) lewat skrip fixture
65. [Sesi A] Buka Global Settings > Import, pilih Sub-Tab Brand
66. [Sesi A] Buka notifikasi lonceng, catat jumlah rekaman "Importing Brand..." sebagai baseline, lalu tutup lonceng
67. [Sesi B] Buka Global Settings > Import, buka notifikasi lonceng, catat jumlah rekaman "Importing Brand..." sebagai baseline, lalu tutup lonceng
68. Aktifkan kontrol worker commit mode 1 (dijeda sebelum batch pertama diproses)
69. [Sesi A] Klik `[Import (250)]`
70. [Sesi A] Buka notifikasi lonceng
71. [Sesi A] Verifikasi jumlah rekaman "Importing Brand..." bertambah tepat 1 dari baseline langkah 66
72. [Sesi A] Verifikasi notifikasi baru "Importing Brand..." berisi "0 of 250 records processed."
73. [Sesi A] Verifikasi notifikasi baru tanpa tombol aksi
74. [Sesi B] Buka notifikasi lonceng
75. [Sesi B] Verifikasi jumlah rekaman "Importing Brand..." bertambah tepat 1 dari baseline langkah 67
76. [Sesi B] Verifikasi notifikasi baru "Importing Brand..." berisi "0 of 250 records processed."
77. [Sesi B] Verifikasi notifikasi baru tanpa tombol aksi

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (d); objek uji adalah notifikasi progres commit yang dihasilkan job latar belakang, kontrol worker D-47, dan penanda kemajuan job. TC-GS-IMPORT-411 melibatkan Admin kedua hanya sebagai pengamat lonceng (tidak dipindahkan ke kelas multi-konteks; Sesi B tidak memicu apa pun).
- Alasan melewati sekitar 35 langkah (77 langkah nominal): lima blok homogen (satu job commit per blok dengan pembacaan lonceng), semua satu kelas harness dan berdiri sendiri dengan reset Client E di awal tiap blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-GS-IMPORT-411 diletakkan terakhir karena memakai Sesi B.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan blok mengikuti kebutuhan state: commit yang selesai (413, 414) lebih dulu, lalu pembaruan per batch (412), job yang berhenti (415), dan penerima dua akun (411).
- Pengganti ganti akun: TC-GS-IMPORT-411 Langkah 4 "Login sebagai Admin kedua Client E" dipenuhi dengan Sesi B yang login di hook `before` (langkah 67 dan 74 sampai 77).
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 14, 28, 46, 64), pembukaan halaman dan Sub-Tab, pencatatan baseline (langkah 3, 16, 30, 48, 66, 67), aktivasi kontrol worker, "Tunggu aksi selesai (permintaan mendapat respons)" persis sesudah klik `[Import (N)]` dan sebelum polling (langkah 5, 18, 51; K-16 dan bagian 8b butir 8), penyetelan penanda kemajuan (langkah 53, 56), polling job (langkah 6, 19, 52, 54, 57), membuka dan menutup lonceng, serta langkah 36, 40 (melepas batch) dan 37, 41 (membaca isi tanpa muat ulang), juga langkah 44 (menunggu 5 detik tanpa memuat ulang halaman sebelum asersi absence propagasi SSE; jendela amat SSE, pilihan spec).
- Langkah 45 (tidak ada rekaman "Importing Brand..." baru per batch) adalah asersi absence atas propagasi SSE; didahului langkah 44 (tunggu 5 detik tanpa memuat ulang halaman) supaya absence bukan karena event belum tiba. Anchor positif yang terhubung ke pemicu adalah langkah 34, 38, dan 42 (rekaman yang sama diperbarui in-place).
- P-6 (pengamat read-only): Sesi B pada TC-411 adalah konteks pengamat dalam spec kelas d: login di hook `before`, ditutup di `after`, tanpa interaksi selain membuka Global Settings > Import dan membuka serta membaca lonceng (langkah 67, 74 sampai 77), dan hanya satu TC (TC-411) yang memakainya. Alasan: objek uji adalah notifikasi progres commit dari job latar belakang dan kontrol worker D-47 (kelas d); Sesi B hanya mengamati notifikasi yang diterima Admin kedua dan tidak memicu apa pun.
- Temuan untuk QA:
  - Penanda selesai untuk klik `[Import (N)]` (langkah 5, 18, 51) tidak disebut di TC atau PRD; langkah "Tunggu aksi selesai" memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati.
  - TC-GS-IMPORT-411, 412, 413, 414, 415 tidak merujuk D-47 pada beberapa baris kolom D-ref walau membutuhkan kontrol worker; TC-GS-IMPORT-412 memakai kontrol "jeda setelah tiap batch dan lepas satu batch per perintah" yang setara mode 7 D-47 (jeda sebelum tiap batch).
  - TC-GS-IMPORT-411, 412, 413, 414, 415 mengasersi notifikasi tanpa baseline jumlah; spec menambah baseline jumlah notifikasi (S-12) dan mengasersi pertambahan tepat 1 sebelum membaca isi.
  - TC-GS-IMPORT-415 menulis "menghentikan worker commit setelah batch pertama selesai"; D-47 mendefinisikan "dijeda setelah batch pertama selesai" (mode 3). Spec memakai mode 3.
  - TC-GS-IMPORT-414 Expected b menyebut Unsaved Banner dan kartu Errors 5 tanpa menyebut Banner Hasil Commit sebagai anchor; Banner Hasil Commit dipakai pada Langkah TC 2 hanya sebagai penanda commit selesai.
  - Post Condition TC-GS-IMPORT-411 sampai 415 (draft dihapus atau berisi N baris, N record Brand tersimpan) tidak punya langkah observasi tersendiri selain Expected dan tidak diasersi tambahan (S-01).
