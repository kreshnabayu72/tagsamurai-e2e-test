---
id: TC-FA-COA-E2E-040-search-tabel-per-kolom-hidden-dan-used-by
title: "Search Tabel: Per Kolom, Hidden, dan Used By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-72
  - TC-FA-COA-73
  - TC-FA-COA-74
  - TC-FA-COA-183
  - TC-FA-COA-320
coverage:
  web: automated
---

# Search Tabel: Per Kolom, Hidden, dan Used By

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup yang hanya dibaca dan tidak diubah (disediakan tim FE lewat `fixtures/settings-chart-of-accounts.json`, nama kunci ditetapkan tim FE; seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`):
  - P1 `Fixture.settingsChartOfAccounts.p1` (Account Code `5-6001`, Account Name `Depreciation Expense – Admin`, Function Depreciation Expense, Active, Used By 0; Code, Name, dan Function tanpa digit 3).
  - P2 `Fixture.settingsChartOfAccounts.p2` (Account Name `Repairs & Maintenance Expense`, Function Capitalization Offset, Active, Used By 0).
  - P3 `Fixture.settingsChartOfAccounts.p3` dan P5 `Fixture.settingsChartOfAccounts.p5` ada di tabel (P1 sampai P5 tampil pada ukuran halaman bawaan).
  - P39 `Fixture.settingsChartOfAccounts.p39` (asumsi pre-setup, bukan data PRD): satu akun dengan Used By 3 yang Account Code, Account Name, dan Function-nya tidak memuat digit 3.
  - P40 (asumsi pre-setup, bukan data PRD): akun P1 terakhir diubah user A; nama depan user A `Fixture.settingsChartOfAccounts.p40.userAFirstName` tidak muncul di Account Code, Account Name, atau Function akun mana pun.
- Kolom Used By tampil (default) dan kolom Modified By tersembunyi (default) saat spec mulai. Perubahan Setup Column pada langkah 23 dan 28 dipulihkan dengan langkah eksplisit (langkah 28); hook `after` menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-74: Search tanpa debounce, hasil baru setelah Enter

1. Klik ikon Search, ketik `Repairs` di kotak Search tanpa menekan Enter
2. Verifikasi tabel belum berubah sebelum Enter (baris P1 `Fixture.settingsChartOfAccounts.p1.code` masih tampil)
3. Klik `(←)` pada kotak Search

### TC-FA-COA-72: Search per kolom mengembalikan hasil cocok

4. Ketik Search `Depreciation`, tekan Enter
5. Verifikasi tabel memuat akun yang Account Code, Account Name, atau Function-nya mengandung `Depreciation`
6. Verifikasi baris P1 (`Fixture.settingsChartOfAccounts.p1.code`) tampil karena Function-nya Depreciation Expense
7. Verifikasi chip filter tidak berubah (tidak ada chip filter)
8. Klik `(←)` pada kotak Search

### TC-FA-COA-320: Potongan kata pada Account Name

9. Ketik Search `preciation Exp`, tekan Enter
10. Verifikasi tabel memuat akun dengan Account Name mengandung `preciation Exp`
11. Verifikasi baris P1 (`Fixture.settingsChartOfAccounts.p1.code`) termasuk dalam hasil
12. Klik `(←)` pada kotak Search

### TC-FA-COA-73: Search tidak mencakup kolom hidden dan kolom tanggal atau periode

13. Verifikasi kolom Modified By tidak tampil pada tabel
14. Verifikasi baris P1 (`Fixture.settingsChartOfAccounts.p1.code`) tampil di tabel
15. Ketik Search `Fixture.settingsChartOfAccounts.p40.userAFirstName` (nama pengubah akun P1), tekan Enter
16. Verifikasi tidak ada hasil berdasarkan Modified By (baris P1 yang diubah user A tidak tampil)
17. Verifikasi pencarian tanggal atau periode Last Used in Journal tidak dilakukan (hasil langkah 15 tidak memuat baris yang cocok berdasarkan kolom Last Used in Journal)
18. Klik `(←)` pada kotak Search

### TC-FA-COA-183: Search nilai kolom Used By dan berhenti mencari saat kolom disembunyikan

19. Verifikasi kolom Used By tampil pada tabel
20. Ketik Search `3`, tekan Enter
21. Verifikasi baris P39 (`Fixture.settingsChartOfAccounts.p39.code`) tampil karena nilai Used By 3 cocok
22. Verifikasi baris P1 (`Fixture.settingsChartOfAccounts.p1.code`) tidak tampil
23. Klik header Actions ⋯, hapus centang Used By
24. Verifikasi header kolom Used By hilang dari tabel
25. Ganti isi kotak Search dengan `3`, tekan Enter
26. Verifikasi baris P39 tidak tampil karena kolom Used By hidden tidak ikut dicari
27. Verifikasi baris P1 tetap tidak tampil
28. Klik header Actions ⋯, centang kembali Used By
29. Klik `(←)` pada kotak Search

## Notes

- Search pada kolom Modified By yang ditampilkan dan guard negatif kolom non-Searchable dicakup spec `TC-FA-COA-E2E-090-search-tabel-modified-by-dan-guard-negatif`.
- Langkah penghubung (S-03): langkah 3, 8, 12, 18, 29 (`(←)` menutup kotak Search dan mereset tabel sebelum TC berikutnya, S-09); langkah 14 (anchor positif sebelum asersi absence, 8b.2); langkah 23 dan 28 (menyembunyikan dan memulihkan kolom Used By, R-24 dan 8b.13).
- Langkah 24 menjadi anchor positif bagi asersi absence langkah 26 dan 27 (8b.2).
- Temuan untuk QA:
  - TC-FA-COA-73 Expected butir b ("pencarian tanggal atau periode Last Used in Journal tidak dilakukan") tidak punya langkah aksi sendiri; spec mengasersinya dari hasil Search yang sama pada langkah 15 (guard negatif kolom tanggal ada di TC-FA-COA-185).
  - TC-FA-COA-73 tidak menyebut nilai Search; spec memakai nama depan user A dari asumsi pre-setup P40 (TC-FA-COA-184 memakai P40 yang sama).
  - TC-FA-COA-72 menyebut "chip filter tidak berubah" tanpa kondisi awal; spec mengasersi tidak ada chip filter pada tabel awal.
  - P39 dan P40 adalah asumsi pre-setup (bukan data PRD) yang perlu dikonfirmasi tim FE.
