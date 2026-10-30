---
id: TC-GS-ROLE-E2E-058-download-tab-total-control-dan-read-only-isi-file
title: "Download Tab Total Control dan Read Only: Nama File, Isi File, Cakupan Baris, Kolom Visible, dan Transformasi Nilai"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-174
  - TC-GS-ROLE-175
  - TC-GS-ROLE-176
  - TC-GS-ROLE-177
  - TC-GS-ROLE-178
coverage:
  web: automated
---

# Download Tab Total Control dan Read Only: Nama File, Isi File, Cakupan Baris, Kolom Visible, dan Transformasi Nilai

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Role; tabel dan berkas dibuat dari backend nyata.
- Akun: Total Control, Ahmad Fauzi (Pre-setup #1), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Role & Permission > Total Control dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (tetap di environment, hanya dibaca): Tab Total Control berisi N_TC user (11 atau lebih, Pre-setup #17) termasuk Budi Santoso (Default User; Position, Division, Modified By, dan Last Updated kosong di tabel), Dewi Lestari (Inactive; Pre-setup #3), dan N_aktif user berstatus Active; Tab Read Only berisi sedikitnya 3 user. N_TC dan N_aktif dihitung dari seeding environment, bukan dibaca dari tabel yang hanya menampilkan satu halaman.
- Data uji: format `CSV` (TC-GS-ROLE-174, 175, 176, 177) dan `XLSX` (TC-GS-ROLE-174, 175, 178); Filter Status `Active` (TC-GS-ROLE-176); kolom `Division` di-hide lalu di-unhide (TC-GS-ROLE-177).
- Date Format dan Time Format General Settings: nilai aktif environment (tidak diubah spec ini); asersi format tanggal memakai nilai aktif itu.
- Kemampuan teknis (kelas binary buffer, prinsip 13f konvensi): menangkap berkas unduhan browser (event download) ke direktori bersih per unduhan supaya nama berkas yang sama (`Role-Permission-Total-Control.csv`) tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV dan XLSX (nama kolom, jumlah baris data, nilai sel, jenis nilai); memeriksa avatar atau warna pada sel. Berkas unduhan dihapus di hook `after`.
- Preferensi kolom tersimpan per user di browser per tabel dan menjadi permanen setelah `[Save]` (prd-conventions.md §9.3).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan: Filter Status `Active` (dikosongkan pada langkah 33 sampai 35) dan visibilitas kolom `Division` (ditampilkan kembali pada langkah 47); hook `after` sebagai cadangan.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission, Tab Total Control.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-174: Download Tab Total Control sebagai CSV dan XLSX

1. Klik icon Download
2. Verifikasi overlay Download menampilkan `Download as CSV` dan `Download as XLSX`
3. Klik `Download as CSV`
4. Verifikasi tidak ada toast sukses
5. Verifikasi file `Role-Permission-Total-Control.csv` terunduh
6. Klik icon Download
7. Klik `Download as XLSX`
8. Verifikasi tidak ada toast sukses
9. Verifikasi file `Role-Permission-Total-Control.xlsx` terunduh

### TC-GS-ROLE-175: Download Tab Read Only sebagai CSV dan XLSX

10. Klik Tab `Read Only`
11. Klik icon Download
12. Klik `Download as CSV`
13. Verifikasi tidak ada toast sukses
14. Verifikasi file `Role-Permission-Read-Only.csv` terunduh
15. Klik icon Download
16. Klik `Download as XLSX`
17. Verifikasi tidak ada toast sukses
18. Verifikasi file `Role-Permission-Read-Only.xlsx` terunduh

### TC-GS-ROLE-176: Cakupan baris Download Tab Total Control tanpa dan dengan filter

19. Klik Tab `Total Control`
20. Klik icon Download
21. Klik `Download as CSV`
22. Buka isi file CSV yang diunduh
23. Verifikasi file memuat N_TC baris data, yaitu seluruh user Total Control di semua halaman (bukan hanya 10 baris halaman 1)
24. Klik Filter
25. Pilih Status `Active`
26. Klik `[Apply]`
27. Klik icon Download
28. Klik `Download as CSV`
29. Buka isi file CSV yang diunduh
30. Verifikasi file memuat sedikitnya satu baris data
31. Verifikasi setiap baris data di file berstatus `Active`
32. Verifikasi file memuat N_aktif baris data, yaitu seluruh user Active di semua halaman
33. Klik Filter
34. Klik `[Clear Field]`
35. Klik `[Apply]`

### TC-GS-ROLE-177: Download mengikuti kolom yang tampil

36. Klik header kolom Column Visibility (⋯)
37. Klik item `Setup Column...`
38. Hilangkan centang `Division`
39. Klik `[Save]`
40. Klik icon Download
41. Klik `Download as CSV`
42. Buka isi file CSV yang diunduh
43. Verifikasi file memuat kolom `Name`
44. Verifikasi file tidak memuat kolom `Division`
45. Klik header kolom Column Visibility (⋯)
46. Klik item `Setup Column...`
47. Centang `Division`
48. Klik `[Save]`
49. Klik icon Download
50. Klik `Download as CSV`
51. Buka isi file CSV yang diunduh
52. Verifikasi file memuat kolom `Division`

### TC-GS-ROLE-178: Transformasi nilai pada file Download Tab Total Control

53. Klik icon Download
54. Klik `Download as XLSX`
55. Buka isi file XLSX yang diunduh
56. Periksa baris Budi Santoso dan Dewi Lestari
57. Verifikasi Status baris Budi Santoso (Default User) ditulis sebagai label teks `Active` tanpa warna
58. Verifikasi Status baris Dewi Lestari ditulis sebagai label teks `Inactive` tanpa warna
59. Verifikasi Position, Division, Modified By, dan Last Updated baris Budi Santoso ditulis `-`
60. Verifikasi Status baris Budi Santoso tidak kosong
61. Verifikasi kolom `Name` tanpa avatar
62. Verifikasi Last Updated baris Dewi Lestari mengikuti format tanggal General Settings

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE. Kelas harness binary buffer (prinsip 13f): isi berkas CSV dan XLSX dipisah dari kegagalan ekspor (spec 069) dan dari Download di atas 5.000 baris (spec 059).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (174, 175, 176, 177, 178) dipertahankan.
- Asersi absence atas state sementara (toast sukses) diletakkan segera sesudah klik pilihan format dan sebelum asersi berkas; klik pilihan format menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh. Asersi "setiap baris data berstatus `Active`" didahului `Verifikasi` yang membuktikan file memuat sedikitnya satu baris; asersi `Division` tidak ada didahului `Verifikasi` kolom `Name` ada pada file yang sama.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 33 sampai 35 (mengosongkan Filter Status), langkah 47 dan langkah sesudahnya (menampilkan kembali kolom `Division`, `[Save]`), dan langkah "Buka isi file ..." serta "Periksa baris ..." (membaca isi berkas). TC-GS-ROLE-174 dan 175 hanya mengasersi nama file dan tidak membuka isi berkas karena Expected-nya tidak menyebut isi.
- Spec melewati sekitar 35 langkah (62 langkah) karena lima TC Download memakai dataset Tab Total Control dan Tab Read Only yang sama dan satu kelas harness (binary buffer). Blok 174, 175, 176, 177, dan 178 masing-masing mengunduh berkas sendiri dan tidak bergantung pada berkas blok lain; blok 177 menyembunyikan lalu menampilkan kembali `Division` sehingga blok 178 berjalan pada konfigurasi default. Langkah membuka isi berkas termasuk blok baca berpola.
- Pembagian TC lintas spec: TC-GS-ROLE-179 (Download gagal) di spec 069; TC-GS-ROLE-180 (lebih dari 5.000 baris) di spec 059; TC-GS-ROLE-185, 194, dan 303 (Tab System dan Detail) di spec 061.
- Temuan untuk QA:
  - TC-GS-ROLE-174, 175, 176, 177, 178: TC tidak menyebut cara menangkap berkas unduhan dan membaca isinya; kemampuan tersebut disediakan tim FE (Prerequisites).
  - TC-GS-ROLE-176: TC tidak menyebut jumlah baris konkret; spec memakai N_TC dan N_aktif dari seeding. TC juga tidak menyebut cara memastikan berkas XLSX dan CSV memuat jumlah baris yang sama.
  - TC-GS-ROLE-178 Expected d: TC tidak menyebut nilai format tanggal; spec mengasersi format sesuai General Settings aktif tanpa pola tertentu. TC juga tidak menyebut apakah baris Budi Santoso ditemukan lewat nama atau email; spec memakai Name pada berkas.
  - TC-GS-ROLE-178: TC tidak menyebut nama sheet dan nama kolom berkas XLSX; spec mengasersi nilai sel baris Budi Santoso dan Dewi Lestari.
