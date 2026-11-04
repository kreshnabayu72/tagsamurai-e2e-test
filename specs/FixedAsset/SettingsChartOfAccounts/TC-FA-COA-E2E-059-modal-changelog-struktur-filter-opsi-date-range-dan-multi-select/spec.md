---
id: TC-FA-COA-E2E-059-modal-changelog-struktur-filter-opsi-date-range-dan-multi-select
title: "Modal Changelog: Struktur Filter, Date Range, dan Multi-Select"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-90
  - TC-FA-COA-202
  - TC-FA-COA-204
  - TC-FA-COA-205
coverage:
  web: automated
---

# Modal Changelog: Struktur Filter, Date Range, dan Multi-Select

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Riwayat Changelog P41 (asumsi pre-setup, bukan data PRD): empat baris Example Data Modal Changelog (PRD §4.1.1; tanggal contoh 20 sampai 23 Oct 2026; kode 5-6001, 6-2001, 1-1002, 5-6000; Modified By Rina P) ditambah satu baris Create, satu baris Delete, satu baris Activate (Status Inactive menjadi Active), dan satu entri oleh user B; baris tambahan memakai kode akun selain 1-1002 dan tidak memuat teks `Depr Expense`, `Aug 2026`, atau `Rina` di kolom selain Modified By. Riwayat memuat aksi Create, Edit, dan Delete (TC-90). Changelog adalah audit trail permanen yang tumbuh; asersi memakai baris seed P41 yang dikenali lewat tanggal contoh dan Modified By pada ukuran halaman 100 (langkah 2).
- Rentang Date TC-204: 21 sampai 22 Oct 2026 (tanggal baris kode 1-1002 sampai tanggal baris kode 6-2001, tanggal contoh PRD) dan satu hari 22 Oct 2026.
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-90: Search dan Filter Action

1. Klik ikon Changelog di toolbar
2. Pilih ukuran halaman 100
3. Klik ikon Filter di modal Changelog
4. Pilih Action = Delete, lalu klik Apply
5. Verifikasi baris Action Delete tampil
6. Ketik Search `Depreciation`, tekan Enter
7. Verifikasi sedikitnya satu baris Action Delete tampil setelah Search `Depreciation`
8. Verifikasi hanya baris Action Delete yang cocok tampil
9. Verifikasi tidak ada baris Edit (mis. baris Edit kode 5-6001 seed P41)
10. Klik `(←)` pada kotak Search
11. Klik Clear Field pada Action, lalu klik Apply

### TC-FA-COA-202: Screening struktur Filter Panel

12. Verifikasi field Date: label `Date`, date range picker, placeholder "Select date"
13. Verifikasi field Action: label `Action`, multi-select searchable, placeholder "All actions"
14. Verifikasi field Account Code: label `Account Code`, multi-select searchable, placeholder "All account codes"
15. Verifikasi field Field: label `Field`, multi-select searchable, placeholder "All fields"
16. Verifikasi field Modified By: label `Modified By`, multi-select searchable, placeholder "All users"
17. Verifikasi Old Value dan New Value tidak memiliki field filter

### TC-FA-COA-204: Filter Date range inklusif

18. Pilih rentang Date dari tanggal baris kode 1-1002 sampai tanggal baris kode 6-2001 (21 sampai 22 Oct 2026), lalu klik Apply
19. Verifikasi tabel memuat baris tanggal awal dan tanggal akhir rentang serta baris di antaranya
20. Verifikasi baris di luar rentang (tanggal baris kode 5-6000 dan baris kode 5-6001) tidak tampil
21. Klik Clear Field pada Date, pilih rentang satu hari pada tanggal baris kode 6-2001 (22 Oct 2026), lalu klik Apply
22. Verifikasi baris kode 6-2001 (22 Oct 2026) tampil
23. Verifikasi baris kode 5-6000 tidak tampil
24. Verifikasi tabel hanya memuat baris pada tanggal itu (Start Date sama dengan End Date)
25. Klik Clear Field pada Date, lalu klik Apply

### TC-FA-COA-205: Filter multi-select

26. Pilih Account Code `1-1002` dan `6-2001`, lalu klik Apply
27. Verifikasi tabel memuat baris kode 1-1002 dan baris kode 6-2001
28. Verifikasi baris kode 5-6001 tidak tampil
29. Klik Clear Field pada Account Code
30. Pilih Field `Status` dan `Account Name`, lalu klik Apply
31. Verifikasi tabel memuat baris Field Status dan baris Field Account Name
32. Verifikasi baris Field Account Code dan Last Used in Journal tidak tampil
33. Klik Clear Field pada Field
34. Pilih Modified By user B, lalu klik Apply
35. Verifikasi baris yang diubah user B tampil
36. Verifikasi baris Rina P tidak tampil
37. Verifikasi tabel hanya memuat baris yang diubah user B
38. Klik Clear Field pada Modified By, lalu klik Apply
39. Pilih ukuran halaman 10
40. Tutup modal dengan ikon ✕

## Notes

- Alasan di atas 35 langkah (40): empat blok memakai satu modal Changelog dan satu Filter Panel (satu kelas harness: filter dan search modal), dan Verifikasi pembanding presence/absence ditambahkan sebelum asersi universal (S-01, 8b butir 2); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): langkah 2 dan 39 (ukuran halaman 100 sementara agar baris seed teramati dalam satu halaman, S-14, dan pemulihannya), langkah 10 dan 11 (menutup kotak Search dan membersihkan filter Action, S-09), langkah 25, 29, 33, dan 38 (membersihkan filter antar-TC), langkah 40 (menutup modal).
- Panel Filter tetap terbuka setelah Apply (sesuai urutan TC-90, TC-202, TC-204, dan TC-205); TC-202 dijalankan pada panel yang dibuka di langkah 3.
- TC-FA-COA-203 (isi opsi dropdown filter) ada di spec 093.
- Temuan untuk QA:
  - TC-90 butir b ("bila tidak ada hasil, tampil No results found") bersyarat dan tidak menentukan data uji; spec tidak mengasersi butir b dan hanya mengasersi butir a. Search `Depreciation` bersama Filter Action = Delete bergantung pada isi baris Delete P41 yang tidak diuraikan TC.
  - TC-204 menyebut tanggal contoh PRD tanpa format tampilan; spec memakai tanggal itu apa adanya dan format tampilan mengikuti General Settings client.
  - Audit trail tumbuh oleh spec lain; baris pembanding hanya memakai baris seed P41.
  - Verifikasi pembanding (8b butir 2) hanya memakai baris seed P41: baris Delete (langkah 7), baris kode 6-2001 tanggal 22 Oct 2026 dan baris kode 5-6000 (langkah 22 dan 23), baris user B dan Rina P (langkah 35 dan 36). P41 tidak menguraikan isi baris Delete (Account Name) maupun kode akun baris user B; spec tidak menebaknya dan hanya mengasersi keberadaan baris menurut Action atau Modified By.
  - P41 adalah asumsi pre-setup, bukan data PRD.
