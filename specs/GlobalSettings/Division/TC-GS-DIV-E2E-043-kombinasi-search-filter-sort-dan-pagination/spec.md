---
id: TC-GS-DIV-E2E-043-kombinasi-search-filter-sort-dan-pagination
title: "Kombinasi Search, Filter, Sort, dan Pagination Tabel Division"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-153
  - TC-GS-DIV-154
  - TC-GS-DIV-155
  - TC-GS-DIV-156
  - TC-GS-DIV-157
  - TC-GS-DIV-158
  - TC-GS-DIV-159
coverage:
  web: automated
---

# Kombinasi Search, Filter, Sort, dan Pagination Tabel Division

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Division.
- Akun: Total Control, `Sari Dewi (Sari D)`, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > Division dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (tetap di environment, hanya dibaca): Finance (FIN), Human Resources (HR), Legal (LGL), Operations (OPS), Compliance (CMP), Treasury (TRS). Last Updated keenam Division ini identik, lebih lama dari hari uji, dan tidak diubah TC mana pun (Tabel Data Uji Pre-setup TC).
- Tanggal pre-setup (`{tanggal pre-setup}`): teks tanggal pada sel Last Updated baris Pre-setup `Compliance` (urutan ke-5 pada sort default Name A-Z, sehingga ada di halaman 1 tabel 32 baris; Last Updated keenam Division Pre-setup identik; format mengikuti Date Format General Settings), dibaca sekali di hook `before` dan dipakai untuk memilih rentang tanggal di Filter Panel.
- Data Dinamis: Population D-02 (26 Division, Name (Code)): Accounting (ACC); Administration (ADM); Audit (AUD); Business Development (BD); Corporate Communication (CCM); Customer Service (CSV); Data Analytics (DA); Engineering (ENG); Facilities (FAC); General Affairs (GA); Information Technology (IT); Internal Control (IC); Logistics (LOG); Marketing (MKT); Procurement (PRC); Product Management (PM); Production (PRD); Quality Assurance (QA); Research and Development (RND); Risk Management (RSK); Sales (SLS); Security (SEC); Strategy (STR); Supply Chain (SC); Training (TRN); Warehouse (WH). Di-seed idempotent lewat kemampuan seeding Division lewat API di hook `before` dengan Name dan Code literal (dilewati bila sudah ada), sehingga tabel memuat 32 baris dan Last Updated Population = hari uji. Nama literal tanpa suffix karena asersi irisan (`Human Resources` sebagai satu-satunya hasil, `Facilities` dan `Sales` tersaring keluar) bergantung pada kumpulan nama ini (bagian 5 konvensi, S-12). Cleanup di hook `after` hanya menghapus Division Population yang dibuat spec ini lewat API, tanpa berasumsi seeding berhasil penuh.
- Data uji per TC: keyword `es` (TC-GS-DIV-153, 154) dan `a` (TC-GS-DIV-155 sampai 159); rentang pre-setup `{tanggal pre-setup}` sampai `{tanggal pre-setup}`; rentang kosong 1 Januari 2020 sampai 31 Januari 2020 (TC-GS-DIV-159); page size 25 (TC-GS-DIV-155); sort Name descending.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan: Search, Filter, sort, dan page size dikembalikan ke default (Search kosong dan tertutup, Filter kosong, sort default Name A-Z, page size 10) di akhir spec; hook `after` sebagai cadangan.
- Hook `beforeEach`: kembali ke layar Global Settings > User > Division.
- Suite berjalan serial (`parallel: false`): tabel harus memuat tepat 32 baris saat spec mulai.
- Kemampuan teknis: memilih rentang tanggal pada date range picker Filter Panel; membaca teks sel Last Updated.

## Test Steps

### TC-GS-DIV-153: Search lalu Filter menghasilkan irisan keduanya

1. Ketik Search `es`, tekan Enter
2. Klik icon Filter
3. Pilih rentang tanggal `{tanggal pre-setup}` sampai `{tanggal pre-setup}` pada field `Last Updated`
4. Klik `[Apply]`
5. Verifikasi tabel hanya menampilkan baris `Human Resources`
6. Verifikasi Division Population `Facilities` dan `Sales` tersaring keluar
7. Verifikasi keyword `es` tidak tereset setelah Apply (input Search tetap `es`)

### TC-GS-DIV-154: Filter lalu Search menghasilkan irisan keduanya

8. Klik icon `(✕)` pada input Search
9. Tekan Enter pada input kosong
10. Ketik Search `es`, tekan Enter
11. Verifikasi hasil identik dengan Search lalu Filter: hanya baris `Human Resources` tampil
12. Verifikasi kriteria filter tetap aktif saat Search dijalankan (`Facilities` dan `Sales` tidak tampil)

### TC-GS-DIV-155: Kombinasi Search, Filter, Sort, dan Pagination bersamaan

13. Ganti isi kotak search dengan `a`, tekan Enter
14. Klik header Name (ascending)
15. Klik header Name (descending)
16. Ubah page size ke 25
17. Verifikasi 6 Division Pre-setup terurut Name Z-A: `Treasury`, `Operations`, `Legal`, `Human Resources`, `Finance`, `Compliance`
18. Verifikasi page size 25 terpilih
19. Verifikasi keyword `a` tetap aktif pada input Search

### TC-GS-DIV-156: Clear Filter saat Search dan Sort aktif mempertahankan Search dan Sort

20. Klik icon Filter
21. Klik `[Clear Field]`
22. Klik `[Apply]`
23. Verifikasi keyword `a` tetap aktif pada input Search
24. Verifikasi sort Name descending tetap aktif (baris pertama `Warehouse`)

### TC-GS-DIV-157: Clear Search saat Filter dan Sort aktif mempertahankan Filter dan Sort

25. Klik icon Filter
26. Pilih rentang tanggal `{tanggal pre-setup}` sampai `{tanggal pre-setup}` pada field `Last Updated`
27. Klik `[Apply]`
28. Klik icon `(✕)` pada input Search
29. Tekan Enter pada input kosong
30. Verifikasi Filter rentang tanggal tetap aktif (tabel hanya menampilkan 6 Division Pre-setup)
31. Verifikasi sort Name descending tetap aktif (urutan `Treasury`, `Operations`, `Legal`, `Human Resources`, `Finance`, `Compliance`)

### TC-GS-DIV-158: Ganti kolom sort saat Search dan Filter aktif tidak mereset saringan

32. Ketik Search `a`, tekan Enter
33. Klik header Name (kembali ke sort default dari descending)
34. Klik header Name (ascending)
35. Klik header Code
36. Verifikasi sort berpindah ke kolom Code ascending: `Compliance` (CMP), `Finance` (FIN), `Human Resources` (HR), `Legal` (LGL), `Operations` (OPS), `Treasury` (TRS)
37. Verifikasi ikon sort kolom Name kembali netral
38. Verifikasi kotak search tetap berisi `a`
39. Verifikasi Filter tetap aktif (tabel hanya menampilkan 6 Division Pre-setup)

### TC-GS-DIV-159: Empty state hasil kombinasi pulih saat salah satu saringan dilepas

40. Klik icon Filter
41. Pilih rentang tanggal 1 Januari 2020 sampai 31 Januari 2020 pada field `Last Updated`
42. Klik `[Apply]`
43. Verifikasi tabel menampilkan `No results found`
44. Verifikasi tabel menampilkan `Try adjusting your search or filter.`
45. Klik icon Filter
46. Klik `[Clear Field]`
47. Klik `[Apply]`
48. Verifikasi tabel pulih menampilkan hasil pencarian `a` (Division yang Name atau Code-nya memuat `a`)
49. Verifikasi hasil pencarian `a` memuat Division Population
50. Verifikasi kotak search tetap berisi `a`
51. Klik icon `(✕)` pada input Search
52. Tekan Enter pada input kosong
53. Klik header Code (descending)
54. Klik header Code (kembali ke sort default)
55. Ubah page size ke 10

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE. Dependensi TC-GS-DIV-30 (Population) dipenuhi spec ini lewat seeding di hook `before`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (153 sampai 159) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 33 (kembali ke sort default dari Name descending sebelum TC-GS-DIV-158 mengklik Name lalu Code) dan langkah 51 sampai 55 (mengosongkan Search dan mengembalikan sort Code serta page size 10 di akhir spec; Filter sudah dikosongkan pada langkah 45 sampai 47).
- Prasyarat TC-GS-DIV-154 sampai 159 yang berantai (TC-GS-DIV-153 dan TC-GS-DIV-155) dipenuhi dengan menjalankan TC dependensi di dalam spec ini dan memakai state akhirnya: langkah 1 TC-GS-DIV-154 (Filter rentang pre-setup) dipenuhi state akhir TC-GS-DIV-153 setelah Search dikosongkan (langkah 8 dan 9); langkah 1 dan 2 TC-GS-DIV-155 ("Cari `a`", Filter) dipenuhi langkah 13 serta Filter yang masih aktif; langkah 1 dan 2 TC-GS-DIV-156 dipenuhi state akhir TC-GS-DIV-155; langkah 2 TC-GS-DIV-157 ("Cari `a`, klik header Name descending") dipenuhi state akhir TC-GS-DIV-156 (keyword `a` dan sort Name descending masih aktif); langkah 1 TC-GS-DIV-158 memakai Filter yang masih aktif dari TC-GS-DIV-157; langkah 1 TC-GS-DIV-159 ("Cari `a`") dipenuhi langkah 32. Search bar tetap terbuka sejak langkah 1; Search memakai langkah atomik "Ketik Search" (langkah 1, 10, dan 32) dan "ganti isi kotak search dengan" bila input berisi (langkah 13) (bagian 8b butir 9).
- Spec melewati sekitar 35 langkah (55 langkah) karena tujuh TC kombinasi satu kelas harness (fungsional) berbagi dataset 32 baris yang sama dan saling berantai lewat state Search, Filter, dan Sort; memisahkannya mengulang login, seeding, dan pembuatan state kombinasi yang sama, sehingga tetap satu spec.
- Pembagian TC lintas spec: TC-GS-DIV-141 sampai 148 (Search toolbar) ada di spec 041; TC-GS-DIV-149, 150, 152, 169 (Filter Panel) ada di spec 042; TC-GS-DIV-163 sampai 165 (Sort) ada di spec 045; TC-GS-DIV-166 sampai 168, 170 (Pagination) ada di spec 046.
- Asersi tambahan (konkretisasi Expected): langkah 24 (baris pertama `Warehouse` untuk "sort tetap aktif" TC-GS-DIV-156), langkah 30 dan 39 (tabel hanya menampilkan 6 Division Pre-setup untuk "Filter tetap aktif" TC-GS-DIV-157 dan 158), dan langkah 31 dan 36 (urutan Name Z-A dan Code A-Z dari 6 Pre-setup untuk "sort tetap aktif" dan "sort berpindah" TC-GS-DIV-157 dan 158); semuanya turunan dari 6 Pre-setup yang lolos Filter rentang tanggal Pre-setup dan keyword `a`.
- Temuan untuk QA:
  - TC-GS-DIV-153 sampai 159: tanggal pre-setup tidak disebut konkret; spec membacanya dari sel Last Updated baris `Compliance` halaman 1 (Last Updated keenam Division Pre-setup identik menurut Tabel Data Uji Pre-setup TC).
  - TC-GS-DIV-155 Expected b ("Tidak ada kontrol yang menimpa kontrol lain") adalah kesimpulan dari Expected a; diasersi lewat langkah 18 dan 19 (page size dan keyword tetap) bersama urutan pada langkah 17.
  - TC-GS-DIV-158: TC tidak menyatakan state sort awal; spec mengembalikan sort ke default lebih dulu (langkah 33) supaya klik Name berikutnya menghasilkan ascending seperti langkah TC.
  - TC-GS-DIV-159: TC menulis rentang `01-01-2020` sampai `31-01-2020`; spec memilih tanggal tersebut di date range picker tanpa mengasumsikan format teks input.
