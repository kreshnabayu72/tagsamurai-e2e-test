---
id: TC-GS-USER-E2E-128-subtab-pending-approvals-kombinasi-search-filter-clear-dan-filter-kolom-hidden
title: "Sub-tab Pending Approvals: Kombinasi Search dan Filter, Clear, Filter Kolom Hidden, dan Nol Baris"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-807
  - TC-GS-USER-808
  - TC-GS-USER-809
  - TC-GS-USER-810
  - TC-GS-USER-811
coverage:
  web: automated
---

# Sub-tab Pending Approvals: Kombinasi Search dan Filter, Clear, Filter Kolom Hidden, dan Nol Baris

## Prerequisites

- Mode: FE+BE. Spec hanya membaca sub-tab Pending Approvals Ahmad Fauzi (read-only, tanpa row action) dan tidak mengubah data Pre-setup User.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before` (seedSession); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca): Ahmad Fauzi (No. 13, data Responsibilities FAMS).
- Data Dinamis (HK8, seeding minimal S-11; seeding user dan approval FAMS lewat API di hook `before` adalah kemampuan yang disediakan tim FE/BE, endpoint tidak disebut di TC, PRD, dan LLD):
  - Requester seed (user biasa, Access `Fixed Asset`, Division `Finance`): R1 First Name `Budi`, Last Name `Santoso {runId}-128`, email `budisantoso+{runId}-128@qwertysystem.net`, tampil di tabel `Budi S`; R2 First Name `Citra`, Last Name `Anggraini {runId}-128`, email `citraanggraini+{runId}-128@qwertysystem.net`, tampil `Citra A`; R3 First Name `Dedi`, Last Name `Kurniawan {runId}-128`, email `dedikurniawan+{runId}-128@qwertysystem.net`, tampil `Dedi K`.
  - 30 request approval in-flight (status Waiting for Approval) dengan Approver Ahmad Fauzi (Pre-setup No. 13), sehingga tabel Pending Approvals Ahmad Fauzi memuat lebih dari satu halaman (page size 10). Transaction ID dibuat FAMS saat seeding dan dikembalikan ke spec; nilainya tidak ditulis di spec. Submission Date `D1` = hari uji dikurangi 14 hari dan `D2` = hari uji dikurangi 7 hari (kemampuan menetapkan Submission Date seed disediakan tim FE/BE), teks tanggal dibaca dari sel tabel dalam Date Format General Settings.
  - Transaction `Transfer`, `{transaksi-B}`, dan `{transaksi-C}`: `Transfer` dan dua nilai Transaction FAAP lain yang namanya tidak memuat `ransf`, dipilih tim FE/BE saat seeding (TC dan PRD tidak menyebut nilai selain `Transfer`). `{transaksi-D}` = satu nilai Transaction FAAP lain yang tidak di-seed (tidak punya baris).

    | Kelompok | Transaction | Requester | Submission Date | Jumlah baris |
    |---|---|---|---|---|
    | S1 | `Transfer` | R1 `Budi S` | D1 | 6 |
    | S2 | `Transfer` | R2 `Citra A` | D2 | 4 |
    | S3 | `{transaksi-B}` | R2 `Citra A` | D1 | 6 |
    | S4 | `{transaksi-B}` | R3 `Dedi K` | D2 | 6 |
    | S5 | `{transaksi-C}` | R3 `Dedi K` | D1 | 4 |
    | S6 | `{transaksi-C}` | R1 `Budi S` | D2 | 4 |

  - Hasil per dimensi: Transaction `Transfer` 10 baris, `{transaksi-B}` 12 baris, `{transaksi-C}` 8 baris; Requester R1, R2, R3 masing-masing 10 baris; Submission Date D1 16 baris, D2 14 baris. Tiap kolom yang diuji (Transaction, Requester, Submission Date) memuat tiga, tiga, dan dua nilai distinct.
  - Baris contoh = satu baris kelompok S1 (Transfer, R1 `Budi S`, D1); Transaction ID-nya `{trxId-contoh}` dikembalikan oleh seeding.
  - Keyword unik Requester (hanya cocok dengan Requester seed spec ini karena memuat suffix): `ntoso {runId}-128` (R1), `raini {runId}-128` (R2), `{runId}-128` (R1, R2, R3).
  - Baris Pre-setup Pending Approvals Ahmad Fauzi (bila ada) tidak diubah dan jumlahnya tidak diasumsikan: asersi jumlah baris memakai keyword atau filter yang hanya cocok dengan baris seed, dan asersi urutan atau isi umum tidak bergantung pada baris Pre-setup.
  - Cleanup di hook `after` (tanpa berasumsi seeding berhasil penuh): hapus 30 request approval seed dan user Requester seed lewat API.
- Data uji per TC: TC-GS-USER-807 Search `ntoso {runId}-128` dan Filter Transaction `Transfer`; TC-GS-USER-808 Filter Transaction `Transfer` dan Search `raini {runId}-128`; TC-GS-USER-809 Search `ntoso {runId}-128`, sort Transaction ID, dan Filter Transaction `Transfer`; TC-GS-USER-810 Filter Requester `Citra A` dan kolom `Requester` di-hide; TC-GS-USER-811 Search `raini {runId}-128` dan Filter Transaction `{transaksi-C}` (R2 tidak memiliki request `{transaksi-C}`, sehingga tidak beririsan).
- State yang diubah dan dipulihkan: Search ditutup dan dikosongkan, Filter dikosongkan, sort dikembalikan ke default (langkah 42 dan 43), dan visibilitas kolom `Requester` dikembalikan (langkah 60) di akhir blok masing-masing; page size dikembalikan ke 10 oleh hook `after`; hook `after` sebagai cadangan.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`): tabel Pending Approvals Ahmad Fauzi hanya boleh memuat baris Pre-setup dan seed spec ini saat spec berjalan.
- Kemampuan teknis: memilih opsi pada multi-select Filter Panel; membaca teks sel tabel dan menghitung baris; membaca indikator sort pada header kolom.

## Test Steps

### TC-GS-USER-807: Search lalu Filter menghasilkan irisan

1. Ketik Search `Ahmad Fauzi`, tekan Enter
2. Klik Name `Ahmad Fauzi` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Pending Approvals`
5. Ubah page size ke 100 supaya seluruh baris seed tampil dalam satu halaman
6. Klik icon Search, ketik `ntoso {runId}-128`, tekan Enter
7. Verifikasi tabel menampilkan 10 baris dengan Requester `Budi S`
8. Klik icon Filter
9. Buka dropdown Transaction
10. Pilih opsi `Transfer` di dropdown Transaction
11. Klik `[Apply]`
12. Verifikasi hasil = Search ∩ Filter: 6 baris, seluruhnya bernilai Transaction `Transfer` dan Requester `Budi S`
13. Verifikasi keyword tidak ter-reset (kotak Search masih berisi `ntoso {runId}-128`)
14. Klik icon Filter
15. Klik `[Clear Field]`
16. Klik `[Apply]`
17. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-808: Filter lalu Search menghasilkan irisan

18. Klik icon Filter
19. Buka dropdown Transaction
20. Pilih opsi `Transfer` di dropdown Transaction
21. Klik `[Apply]`
22. Klik icon Search, ketik `raini {runId}-128`, tekan Enter
23. Verifikasi hasil = Filter ∩ Search: 4 baris, seluruhnya bernilai Transaction `Transfer` dan Requester `Citra A`
24. Klik icon panah `(←)` untuk menutup Search dan mereset tabel
25. Klik icon Filter
26. Klik `[Clear Field]`
27. Klik `[Apply]`

### TC-GS-USER-809: Clear filter saat Search dan Sort aktif

28. Klik icon Search, ketik `ntoso {runId}-128`, tekan Enter
29. Klik header Transaction ID
30. Klik icon Filter
31. Buka dropdown Transaction
32. Pilih opsi `Transfer` di dropdown Transaction
33. Klik `[Apply]`
34. Klik icon Filter
35. Klik `[Clear Field]`
36. Klik `[Apply]`
37. Verifikasi keyword tetap aktif (kotak Search masih berisi `ntoso {runId}-128`)
38. Verifikasi arah sort tetap aktif (Transaction ID terurut A-Z)
39. Verifikasi baris dengan Transaction `{transaksi-C}` kembali tampil (hasil Search Requester `Budi S` tanpa Filter)
40. Klik header Transaction ID
41. Klik header Transaction ID
42. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-810: Filter tetap tersedia untuk kolom yang di-hide

43. Klik icon Filter
44. Buka dropdown Requester
45. Pilih opsi `Citra A` di dropdown Requester
46. Klik `[Apply]`
47. Verifikasi tabel menampilkan 10 baris dengan Requester `Citra A`
48. Klik header kolom Actions (⋯)
49. Hilangkan centang kolom `Requester` pada Overlay Column Visibility
50. Tutup Overlay Column Visibility
51. Verifikasi kolom `Requester` tidak tampil di tabel
52. Verifikasi filter tetap aktif menyaring: tabel tetap menampilkan 10 baris dan tidak ada baris dengan Transaction `{transaksi-C}`
53. Klik icon Filter
54. Verifikasi field `Requester` tetap ada di Filter Panel
55. Klik `[Clear Field]`
56. Klik `[Apply]`
57. Klik header kolom Actions (⋯)
58. Centang kembali kolom `Requester` pada Overlay Column Visibility
59. Tutup Overlay Column Visibility

### TC-GS-USER-811: Kombinasi Search + Filter menghasilkan 0 baris lalu pulih saat salah satu dilepas

60. Klik icon Search, ketik `raini {runId}-128`, tekan Enter
61. Verifikasi tabel menampilkan 10 baris dengan Requester `Citra A`
62. Klik icon Filter
63. Buka dropdown Transaction
64. Pilih opsi `{transaksi-C}` di dropdown Transaction
65. Klik `[Apply]`
66. Verifikasi empty filtered state: ilustrasi, `No results found`, dan `Try adjusting your search or filter.`
67. Klik icon Filter
68. Klik `[Clear Field]`
69. Klik `[Apply]`
70. Verifikasi baris hasil search tampil kembali: 10 baris dengan Requester `Citra A`
71. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Dependensi data Pending Approvals Ahmad Fauzi dipenuhi spec ini lewat seeding di hook `before`, tanpa menumpang spec lain.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (807 sampai 811) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Search nama baris persis sebelum Klik Name, karena User List bisa lebih dari satu halaman; akhiran runId saja tidak cukup), langkah 5 (page size 100 supaya seluruh baris seed tampil di satu halaman), 17, 24, 42, dan 71 (menutup Search dan mereset tabel), 40 dan 41 (klik kedua dan ketiga header Transaction ID mengembalikan sort ke default), 50 dan 59 (menutup Overlay Column Visibility), 55 dan 56 (`[Clear Field]` dan `[Apply]` melepas Filter), 57 dan 58 (membuka overlay dan mencentang kembali kolom `Requester`), serta pasangan `[Clear Field]` dan `[Apply]` di akhir TC-GS-USER-807, 808, 809, dan 811.
- Pada TC-GS-USER-809 Filter diterapkan dahulu (langkah Apply) lalu dilepas sesuai langkah TC; keadaan antara tidak diasersi karena Expected TC hanya menyebut keyword, sort, dan Filter sesudah `[Clear Field]` + `[Apply]`. Jumlah baris 10, 6, dan 4 berasal dari matriks seed.
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` 10 baris Requester `Budi S` atau `Citra A` sebelum Filter diterapkan (TC-GS-USER-807, 810, 811) dan `Verifikasi` baris `{transaksi-C}` kembali tampil (TC-GS-USER-809) berfungsi sebagai pembanding bagi hasil yang disaring (8b butir 2).
- Pembagian TC lintas spec: TC-GS-USER-393, 394, 792 sampai 797 ada di spec 126; TC-GS-USER-798 sampai 806 ada di spec 127; TC-GS-USER-812, 813, 828, 829 ada di spec 129; TC-GS-USER-814 sampai 822 ada di spec 130; TC-GS-USER-395 dan 823 sampai 827 ada di spec 131.
- Spec melewati sekitar 35 langkah (71 langkah) karena lima TC kombinasi berada di satu kelas harness (fungsional, baca saja), satu sub-tab, dan dataset seed yang sama; tiap blok berdiri sendiri dan membersihkan state-nya sendiri (Search, Filter, sort, kolom), jadi kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-USER-807 sampai 811: TC memakai "keyword" dan "filter" tanpa nilai; spec memilih Search atas Requester seed dan Filter Transaction/Requester sesuai matriks seed.
  - TC-GS-USER-809: TC tidak menyebut kolom yang di-sort; spec memilih Transaction ID.
  - TC-GS-USER-810: TC tidak menyebut kolom yang di-hide; spec memilih kolom `Requester` yang juga dipakai Filter.
  - Mekanisme seeding user Requester dan request approval FAMS (jenis Transaction, Requester, Submission Date, Approver) tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE tanpa endpoint karangan. TC tidak menyebut nilai Transaction selain `Transfer`; dua nilai FAAP lain dipilih tim FE/BE.
  - Mekanisme menyetel flag Guided Tooltip `gs-user` tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (hook suite).
