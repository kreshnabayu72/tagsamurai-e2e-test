---
id: TC-FA-COA-E2E-054-format-tampilan-last-updated-modified-by-dan-date-changelog
title: "Format Tampilan Last Updated, Modified By, dan Date Changelog"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-311
  - TC-FA-COA-312
  - TC-FA-COA-313
  - TC-FA-COA-314
  - TC-FA-COA-315
coverage:
  web: automated
---

# Format Tampilan Last Updated, Modified By, dan Date Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Akun Pre-setup (hanya dibaca dan tidak diubah; identitas dibaca dari `Fixture.settingsChartOfAccounts.p<N>`: `.code` Account Code dan `.name` Account Name; kunci ditetapkan tim FE; fixture belum ada):

  | Akun | Kondisi |
  |---|---|
  | P1 `5-6001 – Depreciation Expense – Admin` | terakhir diubah user A (asumsi pre-setup P40: nama depan user A tidak muncul di Account Code, Account Name, atau Account Function akun mana pun) |
  | P44 `5-6980 – Depreciation Expense – Seeded` | tanpa entri Changelog (record seed atau hasil import; asumsi pre-setup, bukan data PRD) |
  | Riwayat Changelog P41 | berisi entri oleh user Rina P (asumsi pre-setup, bukan data PRD) |

- Kemampuan teknis: membaca waktu dibuat akun P44 lewat BE untuk `Verifikasi` langkah 11 (TC-314); disediakan tim FE/BE.
- General Settings non-default untuk TC-311 dan TC-312: Date Format `dd/MM/yy`, Time Format 24 jam, dan Timezone non-default (perlu dikonfirmasi tim FE, lihat Temuan untuk QA). Mekanisme mengubah dan mengembalikan nilai General Settings disediakan tim FE/BE (langkah 12 dan 23). Jam server dan jam browser sinkron.
- State global yang diubah: Date Format, Time Format, dan Timezone General Settings; dikembalikan ke nilai awal pada langkah 23 dan oleh hook `after` sebagai cadangan.
- State yang diubah spec: konfigurasi kolom (Modified By dan Last Updated ditampilkan pada langkah 1 sampai 3, dipulihkan pada langkah 29 sampai 31). Hook `after` menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Persiapan kolom

1. Klik header Actions ⋯ > `Setup Column...`
2. Centang kolom Modified By dan Last Updated
3. Klik `[Save]`

### TC-FA-COA-313: Modified By tabel utama

4. Ketik Search `Fixture.settingsChartOfAccounts.p1.code`, tekan Enter
5. Verifikasi baris akun P1 tampil di tabel
6. Verifikasi Modified By baris P1 tampil dalam format `[First Name] [Last Initial]`
7. Arahkan kursor ke nilai Modified By baris P1
8. Verifikasi tooltip menampilkan nama lengkap user A

### TC-FA-COA-314: Akun tanpa entri Changelog

9. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p44.code`, tekan Enter
10. Verifikasi Modified By baris P44 tampil `System`
11. Verifikasi Last Updated baris P44 menampilkan waktu akun dibuat

### TC-FA-COA-311: Last Updated tabel utama mengikuti General Settings

12. Ubah General Settings ke Date Format `dd/MM/yy`, Time Format 24 jam, dan Timezone non-default, lalu muat ulang halaman
13. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p1.code`, tekan Enter
14. Verifikasi kolom Last Updated baris P1 menampilkan tanggal dan waktu sesuai Date Format, Time Format, dan Timezone yang dipilih
15. Klik ikon Filter, lalu pilih satu tanggal pada field Last Updated
16. Verifikasi teks input filter Last Updated menampilkan tanggal sesuai Date Format yang dipilih
17. Tutup Filter Panel dengan klik ulang ikon Filter

### TC-FA-COA-312: Date Changelog mengikuti General Settings

18. Klik ikon Changelog di toolbar
19. Verifikasi kolom Date menampilkan tanggal dan waktu sesuai Date Format, Time Format, dan Timezone yang dipilih
20. Klik ikon Filter di modal Changelog, lalu pilih satu tanggal pada field Date
21. Verifikasi teks input filter Date menampilkan tanggal sesuai Date Format yang dipilih
22. Tutup modal Changelog dengan ikon ✕
23. Kembalikan Date Format, Time Format, dan Timezone General Settings ke nilai awal

### TC-FA-COA-315: Modified By modal Changelog

24. Klik ikon Changelog di toolbar
25. Verifikasi kolom Modified By tampil dalam format `[First Name] [Last Initial]` (mis. `Rina P`)
26. Arahkan kursor ke nilai Modified By pada baris Rina P
27. Verifikasi tooltip menampilkan nama lengkap
28. Tutup modal Changelog dengan ikon ✕

### Pemulihan

29. Klik header Actions ⋯ > `Setup Column...`
30. Hapus centang kolom Modified By dan Last Updated
31. Klik `[Save]`
32. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): langkah 1 sampai 3 (menampilkan kolom, precondition TC-311, TC-313, TC-314), langkah 4, 9, 13 (Search untuk menemukan baris target, R-16), langkah 12 dan 23 (mengubah dan mengembalikan General Settings), langkah 17, 22, 28 (menutup panel atau modal), langkah 29 sampai 32 (pemulihan Setup Column eksplisit, R-24 dan 8b.14, dan Search dikosongkan).
- TC-311 dan TC-312 berbagi satu perubahan General Settings (langkah 12); pemulihan TC-311 langkah 3 dan TC-312 langkah 3 digabung pada langkah 23, setelah TC-312 selesai. TC-313, TC-314, dan TC-315 berjalan pada format General Settings awal.
- Urutan blok TC (TC-313, TC-314, TC-311, TC-312, TC-315) berbeda dari `sourceTc`: TC-313 dan TC-314 dibaca pada format General Settings awal sebelum TC-311 dan TC-312 mengubahnya; TC-315 dibaca sesudah General Settings dipulihkan (langkah 23).
- Modified By memakai format `[First Name] [Last Initial]` (R-14).
- Temuan untuk QA:
  - TC-311 dan TC-312 menyebut nilai "non-default" tanpa menyebut nilainya; spec memakai `dd/MM/yy`, 24 jam (nilai TC-358 dan TC-106) dan Timezone non-default yang perlu dikonfirmasi tim FE.
  - TC-311 dan TC-312 tidak menyebut mekanisme mengubah General Settings; spec menyebutnya "disediakan tim FE/BE".
  - TC-314 butir b ("waktu akun dibuat") tidak menyebut nilai pembanding; nilai waktu dibuat P44 dibaca lewat kemampuan baca BE yang disediakan tim FE/BE, dan akun P44 adalah asumsi pre-setup.
  - Akun P1 dan user A (P40), serta Riwayat Changelog P41, adalah asumsi pre-setup, bukan data PRD.
