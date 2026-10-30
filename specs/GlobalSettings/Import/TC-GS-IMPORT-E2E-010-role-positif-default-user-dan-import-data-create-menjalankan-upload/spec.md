---
id: TC-GS-IMPORT-E2E-010-role-positif-default-user-dan-import-data-create-menjalankan-upload
title: "Role Positif: Default User dan Import data (Create) Menjalankan Upload, Confirm Mapping, Import, Save, Remove, Bulk Delete, AI Accept dan Dismiss, Discard, dan Create Missing Tanpa Penolakan Izin"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-33
  - TC-GS-IMPORT-598
  - TC-GS-IMPORT-599
  - TC-GS-IMPORT-600
coverage:
  web: automated
---

# Role Positif: Default User dan Import data (Create) Menjalankan Upload, Confirm Mapping, Import, Save, Remove, Bulk Delete, AI Accept dan Dismiss, Discard, dan Create Missing Tanpa Penolakan Izin

## Prerequisites

- Mode: FE+BE (backend nyata). Commit Import nyata di Client E (tunggu selesai, kemungkinan sampai 2 menit).
- Suite serial (`parallel: false`) karena spec menjalankan commit di Client E, memakai mock layanan AI dan hook umur draft; lihat `suite.md`.
- Akun aktor (urutan blok; ganti akun/client ditulis eksplisit):
  - Default User Client E (Nanda Prakoso) `defaultUser_automated_qaTeam5@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-33. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTE_DU_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`).
  - Import data (Create) Client E (Lutfi Hakim) `importCreate_automated_qaTeam5@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-598 dan 599: `Spectra.env.GS_CLIENTE_IMPORTCREATE_PASSWORD` (env baru).
  - Import data (Create) Client C (Kiki Amalia) `importCreate_automated_qaTeam3@qwertysystem.net` (Pre-setup; tanpa capability Division/Position) untuk TC-GS-IMPORT-600: `Spectra.env.GS_CLIENTC_IMPORTCREATE_PASSWORD` (env baru).
  - Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk akun aktor; TC-GS-IMPORT-600 membuka menu Import karena TC menyebutnya.
- Data Dinamis:
  - TC-GS-IMPORT-33: Client E tanpa draft Tab Brand (Kontrak Fixture R1); `brand-12.csv` (12 baris, isi D-01: Acme Corp, Lenovo, Zebra Technologies, Honeywell, Dell, HP Inc, Canon, Epson, Brother, Logitech, Cisco, Asus).
  - TC-GS-IMPORT-598: Client E tanpa draft Tab Brand; `brand-6.csv` (header `Brand Name`; Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp).
  - TC-GS-IMPORT-599: D-17 draft Brand 14 baris pada Client E (12 `pending` seperti `brand-12.csv`; baris #13 dan #14 `error` dengan Brand Name 121 dan 125 karakter dan badge saran AI `Samsung Electronics Indonesia` dan `Lenovo Technology Indonesia`); D-40 mode mock AI normal (tabel D-41 dan D-42); D-76 varian 1 (`created_at` dimundurkan 25 jam, seed backdate) sehingga Unsaved Banner tampil.
  - TC-GS-IMPORT-600: D-14 draft User Login 4 baris pada Client C (`user-login-cm.csv`: #1 Ahmad Fauzi / Engineering / Senior Developer; #2 Citra Lestari / Marketing; #3 Dedi Prakoso, Division `Logistik` tidak ditemukan; #4 Eka Putri, Position `Store Supervisor` tidak ditemukan; Access `Global Settings`).
- Reset dan cleanup: hook `beforeEach` mereset Client E ke tanpa draft; setelah tiap blok commit, Client E dipulihkan ke kondisi Pre-setup (hapus Brand hasil commit `Acme Corp`, `Lenovo`, `Zebra Technologies`, `Honeywell`, `Dell`, `HP Inc`, `Canon`, `Epson`, `Brother`, `Logitech`, `Cisco`, `Asus`, `Nikon`, `Ricoh`, `Xerox`, `Sony`, `Panasonic`, `Sharp`) lewat API (Kontrak Fixture R2); Division `Logistik` yang dibuat TC-GS-IMPORT-600 dihapus kembali dan draft Client C dibuang di hook `after`; mode mock AI dikembalikan ke normal. Cleanup tidak berasumsi seeding berhasil penuh.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk ketiga akun, lihat `suite.md`.
- Kemampuan teknis: hook umur draft D-76; mock AI D-40; skrip seed/reset draft dan pemulihan master data (disediakan tim FE/BE); file picker; muat ulang halaman; ganti akun dan client.
- State global: mode mock layanan AI dan umur draft (dipulihkan hook).

## Test Steps

### TC-GS-IMPORT-33: Default User menjalankan Upload, Confirm Mapping, dan Import tanpa penolakan izin

1. Klik `[Upload File]`
2. Pilih berkas `brand-12.csv` di file picker
3. Verifikasi Modal Column Mapping terbuka
4. Verifikasi tidak ada toast penolakan izin
5. Klik `[Confirm Mapping]`
6. Verifikasi modal tertutup dengan toast sukses "Success, row has been added."
7. Perhatikan Staging Table dan Footer
8. Verifikasi Staging Metric Cards: Total Rows 12 (Active)
9. Verifikasi Staging Metric Cards: Ready to Import 12
10. Verifikasi Footer menampilkan `[Import (12)]` Enabled
11. Klik `[Import (12)]`
12. Verifikasi tidak muncul toast "You don't have permission to do this."
13. Tunggu commit selesai: muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
14. Perhatikan halaman Import pada pemuatan terakhir
15. Verifikasi halaman kembali ke state belum ada draft dengan Dropzone
16. Pulihkan Client E ke kondisi Pre-setup (hapus Brand hasil commit)

### TC-GS-IMPORT-598: Import data (Create) menjalankan Upload, Confirm Mapping, dan Import tanpa penolakan izin

17. Ganti akun: logout dari Default User Client E
18. Login sebagai Import data (Create) Client E dengan `Spectra.env.GS_CLIENTE_IMPORTCREATE_PASSWORD`
19. Buka menu Import dari sidebar (User berada di Import > Brand)
20. Klik `[Upload File]`
21. Pilih berkas `brand-6.csv` di file picker
22. Klik `[Confirm Mapping]`
23. Verifikasi modal tertutup dengan toast sukses "Success, row has been added."
24. Perhatikan Staging Table dan Footer
25. Verifikasi Staging Table memuat 6 baris `pending`
26. Verifikasi Staging Metric Cards: Total Rows 6
27. Verifikasi Staging Metric Cards: Ready to Import 6
28. Verifikasi Footer menampilkan `[Import (6)]` Enabled
29. Klik `[Import (6)]`
30. Verifikasi tidak muncul toast "You don't have permission to do this."
31. Tunggu commit selesai: muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
32. Perhatikan halaman Import pada pemuatan terakhir
33. Verifikasi halaman kembali ke state belum ada draft dengan Dropzone
34. Pulihkan Client E ke kondisi Pre-setup (hapus Brand hasil commit)

### TC-GS-IMPORT-599: Import data (Create) menjalankan Save, Remove, Bulk Delete, AI Accept, AI Dismiss, dan Discard Draft

35. Siapkan draft D-17 pada Client E (mode mock AI normal D-40, D-76 varian 1), muat ulang halaman Import > Brand
36. Klik `[⋯]` pada baris #1
37. Pilih Edit
38. Ubah Brand Name baris #1 dari `Acme Corp` menjadi `Acme Corporation`
39. Klik `[Save]`
40. Verifikasi muncul toast sukses "Success, row has been updated."
41. Verifikasi baris #1 berisi `Acme Corporation`
42. Klik `[⋯]` pada baris #2
43. Pilih Remove
44. Klik `[Delete]` pada dialog Delete Row
45. Verifikasi muncul toast sukses "Success, row has been deleted."
46. Verifikasi baris `Lenovo` hilang dari Staging Table
47. Centang checkbox baris #2
48. Centang checkbox baris #3
49. Klik `[Bulk Action ▾]`
50. Pilih `[Delete]`
51. Klik `[Delete]` pada dialog Delete Rows
52. Verifikasi muncul toast sukses "Success, row has been deleted."
53. Verifikasi baris `Zebra Technologies` dan `Honeywell` hilang dari Staging Table
54. Tunggu hingga toast hilang dari layar
55. Klik `[Accept]` pada badge saran AI baris error pertama (baris ke-10 Staging Table)
56. Verifikasi sel Brand Name baris error pertama berisi `Samsung Electronics Indonesia`
57. Verifikasi badge saran baris error pertama hilang
58. Verifikasi tidak ada toast
59. Klik halaman 2 pada Pagination
60. Klik `[Dismiss]` pada badge saran AI baris error kedua (baris ke-11 Staging Table)
61. Verifikasi badge saran baris error kedua hilang
62. Verifikasi baris tetap `error` dengan Brand Name 125 karakter semula
63. Verifikasi tidak ada toast
64. Klik `[Discard]` pada Unsaved Banner
65. Klik `[Discard Draft]` pada dialog Discard Draft
66. Verifikasi muncul toast sukses "Success, draft has been discarded."
67. Verifikasi halaman menampilkan Dropzone tanpa draft

### TC-GS-IMPORT-600: Import data (Create) tanpa capability Division menjalankan Create Missing Divisions

68. Ganti akun dan client: logout dari Import data (Create) Client E, login sebagai Import data (Create) Client C dengan `Spectra.env.GS_CLIENTC_IMPORTCREATE_PASSWORD`
69. Buka menu Import dari sidebar
70. Klik Sub-Tab User Login
71. Klik `[Create Missing Divisions]` pada Error Summary Callout
72. Perhatikan halaman dan toast
73. Verifikasi tidak muncul toast "You don't have permission to do this."
74. Verifikasi muncul toast sukses "Success, division has been created."
75. Muat ulang halaman Import
76. Klik Sub-Tab User Login
77. Perhatikan Staging Metric Cards dan Error Summary Callout
78. Verifikasi baris Dedi Prakoso dengan Division `Logistik` berstatus `pending`
79. Verifikasi Staging Metric Cards: Ready to Import 3
80. Verifikasi Staging Metric Cards: Errors 1
81. Verifikasi Error Summary Callout hanya memuat pesan "Position not found"
82. Hapus Division `Logistik` hasil TC dan buang draft Client C (pemulihan master data, Kontrak Fixture R2)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 33, 598, 599 (semua Client E), lalu 600 (Client C) dengan langkah ganti akun dan client eksplisit (langkah 68). TC-GS-IMPORT-600 menciptakan Division permanen sehingga ditaruh terakhir.
- Alasan di atas sekitar 35 langkah (82 langkah): satu topik (role positif menjalankan aksi tulis tanpa penolakan izin); empat blok berdiri sendiri dengan akun/client berbeda dan state direset antar blok; bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3, ganti akun eksplisit).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7, 14, 24, 32, 72, 77 (mengamati sesuai Langkah Uji TC); langkah 13 dan 31 (polling tunggu commit, batas 2 menit, sesuai Langkah Uji TC); langkah 16, 34, 35, 82 (pemulihan/seed, S-09); langkah 17 sampai 19, 68 sampai 70, 75, 76 (ganti akun dan navigasi); langkah 54 (tunggu toast hilang, 8b butir 8). Langkah 3 dan 4 adalah pecahan Expected a TC-GS-IMPORT-33 per klausa (S-01).
- Expected g TC-GS-IMPORT-599 (tidak muncul toast izin pada rangkaian aksi) dibuktikan per aksi oleh toast sukses pada langkah 40, 45, 52, dan 66 serta tidak adanya toast pada langkah 58 dan 63; tidak ada `Verifikasi` titik waktu atas seluruh rentang karena toast yang sudah hilang tidak teramati.
- Commit nyata pada Client E berjalan dengan worker normal (bukan kontrol worker D-47). Pemulihan master data Client E mengikuti Kontrak Fixture R2/R3.
- Temuan untuk QA:
  - TC-GS-IMPORT-33 dan 598 menunggu commit "setiap 5 detik hingga 2 menit"; tidak menyebut jumlah percobaan polling atau jam browser; spec mengikuti TC (jeda nyata disebut di Prerequisites).
  - TC-GS-IMPORT-599 Langkah 14 menyebut "baris ke-10 Staging Table" untuk baris error pertama dan Langkah 16 "baris ke-11"; posisi bergantung pada hasil Remove dan Bulk Delete sebelumnya (14 baris awal dikurangi 3 menjadi 11 baris; error pertama ke-10, kedua ke-11). Spec mengikuti angka TC.
  - TC-GS-IMPORT-599 Expected g menyebut rentang langkah ("Pada langkah 1 sampai 18 tidak muncul toast") yang tidak teramati oleh `Verifikasi` titik waktu; spec membuktikannya per aksi lewat toast sukses (langkah 40, 45, 52, 66) dan tanpa toast di langkah 58 dan 63.
  - Skrip seed/reset draft, hook umur draft, mock AI, dan pemulihan master data tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13). Nama data literal Population tanpa suffix `{runId}`.
