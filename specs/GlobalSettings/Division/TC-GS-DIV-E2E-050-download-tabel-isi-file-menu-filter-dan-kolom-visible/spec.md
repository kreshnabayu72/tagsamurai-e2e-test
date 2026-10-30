---
id: TC-GS-DIV-E2E-050-download-tabel-isi-file-menu-filter-dan-kolom-visible
title: "Download Tabel Division: Menu, Isi File, Search/Filter Aktif, dan Kolom Visible"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-180
  - TC-GS-DIV-181
  - TC-GS-DIV-182
  - TC-GS-DIV-183
  - TC-GS-DIV-184
  - TC-GS-DIV-185
  - TC-GS-DIV-187
coverage:
  web: automated
---

# Download Tabel Division: Menu, Isi File, Search/Filter Aktif, dan Kolom Visible

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Division.
- Akun: Total Control, `Sari Dewi (Sari D)`, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > Division dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (tetap di environment, hanya dibaca): Finance (FIN), Human Resources (HR), Legal (LGL), Operations (OPS), Compliance (CMP), Treasury (TRS). Last Updated keenam Division ini identik (Tabel Data Uji Pre-setup TC), lebih lama dari hari uji, dan tidak diubah TC mana pun.
- Tanggal pre-setup (`{tanggal pre-setup}`): teks tanggal pada sel Last Updated baris Pre-setup `Compliance` (urutan ke-5 pada sort default Name A-Z, sehingga ada di halaman 1 tabel 32 baris; Last Updated keenam Division Pre-setup identik; format mengikuti Date Format General Settings), dibaca sekali di hook `before` dan dipakai untuk memilih rentang tanggal di Filter Panel.
- Data Dinamis: Population D-02 (26 Division, Name (Code)): Accounting (ACC); Administration (ADM); Audit (AUD); Business Development (BD); Corporate Communication (CCM); Customer Service (CSV); Data Analytics (DA); Engineering (ENG); Facilities (FAC); General Affairs (GA); Information Technology (IT); Internal Control (IC); Logistics (LOG); Marketing (MKT); Procurement (PRC); Product Management (PM); Production (PRD); Quality Assurance (QA); Research and Development (RND); Risk Management (RSK); Sales (SLS); Security (SEC); Strategy (STR); Supply Chain (SC); Training (TRN); Warehouse (WH). Di-seed idempotent lewat kemampuan seeding Division lewat API di hook `before` dengan Name dan Code literal (dilewati bila sudah ada), sehingga tabel memuat 32 baris dan Last Updated Population = hari uji. Nama literal tanpa suffix karena asersi jumlah 32 baris pada berkas dan pemisahan Pre-setup terhadap Population bergantung pada kumpulan nama ini (pengecualian S-12 untuk Population Division: seeding idempotent, cleanup milik spec, suite serial). Cleanup di hook `after` hanya menghapus Division Population yang dibuat spec ini lewat API, tanpa berasumsi seeding berhasil penuh.
- Data uji: format `CSV` (TC-GS-DIV-181, 183, 184, 185, 187) dan `XLSX` (TC-GS-DIV-182); keyword `a` dan rentang pre-setup (TC-GS-DIV-182); kolom `Code` di-hide lalu di-unhide (TC-GS-DIV-183, 184).
- Date Format General Settings `DD/MM/YY` (default environment) dan Time Format default; spec ini tidak mengubah General Settings. Spec 052 mengubah dan memulihkan nilai ini di hook `after`-nya, sehingga suite berjalan serial.
- Kemampuan teknis (kelas binary buffer, prinsip 13f konvensi): menangkap berkas unduhan browser (event download) ke direktori bersih per unduhan supaya nama berkas yang sama (`Division.csv`) tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV dan XLSX (nama kolom, jumlah baris, nilai sel). Berkas unduhan dihapus di hook `after`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan: visibilitas kolom `Code` (dikembalikan tampil di langkah 26), Search dan Filter (dikosongkan di langkah 40 sampai 43); hook `after` sebagai cadangan.
- Hook `beforeEach`: kembali ke layar Global Settings > User > Division.
- Suite berjalan serial (`parallel: false`): tabel harus memuat tepat 32 baris saat spec mulai.

## Test Steps

### TC-GS-DIV-180: Screening menu Download tabel Division

1. Klik icon Download
2. Verifikasi popover menampilkan opsi `Download CSV`
3. Verifikasi popover menampilkan opsi `Download XLSX`

### TC-GS-DIV-181: Download tanpa Search dan Filter mengekspor seluruh baris

4. Klik `Download CSV`
5. Verifikasi tidak ada toast sukses
6. Verifikasi file `Division.csv` terunduh
7. Buka isi file `Division.csv` yang diunduh
8. Verifikasi file memuat seluruh 32 baris data (bukan hanya 10 baris halaman yang tampil)

### TC-GS-DIV-185: Download berhasil tidak menampilkan toast sukses

9. Klik icon Download
10. Klik `Download CSV`
11. Verifikasi tidak ada toast sukses
12. Verifikasi file langsung terunduh

### TC-GS-DIV-187: Isi file ekspor memakai format tanggal General Settings dan nilai kosong tidak ada

13. Buka isi file `Division.csv` hasil unduhan pada langkah 4
14. Verifikasi kolom `Last Updated` memakai format tanggal `DD/MM/YY`
15. Verifikasi kolom `Last Updated` memakai format jam General Settings
16. Verifikasi kolom `Name` dan `Code` terisi pada seluruh baris (tidak ada sel `-`)

### TC-GS-DIV-183: Download hanya mengekspor kolom yang visible

17. Klik header kolom Actions (⋯)
18. Hilangkan centang kolom `Code` pada Overlay Column Visibility
19. Klik icon Download
20. Klik `Download CSV`
21. Verifikasi tidak ada toast atau peringatan partial export
22. Buka isi file hasil unduhan
23. Verifikasi file memuat kolom `Name` dan `Last Updated`
24. Verifikasi kolom `Code` tidak ikut diekspor

### TC-GS-DIV-184: Kolom yang di-unhide kembali ikut diekspor

25. Klik header kolom Actions (⋯)
26. Centang kembali kolom `Code` pada Overlay Column Visibility
27. Klik icon Download
28. Klik `Download CSV`
29. Buka isi file hasil unduhan
30. Verifikasi file memuat kolom `Name`, `Code`, dan `Last Updated`

### TC-GS-DIV-182: Download dengan Search dan Filter aktif hanya mengekspor baris yang cocok

31. Ketik Search `a`, tekan Enter
32. Klik icon Filter
33. Pilih rentang tanggal `{tanggal pre-setup}` sampai `{tanggal pre-setup}` pada field `Last Updated`
34. Klik `[Apply]`
35. Klik icon Download
36. Klik `Download XLSX`
37. Verifikasi file `Division.xlsx` terunduh
38. Buka isi file `Division.xlsx` yang diunduh
39. Verifikasi file hanya memuat baris yang cocok dengan keyword `a` pada Search dan Filter aktif: 6 Division Pre-setup (`Compliance`, `Finance`, `Human Resources`, `Legal`, `Operations`, `Treasury`) tanpa Division Population
40. Klik icon panah `(←)` untuk menutup Search dan mereset tabel
41. Klik icon Filter
42. Klik `[Clear Field]`
43. Klik `[Apply]`

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE. Kelas harness binary buffer (prinsip 13f): isi berkas CSV dan XLSX dipisah dari kegagalan ekspor (spec 051). Dependensi TC-GS-DIV-30 (Population) dipenuhi spec ini lewat seeding di hook `before`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 180, 181, 185, 187 (seluruh data, semua kolom), 183, 184 (kolom visible), lalu 182 (Search dan Filter aktif) di akhir, karena TC-GS-DIV-182 memerlukan Search dan Filter yang harus dibersihkan sesudahnya, sedangkan TC-GS-DIV-183 dan 184 memerlukan tabel tanpa Search dan Filter. Urutan di `tc-division.md`: 180, 181, 182, 183, 184, 185, 187.
- TC-GS-DIV-187 membaca berkas `Division.csv` yang sama dengan unduhan TC-GS-DIV-181 (langkah 4), tanpa unduh ulang: state tabel keduanya identik (tanpa Search dan Filter, semua kolom, 32 baris), sehingga langkah "Download CSV" TC-GS-DIV-187 terpenuhi unduhan itu. TC-GS-DIV-185 melakukan unduhan sendiri (langkah 9 dan 10) karena Expected-nya menyangkut perilaku layar saat klik. Langkah 1 TC-GS-DIV-181 ("Klik icon Download lalu `Download CSV`") memakai popover yang masih terbuka dari TC-GS-DIV-180.
- Langkah 1 TC-GS-DIV-184 ("Hilangkan lalu centang kembali kolom `Code`") dipenuhi state hidden dari TC-GS-DIV-183 sehingga hanya langkah centang kembali (langkah 25 dan 26) yang ditulis; langkah 26 sekaligus memulihkan visibilitas kolom (hook `after` sebagai cadangan).
- Asersi tambahan (konkretisasi Expected): langkah 39 (daftar enam nama Division Pre-setup dan tanpa Division Population untuk "hanya baris yang cocok" TC-GS-DIV-182) adalah turunan dari Population D-02 dan 6 Pre-setup yang lolos keyword `a` serta Filter rentang tanggal Pre-setup.
- Asersi absence atas state sementara (toast sukses, toast atau peringatan partial export) diletakkan segera sesudah klik pilihan format dan sebelum asersi berkas (langkah 5, 11, dan 21); klik pilihan format menjadi anchor positif yang buktinya menyusul pada asersi berkas terunduh (langkah 6, 12, dan 23 sampai 24).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7, 13, 22, 29, dan 38 (membaca isi berkas unduhan) serta langkah 40 sampai 43 (menutup Search dan mengosongkan Filter di akhir spec).
- Spec melewati sekitar 35 langkah (43 langkah) karena tujuh TC Download memakai dataset 32 baris yang sama dan satu kelas harness (binary buffer). Blok 181, 185, 183, 184, dan 182 mengunduh berkas sendiri; blok 181 meneruskan popover dari blok 180; blok 187 membaca berkas hasil unduhan blok 181 (langkah 4); blok 184 memakai state kolom hidden hasil blok 183. Langkah membaca isi berkas termasuk blok baca berpola.
- Pembagian TC lintas spec: TC-GS-DIV-186 (Download tabel gagal) dan TC-GS-DIV-223 (Download Changelog gagal) ada di spec 051; TC-GS-DIV-221 dan 222 (isi berkas Download Changelog) ada di spec 063; TC-GS-DIV-151 dan 212 (format tanggal pada Filter dan Changelog) ada di spec 052.
- Temuan untuk QA:
  - TC-GS-DIV-187: TC tidak menyebut Time Format General Settings; spec mengasersi format jam mengikuti General Settings tanpa pola jam tertentu. TC juga tidak menyebut format tanggal di dalam CSV selain `DD/MM/YY` (default).
  - TC-GS-DIV-181, 182, 183, 184, 185: TC tidak menyebut cara menangkap berkas unduhan dan membaca isinya; kemampuan tersebut disediakan tim FE (Prerequisites). TC-GS-DIV-182 tidak menyebut nama kolom berkas XLSX; spec mengasersi baris yang dimuat.
  - TC-GS-DIV-182: tanggal pre-setup tidak disebut konkret di TC; spec membacanya dari sel Last Updated baris `Compliance` (halaman 1) karena keenam Division Pre-setup berbagi tanggal yang sama (Tabel Data Uji Pre-setup TC).
