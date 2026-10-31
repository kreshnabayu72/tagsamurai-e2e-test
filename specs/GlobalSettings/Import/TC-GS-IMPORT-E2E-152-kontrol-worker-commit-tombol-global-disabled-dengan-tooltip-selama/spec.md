---
id: TC-GS-IMPORT-E2E-152-kontrol-worker-commit-tombol-global-disabled-dengan-tooltip-selama
title: "Kontrol worker commit: tombol global Disabled dengan tooltip selama committing, fitur baca tetap berfungsi, tanpa toast Preparing"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-373
  - TC-GS-IMPORT-374
  - TC-GS-IMPORT-375
  - TC-GS-IMPORT-387
  - TC-GS-IMPORT-581
  - TC-GS-IMPORT-736
coverage:
  web: automated
---

# Kontrol worker commit: tombol global Disabled dengan tooltip selama committing, fitur baca tetap berfungsi, tanpa toast Preparing

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah state global (kontrol worker commit) dan melakukan commit nyata di Client E yang dipakai bersama spec commit lain; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client E dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; kontrol worker commit tidak dirujuk D-47 pada kolom referensi TC-373, 374, 375, 387, 581, 736 tetapi dibutuhkan semuanya):
  - Kontrol worker commit D-47 mode 2 (dijeda di dalam batch pertama sesudah uji ulang late-binding dan sebelum batch selesai) dan pelepasan jeda (TC-581).
  - Hook umur draft D-76 varian 1 (>=24 jam; `created_at` dimundurkan 25 jam) agar Unsaved Banner dan `[Discard]` tampil.
  - Skrip fixture reset Client E (D-47: hapus draft, lanjutkan worker, hapus Brand hasil commit, reset hasil commit terakhir dan penanda Banner Hasil Commit) dan seeding draft.
  - Jeda nyata: TC-736 mengamati area toast selama 10 detik sebagai satu pengamatan kontinu (di bawah batas ±30 detik; kemampuan pengamatan kontinu disediakan tim FE); TC-581 menunggu job selesai lewat polling "muat ulang setiap 5 detik" (bukan menunggu jam).
- Data Dinamis (milik spec ini; hasil commit dihapus oleh reset):
  - D-56 `brand-250-impor.csv`: `Brand Impor 001` (#1) sampai `Brand Impor 250` (#250), semua valid dan unik.
  - D-57 `brand-250-mixed.csv`: 248 `pending` (`Brand Impor nnn`), baris #5 `error` (Brand Name 121 karakter, nilai sumber Brand pertama tabel D-41, badge saran AI), baris #20 `duplicate` (`Samsung`); batch pertama = baris #1-#4, #6-#19, #21-#102.
  - `brand-250-mutual.csv`: 250 baris `Brand Impor nnn` kecuali baris #10, #11, #12, #13 bernama `Brand Kembar`; baris #10 sampai #12 `duplicate` (duplikat antar-baris), baris #13 `pending` (247 `pending`, 3 `duplicate`).
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): lanjutkan worker commit, hapus draft Client E, hapus Brand hasil commit (`Brand Impor nnn`, `Brand Kembar`), reset hasil commit terakhir, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-736, TC-GS-IMPORT-373, TC-GS-IMPORT-374, TC-GS-IMPORT-387: Satu sesi committing (draft D-56)

1. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
2. Buka Global Settings > Import, pilih Sub-Tab Brand
3. Verifikasi Unsaved Banner tampil
4. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
5. Klik `[Import (250)]`
6. Verifikasi tidak ada toast apa pun pada area toast selama 10 detik sejak klik `[Import (250)]` (pengamatan kontinu, jeda nyata; tidak ada toast "Preparing…")
7. Verifikasi `[Import (250)]` Disabled
8. Muat ulang halaman Import > Brand
9. Hover `[Import (250)]`
10. Verifikasi `[Import (250)]` tampil dan Disabled dengan tooltip "Can't do this while an import is in progress." (TC-736 b)
11. Klik `[Import (250)]`
12. Verifikasi tidak ada dialog yang terbuka
13. Verifikasi tidak ada toast yang tampil
14. Hover `[Discard]` pada Unsaved Banner
15. Verifikasi `[Discard]` tetap tampil dan Disabled
16. Verifikasi tooltip pada `[Discard]` "Can't discard while an import is in progress."
17. Hover `[Upload File]`
18. Verifikasi `[Upload File]` tetap tampil dan Disabled
19. Verifikasi tooltip pada `[Upload File]` "Can't do this while an import is in progress."
20. Atur Rows per page 100
21. Buka halaman 3
22. Buka menu `⋯` baris #230
23. Hover Duplicate
24. Verifikasi row action Duplicate tetap tampil dan Disabled
25. Verifikasi tooltip pada Duplicate "Can't do this while an import is in progress."
26. Hover Edit pada menu yang sama
27. Verifikasi row action Edit tetap tampil dan Disabled
28. Verifikasi tooltip pada Edit "Can't do this while an import is in progress."
29. Tutup menu `⋯` baris #230
30. Hover toggle "Edit this page"
31. Verifikasi toggle "Edit this page" tetap tampil dan Disabled
32. Verifikasi tooltip pada toggle "Edit this page" "Can't do this while an import is in progress."

### TC-GS-IMPORT-375: Kartu Errors, View Data, chip filter, Sub-Tab, Download Template, dan Changelog tetap berfungsi

33. Reset Client E (D-47) dan seed draft Brand D-57 (250 baris: 248 `pending`, 1 `error` baris #5, 1 `duplicate` baris #20) lewat skrip fixture
34. Buka Global Settings > Import, pilih Sub-Tab Brand
35. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
36. Klik `[Import (248)]`
37. Tunggu aksi selesai (permintaan mendapat respons)
38. Muat ulang halaman Import > Brand
39. Verifikasi sedikitnya satu baris tampil pada Staging Table
40. Klik kartu Errors
41. Verifikasi kartu Errors Active
42. Verifikasi tabel hanya menampilkan baris #5
43. Klik `[View Data]` pada baris pesan Error Summary Callout "Brand Name: Max. 120 characters"
44. Verifikasi chip "Showing rows with: Brand Name: Max. 120 characters" dengan `[×]` tampil di atas tabel
45. Verifikasi tabel hanya menampilkan baris #5
46. Klik `[×]` pada chip filter kategori
47. Verifikasi kartu Errors tetap Active
48. Verifikasi chip filter kategori hilang
49. Klik Sub-Tab Measurement
50. Verifikasi Breadcrumb menampilkan "Import > Measurement"
51. Klik Sub-Tab Brand
52. Verifikasi Breadcrumb menampilkan "Import > Brand"
53. Klik `[Download Template]`
54. Verifikasi berkas `Template-Import-Brand.xlsx` terunduh
55. Verifikasi tidak ada toast yang tampil
56. Klik `[Changelog]` di header halaman
57. Verifikasi modal "Changelog: Import" terbuka
58. Tutup modal Changelog (`✕`)

### TC-GS-IMPORT-581: Baris duplicate tetap tampil selama committing dan dihapus saat commit selesai

59. Reset Client E (D-47) dan seed draft Brand `brand-250-mutual.csv` (247 `pending`, 3 `duplicate`) lewat skrip fixture
60. Buka Global Settings > Import, pilih Sub-Tab Brand
61. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
62. Klik `[Import (247)]`
63. Tunggu aksi selesai (permintaan mendapat respons)
64. Muat ulang halaman Import > Brand
65. Atur Rows per page 100
66. Verifikasi kartu Duplicates menampilkan 3
67. Verifikasi baris #10, #11, dan #12 berstatus `duplicate` tampil di Staging Table
68. Lepaskan worker lewat kontrol worker
69. Tunggu commit selesai: muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
70. Verifikasi Dropzone tampil
71. Verifikasi ketiga baris `duplicate` tidak lagi ada di Staging Table dan tidak disisipkan kembali

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (d); objek uji adalah state `committing` yang dibentuk kontrol worker D-47.
- Alasan melewati sekitar 35 langkah (71 langkah nominal): tiga blok homogen (satu sesi committing yang dibagi empat TC, satu sesi committing dengan draft campuran, satu commit sampai selesai), semua satu kelas dan berdiri sendiri dengan reset Client E di awal tiap blok.
- Pembagian TC lintas blok: TC-GS-IMPORT-736, 373, 374, dan 387 diamati pada satu job `committing` yang dibentuk satu kali (langkah 1 sampai 5) karena keempatnya hanya mengamati state yang sama dan job yang sudah `committing` tidak dapat dimulai ulang tanpa reset. Draft D-56 diberi umur >=24 jam (D-76 varian 1) agar `[Discard]` pada Unsaved Banner tampil untuk TC-373; TC-374, 387, dan 736 tidak bergantung pada banner. Langkah 6 (TC-736 a) dilakukan segera setelah klik `[Import (250)]`, sebelum `Verifikasi` artefak langkah 7 dan sebelum muat ulang, sesuai butir 5 dan 11 bagian 8b (state sementara diasersi sebelum langkah yang mengubahnya). Urutan langkah TC-736, 387, 373, 374 mengikuti urutan state halaman, bukan nomor TC.
- TC-GS-IMPORT-387 hanya mengasersi bahwa klik pada tombol Disabled tidak membuka dialog dan tidak menampilkan toast; tooltip `[Import (250)]` diasersi pada langkah 10 (TC-736 b) dan tidak diasersi ulang pada TC-387 a karena nilainya sama.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 33, 59), aktivasi dan pelepasan kontrol worker (langkah 4, 35, 61, 68), pembukaan halaman dan Sub-Tab, hover, pengaturan Rows per page (langkah 20 dan 65; langkah 65 menampilkan baris #10 sampai #12 pada satu halaman), pindah halaman (langkah 21), menutup menu `⋯` (langkah 29), menutup modal Changelog (langkah 58), langkah 37 dan 63 (Tunggu aksi selesai: permintaan mendapat respons, memisahkan klik `[Import (248)]` dan `[Import (247)]` dari muat ulang), dan polling job (langkah 69) yang menunggu job latar belakang dan bukan jam. Langkah 3 dan 38 adalah `Verifikasi` tambahan di luar Expected TC yang menjadi anchor positif (Unsaved Banner tampil pada draft berumur >=24 jam; ada baris sebelum filter), sebelum asersi absence atau asersi universal.
- Langkah 6, 13, 55 adalah asersi absence toast; langkah 6 ditulis segera sesudah pemicu klik `[Import (250)]` dan sebelum `Verifikasi` artefak langkah 7 (`[Import (250)]` Disabled) sesuai butir 11 bagian 8b, sehingga anchor positif menyusul; langkah 12 (absence dialog) didahului langkah 10 yang membuktikan tombol tampil; langkah 54 berkas terunduh mendahului langkah 55.
- Temuan untuk QA:
  - TC-GS-IMPORT-373, 374, 375, 387, 581, 736 tidak merujuk kontrol worker D-47 pada kolom D-ref walau butuh worker dijeda.
  - TC-GS-IMPORT-736 bertanda "Preparing" tanpa PRD; asersi absence toast hanya selama 10 detik (Langkah TC, satu pengamatan kontinu pada langkah 6) dan tidak mencakup toast yang muncul sesudahnya.
  - TC-GS-IMPORT-581 mendefinisikan berkas `brand-250-mutual.csv` secara inline tanpa entri D-xx pada Tabel Data Dinamis; spec mengikuti Data Uji TC.
  - TC-GS-IMPORT-581 Post Condition b ("247 record Brand baru tersimpan") tidak punya langkah observasi dan tidak diasersi (S-01); hook `after` menghapus Brand hasil commit.
  - Post Condition TC-GS-IMPORT-373, 374, 375, 387, 736 ("job Brand Client E berstatus committing dengan worker dijeda; draft tetap 250 baris") tidak punya langkah observasi tersendiri dan tidak diasersi.
  - TC-GS-IMPORT-375 Expected b menyebut chip "Showing rows with: Brand Name: Max. 120 characters" dengan `[×]`; spec memecahnya menjadi chip tampil (langkah 43) dan tabel hanya baris #5 (langkah 44).
