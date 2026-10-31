---
id: TC-GS-IMPORT-E2E-036-validasi-sel-position-name-dan-division-name-120-121-karakter-dan-emoji
title: "Validasi Sel Position Name dan Division Name: 120 dan 121 Karakter dan Emoji"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-145
  - TC-GS-IMPORT-146
  - TC-GS-IMPORT-147
  - TC-GS-IMPORT-148
  - TC-GS-IMPORT-636
  - TC-GS-IMPORT-637
coverage:
  web: automated
---

# Validasi Sel Position Name dan Division Name: 120 dan 121 Karakter dan Emoji

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; perpindahan Sub-Tab ditulis sebagai langkah eksplisit.
- Data: Client C tanpa draft Tab Position dan Division (Kontrak Fixture R1; skrip reset disediakan tim FE/BE).
- Reset dan cleanup: tiap blok membuat draft 3 baris pada Client C; draft dibuang (langkah reset eksplisit, S-09) sebelum blok berikutnya dan di hook `after`; tidak berasumsi seeding berhasil penuh.
- Berkas fixture D-07 (isi literal; berkas Position berheader `Position Name`, berkas Division berheader `Division Name,Code`; 3 baris data). Tabel "Parameter validasi" (satu baris per blok TC; langkah per baris identik):

  | TC | Sub-Tab | Berkas dan isi | Status baris | Sel Name baris 2 | Error Summary Callout | Staging Metric Cards |
  |---|---|---|---|---|---|---|
  | 145 | Position | `position-len-121.csv`: `Teknisi Gudang` / `P` diulang 121 kali / `Kepala Shift` | baris 2 `error`, lain `pending` | berborder merah dengan ikon penanda merah dan pesan "Max. 120 characters" | satu baris pesan "Position Name: Max. 120 characters" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 146 | Position | `position-emoji.csv`: `Teknisi Gudang` / `Manager 😊` / `Kepala Shift` | baris 2 `error`, lain `pending` | berborder merah dengan ikon penanda merah dan pesan "Position name contains invalid characters" | satu baris pesan "Position name contains invalid characters" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 636 | Position | `position-len-120.csv`: `Teknisi Gudang` / `P` diulang 120 kali / `Kepala Shift` | 3 baris `pending` | tidak berborder merah dan tanpa ikon penanda error | tidak tampil | Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled) |
  | 147 | Division | `division-len-121.csv`: `Logistik,LOG` / `D` diulang 121 kali dengan Code kosong / `Keuangan,KEU` | baris 2 `error`, lain `pending` | berborder merah dengan ikon penanda merah dan pesan "Max. 120 characters" | satu baris pesan "Division Name: Max. 120 characters" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 148 | Division | `division-emoji.csv`: `Logistik,LOG` / `Tim Unggulan 🚀,` (Code kosong) / `Keuangan,KEU` | baris 2 `error`, lain `pending` | berborder merah dengan ikon penanda merah dan pesan "Division name contains invalid characters" | satu baris pesan "Division name contains invalid characters" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 637 | Division | `division-len-120.csv`: `Logistik,LOG` / `D` diulang 120 kali dengan Code kosong / `Keuangan,KEU` | 3 baris `pending` | tidak berborder merah dan tanpa ikon penanda error | tidak tampil | Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled) |

- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft; pembacaan gaya border dan ikon sel Staging Table.
- State global: tidak ada yang diubah selain draft Client C (dibuang hook).

## Test Steps

### TC-GS-IMPORT-145, 146, 636 (Position) lalu TC-GS-IMPORT-147, 148, 637 (Division)

Untuk setiap baris tabel "Parameter validasi" (langkah 1 sampai 13; diulang enam kali berurutan: TC 145, 146, 636, 147, 148, 637):

1. Klik Sub-Tab sesuai kolom Sub-Tab
2. Klik `[Upload File]`
3. Pilih berkas pada kolom Berkas di file picker
4. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
5. Verifikasi modal tertutup
6. Verifikasi muncul toast "Success, row has been added."
7. Perhatikan baris Data Uji pada Staging Table, Staging Metric Cards, dan Error Summary Callout
8. Verifikasi Staging Table menampilkan 3 baris dengan status sesuai kolom Status baris
9. Verifikasi sel Name baris 2 sesuai kolom Sel Name baris 2
10. Verifikasi Error Summary Callout sesuai kolom Error Summary Callout
11. Verifikasi Staging Metric Cards sesuai kolom Staging Metric Cards
12. Buang draft pada Sub-Tab itu di Client C (reset ke tanpa draft, Kontrak Fixture R1)
13. Muat ulang halaman Import

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Langkah 1 sampai 13 diulang enam kali (ekspansi 78 langkah); parameter tiap iterasi ada di tabel "Parameter validasi"; nomor langkah yang diulang: 1 sampai 13 (konvensi 8b butir 7). Langkah 1 memilih Sub-Tab sesuai tabel (aksi idempoten bila sudah aktif).
- Alasan di atas sekitar 35 langkah: enam blok homogen satu pola (upload berkas Position atau Division, Confirm Mapping, verifikasi status dan sel), masing-masing dengan draft yang dibuang sesudahnya; tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (pindah Sub-Tab), langkah 7 (mengamati sesuai Langkah Uji TC), langkah 12 dan 13 (reset draft dan muat ulang supaya halaman kembali ke state Dropzone, S-09; pada iterasi terakhir juga berfungsi sebagai cleanup).
- Temuan untuk QA:
  - Berkas literal tanpa suffix `{runId}`; keunikan dijaga lewat reset draft di langkah 12.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
