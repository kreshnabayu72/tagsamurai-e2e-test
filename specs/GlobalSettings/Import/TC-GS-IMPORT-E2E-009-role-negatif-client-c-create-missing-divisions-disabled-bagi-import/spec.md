---
id: TC-GS-IMPORT-E2E-009-role-negatif-client-c-create-missing-divisions-disabled-bagi-import
title: "Role Negatif Client C: Create Missing Divisions Disabled bagi Import data (Read Only) dan Izin Create Dicabut Saat Modal Column Mapping Terbuka"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-44
  - TC-GS-IMPORT-597
coverage:
  web: automated
---

# Role Negatif Client C: Create Missing Divisions Disabled bagi Import data (Read Only) dan Izin Create Dicabut Saat Modal Column Mapping Terbuka

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena TC-GS-IMPORT-44 mengubah capability akun (state global role); lihat `suite.md`.
- Akun aktor (Client C):
  - Import data (Read Only) Client C (Hari Wibowo) `importRead_automated_qaTeam3@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-597. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_IMPORTRO_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`).
  - Import data (Create) Client C (Kiki Amalia) `importCreate_automated_qaTeam3@qwertysystem.net` (Pre-setup; capability Import data C dan R, tanpa capability Division/Position) untuk TC-GS-IMPORT-44: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_CLIENTC_IMPORTCREATE_PASSWORD` (env baru). Hook `after` mengembalikan sesi ke Total Control Client A.
  - Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import untuk akun aktor. Langkah 1 menyiapkan draft D-14 sesudah reset `beforeEach` dan langkah 2 memuat ulang halaman Import > Brand supaya draft terbaca.
- Data Dinamis:
  - D-14: draft User Login 4 baris pada Client C (`user-login-cm.csv`; #1 Ahmad Fauzi / Engineering / Senior Developer; #2 Citra Lestari / Marketing; #3 Dedi Prakoso dengan Division `Logistik` tidak ditemukan; #4 Eka Putri dengan Position `Store Supervisor` tidak ditemukan; Access `Global Settings`), disiapkan oleh langkah 1 lewat skrip fixture.
  - TC-GS-IMPORT-44: Client C tanpa draft Tab Brand (Kontrak Fixture R1); berkas `brand-12.csv` (header `Brand Name`; 12 baris sesuai D-01).
- Kemampuan teknis: fixture Role & Permission untuk mencabut dan memulihkan capability Import data (Create) akun uji (disediakan tim FE/BE; pemicu state, P-2); file picker; muat ulang halaman; skrip reset draft; membaca status respons permintaan Confirm Mapping yang dikirim browser (intercept network, disediakan tim FE). Hook `after` memulihkan capability Import data (Create) akun uji walau spec gagal di tengah.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk kedua akun, lihat `suite.md`.
- State global: capability akun Import data (Create) Client C (dicabut di tengah TC-GS-IMPORT-44 dan dipulihkan hook `after`).

## Test Steps

### TC-GS-IMPORT-597: Create Missing Divisions pada Callout dan menu row action Disabled bagi Import data (Read Only)

1. Reset Client C ke tanpa draft; seed draft User Login D-14 (4 baris, `user-login-cm.csv`) lewat skrip fixture
2. Muat ulang halaman Import > Brand
3. Klik Sub-Tab User Login
4. Perhatikan Error Summary Callout
5. Verifikasi Error Summary Callout memuat pesan "Division not found" dengan badge "1 row"
6. Verifikasi Error Summary Callout memuat `[View Data]`, `[Delete All Rows]`, dan `[Create Missing Divisions]`
7. Hover `[Create Missing Divisions]` pada Error Summary Callout
8. Verifikasi `[Create Missing Divisions]` pada Callout tampil Disabled
9. Verifikasi tooltip "You don't have permission to do this."
10. Klik `[⋯]` pada baris dengan Division `Logistik`
11. Perhatikan menu
12. Verifikasi menu `[⋯]` baris `Logistik` memuat item `[Create Missing Divisions]`
13. Hover item `[Create Missing Divisions]` pada menu
14. Verifikasi item `[Create Missing Divisions]` tampil Disabled
15. Verifikasi tooltip "You don't have permission to do this."

### TC-GS-IMPORT-44: Capability Import data (Create) dicabut saat Modal Column Mapping terbuka menolak Confirm Mapping

16. Ganti akun: logout dari Import data (Read Only) Client C
17. Login sebagai Import data (Create) Client C dengan `Spectra.env.GS_CLIENTC_IMPORTCREATE_PASSWORD`
18. Buka menu Import dari sidebar (User berada di Import > Brand tanpa draft)
19. Klik `[Upload File]`
20. Pilih berkas `brand-12.csv` di file picker
21. Tunggu aksi selesai (permintaan mendapat respons)
22. Cabut capability Import data (Create) dari akun uji lewat fixture tanpa menutup Modal Column Mapping (capability Read tetap aktif)
23. Klik `[Confirm Mapping]`
24. Perhatikan halaman
25. Verifikasi server menolak permintaan Confirm Mapping dengan 403 Forbidden
26. Verifikasi tampil toast error "You don't have permission to do this."
27. Muat ulang halaman Import
28. Perhatikan halaman
29. Verifikasi halaman menampilkan Dropzone Disabled tanpa draft
30. Verifikasi Staging Metric Cards: Total Rows 0, Ready to Import 0, Errors 0, dan Duplicates 0
31. Pulihkan capability Import data (Create) akun uji lewat fixture

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 597, 44. TC-GS-IMPORT-44 di akhir karena ganti akun dan mengubah capability akun (state global).
- P-2: pencabutan capability lewat fixture Role & Permission (langkah 22) hanya pemicu state; objek uji adalah penolakan Confirm Mapping di UI dan responsnya, bukan request langsung ke server (kelas a). Tidak ada konteks UI kedua.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (reset dan seed lewat skrip fixture sinkron, tanpa penanda tunggu), langkah 2 (muat ulang halaman), langkah 4, 11, 24, 28 (mengamati sesuai Langkah Uji TC), langkah 16 sampai 18 (ganti akun dan buka menu), langkah 21 (menunggu unggahan berkas diproses sebelum pencabutan capability), langkah 31 (pemulihan capability, S-09; hook `after` sebagai cadangan).
- Langkah 25 (403 Forbidden) mengasersi respons server atas Confirm Mapping yang dikirim browser (bukan request langsung); toast pada langkah 26 diasersi karena ditulis di Expected TC.
- Temuan untuk QA:
  - TC-GS-IMPORT-44 mengandalkan fixture Role & Permission untuk mencabut/memulihkan capability tanpa mendefinisikan mekanismenya di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
  - TC-GS-IMPORT-597 mensyaratkan draft D-14 dan akun Import data (Read Only) Client C; seed draft memakai skrip fixture yang disediakan tim FE/BE. Data literal Population tanpa suffix `{runId}`.
