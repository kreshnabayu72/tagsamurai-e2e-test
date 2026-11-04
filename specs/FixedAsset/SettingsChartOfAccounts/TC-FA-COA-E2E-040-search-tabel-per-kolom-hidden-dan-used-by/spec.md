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
- Data Pre-setup yang hanya dibaca dan tidak diubah (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE, nama kunci ditetapkan tim FE; seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`):
  - P1 `Fixture.settingsChartOfAccounts.p1` (Account Code `5-6001`, Account Name `Depreciation Expense – Admin`, Function Depreciation Expense, Active, Used By 0; Code, Name, dan Function tanpa digit 3).
  - P2 `Fixture.settingsChartOfAccounts.p2`, P3 `Fixture.settingsChartOfAccounts.p3`, dan P5 `Fixture.settingsChartOfAccounts.p5` tidak dirujuk langkah; ada di tabel hanya sebagai precondition TC-72 ("Akun P1–P5 ada").
  - Pada ukuran halaman bawaan 10 baris urut Account Code A-Z, P1 `5-6001` berada sekitar posisi 25 atau halaman 3 sehingga tidak tampil di halaman 1 tanpa filter dan dibuktikan lewat Search.
  - P39 `Fixture.settingsChartOfAccounts.p39` (asumsi pre-setup, bukan data PRD; Account Code `7-1001` menurut Pre-setup TC): satu akun dengan Used By 3 yang Account Code, Account Name, dan Function-nya tidak memuat digit 3.
  - P40 (asumsi pre-setup, bukan data PRD): akun P1 terakhir diubah user A; nama depan user A `Fixture.settingsChartOfAccounts.p40.userAFirstName` tidak muncul di Account Code, Account Name, atau Function akun mana pun.
- Kolom Used By tampil (default) dan kolom Modified By tersembunyi (default) saat spec mulai. Perubahan Setup Column pada langkah 24 dan 30 dipulihkan dengan langkah eksplisit (langkah 30); hook `after` menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-74: Search tanpa debounce, hasil baru setelah Enter

1. Catat Account Code baris pertama tabel, klik ikon Search, ketik `Repairs` di kotak Search tanpa menekan Enter
2. Verifikasi tabel belum berubah sebelum Enter (baris pertama tabel masih sama dengan yang dicatat pada langkah 1 dan halaman 1 masih menampilkan 10 baris)
3. Klik `(←)` pada kotak Search

### TC-FA-COA-72: Search per kolom mengembalikan hasil cocok

4. Ketik Search `Depreciation`, tekan Enter
5. Verifikasi baris P1 (`Fixture.settingsChartOfAccounts.p1.code`) tampil karena Function-nya Depreciation Expense
6. Verifikasi tabel memuat akun yang Account Code, Account Name, atau Function-nya mengandung `Depreciation`
7. Verifikasi chip filter tidak berubah (tidak ada chip filter)
8. Klik `(←)` pada kotak Search

### TC-FA-COA-320: Potongan kata pada Account Name

9. Ketik Search `preciation Exp`, tekan Enter
10. Verifikasi baris P1 (`Fixture.settingsChartOfAccounts.p1.code`) termasuk dalam hasil
11. Verifikasi tabel memuat akun dengan Account Name mengandung `preciation Exp`
12. Klik `(←)` pada kotak Search

### TC-FA-COA-73: Search tidak mencakup kolom hidden dan kolom tanggal atau periode

13. Verifikasi kolom Modified By tidak tampil pada tabel
14. Ketik Search `Fixture.settingsChartOfAccounts.p1.code`, tekan Enter
15. Verifikasi baris P1 (`Fixture.settingsChartOfAccounts.p1.code`) tampil di tabel
16. Ganti isi kotak Search dengan `Fixture.settingsChartOfAccounts.p40.userAFirstName` (nama pengubah akun P1), tekan Enter
17. Verifikasi tidak ada hasil berdasarkan Modified By (baris P1 yang diubah user A tidak tampil)
18. Verifikasi pencarian tanggal atau periode Last Used in Journal tidak dilakukan (hasil langkah 16 tidak memuat baris yang cocok berdasarkan kolom Last Used in Journal)
19. Klik `(←)` pada kotak Search

### TC-FA-COA-183: Search nilai kolom Used By dan berhenti mencari saat kolom disembunyikan

20. Verifikasi kolom Used By tampil pada tabel
21. Ketik Search `3`, tekan Enter
22. Verifikasi baris P39 (`Fixture.settingsChartOfAccounts.p39.code`) tampil karena nilai Used By 3 cocok
23. Verifikasi baris P1 (`Fixture.settingsChartOfAccounts.p1.code`) tidak tampil
24. Klik header Actions ⋯, hapus centang Used By
25. Verifikasi header kolom Used By hilang dari tabel
26. Ganti isi kotak Search dengan `3`, tekan Enter
27. Verifikasi sedikitnya satu baris akun tampil di tabel
28. Verifikasi baris P39 tidak tampil karena kolom Used By hidden tidak ikut dicari
29. Verifikasi baris P1 tetap tidak tampil
30. Klik header Actions ⋯, centang kembali Used By
31. Klik `(←)` pada kotak Search

## Notes

- Search pada kolom Modified By yang ditampilkan dan guard negatif kolom non-Searchable dicakup spec `TC-FA-COA-E2E-090-search-tabel-modified-by-dan-guard-negatif`.
- Langkah penghubung (S-03): langkah 3, 8, 12, 19, 31 (`(←)` menutup kotak Search dan mereset tabel sebelum TC berikutnya, S-09); langkah 1 (mencatat baris pertama tabel sebagai pembanding langkah 2); langkah 14 dan 15 (Search P1 lalu anchor positif sebelum asersi absence, 8b.2 dan 8b.13: P1 sekitar posisi 25 tidak tampil di halaman 1 tanpa filter); langkah 24 dan 30 (menyembunyikan dan memulihkan kolom Used By, R-24 dan 8b.14).
- Langkah 27 menjadi anchor positif bagi asersi absence langkah 28 dan 29 (8b.2). Langkah 5 dan 10 (presence P1) ditulis mendahului asersi universal langkah 6 dan 11 sehingga urutan Expected TC-72 dan TC-320 berubah untuk itu (8b.2).
- Asersi precondition atau tambahan di luar Expected TC (S-03): langkah 2 (halaman 1 masih menampilkan 10 baris sebagai bukti tabel belum berubah), langkah 13 (precondition TC-73 b: kolom Modified By hidden), dan langkah 20 (precondition TC-183 e: kolom Used By tampil).
- Temuan untuk QA:
  - TC-FA-COA-73 Expected butir b ("pencarian tanggal atau periode Last Used in Journal tidak dilakukan") tidak punya langkah aksi sendiri; spec mengasersinya dari hasil Search yang sama pada langkah 16 (guard negatif kolom tanggal ada di TC-FA-COA-185).
  - TC-FA-COA-73 tidak menyebut nilai Search; spec memakai nama depan user A dari asumsi pre-setup P40 (TC-FA-COA-184 memakai P40 yang sama).
  - TC-FA-COA-72 menyebut "chip filter tidak berubah" tanpa kondisi awal; spec mengasersi tidak ada chip filter pada tabel awal.
  - P39 dan P40 adalah asumsi pre-setup (bukan data PRD) yang perlu dikonfirmasi tim FE.
  - Langkah 22 mengasumsikan P39 (`7-1001`) berada di halaman 1 hasil Search `3` (10 baris urut Account Code A-Z). Posisinya setelah semua akun berawalan 1 sampai 6 yang memuat digit 3; bila akun Pre-setup itu lebih dari 10, P39 jatuh di halaman berikutnya. Jumlah akun itu perlu dipastikan tim FE.
