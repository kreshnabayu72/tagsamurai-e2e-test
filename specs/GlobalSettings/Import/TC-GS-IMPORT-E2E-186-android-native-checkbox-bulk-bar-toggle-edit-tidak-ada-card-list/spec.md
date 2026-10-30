---
id: TC-GS-IMPORT-E2E-186-android-native-checkbox-bulk-bar-toggle-edit-tidak-ada-card-list
title: "Android native: checkbox/bulk bar/toggle Edit tidak ada, card list, Download Template di bottom sheet, form satu kolom di bottom sheet, bottom sheet layar penuh, grid kartu 2 kolom, tombol callout wrap, tooltip Disabled hilang otomatis"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-555
  - TC-GS-IMPORT-556
  - TC-GS-IMPORT-557
  - TC-GS-IMPORT-558
  - TC-GS-IMPORT-559
  - TC-GS-IMPORT-560
  - TC-GS-IMPORT-561
  - TC-GS-IMPORT-562
  - TC-GS-IMPORT-811
  - TC-GS-IMPORT-836
  - TC-GS-IMPORT-935
coverage:
  mobile: automated
---

# Android native: checkbox/bulk bar/toggle Edit tidak ada, card list, Download Template di bottom sheet, form satu kolom di bottom sheet, bottom sheet layar penuh, grid kartu 2 kolom, tombol callout wrap, tooltip Disabled hilang otomatis

## Prerequisites

- Mode: FE+BE (backend nyata). Platform: aplikasi native Android (PRD §4.6); tampilan berupa card list, bottom sheet, dan grid kartu. Semua TC bertanda Manual Only di sumber (kriteria b: perangkat Android native) dan tetap spec; kebutuhan perangkat tercatat di sini.
- Suite serial (`parallel: false`): perangkat Android bersama dipakai satu spec dalam satu waktu (S-09) dan draft Import dibagikan ke seluruh admin satu client; lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; pola enroll atau prefix perangkat tidak didefinisikan di TC, PRD, atau LLD selain nama kemampuannya):
  - Perangkat atau emulator Android dengan aplikasi native TAG Samurai terpasang, serta kemampuan mengetuk elemen UI, memilih berkas dari penyimpanan perangkat (`brand-12.csv` tersedia di perangkat), dan membaca gaya tampilan (tebal, pudar, wrap, layar penuh).
  - Hook umur draft D-76 varian 1 (>=24 jam; `created_at` dimundurkan 25 jam) agar Unsaved Banner tampil pada TC-557.
  - Skrip fixture pemulihan draft dasar Client A (D-01 Brand 12 baris dan D-05 User Login 8 baris, Kontrak Fixture R2), reset Client B ke tanpa draft Tab Brand, dan seeding draft Client C (1 baris User Login dengan Division `Gudng`).
- Akun (login aktor pertama di aplikasi Android pada hook `before`; ganti akun eksplisit di tengah spec, hook `after` mengembalikan sesi ke akun default suite). Password tidak ditulis di spec atau fixture:
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), `Spectra.env.GS_TC_PASSWORD`: aktor pertama (TC-556, 560, 557, 555, 558, 811, 836, 935).
  - Import data (Read Only) Client A (Tono Hartono) `importRead_automated_qaTeam1@qwertysystem.net` (Pre-setup), `Spectra.env.GS_IMPORTRO_PASSWORD` (TC-562).
  - Total Control Client B (Bayu Santoso) `totalControl_automated_qaTeam2@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTB_TC_PASSWORD` (TC-559).
  - Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTC_TC_PASSWORD` (TC-561).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk setiap akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Data Dinamis (milik spec ini; Population Client A, nama literal karena asersi isi kartu; seeding idempotent dan dipulihkan sebelum tiap blok):
  - D-01 draft Brand 12 baris `pending` Client A (`Acme Corp`, `Lenovo`, `Zebra Technologies`, `Honeywell`, `Dell`, `HP Inc`, `Canon`, `Epson`, `Brother`, `Logitech`, `Cisco`, `Asus`).
  - D-05 draft User Login 8 baris `pending` Client A dari `user-login-8.csv`: card #1 Ahmad Fauzi `ahmad.fauzi@example.com` Division Engineering; card #2 Citra Lestari `citra.lestari@example.com` Division Marketing.
  - `brand-12.csv` (TC-559): isi seperti D-01; draft Client C TC-561: 1 baris User Login dengan Division `Gudng` yang tidak ditemukan.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan draft dasar Client A, hapus draft Client B dan Client C, batalkan sesi Duplicate atau Edit yang masih terbuka, tutup bottom sheet dan dialog, dan kembalikan sesi ke akun default suite.

## Test Steps

### Brand Client A: card list dan kartu (TC-GS-IMPORT-556, TC-GS-IMPORT-560, TC-GS-IMPORT-557)

1. Pulihkan draft dasar Client A D-01 (Brand 12 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
2. Buka halaman Import > Brand di aplikasi Android
3. Verifikasi satu card per baris berisi `#`
4. Verifikasi satu card per baris berisi Brand Name sebagai identifier utama bertulisan tebal
5. Verifikasi satu card per baris berisi badge Status
6. Verifikasi satu card per baris berisi `[⋯]` di pojok kanan atas
7. Verifikasi empat kartu tampil sebagai grid 2 kolom (2 baris x 2 kolom)
8. Verifikasi kartu Total Rows 12 Active
9. Verifikasi kartu Ready to Import 12 Enabled
10. Verifikasi kartu Errors 0 Disabled
11. Verifikasi kartu Duplicates 0 Disabled
12. Verifikasi angka `0` pada kartu Errors dan Duplicates pudar
13. Verifikasi `[Upload File]` tampil sebagai tombol utama di atas card list
14. Verifikasi tidak ada `[🔍]`
15. Verifikasi `[Discard]` tersedia lewat Unsaved Banner
16. Verifikasi `[Import (12)]` tampil full-width sebagai footer tetap
17. Verifikasi `[Changelog]` tetap berada di header halaman
18. Ketuk `[⋯]` di toolbar
19. Verifikasi `[Download Template]` ada di bottom sheet `[⋯]`
20. Tutup bottom sheet `[⋯]`

### Brand Client A: tanpa checkbox, Bulk Action Bar, toggle Edit (TC-GS-IMPORT-555)

21. Perhatikan card list dan toolbar
22. Verifikasi card list Staging Table tidak memuat checkbox
23. Verifikasi tidak ada Bulk Action Bar `[Delete]`
24. Verifikasi tidak ada toggle "Edit this page"
25. Ketuk `[⋯]` pada card #1
26. Verifikasi row action `⋯` pada card memuat Remove sebagai jalur penghapusan satu baris
27. Tutup menu row action

### Brand Client A: form satu kolom di bottom sheet (TC-GS-IMPORT-558, TC-GS-IMPORT-811)

28. Ketuk row action `[⋯]` pada card #1 lalu Edit
29. Verifikasi bottom sheet terbuka berisi form satu kolom dengan field Brand Name
30. Verifikasi footer bottom sheet `[Cancel]` dan `[Save]`
31. Ketuk `[Cancel]`
32. Ketuk row action `[⋯]` pada card #1
33. Pilih Duplicate
34. Verifikasi bottom sheet terbuka berisi form satu kolom dengan field Brand Name
35. Verifikasi footer bottom sheet `[Cancel]` dan `[Save]`
36. Ketuk `[Cancel]` (sesi Duplicate dibatalkan)

### User Login Client A: kartu baris dan kontrol penyuntingan (TC-GS-IMPORT-836, TC-GS-IMPORT-935)

37. Pulihkan draft dasar Client A D-05 (User Login 8 baris `pending`) lewat skrip fixture
38. Buka halaman Import > User Login di aplikasi Android
39. Verifikasi card #1 menampilkan `#` bernilai 1
40. Verifikasi card #1 menampilkan "Ahmad" (First Name) sebagai identifier utama bertulisan tebal
41. Verifikasi card #1 menampilkan badge Status `pending`
42. Verifikasi card #1 menampilkan tiga field kunci: Last Name "Fauzi", Email "ahmad.fauzi@example.com", Division "Engineering"
43. Verifikasi card #1 tidak menampilkan Position, Employee ID, Access, Active Period, maupun Custom Field Shift sebagai field kunci
44. Verifikasi card #2 menampilkan "Citra" sebagai identifier utama bertulisan tebal
45. Verifikasi card #2 menampilkan tiga field kunci: Last Name "Lestari", Email "citra.lestari@example.com", Division "Marketing"
46. Ketuk `[⋯]` pada card #1 lalu pilih Edit
47. Verifikasi bottom sheet menampilkan form satu kolom dengan `[Cancel]` dan `[Save]` di footer
48. Verifikasi Division, Position, dan Shift berupa Select pencarian
49. Verifikasi Access berupa MultiSelect
50. Verifikasi Active Period berupa DatePicker (kontrol sama dengan desktop)
51. Ketuk `[Cancel]`
52. Verifikasi bottom sheet tertutup tanpa dialog

### Import data (Read Only) Client A: tooltip Disabled hilang otomatis (TC-GS-IMPORT-562)

53. Ganti akun: keluar dari aplikasi Android, lalu masuk sebagai Import data (Read Only) Client A (Tono Hartono)
54. Pulihkan draft dasar Client A D-01 (Brand 12 baris `pending`) lewat skrip fixture
55. Buka halaman Import > Brand di aplikasi Android
56. Ketuk `[Upload File]`
57. Verifikasi tooltip "You don't have permission to do this." tampil
58. Tunggu tooltip hilang otomatis tanpa aksi pengguna
59. Verifikasi tooltip hilang

### Client B: Modal Column Mapping dan dialog konfirmasi bottom sheet layar penuh (TC-GS-IMPORT-559)

60. Ganti akun: keluar dari aplikasi Android, lalu masuk sebagai Total Control Client B (Bayu Santoso)
61. Reset Client B ke tanpa draft Tab Brand lewat skrip fixture
62. Buka halaman Import > Brand di aplikasi Android
63. Ketuk `[Upload File]` dan pilih berkas `brand-12.csv`
64. Verifikasi Modal Column Mapping `Column Mapping: Brand` tampil sebagai bottom sheet layar penuh
65. Verifikasi Modal Column Mapping memuat deskripsi "Map columns from your uploaded file to the system attributes."
66. Ketuk `[Confirm Mapping]`
67. Ketuk row action `[⋯]` pada card #1 lalu Remove
68. Verifikasi dialog Delete Row tampil sebagai bottom sheet layar penuh
69. Verifikasi dialog Delete Row memuat Title "Delete Row"
70. Verifikasi dialog Delete Row memuat Body `Row #1` diikuti "This row will be permanently removed from this draft. Are you sure you want to delete it? This action cannot be undone."
71. Verifikasi dialog Delete Row memuat tombol `[Cancel]` dan `[Delete]`
72. Ketuk `[Cancel]` pada dialog Delete Row

### Client C: tombol aksi baris pesan Callout wrap (TC-GS-IMPORT-561)

73. Ganti akun: keluar dari aplikasi Android, lalu masuk sebagai Total Control Client C (Rudi Hartanto)
74. Seed draft User Login 1 baris dengan Division `Gudng` yang tidak ditemukan di Client C lewat skrip fixture
75. Buka halaman Import > User Login di aplikasi Android
76. Verifikasi Error Summary Callout tampil full-width
77. Verifikasi baris pesan `Division not found` memuat `[View Data]`, `[Delete All Rows]`, dan `[Create Missing Divisions]`
78. Verifikasi tombol pada baris pesan `Division not found` wrap ke baris berikutnya di bawah teks pesan

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Platform: aplikasi native Android (PRD §4.6). Tidak ada kelas harness lain; semua TC adalah verifikasi tampilan dan interaksi mobile yang berbeda dari web. Semua TC bertanda Manual Only di sumber (kriteria b) tetapi tetap spec sesuai konvensi bagian 2 (hambatan teknis dan label Manual bukan alasan mengeluarkan TC).
- Alasan melewati sekitar 35 langkah (78 langkah nominal): enam blok homogen (verifikasi tampilan Android pada Sub-Tab dan akun yang sama), satu platform dan berdiri sendiri; urutan blok dikelompokkan per akun dengan langkah ganti akun eksplisit (langkah 53, 60, 73) sehingga bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal. Blok Client A memakai satu draft tanpa mengubah data (hanya membuka bottom sheet dan membatalkannya).
- Subjudul `###` memetakan langkah ke id TC granular. Urutan blok: screening (TC-556, 560, 557, 555) sebelum bottom sheet penyuntingan (TC-558, 811) dan blok User Login (TC-836, 935); `[Cancel]` pada bottom sheet dan menutup sheet ditulis sebagai langkah penghubung.
- Langkah penghubung (tanpa `Verifikasi`): pemulihan dan seeding (langkah 1, 37, 54, 61, 74), pembukaan halaman, mengetuk `[⋯]` di toolbar dan menutup bottom sheet (langkah 18 dan 20), menutup menu row action (langkah 27), ketuk `[Cancel]` (langkah 31, 36, 51, 72), konfirmasi mapping (langkah 66), dan ganti akun (langkah 53, 60, 73). Langkah 14 (tidak ada `[🔍]`) dan 22 sampai 24 (tidak ada checkbox, Bulk Action Bar, toggle) adalah asersi absence atas elemen UI pada halaman yang sudah termuat; kartu dan card list tampil lebih dulu (langkah 3 sampai 13) sebagai anchor permukaan.
- Urutan asersi TC-GS-IMPORT-557: asersi halaman (Expected b sampai f) dilakukan sebelum membuka bottom sheet toolbar (Expected a) karena bottom sheet menutupi halaman (butir 5 bagian 8b).
- Temuan untuk QA:
  - TC-GS-IMPORT-555 sampai 562, 811, 836, 935 tidak menyebut cara masuk ke aplikasi Android native dan pola enroll atau prefix perangkat; kebutuhan ini ditulis di Prerequisites dan disediakan tim FE/BE.
  - TC-GS-IMPORT-557 mengasersi `[Discard]` tersedia lewat Unsaved Banner (umur draft >=24 jam, D-76) tetapi hanya menyebut D-76 pada Precondition d; spec memakai hook umur draft di langkah 1.
  - TC-GS-IMPORT-557 Expected c ("Tidak ada `[🔍]`") adalah asersi absence tanpa anchor pada TC; spec menyusun anchor lewat asersi toolbar dan header lain (langkah 13, 15 sampai 17).
  - TC-GS-IMPORT-559 menyebut Body dialog Delete Row `Row #1` diikuti kalimat konfirmasi; spec menuliskan teks persis dari Expected.
  - TC-GS-IMPORT-560 menyebut angka `0` pudar tanpa nilai kontras atau opasitas; spec mengasersinya sebagai kata TC.
  - TC-GS-IMPORT-561 menyebut tombol "wrap ke baris berikutnya di bawah teks" tanpa ukuran layar acuan; spec mengikuti kata TC pada perangkat uji.
  - Post Condition TC-GS-IMPORT-811 ("sesi Duplicate dibatalkan dengan `[Cancel]`") dikerjakan langkah 36; Post Condition TC lain "-".
