---
id: TC-GS-IMPORT-E2E-035-validasi-sel-measurement-unit-name-dan-symbol-120-121-10-11-emoji
title: "Validasi Sel Measurement: Unit Name dan Symbol (120 dan 121, 10 dan 11, Emoji, Symbol Duplikat Sah, dan Trim)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-139
  - TC-GS-IMPORT-140
  - TC-GS-IMPORT-141
  - TC-GS-IMPORT-142
  - TC-GS-IMPORT-143
  - TC-GS-IMPORT-144
  - TC-GS-IMPORT-635
coverage:
  web: automated
---

# Validasi Sel Measurement: Unit Name dan Symbol (120 dan 121, 10 dan 11, Emoji, Symbol Duplikat Sah, dan Trim)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; langkah pertama memilih Sub-Tab Measurement.
- Data: Client C tanpa draft Tab Measurement (Kontrak Fixture R1; skrip reset disediakan tim FE/BE).
- Reset dan cleanup: tiap blok membuat draft Measurement 3 baris pada Client C; draft dibuang (langkah reset eksplisit, S-09) sebelum blok berikutnya dan di hook `after`; tidak berasumsi seeding berhasil penuh.
- Berkas fixture D-07 (isi literal; semua berheader `Unit Name,Symbol`, 3 baris data; baris 1 `Meter,m` dan baris 3 `Liter,L` kecuali dinyatakan lain). Tabel "Parameter validasi" (satu baris per blok TC; langkah per baris identik):

  | TC | Berkas dan baris 2 | Status baris | Sel baris 2 | Error Summary Callout | Staging Metric Cards |
  |---|---|---|---|---|---|
  | 139 | `measurement-unit-121.csv`: Unit Name `U` diulang 121 kali, Symbol `u` | baris 2 `error`, lain `pending` | sel Unit Name berborder merah dengan ikon penanda merah dan pesan "Max. 120 characters" | satu baris pesan "Unit Name: Max. 120 characters" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 140 | `measurement-unit-emoji.csv`: `Kilo 😀,kk` | baris 2 `error`, lain `pending` | sel Unit Name berborder merah dengan ikon penanda merah dan pesan "Unit name contains invalid characters" | satu baris pesan "Unit name contains invalid characters" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 141 | `measurement-symbol-10.csv`: `Unit Sepuluh,abcdefghij` | 3 baris `pending` | sel Symbol tidak berborder merah dan tanpa ikon penanda error | tidak tampil | Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled) |
  | 142 | `measurement-symbol-11-3rows.csv`: `Unit Sebelas,abcdefghijk` | baris 2 `error`, lain `pending` | sel Symbol berborder merah dengan ikon penanda merah dan pesan "Max. 10 characters" | satu baris pesan "Symbol: Max. 10 characters" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 143 | `measurement-symbol-emoji.csv`: `Unit Berikon,kg😀` | baris 2 `error`, lain `pending` | sel Symbol berborder merah dengan ikon penanda merah dan pesan "Symbol contains invalid characters" | satu baris pesan "Symbol contains invalid characters" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 144 | `measurement-symbol-dup.csv`: baris 2 `Kilogram Metrik,kg`, baris 3 `Kilogram Troy,kg` (baris 3 menggantikan `Liter,L`) | 3 baris `pending`; baris 2 dan 3 memakai Symbol `kg` yang sama | badge Status baris 2 dan baris 3 bertuliskan `pending` (bukan `duplicate`) | tidak tampil | Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled) |
  | 635 | `measurement-len-120.csv`: Unit Name `U` diulang 120 kali, Symbol `  abcdefghij  ` (dua spasi di kiri dan di kanan) | 3 baris `pending` | sel Unit Name dan Symbol tidak berborder merah dan tanpa ikon penanda error | tidak tampil | Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled) |

- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft; pembacaan gaya border dan ikon sel Staging Table.
- State global: tidak ada yang diubah selain draft Client C (dibuang hook).

## Test Steps

### TC-GS-IMPORT-139, 140, 141, 142, 143, 144, 635: validasi sel Measurement

1. Klik Sub-Tab Measurement

Untuk setiap baris tabel "Parameter validasi" (langkah 2 sampai 13; diulang tujuh kali berurutan, TC 139 sampai 144 lalu 635):

2. Klik `[Upload File]`
3. Pilih berkas pada kolom Berkas di file picker
4. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
5. Verifikasi modal tertutup
6. Verifikasi muncul toast "Success, row has been added."
7. Perhatikan baris Data Uji pada Staging Table, Staging Metric Cards, dan Error Summary Callout
8. Verifikasi Staging Table menampilkan 3 baris dengan status sesuai kolom Status baris
9. Verifikasi sel baris 2 sesuai kolom Sel baris 2
10. Verifikasi Error Summary Callout sesuai kolom Error Summary Callout
11. Verifikasi Staging Metric Cards sesuai kolom Staging Metric Cards
12. Buang draft Measurement Client C (reset ke tanpa draft, Kontrak Fixture R1)
13. Muat ulang halaman Import > Measurement

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Langkah 2 sampai 13 diulang tujuh kali (ekspansi 84 langkah, ditambah langkah 1 menjadi 85); parameter tiap iterasi ada di tabel "Parameter validasi"; nomor langkah yang diulang: 2 sampai 13 (konvensi 8b butir 7).
- Alasan di atas sekitar 35 langkah: tujuh blok homogen satu pola (upload berkas Measurement, Confirm Mapping, verifikasi status dan sel), masing-masing dengan draft yang dibuang sesudahnya; tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (pindah Sub-Tab), langkah 7 (mengamati sesuai Langkah Uji TC), langkah 12 dan 13 (reset draft dan muat ulang supaya halaman kembali ke state Dropzone, S-09; pada iterasi terakhir juga berfungsi sebagai cleanup).
- Temuan untuk QA:
  - Berkas literal tanpa suffix `{runId}` (`Meter`, `Liter`, dan sebagainya); keunikan dijaga lewat reset draft di langkah 12.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
