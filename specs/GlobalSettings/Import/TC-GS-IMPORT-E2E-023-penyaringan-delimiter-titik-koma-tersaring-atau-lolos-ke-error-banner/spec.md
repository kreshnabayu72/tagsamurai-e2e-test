---
id: TC-GS-IMPORT-E2E-023-penyaringan-delimiter-titik-koma-tersaring-atau-lolos-ke-error-banner
title: "Penyaringan Delimiter: Titik Koma Tersaring atau Lolos ke Error Banner Pemetaan (Measurement, Brand, Position, Division, dan Tab User Client G)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-94
  - TC-GS-IMPORT-564
  - TC-GS-IMPORT-815
  - TC-GS-IMPORT-859
  - TC-GS-IMPORT-867
coverage:
  web: automated
---

# Penyaringan Delimiter: Titik Koma Tersaring atau Lolos ke Error Banner Pemetaan (Measurement, Brand, Position, Division, dan Tab User Client G)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor:
  - Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-94, 564, dan 815. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`).
  - Total Control Client G (Putri Ananda) `totalControl_automated_qaTeam10@qwertysystem.net` (Pre-setup; Custom Field Active Required `Badge Code` (Text) satu-satunya) untuk TC-GS-IMPORT-859 dan 867: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_CLIENTG_TC_PASSWORD` (env baru). Hook `after` mengembalikan sesi ke Total Control Client A.
  - Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk akun aktor pertama; perpindahan Sub-Tab ditulis sebagai langkah eksplisit.
- Data: Client C tanpa draft Tab Measurement, Brand, Position, dan Division; Client G tanpa draft Tab User Login (Kontrak Fixture R1; skrip reset disediakan tim FE/BE). Tidak ada draft yang tercipta karena tidak ada Confirm Mapping. Berkas fixture (D-07, isi literal):
  - `measurement-semicolon.csv`: header `Unit Name;Symbol`; baris `Meter;m`, `Liter;L`, `Gram;g`.
  - `brand-semicolon.csv`: header `Brand Name;Catatan`; baris `Nikon;a`, `Ricoh;b`, `Xerox;c`.
  - `position-semicolon.csv`: header `Position Name;Catatan`; baris `Teknisi;a`, `Kepala Shift;b`, `Operator;c`.
  - `division-semicolon.csv`: header `Division Name;Code`; baris `Logistik;LOG`, `Keuangan;KEU`, `Pemasaran;PMS`.
  - `user-login-5cols.csv`: header `First Name,Last Name,Email,Division,Access` (pemisah koma, tanpa kolom `Badge Code`); 1 baris data valid.
  - `user-login-4cols.csv`: header `First Name,Last Name,Email,Division` (pemisah koma, tanpa kolom `Access` dan `Badge Code`); 1 baris data valid.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk kedua akun, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft; ganti akun dan client.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-IMPORT-94: Berkas CSV Measurement berdelimiter titik koma tersaring

1. Klik Sub-Tab Measurement
2. Klik `[Upload File]`
3. Pilih berkas `measurement-semicolon.csv` di file picker
4. Perhatikan halaman
5. Verifikasi halaman tetap menampilkan Dropzone tanpa draft
6. Verifikasi berkas tidak diproses: tanpa toast dan tanpa pesan error
7. Verifikasi Modal Column Mapping tidak terbuka

### TC-GS-IMPORT-564: Berkas Brand berdelimiter titik koma melewati penyaringan dan berhenti di Error Banner pemetaan

8. Klik Sub-Tab Brand
9. Klik `[Upload File]`
10. Pilih berkas `brand-semicolon.csv` di file picker
11. Perhatikan Modal Column Mapping
12. Verifikasi Modal Column Mapping terbuka
13. Verifikasi header terbaca sebagai satu kolom `Brand Name;Catatan` yang tidak ter-auto-match
14. Verifikasi dropdown Brand Name "No Column"
15. Verifikasi Error Banner "The following columns contain errors and cannot be imported:" memuat `Brand Name`
16. Verifikasi `[Confirm Mapping]` tetap Enabled
17. Klik `[Cancel]`

### TC-GS-IMPORT-815: Berkas titik koma pada Position dan Division melewati penyaringan dan berhenti di Error Banner pemetaan

18. Klik Sub-Tab Position
19. Klik `[Upload File]`
20. Pilih berkas `position-semicolon.csv` di file picker
21. Perhatikan Modal Column Mapping
22. Verifikasi Modal Column Mapping terbuka
23. Verifikasi header terbaca sebagai satu kolom `Position Name;Catatan` yang tidak ter-auto-match
24. Verifikasi dropdown Position Name "No Column"
25. Verifikasi Error Banner "The following columns contain errors and cannot be imported:" memuat `Position Name`
26. Verifikasi `[Confirm Mapping]` tetap Enabled
27. Klik `[Cancel]`
28. Verifikasi modal tertutup
29. Verifikasi Import > Position menampilkan Dropzone tanpa draft
30. Klik Sub-Tab Division
31. Klik `[Upload File]`
32. Pilih berkas `division-semicolon.csv` di file picker
33. Perhatikan Modal Column Mapping
34. Verifikasi Modal Column Mapping terbuka
35. Verifikasi header terbaca sebagai satu kolom `Division Name;Code` yang tidak ter-auto-match
36. Verifikasi dropdown Division Name "No Column"
37. Verifikasi Error Banner "The following columns contain errors and cannot be imported:" memuat `Division Name`
38. Verifikasi `[Confirm Mapping]` tetap Enabled
39. Klik `[Cancel]`
40. Verifikasi modal tertutup
41. Verifikasi Import > Division menampilkan Dropzone tanpa draft

### TC-GS-IMPORT-859: Penyaringan delimiter Tab User tidak menghitung Custom Field wajib (Client G)

42. Ganti akun: logout dari Total Control Client C
43. Login sebagai Total Control Client G dengan `Spectra.env.GS_CLIENTG_TC_PASSWORD`
44. Buka Import > User Login
45. Klik `[Upload File]`
46. Pilih berkas `user-login-5cols.csv` di file picker
47. Perhatikan Modal Column Mapping
48. Verifikasi berkas lolos penyaringan dan Modal Column Mapping terbuka
49. Verifikasi Error Banner mendaftar `Badge Code` sebagai field wajib yang belum terpetakan
50. Klik `[Cancel]`

### TC-GS-IMPORT-867: Penyaringan delimiter Tab User: header koma dengan 4 kolom kurang dari 5 atribut wajib bawaan tersaring (Client G)

51. Klik `[Upload File]`
52. Pilih berkas `user-login-4cols.csv` di file picker
53. Perhatikan halaman
54. Verifikasi halaman tetap menampilkan Dropzone tanpa draft
55. Verifikasi berkas tersaring dan tidak diproses
56. Verifikasi tanpa toast dan tanpa pesan error
57. Verifikasi Modal Column Mapping tidak terbuka
58. Verifikasi tidak ada draft dibuat

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 94, 564, 815 (Client C), lalu 859 dan 867 (Client G) dengan langkah ganti akun eksplisit (langkah 42 dan 43). Bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Alasan di atas sekitar 35 langkah (58 langkah): satu topik (penyaringan delimiter dan Error Banner pemetaan) tanpa aksi yang mengubah data; tiap blok memakai berkas sendiri sehingga berdiri sendiri; blok akun lain di akhir.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 8, 18, 30 (pindah Sub-Tab), langkah 4, 11, 21, 33, 47, 53 (mengamati sesuai Langkah Uji TC), langkah 17, 27, 39, 50 (menutup modal dengan `[Cancel]`), langkah 42 sampai 44 (ganti akun dan buka tab).
- Penjelasan internal pada Expected TC-GS-IMPORT-859 a ("header terurai menjadi 5 kolom, sama dengan jumlah atribut wajib bawaan") dan TC-GS-IMPORT-867 a ("header terurai menjadi 4 kolom, kurang dari 5 atribut wajib bawaan; Custom Field `Badge Code` tidak dihitung") tidak diasersi karena jumlah kolom hasil penguraian tidak teramati di UI; yang diasersi hanya keadaan teramati: Modal Column Mapping terbuka (langkah 48) dan Error Banner `Badge Code` (langkah 49) untuk 5 kolom; Dropzone tetap, berkas tidak diproses, tanpa toast dan pesan error, modal tidak terbuka, tanpa draft (langkah 54 sampai 58) untuk 4 kolom.
- Temuan untuk QA:
  - TC-GS-IMPORT-859 dan 867 menyebut "berkas pada Data Uji" tanpa langkah memilih nama berkas yang eksplisit pada kolom Langkah; spec memakai nama berkas pada Data Uji (`user-login-5cols.csv`, `user-login-4cols.csv`).
  - Expected TC-GS-IMPORT-859 a dan 867 a memuat penjelasan internal ("header terurai menjadi N kolom", perbandingan dengan jumlah atribut wajib bawaan) yang tidak teramati di UI; spec tidak mengasersinya dan memakai hasil teramati (modal terbuka atau tersaring).
  - Skrip reset draft Client C dan Client G tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
