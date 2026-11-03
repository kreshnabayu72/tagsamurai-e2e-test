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
  | `999` |
  | `abc` |
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-434: Pagination Sub-tab Borrowed Assets: page size, navigasi, dan kasus tepi

1. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
2. Verifikasi default 10 baris per halaman
3. Buka dropdown page size
4. Verifikasi pilihan page size 10, 25, 50, 100 tanpa opsi All
5. Tutup dropdown page size dengan Esc
6. Untuk setiap baris tabel "Nomor halaman tidak valid" di Prerequisites (langkah 6 sampai 7): isi nomor halaman pada baris tabel lalu tekan Enter
7. Verifikasi nomor halaman diabaikan dan tabel tetap di halaman 1
8. Ganti page size ke 25
9. Ganti page size ke 10
10. Verifikasi mengganti page size tetap menampilkan halaman 1
11. Klik header kolom Name satu kali
12. Verifikasi mengganti sort tetap menampilkan halaman 1
13. Klik header kolom Name dua kali lagi sampai kembali netral
14. Ketik Search `Kamera`, tekan Enter
15. Verifikasi Search yang mengubah hasil tetap menampilkan halaman 1
16. Klik `(←)` pada kotak Search

### TC-FA-SU-439: Tooltip icon Table Tools dan header Actions Sub-tab Borrowed Assets

17. Hover icon Search
18. Verifikasi tooltip `Search`
19. Hover icon Filter
20. Verifikasi tooltip `Filter`
21. Hover icon Download
22. Verifikasi tooltip `Download`
23. Hover header kolom Actions (⋯)
24. Verifikasi tooltip `Column Visibility`

### TC-FA-SU-441: State Sub-tab Borrowed Assets dipertahankan per sub-tab

25. Ketik Search `Kamera`, tekan Enter
26. Klik icon Filter
27. Buka dropdown Brand
28. Centang `Canon`
29. Klik `[Apply]`
30. Klik header kolom Name satu kali
31. Ganti page size ke 25
32. Klik Sub-tab Assigned Assets
33. Verifikasi Sub-tab Assigned Assets tidak memuat Search, Filter, Sort, dan page size dari Sub-tab Borrowed Assets
34. Klik satu header kolom sortable pada Sub-tab Assigned Assets
35. Klik Sub-tab Borrowed Assets
36. Verifikasi state Sub-tab Borrowed Assets dipulihkan setelah pindah sub-tab: Search `Kamera`, Filter Brand `Canon`, Sort Name, dan page size 25
37. Klik Sub-tab Assigned Assets
38. Verifikasi sort Sub-tab Assigned Assets tetap sesuai header yang diklik dan tidak terpengaruh state Sub-tab Borrowed Assets
39. Klik Sub-tab Borrowed Assets
40. Klik Back breadcrumb ke User List
41. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
42. Verifikasi state Sub-tab Borrowed Assets dipulihkan setelah Back breadcrumb: Search, Filter, Sort, dan page size 25
43. Tekan F5
44. Verifikasi state Sub-tab Borrowed Assets dipulihkan setelah refresh F5: Search, Filter, Sort, dan page size 25
45. Klik menu Settings > User pada sidebar
46. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
47. Verifikasi state Sub-tab Borrowed Assets kembali ke default setelah keluar lewat menu sidebar

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Pembagian TC lintas spec: TC-FA-SU-440 (empty state, hasil pencarian kosong, loading, dan error load Sub-tab Borrowed Assets) ada di spec 360.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Rentang langkah 6 sampai 7 diulang untuk tiga nilai pada tabel "Nomor halaman tidak valid" (Prerequisites).
- Alasan melewati sekitar 35 langkah (47 langkah tertulis, 51 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-434 butir b menyebut nomor halaman negatif, sedangkan Data Uji langkah 3 hanya `0`, `999`, dan `abc`; spec mengikuti langkah. Butir e adalah catatan fixture satu halaman dan tidak diasersi (rujukan TC-FA-SU-359 dan TC-FA-SU-1057).
  - TC-FA-SU-441: "sub-tab lain" dan header yang diklik di sana tidak disebut TC; spec memakai Sub-tab Assigned Assets dan satu header kolom sortable. Nilai Search, Filter, dan Sort Sub-tab Borrowed Assets dipilih penulis karena Data Uji kosong. Nomor halaman aktif tidak diuji (fixture satu halaman, sesuai TC).
