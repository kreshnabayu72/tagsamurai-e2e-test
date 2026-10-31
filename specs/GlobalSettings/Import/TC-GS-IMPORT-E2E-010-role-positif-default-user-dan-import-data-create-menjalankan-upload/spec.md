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
  - TC-GS-IMPORT-600: disiapkan oleh langkah 70; D-14 draft User Login 4 baris pada Client C (`user-login-cm.csv`: #1 Ahmad Fauzi / Engineering / Senior Developer; #2 Citra Lestari / Marketing; #3 Dedi Prakoso, Division `Logistik` tidak ditemukan; #4 Eka Putri, Position `Store Supervisor` tidak ditemukan; Access `Global Settings`).
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
12. Tunggu aksi selesai (permintaan mendapat respons)
13. Verifikasi tidak muncul toast "You don't have permission to do this."
14. Tunggu commit selesai: muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
15. Perhatikan halaman Import pada pemuatan terakhir
16. Verifikasi halaman kembali ke state belum ada draft dengan Dropzone
17. Pulihkan Client E ke kondisi Pre-setup (hapus Brand hasil commit)

### TC-GS-IMPORT-598: Import data (Create) menjalankan Upload, Confirm Mapping, dan Import tanpa penolakan izin

18. Ganti akun: logout dari Default User Client E
19. Login sebagai Import data (Create) Client E dengan `Spectra.env.GS_CLIENTE_IMPORTCREATE_PASSWORD`
20. Buka menu Import dari sidebar (User berada di Import > Brand)
21. Klik `[Upload File]`
22. Pilih berkas `brand-6.csv` di file picker
23. Klik `[Confirm Mapping]`
24. Verifikasi modal tertutup dengan toast sukses "Success, row has been added."
25. Perhatikan Staging Table dan Footer
26. Verifikasi Staging Table memuat 6 baris `pending`
27. Verifikasi Staging Metric Cards: Total Rows 6
28. Verifikasi Staging Metric Cards: Ready to Import 6
29. Verifikasi Footer menampilkan `[Import (6)]` Enabled
30. Klik `[Import (6)]`
31. Tunggu aksi selesai (permintaan mendapat respons)
32. Verifikasi tidak muncul toast "You don't have permission to do this."
33. Tunggu commit selesai: muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
34. Perhatikan halaman Import pada pemuatan terakhir
35. Verifikasi halaman kembali ke state belum ada draft dengan Dropzone
36. Pulihkan Client E ke kondisi Pre-setup (hapus Brand hasil commit)

### TC-GS-IMPORT-599: Import data (Create) menjalankan Save, Remove, Bulk Delete, AI Accept, AI Dismiss, dan Discard Draft

37. Siapkan draft D-17 pada Client E (mode mock AI normal D-40, D-76 varian 1), muat ulang halaman Import > Brand
38. Klik `[⋯]` pada baris #1
39. Pilih Edit
40. Ubah Brand Name baris #1 dari `Acme Corp` menjadi `Acme Corporation`
41. Klik `[Save]`
42. Verifikasi muncul toast sukses "Success, row has been updated."
43. Verifikasi baris #1 berisi `Acme Corporation`
44. Klik `[⋯]` pada baris #2
45. Pilih Remove
46. Klik `[Delete]` pada dialog Delete Row
47. Verifikasi muncul toast sukses "Success, row has been deleted."
48. Verifikasi baris `Lenovo` hilang dari Staging Table
49. Centang checkbox baris #2
50. Centang checkbox baris #3
51. Klik `[Bulk Action ▾]`
52. Pilih `[Delete]`
53. Klik `[Delete]` pada dialog Delete Rows
54. Verifikasi muncul toast sukses "Success, row has been deleted."
55. Verifikasi baris `Zebra Technologies` dan `Honeywell` hilang dari Staging Table
56. Tunggu hingga toast hilang dari layar
57. Klik `[Accept]` pada badge saran AI baris error pertama (baris ke-10 Staging Table)
58. Verifikasi sel Brand Name baris error pertama berisi `Samsung Electronics Indonesia`
59. Verifikasi badge saran baris error pertama hilang
60. Verifikasi tidak ada toast
61. Klik halaman 2 pada Pagination
62. Klik `[Dismiss]` pada badge saran AI baris error kedua (baris ke-11 Staging Table)
63. Verifikasi badge saran baris error kedua hilang
64. Verifikasi baris tetap `error` dengan Brand Name 125 karakter semula
65. Verifikasi tidak ada toast
66. Klik `[Discard]` pada Unsaved Banner
67. Klik `[Discard Draft]` pada dialog Discard Draft
68. Verifikasi muncul toast sukses "Success, draft has been discarded."
69. Verifikasi halaman menampilkan Dropzone tanpa draft

### TC-GS-IMPORT-600: Import data (Create) tanpa capability Division menjalankan Create Missing Divisions

70. Reset Client C ke tanpa draft; seed draft User Login D-14 (4 baris, `user-login-cm.csv`) lewat skrip fixture
71. Ganti akun dan client: logout dari Import data (Create) Client E, login sebagai Import data (Create) Client C dengan `Spectra.env.GS_CLIENTC_IMPORTCREATE_PASSWORD`
72. Buka menu Import dari sidebar
73. Klik Sub-Tab User Login
74. Klik `[Create Missing Divisions]` pada Error Summary Callout
75. Perhatikan halaman dan toast
76. Verifikasi tidak muncul toast "You don't have permission to do this."
77. Verifikasi muncul toast sukses "Success, division has been created."
78. Muat ulang halaman Import
79. Klik Sub-Tab User Login
80. Perhatikan Staging Metric Cards dan Error Summary Callout
81. Verifikasi baris Dedi Prakoso dengan Division `Logistik` berstatus `pending`
82. Verifikasi Staging Metric Cards: Ready to Import 3
83. Verifikasi Staging Metric Cards: Errors 1
84. Verifikasi Error Summary Callout hanya memuat pesan "Position not found"
85. Hapus Division `Logistik` hasil TC dan buang draft Client C (pemulihan master data, Kontrak Fixture R2)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 33, 598, 599 (semua Client E), lalu 600 (Client C) dengan langkah ganti akun dan client eksplisit (langkah 71). TC-GS-IMPORT-600 menciptakan Division permanen sehingga ditaruh terakhir.
- Alasan di atas sekitar 35 langkah (85 langkah): satu topik (role positif menjalankan aksi tulis tanpa penolakan izin); empat blok berdiri sendiri dengan akun/client berbeda dan state direset antar blok; bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3, ganti akun eksplisit).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7, 15, 25, 34, 75, 80 (mengamati sesuai Langkah Uji TC); langkah 14 dan 33 (polling tunggu commit, batas 2 menit, sesuai Langkah Uji TC); langkah 12 dan 31 (penanda "permintaan mendapat respons" sesudah klik `[Import (N)]`; penanda ini tidak ada di TC dan dicatat di Temuan untuk QA); langkah 17, 36, 37, 70, 85 (pemulihan/seed lewat skrip fixture sinkron, tanpa penanda tunggu, S-09); langkah 18 sampai 20, 71 sampai 73, 78, 79 (ganti akun dan navigasi); langkah 56 (tunggu toast hilang, 8b butir 8). Langkah 3 dan 4 adalah pecahan Expected a TC-GS-IMPORT-33 per klausa (S-01).
- Expected g TC-GS-IMPORT-599 (tidak muncul toast izin pada rangkaian aksi) dibuktikan per aksi oleh toast sukses pada langkah 42, 47, 54, dan 68 serta tidak adanya toast pada langkah 60 dan 65; tidak ada `Verifikasi` titik waktu atas seluruh rentang karena toast yang sudah hilang tidak teramati.
- Commit nyata pada Client E berjalan dengan worker normal (bukan kontrol worker D-47). Pemulihan master data Client E mengikuti Kontrak Fixture R2/R3.
- Temuan untuk QA:
  - TC-GS-IMPORT-33 dan 598 menunggu commit "setiap 5 detik hingga 2 menit"; tidak menyebut jumlah percobaan polling atau jam browser; spec mengikuti TC (jeda nyata disebut di Prerequisites).
  - TC-GS-IMPORT-599 Langkah 14 menyebut "baris ke-10 Staging Table" untuk baris error pertama dan Langkah 16 "baris ke-11"; posisi bergantung pada hasil Remove dan Bulk Delete sebelumnya (14 baris awal dikurangi 3 menjadi 11 baris; error pertama ke-10, kedua ke-11). Spec mengikuti angka TC.
  - TC-GS-IMPORT-599 Expected g menyebut rentang langkah ("Pada langkah 1 sampai 18 tidak muncul toast") yang tidak teramati oleh `Verifikasi` titik waktu; spec membuktikannya per aksi lewat toast sukses (langkah 42, 47, 54, 68) dan tanpa toast di langkah 60 dan 65.
  - Penanda "Tunggu aksi selesai (permintaan mendapat respons)" pada langkah 12 dan 31 tidak ada di TC; penanda teramati sesudah klik `[Import (N)]` belum ditetapkan TC/PRD.
  - Skrip seed/reset draft, hook umur draft, mock AI, dan pemulihan master data tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13). Nama data literal Population tanpa suffix `{runId}`.
