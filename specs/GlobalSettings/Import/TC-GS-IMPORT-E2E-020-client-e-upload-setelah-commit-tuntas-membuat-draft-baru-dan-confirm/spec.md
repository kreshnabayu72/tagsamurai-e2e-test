---
id: TC-GS-IMPORT-E2E-020-client-e-upload-setelah-commit-tuntas-membuat-draft-baru-dan-confirm
title: "Client E: Upload Setelah Commit Tuntas Membuat Draft Baru, dan Confirm Mapping User Login dan User Non Login dengan Referensi Valid"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-76
  - TC-GS-IMPORT-759
  - TC-GS-IMPORT-760
coverage:
  web: automated
---

# Client E: Upload Setelah Commit Tuntas Membuat Draft Baru, dan Confirm Mapping User Login dan User Non Login dengan Referensi Valid

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena Client E dipakai bergantian dengan spec commit; lihat `suite.md`.
- Akun aktor: Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup; Date Format `dd MMM yy`). Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTE_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk Total Control Client E; perpindahan Sub-Tab ke User Login dan User Non Login ditulis sebagai langkah eksplisit.
- Data:
  - D-19 (a): keadaan Client E setelah commit tuntas, disiapkan skrip fixture tanpa menjalankan commit lewat UI: commit Brand tuntas dengan 0 baris tersisa dan tanpa draft Brand (dipakai sebagai precondition TC, tidak diasersi).
  - Client E tanpa draft Tab User Login dan User Non Login (Kontrak Fixture R1; skrip reset disediakan tim FE/BE).
  - Data master Pre-setup Client E (tidak diubah): Division `Gudang`, `Warehouse`, `Marketing`, `Engineering`, `Finance`; Position `Technician`; User Login aktif `rina.admin.e@example.com`, `budi.manager.e@example.com`, `dewi.anggraini.e@example.com`.
  - Berkas fixture (D-07, isi literal): `brand-6.csv` (header `Brand Name`; Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp); `user-login-ref.csv` (D-62; header `First Name,Last Name,Email,Division,Position,Access`; #1 Budi, Santosa, budi.santosa.ref@example.com, Gudang, Technician, Global Settings; #2 Citra, Wulandari, citra.wulandari.ref@example.com, Warehouse, (kosong), `Global Settings;Fixed Asset`; #3 Dedi, Kurniawan, dedi.kurniawan.ref@example.com, Marketing, (kosong), Global Settings); `user-non-login-ref.csv` (D-63; header `First Name,Last Name,Email,Division,Represented By`; #1 Gita, Permata, gita.permata.ref@example.com, Engineering, budi.manager.e@example.com; #2 Hadi, Pranoto, hadi.pranoto.ref@example.com, Marketing, dewi.anggraini.e@example.com; #3 Indah, Sari, indah.sari.ref@example.com, Finance, dewi.anggraini.e@example.com).
- Cleanup: spec membuat draft Brand (6 baris), User Login (3 baris), dan User Non Login (3 baris) pada Client E; hook `after` membuang ketiga draft dan memulihkan Client E ke keadaan D-19 (Kontrak Fixture R1/R3), tidak berasumsi seeding berhasil penuh.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: file picker; skrip fixture keadaan commit tuntas D-19 dan reset draft (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain draft Client E (dibuang hook).

## Test Steps

### TC-GS-IMPORT-76: Upload setelah commit tuntas tidak menampilkan dialog Append dan membuat draft baru

1. Klik `[Upload File]`
2. Pilih berkas `brand-6.csv` di file picker
3. Perhatikan halaman
4. Verifikasi Modal Column Mapping terbuka
5. Verifikasi tidak ada dialog Confirm Append Draft
6. Klik `[Confirm Mapping]`
7. Perhatikan Staging Table
8. Verifikasi draft baru dibuat dengan 6 baris berstatus `pending`

### TC-GS-IMPORT-759: Confirm Mapping berkas User Login dengan Division, Position, dan Access yang sudah ada menghasilkan 3 baris pending

9. Klik Sub-Tab User Login
10. Klik `[Upload File]`
11. Pilih berkas `user-login-ref.csv`
12. Klik `[Confirm Mapping]`
13. Verifikasi modal tertutup
14. Verifikasi muncul toast sukses "Success, row has been added."
15. Perhatikan Staging Table dan Staging Metric Cards
16. Verifikasi Staging Table menampilkan 3 baris berstatus `pending` dengan Row # 1 sampai 3
17. Verifikasi Staging Metric Cards: Total Rows 3, Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled)
18. Verifikasi Footer menampilkan `[Import (3)]`

### TC-GS-IMPORT-760: Confirm Mapping berkas User Non Login dengan Represented By aktif menghasilkan 3 baris pending

19. Klik Sub-Tab User Non Login
20. Klik `[Upload File]`
21. Pilih berkas `user-non-login-ref.csv`
22. Klik `[Confirm Mapping]`
23. Verifikasi modal tertutup
24. Verifikasi muncul toast sukses "Success, row has been added."
25. Perhatikan Staging Table dan Staging Metric Cards
26. Verifikasi Staging Table menampilkan 3 baris berstatus `pending` dengan Row # 1 sampai 3
27. Verifikasi Staging Metric Cards: Total Rows 3, Ready to Import 3, Errors 0 (Disabled), Duplicates 0 (Disabled)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3, 7, 15, 25 (mengamati sesuai Langkah Uji TC), langkah 9 dan 19 (pindah Sub-Tab). Tiap blok memakai Sub-Tab berbeda sehingga draft satu blok tidak memengaruhi blok lain.
- Temuan untuk QA:
  - TC-GS-IMPORT-76 bergantung pada keadaan "commit tuntas, 0 baris tersisa" (D-19 a) yang disiapkan skrip fixture tanpa commit lewat UI; mekanismenya tidak didefinisikan di TC, PRD, atau LLD dan disediakan tim FE/BE (S-13).
  - TC-GS-IMPORT-759 dan 760 hanya mengasersi Expected a sampai d; tidak ada asersi isi sel Division/Position/Access/Represented By. Spec mengikuti TC.
  - Berkas fixture literal tanpa suffix `{runId}`; keunikan dijaga lewat reset draft.
