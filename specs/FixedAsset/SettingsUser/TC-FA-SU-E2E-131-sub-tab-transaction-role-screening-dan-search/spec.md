---
id: TC-FA-SU-E2E-131-sub-tab-transaction-role-screening-dan-search
title: "Sub-tab Transaction Role: Screening dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-383
  - TC-FA-SU-384
  - TC-FA-SU-385
  - TC-FA-SU-386
coverage:
  web: automated
---

# Sub-tab Transaction Role: Screening dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Role (#39). Pengguna target: Yuda Pratama dengan 7 baris Transaction Role: `Borrowing & Assignment - Approver` pada IT Infrastructure; `Damaged - Monitoring & Report` pada Branch Surabaya; `Disposal - Approver` pada All Groups; `Disposal - Staff` pada Logistics Warehouse; `Missing - Approver` pada Branch Surabaya, General Affairs, dan Logistics Warehouse; `Transfer - Asset Admin` pada Finance & Accounting dan IT Infrastructure; `Transfer - Monitoring & Report` pada Branch Surabaya. Ketujuh baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-383: Screening Sub-tab Transaction Role: Table Tools, kolom, dan default sort

1. Ketik Search `Yuda Pratama`, tekan Enter
2. Buka Detail Yuda Pratama > Tab Role > Sub-tab Transaction Role
3. Verifikasi Table Tools `Search | Filter | [+ Assign] | Changelog` tampil rata kanan, dengan `[+ Assign]` tampil bagi aktor berwenang
4. Hover tiap icon Table Tools
5. Verifikasi tooltip hover masing-masing icon sesuai nama icon
6. Klik icon Search
7. Verifikasi placeholder Search `Search transaction, role, or group...`
8. Klik `(←)` pada kotak Search
9. Verifikasi Bulk Actions Bar dengan `[Bulk Remove]` tidak tampil selama belum ada baris terpilih
10. Centang satu baris
11. Verifikasi Bulk Actions Bar dengan `[Bulk Remove]` tampil
12. Hapus centang baris itu
13. Verifikasi kolom tabel berurutan `checkbox | Transaction | Role | Group | Actions`
14. Verifikasi kolom Transaction dan Group sortable, kolom Role unsortable
15. Klik header kolom Actions (⋯)
16. Verifikasi overlay Column Visibility terbuka
17. Tutup overlay Column Visibility dengan Esc
18. Verifikasi tiap baris memiliki aksi `[Assign Group]`
19. Klik `⋯` pada satu baris
20. Verifikasi menu `⋯` berisi `Remove`
21. Tutup menu `⋯` dengan Esc
22. Verifikasi pengurutan default Transaction ascending
23. Verifikasi 7 baris pada satu halaman terurut Transaction ascending: `Borrowing & Assignment - Approver`, `Damaged - Monitoring & Report`, dua baris `Disposal` (`Approver`, `Staff`), `Missing - Approver`, dua baris `Transfer` (`Asset Admin`, `Monitoring & Report`); urutan Role pada Transaction yang sama tidak diasersikan
24. Verifikasi footer pagination 10 data per halaman
25. Buka dropdown page size
26. Verifikasi pilihan page size 10, 25, 50, 100
27. Tutup dropdown page size dengan Esc

### TC-FA-SU-384: Search Sub-tab Transaction Role kelas teks: kolom Transaction, Role

28. Ketik Search `Transfer` (kolom Transaction), tekan Enter
29. Verifikasi kolom Transaction: keyword `Transfer` menyisakan `Transfer - Asset Admin` dan `Transfer - Monitoring & Report` (2 baris)
30. Kosongkan isi kotak search, tekan Enter
31. Ketik Search `Approver` (kolom Role), tekan Enter
32. Verifikasi kolom Role: keyword `Approver` menyisakan `Borrowing & Assignment - Approver`, `Disposal - Approver`, dan `Missing - Approver` (3 baris)
33. Klik `(←)` pada kotak Search

### TC-FA-SU-385: Search Sub-tab Transaction Role kelas badge: kolom Group

34. Ketik Search `Surabaya` (kolom Group), tekan Enter
35. Verifikasi kolom Group: keyword `Surabaya` menyisakan `Damaged - Monitoring & Report`, `Missing - Approver`, dan `Transfer - Monitoring & Report` (3 baris)
36. Klik `(←)` pada kotak Search

### TC-FA-SU-386: Siklus interaksi Search Sub-tab Transaction Role: reveal, Enter, clear, collapse

37. Klik icon Search
38. Verifikasi input Search melebar
39. Verifikasi kursor fokus pada input Search
40. Verifikasi placeholder `Search transaction, role, or group...`
41. Hover icon Search
42. Verifikasi tooltip `Search`
43. Ketik 1 karakter dari `Transfer`
44. Verifikasi icon ✕ tampil di kanan input
45. Verifikasi tabel belum tersaring
46. Ketik sisa `Transfer`, tekan Enter
47. Verifikasi tabel tersaring menjadi `Transfer - Asset Admin` dan `Transfer - Monitoring & Report`
48. Klik ✕
49. Verifikasi input Search kosong
50. Verifikasi search bar tetap terbuka
51. Verifikasi kursor fokus pada input Search
52. Verifikasi tabel tetap menampilkan hasil search terakhir
53. Tekan Enter pada input kosong
54. Verifikasi tabel kembali ke semua baris
55. Ketik `Transfer`, tekan Enter, lalu klik `(←)`
56. Verifikasi search bar menutup
57. Verifikasi keyword dikosongkan
58. Verifikasi tabel langsung kembali ke semua baris
59. Klik icon Search, ketik `  Transfer  ` (spasi awal dan akhir), tekan Enter
60. Verifikasi hasil sama dengan `Transfer` tanpa spasi
61. Verifikasi isi input tidak berubah
62. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Langkah penghubung Search (S-03, R-16): langkah 1 (Ketik Search `Yuda Pratama`, tekan Enter) untuk menemukan baris Yuda Pratama di User List 25 pengguna (3 halaman) sebelum membuka Detail.
- Alasan melewati sekitar 35 langkah (62 langkah tertulis, 62 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-383: butir a menyebut `[+ Assign]` tampil bagi aktor berwenang; spec memakai Total Control sehingga hanya kasus tampil yang diasersi.
