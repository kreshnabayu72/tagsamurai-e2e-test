---
id: TC-FA-SU-E2E-147-sub-tab-borrowed-assets-download
title: "Sub-tab Borrowed Assets: Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-435
  - TC-FA-SU-436
coverage:
  web: automated
---

# Sub-tab Borrowed Assets: Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Responsibilities (#24). Pengguna target: Budi Santoso dengan 5 baris Borrowed Assets: `Laptop - 1`, `Laptop - 2` (Transaction ID `BRW-20260610`, PIC `Ahmad D`), `Kamera DSLR` (Brand `Canon`), `Proyektor Portable` (Asset ID `AST-01011`), dan `Kendaraan Operasional` (Model / Type `Vario 125`); nilai kolom lain tiap baris mengikuti Pre-setup #24. Kelima baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.
- Kemampuan teknis: browser mengunduh berkas ke folder uji; pembacaan isi berkas CSV dan XLSX (BOM, pembungkus tanda kutip, nama sheet, baris, dan kolom) disediakan tim FE. Folder unduhan dibersihkan di hook `after`.

## Test Steps

### TC-FA-SU-435: Download Sub-tab Borrowed Assets: format CSV dan XLSX, nama file, dan tanpa toast sukses

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
3. Hover icon Download
4. Verifikasi tooltip `Download`
5. Klik icon Download
6. Verifikasi overlay `Download as CSV` dan `Download as XLSX` tampil
7. Pilih `Download as CSV`
8. Verifikasi tidak ada toast sukses saat unduhan CSV berhasil
9. Verifikasi file `Borrowed-Assets-Budi-Santoso.csv` terunduh
10. Klik icon Download
11. Pilih `Download as XLSX`
12. Verifikasi tidak ada toast sukses saat unduhan XLSX berhasil
13. Verifikasi file `Borrowed-Assets-Budi-Santoso.xlsx` terunduh
14. Buka berkas CSV hasil unduhan
15. Verifikasi CSV berencoding UTF-8 dengan BOM
16. Verifikasi nilai ber-koma, tanda kutip, atau baris baru dibungkus tanda kutip ganda
17. Buka berkas XLSX hasil unduhan
18. Verifikasi XLSX satu sheet bernama `Sheet1`

### TC-FA-SU-436: Cakupan baris dan kolom Download Sub-tab Borrowed Assets: Search, Filter, Sort, dan Column Visibility

19. Klik icon Download
20. Pilih `Download as CSV`
21. Verifikasi berkas CSV memuat seluruh baris (bukan hanya halaman aktif) dalam urutan sort aktif
22. Ketik Search `Kamera`, tekan Enter
23. Klik icon Filter
24. Buka dropdown Name
25. Centang `Kamera DSLR`
26. Klik `[Apply]`
27. Tutup panel Filter dengan klik icon Filter
28. Klik icon Download
29. Pilih `Download as CSV`
30. Verifikasi dengan Search dan Filter aktif, berkas CSV hanya memuat baris yang cocok (`Kamera DSLR`)
31. Klik `(←)` pada kotak Search
32. Klik icon Filter
33. Klik `[Clear Field]`
34. Klik `[Apply]`
35. Tutup panel Filter dengan klik icon Filter
36. Klik header kolom Column Visibility (⋯)
37. Hapus centang Brand pada overlay Column Visibility
38. Tutup overlay Column Visibility dengan Esc
39. Klik icon Download
40. Pilih `Download as CSV`
41. Verifikasi tidak ada toast peringatan saat kolom di-hide
42. Verifikasi kolom Brand yang di-hide tidak ikut berkas CSV
43. Klik header kolom Column Visibility (⋯)
44. Centang kembali Brand pada overlay Column Visibility
45. Tutup overlay Column Visibility dengan Esc
46. Klik icon Download
47. Pilih `Download as CSV`
48. Verifikasi setelah di-unhide kolom Brand ikut kembali dalam berkas CSV
49. Ketik Search `zzzz` (keyword tanpa hasil), tekan Enter
50. Klik icon Download
51. Pilih `Download as CSV`
52. Verifikasi unduhan hasil 0 baris tanpa toast
53. Verifikasi hasil 0 baris tetap dapat diunduh dengan hanya baris header kolom yang visible
54. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Pembagian TC lintas spec: TC-FA-SU-437 (transformasi data Download per tipe kolom) ada di spec 370; TC-FA-SU-438 (Download gagal) ada di spec 366.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Langkah penghubung (S-03, R-16): sebelum Detail pengguna dibuka, kotak Search User List diisi nama persis `Budi Santoso` (nama Pre-setup) karena User List memuat 25 pengguna pada 3 halaman dan posisi baris tidak diandalkan (R-23, 8b.13); langkah itu hanya menyaring baris target dan tidak diverifikasi.
- Alasan melewati sekitar 35 langkah (54 langkah tertulis, 54 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-435 butir d (BOM UTF-8, pembungkusan tanda kutip ganda, nama sheet) adalah asersi isi berkas (kelas f, bagian 3 prinsip 13) yang ditulis di spec ini; membutuhkan kemampuan baca isi berkas CSV/XLSX yang disediakan tim FE. Pre-setup #24 tidak menyebut nilai ber-koma, bertanda kutip, atau berbaris baru, sehingga pembungkusan hanya dapat diasersi bila data itu ada pada baris Budi Santoso.
  - TC-FA-SU-436: keyword tanpa hasil tidak diberi nilai; spec memakai `zzzz`. Kolom yang di-hide tidak disebut; spec memakai Brand. Cakupan baris dan kolom berkas diasersi lewat kemampuan baca isi berkas (tim FE).
