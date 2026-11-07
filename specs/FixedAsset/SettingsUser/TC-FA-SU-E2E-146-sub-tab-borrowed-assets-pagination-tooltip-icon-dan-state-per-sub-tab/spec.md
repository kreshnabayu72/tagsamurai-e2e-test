---
id: TC-FA-SU-E2E-146-sub-tab-borrowed-assets-pagination-tooltip-icon-dan-state-per-sub-tab
title: "Sub-tab Borrowed Assets: Pagination, Tooltip Icon, dan State per Sub-tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-434
  - TC-FA-SU-439
  - TC-FA-SU-441
coverage:
  web: automated
---

# Sub-tab Borrowed Assets: Pagination, Tooltip Icon, dan State per Sub-tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Responsibilities (#24). Pengguna target: Budi Santoso dengan 5 baris Borrowed Assets: `Laptop - 1`, `Laptop - 2` (Transaction ID `BRW-20260610`, PIC `Ahmad D`), `Kamera DSLR` (Brand `Canon`), `Proyektor Portable` (Asset ID `AST-01011`), dan `Kendaraan Operasional` (Model / Type `Vario 125`); nilai kolom lain tiap baris mengikuti Pre-setup #24. Kelima baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Tabel "Nomor halaman tidak valid" (satu nilai per iterasi langkah berulang):

  | Nilai |
  |---|
  | `0` |
  | `-1` |
  | `999` |
  | `abc` |
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-434: Pagination Sub-tab Borrowed Assets: page size, navigasi, dan kasus tepi

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
3. Verifikasi default 10 baris per halaman
4. Buka dropdown page size
5. Verifikasi pilihan page size 10, 25, 50, 100 tanpa opsi All
6. Tutup dropdown page size dengan Esc
7. Untuk setiap baris tabel "Nomor halaman tidak valid" di Prerequisites (langkah 7 sampai 8): isi nomor halaman pada baris tabel lalu tekan Enter
8. Verifikasi nomor halaman diabaikan dan tabel tetap di halaman 1
9. Ganti page size ke 25
10. Ganti page size ke 10
11. Verifikasi mengganti page size tetap menampilkan halaman 1
12. Klik header kolom Name satu kali
13. Verifikasi mengganti sort tetap menampilkan halaman 1
14. Klik header kolom Name dua kali lagi sampai kembali netral
15. Ketik Search `Kamera`, tekan Enter
16. Verifikasi Search yang mengubah hasil tetap menampilkan halaman 1
17. Klik `(←)` pada kotak Search

### TC-FA-SU-439: Tooltip icon Table Tools dan header Actions Sub-tab Borrowed Assets

18. Hover icon Search
19. Verifikasi tooltip `Search`
20. Hover icon Filter
21. Verifikasi tooltip `Filter`
22. Hover icon Download
23. Verifikasi tooltip `Download`
24. Hover header kolom Actions (⋯)
25. Verifikasi tooltip `Column Visibility`

### TC-FA-SU-441: State Sub-tab Borrowed Assets dipertahankan per sub-tab

26. Ketik Search `Kamera`, tekan Enter
27. Klik icon Filter
28. Buka dropdown Brand
29. Centang `Canon`
30. Klik `[Apply]`
31. Klik header kolom Name satu kali
32. Ganti page size ke 25
33. Klik Sub-tab Assigned Assets
34. Verifikasi Sub-tab Assigned Assets tidak memuat Search, Filter, Sort, dan page size dari Sub-tab Borrowed Assets
35. Klik satu header kolom sortable pada Sub-tab Assigned Assets
36. Klik Sub-tab Borrowed Assets
37. Verifikasi state Sub-tab Borrowed Assets dipulihkan setelah pindah sub-tab: Search `Kamera`, Filter Brand `Canon`, Sort Name, dan page size 25
38. Klik Sub-tab Assigned Assets
39. Verifikasi sort Sub-tab Assigned Assets tetap sesuai header yang diklik dan tidak terpengaruh state Sub-tab Borrowed Assets
40. Klik Sub-tab Borrowed Assets
41. Klik Back breadcrumb ke User List
42. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
43. Verifikasi state Sub-tab Borrowed Assets dipulihkan setelah Back breadcrumb: Search, Filter, Sort, dan page size 25
44. Tekan F5
45. Verifikasi state Sub-tab Borrowed Assets dipulihkan setelah refresh F5: Search, Filter, Sort, dan page size 25
46. Klik menu Settings > User pada sidebar
47. Ketik Search `Budi Santoso`, tekan Enter
48. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
49. Verifikasi state Sub-tab Borrowed Assets kembali ke default setelah keluar lewat menu sidebar

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Pembagian TC lintas spec: TC-FA-SU-440 (empty state, hasil pencarian kosong, loading, dan error load Sub-tab Borrowed Assets) ada di spec 360.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Langkah penghubung (S-03, R-16): sebelum Detail pengguna dibuka, kotak Search User List diisi nama persis `Budi Santoso` (nama Pre-setup) karena User List memuat 25 pengguna pada 3 halaman dan posisi baris tidak diandalkan (R-23, 8b.13); langkah itu hanya menyaring baris target dan tidak diverifikasi. Sesudah Back breadcrumb kotak Search mempertahankan nilainya (8b.9), sehingga isinya diganti dengan nama persis yang sama (langkah 42, "ganti isi kotak search") sebelum Detail dibuka ulang; sesudah pindah lewat menu sidebar Search diketik ulang (langkah 47).
- Rentang langkah 7 sampai 8 diulang untuk empat nilai pada tabel "Nomor halaman tidak valid" (Prerequisites).
- Alasan melewati sekitar 35 langkah (49 langkah tertulis, 55 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-434 butir e adalah catatan fixture satu halaman dan tidak diasersi (rujukan TC-FA-SU-359 dan TC-FA-SU-1057).
  - TC-FA-SU-441: "sub-tab lain" dan header yang diklik di sana tidak disebut TC; spec memakai Sub-tab Assigned Assets dan satu header kolom sortable. Nilai Search, Filter, dan Sort Sub-tab Borrowed Assets dipilih penulis karena Data Uji kosong. Nomor halaman aktif tidak diuji (fixture satu halaman, sesuai TC).
