---
id: TC-FA-SU-E2E-143-sub-tab-borrowed-assets-filter-dan-kontrol-filter-dan-setup-column
title: "Sub-tab Borrowed Assets: Filter dan Kontrol Filter dan Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-426
  - TC-FA-SU-427
  - TC-FA-SU-428
  - TC-FA-SU-429
coverage:
  web: automated
---

# Sub-tab Borrowed Assets: Filter dan Kontrol Filter dan Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Responsibilities (#24). Pengguna target: Budi Santoso dengan 5 baris Borrowed Assets: `Laptop - 1`, `Laptop - 2` (Transaction ID `BRW-20260610`, PIC `Ahmad D`), `Kamera DSLR` (Brand `Canon`), `Proyektor Portable` (Asset ID `AST-01011`), dan `Kendaraan Operasional` (Model / Type `Vario 125`); nilai kolom lain tiap baris mengikuti Pre-setup #24. Kelima baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-426: Perilaku Filter Panel Sub-tab Borrowed Assets: tutup tanpa Apply, indikator titik, dan nilai kosong

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
3. Klik icon Filter
4. Buka dropdown Name
5. Centang `Kamera DSLR`
6. Klik di luar panel Filter
7. Klik icon Filter
8. Verifikasi panel dibuka lagi menampilkan nilai ter-Apply terakhir: field Name kosong dengan placeholder `All assets`
9. Verifikasi tabel tidak berubah: 5 baris tetap tampil
10. Buka dropdown Name
11. Verifikasi dropdown Name tidak memiliki opsi untuk nilai kosong
12. Centang `Kamera DSLR`
13. Klik `[Apply]`
14. Verifikasi memilih opsi menyaring keluar baris yang nilainya kosong: sedikitnya satu baris tampil dan tidak ada baris dengan Name kosong
15. Klik icon Filter
16. Verifikasi icon Filter menampilkan badge titik saat panel tertutup
17. Klik icon Filter
18. Verifikasi icon Filter menampilkan badge titik saat panel terbuka
19. Klik header kolom Column Visibility (⋯)
20. Hapus centang Name pada overlay Column Visibility
21. Tutup overlay Column Visibility dengan Esc
22. Verifikasi field Name tetap ada pada panel Filter
23. Verifikasi filter ter-Apply tetap berlaku: tabel menyisakan 1 baris
24. Klik header kolom Column Visibility (⋯)
25. Centang kembali Name pada overlay Column Visibility
26. Tutup overlay Column Visibility dengan Esc
27. Klik `[Clear Field]`
28. Klik `[Apply]`
29. Verifikasi badge titik pada icon Filter hilang
30. Tutup panel Filter dengan klik icon Filter

### TC-FA-SU-427: Chip dan checkbox dropdown Filter Sub-tab Borrowed Assets sinkron dua arah, logika OR dalam field

31. Klik icon Filter
32. Buka dropdown Name
33. Centang `Kamera DSLR`
34. Centang `Laptop - 1`
35. Klik `[Apply]`
36. Verifikasi dua chip `Kamera DSLR` dan `Laptop - 1` tampil di dalam field Name
37. Verifikasi hasil adalah gabungan (OR) kedua opsi: `Laptop - 1` dan `Kamera DSLR`
38. Klik ✕ pada chip `Kamera DSLR` tanpa membuka dropdown
39. Verifikasi chip `Kamera DSLR` hilang
40. Verifikasi checkbox opsi `Kamera DSLR` ter-uncheck
41. Verifikasi chip `Laptop - 1` tetap tampil
42. Buka dropdown Name
43. Centang `Proyektor Portable`
44. Hapus centang `Laptop - 1`
45. Verifikasi chip `Laptop - 1` hilang
46. Verifikasi chip `Proyektor Portable` tetap tampil
47. Hapus centang `Proyektor Portable`
48. Ketik `lap` di kotak cari dropdown
49. Verifikasi pencarian di dalam dropdown mempersempit opsi menjadi `Laptop - 1` dan `Laptop - 2` (substring, tidak case-sensitive)
50. Ganti isi kotak cari dropdown dengan `zzz`
51. Verifikasi keyword tanpa hasil menampilkan `No results found`
52. Tutup dropdown Name dengan Esc
53. Klik `[Clear Field]`
54. Klik `[Apply]`
55. Tutup panel Filter dengan klik icon Filter

### TC-FA-SU-428: Screening Overlay Column Visibility Sub-tab Borrowed Assets

56. Klik header kolom Actions (⋯)
57. Verifikasi overlay tampil dengan tooltip `Column Visibility` pada header
58. Verifikasi daftar kolom berurutan Photo, Name, Asset ID, Transaction ID, Brand, Model / Type, Due Return Date, PIC
59. Verifikasi tiap kolom memiliki checkbox ☑ Hideable terpilih dan enabled
60. Verifikasi tiap kolom memiliki drag handle
61. Verifikasi item `Setup Column...` di bagian bawah overlay
62. Tutup overlay Column Visibility dengan Esc

### TC-FA-SU-429: Screening Popup Setup Column dan Preview Table Sub-tab Borrowed Assets

63. Klik header kolom Actions (⋯)
64. Klik `Setup Column...`
65. Verifikasi Title popup `Setup Column`
66. Verifikasi deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
67. Verifikasi icon close ✕ pada header popup
68. Verifikasi body memuat daftar kolom Photo, Name, Asset ID, Transaction ID, Brand, Model / Type, Due Return Date, PIC
69. Verifikasi tiap kolom memiliki checkbox
70. Verifikasi tiap kolom memiliki drag handle
71. Verifikasi tiap kolom memiliki icon Pin
72. Verifikasi Live Preview tabel tampil
73. Verifikasi footer `[Reset to Default]` dan `[Save]` rata kanan
74. Verifikasi footer tanpa `[Cancel]`
75. Tutup popup Setup Column dengan ✕

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Langkah penghubung (S-03, R-16): sebelum Detail pengguna dibuka, kotak Search User List diisi nama persis `Budi Santoso` (nama Pre-setup) karena User List memuat 25 pengguna pada 3 halaman dan posisi baris tidak diandalkan (R-23, 8b.13); langkah itu hanya menyaring baris target dan tidak diverifikasi.
- Asersi tambahan (S-03): TC-FA-SU-427: opsi `Proyektor Portable` dicentang sebelum `Laptop - 1` di-uncheck (langkah penghubung tambahan) supaya klausa c "chip lain tetap" dapat diasersi; keyword `lap` dan `zzz` pada kotak cari dropdown dipilih penulis karena Data Uji TC kosong.
- Alasan melewati sekitar 35 langkah (75 langkah tertulis, 75 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-426 butir c: Pre-setup #24 tidak memuat baris dengan Name kosong, sehingga "menyaring keluar baris yang nilainya kosong" diasersi sebagai tidak ada baris dengan Name kosong pada hasil.
  - TC-FA-SU-427: Data Uji kosong; butir c "chip lain tetap" tidak teramati bila hanya satu chip tersisa (lihat catatan S-03 di atas).
