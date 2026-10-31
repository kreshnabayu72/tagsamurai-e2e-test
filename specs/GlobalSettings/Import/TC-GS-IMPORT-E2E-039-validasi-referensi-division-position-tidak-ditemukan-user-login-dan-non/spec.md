---
id: TC-GS-IMPORT-E2E-039-validasi-referensi-division-position-tidak-ditemukan-user-login-dan-non
title: "Validasi Referensi Division dan Position: Tidak Ditemukan (User Login dan Non Login), Kosong Valid, dan Pencocokan Tidak Peka Huruf"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-159
  - TC-GS-IMPORT-160
  - TC-GS-IMPORT-161
  - TC-GS-IMPORT-162
  - TC-GS-IMPORT-628
coverage:
  web: automated
---

# Validasi Referensi Division dan Position: Tidak Ditemukan (User Login dan Non Login), Kosong Valid, dan Pencocokan Tidak Peka Huruf

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; perpindahan Sub-Tab ditulis sebagai langkah eksplisit.
- Data: Client C tanpa draft Tab User Login dan User Non Login (Kontrak Fixture R1; skrip reset disediakan tim FE/BE); Client C berisi Division `Engineering` dan Position `Finance Manager` (Pre-setup, Kontrak Fixture R4); User Login aktif `rina.admin.c@example.com` (Pre-setup). Mock layanan AI mode normal (D-42: `Gudng` menjadi saran `Gudang`) tidak diasersi di spec ini.
- Reset dan cleanup: tiap blok membuat draft 3 baris pada Client C; draft dibuang (langkah reset eksplisit, S-09) sebelum blok berikutnya dan di hook `after`; tidak berasumsi seeding berhasil penuh.
- Berkas fixture D-07 (isi literal; 3 baris data; baris valid User Login mengikuti pola `Budi,Setiawan,budi.setiawan2@example.com,Engineering,Finance Manager,EMP-1002,Global Settings,`; baris valid User Non Login mengikuti pola `Siti,Rahayu,siti.rahayu2@example.com,Engineering,,,rina.admin.c@example.com,`; angka pada Email dan Employee ID mengikuti nomor baris data). Berkas User Login berheader `First Name,Last Name,Email,Division,Position,Employee ID,Access,Active Period`; berkas User Non Login berheader `First Name,Last Name,Email,Division,Position,Employee ID,Represented By,Active Period`. Tabel "Parameter validasi" (satu baris per blok TC; langkah per baris identik):

  | TC | Sub-Tab | Berkas dan baris bermasalah | Status baris | Sel baris bermasalah | Error Summary Callout | Staging Metric Cards |
  |---|---|---|---|---|---|---|
  | 159 | User Login | `user-login-div-nf.csv`: baris ke-2 Division `Gudng` | baris 2 `error`, lain `pending` | sel Division baris 2 berborder merah dengan ikon penanda merah dan pesan "Division 'Gudng' was not found. Check spelling, or create the missing division from this row." | satu baris pesan "Division not found" dengan badge "1 row", `[View Data]`, `[Delete All Rows]`, dan `[Create Missing Divisions]` | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 160 | User Login | `user-login-pos-nf.csv`: baris ke-2 Position `Seniur Developer` | baris 2 `error`, lain `pending` | sel Position baris 2 berborder merah dengan ikon penanda merah dan pesan "Position 'Seniur Developer' was not found. Check spelling, create the missing position from this row, or leave blank." | satu baris pesan "Position not found" dengan badge "1 row", `[View Data]`, `[Delete All Rows]`, dan `[Create Missing Positions]` | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 161 | User Login | `user-login-pos-blank.csv`: baris ke-2 Position, Employee ID, dan Active Period kosong | 3 baris `pending` | sel Position, Employee ID, dan Active Period baris 2 menampilkan `—` tanpa border merah | tidak tampil | Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled) |
  | 162 | User Login | `user-login-div-case.csv`: baris ke-2 Division `  engineering  ` (huruf kecil dengan spasi tepi) | 3 baris `pending` | sel Division baris 2 tidak berborder merah dan tanpa ikon penanda error | tidak tampil | Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled) |
  | 628 | User Non Login | `user-non-login-div-pos-nf.csv`: baris ke-2 Division `Gudng`, baris ke-3 Position `Seniur Developer` | baris 1 `pending`, baris 2 dan 3 `error` | sel Division baris 2 berborder merah dengan pesan "Division 'Gudng' was not found. Check spelling, or create the missing division from this row."; sel Position baris 3 berborder merah dengan pesan "Position 'Seniur Developer' was not found. Check spelling, create the missing position from this row, or leave blank." | dua baris pesan: "Division not found" dengan badge "1 row", `[View Data]`, `[Delete All Rows]`, `[Create Missing Divisions]`; dan "Position not found" dengan badge "1 row", `[View Data]`, `[Delete All Rows]`, `[Create Missing Positions]` | Total Rows 3 (Active), Ready to Import 1, Errors 2, Duplicates 0 (Disabled) |

- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip reset draft; pembacaan gaya border dan ikon sel Staging Table.
- State global: tidak ada yang diubah selain draft Client C (dibuang hook).

## Test Steps

### TC-GS-IMPORT-159, 160, 161, 162 (User Login) lalu TC-GS-IMPORT-628 (User Non Login)

Untuk setiap baris tabel "Parameter validasi" (langkah 1 sampai 13; diulang lima kali berurutan: TC 159, 160, 161, 162, 628):

1. Klik Sub-Tab sesuai kolom Sub-Tab
2. Klik `[Upload File]`
3. Pilih berkas pada kolom Berkas di file picker
4. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
5. Verifikasi modal tertutup
6. Verifikasi muncul toast "Success, row has been added."
7. Perhatikan baris Data Uji pada Staging Table, Staging Metric Cards, dan Error Summary Callout
8. Verifikasi Staging Table menampilkan 3 baris dengan status sesuai kolom Status baris
9. Verifikasi sel baris bermasalah sesuai kolom Sel baris bermasalah
10. Verifikasi Error Summary Callout sesuai kolom Error Summary Callout
11. Verifikasi Staging Metric Cards sesuai kolom Staging Metric Cards
12. Buang draft pada Sub-Tab itu di Client C (reset ke tanpa draft, Kontrak Fixture R1)
13. Muat ulang halaman Import

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Langkah 1 sampai 13 diulang lima kali (ekspansi 65 langkah); parameter tiap iterasi ada di tabel "Parameter validasi"; nomor langkah yang diulang: 1 sampai 13 (konvensi 8b butir 7). Langkah 1 memilih Sub-Tab sesuai tabel (aksi idempoten bila sudah aktif).
- Alasan di atas sekitar 35 langkah: lima blok homogen satu pola (upload berkas User Login atau User Non Login, Confirm Mapping, verifikasi status dan sel), masing-masing dengan draft yang dibuang sesudahnya; tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (pindah Sub-Tab), langkah 7 (mengamati sesuai Langkah Uji TC), langkah 12 dan 13 (reset draft dan muat ulang supaya halaman kembali ke state Dropzone, S-09; pada iterasi terakhir juga berfungsi sebagai cleanup).
- Pembagian TC: perilaku `[Create Missing Divisions]` dan `[Create Missing Positions]` serta saran AI atas nilai `Gudng` diuji di spec lain; spec ini hanya memverifikasi kehadiran tombol dan pesan.
- Temuan untuk QA:
  - TC-GS-IMPORT-159, 160, dan 628 memakai nilai salah ketik literal (`Gudng`, `Seniur Developer`) tanpa suffix `{runId}`; nilai itu tidak di-commit sehingga tidak bentrok antar run.
  - Skrip reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
