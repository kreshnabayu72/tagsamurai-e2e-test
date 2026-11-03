---
id: TC-GS-NLU-E2E-104-assigned-assets-screening-default-sort-search
title: "Assigned Assets: Screening, Default Sort, dan Search"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-377
  - TC-GS-NLU-378
  - TC-GS-NLU-379
  - TC-GS-NLU-380
coverage:
  web: automated
---

# Assigned Assets: Screening, Default Sort, dan Search

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup (hanya dibaca, tidak diubah atau dihapus): Tabel Data Uji Pre-setup No. 9 sampai 13 (Position, Division, pool Login User Represented By, Non-Login User dasar, Custom Field dasar).
- Non-Login User `Budi Kurniawan` (Pre-setup No. 11) dan data FAMS (No. 14) hanya dibaca; spec tidak membuat, mengubah, atau menghapus data.
- Data FAMS (Tabel Data Uji Pre-setup No. 14, hanya dibaca; diakses lewat rute modul aset FAMS, LLD §4): Budi Kurniawan memiliki Borrowed `BRW-20260610-0001` (Laptop - 1, Asset ID `AST-00123`, Dell Latitude 5420, due `20/08/26`) dan `BRW-20260702-0003` (Proyektor, Epson EB-X06, due `05/08/26`), Assigned `ASG-20260505-0001` (Company Vehicle B1234XY, Asset ID `AST-00456`, Honda Vario 125) dan `ASG-20260610-0002` (Mesin Bor, Asset ID `AST-00789`, Bosch GSB 13), semuanya dengan PIC `Siti Rahma`.
- Tabel `Data uji Search TC-GS-NLU-379` (dipakai langkah 13 sampai 14):

  | Kolom | Kata kunci | Baris yang diharapkan |
  |---|---|---|
  | `Transaction ID` | `0001` | `Company Vehicle B1234XY` |
  | `Name` | `vehicle` | `Company Vehicle B1234XY` |
  | `Asset ID` | `00456` | `Company Vehicle B1234XY` |
  | `Brand` | `honda` | `Company Vehicle B1234XY` |
  | `Model / Type` | `vario` | `Company Vehicle B1234XY` |
  | `PIC` | `rahma` | `Company Vehicle B1234XY dan Mesin Bor` |
- Kemampuan teknis: membaca teks sel tabel dan header kolom.
- Suite berjalan serial (`parallel: false`). Hook `after` memulihkan sesi ke akun default suite.

## Test Steps

### TC-GS-NLU-377: Screening sub-tab Assigned Assets

1. Ketik Search `Budi Kurniawan`, tekan Enter
2. Buka Detail Non-Login User dengan Name tepat `Budi Kurniawan`
3. Klik tab `Responsibilities`, sub-tab `Assigned Assets`
4. Verifikasi sub-tab `Assigned Assets` aktif
5. Verifikasi toolbar: `Search | Filter | Download`
6. Verifikasi kolom: `Photo | Transaction ID (sortable) | Name (sortable) | Asset ID (sortable) | Brand (sortable) | Model / Type (sortable) | PIC (sortable) | Column Visibility (⋯) (unsortable)`
7. Verifikasi tabel tidak memuat kolom tanggal
8. Verifikasi baris `Company Vehicle B1234XY`: Transaction ID `ASG-20260505-0001`, Asset ID `AST-00456`, Brand `Honda`, Model / Type `Vario 125`, PIC `Siti Rahma`
9. Verifikasi baris `Mesin Bor`: Transaction ID `ASG-20260610-0002`, Asset ID `AST-00789`, Brand `Bosch`, Model / Type `GSB 13`, PIC `Siti Rahma`
10. Verifikasi tabel memuat tepat dua baris

### TC-GS-NLU-378: Default sort Assigned Assets Name A-Z

11. Verifikasi baris terurut Name A-Z: `Company Vehicle B1234XY` sebelum `Mesin Bor`

### TC-GS-NLU-379: Search substring dan case-insensitive pada kolom Transaction ID, Name, Asset ID, Brand, Model / Type, PIC di Assigned Assets

12. Klik icon Search
13. Untuk setiap baris tabel `Data uji Search TC-GS-NLU-379` di `## Prerequisites` (langkah 13 sampai 14): ketik Search kata kunci pada baris tabel, tekan Enter
14. Verifikasi baris yang diharapkan pada baris tabel ditemukan dan setiap baris yang tampil memuat kata kunci pada kolom pada baris tabel (substring, tidak membedakan huruf besar kecil)

### TC-GS-NLU-380: Empty state saat Search tidak ditemukan di Assigned Assets

15. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
16. Verifikasi ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
17. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (377, 378, 379, 380) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 3 (Search `Budi Kurniawan`, membuka Detail, dan sub-tab `Assigned Assets`; R-16); langkah 12 (membuka input Search); langkah 17 (mengosongkan Search di akhir spec). TC-GS-NLU-378 tidak mengulang klik sub-tab karena dijalankan pada state TC-GS-NLU-377.
- Langkah yang diulang: langkah 13 sampai 14 diulang untuk enam baris tabel `Data uji Search TC-GS-NLU-379` di Prerequisites.
- Asersi tambahan (konkretisasi Expected): "Dua baris" (TC-GS-NLU-377 d) ditulis juga sebagai tabel memuat tepat dua baris; kolom "Baris yang diharapkan" pada tabel Search diturunkan dari data FAMS Pre-setup No. 14.
- Pembagian TC lintas spec: Filter, Sort, Download, empty state ada di spec 105; Setup Column ada di spec 106 dan 107; Borrowed Assets ada di spec 099 sampai 103.
- Temuan untuk QA:
  - TC-GS-NLU-378: precondition menunjuk "Detail Non-Login User dengan dua Assigned Asset (Pre-setup No. 14)" tanpa menyebut nama; spec memakai Budi Kurniawan sesuai TC-GS-NLU-377. Cara membuka Detail Non-Login User dari daftar tidak dijelaskan TC (hanya "User > Detail"); spec menulis "Buka Detail Non-Login User" tanpa mekanisme klik tertentu.
