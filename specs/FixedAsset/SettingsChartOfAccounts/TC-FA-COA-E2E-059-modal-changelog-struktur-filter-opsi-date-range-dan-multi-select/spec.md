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
7. Verifikasi hanya baris Action Delete yang cocok tampil
8. Verifikasi tidak ada baris Edit
9. Klik `(←)` pada kotak Search
10. Klik Clear Field pada Action, lalu klik Apply

### TC-FA-COA-202: Screening struktur Filter Panel

11. Verifikasi field Date: label `Date`, date range picker, placeholder "Select date"
12. Verifikasi field Action: label `Action`, multi-select searchable, placeholder "All actions"
13. Verifikasi field Account Code: label `Account Code`, multi-select searchable, placeholder "All account codes"
14. Verifikasi field Field: label `Field`, multi-select searchable, placeholder "All fields"
15. Verifikasi field Modified By: label `Modified By`, multi-select searchable, placeholder "All users"
16. Verifikasi Old Value dan New Value tidak memiliki field filter

### TC-FA-COA-204: Filter Date range inklusif

17. Pilih rentang Date dari tanggal baris kode 1-1002 sampai tanggal baris kode 6-2001 (21 sampai 22 Oct 2026), lalu klik Apply
18. Verifikasi tabel memuat baris tanggal awal dan tanggal akhir rentang serta baris di antaranya
19. Verifikasi baris di luar rentang (tanggal baris kode 5-6000 dan baris kode 5-6001) tidak tampil
20. Klik Clear Field pada Date, pilih rentang satu hari pada tanggal baris kode 6-2001 (22 Oct 2026), lalu klik Apply
21. Verifikasi tabel hanya memuat baris pada tanggal itu (Start Date sama dengan End Date)
22. Klik Clear Field pada Date, lalu klik Apply

### TC-FA-COA-205: Filter multi-select

23. Pilih Account Code `1-1002` dan `6-2001`, lalu klik Apply
24. Verifikasi tabel memuat baris kode 1-1002 dan baris kode 6-2001
25. Verifikasi baris kode 5-6001 tidak tampil
26. Klik Clear Field pada Account Code
27. Pilih Field `Status` dan `Account Name`, lalu klik Apply
28. Verifikasi tabel memuat baris Field Status dan baris Field Account Name
29. Verifikasi baris Field Account Code dan Last Used in Journal tidak tampil
30. Klik Clear Field pada Field
31. Pilih Modified By user B, lalu klik Apply
32. Verifikasi tabel hanya memuat baris yang diubah user B
33. Klik Clear Field pada Modified By, lalu klik Apply
34. Pilih ukuran halaman 10
35. Tutup modal dengan ikon ✕

## Notes

- Langkah penghubung (S-03): langkah 2 dan 34 (ukuran halaman 100 sementara agar baris seed teramati dalam satu halaman, S-14, dan pemulihannya), langkah 9 dan 10 (menutup kotak Search dan membersihkan filter Action, S-09), langkah 22, 26, 30, dan 33 (membersihkan filter antar-TC), langkah 35 (menutup modal).
- Panel Filter tetap terbuka setelah Apply (sesuai urutan TC-90, TC-202, TC-204, dan TC-205); TC-202 dijalankan pada panel yang dibuka di langkah 3.
- TC-FA-COA-203 (isi opsi dropdown filter) ada di spec 093.
- Temuan untuk QA:
  - TC-90 butir b ("bila tidak ada hasil, tampil No results found") bersyarat dan tidak menentukan data uji; spec tidak mengasersi butir b dan hanya mengasersi butir a. Search `Depreciation` bersama Filter Action = Delete bergantung pada isi baris Delete P41 yang tidak diuraikan TC.
  - TC-204 menyebut tanggal contoh PRD tanpa format tampilan; spec memakai tanggal itu apa adanya dan format tampilan mengikuti General Settings client.
  - Audit trail tumbuh oleh spec lain; baris pembanding hanya memakai baris seed P41.
  - P41 adalah asumsi pre-setup, bukan data PRD.
