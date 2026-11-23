---
id: TC-FA-SU-E2E-446-tab-transaction-admin-log-borrow-self-processed-dan-filter-name-dan-borrower
title: "Tab Transaction Admin Log Sub-tab Borrow: Self-processed, Filter Name, dan Filter Borrower"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1137
  - TC-FA-SU-1138
  - TC-FA-SU-1139
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Borrow: Self-processed, Filter Name, dan Filter Borrower

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrow berisi 5 baris sesuai Pre-setup #29 TC (`BRW-2026-0315` `Returned · Self-processed` `Laptop Dell Latitude - 3` `Rina Wijaya` `General Affairs`; `BRW-2026-0314` `Rejected` `Projector Epson - 1` `Andi Pratama` `Branch Surabaya`; `BRW-2026-0313` `Handed over` `Camera Sony A7 - 2` `Budi Santoso` `Logistics Warehouse`; `BRW-2026-0312` `Requested` `Laptop Dell Latitude - 5` `Dewi Lestari` `Finance & Accounting`; satu baris `Draft created` `Tablet Samsung Tab - 4` dengan Transaction ID dan Borrower `—` `IT Infrastructure`). Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca; state yang diubah hanya Search dan Filter sisi klien.

## Test Steps

1. Ketik Search `Budi Santoso`, tekan Enter, klik Name Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow

### TC-FA-SU-1137: Penanda Self-processed pada Activity

2. Verifikasi baris `BRW-2026-0315` menampilkan Activity `Returned · Self-processed` (nama node diikuti penanda `Self-processed`)
3. Verifikasi Activity baris `BRW-2026-0315` tampil sebagai teks biasa tanpa badge berwarna
4. Verifikasi baris `BRW-2026-0314` menampilkan Activity `Rejected` tanpa penanda `Self-processed`
5. Klik icon Search
6. Ketik Search `Self-processed`, tekan Enter
7. Verifikasi tabel menyisakan `BRW-2026-0315` (1 baris)
8. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-1138: Filter kelas fk, Name

9. Klik icon Filter
10. Buka dropdown Name
11. Verifikasi field `Name` (placeholder `All assets`) berupa multi-select searchable
12. Verifikasi opsi dropdown = DISTINCT nilai kolom Name pada tabel: `Camera Sony A7 - 2`, `Laptop Dell Latitude - 3`, `Laptop Dell Latitude - 5`, `Projector Epson - 1`, `Tablet Samsung Tab - 4`
13. Ketik `Projector` di kotak cari dropdown
14. Verifikasi opsi dropdown menyempit menjadi `Projector Epson - 1`
15. Centang `Projector Epson - 1`
16. Klik `[Apply]`
17. Verifikasi tabel menyisakan `BRW-2026-0314` (1 baris)
18. Verifikasi chip `Projector Epson - 1` tampil di dalam field `Name`
19. Verifikasi panel Filter tetap terbuka setelah `[Apply]`
20. Klik icon Filter untuk menutup panel
21. Verifikasi panel Filter tertutup

### TC-FA-SU-1139: Filter kelas fk, Borrower

22. Klik icon Filter, lalu klik `[Clear Field]`
23. Klik `[Apply]`
24. Buka dropdown Borrower
25. Verifikasi field `Borrower` (placeholder `All borrowers`) berupa multi-select searchable
26. Verifikasi opsi dropdown = DISTINCT nilai kolom Borrower pada tabel: `Andi Pratama`, `Budi Santoso`, `Dewi Lestari`, `Rina Wijaya`
27. Verifikasi dropdown Borrower tanpa opsi untuk nilai kosong `—`
28. Centang `Dewi Lestari`
29. Klik `[Apply]`
30. Verifikasi tabel menyisakan `BRW-2026-0312` (1 baris)
31. Verifikasi chip `Dewi Lestari` tampil di dalam field `Borrower`
32. Buka dropdown Borrower, lalu centang `Andi Pratama`
33. Klik `[Apply]`
34. Verifikasi tabel menyisakan `BRW-2026-0312` dan `BRW-2026-0314` (2 baris, logika OR dalam field)
35. Verifikasi panel Filter tetap terbuka setelah `[Apply]`
36. Klik icon Filter untuk menutup panel
37. Verifikasi panel Filter tertutup
38. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
39. Klik icon Filter untuk menutup panel

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna lewat Search di User List, R-16, lalu membuka tab dan sub-tab), langkah 5, 9, 10, 13, 15, 16, 20, 24, 28, 29, 32, 33, 36 (membuka dan menutup input Search, panel Filter, dan dropdown), pengosongan Search di langkah 8, serta langkah 22, 23, 38, dan 39 (membersihkan Filter, S-09). Langkah 2 sampai 4 menjadi pembanding bahwa tabel memuat baris lain sebelum asersi "menyisakan" (8b.2); langkah 22 dan 23 membersihkan filter Name sebelum blok Borrower.
- Alasan melewati sekitar 35 langkah (39 langkah): ketiga TC satu kelas (fungsional baca) pada satu pengguna dengan seed yang sama, berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; ukuran berasal dari satu `Verifikasi` per klausa Expected (S-01), termasuk pembersihan filter di antara blok (S-09).
- Pengguna target adalah Budi Santoso Pre-setup yang hanya dibaca (tabel satu halaman, 5 baris), sehingga tidak memakai data bersuffix.
- Temuan untuk QA (S-15): kolom ACC TC-FA-SU-1137 sampai 1139 `#20; Role Total Control` menunjuk Client `FaUserMain`, bukan akun; aktor diambil dari hook suite (Lina Marlina, #1). Post Condition tidak ada.
