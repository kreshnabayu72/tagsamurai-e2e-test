---
id: TC-GS-IMPORT-E2E-041-validasi-panjang-dan-trim-pada-user-login-first-name-last-name-email
title: "Validasi Panjang dan Trim pada User Login: First Name, Last Name, Email, dan Employee ID (121 dan 120 Karakter)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-155
  - TC-GS-IMPORT-156
  - TC-GS-IMPORT-157
  - TC-GS-IMPORT-158
  - TC-GS-IMPORT-631
  - TC-GS-IMPORT-632
coverage:
  web: automated
---

# Validasi Panjang dan Trim pada User Login: First Name, Last Name, Email, dan Employee ID (121 dan 120 Karakter)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; langkah pertama memilih Sub-Tab User Login.
- Data: Client C tanpa draft Tab User Login (Kontrak Fixture R1; skrip reset disediakan tim FE/BE); Client C berisi Division `Engineering` dan Position `Finance Manager` (Pre-setup, Kontrak Fixture R4).
- Reset dan cleanup: tiap blok membuat draft User Login 3 baris pada Client C; draft dibuang (langkah reset eksplisit, S-09) sebelum blok berikutnya dan di hook `after`; tidak berasumsi seeding berhasil penuh.
- Berkas fixture D-07 (isi literal; semua berheader `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period`, 3 baris data; baris valid mengikuti pola `Budi,Setiawan,budi.setiawan2@example.com,Engineering,Finance Manager,EMP-1002,Global Settings,`, angka pada Email dan Employee ID mengikuti nomor baris data). Email 121 karakter berformat valid: `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.example.com`; Email 120 karakter berformat valid: `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.example.com`.
- Tabel "Parameter validasi" (satu baris per blok TC; langkah per baris identik):

  | TC | Berkas dan nilai baris ke-2 | Status baris | Sel baris 2 | Error Summary Callout | Staging Metric Cards |
  |---|---|---|---|---|---|
  | 155 | `user-login-first-121.csv`: First Name `A` diulang 121 kali | baris 2 `error`, lain `pending` | sel First Name berborder merah dengan ikon penanda merah dan pesan "Max. 120 characters" | satu baris pesan "First Name: Max. 120 characters" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 156 | `user-login-last-121.csv`: Last Name `S` diulang 121 kali | baris 2 `error`, lain `pending` | sel Last Name berborder merah dengan ikon penanda merah dan pesan "Max. 120 characters" | satu baris pesan "Last Name: Max. 120 characters" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 157 | `user-login-email-121.csv`: Email 121 karakter berformat valid | baris 2 `error`, lain `pending` | sel Email berborder merah dengan ikon penanda merah dan pesan "Max. 120 characters" | satu baris pesan "Email: Max. 120 characters" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 158 | `user-login-emp-121.csv`: Employee ID `E` diulang 121 kali | baris 2 `error`, lain `pending` | sel Employee ID berborder merah dengan ikon penanda merah dan pesan "Max. 120 characters" | satu baris pesan "Employee ID: Max. 120 characters" dengan badge "1 row" | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 631 | `user-login-len-120.csv`: First Name `A` diulang 120 kali, Last Name `S` diulang 120 kali, Email 120 karakter berformat valid, Employee ID `E` diulang 120 kali | 3 baris `pending` | sel First Name, Last Name, Email, dan Employee ID tidak berborder merah dan tanpa ikon penanda error | tidak tampil | Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled) |
  | 632 | `user-login-trim.csv`: First Name = 3 spasi + `A` diulang 120 kali + 3 spasi; Email = 2 spasi + `budi.baru@example.com` + 2 spasi; Employee ID = 2 spasi + `E` diulang 120 kali + 2 spasi | 3 baris `pending` | sel First Name, Email, dan Employee ID tidak berborder merah dan tanpa ikon penanda error | tidak tampil | Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled) |

- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft; pembacaan gaya border dan ikon sel Staging Table.
- State global: tidak ada yang diubah selain draft Client C (dibuang hook).

## Test Steps

### TC-GS-IMPORT-155, 156, 157, 158, 631, 632: validasi panjang dan trim User Login

1. Klik Sub-Tab User Login

Untuk setiap baris tabel "Parameter validasi" (langkah 2 sampai 13; diulang enam kali berurutan, TC 155 sampai 158, 631, 632):

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
12. Buang draft User Login Client C (reset ke tanpa draft, Kontrak Fixture R1)
13. Muat ulang halaman Import > User Login

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Langkah 2 sampai 13 diulang enam kali (ekspansi 72 langkah, ditambah langkah 1 menjadi 73); parameter tiap iterasi ada di tabel "Parameter validasi"; nomor langkah yang diulang: 2 sampai 13 (konvensi 8b butir 7).
- Alasan di atas sekitar 35 langkah: enam blok homogen satu pola (upload berkas User Login, Confirm Mapping, verifikasi status dan sel), masing-masing dengan draft yang dibuang sesudahnya; tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (pindah Sub-Tab), langkah 7 (mengamati sesuai Langkah Uji TC), langkah 12 dan 13 (reset draft dan muat ulang supaya halaman kembali ke state Dropzone, S-09; pada iterasi terakhir juga berfungsi sebagai cleanup).
- Temuan untuk QA:
  - Nilai literal Email dan Employee ID memakai pola tetap tanpa suffix `{runId}`; data hanya masuk draft Staging Table (tidak di-commit) dan dibuang lewat reset di langkah 12.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
