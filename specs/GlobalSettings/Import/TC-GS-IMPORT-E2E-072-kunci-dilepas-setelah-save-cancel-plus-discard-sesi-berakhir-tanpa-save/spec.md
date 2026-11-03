---
id: TC-GS-IMPORT-E2E-072-kunci-dilepas-setelah-save-cancel-plus-discard-sesi-berakhir-tanpa-save
title: "Kunci Dilepas: Setelah Save, Cancel plus Discard, Sesi Berakhir Tanpa Save, Navigasi Sidebar, Klik Sel Tanpa Mengambil Kunci, dan Tab Ditutup"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-191
  - TC-GS-IMPORT-255
  - TC-GS-IMPORT-256
  - TC-GS-IMPORT-661
  - TC-GS-IMPORT-678
  - TC-GS-IMPORT-871@L1080
coverage:
  web: automated
---

# Kunci Dilepas: Setelah Save, Cancel plus Discard, Sesi Berakhir Tanpa Save, Navigasi Sidebar, Klik Sel Tanpa Mengambil Kunci, dan Tab Ditutup

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Dua sesi browser (kelas multi-konteks), konteks terpisah dengan sesi login sendiri:
  - Client A (TC-GS-IMPORT-255, 256, 661, 678, 871@L1080; keduanya login di hook `before`): Sesi TC Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`; Sesi Admin kedua Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC2_PASSWORD`.
  - Client E (TC-GS-IMPORT-191; login lewat langkah ganti akun): Sesi TC Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`, `Spectra.env.GS_CLIENTE_TC_PASSWORD`; Sesi Admin kedua Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net`, `Spectra.env.GS_CLIENTE_TC2_PASSWORD`.
  - Password tidak ditulis di spec atau fixture. Hook `after` menutup konteks Sesi Admin kedua dan mengembalikan sesi ke akun default suite.
- Data Dinamis: Client A D-01 draft Brand 12 baris `pending` dari `brand-12.csv` (Row # 1 `Acme Corp`, #2 `Lenovo`), dipulihkan oleh hook `beforeEach` suite dan, sesudah TC-GS-IMPORT-255, oleh langkah 11. Client E (direset dan di-seed oleh langkah 54, Kontrak Fixture R1): D-58 draft Brand 15 baris dari `brand-partial-15.csv` (#1-#9 `pending`; #10 dan #11 `Brand Kembar` `duplicate`; #12 `Brand Kembar` `pending`; #13 `Samsung` `duplicate`; #14 dan #15 `error`).
- Tabel varian TC-GS-IMPORT-678 (aksi varian pada langkah 26, dalam loop langkah 26 sampai 32; aksi Sesi TC yang mengakhiri sesi edit):

| Varian | Aksi Sesi TC |
|---|---|
| 1 Cancel tanpa perubahan | klik `⋯` baris #1, pilih Edit, klik `[Cancel]` |
| 2 Switch dimatikan tanpa perubahan | aktifkan Switch `Edit this page` lalu matikan |
| 3 Save tanpa perubahan | klik `⋯` baris #1, pilih Edit, klik `[Save]` (toast "No changes to save.") |
| 4 Leave | klik `⋯` baris #1, pilih Edit, ubah Brand Name menjadi `Acme Corporation`, klik menu sidebar Global Settings > User, klik `[Leave]` |

- Kemampuan teknis yang disediakan tim FE/BE: menangani dialog native browser `beforeunload` dan menutup tab (TC-GS-IMPORT-871@L1080, bertanda Manual Only di TC); fixture jam server hanya untuk membaca bahwa jam tidak dimajukan.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk kedua sesi. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk semua akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft D-01 dipulihkan antar TC; Client E direset sesuai D-47 sesudah TC-GS-IMPORT-191.

## Test Steps

### TC-GS-IMPORT-255: Kunci dilepas setelah Save berhasil

1. [Sesi TC] Klik `⋯` pada baris #1
2. [Sesi TC] Pilih Edit
3. [Sesi TC] Ubah Brand Name baris #1 menjadi `Acme Corporation`
4. [Sesi TC] Klik `[Save]`
5. [Sesi TC] Tunggu aksi selesai (permintaan mendapat respons)
6. [Sesi Admin kedua] Klik `⋯` pada baris #2
7. [Sesi Admin kedua] Pilih Edit
8. [Sesi Admin kedua] Verifikasi baris #2 menjadi input aktif
9. [Sesi Admin kedua] Verifikasi footer menampilkan `[Cancel]` dan `[Save]`
10. [Sesi Admin kedua] Verifikasi tidak ada dialog
11. [Sesi Admin kedua] Klik `[Cancel]` pada footer; pulihkan draft D-01
12. [Sesi TC] Muat ulang halaman Import > Brand
13. [Sesi Admin kedua] Muat ulang halaman Import > Brand

### TC-GS-IMPORT-256: Kunci dilepas setelah Cancel dengan perubahan dilanjutkan Discard

14. [Sesi TC] Klik `⋯` pada baris #1
15. [Sesi TC] Pilih Edit
16. [Sesi TC] Ubah Brand Name baris #1 menjadi `Acme Corporation`
17. [Sesi TC] Klik `[Cancel]`
18. [Sesi TC] Klik `[Discard]` pada dialog
19. [Sesi TC] Tunggu aksi selesai (dialog tertutup)
20. [Sesi Admin kedua] Klik `⋯` pada baris #2
21. [Sesi Admin kedua] Pilih Edit
22. [Sesi Admin kedua] Verifikasi baris #2 menjadi input aktif
23. [Sesi Admin kedua] Verifikasi footer menampilkan `[Cancel]` dan `[Save]`
24. [Sesi Admin kedua] Verifikasi tidak ada dialog
25. [Sesi Admin kedua] Klik `[Cancel]` pada footer

### TC-GS-IMPORT-678: Kunci dilepas setelah sesi edit berakhir tanpa Save

Untuk setiap varian pada tabel varian (langkah 26 sampai 32):

26. [Sesi TC] Buka menu Import dari sidebar, lalu lakukan aksi varian sampai sesi edit berakhir
27. [Sesi TC] Tunggu aksi selesai (permintaan mendapat respons)
28. [Sesi Admin kedua] Klik `⋯` pada baris #2
29. [Sesi Admin kedua] Pilih Edit
30. [Sesi Admin kedua] Verifikasi baris #2 menjadi input aktif
31. [Sesi Admin kedua] Verifikasi footer menampilkan `[Cancel]` dan `[Save]`
32. [Sesi Admin kedua] Verifikasi dialog "Draft Is Being Edited" tidak tampil, lalu klik `[Cancel]` pada footer

### TC-GS-IMPORT-661: Navigasi sidebar tanpa perubahan melepas kunci

33. [Sesi TC] Buka menu Import dari sidebar; klik `⋯` pada baris #1
34. [Sesi TC] Pilih Edit
35. [Sesi TC] Klik menu sidebar Global Settings > User
36. [Sesi TC] Verifikasi tidak ada dialog yang tampil
37. [Sesi TC] Verifikasi halaman Global Settings > User terbuka
38. [Sesi Admin kedua] Klik `⋯` pada baris #2
39. [Sesi Admin kedua] Pilih Edit
40. [Sesi Admin kedua] Verifikasi baris #2 menjadi input aktif
41. [Sesi Admin kedua] Verifikasi footer menampilkan `[Cancel]` dan `[Save]` tanpa dialog
42. [Sesi Admin kedua] Klik `[Cancel]` pada footer

### TC-GS-IMPORT-871 (baris L1080): Menutup tab pemegang melepas kunci best-effort

43. [Sesi TC] Buka menu Import dari sidebar; klik `⋯` pada baris #1
44. [Sesi TC] Pilih Edit
45. [Sesi TC] Tutup tab Import Client A dan pilih keluar pada dialog native browser
46. [Sesi TC] Tunggu aksi selesai (tab tertutup)
47. [Sesi Admin kedua] Klik `⋯` pada baris #2
48. [Sesi Admin kedua] Pilih Edit
49. [Sesi Admin kedua] Verifikasi baris #2 menjadi input aktif
50. [Sesi Admin kedua] Verifikasi footer menampilkan `[Cancel]` dan `[Save]`
51. [Sesi Admin kedua] Verifikasi tidak ada dialog Konflik Kunci Sesi
52. [Sesi Admin kedua] Verifikasi jam server tidak dimajukan: sejak sesi edit dimulai belum lewat 10 menit
53. [Sesi Admin kedua] Klik `[Cancel]` pada footer
54. Reset Client E ke tanpa draft; seed draft D-58 lewat skrip fixture

### TC-GS-IMPORT-191: Klik sel tidak memulai sesi edit dan tidak mengambil kunci

55. Ganti akun: Sesi TC login sebagai Total Control Client E dan Sesi Admin kedua login sebagai Admin kedua Client E; keduanya membuka Import > Brand (draft D-58)
56. [Sesi TC] Klik sel Brand Name baris #1 (status `pending`)
57. [Sesi TC] Verifikasi tidak ada sel atau baris yang berubah menjadi input
58. [Sesi TC] Verifikasi tidak ada dialog
59. [Sesi TC] Verifikasi footer tetap `[Import (10)]` tanpa `[Cancel]` dan `[Save]`
60. [Sesi TC] Klik sel Brand Name baris #10 (status `duplicate`)
61. [Sesi TC] Verifikasi tidak ada sel atau baris yang berubah menjadi input
62. [Sesi TC] Verifikasi tidak ada dialog
63. [Sesi TC] Verifikasi footer tetap `[Import (10)]` tanpa `[Cancel]` dan `[Save]`
64. [Sesi TC] Klik halaman 2 pada Pagination
65. [Sesi TC] Klik sel Brand Name baris #14 (status `error`)
66. [Sesi TC] Verifikasi tidak ada sel atau baris yang berubah menjadi input
67. [Sesi TC] Verifikasi tidak ada dialog
68. [Sesi TC] Verifikasi footer tetap `[Import (10)]` tanpa `[Cancel]` dan `[Save]`
69. [Sesi TC] Verifikasi Pagination tetap `Showing 11 - 15 of 15 items`
70. [Sesi Admin kedua] Klik `⋯` pada baris #1
71. [Sesi Admin kedua] Pilih Edit
72. [Sesi Admin kedua] Verifikasi baris #1 menjadi input aktif untuk Admin kedua
73. [Sesi Admin kedua] Verifikasi footer Admin kedua menampilkan `[Cancel]` dan `[Save]`
74. [Sesi Admin kedua] Verifikasi dialog "Draft Is Being Edited" tidak tampil (klik sel tidak mengambil kunci sesi edit)
75. [Sesi Admin kedua] Klik `[Cancel]` pada footer; reset Client E ke tanpa draft

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: multi-konteks (kelas c, prinsip 13c); asersi pada sesi UI kedua (Admin kedua) menjadi objek uji pelepasan kunci.
- Spec memuat 75 langkah (langkah 26 sampai 32 diulang 4 varian; ekspansi sekitar 96 langkah), di atas smell 35 langkah. Alasan: semua blok satu kelas harness (dua sesi admin) dengan pola identik (Sesi TC melepas kunci, Admin kedua langsung dapat memulai sesi edit) dan tiap blok berdiri sendiri; TC-GS-IMPORT-191 memakai Client E dengan ganti akun eksplisit (langkah 55) dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal. Parameter varian ada di tabel Prerequisites.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 11, 25, 32 (bagian klik), 42, 53, 75 (menutup sesi edit Admin kedua dan memulihkan draft), langkah 12 dan 13 (memuat ulang halaman kedua sesi sesudah draft dipulihkan), langkah 26, 33, 43 (membuka kembali halaman Import untuk Sesi TC), langkah 54 (reset dan seed fixture Client E), langkah 55 (ganti akun), langkah 64 (pindah halaman), langkah 5, 19, 27, 46 (menunggu aksi Sesi TC selesai sebelum Sesi Admin kedua bertindak; langkah 27 bagian dari varian).
- Pembagian TC lintas spec: nomor TC-GS-IMPORT-871 dipakai dua baris; spec ini memuat baris L1080 (tab ditutup) dan baris L938 (Code Division manual) berada di spec lain. TC-GS-IMPORT-868@L1077 dan 870@L1079 ada di spec 073; 869@L1078 di spec 077.
- Temuan untuk QA:
  - ID ganda TC-GS-IMPORT-868 (L738 dan L1077), 869 (L937 dan L1078), 870 (L1020 dan L1079), 871 (L938 dan L1080) dengan isi berbeda; `sourceTc` dan `check-suite.py` tidak dapat membedakannya. Usulan: QA memberi nomor baru pada empat baris di L1077-L1080.
  - TC-GS-IMPORT-871@L1080 bertanda Manual Only dan Expected b ("Jam server tidak dimajukan") tidak memuat langkah observasi; spec menuliskannya sebagai `Verifikasi` berbasis pembacaan jam server oleh fixture. Pelepasan best-effort saat tab ditutup konsisten dengan IMP-LOGIC-04 tetapi tidak ada TC yang menetapkan perilaku defaultnya secara pasti (bandingkan TC-GS-IMPORT-207 yang mengasumsikan pelepasan gagal).
  - Penanda "tab tertutup" pada langkah 46 tidak ada di TC-GS-IMPORT-871@L1080; spec memakai penanda itu sebagai langkah penghubung.
  - TC-GS-IMPORT-191 memakai Client E sedangkan TC lain di spec ini memakai Client A.
  - Penanda selesai untuk langkah 5 dan 27 (setelah `[Save]` dan setelah aksi varian pada TC-GS-IMPORT-678) tidak ada di TC; spec memakai "permintaan mendapat respons" sebagai penanda tunggu tanpa hasil UI.
