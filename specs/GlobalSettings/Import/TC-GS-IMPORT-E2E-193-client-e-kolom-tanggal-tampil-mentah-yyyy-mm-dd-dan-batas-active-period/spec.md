---
id: TC-GS-IMPORT-E2E-193-client-e-kolom-tanggal-tampil-mentah-yyyy-mm-dd-dan-batas-active-period
title: "Client E: kolom tanggal tampil mentah YYYY-MM-DD dan batas Active Period besok menurut zona waktu client"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-486
  - TC-GS-IMPORT-529
coverage:
  web: automated
---

# Client E: kolom tanggal tampil mentah YYYY-MM-DD dan batas Active Period besok menurut zona waktu client

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah jam server dan jam browser (state global) untuk TC-GS-IMPORT-529; hook `after` memulihkannya (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC_PASSWORD`.
- Layar awal: hook `beforeEach` membuka Import > Brand Client E; Sub-Tab User Login dibuka di langkah.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Pre-setup: Client E tanpa draft Tab User Login (Kontrak Fixture R1); General Settings Client E: Date Format `dd MMM yy`, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`. Division `Engineering` ada di Client E (R4).
- Jam (TC-GS-IMPORT-529): jam server dan jam browser diatur bersama ke 01:30 waktu lokal Client E (UTC+7) pada hari uji lewat kemampuan fixture jam server dan emulasi jam browser (disediakan tim FE/BE); dengan jam itu tanggal hari ini menurut zona Client E berbeda dari tanggal UTC, dan itulah yang diuji. Tanggal berkas dihitung dari jam yang telah diatur dan zona Client E, bukan dari jam hook. Jam dipulihkan lewat langkah aksi di akhir TC-GS-IMPORT-529 dan oleh hook `after` sebagai cadangan.
- Berkas uji (pembuat data lewat upload UI; draft tidak di-commit): `user-login-date.csv` (1 baris, Email unik bersuffix `+{runId}-193`, Division `Engineering`, Access `Global Settings`, Active Period tanggal besok, Join Date 30 hari sebelum hari uji, `YYYY-MM-DD`); `user-login-ap-hari-ini.csv` (header First Name,Last Name,Email,Division,Access,Active Period; 1 baris, Email unik, Division `Engineering`, Access `Global Settings`, Active Period tanggal hari ini menurut zona Client E); `user-login-ap-besok.csv` (isi sama dengan Email unik lain dan Active Period tanggal besok menurut zona Client E).
- Cleanup (hook `after`): draft User Login Client E dibuang lewat skrip reset; jam server dan jam browser dipulihkan; fixture master data dan Custom Field dipulihkan ke Pre-setup (R2).
- State global: jam server dan jam browser (dipulihkan), flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Tanggal mentah (TC-GS-IMPORT-486)

1. Pindah ke Sub-Tab User Login
2. Klik `[Upload File]` dan pilih berkas `user-login-date.csv`
3. Klik `[Confirm Mapping]`
4. Verifikasi sel Active Period menampilkan tanggal besok persis seperti isi berkas dalam bentuk `YYYY-MM-DD`
5. Verifikasi sel Active Period tidak menampilkan bentuk `dd MMM yy`
6. Verifikasi sel Join Date menampilkan tanggal 30 hari sebelum hari uji persis seperti isi berkas dalam bentuk `YYYY-MM-DD`
7. Verifikasi sel Join Date tidak menampilkan bentuk `dd MMM yy`
8. Reset draft Tab User Login Client E lewat skrip reset, lalu muat ulang halaman dan buka Sub-Tab User Login

### Batas Active Period menurut zona waktu (TC-GS-IMPORT-529)

9. Atur jam server dan jam browser ke 01:30 waktu lokal Client E (UTC+7) pada hari uji
10. Klik `[Upload File]`
11. Pilih berkas `user-login-ap-hari-ini.csv`
12. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
13. Verifikasi Modal Column Mapping tetap terbuka
14. Verifikasi Error Banner berheader "1 row couldn't be imported. Fix the following and upload again:"
15. Verifikasi Error Banner memuat baris pesan `Active Period: Please select a future date. 1`
16. Verifikasi tidak ada baris masuk Staging Table
17. Klik `[Reupload File]`
18. Pilih berkas `user-login-ap-besok.csv`
19. Klik `[Confirm Mapping]` tanpa mengubah dropdown File Column dari hasil auto-match
20. Verifikasi modal tertutup
21. Verifikasi muncul toast sukses: "Success, row has been added."
22. Verifikasi Staging Table memuat 1 baris berstatus `pending`
23. Verifikasi baris itu menampilkan Active Period tanggal besok menurut zona waktu Client E
24. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-GS-IMPORT-486 lebih dulu karena tidak mengubah jam; langkah 8 mereset draft karena TC-GS-IMPORT-529 mensyaratkan tanpa draft Tab User Login (S-03, S-09).
- Langkah 24 memulihkan jam sebagai aksi tanpa `Verifikasi` (S-09).
- Temuan untuk QA:
  - TC-GS-IMPORT-529 hasilnya bergantung pada jam saat run (dekat tengah malam UTC+7 terhadap UTC); spec mengatur jam server dan jam browser ke 01:30 UTC+7 sesuai Precondition d agar deterministik. Mekanisme pengaturan jam (fixture jam server, emulasi jam browser) disediakan tim FE/BE.
  - TC-GS-IMPORT-486 dan 529 Data Uji menulis Email sebagai "Email unik" tanpa nilai; spec memakai suffix per run.
  - TC-GS-IMPORT-529 Post Condition (fixture dipulihkan) ditulis sebagai langkah pemulihan, tanpa asersi.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
