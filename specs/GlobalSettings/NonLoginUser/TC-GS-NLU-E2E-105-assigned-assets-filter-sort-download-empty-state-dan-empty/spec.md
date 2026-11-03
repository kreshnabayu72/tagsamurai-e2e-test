---
id: TC-GS-NLU-E2E-105-assigned-assets-filter-sort-download-empty-state-dan-empty
title: "Assigned Assets: Filter, Sort, Download, Empty State, dan Empty Borrowed"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-373
  - TC-GS-NLU-381
  - TC-GS-NLU-382
  - TC-GS-NLU-391
  - TC-GS-NLU-392
  - TC-GS-NLU-393
coverage:
  web: automated
---

# Assigned Assets: Filter, Sort, Download, Empty State, dan Empty Borrowed

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup (hanya dibaca, tidak diubah atau dihapus): Tabel Data Uji Pre-setup No. 9 sampai 13 (Position, Division, pool Login User Represented By, Non-Login User dasar, Custom Field dasar).
- Non-Login User Pre-setup `Siti Rahayu` (tanpa transaksi) dan `Budi Kurniawan` (No. 11) dan data FAMS (No. 14) hanya dibaca; spec tidak membuat, mengubah, atau menghapus data.
- Data FAMS (Tabel Data Uji Pre-setup No. 14, hanya dibaca; diakses lewat rute modul aset FAMS, LLD §4): Budi Kurniawan memiliki Borrowed `BRW-20260610-0001` (Laptop - 1, Asset ID `AST-00123`, Dell Latitude 5420, due `20/08/26`) dan `BRW-20260702-0003` (Proyektor, Epson EB-X06, due `05/08/26`), Assigned `ASG-20260505-0001` (Company Vehicle B1234XY, Asset ID `AST-00456`, Honda Vario 125) dan `ASG-20260610-0002` (Mesin Bor, Asset ID `AST-00789`, Bosch GSB 13), semuanya dengan PIC `Siti Rahma`.
- Tabel `Kolom sort kelas teks TC-GS-NLU-382` (dipakai langkah 24 sampai 29):

  | Kolom |
  |---|
  | `Transaction ID` |
  | `Name` |
  | `Asset ID` |
  | `Brand` |
  | `Model / Type` |
  | `PIC` |
- Pemulihan Setup Column: konfigurasi kolom yang disimpan spec ini dipulihkan hook `after` dengan menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE; TC-GS-NLU-393 menyimpan konfigurasi kolom Borrowed Assets).
- Kemampuan teknis: membaca urutan baris tabel, menerima unduhan berkas XLSX dan membaca nama berkas serta headernya.
- Suite berjalan serial (`parallel: false`). Hook `after` memulihkan state yang diubah spec ini (preferensi kolom di browser).

## Test Steps

### TC-GS-NLU-373: Empty state Borrowed Assets saat tidak ada aset dipinjam

1. Ketik Search `Siti Rahayu`, tekan Enter
2. Buka Detail Non-Login User dengan Name tepat `Siti Rahayu`
3. Klik tab `Responsibilities`, sub-tab `Borrowed Assets`
4. Verifikasi empty state Borrowed Assets: ilustrasi dengan judul `"No borrowed assets"` dan deskripsi `"This user has no borrowed assets currently."`

### TC-GS-NLU-392: Empty state Assigned Assets saat tidak ada aset ditugaskan

5. Klik sub-tab `Assigned Assets`
6. Verifikasi empty state Assigned Assets: ilustrasi dengan judul `"No assigned assets"` dan deskripsi `"This user has no assigned assets currently."`

### TC-GS-NLU-381: Filter Assigned Assets: Name, Brand, dan PIC

7. Kembali ke daftar Non-Login User (Global Settings > User > User List > sub-tab Non-Login User)
8. Ketik Search `Budi Kurniawan`, tekan Enter
9. Buka Detail Non-Login User dengan Name tepat `Budi Kurniawan`
10. Klik tab `Responsibilities`, sub-tab `Assigned Assets`
11. Klik icon Filter
12. Verifikasi field Filter Panel: `Name` (`"All assets"`), `Brand` (`"All brands"`), `PIC` (`"All PICs"`)
13. Verifikasi Filter Panel tidak memuat filter tanggal
14. Verifikasi tabel sebelum Filter memuat baris `Company Vehicle B1234XY` dan `Mesin Bor` (pembanding generik)
15. Pilih Name `Mesin Bor`, klik `[Apply]`
16. Verifikasi setiap baris yang tampil ber-Name `Mesin Bor`
17. Klik `[Clear Field]` pada Filter Panel, klik `[Apply]`
18. Pilih Brand `Honda`, klik `[Apply]`
19. Verifikasi setiap baris yang tampil ber-Brand `Honda`
20. Klik `[Clear Field]` pada Filter Panel, klik `[Apply]`
21. Pilih PIC `Siti Rahma`, klik `[Apply]`
22. Verifikasi setiap baris yang tampil ber-PIC `Siti Rahma`
23. Klik `[Clear Field]` pada Filter Panel, klik `[Apply]`

### TC-GS-NLU-382: Sort 3 tahap kelas teks alfabetis pada Assigned Assets

24. Untuk setiap baris tabel `Kolom sort kelas teks TC-GS-NLU-382` di `## Prerequisites` (langkah 24 sampai 29): klik header kolom pada baris tabel satu kali
25. Verifikasi klik #1: baris terurut ascending A-Z pada kolom tersebut
26. Klik header kolom yang sama untuk kedua kali
27. Verifikasi klik #2: baris terurut descending Z-A pada kolom tersebut
28. Klik header kolom yang sama untuk ketiga kali
29. Verifikasi klik #3: urutan kembali ke default sort tabel (Name A-Z)

### TC-GS-NLU-391: Download Assigned Assets

30. Klik Download > `Download as XLSX`
31. Verifikasi tidak ada toast sukses
32. Verifikasi berkas `Assigned-Assets-Budi-Kurniawan.xlsx` terunduh
33. Verifikasi header berkas tanpa kolom Photo

### TC-GS-NLU-393: Cache Setup Column Borrowed Assets terpisah dari Assigned Assets

34. Klik sub-tab `Borrowed Assets`
35. Klik ikon `⋯` pada header kolom Actions, lalu klik `Setup Column...`
36. Hapus centang kolom `Brand`, klik `[Save]`
37. Klik sub-tab `Assigned Assets`
38. Verifikasi kolom `Brand` di Assigned Assets tetap tampil

## Notes

- Sumber TC: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber diubah: TC-GS-NLU-373 dan TC-GS-NLU-392 (empty state, Detail `Siti Rahayu`) ditaruh paling awal karena memakai Detail yang sama, lalu 381, 382, 391, 393 pada Detail `Budi Kurniawan`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 3 dan 7, 8, 9, 10 (Search nama, membuka Detail, dan memilih sub-tab; R-16); langkah 5 (berpindah ke sub-tab `Assigned Assets` untuk TC-GS-NLU-392); langkah 11 (membuka Filter Panel); langkah 17, 20, 23 (mengosongkan Filter, S-09); langkah 34 (berpindah ke sub-tab `Borrowed Assets`, langkah 1 TC-GS-NLU-393).
- Langkah yang diulang: langkah 24 sampai 29 diulang untuk enam baris tabel `Kolom sort kelas teks TC-GS-NLU-382` di Prerequisites; default sort Assigned Assets adalah Name A-Z.
- Asersi tambahan (konkretisasi Expected): "Setiap filter menyaring baris" (TC-GS-NLU-381 b) ditulis sebagai asersi universal per Filter dengan nilai Name `Mesin Bor`, Brand `Honda`, dan PIC `Siti Rahma` yang dipilih spec, didahului pembanding generik.
- Konfigurasi kolom Borrowed Assets yang disimpan TC-GS-NLU-393 dipulihkan hook `after` dengan menghapus preferensi kolom di browser.
- Pembagian TC lintas spec: Screening, default sort, Search ada di spec 104; Setup Column Assigned Assets ada di spec 106 dan 107; Borrowed Assets ada di spec 099 sampai 103.
- Temuan untuk QA:
  - TC-GS-NLU-381: langkah TC "Pilih Name, Brand, PIC bergantian" tidak menyebut nilai yang dipilih maupun apakah Filter bersifat kumulatif; spec memilih nilai dari data Pre-setup dan mengosongkan Filter di antaranya.
  - TC-GS-NLU-382: PIC bernilai satu (`Siti Rahma`) pada semua transaksi Budi Kurniawan sehingga hasil sort kolom `PIC` tidak punya dua nilai distinct pada halaman teramati; asersi urutan kolom itu tidak dapat membuktikan sort (S-11, S-14). Data transaksi dengan PIC kedua perlu disediakan tim FE atau dikonfirmasi QA.
- Spec melewati sekitar 35 langkah (38 langkah nominal, 68 dengan ekspansi sort enam kolom). Alasan: seluruh blok memakai satu surface (sub-tab Assigned Assets), satu dataset, dan satu kelas harness (fungsional), dan tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); memisahkannya mengulang login dan navigasi Detail.
  - TC-GS-NLU-391: Expected "berkas berisi baris Assigned Assets" adalah isi sel berkas (kelas f); spec mengasersi nama berkas, header tanpa kolom Photo, dan tidak adanya toast sukses. Cara membuka Detail Non-Login User dari daftar tidak dijelaskan TC (hanya "User > Detail"); spec menulis "Buka Detail Non-Login User" tanpa mekanisme klik tertentu.
