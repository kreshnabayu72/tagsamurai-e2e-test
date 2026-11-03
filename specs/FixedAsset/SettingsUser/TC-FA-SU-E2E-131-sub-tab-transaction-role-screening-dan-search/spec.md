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

1. Buka Detail Yuda Pratama > Tab Role > Sub-tab Transaction Role
2. Verifikasi Table Tools `Search | Filter | [+ Assign] | Changelog` tampil rata kanan, dengan `[+ Assign]` tampil bagi aktor berwenang
3. Hover tiap icon Table Tools
4. Verifikasi tooltip hover masing-masing icon sesuai nama icon
5. Klik icon Search
6. Verifikasi placeholder Search `Search transaction, role, or group...`
7. Klik `(←)` pada kotak Search
8. Verifikasi Bulk Actions Bar dengan `[Bulk Remove]` tidak tampil selama belum ada baris terpilih
9. Centang satu baris
10. Verifikasi Bulk Actions Bar dengan `[Bulk Remove]` tampil
11. Hapus centang baris itu
12. Verifikasi kolom tabel berurutan `checkbox | Transaction | Role | Group | Actions`
13. Verifikasi kolom Transaction dan Group sortable, kolom Role unsortable
14. Klik header kolom Actions (⋯)
15. Verifikasi overlay Column Visibility terbuka
16. Tutup overlay Column Visibility dengan Esc
17. Verifikasi tiap baris memiliki aksi `[Assign Group]`
18. Klik `⋯` pada satu baris
19. Verifikasi menu `⋯` berisi `Remove`
20. Tutup menu `⋯` dengan Esc
21. Verifikasi pengurutan default Transaction ascending
22. Verifikasi 7 baris pada satu halaman terurut Transaction ascending: `Borrowing & Assignment - Approver`, `Damaged - Monitoring & Report`, dua baris `Disposal` (`Approver`, `Staff`), `Missing - Approver`, dua baris `Transfer` (`Asset Admin`, `Monitoring & Report`); urutan Role pada Transaction yang sama tidak diasersikan
23. Verifikasi footer pagination 10 data per halaman
24. Buka dropdown page size
25. Verifikasi pilihan page size 10, 25, 50, 100
26. Tutup dropdown page size dengan Esc

### TC-FA-SU-384: Search Sub-tab Transaction Role kelas teks: kolom Transaction, Role

27. Ketik Search `Transfer` (kolom Transaction), tekan Enter
28. Verifikasi kolom Transaction: keyword `Transfer` menyisakan `Transfer - Asset Admin` dan `Transfer - Monitoring & Report` (2 baris)
29. Kosongkan isi kotak search, tekan Enter
30. Ketik Search `Approver` (kolom Role), tekan Enter
31. Verifikasi kolom Role: keyword `Approver` menyisakan `Borrowing & Assignment - Approver`, `Disposal - Approver`, dan `Missing - Approver` (3 baris)
32. Klik `(←)` pada kotak Search

### TC-FA-SU-385: Search Sub-tab Transaction Role kelas badge: kolom Group

33. Ketik Search `Surabaya` (kolom Group), tekan Enter
34. Verifikasi kolom Group: keyword `Surabaya` menyisakan `Damaged - Monitoring & Report`, `Missing - Approver`, dan `Transfer - Monitoring & Report` (3 baris)
35. Klik `(←)` pada kotak Search

### TC-FA-SU-386: Siklus interaksi Search Sub-tab Transaction Role: reveal, Enter, clear, collapse

36. Klik icon Search
37. Verifikasi input Search melebar
38. Verifikasi kursor fokus pada input Search
39. Verifikasi placeholder `Search transaction, role, or group...`
40. Hover icon Search
41. Verifikasi tooltip `Search`
42. Ketik 1 karakter dari `Transfer`
43. Verifikasi icon ✕ tampil di kanan input
44. Verifikasi tabel belum tersaring
45. Ketik sisa `Transfer`, tekan Enter
46. Verifikasi tabel tersaring menjadi `Transfer - Asset Admin` dan `Transfer - Monitoring & Report`
47. Klik ✕
48. Verifikasi input Search kosong
49. Verifikasi search bar tetap terbuka
50. Verifikasi kursor fokus pada input Search
51. Verifikasi tabel tetap menampilkan hasil search terakhir
52. Tekan Enter pada input kosong
53. Verifikasi tabel kembali ke semua baris
54. Ketik `Transfer`, tekan Enter, lalu klik `(←)`
55. Verifikasi search bar menutup
56. Verifikasi keyword dikosongkan
57. Verifikasi tabel langsung kembali ke semua baris
58. Klik icon Search, ketik `  Transfer  ` (spasi awal dan akhir), tekan Enter
59. Verifikasi hasil sama dengan `Transfer` tanpa spasi
60. Verifikasi isi input tidak berubah
61. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Alasan melewati sekitar 35 langkah (61 langkah tertulis, 61 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-383: butir a menyebut `[+ Assign]` tampil bagi aktor berwenang; spec memakai Total Control sehingga hanya kasus tampil yang diasersi.
