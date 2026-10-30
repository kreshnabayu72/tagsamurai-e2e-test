---
id: TC-GS-IMPORT-E2E-040-validasi-represented-by-pada-user-non-login-bukan-user-login-aktif-non
title: "Validasi Represented By pada User Non Login: Bukan User Login Aktif (Non-Login, Pending, Inactive, Nama Bukan Email, Draft Belum Commit) dan Cocok Tidak Peka Huruf"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-165
  - TC-GS-IMPORT-166
  - TC-GS-IMPORT-167
  - TC-GS-IMPORT-168
  - TC-GS-IMPORT-169
  - TC-GS-IMPORT-569
  - TC-GS-IMPORT-629
  - TC-GS-IMPORT-630
coverage:
  web: automated
---

# Validasi Represented By pada User Non Login: Bukan User Login Aktif (Non-Login, Pending, Inactive, Nama Bukan Email, Draft Belum Commit) dan Cocok Tidak Peka Huruf

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client C; langkah pembuka memilih Sub-Tab User Non Login.
- Data:
  - Client C tanpa draft Tab User Non Login (Kontrak Fixture R1; skrip reset disediakan tim FE/BE); Client C berisi Division `Engineering` dan Position `Finance Manager` (Pre-setup, Kontrak Fixture R4).
  - Pre-setup Client C (tidak diubah): User Login aktif `rina.admin.c@example.com` (nama `Rina Admin`); User Login `tono.inactive.c@example.com` (Inactive); User Login `baru.impor.c@example.com` (Pending Activation); User Non Login `agus.nonlogin.c@example.com`.
  - D-20: draft User Login Client C 8 baris `pending` dari `user-login-8.csv` (salinan D-05 pada Client C; baris #1 `ahmad.fauzi@example.com`), belum di-commit, disiapkan skrip fixture di langkah 1 (dipakai sebagai sumber email Pending pada TC-GS-IMPORT-167).
  - Berkas fixture D-07 (isi literal; semua berheader `First Name,Last Name,Email,Division,Position,Employee ID,Represented By,Active Period`, 3 baris data; baris valid mengikuti pola `Siti,Rahayu,siti.rahayu2@example.com,Engineering,,,rina.admin.c@example.com,`, angka pada Email mengikuti nomor baris data).
- Reset dan cleanup: tiap blok membuat draft User Non Login 3 baris pada Client C; draft dibuang (langkah reset eksplisit, S-09) sebelum blok berikutnya; draft D-20 dan sisa draft dibuang di hook `after`; tidak berasumsi seeding berhasil penuh.
- Tabel "Parameter validasi" (satu baris per blok TC; langkah per baris identik). Kolom Callout untuk TC dengan status `error`: satu baris pesan "Represented by must be an active User Login account" dengan badge "1 row", `[View Data]`, dan `[Delete All Rows]` tanpa tombol `[Create Missing …]`. Kolom Sel untuk TC `error`: sel Represented By baris 2 berborder merah dengan ikon penanda merah dan pesan "Represented by must be an active User Login account", dan tidak menampilkan badge AI Reference Suggestion.

  | TC | Berkas | Represented By baris ke-2 | Status baris | Sel Represented By baris 2 | Error Summary Callout | Staging Metric Cards |
  |---|---|---|---|---|---|---|
  | 165 | `user-non-login-rep-nf.csv` | `rina.admn.c@example.com` (salah ketik satu huruf dari akun yang ada) | baris 2 `error`, lain `pending` | sesuai kolom Sel untuk TC `error` | sesuai kolom Callout untuk TC `error` | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 166 | `user-non-login-rep-nlu.csv` | `agus.nonlogin.c@example.com` (User Non Login) | baris 2 `error`, lain `pending` | sesuai kolom Sel untuk TC `error` | sesuai kolom Callout untuk TC `error` | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 167 | `user-non-login-rep-pending.csv` | `ahmad.fauzi@example.com` (baris Pending pada draft User Login D-20 yang belum di-commit) | baris 2 `error`, lain `pending` | sesuai kolom Sel untuk TC `error` | sesuai kolom Callout untuk TC `error` | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 168 | `user-non-login-rep-case.csv` | `  RINA.ADMIN.C@Example.com  ` (huruf besar-kecil campur dengan spasi tepi) | 3 baris `pending` | tidak berborder merah dan tanpa ikon penanda error | tidak tampil | Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled) |
  | 169 | `user-non-login-rep-ok.csv` | `rina.admin.c@example.com` | 3 baris `pending` | tidak berborder merah dan tanpa ikon penanda error | tidak tampil | Total Rows 3 (Active), Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled) |
  | 569 | `user-non-login-rep-pending-activation.csv` | `baru.impor.c@example.com` (Login User berstatus Pending Activation) | baris 2 `error`, lain `pending` | sesuai kolom Sel untuk TC `error` | sesuai kolom Callout untuk TC `error` | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 629 | `user-non-login-rep-name.csv` | `Rina Admin` (nama User Login, bukan alamat email) | baris 2 `error`, lain `pending` | sesuai kolom Sel untuk TC `error` | sesuai kolom Callout untuk TC `error` | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |
  | 630 | `user-non-login-rep-inactive.csv` | `tono.inactive.c@example.com` (User Login Inactive) | baris 2 `error`, lain `pending` | sesuai kolom Sel untuk TC `error` | sesuai kolom Callout untuk TC `error` | Total Rows 3 (Active), Ready to Import 2, Errors 1, Duplicates 0 (Disabled) |

- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip seed/reset draft (D-20); pembacaan gaya border dan ikon sel Staging Table.
- State global: tidak ada yang diubah selain draft Client C (dibuang hook).

## Test Steps

### Persiapan

1. Siapkan draft D-20 (User Login 8 baris `pending`) pada Client C lewat skrip fixture
2. Klik Sub-Tab User Non Login

### TC-GS-IMPORT-165, 166, 167, 168, 169, 569, 629, 630: validasi Represented By

Untuk setiap baris tabel "Parameter validasi" (langkah 3 sampai 14; diulang delapan kali berurutan, TC 165 sampai 169, 569, 629, 630):

3. Klik `[Upload File]`
4. Pilih berkas pada kolom Berkas di file picker
5. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
6. Verifikasi modal tertutup
7. Verifikasi muncul toast "Success, row has been added."
8. Perhatikan baris Data Uji pada Staging Table, Staging Metric Cards, dan Error Summary Callout
9. Verifikasi Staging Table menampilkan 3 baris dengan status sesuai kolom Status baris
10. Verifikasi sel Represented By baris 2 sesuai kolom Sel Represented By baris 2
11. Verifikasi Error Summary Callout sesuai kolom Error Summary Callout
12. Verifikasi Staging Metric Cards sesuai kolom Staging Metric Cards
13. Buang draft User Non Login Client C (reset ke tanpa draft, Kontrak Fixture R1)
14. Muat ulang halaman Import > User Non Login

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Langkah 3 sampai 14 diulang delapan kali (ekspansi 96 langkah, ditambah langkah 1 dan 2 menjadi 98); parameter tiap iterasi ada di tabel "Parameter validasi"; nomor langkah yang diulang: 3 sampai 14 (konvensi 8b butir 7).
- Alasan di atas sekitar 35 langkah: delapan blok homogen satu pola dalam satu Sub-Tab (upload berkas User Non Login dengan Represented By berbeda, Confirm Mapping, verifikasi status dan sel), masing-masing dengan draft yang dibuang sesudahnya; tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 2 (penyiapan draft D-20 dan pindah Sub-Tab), langkah 8 (mengamati sesuai Langkah Uji TC), langkah 13 dan 14 (reset draft dan muat ulang supaya halaman kembali ke state Dropzone, S-09; pada iterasi terakhir juga berfungsi sebagai cleanup).
- Temuan untuk QA:
  - TC-GS-IMPORT-167 mensyaratkan draft D-20 (User Login) tetap ada saat blok User Non Login dijalankan; spec menyiapkannya sekali di awal pada Sub-Tab User Login yang tidak tersentuh blok lain.
  - TC-GS-IMPORT-569 menyebut Login User `baru.impor.c@example.com` berstatus Pending Activation sebagai kondisi Client C yang tidak tertulis lengkap pada Tabel Pre-setup (hanya pada ringkasan Client C); ketersediaannya disediakan tim FE/BE.
  - Skrip seed/reset draft Client C tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13). Nilai data literal tanpa suffix `{runId}`; nilai itu tidak di-commit.
