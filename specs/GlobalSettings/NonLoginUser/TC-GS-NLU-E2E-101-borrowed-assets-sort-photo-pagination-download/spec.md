---
id: TC-GS-NLU-E2E-101-borrowed-assets-sort-photo-pagination-download
title: "Borrowed Assets: Sort, Photo, Pagination, dan Download"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-361
  - TC-GS-NLU-362
  - TC-GS-NLU-363
  - TC-GS-NLU-372
  - TC-GS-NLU-374
coverage:
  web: automated
---

# Borrowed Assets: Sort, Photo, Pagination, dan Download

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup (hanya dibaca, tidak diubah atau dihapus): Tabel Data Uji Pre-setup No. 9 sampai 13 (Position, Division, pool Login User Represented By, Non-Login User dasar, Custom Field dasar).
- Non-Login User Pre-setup `Budi Kurniawan` dan `Banyak Aset` (No. 11, dengan 12 Borrowed Asset pada No. 14) dan data FAMS hanya dibaca; spec tidak membuat, mengubah, atau menghapus data.
- Data FAMS (Tabel Data Uji Pre-setup No. 14, hanya dibaca; diakses lewat rute modul aset FAMS, LLD §4): Budi Kurniawan memiliki Borrowed `BRW-20260610-0001` (Laptop - 1, Asset ID `AST-00123`, Dell Latitude 5420, due `20/08/26`) dan `BRW-20260702-0003` (Proyektor, Epson EB-X06, due `05/08/26`), Assigned `ASG-20260505-0001` (Company Vehicle B1234XY, Asset ID `AST-00456`, Honda Vario 125) dan `ASG-20260610-0002` (Mesin Bor, Asset ID `AST-00789`, Bosch GSB 13), semuanya dengan PIC `Siti Rahma`.
- Tabel `Kolom sort kelas teks TC-GS-NLU-361` (dipakai langkah 5 sampai 10):

  | Kolom |
  |---|
  | `Transaction ID` |
  | `Name` |
  | `Asset ID` |
  | `Brand` |
  | `Model / Type` |
  | `PIC` |
- Format tanggal General Settings: Date Format `dd/MM/yy` (Tabel Data Uji Pre-setup No. 16); spec tidak mengubahnya.
- Kemampuan teknis: membaca urutan baris tabel, menerima unduhan berkas CSV dan membaca nama berkas serta header dan jumlah barisnya.
- Suite berjalan serial (`parallel: false`). Hook `after` memulihkan sesi ke akun default suite.

## Test Steps

### TC-GS-NLU-363: Kolom Photo tidak memiliki ikon sort

1. Ketik Search `Budi Kurniawan`, tekan Enter
2. Buka Detail Non-Login User dengan Name tepat `Budi Kurniawan`
3. Klik tab `Responsibilities`, sub-tab `Borrowed Assets`
4. Verifikasi header kolom Photo tanpa ikon sort

### TC-GS-NLU-361: Sort 3 tahap kelas teks alfabetis pada Borrowed Assets

5. Untuk setiap baris tabel `Kolom sort kelas teks TC-GS-NLU-361` di `## Prerequisites` (langkah 5 sampai 10): klik header kolom pada baris tabel satu kali
6. Verifikasi klik #1: baris terurut ascending A-Z pada kolom tersebut
7. Klik header kolom yang sama untuk kedua kali
8. Verifikasi klik #2: baris terurut descending Z-A pada kolom tersebut
9. Klik header kolom yang sama untuk ketiga kali
10. Verifikasi klik #3: urutan kembali ke default sort tabel (Due Return Date naik)

### TC-GS-NLU-362: Sort 3 tahap kelas tanggal pada Borrowed Assets

11. Klik header kolom `Due Return Date` satu kali
12. Verifikasi klik #1: baris terurut `Oldest First` pada kolom `Due Return Date` (default ascending)
13. Klik header kolom `Due Return Date` untuk kedua kali
14. Verifikasi klik #2: baris terurut `Newest First` pada kolom `Due Return Date`
15. Klik header kolom `Due Return Date` untuk ketiga kali
16. Verifikasi klik #3: urutan kembali ke default sort tabel (Due Return Date naik)

### TC-GS-NLU-372: Download Borrowed Assets mengikuti filter

17. Klik icon Filter, pilih Brand `Dell`, klik `[Apply]`
18. Klik Download > `Download as CSV`
19. Verifikasi tidak ada toast sukses
20. Verifikasi berkas `Borrowed-Assets-Budi-Kurniawan.csv` terunduh
21. Verifikasi header berkas tanpa kolom Photo
22. Verifikasi jumlah baris data berkas sama dengan jumlah baris hasil Filter Brand `Dell` (satu baris)
23. Klik `[Clear Field]` pada Filter Panel, klik `[Apply]`

### TC-GS-NLU-374: Pagination Borrowed Assets tampil saat baris lebih dari 10

24. Kembali ke daftar Non-Login User (Global Settings > User > User List > sub-tab Non-Login User)
25. Ketik Search `Banyak Aset`, tekan Enter
26. Buka Detail Non-Login User dengan Name tepat `Banyak Aset`
27. Klik tab `Responsibilities`, sub-tab `Borrowed Assets`
28. Verifikasi kontrol pagination tampil dengan default 10 baris per halaman
29. Klik halaman 2
30. Verifikasi halaman 2 memuat 2 baris

## Notes

- Sumber TC: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber diubah: TC-GS-NLU-363 (kolom Photo tanpa ikon sort) ditaruh paling awal sebagai screening, lalu 361, 362, 372, 374.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 3 (Search `Budi Kurniawan`, membuka Detail, dan sub-tab `Borrowed Assets`; R-16); langkah 17 dan 23 (memasang dan mengosongkan Filter Brand); langkah 24, 25, 26, 27 (kembali ke daftar dan membuka Detail `Banyak Aset`).
- Langkah yang diulang: langkah 5 sampai 10 diulang untuk enam baris tabel `Kolom sort kelas teks TC-GS-NLU-361` di Prerequisites; pada tahap ketiga default sort Borrowed Assets adalah Due Return Date naik.
- Asersi tambahan (konkretisasi Expected): TC-GS-NLU-372 "berkas hanya memuat baris Dell" ditulis sebagai jumlah baris data berkas sama dengan hasil Filter (satu baris), karena isi sel berkas termasuk kelas f (bagian 3 prinsip 13f) dan tidak diasersi di spec ini.
- Pembagian TC lintas spec: Screening, data, default sort, scope ada di spec 099; Search dan Filter ada di spec 100; Setup Column ada di spec 102 dan 103.
- Temuan untuk QA:
  - TC-GS-NLU-361: PIC bernilai satu (`Siti Rahma`) pada semua transaksi Budi Kurniawan sehingga hasil sort kolom `PIC` tidak punya dua nilai distinct pada halaman teramati; asersi urutan kolom itu tidak dapat membuktikan sort (S-11, S-14). Data transaksi dengan PIC kedua perlu disediakan tim FE atau dikonfirmasi QA.
  - TC-GS-NLU-372: Expected "berkas hanya memuat baris Dell" adalah isi sel berkas (kelas f); belum ada spec kelas f untuk isi berkas Borrowed Assets.
- Spec melewati sekitar 35 langkah (30 langkah nominal, 60 dengan ekspansi sort enam kolom). Alasan: seluruh blok memakai satu surface (sub-tab Borrowed Assets), satu dataset, dan satu kelas harness (fungsional), dan tiap blok berdiri sendiri (kegagalan sort satu kolom tidak membuat blok lain kehilangan makna); memisahkannya mengulang login dan navigasi Detail.
  - TC-GS-NLU-374: TC tidak menyebut siapa user dengan 12 Borrowed Asset; spec memakai Non-Login User `Banyak Aset` (Pre-setup No. 14). Cara membuka Detail Non-Login User dari daftar tidak dijelaskan TC (hanya "User > Detail"); spec menulis "Buka Detail Non-Login User" tanpa mekanisme klik tertentu.
