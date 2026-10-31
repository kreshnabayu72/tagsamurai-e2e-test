---
id: TC-GS-IMPORT-E2E-034-validasi-sel-brand-120-121-karakter-emoji-karakter-cetak-trim-urutan
title: "Validasi Sel Brand: 120 dan 121 Karakter, Emoji, Karakter Cetak, Trim, dan Urutan Aturan pada Satu Sel"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-134
  - TC-GS-IMPORT-135
  - TC-GS-IMPORT-136
  - TC-GS-IMPORT-137
  - TC-GS-IMPORT-138
  - TC-GS-IMPORT-171
coverage:
  web: automated
---

# Validasi Sel Brand: 120 dan 121 Karakter, Emoji, Karakter Cetak, Trim, dan Urutan Aturan pada Satu Sel

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; spec ini tidak menguji navigasi.
- Data: Client C tanpa draft Tab Brand (Kontrak Fixture R1; skrip reset disediakan tim FE/BE).
- Reset dan cleanup: tiap blok membuat draft Brand 3 baris pada Client C; draft dibuang (langkah reset eksplisit, S-09) sebelum blok berikutnya dan di hook `after`; tidak berasumsi seeding berhasil penuh.
- Berkas fixture D-07 (isi literal; semua berheader `Brand Name`, 3 baris data; baris 1 `Merek Satu` dan baris 3 `Merek Tiga`):
- Tabel "Parameter validasi" (satu baris per blok TC; langkah per baris identik):

  | TC | Berkas | Brand Name baris 2 | Status baris | Sel Brand Name baris 2 | Error Summary Callout | Staging Metric Cards |
  |---|---|---|---|---|---|---|
  | 134 | `brand-len-120.csv` | `B` diulang 120 kali | 3 baris `pending` | tidak berborder merah dan tanpa ikon penanda error | tidak tampil | Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled) |
  | 135 | `brand-len-121.csv` | `B` diulang 121 kali | baris 2 `error`, baris lain `pending` | berborder merah dengan ikon penanda merah dan pesan "Max. 120 characters" | satu baris pesan "Brand Name: Max. 120 characters" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 136 | `brand-emoji.csv` | `Acme 🚀 Corp` | baris 2 `error`, baris lain `pending` | berborder merah dengan ikon penanda merah dan pesan "Brand name contains invalid characters" | satu baris pesan "Brand name contains invalid characters" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 137 | `brand-special.csv` | `Café O'Neil – Ünïcode ß & Co. (東京)` | 3 baris `pending` | tidak berborder merah dan tanpa ikon penanda error | tidak tampil | Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled) |
  | 138 | `brand-trim.csv` | `B` diulang 120 kali diapit 3 spasi di kiri dan 3 spasi di kanan | 3 baris `pending` | tidak berborder merah dan tanpa ikon penanda error | tidak tampil | Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled) |
  | 171 | `brand-121-emoji.csv` | 121 karakter yang memuat emoji (`B` diulang 120 kali diikuti `🚀`) | baris 2 `error`, baris lain `pending` | berborder merah dengan satu pesan "Max. 120 characters" dan tanpa pesan "Brand name contains invalid characters" | satu baris pesan "Brand Name: Max. 120 characters" dengan badge "1 row" tanpa baris pesan "Brand name contains invalid characters" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |

- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft; pembacaan gaya border dan ikon sel Staging Table.
- State global: tidak ada yang diubah selain draft Client C (dibuang hook).

## Test Steps

### TC-GS-IMPORT-134, 135, 136, 137, 138, 171: validasi sel Brand Name

Untuk setiap baris tabel "Parameter validasi" (langkah 1 sampai 12; diulang enam kali berurutan, TC 134 sampai 138 lalu 171):

1. Klik `[Upload File]`
2. Pilih berkas pada kolom Berkas di file picker
3. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
4. Verifikasi modal tertutup
5. Verifikasi muncul toast "Success, row has been added."
6. Perhatikan baris Data Uji pada Staging Table, Staging Metric Cards, dan Error Summary Callout
7. Verifikasi Staging Table menampilkan 3 baris dengan status sesuai kolom Status baris
8. Verifikasi sel Brand Name baris 2 sesuai kolom Sel Brand Name baris 2
9. Verifikasi Error Summary Callout sesuai kolom Error Summary Callout
10. Verifikasi Staging Metric Cards sesuai kolom Staging Metric Cards
11. Buang draft Brand Client C (reset ke tanpa draft, Kontrak Fixture R1)
12. Muat ulang halaman Import > Brand

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Langkah 1 sampai 12 diulang enam kali (ekspansi 72 langkah); parameter tiap iterasi ada di tabel "Parameter validasi"; nomor langkah yang diulang: 1 sampai 12 (konvensi 8b butir 7).
- Alasan di atas sekitar 35 langkah: enam blok homogen satu pola (upload berkas Brand, Confirm Mapping, verifikasi status dan sel), masing-masing dengan draft yang dibuang sesudahnya; tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 (mengamati sesuai Langkah Uji TC), langkah 11 dan 12 (reset draft dan muat ulang agar halaman kembali ke state Dropzone untuk iterasi berikutnya, S-09). Pada iterasi terakhir langkah 11 dan 12 juga dijalankan sebagai cleanup.
- Teks pesan "Brand Name: Max. 120 characters" pada Error Summary Callout dan "Max. 120 characters" pada sel mengikuti Expected TC.
- Temuan untuk QA:
  - Berkas literal tanpa suffix `{runId}` (`Merek Satu`, `Merek Tiga`); keunikan dijaga lewat reset draft di langkah 11.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
