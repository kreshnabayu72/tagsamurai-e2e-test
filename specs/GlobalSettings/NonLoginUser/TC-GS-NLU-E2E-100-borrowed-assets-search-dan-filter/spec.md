---
id: TC-GS-NLU-E2E-100-borrowed-assets-search-dan-filter
title: "Borrowed Assets: Search dan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-357
  - TC-GS-NLU-358
  - TC-GS-NLU-359
  - TC-GS-NLU-360
coverage:
  web: automated
---

# Borrowed Assets: Search dan Filter

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup (hanya dibaca, tidak diubah atau dihapus): Tabel Data Uji Pre-setup No. 9 sampai 13 (Position, Division, pool Login User Represented By, Non-Login User dasar, Custom Field dasar).
- Non-Login User `Budi Kurniawan` (Pre-setup No. 11) dan data FAMS (No. 14) hanya dibaca; spec tidak membuat, mengubah, atau menghapus data.
- Data FAMS (Tabel Data Uji Pre-setup No. 14, hanya dibaca; diakses lewat rute modul aset FAMS, LLD §4): Budi Kurniawan memiliki Borrowed `BRW-20260610-0001` (Laptop - 1, Asset ID `AST-00123`, Dell Latitude 5420, due `20/08/26`) dan `BRW-20260702-0003` (Proyektor, Epson EB-X06, due `05/08/26`), Assigned `ASG-20260505-0001` (Company Vehicle B1234XY, Asset ID `AST-00456`, Honda Vario 125) dan `ASG-20260610-0002` (Mesin Bor, Asset ID `AST-00789`, Bosch GSB 13), semuanya dengan PIC `Siti Rahma`.
- Tabel `Data uji Search TC-GS-NLU-357` (dipakai langkah 6 sampai 7):

  | Kolom | Kata kunci | Baris yang diharapkan |
  |---|---|---|
  | `Transaction ID` | `0003` | `Proyektor` |
  | `Name` | `proyek` | `Proyektor` |
  | `Asset ID` | `00123` | `Laptop - 1` |
  | `Brand` | `dell` | `Laptop - 1` |
  | `Model / Type` | `x06` | `Proyektor` |
  | `PIC` | `rahma` | `Proyektor dan Laptop - 1` |
- Format tanggal General Settings: Date Format `dd/MM/yy` (Tabel Data Uji Pre-setup No. 16); spec tidak mengubahnya.
- Kemampuan teknis: memilih rentang tanggal pada Filter Panel, membaca opsi dropdown Filter.
- Suite berjalan serial (`parallel: false`). Hook `after` memulihkan sesi ke akun default suite.

## Test Steps

### TC-GS-NLU-357: Search substring dan case-insensitive pada kolom Transaction ID, Name, Asset ID, Brand, Model / Type, PIC di Borrowed Assets

1. Ketik Search `Budi Kurniawan`, tekan Enter
2. Buka Detail Non-Login User dengan Name tepat `Budi Kurniawan`
3. Klik tab `Responsibilities`, sub-tab `Borrowed Assets`
4. Verifikasi tabel Borrowed Assets memuat baris Proyektor dan Laptop - 1 sebelum Search (pembanding generik)
5. Klik icon Search
6. Untuk setiap baris tabel `Data uji Search TC-GS-NLU-357` di `## Prerequisites` (langkah 6 sampai 7): ketik Search kata kunci pada baris tabel, tekan Enter
7. Verifikasi baris yang diharapkan pada baris tabel ditemukan dan setiap baris yang tampil memuat kata kunci pada kolom pada baris tabel (substring, tidak membedakan huruf besar kecil)

### TC-GS-NLU-358: Kolom Photo dan Due Return Date tidak dapat dicari lewat Search Borrowed Assets

8. Ganti isi kotak search dengan `05/08/26` (teks Due Return Date baris Proyektor), tekan Enter
9. Verifikasi empty state `No results found`

### TC-GS-NLU-359: Empty state saat Search tidak ditemukan di Borrowed Assets

10. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
11. Verifikasi ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
12. Klik `(←)` pada kotak Search

### TC-GS-NLU-360: Filter Borrowed Assets: Name, Brand, PIC, dan Due Return Date

13. Klik icon Filter
14. Verifikasi field Filter Panel: `Name` (`"All assets"`), `Brand` (`"All brands"`), `PIC` (`"All PICs"`), `Due Return Date` (`"Select date"`)
15. Verifikasi tabel sebelum Filter memuat baris Proyektor dan Laptop - 1 (pembanding generik)
16. Verifikasi opsi dropdown Name hanya `Proyektor` dan `Laptop - 1` (nilai yang ada di tabel)
17. Pilih Name `Proyektor`, klik `[Apply]`
18. Verifikasi setiap baris yang tampil ber-Name `Proyektor`
19. Klik `[Clear Field]` pada Filter Panel, klik `[Apply]`
20. Verifikasi opsi dropdown Brand hanya `Dell` dan `Epson` (nilai yang ada di tabel)
21. Pilih Brand `Dell`, klik `[Apply]`
22. Verifikasi setiap baris yang tampil ber-Brand `Dell`
23. Klik `[Clear Field]` pada Filter Panel, klik `[Apply]`
24. Verifikasi opsi dropdown PIC hanya `Siti Rahma` (nilai yang ada di tabel)
25. Pilih PIC `Siti Rahma`, klik `[Apply]`
26. Verifikasi setiap baris yang tampil ber-PIC `Siti Rahma`
27. Klik `[Clear Field]` pada Filter Panel, klik `[Apply]`
28. Pilih rentang Due Return Date `01/08/26` sampai `10/08/26`, klik `[Apply]`
29. Verifikasi setiap baris yang tampil ber-Due Return Date dalam rentang yang dipilih
30. Klik `[Clear Field]` pada Filter Panel, klik `[Apply]`

## Notes

- Sumber TC: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (357, 358, 359, 360) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 3 (Search `Budi Kurniawan`, membuka Detail, dan sub-tab `Borrowed Assets`; R-16); langkah 5 (membuka input Search); langkah 12 (mengosongkan Search); langkah 13 (membuka Filter Panel); langkah 19, 23, 27, 30 (mengosongkan Filter di antara dan sesudah filter, S-09).
- Langkah yang diulang: langkah 6 sampai 7 diulang untuk enam baris tabel `Data uji Search TC-GS-NLU-357` di Prerequisites.
- Asersi tambahan (konkretisasi Expected): kolom "Baris yang diharapkan" pada tabel Search diturunkan dari data FAMS Pre-setup No. 14; "opsi hanya nilai yang ada di tabel" (TC-GS-NLU-360 b) ditulis sebagai daftar opsi dari data Pre-setup; rentang Due Return Date `01/08/26` sampai `10/08/26` dipilih spec supaya hanya Proyektor (`05/08/26`) masuk rentang.
- Pembagian TC lintas spec: Screening, data, default sort, scope, hanya-baca ada di spec 099; Sort, Photo, Pagination, Download ada di spec 101; Setup Column ada di spec 102 dan 103.
- Temuan untuk QA:
  - TC-GS-NLU-360: langkah TC memilih Name `Proyektor` lalu Brand `Dell` lalu PIC berurutan; bila Filter bersifat kumulatif, kombinasi `Proyektor` (Epson) dan `Dell` menghasilkan hasil kosong. Spec mengosongkan Filter dengan `[Clear Field]` di antara tiap Filter sehingga tiap Filter diuji sendiri, dan tidak menguji kombinasi.
  - TC-GS-NLU-358: TC tidak menyebut tanggal yang diketik; spec memakai `05/08/26` (Due Return Date baris Proyektor). Judul TC menyebut kolom Photo tetapi langkah dan Expected hanya memuat Due Return Date; kolom Photo tidak diuji.
- Spec melewati sekitar 35 langkah (30 langkah nominal, 40 dengan ekspansi Search enam kolom). Alasan: seluruh blok memakai satu layar (sub-tab Borrowed Assets), satu dataset, dan satu kelas harness (fungsional), dan tiap blok berdiri sendiri (kegagalan satu kata kunci tidak membuat blok lain kehilangan makna); memisahkannya mengulang login dan navigasi Detail.
  - TC-GS-NLU-360: TC tidak menyebut rentang Due Return Date. Cara membuka Detail Non-Login User dari daftar tidak dijelaskan TC (hanya "User > Detail"); spec menulis "Buka Detail Non-Login User" tanpa mekanisme klik tertentu.
