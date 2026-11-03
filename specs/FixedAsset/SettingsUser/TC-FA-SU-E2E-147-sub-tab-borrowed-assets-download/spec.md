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

1. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
2. Hover icon Download
3. Verifikasi tooltip `Download`
4. Klik icon Download
5. Verifikasi overlay `Download as CSV` dan `Download as XLSX` tampil
6. Pilih `Download as CSV`
7. Verifikasi tidak ada toast sukses saat unduhan CSV berhasil
8. Verifikasi file `Borrowed-Assets-Budi-Santoso.csv` terunduh
9. Klik icon Download
10. Pilih `Download as XLSX`
11. Verifikasi tidak ada toast sukses saat unduhan XLSX berhasil
12. Verifikasi file `Borrowed-Assets-Budi-Santoso.xlsx` terunduh
13. Buka berkas CSV hasil unduhan
14. Verifikasi CSV berencoding UTF-8 dengan BOM
15. Verifikasi nilai ber-koma, tanda kutip, atau baris baru dibungkus tanda kutip ganda
16. Buka berkas XLSX hasil unduhan
17. Verifikasi XLSX satu sheet bernama `Sheet1`

### TC-FA-SU-436: Cakupan baris dan kolom Download Sub-tab Borrowed Assets: Search, Filter, Sort, dan Column Visibility

18. Klik icon Download
19. Pilih `Download as CSV`
20. Verifikasi berkas CSV memuat seluruh baris (bukan hanya halaman aktif) dalam urutan sort aktif
21. Ketik Search `Kamera`, tekan Enter
22. Klik icon Filter
23. Buka dropdown Name
24. Centang `Kamera DSLR`
25. Klik `[Apply]`
26. Tutup panel Filter dengan klik icon Filter
27. Klik icon Download
28. Pilih `Download as CSV`
29. Verifikasi dengan Search dan Filter aktif, berkas CSV hanya memuat baris yang cocok (`Kamera DSLR`)
30. Klik `(←)` pada kotak Search
31. Klik icon Filter
32. Klik `[Clear Field]`
33. Klik `[Apply]`
34. Tutup panel Filter dengan klik icon Filter
35. Klik header kolom Column Visibility (⋯)
36. Hapus centang Brand pada overlay Column Visibility
37. Tutup overlay Column Visibility dengan Esc
38. Klik icon Download
39. Pilih `Download as CSV`
40. Verifikasi tidak ada toast peringatan saat kolom di-hide
41. Verifikasi kolom Brand yang di-hide tidak ikut berkas CSV
42. Klik header kolom Column Visibility (⋯)
43. Centang kembali Brand pada overlay Column Visibility
44. Tutup overlay Column Visibility dengan Esc
45. Klik icon Download
46. Pilih `Download as CSV`
47. Verifikasi setelah di-unhide kolom Brand ikut kembali dalam berkas CSV
48. Ketik Search `zzzz` (keyword tanpa hasil), tekan Enter
49. Klik icon Download
50. Pilih `Download as CSV`
51. Verifikasi unduhan hasil 0 baris tanpa toast
52. Verifikasi hasil 0 baris tetap dapat diunduh dengan hanya baris header kolom yang visible
53. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Pembagian TC lintas spec: TC-FA-SU-437 (transformasi data Download per tipe kolom) ada di spec 370; TC-FA-SU-438 (Download gagal) ada di spec 366.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Alasan melewati sekitar 35 langkah (53 langkah tertulis, 53 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-435 butir d (BOM UTF-8, pembungkusan tanda kutip ganda, nama sheet) adalah asersi isi berkas (kelas f, bagian 3 prinsip 13) yang ditulis di spec ini; membutuhkan kemampuan baca isi berkas CSV/XLSX yang disediakan tim FE. Pre-setup #24 tidak menyebut nilai ber-koma, bertanda kutip, atau berbaris baru, sehingga pembungkusan hanya dapat diasersi bila data itu ada pada baris Budi Santoso.
  - TC-FA-SU-436: keyword tanpa hasil tidak diberi nilai; spec memakai `zzzz`. Kolom yang di-hide tidak disebut; spec memakai Brand. Cakupan baris dan kolom berkas diasersi lewat kemampuan baca isi berkas (tim FE).
