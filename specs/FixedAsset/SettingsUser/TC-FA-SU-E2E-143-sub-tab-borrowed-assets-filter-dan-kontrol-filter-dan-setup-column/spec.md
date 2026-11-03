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

1. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
2. Klik icon Filter
3. Buka dropdown Name
4. Centang `Kamera DSLR`
5. Klik di luar panel Filter
6. Klik icon Filter
7. Verifikasi panel dibuka lagi menampilkan nilai ter-Apply terakhir: field Name kosong dengan placeholder `All assets`
8. Verifikasi tabel tidak berubah: 5 baris tetap tampil
9. Buka dropdown Name
10. Verifikasi dropdown Name tidak memiliki opsi untuk nilai kosong
11. Centang `Kamera DSLR`
12. Klik `[Apply]`
13. Verifikasi memilih opsi menyaring keluar baris yang nilainya kosong: sedikitnya satu baris tampil dan tidak ada baris dengan Name kosong
14. Klik icon Filter
15. Verifikasi icon Filter menampilkan badge titik saat panel tertutup
16. Klik icon Filter
17. Verifikasi icon Filter menampilkan badge titik saat panel terbuka
18. Klik header kolom Column Visibility (⋯)
19. Hapus centang Name pada overlay Column Visibility
20. Tutup overlay Column Visibility dengan Esc
21. Verifikasi field Name tetap ada pada panel Filter
22. Verifikasi filter ter-Apply tetap berlaku: tabel menyisakan 1 baris
23. Klik header kolom Column Visibility (⋯)
24. Centang kembali Name pada overlay Column Visibility
25. Tutup overlay Column Visibility dengan Esc
26. Klik `[Clear Field]`
27. Klik `[Apply]`
28. Verifikasi badge titik pada icon Filter hilang
29. Tutup panel Filter dengan klik icon Filter

### TC-FA-SU-427: Chip dan checkbox dropdown Filter Sub-tab Borrowed Assets sinkron dua arah, logika OR dalam field

30. Klik icon Filter
31. Buka dropdown Name
32. Centang `Kamera DSLR`
33. Centang `Laptop - 1`
34. Klik `[Apply]`
35. Verifikasi dua chip `Kamera DSLR` dan `Laptop - 1` tampil di dalam field Name
36. Verifikasi hasil adalah gabungan (OR) kedua opsi: `Laptop - 1` dan `Kamera DSLR`
37. Klik ✕ pada chip `Kamera DSLR` tanpa membuka dropdown
38. Verifikasi chip `Kamera DSLR` hilang
39. Verifikasi checkbox opsi `Kamera DSLR` ter-uncheck
40. Verifikasi chip `Laptop - 1` tetap tampil
41. Buka dropdown Name
42. Centang `Proyektor Portable`
43. Hapus centang `Laptop - 1`
44. Verifikasi chip `Laptop - 1` hilang
45. Verifikasi chip `Proyektor Portable` tetap tampil
46. Hapus centang `Proyektor Portable`
47. Ketik `lap` di kotak cari dropdown
48. Verifikasi pencarian di dalam dropdown mempersempit opsi menjadi `Laptop - 1` dan `Laptop - 2` (substring, tidak case-sensitive)
49. Ganti isi kotak cari dropdown dengan `zzz`
50. Verifikasi keyword tanpa hasil menampilkan `No results found`
51. Tutup dropdown Name dengan Esc
52. Klik `[Clear Field]`
53. Klik `[Apply]`
54. Tutup panel Filter dengan klik icon Filter

### TC-FA-SU-428: Screening Overlay Column Visibility Sub-tab Borrowed Assets

55. Klik header kolom Actions (⋯)
56. Verifikasi overlay tampil dengan tooltip `Column Visibility` pada header
57. Verifikasi daftar kolom berurutan Photo, Name, Asset ID, Transaction ID, Brand, Model / Type, Due Return Date, PIC
58. Verifikasi tiap kolom memiliki checkbox ☑ Hideable terpilih dan enabled
59. Verifikasi tiap kolom memiliki drag handle
60. Verifikasi item `Setup Column...` di bagian bawah overlay
61. Tutup overlay Column Visibility dengan Esc

### TC-FA-SU-429: Screening Popup Setup Column dan Preview Table Sub-tab Borrowed Assets

62. Klik header kolom Actions (⋯)
63. Klik `Setup Column...`
64. Verifikasi Title popup `Setup Column`
65. Verifikasi deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
66. Verifikasi icon close ✕ pada header popup
67. Verifikasi body memuat daftar kolom Photo, Name, Asset ID, Transaction ID, Brand, Model / Type, Due Return Date, PIC
68. Verifikasi tiap kolom memiliki checkbox
69. Verifikasi tiap kolom memiliki drag handle
70. Verifikasi tiap kolom memiliki icon Pin
71. Verifikasi Live Preview tabel tampil
72. Verifikasi footer `[Reset to Default]` dan `[Save]` rata kanan
73. Verifikasi footer tanpa `[Cancel]`
74. Tutup popup Setup Column dengan ✕

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Asersi tambahan (S-03): TC-FA-SU-427: opsi `Proyektor Portable` dicentang sebelum `Laptop - 1` di-uncheck (langkah penghubung tambahan) supaya klausa c "chip lain tetap" dapat diasersi; keyword `lap` dan `zzz` pada kotak cari dropdown dipilih penulis karena Data Uji TC kosong.
- Alasan melewati sekitar 35 langkah (74 langkah tertulis, 74 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-426 butir c: Pre-setup #24 tidak memuat baris dengan Name kosong, sehingga "menyaring keluar baris yang nilainya kosong" diasersi sebagai tidak ada baris dengan Name kosong pada hasil.
  - TC-FA-SU-427: Data Uji kosong; butir c "chip lain tetap" tidak teramati bila hanya satu chip tersisa (lihat catatan S-03 di atas).
