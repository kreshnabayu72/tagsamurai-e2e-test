---
id: TC-GS-IMPORT-E2E-014-dropdown-file-column-header-duplikat-tidak-di-auto-match-kolom-terpakai
title: "Dropdown File Column: Header Duplikat Tidak Di-Auto-Match, Kolom Terpakai Disabled dan Kembali Enabled, Nilai Contoh, Ellipsis, dan Aksesibilitas"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-55
  - TC-GS-IMPORT-58
  - TC-GS-IMPORT-886
  - TC-GS-IMPORT-887
  - TC-GS-IMPORT-888
coverage:
  web: automated
---

# Dropdown File Column: Header Duplikat Tidak Di-Auto-Match, Kolom Terpakai Disabled dan Kembali Enabled, Nilai Contoh, Ellipsis, dan Aksesibilitas

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import untuk Total Control Client C; langkah pertama memilih Sub-Tab Measurement.
- Data: Client C tanpa draft Tab Measurement (Kontrak Fixture R1; skrip reset disediakan tim FE/BE). Spec tidak menjalankan Confirm Mapping sehingga tidak ada draft yang tercipta. Berkas fixture (D-07, isi literal, satu nama berkas satu isi):
  - `measurement-dup-header.csv` untuk TC-GS-IMPORT-55: header `Unit Name,Unit Name,Symbol`; 3 baris data: Meter/Metre/m, Liter/Litre/L, Gram/Gramme/g.
  - `measurement-dup-header-symbol.csv` untuk TC-GS-IMPORT-887: header `Unit Name,Symbol,Symbol`; 3 baris data: Meter/m/mtr, Liter/L/ltr, Gram/g/gr (nama berkas dibedakan karena TC sumber memakai nama `measurement-dup-header.csv` untuk dua isi berbeda; lihat Temuan untuk QA).
  - `measurement-extra-col.csv` untuk TC-GS-IMPORT-58 dan 886: header `Unit Name,Symbol,Catatan`; 3 baris data: Meter/m/a, Liter/L/b, Gram/g/c.
  - `measurement-sample-edge.csv` untuk TC-GS-IMPORT-888: header `Unit Name,Symbol,Catatan`; baris data #1 kosong seluruhnya (`,,`); #2 Meter, Symbol kosong, Catatan `Catatan pengujian yang sangat panjang untuk memastikan nilai contoh pada opsi dropdown File Column dipotong dengan ellipsis di ujung baris`; #3 Liter/L/b.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; pembacaan gaya terhitung (font-size, color, opacity) dan nama aksesibel (pohon aksesibilitas) opsi dropdown; skrip reset draft.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-IMPORT-55: Header berkas yang muncul lebih dari sekali tidak di-auto-match

1. Klik Sub-Tab Measurement
2. Klik `[Upload File]`
3. Pilih berkas `measurement-dup-header.csv` di file picker
4. Perhatikan dropdown Unit Name, dropdown Symbol, dan Modal Column Mapping
5. Verifikasi dropdown Unit Name tetap "No Column" (tidak di-auto-match)
6. Verifikasi dropdown Symbol terisi otomatis `Symbol`
7. Verifikasi Error Banner pra-konfirmasi berheader "The following columns contain errors and cannot be imported:" dengan daftar `Unit Name`
8. Klik `[Cancel]` (tutup bersih)

### TC-GS-IMPORT-887: Header yang muncul dua kali tidak di-auto-match dan kedua opsi dibedakan oleh nilai contohnya

9. Klik `[Upload File]`
10. Pilih berkas `measurement-dup-header-symbol.csv` di file picker
11. Perhatikan Modal Column Mapping
12. Verifikasi dropdown Unit Name ter-auto-match ke kolom berkas `Unit Name`
13. Verifikasi dropdown Symbol tetap "No Column" (header yang muncul lebih dari sekali tidak di-auto-match)
14. Verifikasi tidak ada Error Banner karena Symbol atribut opsional
15. Klik dropdown File Column untuk Symbol
16. Perhatikan opsi bernama `Symbol` pada dropdown
17. Verifikasi dropdown memuat dua opsi bernama `Symbol`: opsi pertama dengan teks sekunder `m` dan opsi kedua dengan teks sekunder `mtr`
18. Verifikasi kedua opsi `Symbol` Enabled
19. Pilih opsi `Symbol` yang menampilkan nilai contoh `mtr`
20. Perhatikan dropdown File Column untuk Symbol
21. Verifikasi dropdown Symbol menampilkan `Symbol` dengan teks sekunder `mtr`
22. Klik `[Cancel]`, lalu klik `[Leave]` pada dialog Unsaved Changes (mapping sudah diubah)

### TC-GS-IMPORT-58: Dropdown File Column menonaktifkan kolom terpakai dan menampilkan nilai contoh

23. Klik `[Upload File]`
24. Pilih berkas `measurement-extra-col.csv` di file picker
25. Klik dropdown File Column untuk Symbol
26. Verifikasi kolom berkas `Unit Name` yang sudah dipakai atribut Unit Name tampil Disabled di dropdown Symbol
27. Verifikasi kolom berkas `Catatan` yang belum dipakai atribut mana pun tampil Enabled (bukan Disabled)
28. Perhatikan opsi `Unit Name`, `Symbol`, dan `Catatan` pada dropdown
29. Verifikasi opsi `Unit Name` menampilkan header sebagai teks utama diikuti `Meter` sebagai teks sekunder pada baris yang sama
30. Verifikasi opsi `Symbol` menampilkan header sebagai teks utama diikuti `m` sebagai teks sekunder pada baris yang sama
31. Verifikasi opsi `Catatan` menampilkan header sebagai teks utama diikuti `a` sebagai teks sekunder pada baris yang sama
32. Verifikasi teks sekunder tidak diawali, diapit, atau dipisah tanda baca (tanpa tanda kurung, tanda hubung, titik dua, maupun koma): teks opsi hanya header, spasi, lalu nilai contoh
33. Verifikasi pada tiap opsi teks sekunder memiliki ukuran huruf (computed font-size) lebih kecil daripada teks utama
34. Verifikasi pada tiap opsi teks sekunder memiliki warna (computed color) lebih muda daripada teks utama
35. Verifikasi opsi `Unit Name` yang Disabled tetap menampilkan `Meter` sebagai teks sekunder
36. Verifikasi teks utama dan teks sekunder opsi `Unit Name` yang Disabled tampil lebih pudar (opacity atau warna lebih muda) daripada teks utama dan teks sekunder opsi `Catatan` yang Enabled
37. Verifikasi nama aksesibel opsi berurutan header lalu nilai contoh: `Unit Name Meter`, `Symbol m`, `Catatan a`
38. Tutup dropdown File Column untuk Symbol
39. Klik `[Cancel]` (tutup bersih)

### TC-GS-IMPORT-888: Nilai contoh kosong tidak ditampilkan, nilai contoh panjang dipotong dengan ellipsis

40. Klik `[Upload File]`
41. Pilih berkas `measurement-sample-edge.csv` di file picker
42. Perhatikan dropdown File Column untuk Symbol dalam keadaan tertutup
43. Verifikasi dropdown Symbol ter-auto-match ke kolom berkas `Symbol`
44. Verifikasi dropdown Symbol menampilkan `Symbol` tanpa teks sekunder (sel kosong pada baris data pertama yang tidak kosong seluruhnya)
45. Klik dropdown File Column untuk Symbol
46. Perhatikan opsi `Unit Name`, `Symbol`, `Catatan`, dan "No Column" pada dropdown
47. Verifikasi opsi `Unit Name` menampilkan teks sekunder `Meter` (baris kosong #1 diabaikan)
48. Verifikasi opsi `Symbol` hanya menampilkan header `Symbol` tanpa teks sekunder dan tanpa tanda pengganti seperti `-`
49. Verifikasi opsi `Catatan` menampilkan `Catatan` utuh diikuti teks sekunder pada baris yang sama
50. Verifikasi teks sekunder opsi `Catatan` terpotong dengan ellipsis di ujung baris (satu baris tanpa membungkus; lebar isi melebihi lebar opsi)
51. Verifikasi teks `Catatan` pada opsi tidak terpotong
52. Verifikasi opsi "No Column" hanya menampilkan "No Column" tanpa teks sekunder
53. Tutup dropdown File Column untuk Symbol
54. Klik `[Cancel]` (tutup bersih)

### TC-GS-IMPORT-886: Kolom berkas kembali tersedia saat dropdown pemakainya diubah, dan "No Column" tidak dihitung terpakai

55. Klik `[Upload File]`
56. Pilih berkas `measurement-extra-col.csv` di file picker
57. Klik dropdown File Column untuk Symbol
58. Verifikasi kolom berkas `Unit Name` yang sudah dipakai atribut Unit Name tampil Disabled di dropdown Symbol
59. Tutup dropdown File Column untuk Symbol
60. Ubah dropdown File Column untuk Unit Name menjadi "No Column"
61. Klik dropdown File Column untuk Symbol
62. Verifikasi kolom berkas `Unit Name` tampil Enabled di dropdown Symbol (kembali tersedia begitu dropdown pemakainya diubah ke "No Column")
63. Pilih kolom berkas `Unit Name` pada dropdown File Column untuk Symbol
64. Verifikasi dropdown Symbol tertutup menampilkan `Unit Name` terpilih dengan teks utama `Unit Name` diikuti teks sekunder `Meter`, sama dengan opsinya dan tanpa tanda baca pemisah
65. Klik dropdown File Column untuk Unit Name
66. Verifikasi kolom berkas `Unit Name` yang sudah dipakai atribut Symbol tampil Disabled di dropdown Unit Name
67. Verifikasi kolom berkas `Symbol` yang sudah dilepas atribut Symbol tampil Enabled
68. Tutup dropdown File Column untuk Unit Name
69. Ubah dropdown File Column untuk Symbol menjadi "No Column"
70. Klik dropdown File Column untuk Unit Name
71. Verifikasi opsi "No Column" tampil Enabled di dropdown Unit Name
72. Tutup dropdown File Column untuk Unit Name
73. Klik dropdown File Column untuk Symbol
74. Verifikasi opsi "No Column" tampil Enabled di dropdown Symbol (dipilih oleh dua atribut sekaligus tanpa kesalahan)
75. Perhatikan Modal Column Mapping
76. Verifikasi Error Banner "The following columns contain errors and cannot be imported:" memuat `Unit Name` (atribut Required)
77. Verifikasi Error Banner tidak memuat `Symbol` (atribut opsional)
78. Verifikasi `[Confirm Mapping]` tetap Enabled
79. Klik `[Cancel]`, lalu klik `[Leave]` pada dialog Unsaved Changes (mapping sudah diubah)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 55, 887, 58, 888, 886. TC-GS-IMPORT-886 (mengubah mapping dan menutup lewat `[Cancel]` + `[Leave]`) terakhir; TC-GS-IMPORT-887 yang juga mengubah mapping memakai penutupan yang sama tanpa membuat draft. Tidak ada Confirm Mapping, sehingga tidak ada data tercipta.
- Alasan di atas sekitar 35 langkah (79 langkah): satu kelas harness (Dropdown File Column pada Modal Column Mapping, tanpa aksi yang mengubah data); tiap blok memakai berkas sendiri dan modal baru sehingga berdiri sendiri. Kegagalan satu blok tidak menghilangkan makna blok lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (pindah Sub-Tab), 8, 22, 39, 54, 79 (menutup modal), langkah 38, 53, 59, 68, 72 (menutup dropdown), langkah mengamati sesuai Langkah Uji TC (4, 11, 16, 20, 28, 42, 46, 75). Penutupan `[Cancel]` + `[Leave]` pada langkah 22 dan 79 mengikuti pola TC-GS-IMPORT-889 untuk modal dengan mapping yang sudah diubah.
- Pembagian TC: TC-GS-IMPORT-887 mengulang sebagian klausa a TC-GS-IMPORT-55 (header kembar tidak di-auto-match) dengan atribut berbeda (Symbol opsional vs Unit Name Required); keduanya ada di spec ini.
- Temuan untuk QA:
  - TC-GS-IMPORT-55 dan TC-GS-IMPORT-887 memakai nama berkas `measurement-dup-header.csv` dengan isi header berbeda (`Unit Name,Unit Name,Symbol` vs `Unit Name,Symbol,Symbol`) padahal Data Dinamis D-07 menyatakan satu nama berkas satu isi; spec memakai nama `measurement-dup-header-symbol.csv` untuk TC-GS-IMPORT-887.
  - Klausa a TC-GS-IMPORT-887 mengulang klausa a TC-GS-IMPORT-55 (tumpang tindih cakupan; beda atribut).
  - TC-GS-IMPORT-58 dan 888 mengasersi gaya terhitung (font-size, color, opacity) tanpa nilai ambang; spec mengasersi relasi "lebih kecil", "lebih muda", dan "lebih pudar" sesuai Expected.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
