---
id: TC-GS-IMPORT-E2E-129-create-missing-options-per-baris-dan-bulk-dedup-ejaan-pertama-sebagian
title: "Create Missing Options: per-baris dan bulk (dedup, ejaan pertama), sebagian atau seluruh gagal, dan tombol Disabled dengan spinner"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-909
  - TC-GS-IMPORT-910
  - TC-GS-IMPORT-911
  - TC-GS-IMPORT-912
  - TC-GS-IMPORT-913
  - TC-GS-IMPORT-926
coverage:
  web: automated
---

# Create Missing Options: per-baris dan bulk (dedup, ejaan pertama), sebagian atau seluruh gagal, dan tombol Disabled dengan spinner

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Spec ini tidak memakai akun lain.
- Layar awal: hook `beforeEach` suite membuka Import > User Login (Client C). TC-GS-IMPORT-910 membuka Import > User Non Login lewat langkah.
- Data Pre-setup Client C (tidak diubah): Custom Field Shift (Dropdown) Active dengan opsi `Pagi`, `Siang`, `Malam`; User Login aktif `budi.manager.c@example.com` (Represented By untuk User Non Login). Client C tanpa draft Tab User Login dan Tab User Non Login pada awal spec (Kontrak Fixture R1). Opsi `Lembur` dan `Piket` belum ada.
- Data Dinamis (fixture baru `Fixture.import.berkas`, disediakan tim QA): `user-login-shift-lembur.csv` (D-79: Shift `Lembur`, `lembur `, `Siang`), `user-non-login-shift-lembur.csv` (D-80: 2 baris Shift `Lembur`), `user-login-shift-bulk.csv` (D-81: Shift `Lembur`, `lembur `, `Piket`, `Siang`), `user-login-shift-3names.csv` (D-82: `Lembur`, `Piket`, huruf `A` diulang 121 kali), `user-login-shift-longname.csv` (D-83: huruf `A` dan `B` masing-masing diulang 121 kali).
- Opsi `Lembur` dan `Piket` literal tanpa suffix karena isi berkas CSV menentukan hasil "Invalid option" (pengecualian S-12 nama literal). Hook `before` menghapus sisa opsi itu dari Custom Field Shift Client C lewat API; langkah penghubung menghapusnya di antara TC; hook `after` mengembalikan Value Setting Shift ke `Pagi, Siang, Malam` (Kontrak Fixture R2), melepas intercept bila masih aktif, dan melakukan Discard Draft Client C.
- Intercept (Spectra.intercept) untuk TC-GS-IMPORT-926: menunda respons permintaan Create Missing 3 detik dan menghitung permintaan yang terkirim. Endpoint permintaan Create Missing tidak disebut TC; pencocokan permintaan memakai kemampuan yang disediakan tim FE (lihat Temuan untuk QA). Intercept dilepas segera setelah respons diterima (langkah 80).
- Layanan AI mock mode normal (D-40, tabel D-41 dan D-42): disetel di hook `before`, dikembalikan di hook `after`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis disediakan tim FE/BE: reset draft Client C (R1) dan pulihkan opsi Custom Field Shift (R2).
- State global: Custom Field Shift Client C; suite berjalan serial (`parallel: false`).
- Env var: `GS_CLIENTC_TC_PASSWORD`.

## Test Steps

### TC-GS-IMPORT-909: Create Missing Options per-baris menambah opsi di akhir daftar

1. Klik [Upload File] di Dropzone dan pilih berkas `user-login-shift-lembur.csv`
2. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
3. Verifikasi baris #1 dan #2 berstatus `error` dan baris #3 berstatus `pending`
4. Verifikasi sel Shift baris #1 berpesan "Lembur is not a valid option for shift"
5. Verifikasi Error Summary Callout memuat "Shift: Invalid option" dengan badge "2 rows"
6. Verifikasi Staging Metric Cards: Total Rows 3, Ready to Import 1, Errors 2
7. Klik `⋯` pada baris #1
8. Verifikasi menu `⋯` baris #1 memuat `Duplicate`, `Edit`, `[Create Missing Options]`, dan `Remove` dalam urutan tersebut
9. Pilih `[Create Missing Options]`
10. Verifikasi tidak ada dialog konfirmasi
11. Verifikasi toast sukses "Success, option has been created."
12. Muat ulang halaman Import > User Login
13. Verifikasi ketiga baris berstatus `pending`
14. Verifikasi Staging Metric Cards: Total Rows 3, Ready to Import 3, Errors 0
15. Verifikasi Error Summary Callout tidak tampil
16. Buka Global Settings > User > Custom Field
17. Verifikasi Value Setting Shift memuat `Pagi`, `Siang`, `Malam`, `Lembur` dengan `Lembur` di akhir daftar dan urutan opsi lain tidak berubah

### TC-GS-IMPORT-910: Create Missing Options per-baris pada Tab User Non Login

18. Hapus opsi `Lembur` dari Custom Field Shift Client C lewat API, reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Non Login
19. Klik [Upload File] di Dropzone dan pilih berkas `user-non-login-shift-lembur.csv`
20. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
21. Verifikasi kedua baris berstatus `error`
22. Verifikasi Error Summary Callout memuat "Shift: Invalid option" dengan badge "2 rows"
23. Klik `⋯` pada baris #1 lalu pilih `[Create Missing Options]`
24. Verifikasi tidak ada dialog konfirmasi
25. Verifikasi toast sukses "Success, option has been created."
26. Muat ulang halaman Import > User Non Login
27. Verifikasi kedua baris berstatus `pending`
28. Verifikasi Staging Metric Cards: Total Rows 2, Ready to Import 2, Errors 0
29. Buka Global Settings > User > Custom Field
30. Verifikasi Value Setting Shift memuat `Pagi`, `Siang`, `Malam`, `Lembur` dengan `Lembur` di akhir daftar

### TC-GS-IMPORT-911: Bulk Create Missing Options melakukan dedup nama dan mempertahankan ejaan pertama

31. Hapus opsi `Lembur` dari Custom Field Shift Client C lewat API, reset draft Tab User Non Login Client C ke tanpa draft, lalu buka Import > User Login
32. Klik [Upload File] di Dropzone dan pilih berkas `user-login-shift-bulk.csv`
33. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
34. Verifikasi baris #1, #2, dan #3 berstatus `error` dan baris #4 berstatus `pending`
35. Verifikasi Error Summary Callout memuat "Shift: Invalid option" dengan badge "3 rows"
36. Verifikasi Staging Metric Cards: Total Rows 4, Ready to Import 1, Errors 3
37. Klik `[Create Missing Options]` pada baris pesan "Shift: Invalid option" di Error Summary Callout
38. Verifikasi toast sukses "Success, option has been created."
39. Muat ulang halaman Import > User Login
40. Verifikasi keempat baris berstatus `pending`
41. Verifikasi Staging Metric Cards: Total Rows 4, Ready to Import 4, Errors 0
42. Buka Global Settings > User > Custom Field
43. Verifikasi Value Setting Shift memuat `Pagi`, `Siang`, `Malam`, `Lembur`, `Piket` menurut urutan itu
44. Verifikasi `Lembur` memakai ejaan baris #1 (bukan `lembur`)
45. Verifikasi `Siang` tidak ditambahkan ulang

### TC-GS-IMPORT-912: Bulk Create Missing Options dengan satu nama melebihi 120 karakter

46. Hapus opsi `Lembur` dan `Piket` dari Custom Field Shift Client C lewat API, reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
47. Klik [Upload File] di Dropzone dan pilih berkas `user-login-shift-3names.csv`
48. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
49. Klik `[Create Missing Options]` pada baris pesan "Shift: Invalid option" di Error Summary Callout
50. Verifikasi toast sukses sebagian "Success, option has been created. Some items were skipped."
51. Muat ulang halaman Import > User Login
52. Verifikasi baris #1 dan #2 berstatus `pending`
53. Verifikasi baris #3 tetap berstatus `error` dengan pesan "Shift: Max. 120 characters"
54. Verifikasi Error Summary Callout memuat "Shift: Max. 120 characters" dengan badge "1 row"
55. Verifikasi Error Summary Callout memuat `[View Data]` dan `[Delete All Rows]` tanpa `[Create Missing Options]`
56. Klik `⋯` pada baris #3
57. Verifikasi menu `⋯` baris #3 memuat `[Create Missing Options]` untuk percobaan ulang
58. Buka Global Settings > User > Custom Field
59. Verifikasi Value Setting Shift memuat `Pagi`, `Siang`, `Malam`, `Lembur`, `Piket`
60. Verifikasi nama 121 karakter tidak ditambahkan ke Value Setting Shift

### TC-GS-IMPORT-913: Seluruh nama Create Missing Options gagal

61. Hapus opsi `Lembur` dan `Piket` dari Custom Field Shift Client C lewat API, reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
62. Klik [Upload File] di Dropzone dan pilih berkas `user-login-shift-longname.csv`
63. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
64. Klik `[Create Missing Options]` pada baris pesan "Shift: Invalid option" di Error Summary Callout
65. Verifikasi toast error "Error, failed to create option."
66. Verifikasi baris #1 dan #2 tetap `error` dengan pesan "Shift: Max. 120 characters"
67. Verifikasi Error Summary Callout memuat "Shift: Max. 120 characters" dengan badge "2 rows"
68. Verifikasi Error Summary Callout tidak lagi memuat "Shift: Invalid option"
69. Buka Global Settings > User > Custom Field
70. Verifikasi Value Setting Shift tetap `Pagi, Siang, Malam`

### TC-GS-IMPORT-926: Tombol Create Missing Options Disabled dengan spinner selama request berjalan

71. Reset draft Tab User Login Client C ke tanpa draft, lalu buka Import > User Login
72. Klik [Upload File] di Dropzone dan pilih berkas `user-login-shift-lembur.csv`
73. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
74. Atur intercept jaringan agar respons permintaan Create Missing ditunda 3 detik dan hitung jumlah permintaan yang terkirim
75. Klik `[Create Missing Options]` pada baris pesan "Shift: Invalid option" di Error Summary Callout
76. Verifikasi tombol `[Create Missing Options]` tampil Disabled dengan spinner
77. Klik lagi tombol yang sama saat permintaan berjalan
78. Verifikasi jumlah permintaan Create Missing yang terkirim pada intercept jaringan tetap 1
79. Tunggu respons diterima
80. Lepas intercept jaringan
81. Buka Global Settings > User > Custom Field
82. Verifikasi Value Setting Shift memuat `Pagi`, `Siang`, `Malam`, `Lembur`
83. Verifikasi `Lembur` muncul tepat satu kali di Value Setting Shift

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md` (TC-GS-IMPORT-909, 910, 911, 912, 913, 926).
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber (909, 910, 911, 912, 913, 926) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 18, 31, 46, 61, dan 71 (hapus opsi buatan TC sebelumnya dan reset draft sebagai precondition TC berikutnya, Kontrak Fixture R1 dan R2); langkah 16, 29, 42, 58, 69, dan 81 berpindah ke Custom Field untuk verifikasi; langkah 80 melepas intercept segera setelah pemicu selesai (S-09).
- Intercept pada TC-GS-IMPORT-926 hanya menahan respons untuk mengamati state UI (Disabled dengan spinner) dan menghitung permintaan; bukan kelas b (tidak ada kegagalan dipaksa), sehingga tetap di spec fungsional. Pada langkah 76 state sementara diasersi segera setelah pemicu dan sebelum langkah yang mengubahnya.
- Spec berisi 83 langkah, di atas sekitar 35 langkah. Alasan: enam blok TC berpola sama (unggah, Confirm Mapping, Create Missing Options, verifikasi draft dan Value Setting Shift), tiap blok berdiri sendiri dengan draft dan opsi yang di-reset di langkah pembuka, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: Create Missing Options saat admin lain mengubah data ada di spec 130; konflik kunci sesi untuk Options (TC-GS-IMPORT-919) di spec 126; log pencatatan Options (TC-GS-IMPORT-922) di spec 128; visibilitas tombol di spec 122; role di spec 131 dan 132.
- Temuan untuk QA:
  - TC-GS-IMPORT-909 Expected a menulis pesan sel "Lembur is not a valid option for shift" (field `shift` huruf kecil) sedangkan kolom lain memakai "Shift"; spec menyalin teks persis dari TC.
  - TC-GS-IMPORT-912 Expected b dan c tidak memuat penanda "Setelah langkah N"; spec menaruhnya sesudah muat ulang (langkah 51) karena berstatus baris dan Callout pasca refresh.
  - TC-GS-IMPORT-926 menulis "permintaan Create Missing" tanpa menyebut endpoint; spec tidak mengarang endpoint dan menyatakan pencocokan permintaan sebagai kemampuan intercept yang disediakan tim FE.
  - TC-GS-IMPORT-926 Langkah 6 mengklik tombol yang Disabled; yang diasersi hanya jumlah permintaan yang terkirim tetap 1.
  - Post Condition "Draft ... berisi N baris" pada TC-GS-IMPORT-909, 911, 912, dan 913 diamati lewat Staging Table dan Metric Cards, bukan lewat pembacaan data BE.
