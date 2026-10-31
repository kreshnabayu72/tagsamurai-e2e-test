---
id: TC-GS-IMPORT-E2E-037-validasi-code-division-15-16-karakter-karakter-tidak-sah-karakter-sah
title: "Validasi Code Division: 15 dan 16 Karakter, Karakter Tidak Sah, Karakter Sah, Bentrok dengan Sistem, dan Identik Antar-Baris"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-149
  - TC-GS-IMPORT-150
  - TC-GS-IMPORT-151
  - TC-GS-IMPORT-152
  - TC-GS-IMPORT-153
  - TC-GS-IMPORT-154
coverage:
  web: automated
---

# Validasi Code Division: 15 dan 16 Karakter, Karakter Tidak Sah, Karakter Sah, Bentrok dengan Sistem, dan Identik Antar-Baris

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; langkah pertama memilih Sub-Tab Division.
- Data: Client C tanpa draft Tab Division (Kontrak Fixture R1; skrip reset disediakan tim FE/BE); Division Pre-setup `Engineering` dengan Code `ENG` ada di Client C (hanya dibaca sebagai pembanding bentrok pada TC-GS-IMPORT-153, tidak diubah).
- Reset dan cleanup: tiap blok membuat draft Division 3 baris pada Client C; draft dibuang (langkah reset eksplisit, S-09) sebelum blok berikutnya dan di hook `after`; tidak berasumsi seeding berhasil penuh.
- Berkas fixture D-07 (isi literal; semua berheader `Division Name,Code`, 3 baris data; baris 1 `Logistik,LOG` dan baris 3 `Keuangan,KEU` kecuali dinyatakan lain). Tabel "Parameter validasi" (satu baris per blok TC; langkah per baris identik):

  | TC | Berkas dan baris 2 | Status baris | Sel Code | Error Summary Callout | Staging Metric Cards |
  |---|---|---|---|---|---|
  | 149 | `division-code-16.csv`: `Layanan Pelanggan,ABCDEFGHIJKLMNOP` (16 karakter) | baris 2 `error`, lain `pending` | sel Code baris 2 berborder merah dengan ikon penanda merah dan pesan "Max. 15 characters" | satu baris pesan "Code: Max. 15 characters" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 150 | `division-code-15.csv`: `Layanan Pelanggan,ABCDEFGHIJKLMNO` (15 karakter) | 3 baris `pending` | sel Code baris 2 tidak berborder merah dan tanpa ikon penanda error | tidak tampil | Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled) |
  | 151 | `division-code-chars.csv`: `Layanan Pelanggan,FIN#1` | baris 2 `error`, lain `pending` | sel Code baris 2 berborder merah dengan ikon penanda merah dan pesan "Code contains invalid characters" | satu baris pesan "Code contains invalid characters" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 152 | `division-code-ok-chars.csv`: `Layanan Pelanggan,fin-1_a.b` | 3 baris `pending` | sel Code baris 2 tidak berborder merah dan tanpa ikon penanda error; sel Code baris 2 menampilkan nilai dalam huruf besar `FIN-1_A.B` | tidak tampil | Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled) |
  | 153 | `division-code-sys.csv`: `Customer Care,ENG` (bentrok dengan Code `ENG` Division di sistem) | baris 2 `error`, lain `pending`; badge Status baris 2 bertuliskan `error` dan bukan `duplicate` | sel Code baris 2 berborder merah dengan ikon penanda merah dan pesan "Code already exists" | satu baris pesan "Code already exists" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 154 | `division-code-rows-3.csv`: baris 1 `Billing,BIL`, baris 2 `Invoicing,BIL`, baris 3 `Keuangan,KEU` (tanpa `Logistik`) | baris 1 `Billing` `error` dengan pesan sel Code "Code already exists"; baris 2 `Invoicing` dan baris 3 `pending` | pesan sel Code baris 1 "Code already exists" | satu baris pesan "Code already exists" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |

- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft; pembacaan gaya border dan ikon sel Staging Table.
- State global: tidak ada yang diubah selain draft Client C (dibuang hook).

## Test Steps

### TC-GS-IMPORT-149, 150, 151, 152, 153, 154: validasi Code Division

1. Klik Sub-Tab Division

Untuk setiap baris tabel "Parameter validasi" (langkah 2 sampai 13; diulang enam kali berurutan, TC 149 sampai 154):

2. Klik `[Upload File]`
3. Pilih berkas pada kolom Berkas di file picker
4. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
5. Verifikasi modal tertutup
6. Verifikasi muncul toast "Success, row has been added."
7. Perhatikan baris Data Uji pada Staging Table, Staging Metric Cards, dan Error Summary Callout
8. Verifikasi Staging Table menampilkan 3 baris dengan status sesuai kolom Status baris
9. Verifikasi sel Code sesuai kolom Sel Code
10. Verifikasi Error Summary Callout sesuai kolom Error Summary Callout
11. Verifikasi Staging Metric Cards sesuai kolom Staging Metric Cards
12. Buang draft Division Client C (reset ke tanpa draft, Kontrak Fixture R1)
13. Muat ulang halaman Import > Division

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Langkah 2 sampai 13 diulang enam kali (ekspansi 72 langkah, ditambah langkah 1 menjadi 73); parameter tiap iterasi ada di tabel "Parameter validasi"; nomor langkah yang diulang: 2 sampai 13 (konvensi 8b butir 7).
- Alasan di atas sekitar 35 langkah: enam blok homogen satu pola (upload berkas Division dengan Code berbeda, Confirm Mapping, verifikasi status dan sel), masing-masing dengan draft yang dibuang sesudahnya; tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (pindah Sub-Tab), langkah 7 (mengamati sesuai Langkah Uji TC), langkah 12 dan 13 (reset draft dan muat ulang supaya halaman kembali ke state Dropzone, S-09; pada iterasi terakhir juga berfungsi sebagai cleanup).
- Temuan untuk QA:
  - TC-GS-IMPORT-153 dan 154 memakai nama Division literal (`Customer Care`, `Billing`, `Invoicing`) tanpa suffix `{runId}`; nama itu hanya masuk draft Staging Table (tidak di-commit) dan dibuang lewat reset di langkah 12. TC-GS-IMPORT-153 tidak mengubah baris Pre-setup `Engineering/ENG` (S-06).
  - TC-GS-IMPORT-154 berstatus baris 1 `error` dan baris 2 `pending` (baris terbawah pending); spec mengikuti Expected.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
