---
id: TC-FA-COA-E2E-090-search-tabel-modified-by-dan-guard-negatif
title: "Search Tabel: Modified By dan Guard Negatif"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-184
  - TC-FA-COA-185
coverage:
  web: automated
---

# Search Tabel: Modified By dan Guard Negatif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup yang hanya dibaca dan tidak diubah (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>` yang disediakan tim FE, nama kunci ditetapkan tim FE; seeding mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`):
  - P1 `Fixture.settingsChartOfAccounts.p1` (Account Code `5-6001`, Active, Function Depreciation Expense).
  - P2 `Fixture.settingsChartOfAccounts.p2` (Account Code `6-2001`, Last Used in Journal `Aug 2026`).
  - P3 `Fixture.settingsChartOfAccounts.p3` (Account Code `4-7001`, Inactive).
  - P40 (asumsi pre-setup, bukan data PRD): akun P1 terakhir diubah user A, akun P2 terakhir diubah user B; nama depan user A `Fixture.settingsChartOfAccounts.p40.userAFirstName` tidak muncul di Account Code, Account Name, atau Function akun mana pun.
- Kolom Modified By dan Last Updated tersembunyi (default) saat spec mulai. Spec menampilkannya lewat quick panel Column Visibility lalu menyembunyikannya kembali dengan langkah eksplisit (langkah 19 dan 28, R-24); hook `after` menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-185: Guard negatif Search, kolom Active, Last Used in Journal, dan Last Updated tidak ikut dicari

1. Klik header Actions ⋯, centang Last Updated
2. Ketik Search `Fixture.settingsChartOfAccounts.p3.code`, tekan Enter
3. Verifikasi baris P3 (`Fixture.settingsChartOfAccounts.p3.code`, Inactive) tampil di tabel
4. Ganti isi kotak Search dengan `Fixture.settingsChartOfAccounts.p2.code`, tekan Enter
5. Verifikasi baris P2 (`Fixture.settingsChartOfAccounts.p2.code`) tampil di tabel
6. Catat teks sel Last Used in Journal akun P2 (`Aug 2026`)
7. Catat teks sel Last Updated akun P2 (disalin dari layar)
8. Klik `(←)` pada kotak Search
9. Ketik Search `Inactive`, tekan Enter
10. Verifikasi tidak ada baris hasil (switch Status Active tidak ikut dicari)
11. Verifikasi empty state "No results found" dengan deskripsi "Try adjusting your search or filter."
12. Ganti isi kotak Search dengan teks sel Last Used in Journal akun P2 yang dicatat pada langkah 6, tekan Enter
13. Verifikasi tidak ada baris hasil (Last Used in Journal tidak ikut dicari)
14. Verifikasi empty state "No results found" dengan deskripsi "Try adjusting your search or filter."
15. Ganti isi kotak Search dengan teks sel Last Updated akun P2 yang dicatat pada langkah 7, tekan Enter
16. Verifikasi tidak ada baris hasil (Last Updated tidak ikut dicari)
17. Verifikasi empty state "No results found" dengan deskripsi "Try adjusting your search or filter."
18. Klik `(←)` pada kotak Search
19. Klik header Actions ⋯, hapus centang Last Updated

### TC-FA-COA-184: Search nilai kolom Modified By saat kolom ditampilkan

20. Klik header Actions ⋯, centang Modified By
21. Verifikasi kolom Modified By tampil pada tabel
22. Ketik Search `Fixture.settingsChartOfAccounts.p40.userAFirstName`, tekan Enter
23. Verifikasi baris P1 (`Fixture.settingsChartOfAccounts.p1.code`) tampil dengan Modified By user A
24. Verifikasi baris P2 (`Fixture.settingsChartOfAccounts.p2.code`) tidak tampil
25. Ganti isi kotak Search dengan `Fixture.settingsChartOfAccounts.p40.userAFirstName` dalam huruf kapital semua, tekan Enter
26. Verifikasi baris P1 tampil dengan Modified By user A (hasil sama dengan langkah 22 karena pencarian tidak case-sensitive)
27. Verifikasi baris P2 tidak tampil
28. Klik header Actions ⋯, hapus centang Modified By
29. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): langkah 1 dan 20 (menampilkan kolom, precondition TC), langkah 8, 18, dan 29 (`(←)` menutup kotak Search dan mereset tabel, S-09), langkah 2 sampai 5 (Search kode P3 lalu kode P2 agar baris yang dibaca tampil pada tabel yang dapat memuat lebih dari satu halaman; R-16, R-23, bagian 8b butir 13), langkah 6 dan 7 (mencatat teks sel saat hasil Search P2 tampil; TC-FA-COA-185 meminta teks "disalin dari layar").
- Langkah 3, 5, dan 21 menjadi anchor positif bagi asersi absence sesudahnya (8b.2).
- Langkah 28 menyembunyikan kembali Modified By dan langkah 19 menyembunyikan kembali Last Updated (pemulihan Setup Column, R-24 dan 8b.14).
- Urutan blok berbeda dari `sourceTc`: TC-FA-COA-185 (guard negatif, tidak ada baris hasil) mendahului TC-FA-COA-184 sesuai bagian 3 prinsip 3 (validasi yang diblokir sebelum aksi yang menghasilkan baris) dan sebelum kolom Modified By ditampilkan.
- Temuan untuk QA:
  - TC-FA-COA-185 Expected butir a tidak menyatakan apakah "tidak menghasilkan baris" dan empty state dua klausa terpisah; spec memecahnya menjadi dua Verifikasi (S-01).
  - TC-FA-COA-184 langkah 2 hanya menyebut "huruf kapital semua"; spec memakai nama depan user A dalam huruf kapital.
  - P40 adalah asumsi pre-setup (bukan data PRD) yang perlu dikonfirmasi tim FE.
