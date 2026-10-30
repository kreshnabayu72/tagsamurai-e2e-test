---
id: TC-GS-USER-E2E-129-subtab-pending-approvals-sort-3-state-pagination-dan-kombinasi
title: "Sub-tab Pending Approvals: Sort 3-State, Pagination, dan Kombinasi Search+Filter+Sort+Pagination"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-812
  - TC-GS-USER-813
  - TC-GS-USER-828
  - TC-GS-USER-829
coverage:
  web: automated
---

# Sub-tab Pending Approvals: Sort 3-State, Pagination, dan Kombinasi Search+Filter+Sort+Pagination

## Prerequisites

- Mode: FE+BE. Spec hanya membaca sub-tab Pending Approvals Ahmad Fauzi (read-only, tanpa row action) dan tidak mengubah data Pre-setup User.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before` (seedSession); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca): Ahmad Fauzi (No. 13, data Responsibilities FAMS).
- Data Dinamis (HK8, seeding minimal S-11; seeding user dan approval FAMS lewat API di hook `before` adalah kemampuan yang disediakan tim FE/BE, endpoint tidak disebut di TC, PRD, dan LLD):
  - Requester seed (user biasa, Access `Fixed Asset`, Division `Finance`): R1 First Name `Budi`, Last Name `Santoso {runId}-129`, email `budisantoso+{runId}-129@qwertysystem.net`, tampil di tabel `Budi S`; R2 First Name `Citra`, Last Name `Anggraini {runId}-129`, email `citraanggraini+{runId}-129@qwertysystem.net`, tampil `Citra A`; R3 First Name `Dedi`, Last Name `Kurniawan {runId}-129`, email `dedikurniawan+{runId}-129@qwertysystem.net`, tampil `Dedi K`.
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
  - Keyword unik Requester (hanya cocok dengan Requester seed spec ini karena memuat suffix): `ntoso {runId}-129` (R1), `raini {runId}-129` (R2), `{runId}-129` (R1, R2, R3).
  - Baris Pre-setup Pending Approvals Ahmad Fauzi (bila ada) tidak diubah dan jumlahnya tidak diasumsikan: asersi jumlah baris memakai keyword atau filter yang hanya cocok dengan baris seed, dan asersi urutan atau isi umum tidak bergantung pada baris Pre-setup.
  - Cleanup di hook `after` (tanpa berasumsi seeding berhasil penuh): hapus 30 request approval seed dan user Requester seed lewat API.
- Data uji per TC: TC-GS-USER-812 dan 813 tiga nilai Requester, tiga nilai Transaction, dan dua tanggal Submission Date dari seed (sort memakai data dengan sedikitnya dua nilai distinct per kolom); TC-GS-USER-828 total baris lebih dari 25 (30 seed ditambah baris Pre-setup) pada page size 10; TC-GS-USER-829 Search `{runId}-129` (30 baris seed), Filter Transaction `Transfer` dan `{transaksi-B}` (22 baris), sort Transaction ID, dan page size 25.
- State yang diubah dan dipulihkan: sort dikembalikan ke default (langkah 50 dan 51), Filter dikosongkan (langkah 52 sampai 54), Search ditutup (langkah 55), dan page size dikembalikan ke 10 (langkah 30 dan 56); hook `after` sebagai cadangan.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`): tabel Pending Approvals Ahmad Fauzi hanya boleh memuat baris Pre-setup dan seed spec ini saat spec berjalan.
- Kemampuan teknis: membaca indikator sort pada header kolom dan urutan nilai sel; membaca indikator halaman aktif; mengubah page size lewat kontrol pagination.

## Test Steps

### TC-GS-USER-812: Sort 3-state kolom kelas teks A-Z

1. Klik Name `Ahmad Fauzi` di User List
2. Klik Tab `Responsibilities`
3. Klik sub-tab `Pending Approvals`
4. Klik header Transaction ID
5. Verifikasi nilai kolom Transaction ID terurut A-Z pada halaman 1 (klik 1)
6. Klik header Transaction ID
7. Verifikasi nilai kolom Transaction ID terurut Z-A pada halaman 1 (klik 2)
8. Klik header Transaction ID
9. Verifikasi tabel kembali ke default sort Submission Date Oldest First (klik 3): tanggal pada halaman 1 terurut dari terlama
10. Klik header Transaction
11. Verifikasi nilai kolom Transaction terurut A-Z pada halaman 1 (klik 1)
12. Klik header Transaction
13. Verifikasi nilai kolom Transaction terurut Z-A pada halaman 1 (klik 2)
14. Klik header Transaction
15. Verifikasi tabel kembali ke default sort Submission Date Oldest First (klik 3): tanggal pada halaman 1 terurut dari terlama
16. Klik header Requester
17. Verifikasi nilai kolom Requester terurut A-Z pada halaman 1 (klik 1)
18. Klik header Requester
19. Verifikasi nilai kolom Requester terurut Z-A pada halaman 1 (klik 2)
20. Klik header Requester
21. Verifikasi tabel kembali ke default sort Submission Date Oldest First (klik 3): tanggal pada halaman 1 terurut dari terlama

### TC-GS-USER-813: Sort 3-state kolom kelas tanggal

22. Klik header Submission Date
23. Verifikasi Submission Date terurut Oldest First pada halaman 1 (klik 1)
24. Klik header Submission Date
25. Verifikasi Submission Date terurut Newest First pada halaman 1 (klik 2)
26. Klik header Submission Date
27. Verifikasi tabel kembali ke default sort Submission Date Oldest First (klik 3)

### TC-GS-USER-828: Pagination ubah page size dan input nomor halaman

28. Ubah page size ke 25
29. Verifikasi tabel menampilkan 25 baris pada halaman 1 (total baris lebih dari 25)
30. Kembalikan page size ke 10
31. Ketik nomor halaman `2` di input halaman, tekan Enter
32. Verifikasi tabel langsung berpindah ke halaman 2
33. Klik tombol next
34. Verifikasi halaman aktif berpindah ke halaman 3
35. Klik tombol prev
36. Verifikasi halaman aktif kembali ke halaman 2

### TC-GS-USER-829: Kombinasi Search + Filter + Sort + Pagination berjalan bersamaan

37. Klik tombol prev ke halaman 1
38. Klik icon Search, ketik `{runId}-129`, tekan Enter
39. Klik icon Filter
40. Buka dropdown Transaction
41. Pilih opsi `Transfer` di dropdown Transaction
42. Pilih opsi `{transaksi-B}` di dropdown Transaction
43. Klik `[Apply]`
44. Klik header Transaction ID
45. Ubah page size ke 25
46. Verifikasi keyword berlaku: kotak Search masih berisi `{runId}-129`
47. Verifikasi filter berlaku: icon Filter gelap dan seluruh baris bernilai Transaction `Transfer` atau `{transaksi-B}`
48. Verifikasi sort berlaku: Transaction ID terurut A-Z
49. Verifikasi page size 25 berlaku: seluruh 22 baris hasil tampil pada halaman 1
50. Klik header Transaction ID
51. Klik header Transaction ID
52. Klik icon Filter
53. Klik `[Clear Field]`
54. Klik `[Apply]`
55. Klik icon panah `(←)` untuk menutup Search dan mereset tabel
56. Kembalikan page size ke 10

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Dependensi data Pending Approvals Ahmad Fauzi dipenuhi spec ini lewat seeding di hook `before`, tanpa menumpang spec lain.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (812, 813, 828, 829) dipertahankan.
- Asersi urutan memakai pemeriksaan urutan nilai pada halaman 1, bukan daftar nilai literal, karena Transaction ID dibuat FAMS dan baris Pre-setup Ahmad Fauzi tidak diasumsikan. Urutan Requester mengikuti nama lengkap (hover); karena nama tampil `[First Name] [Last Initial]`, pemeriksaan dilakukan atas nama lengkap Requester.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 30 (mengembalikan page size ke 10 sebelum mengetik nomor halaman), 37 (kembali ke halaman 1), 50 dan 51 (klik kedua dan ketiga header Transaction ID mengembalikan sort ke default), 52 sampai 54 (melepas Filter), 55 (menutup Search dan mereset tabel), dan 56 (mengembalikan page size ke 10).
- Pembagian TC lintas spec: TC-GS-USER-393, 394, 792 sampai 797 ada di spec 126; TC-GS-USER-798 sampai 806 ada di spec 127; TC-GS-USER-807 sampai 811 ada di spec 128; TC-GS-USER-814 sampai 822 ada di spec 130; TC-GS-USER-395 dan 823 sampai 827 ada di spec 131.
- Spec melewati sekitar 35 langkah (56 langkah) karena empat TC berada di satu kelas harness (fungsional, baca saja), satu sub-tab, dan dataset seed yang sama; TC-GS-USER-812 berisi tiga blok identik (Transaction ID, Transaction, Requester) yang masing-masing berdiri sendiri dan berakhir di sort default.
- Temuan untuk QA:
  - TC-GS-USER-812 dan 813: sort default tabel adalah Submission Date Oldest First, sehingga klik 1 pada Submission Date (Oldest First) menghasilkan urutan yang sama dengan klik 3 (default); keduanya dibedakan lewat nomor klik, bukan urutan baris.
  - TC-GS-USER-828 langkah 5: "Kembali 10" tidak punya Expected sendiri; spec menjalankannya sebagai langkah penghubung.
  - TC-GS-USER-828: Data Uji "≥21 baris" diperluas menjadi lebih dari 25 baris supaya page size 25 teramati membatasi 25 baris dan halaman 3 tersedia untuk next dan prev.
  - TC-GS-USER-829: TC menulis "Terapkan filter bila tersedia"; Filter tersedia pada sub-tab ini sehingga spec menerapkannya.
  - Mekanisme seeding user Requester dan request approval FAMS (jenis Transaction, Requester, Submission Date, Approver) tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE tanpa endpoint karangan. TC tidak menyebut nilai Transaction selain `Transfer`; dua nilai FAAP lain dipilih tim FE/BE.
  - Mekanisme menyetel flag Guided Tooltip `gs-user` tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (hook suite).
