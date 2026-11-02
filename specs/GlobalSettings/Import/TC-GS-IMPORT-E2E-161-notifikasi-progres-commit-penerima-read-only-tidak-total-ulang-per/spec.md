---
id: TC-GS-IMPORT-E2E-161-notifikasi-progres-commit-penerima-read-only-tidak-total-ulang-per
title: "Notifikasi progres commit: penerima (Read Only tidak), total ulang per batch, enam Import Type, Processed termasuk baris gagal"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-416
  - TC-GS-IMPORT-417
  - TC-GS-IMPORT-418
  - TC-GS-IMPORT-847
coverage:
  web: automated
---

# Notifikasi progres commit: penerima (Read Only tidak), total ulang per batch, enam Import Type, Processed termasuk baris gagal

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec melakukan commit nyata di Client E, mengubah state global (kontrol worker commit) dan master data Client E (lima Brand buatan Admin kedua), dan notifikasi lonceng bersifat permanen sehingga asersi memakai baseline; lihat `suite.md`.
- Dua konteks browser, ditandai `[Sesi A]` dan `[Sesi B]` (hanya TC-416 memakai Sesi B). Langkah tanpa tanda dijalankan di Sesi A:
  - Sesi A (aktor): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Login di hook `before`; layar awal Global Settings > Import dibuka hook `beforeEach`.
  - Sesi B (pengamat): Import data (Read Only) Client E (Indra Gunawan) `importRead_automated_qaTeam5@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTE_IMPORTRO_PASSWORD`. Login di hook `before` pada konteks browser terpisah.
  - Pelaku kedua (pemicu): Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTE_TC2_PASSWORD`, memakai sesi API untuk membuat lima Brand pada TC-847 (P-2).
  - Password tidak ditulis di spec atau fixture.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk kedua akun UI spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; TC-416, 417, 418, 847 tidak merujuk D-47 pada kolom D-ref pada sebagian baris tetapi membutuhkannya):
  - Kontrol worker commit D-47: mode 1 (dijeda sebelum job mulai) untuk TC-416 dan TC-418; mode 7 (dijeda sebelum tiap batch, satu batch per perintah lepas) untuk TC-417 dan TC-847.
  - Notifikasi lonceng diperbarui via SSE (tanpa muat ulang halaman).
  - Jendela amat SSE 5 detik (langkah 10) adalah pilihan spec (bukan nilai TC atau PRD) sampai TC menyatakan durasinya.
  - Sesi API Admin kedua Client E untuk membuat Brand `Brand Impor 010`, `020`, `030`, `040`, `050` (TC-847).
  - Skrip fixture reset Client E (D-47: hapus draft, lanjutkan worker, hapus Brand, User Login, User Non Login, Division, Position hasil commit, termasuk lima Brand buatan Admin kedua, reset hasil commit terakhir) dan seeding draft.
  - Jeda nyata: polling "muat ulang setiap 5 detik" menunggu job latar belakang (bukan menunggu jam).
- Baseline notifikasi (S-12): jumlah notifikasi lonceng dengan judul yang diasersi dicatat sebelum aksi pemicu pertama tiap blok; asersi "notifikasi baru" memakai selisih terhadap baseline, bukan posisi atau angka absolut.
- Data Dinamis (milik spec ini; draft dibuang dan hasil commit dihapus oleh reset):
  - D-56 `brand-250-impor.csv`: `Brand Impor 001` sampai `Brand Impor 250`, semua valid dan unik (TC-416, 417, 847); pada TC-847 lima Brand buatan Admin kedua bernama sama dengan baris #10, #20, #30, #40, #50 (anggota batch pertama).
  - Enam draft TC-418 (semua `pending`, tanpa `error` dan `duplicate`): D-50 Brand 12 baris, D-51 Measurement 6 baris (`Meter/m`, `Liter/l`, `Gram/g`, `Centimeter/cm`, `Pack/pk`, `Dozen/dz`), D-52 Position 6 baris (`Store Supervisor`, `HR Business Partner`, `IT Operations Lead`, `Warehouse Staff`, `Procurement Officer`, `Sales Executive`), D-53 Division 6 baris (`Finance & Accounting`/FIN, `Operations`, `IT Support`/ITS, `Procurement`/PRC, `Sales`/SLS, `Legal`/LGL), D-54 User Login 8 baris, D-55 User Non Login 5 baris.
  - Tabel "Pasangan Import Type" (TC-418; langkah 67 sampai 79 diulang untuk tiap baris):

    | Sub-Tab | Tombol | Judul awal | Isi awal | Judul akhir | Isi akhir |
    |---|---|---|---|---|---|
    | Brand | `[Import (12)]` | "Importing Brand..." | "0 of 12 records processed." | "Import Brand completed" | "12 records imported." |
    | Measurement | `[Import (6)]` | "Importing Measurement..." | "0 of 6 records processed." | "Import Measurement completed" | "6 records imported." |
    | Position | `[Import (6)]` | "Importing Position..." | "0 of 6 records processed." | "Import Position completed" | "6 records imported." |
    | Division | `[Import (6)]` | "Importing Division..." | "0 of 6 records processed." | "Import Division completed" | "6 records imported." |
    | User Login | `[Import (8)]` | "Importing User Login..." | "0 of 8 records processed." | "Import User Login completed" | "8 records imported." |
    | User Non Login | `[Import (5)]` | "Importing User Non Login..." | "0 of 5 records processed." | "Import User Non Login completed" | "5 records imported." |
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): lanjutkan worker commit, hapus draft Client E, hapus seluruh record hasil commit dan lima Brand buatan Admin kedua, reset hasil commit terakhir, tutup konteks Sesi B, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-416: Admin Import data (Read Only) tidak menerima notifikasi progres commit

1. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) lewat skrip fixture
2. [Sesi B] Buka notifikasi lonceng, catat jumlah notifikasi sebagai baseline Sesi B, lalu tutup lonceng
3. [Sesi A] Muat ulang halaman Import > Brand
4. [Sesi A] Buka notifikasi lonceng, catat jumlah rekaman "Importing Brand..." sebagai baseline Sesi A, lalu tutup lonceng
5. Aktifkan kontrol worker commit mode 1 (dijeda sebelum batch pertama diproses)
6. [Sesi A] Klik `[Import (250)]`
7. [Sesi A] Tunggu aksi selesai (permintaan mendapat respons)
8. [Sesi A] Buka notifikasi lonceng
9. [Sesi A] Verifikasi jumlah rekaman "Importing Brand..." bertambah tepat 1 dari baseline langkah 4 (notifikasi dipancarkan)
10. Tunggu 5 detik tanpa memuat ulang halaman
11. [Sesi B] Buka notifikasi lonceng
12. [Sesi B] Verifikasi jumlah notifikasi sama dengan baseline langkah 2
13. [Sesi B] Verifikasi lonceng tidak memuat "Importing Brand..."

### TC-GS-IMPORT-417: Total dihitung ulang tiap batch

14. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) lewat skrip fixture
15. Muat ulang halaman Import > Brand
16. Buka notifikasi lonceng, catat jumlah rekaman "Importing Brand..." dan "Import Brand completed" sebagai baseline, lalu tutup lonceng
17. Aktifkan kontrol worker commit mode 7 (dijeda sebelum tiap batch; satu batch per perintah lepas)
18. Klik `[Import (250)]`
19. Tunggu aksi selesai (permintaan mendapat respons)
20. Muat ulang halaman Import > Brand
21. Atur Rows per page 100
22. Buka halaman 3
23. Buka menu `⋯` baris #230
24. Pilih Remove
25. Klik `[Delete]` pada dialog Delete Row
26. Verifikasi toast sukses "Success, row has been deleted."
27. Lepaskan batch pertama lewat kontrol worker commit
28. Buka notifikasi lonceng
29. Verifikasi jumlah rekaman "Importing Brand..." bertambah tepat 1 dari baseline langkah 16
30. Verifikasi notifikasi baru "Importing Brand..." berisi "100 of 249 records processed."
31. Lepaskan semua batch yang tersisa lewat kontrol worker commit
32. Tunggu commit selesai: muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
33. Buka notifikasi lonceng
34. Verifikasi jumlah notifikasi "Import Brand completed" bertambah tepat 1 dari baseline langkah 16
35. Verifikasi notifikasi baru "Import Brand completed" berisi "249 records imported."

### TC-GS-IMPORT-847: Processed mencakup baris yang gagal uji ulang

36. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) lewat skrip fixture
37. Muat ulang halaman Import > Brand
38. Buka notifikasi lonceng, catat jumlah rekaman "Importing Brand..." dan "Import Brand completed" sebagai baseline, lalu tutup lonceng
39. Aktifkan kontrol worker commit mode 7 (dijeda sebelum tiap batch; satu batch per perintah lepas)
40. Klik `[Import (250)]`
41. Tunggu aksi selesai (permintaan mendapat respons)
42. Buka notifikasi lonceng
43. Verifikasi jumlah rekaman "Importing Brand..." bertambah tepat 1 dari baseline langkah 38
44. Verifikasi notifikasi baru "Importing Brand..." berisi "0 of 250 records processed."
45. Verifikasi notifikasi baru "Importing Brand..." tanpa tombol aksi
46. Buat Brand `Brand Impor 010`, `Brand Impor 020`, `Brand Impor 030`, `Brand Impor 040`, dan `Brand Impor 050` di halaman Master Reference > Brand atas nama Admin kedua Client E lewat fixture (sesi API) hingga kelima Brand tersimpan
47. Lepaskan batch pertama lewat kontrol worker commit
48. Baca isi rekaman baru "Importing Brand..." di lonceng tanpa memuat ulang halaman
49. Verifikasi isi rekaman yang sama menjadi "100 of 250 records processed."
50. Lepaskan batch kedua lewat kontrol worker commit
51. Baca isi rekaman baru "Importing Brand..." di lonceng tanpa memuat ulang halaman
52. Verifikasi isi rekaman yang sama menjadi "200 of 250 records processed."
53. Lepaskan batch terakhir lewat kontrol worker commit
54. Tunggu commit selesai: muat ulang halaman Import > Brand setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
55. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 5 errors remain." tampil
56. Buka notifikasi lonceng
57. Verifikasi jumlah notifikasi "Import Brand completed" bertambah tepat 1 dari baseline langkah 38
58. Verifikasi notifikasi baru "Import Brand completed" berisi "245 records imported. 5 errors remain."
59. Verifikasi notifikasi baru "Import Brand completed" memuat tombol `[Detail]`
60. Tutup lonceng
61. Verifikasi Staging Table menampilkan 5 baris berstatus `error`
62. Verifikasi baris bernomor 1 sampai 5 berurutan `Brand Impor 010`, `Brand Impor 020`, `Brand Impor 030`, `Brand Impor 040`, `Brand Impor 050`
63. Verifikasi Error Summary Callout memuat "Brand name already exists" dengan badge "5 rows"

### TC-GS-IMPORT-418: Judul dan isi notifikasi memakai Import Type bersangkutan untuk keenam Import Type

64. Reset Client E (D-47) dan seed enam draft (D-50 sampai D-55), satu per Sub-Tab, lewat skrip fixture
65. Muat ulang halaman Import
66. Untuk setiap baris tabel "Pasangan Import Type" pada Prerequisites, lakukan langkah 67 sampai 79 (enam iterasi)
67. Pilih Sub-Tab sesuai baris tabel
68. Buka notifikasi lonceng, catat jumlah rekaman berjudul awal dan berjudul akhir baris tabel sebagai baseline, lalu tutup lonceng
69. Aktifkan kontrol worker commit mode 1 (dijeda sebelum batch pertama diproses)
70. Klik tombol `[Import (n)]` sesuai baris tabel
71. Tunggu aksi selesai (permintaan mendapat respons)
72. Buka notifikasi lonceng
73. Verifikasi jumlah rekaman berjudul awal bertambah tepat 1 dari baseline langkah 68
74. Verifikasi notifikasi baru memuat judul awal dan isi awal sesuai baris tabel
75. Lepaskan worker lewat kontrol worker commit
76. Tunggu commit selesai: muat ulang halaman Import setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
77. Buka notifikasi lonceng
78. Verifikasi jumlah rekaman berjudul akhir bertambah tepat 1 dari baseline langkah 68
79. Verifikasi notifikasi baru memuat judul akhir dan isi akhir sesuai baris tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (d); objek uji adalah notifikasi progres commit yang dihasilkan job latar belakang dan kontrol worker D-47. Admin kedua hanya pemicu lewat sesi API pada TC-847 (P-2); Sesi B pada TC-416 hanya mengamati lonceng akun Import data (Read Only) dan hasilnya diasersi, sehingga ia konteks UI kedua.
- Alasan melewati sekitar 35 langkah (79 langkah nominal; ekspansi langkah 67 sampai 79 dikali enam iterasi memberi sekitar 144 langkah): empat blok satu kelas harness yang berdiri sendiri dengan reset Client E di awal tiap blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah 67 sampai 79 diulang untuk setiap baris tabel "Pasangan Import Type" tanpa langkah bersyarat; parameter tiap iterasi ada di tabel Prerequisites dan `Verifikasi` tetap satu per klausa.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan blok mengikuti kebutuhan state; blok enam Import Type diletakkan terakhir karena menghasilkan commit di keenam Sub-Tab.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 14, 36, 64), pembukaan dan muat ulang halaman Import dan Sub-Tab, pencatatan baseline (langkah 2, 4, 16, 38, 68), aktivasi dan pelepasan kontrol worker, pemicu sesi API (langkah 46; "hingga kelima Brand tersimpan"), polling job (langkah 32, 54, 76), membuka dan menutup lonceng, serta pembacaan isi tanpa muat ulang (langkah 48, 51), serta langkah 10 (menunggu 5 detik tanpa memuat ulang sebelum asersi absence propagasi SSE; jendela amat SSE, pilihan spec). Langkah 7, 19, 41, dan 71 (Tunggu aksi selesai: permintaan mendapat respons) mengikuti klik `[Import (N)]` pada langkah 6, 18, 40, dan 70 serta mendahului pembukaan lonceng atau muat ulang halaman (bagian 8b butir 8).
- Langkah 13 (tidak ada "Importing Brand..." di lonceng Sesi B) adalah asersi absence atas propagasi SSE; didahului langkah 10 (tunggu 5 detik tanpa memuat ulang halaman) supaya absence bukan karena event belum tiba. Anchor positif yang terhubung ke pemicu adalah langkah 9 (notifikasi dipancarkan ke Sesi A), sesuai Expected a TC-416.
- P-6 (pengamat read-only): Sesi B pada TC-416 adalah konteks pengamat read-only dalam spec kelas d: login di hook `before`, ditutup di `after`, tanpa interaksi selain membuka dan membaca lonceng, dan hanya satu TC (TC-416) yang memakainya. Alasan: objek uji adalah notifikasi progres commit dari job latar belakang dan kontrol worker D-47 (kelas d); Sesi B hanya mengamati bahwa penerima Import data (Read Only) tidak menerima notifikasi.
- Temuan untuk QA:
  - TC-GS-IMPORT-417, 847, 418 tidak menulis baseline jumlah untuk rekaman "Importing Brand..." (417, 847) maupun judul akhir (418); spec menambah baseline dan `Verifikasi` pertambahan tepat 1 sebelum membaca isi (langkah 16 dan 29, 38 dan 43, 68 dan 78; S-12, D-14). Kemampuan membaca jumlah rekaman lonceng per judul sama dengan yang dipakai baseline langkah 4.
  - TC-GS-IMPORT-416, 417, 418, 847 tidak merujuk D-47 pada beberapa baris kolom D-ref; TC-GS-IMPORT-417 menyebut kontrol "menjeda worker di dalam batch pertama dan melepasnya satu batch per perintah", gabungan mode 2 dan mode 7 D-47; spec memakai mode 7 (jeda sebelum tiap batch, satu batch per perintah).
  - TC-GS-IMPORT-416 Langkah 1 dan 7 menyebut login ke Import data (Read Only) dua kali; spec memakai Sesi B yang login di hook `before` dan membaca lonceng tanpa ganti akun.
  - TC-GS-IMPORT-418 menyatakan hasil akhir dibaca "setelah langkah 6" untuk tiap Import Type tanpa baseline notifikasi; spec memakai baseline jumlah rekaman berjudul awal.
  - TC-GS-IMPORT-847 langkah 4 membuat Brand `Brand Impor 010`, `020`, `030`, `040`, `050` atas nama Admin kedua "lewat fixture" tanpa menyebut mekanisme; disediakan tim FE/BE dan dibersihkan di hook `after`.
  - Post Condition TC-GS-IMPORT-416 sampai 418 dan 847 (draft dihapus atau berisi 5 baris `error`, record hasil commit tersimpan) tidak punya langkah observasi tersendiri selain Expected dan tidak diasersi tambahan (S-01).
  - Penanda selesai untuk pemicu sesi API atau fixture tidak disebut di TC atau PRD; langkah "Tunggu aksi selesai" memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati di surface aktor UI.
