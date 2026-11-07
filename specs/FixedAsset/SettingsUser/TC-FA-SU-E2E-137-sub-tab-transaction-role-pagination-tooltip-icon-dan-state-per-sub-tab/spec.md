---
id: TC-FA-SU-E2E-137-sub-tab-transaction-role-pagination-tooltip-icon-dan-state-per-sub-tab
title: "Sub-tab Transaction Role: Pagination, Tooltip Icon, dan State per Sub-tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-404
  - TC-FA-SU-405
  - TC-FA-SU-407
coverage:
  web: automated
---

# Sub-tab Transaction Role: Pagination, Tooltip Icon, dan State per Sub-tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Role (#39). Pengguna target: Yuda Pratama dengan 7 baris Transaction Role: `Borrowing & Assignment - Approver` pada IT Infrastructure; `Damaged - Monitoring & Report` pada Branch Surabaya; `Disposal - Approver` pada All Groups; `Disposal - Staff` pada Logistics Warehouse; `Missing - Approver` pada Branch Surabaya, General Affairs, dan Logistics Warehouse; `Transfer - Asset Admin` pada Finance & Accounting dan IT Infrastructure; `Transfer - Monitoring & Report` pada Branch Surabaya. Ketujuh baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Tabel "Nomor halaman tidak valid" (satu nilai per iterasi langkah berulang):

  | Nilai |
  |---|
  | `0` |
  | `-1` |
  | `999` |
  | `abc` |
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-404: Pagination Sub-tab Transaction Role: page size, navigasi, dan kasus tepi

1. Ketik Search `Yuda Pratama`, tekan Enter
2. Buka Detail Yuda Pratama > Tab Role > Sub-tab Transaction Role
3. Verifikasi default 10 baris per halaman
4. Buka dropdown page size
5. Verifikasi pilihan page size 10, 25, 50, 100 tanpa opsi All
6. Tutup dropdown page size dengan Esc
7. Untuk setiap baris tabel "Nomor halaman tidak valid" di Prerequisites (langkah 7 sampai 8): isi nomor halaman pada baris tabel lalu tekan Enter
8. Verifikasi nomor halaman diabaikan dan tabel tetap di halaman 1
9. Ganti page size ke 25
10. Ganti page size ke 10
11. Verifikasi mengganti page size tetap menampilkan halaman 1
12. Klik header kolom Transaction satu kali
13. Verifikasi mengganti sort tetap menampilkan halaman 1
14. Klik header kolom Transaction dua kali lagi sampai kembali netral
15. Ketik Search `Transfer`, tekan Enter
16. Verifikasi Search yang mengubah hasil tetap menampilkan halaman 1
17. Klik `(←)` pada kotak Search

### TC-FA-SU-405: Tooltip icon Table Tools dan header Actions Sub-tab Transaction Role

18. Hover icon Search
19. Verifikasi tooltip `Search`
20. Hover icon Filter
21. Verifikasi tooltip `Filter`
22. Hover icon Changelog
23. Verifikasi tooltip `Changelog`
24. Hover header kolom Actions (⋯)
25. Verifikasi tooltip `Column Visibility`

### TC-FA-SU-407: State Sub-tab Transaction Role dipertahankan per sub-tab

26. Ketik Search `Transfer`, tekan Enter
27. Klik icon Filter
28. Buka dropdown Role
29. Centang `Asset Admin`
30. Klik `[Apply]`
31. Klik header kolom Group satu kali
32. Ganti page size ke 25
33. Klik Sub-tab Group Role
34. Verifikasi Sub-tab Group Role tidak memuat Search, Filter, Sort, dan page size dari Sub-tab Transaction Role
35. Klik satu header kolom sortable pada Sub-tab Group Role
36. Klik Sub-tab Transaction Role
37. Verifikasi state Sub-tab Transaction Role dipulihkan setelah pindah sub-tab: Search `Transfer`, Filter Role `Asset Admin`, Sort Group, dan page size 25
38. Klik Sub-tab Group Role
39. Verifikasi sort Sub-tab Group Role tetap sesuai header yang diklik dan tidak terpengaruh state Sub-tab Transaction Role
40. Klik Sub-tab Transaction Role
41. Klik Back breadcrumb ke User List
42. Ganti isi kotak search dengan `Yuda Pratama`, tekan Enter
43. Buka Detail Yuda Pratama > Tab Role > Sub-tab Transaction Role
44. Verifikasi state Sub-tab Transaction Role dipulihkan setelah Back breadcrumb: Search, Filter, Sort, dan page size 25
45. Tekan F5
46. Verifikasi state Sub-tab Transaction Role dipulihkan setelah refresh F5: Search, Filter, Sort, dan page size 25
47. Klik menu Settings > User pada sidebar
48. Ketik Search `Yuda Pratama`, tekan Enter
49. Buka Detail Yuda Pratama > Tab Role > Sub-tab Transaction Role
50. Verifikasi state Sub-tab Transaction Role kembali ke default setelah keluar lewat menu sidebar

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Pembagian TC lintas spec: TC-FA-SU-406 (empty state, hasil pencarian kosong, loading, dan error load Sub-tab Transaction Role) ada di spec 360.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Langkah penghubung Search (S-03, R-16): langkah 1 dan 48 (Ketik Search `Yuda Pratama`, tekan Enter) serta langkah 42 (ganti isi kotak search, karena kotak Search mempertahankan nilainya sesudah Back breadcrumb, 8b.9) untuk menemukan baris Yuda Pratama di User List 25 pengguna (3 halaman) sebelum membuka Detail.
- Rentang langkah 7 sampai 8 diulang untuk empat nilai pada tabel "Nomor halaman tidak valid" (Prerequisites).
- Alasan melewati sekitar 35 langkah (50 langkah tertulis, 56 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-404 Langkah Uji 3 dan Data Uji memuat `0`, `-1`, `999`, dan `abc`; spec memakai keempatnya. Butir e adalah catatan fixture satu halaman dan tidak diasersi (rujukan TC-FA-SU-359 dan TC-FA-SU-1057).
  - TC-FA-SU-407: "sub-tab lain" dan header yang diklik di sana tidak disebut TC; spec memakai Sub-tab Group Role dan satu header kolom sortable. Nilai Search, Filter, dan Sort Sub-tab Transaction Role dipilih penulis karena Data Uji kosong. Nomor halaman aktif tidak diuji (fixture satu halaman, sesuai TC).
