---
id: TC-GS-FILEMGR-E2E-037-lintas-surface-search-tanggal-visibilitas-filter-dan-ikon-sort
title: "Lintas Tiga Surface: Search Kolom Tanggal, Search Terikat Visibilitas Kolom, Filter Tanpa Apply, Search Dropdown Filter, dan Ikon Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-118
  - TC-GS-FILEMGR-121
  - TC-GS-FILEMGR-134
  - TC-GS-FILEMGR-139
  - TC-GS-FILEMGR-149
coverage:
  web: automated
---

# Lintas Tiga Surface: Search Kolom Tanggal, Search Terikat Visibilitas Kolom, Filter Tanpa Apply, Search Dropdown Filter, dan Ikon Sort

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data File Manager.
- Akun: Total Control `Sinta Maharani`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login akun ini dilakukan sekali di hook `before`; layar awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Tabel A2 (33 file aktif, tabel utama), Tabel A3 (16 file Recycle Bin: `old-avatar.png` s.d. `recycled-photo-12.jpg`, Deleted By Sinta Maharani, Agus Wibowo, System; retensi 30 hari) dan Tabel A4 (14 entri Changelog `C01` s.d. `C14`; `C03` = `stale-avatar.png`, Modified By Agus Wibowo). Ukuran halaman 10; format tanggal General Settings default `dd/MM/yy HH:mm`. Hook `before` memastikan dataset File Manager client sama dengan Tabel A2, A3, dan A4 (tanpa sisa file atau Recycle Bin dari spec lain) lewat fixture BE yang disediakan tim FE/BE (mekanisme tidak tertulis di TC; lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); hitungan baris tabel utama dan Recycle Bin dalam spec ini mengasumsikan dataset Tabel A2 dan A3 segar tanpa sisa dari spec lain. Changelog adalah audit trail permanen yang tidak dapat di-seed ulang atau dibersihkan dan spec lain menambah entri (S-12), sehingga jumlah entri Changelog tidak diasersi sebagai angka absolut: langkah 53 mencatat baseline jumlah entri total pada pagination sebelum Action dipilih dan langkah 66 membandingkannya.
- Flag Guided Tooltip halaman File Manager: mengikuti pernyataan hook suite di `suite.md` (flag `guided_tooltip_seen_<page_key>` true untuk akun aktor); spec ini tidak mengubahnya.
- Data uji: tabel utama Search `2.4 MB`, `02/09/26` (Upload Date F01), File Format `JPEG`, opsi dropdown `jp`; Recycle Bin Search `Agus`, `29 days` (Auto-Purge In R01), teks Deleted Date baris `old-avatar.png` (dibaca dari tabel, relatif waktu uji), File Format `PNG`, opsi dropdown `PN`; Changelog Search `Agus`, `14/09/26` (Date C01), Action `Delete`, opsi dropdown `perm`.
- Kemampuan teknis: Column Visibility lewat header kolom Actions (`⋯`) pada tabel utama, modal Recycle Bin, dan modal Changelog; membaca teks sel Deleted Date; membaca jumlah entri total pada pagination Changelog; membuka dan menutup modal Recycle Bin dan Changelog (modal kembali ke default setiap dibuka, NC-21).
- Cleanup: hook `after` menutup modal yang terbuka, mengosongkan Search dan Filter, dan menampilkan semua kolom pada tabel utama, Recycle Bin, dan Changelog (preferensi UI).

## Test Steps

### Tabel utama

1. Verifikasi header kolom Checkbox dan kolom Actions `(⋯)` tabel utama tanpa ikon sort (TC-GS-FILEMGR-149)
2. Klik ikon Filter di toolbar (TC-GS-FILEMGR-139)
3. Buka dropdown `File Format`
4. Ketik `jp` di kotak pencarian dropdown
5. Verifikasi opsi yang tampil hanya `JPEG` dan `JPG`
6. Kosongkan kotak pencarian dropdown
7. Tutup dropdown `File Format`
8. Pilih `JPEG` pada `File Format` tanpa `[Apply]` (TC-GS-FILEMGR-134)
9. Klik ikon Filter untuk menutup panel
10. Klik ikon Filter untuk membuka kembali panel
11. Verifikasi field `File Format` kosong
12. Verifikasi tabel tetap menampilkan 33 baris
13. Klik ikon Filter untuk menutup panel
14. Sembunyikan kolom `Size` lewat Column Visibility (header kolom Actions `⋯`) (TC-GS-FILEMGR-121)
15. Ketik Search `2.4 MB`, tekan Enter
16. Verifikasi empty state `No results found` tampil
17. Tampilkan kembali kolom `Size` lewat Column Visibility
18. Ganti isi kotak search dengan `2.4 MB`, tekan Enter
19. Verifikasi tabel hanya memuat satu baris `budi-avatar.jpg`
20. Ganti isi kotak search dengan `02/09/26`, tekan Enter (TC-GS-FILEMGR-118)
21. Verifikasi empty state `No results found` tampil untuk Upload Date `02/09/26`
22. Klik `(←)` pada kotak Search

### Modal Recycle Bin

23. Klik tombol Recycle Bin di toolbar
24. Verifikasi header kolom Checkbox dan kolom Actions `(⋯)` Recycle Bin tanpa ikon sort (TC-GS-FILEMGR-149)
25. Klik ikon Filter di modal Recycle Bin (TC-GS-FILEMGR-139)
26. Buka dropdown `File Format`
27. Ketik `PN` di kotak pencarian dropdown
28. Verifikasi opsi yang tampil hanya `PNG`
29. Kosongkan kotak pencarian dropdown
30. Tutup dropdown `File Format`
31. Pilih `PNG` pada `File Format` tanpa `[Apply]` (TC-GS-FILEMGR-134)
32. Klik ikon Filter untuk menutup panel
33. Klik ikon Filter untuk membuka kembali panel
34. Verifikasi field `File Format` kosong
35. Verifikasi tabel Recycle Bin tetap menampilkan 16 baris
36. Klik ikon Filter untuk menutup panel
37. Sembunyikan kolom `Deleted By` lewat Column Visibility (TC-GS-FILEMGR-121)
38. Ketik Search `Agus`, tekan Enter
39. Verifikasi empty state `No results found` tampil
40. Verifikasi baris `expired-avatar.jpg` tidak tampil
41. Tampilkan kembali kolom `Deleted By` lewat Column Visibility
42. Ganti isi kotak search dengan `Agus`, tekan Enter
43. Verifikasi baris `expired-avatar.jpg` tampil
44. Ganti isi kotak search dengan `29 days`, tekan Enter (TC-GS-FILEMGR-118)
45. Verifikasi empty state `No results found` tampil untuk Auto-Purge In `29 days`
46. Klik `(←)` pada kotak Search
47. Baca teks Deleted Date pada baris `old-avatar.png`
48. Ketik Search teks Deleted Date tersebut, tekan Enter
49. Verifikasi empty state `No results found` tampil untuk Deleted Date
50. Klik `(←)` pada kotak Search
51. Tutup modal Recycle Bin lewat `✕`

### Modal Changelog

52. Klik tombol Changelog di toolbar
53. Catat jumlah entri total Changelog pada pagination sebagai baseline
54. Verifikasi header kolom Actions `(⋯)` Changelog tanpa ikon sort (TC-GS-FILEMGR-149)
55. Verifikasi Changelog tidak memiliki kolom Checkbox
56. Klik ikon Filter di modal Changelog (TC-GS-FILEMGR-139)
57. Buka dropdown `Action`
58. Ketik `perm` di kotak pencarian dropdown
59. Verifikasi opsi yang tampil hanya `Permanently Delete`
60. Kosongkan kotak pencarian dropdown
61. Tutup dropdown `Action`
62. Pilih `Delete` pada `Action` tanpa `[Apply]` (TC-GS-FILEMGR-134)
63. Klik ikon Filter untuk menutup panel
64. Klik ikon Filter untuk membuka kembali panel
65. Verifikasi field `Action` kosong
66. Verifikasi jumlah entri total Changelog pada pagination sama dengan baseline (tidak berubah oleh pilihan Action tanpa `[Apply]`)
67. Klik ikon Filter untuk menutup panel
68. Sembunyikan kolom `Modified By` lewat Column Visibility (TC-GS-FILEMGR-121)
69. Ketik Search `Agus`, tekan Enter
70. Verifikasi empty state `No results found` tampil
71. Verifikasi baris C03 (`stale-avatar.png`) tidak tampil
72. Tampilkan kembali kolom `Modified By` lewat Column Visibility
73. Ganti isi kotak search dengan `Agus`, tekan Enter
74. Verifikasi baris C03 (`stale-avatar.png`) tampil
75. Ganti isi kotak search dengan `14/09/26`, tekan Enter (TC-GS-FILEMGR-118)
76. Verifikasi empty state `No results found` tampil untuk Date `14/09/26`
77. Klik `(←)` pada kotak Search
78. Tutup modal Changelog lewat `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec. Setiap TC sumber (118, 121, 134, 139, 149) menyentuh tiga surface sekaligus (tabel utama, modal Recycle Bin, modal Changelog).
- Struktur: subjudul `###` per surface (bukan per TC) supaya modal dibuka sekali dan ditutup sekali; id TC ditulis di akhir langkah pemicu sebagai `(TC-GS-FILEMGR-NNN)` untuk memetakan report per langkah. Blok TC dalam tiap surface berurutan 149, 139, 134, 121, 118 (urutan sumber 118, 121, 134, 139, 149 dengan 149 didahulukan sebagai screening header dan 118 paling akhir karena mengganti isi Search).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 53 (mencatat baseline jumlah entri Changelog; tidak ada di TC, dicatat per S-03), langkah 6, langkah 29, langkah 60 (mengosongkan ketikan pencarian dropdown sebelum memilih opsi), langkah 13, langkah 36, langkah 67 (menutup Filter Panel), langkah 22, langkah 46, langkah 50, langkah 77 (mereset Search), serta langkah 78 dan langkah menutup modal Recycle Bin (menutup modal; hook `after` menjadi cadangan). Langkah "Baca teks Deleted Date" adalah aksi baca yang menjadi dasar langkah Search sesudahnya.
- Asersi tambahan di luar Expected TC: langkah 39 dan langkah 70 (empty state `No results found` sebagai anchor positif untuk asersi absence baris `expired-avatar.jpg` dan C03, bagian 8b butir 2); kata kunci `Agus` hanya terdapat di kolom Deleted By (Tabel A3) dan Modified By (Tabel A4) sehingga hasil kosong adalah akibat kolom disembunyikan.
- Alasan spec melewati sekitar 35 langkah (ekspansi sekitar 78 langkah): lima TC sumber masing-masing menguji tiga surface; blok per surface memakai dataset (Tabel A2, A3, A4) dan kontrol yang sama, hanya membaca, satu akun, satu topik (kontrol tabel lintas surface), dan tiap blok mereset Search, Filter, serta visibilitas kolom sebelum berpindah surface. Risiko: kegagalan keras saat membuka modal Recycle Bin atau Changelog menghentikan blok sesudahnya dalam spec yang sama; bila ini dinilai terlalu besar, spec dapat dipecah per surface tanpa mengubah `sourceTc`.
- Temuan untuk QA:
  - TC-GS-FILEMGR-121 butir c dan e: Expected hanya "`Agus` tidak mencocokkan baris `expired-avatar.jpg`" dan "... baris C03", tanpa menyebut empty state; spec menambah anchor `No results found` (turunan dari Tabel A3 dan A4) untuk asersi absence. Perlu konfirmasi QA bahwa tidak ada baris lain yang mengandung `Agus` selain pada kolom tersembunyi.
  - TC-GS-FILEMGR-118 butir c: nilai Deleted Date relatif terhadap waktu uji (Tabel A3); spec membaca teks dari tabel dan mencarinya; TC tidak menyebut baris yang dipakai (spec memakai `old-avatar.png`).
  - TC-GS-FILEMGR-134 dan 139: modal Recycle Bin dan Changelog kembali ke default setiap dibuka (NC-21); spec membuka tiap modal sekali.
  - Jumlah baris `16` Recycle Bin mengasumsikan tidak ada spec lain yang menghapus file (Delete menambah baris Recycle Bin); reset dataset lewat fixture BE tidak punya mekanisme tertulis di TC (lihat spec 031 dan 032).
  - TC-GS-FILEMGR-134 Expected c menyatakan "14 baris tetap tampil" untuk Changelog, padahal Changelog tidak dapat di-seed ulang atau dibersihkan dan spec lain menambah entri (S-12). Spec mengasersi makna Expected (Filter yang tidak di-Apply tidak mengubah tabel) sebagai jumlah entri total yang sama dengan baseline langkah 53; pemilik TC perlu menulis ulang Expected c sebagai hitungan relatif atau Filter Date rentang Tabel A4.
  - Selector kontrol Column Visibility, ikon Filter, dan tombol modal "disediakan tim FE"; TC tidak menyebut label aksesibilitasnya.
