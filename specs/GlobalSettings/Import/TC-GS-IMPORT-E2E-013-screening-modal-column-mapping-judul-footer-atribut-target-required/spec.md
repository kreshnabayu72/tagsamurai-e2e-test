---
id: TC-GS-IMPORT-E2E-013-screening-modal-column-mapping-judul-footer-atribut-target-required
title: "Screening Modal Column Mapping: Judul dan Footer, Atribut Target Required (*) User Login dan Non Login, Auto-Match Case-Insensitive, dan Penanda Required Lintas Client"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-51
  - TC-GS-IMPORT-52
  - TC-GS-IMPORT-53
  - TC-GS-IMPORT-54
  - TC-GS-IMPORT-889
coverage:
  web: automated
---

# Screening Modal Column Mapping: Judul dan Footer, Atribut Target Required (*) User Login dan Non Login, Auto-Match Case-Insensitive, dan Penanda Required Lintas Client

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor:
  - Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-51, 52, 53, 54, dan bagian pertama TC-GS-IMPORT-889. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`).
  - Total Control Client G (Putri Ananda) `totalControl_automated_qaTeam10@qwertysystem.net` (Pre-setup) untuk bagian akhir TC-GS-IMPORT-889: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_CLIENTG_TC_PASSWORD` (env baru). Sesi Client C dan Client G dijalankan berurutan, bukan bersamaan. Hook `after` mengembalikan sesi ke Total Control Client A.
  - Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; perpindahan Sub-Tab ditulis sebagai langkah eksplisit.
- Data:
  - Client C tanpa draft pada Tab Brand, User Login, dan User Non Login (Kontrak Fixture R1; skrip reset disediakan tim FE/BE). Spec tidak menjalankan Confirm Mapping sehingga tidak ada draft yang tercipta.
  - Custom Field Active Client C (seluruhnya opsional): Emergency Phone, Join Date, Overtime Hours, Shift, Shift Notes, Tax ID (Text); Custom Field nonaktif Old Badge.
  - Custom Field Active Client G: hanya `Badge Code` (Text, Required). Client G tanpa draft Tab User Login.
  - Berkas fixture (D-07, isi literal): `brand-12.csv` (header `Brand Name`; 12 baris D-01); `user-login-8.csv` (D-05, header `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period,Shift,Overtime Hours`); `user-non-login-5.csv` (D-06); `brand-header-case.csv` (header `  brand name  `, huruf kecil dengan spasi di tepi; 3 baris Nikon, Ricoh, Xerox); `user-login-marker.csv` (header `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period,Badge Code`; 1 baris `Budi,Setiawan,budi.setiawan.c@example.com,Engineering,Finance Manager,EMP-1002,Global Settings,,BC-1`).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk kedua akun, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft; ganti akun dan client.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-IMPORT-51: Screening Modal Column Mapping Tab Brand

1. Klik `[Upload File]`
2. Pilih berkas `brand-12.csv` di file picker
3. Perhatikan modal dari atas ke bawah
4. Verifikasi Header: Title `Column Mapping: Brand`
5. Verifikasi Header: icon close `[✕]`
6. Verifikasi Description "Map columns from your uploaded file to the system attributes."
7. Verifikasi Body: Mapping Form dengan Target Attribute `Brand Name *` (label varian Required dengan asterisk `*`) dan dropdown File Column
8. Verifikasi nilai awal dropdown File Column = kolom berkas `Brand Name` (auto-match)
9. Verifikasi Footer: `[Reupload File]` di kiri
10. Verifikasi Footer: `[Cancel]` dan `[Confirm Mapping]` di kanan
11. Klik dropdown File Column untuk Brand Name
12. Verifikasi dropdown memuat opsi "No Column"
13. Verifikasi dropdown memuat kolom berkas `Brand Name`
14. Tutup dropdown File Column untuk Brand Name
15. Klik `[Cancel]` (tutup bersih)

### TC-GS-IMPORT-54: Auto-match header berkas tidak peka huruf besar-kecil dan abaikan spasi tepi

16. Klik `[Upload File]`
17. Pilih berkas `brand-header-case.csv` di file picker
18. Perhatikan dropdown File Column dan Modal Column Mapping
19. Verifikasi dropdown File Column Brand Name terpilih otomatis ke kolom `brand name`
20. Verifikasi tidak ada Error Banner
21. Klik `[Cancel]` (tutup bersih)

### TC-GS-IMPORT-52: Modal Column Mapping Tab User Login menampilkan atribut standar dan Custom Field Active

22. Klik Sub-Tab User Login
23. Klik `[Upload File]`
24. Pilih berkas `user-login-8.csv` di file picker
25. Perhatikan daftar Target Attribute
26. Verifikasi Target Attribute memuat First Name `*`, Last Name `*`, Email `*`, Division `*`, dan Access `*` (label varian Required)
27. Verifikasi Target Attribute Position, Employee ID, dan Active Period tampil tanpa penanda (opsional)
28. Verifikasi Custom Field Active Emergency Phone, Join Date, Overtime Hours, Shift, Shift Notes, dan Tax ID ditambahkan dinamis tanpa penanda `*` (opsional di Client C)
29. Verifikasi Custom Field nonaktif Old Badge tidak muncul
30. Klik `[Cancel]` (tutup bersih)

### TC-GS-IMPORT-53: Modal Column Mapping Tab User Non Login menampilkan Represented By dan tanpa Access

31. Klik Sub-Tab User Non Login
32. Klik `[Upload File]`
33. Pilih berkas `user-non-login-5.csv` di file picker
34. Perhatikan daftar Target Attribute
35. Verifikasi Target Attribute memuat First Name `*`, Last Name `*`, Email `*`, Division `*`, dan Represented By `*` (label varian Required)
36. Verifikasi Target Attribute Position, Employee ID, dan Active Period tampil tanpa penanda (opsional)
37. Verifikasi tidak ada atribut `Access`
38. Klik `[Cancel]` (tutup bersih)

### TC-GS-IMPORT-889: Penanda Required (`*`) tidak bergantung pada keadaan mapping, lintas Client C dan Client G

39. Total Control Client C: Klik Sub-Tab User Login
40. Total Control Client C: Klik `[Upload File]`
41. Total Control Client C: Pilih berkas `user-login-marker.csv` di file picker
42. Total Control Client C: Perhatikan label Target Attribute pada Modal Column Mapping
43. Verifikasi label First Name, Last Name, Email, Division, dan Access diikuti asterisk `*` (varian Required)
44. Verifikasi label Position, Employee ID, dan Active Period tanpa penanda
45. Verifikasi label Custom Field Active Client C (Emergency Phone, Join Date, Overtime Hours, Shift, Shift Notes, Tax ID) tanpa penanda karena opsional
46. Total Control Client C: Ubah dropdown File Column untuk Division menjadi "No Column"
47. Total Control Client C: Ubah dropdown File Column untuk Position menjadi "No Column"
48. Total Control Client C: Perhatikan label Target Attribute
49. Verifikasi label Division tetap ber-`*` walau dropdown-nya "No Column" (Error Banner memuat Division)
50. Verifikasi label Position tetap tanpa penanda walau dropdown-nya "No Column"
51. Total Control Client C: Ubah dropdown File Column untuk Division menjadi kolom berkas `Division`
52. Total Control Client C: Ubah dropdown File Column untuk Position menjadi kolom berkas `Position`
53. Total Control Client C: Perhatikan label Target Attribute
54. Verifikasi label First Name, Last Name, Email, Division, dan Access ber-`*` setelah kolom berkas dipilih
55. Verifikasi label Position, Employee ID, dan Active Period tanpa penanda setelah kolom berkas dipilih
56. Total Control Client C: Klik `[Cancel]`, lalu klik `[Leave]` pada dialog Unsaved Changes
57. Verifikasi modal tertutup tanpa draft
58. Ganti akun: logout dari Total Control Client C
59. Login sebagai Total Control Client G dengan `Spectra.env.GS_CLIENTG_TC_PASSWORD`
60. Total Control Client G: Buka Import > User Login
61. Total Control Client G: Klik `[Upload File]`
62. Total Control Client G: Pilih berkas `user-login-marker.csv` di file picker
63. Total Control Client G: Perhatikan label Target Attribute
64. Verifikasi label First Name, Last Name, Email, Division, dan Access ber-`*`
65. Verifikasi label Position, Employee ID, dan Active Period tanpa penanda
66. Verifikasi label Custom Field Active Required `Badge Code` ber-`*`
67. Total Control Client G: Ubah dropdown File Column untuk Badge Code menjadi "No Column"
68. Total Control Client G: Perhatikan label Target Attribute
69. Verifikasi label `Badge Code` tetap ber-`*` walau dropdown-nya "No Column" (Error Banner memuat Badge Code)
70. Total Control Client G: Klik `[Cancel]`, lalu klik `[Leave]` pada dialog Unsaved Changes

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 51, 54, 52, 53, 889. TC-GS-IMPORT-54 mengikuti TC-GS-IMPORT-51 karena sama-sama di Tab Brand (hemat perpindahan Sub-Tab); TC-GS-IMPORT-889 terakhir karena ganti client ke Client G (bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal).
- Alasan di atas sekitar 35 langkah (70 langkah): satu kelas harness (screening Modal Column Mapping tanpa Confirm sehingga tidak ada data tercipta), tiap blok berdiri sendiri; blok akun lain (Client G) di akhir dengan langkah ganti akun eksplisit.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 14, 15, 21, 30, 38 (menutup dropdown/modal secara bersih dengan `[Cancel]`; tidak ada dialog Unsaved Changes karena tidak ada perubahan mapping), langkah 22, 31, 39 (pindah Sub-Tab), langkah 57 (`Verifikasi` Expected e TC-GS-IMPORT-889), langkah 58 sampai 60 (ganti akun dan buka tab).
- Pembagian TC: TC-GS-IMPORT-55 dan 887 (header kembar) ada di spec 014; TC-GS-IMPORT-889 menguji penanda Required lintas client sehingga diletakkan di spec ini.
- Temuan untuk QA:
  - TC-GS-IMPORT-51, 52, 53, 54 tidak menyebut cara menutup Modal Column Mapping setelah asersi; spec menutup bersih lewat `[Cancel]` sebagai langkah penghubung.
  - TC-GS-IMPORT-889 menyebut "sesi browser terpisah" untuk Client C dan Client G; spec menjalankannya berurutan dengan ganti akun eksplisit (tidak ada asersi lintas sesi).
  - Skrip reset draft Client C/G tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13). Berkas fixture literal tanpa suffix `{runId}`.
