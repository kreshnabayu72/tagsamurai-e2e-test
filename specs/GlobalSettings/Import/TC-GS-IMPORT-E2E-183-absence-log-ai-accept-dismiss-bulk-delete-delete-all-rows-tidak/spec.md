---
id: TC-GS-IMPORT-E2E-183-absence-log-ai-accept-dismiss-bulk-delete-delete-all-rows-tidak
title: "Absence log: AI Accept/Dismiss, Bulk Delete, Delete All Rows tidak mencatat ke Changelog Import, System Log, Activity Log (Client C)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-434
  - TC-GS-IMPORT-753
  - TC-GS-IMPORT-754
coverage:
  web: automated
---

# Absence log: AI Accept/Dismiss, Bulk Delete, Delete All Rows tidak mencatat ke Changelog Import, System Log, Activity Log (Client C)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): draft Client C dibagikan ke seluruh admin, mode mock AI adalah state global, dan Changelog Import, System Log, serta Activity Log bersifat permanen sehingga asersi memakai baseline jumlah; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client C dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE): mock layanan AI deterministik mode normal D-40 (tabel D-41 dan D-42: `Gudng` menghasilkan saran `Gudang` 0,91; `Enginering` menghasilkan `Engineering` 0,95) sebagai pemicu badge saran (P-2); skrip fixture reset Client C ke tanpa draft pada Sub-Tab User Login dan Brand (Kontrak Fixture R1) dan seeding draft.
- Baseline log (S-12): tiga surface log dicatat sebelum aksi pemicu pertama tiap TC dari teks Pagination "Showing [From] - [To] of [N] items" (0 bila yang tampil adalah empty state): Changelog Import (icon `[Changelog]` di header halaman Import), System Log pada Detail User Rudi Hartanto (Tab System Log), dan Activity Log (Global Settings > Activity Log, tab User Action). Asersi memakai kesamaan total terhadap baseline, bukan angka absolut atau posisi baris.
- Data Dinamis (milik spec ini; draft dibuang oleh reset sehingga nama baris berkas literal sesuai Data Uji TC):
  - `user-login-ai-4.csv` (TC-434): kolom First Name; Last Name; Email; Division; Access; #1 Rahmat Hidayat `rahmat.hidayat@example.com` Division `Gudng` (saran `Gudang`) `Global Settings`; #2 Sekar Ayu `sekar.ayu@example.com` Division `Enginering` (saran `Engineering`); #3 Teguh Prasetyo `teguh.prasetyo@example.com` Engineering; #4 Umi Kulsum `umi.kulsum@example.com` Engineering. Hasil staging: baris #1 dan #2 `error` (Division tidak ditemukan), baris #3 dan #4 `pending`.
  - `brand-c-3.csv` (TC-753, 754): kolom Brand Name; #1 `Nikon` (`pending`), #2 Brand Name 121 karakter huruf `A` (`error`), #3 Brand Name 121 karakter huruf `B` (`error`).
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): kembalikan mock AI ke normal, hapus draft Brand dan User Login Client C, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-434: AI Accept dan Dismiss

1. Reset Client C ke tanpa draft pada Sub-Tab User Login dan Brand, pastikan mock AI mode normal, lalu seed draft User Login `user-login-ai-4.csv` (4 baris: 2 `error`, 2 `pending`) lewat skrip fixture
2. Buka Changelog Import (icon `[Changelog]` di header halaman) dan catat angka total pada teks Pagination sebagai baseline Changelog
3. Buka System Log pada Detail User Rudi Hartanto (Tab System Log) dan catat angka total pada teks Pagination sebagai baseline System Log
4. Buka Activity Log (Global Settings > Activity Log) pada tab User Action dan catat angka total pada teks Pagination sebagai baseline Activity Log
5. Buka halaman Import > User Login
6. Klik `[Accept]` pada badge saran Division baris #1
7. Klik `[Dismiss]` pada badge saran Division baris #2
8. Verifikasi sel Division baris #1 menampilkan `Gudang`
9. Verifikasi badge saran pada baris #2 hilang
10. Buka Changelog Import dan baca angka total pada teks Pagination
11. Verifikasi total Changelog Import sama dengan baseline langkah 2
12. Buka System Log pada Detail User Rudi Hartanto (Tab System Log) dan baca angka total
13. Verifikasi total System Log sama dengan baseline langkah 3
14. Buka Activity Log pada tab User Action dan baca angka total
15. Verifikasi total Activity Log sama dengan baseline langkah 4

### TC-GS-IMPORT-753: Bulk Delete

16. Reset Client C ke tanpa draft pada Sub-Tab User Login dan Brand, lalu seed draft Brand `brand-c-3.csv` (3 baris: 1 `pending`, 2 `error`) lewat skrip fixture
17. Buka Changelog Import dan catat angka total pada teks Pagination sebagai baseline Changelog
18. Buka System Log pada Detail User Rudi Hartanto (Tab System Log) dan catat angka total sebagai baseline System Log
19. Buka Activity Log pada tab User Action dan catat angka total sebagai baseline Activity Log
20. Buka halaman Import > Brand
21. Centang baris #1
22. Centang baris #2
23. Klik `[Bulk Action ▾]`
24. Klik `[Delete]` pada overlay
25. Klik `[Delete]` pada dialog Delete Rows
26. Verifikasi toast sukses "Success, row has been deleted." tampil
27. Verifikasi kartu Total Rows menampilkan 1
28. Buka Changelog Import dan baca angka total pada teks Pagination
29. Verifikasi total Changelog Import sama dengan baseline langkah 17
30. Buka System Log pada Detail User Rudi Hartanto (Tab System Log) dan baca angka total
31. Verifikasi total System Log sama dengan baseline langkah 18
32. Buka Activity Log pada tab User Action dan baca angka total
33. Verifikasi total Activity Log sama dengan baseline langkah 19

### TC-GS-IMPORT-754: Delete All Rows

34. Reset Client C ke tanpa draft pada Sub-Tab Brand, lalu seed draft Brand `brand-c-3.csv` (3 baris: 1 `pending`, 2 `error`) lewat skrip fixture
35. Buka Changelog Import dan catat angka total pada teks Pagination sebagai baseline Changelog
36. Buka System Log pada Detail User Rudi Hartanto (Tab System Log) dan catat angka total sebagai baseline System Log
37. Buka Activity Log pada tab User Action dan catat angka total sebagai baseline Activity Log
38. Buka halaman Import > Brand
39. Klik `[Delete All Rows]` pada baris pesan Error Summary Callout "Brand Name: Max. 120 characters"
40. Verifikasi toast sukses "Success, row has been deleted." tampil
41. Verifikasi kartu Total Rows menampilkan 1
42. Verifikasi Error Summary Callout tidak tampil
43. Buka Changelog Import dan baca angka total pada teks Pagination
44. Verifikasi total Changelog Import sama dengan baseline langkah 35
45. Buka System Log pada Detail User Rudi Hartanto (Tab System Log) dan baca angka total
46. Verifikasi total System Log sama dengan baseline langkah 36
47. Buka Activity Log pada tab User Action dan baca angka total
48. Verifikasi total Activity Log sama dengan baseline langkah 37

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: asersi absence (g); setiap TC memuat aksi nyata (AI Accept dan Dismiss, Bulk Delete, Delete All Rows) dengan baseline tiga surface sendiri, sehingga memenuhi S-05. Mock AI hanya pemicu badge saran (P-5a).
- Alasan melewati sekitar 35 langkah (48 langkah nominal): tiga blok homogen satu kelas (absence log) yang berdiri sendiri dengan reset draft Client C di awal tiap blok. Sebagian besar langkah adalah blok baca-log berpola (buka surface, catat atau baca total, `Verifikasi` sama dengan baseline) yang tidak dihitung sebagai smell (bagian 3 konvensi). TC-GS-IMPORT-754 diletakkan terakhir (aksi yang menghapus data di akhir).
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 16, 34), pembukaan surface dan pencatatan baseline (langkah 2 sampai 4, 17 sampai 19, 35 sampai 37), pembacaan total, dan pembukaan Import > User Login atau Brand. Asersi absence (kesamaan total) didahului Verifikasi hasil aksi (langkah 8 dan 9; langkah 26 dan 27; langkah 40 dan 41) sebagai anchor positif yang terhubung ke pemicu.
- Temuan untuk QA:
  - TC-GS-IMPORT-434 menyebut layanan AI mock menghasilkan saran peringkat 1 "untuk nilai Data Uji"; spec memakai D-42 (`Gudng` menghasilkan `Gudang`, `Enginering` menghasilkan `Engineering`).
  - TC-GS-IMPORT-753 dan TC-GS-IMPORT-754 berbagi data `brand-c-3.csv` dan menyebut draft "direset sebelum TC"; spec mereset dan men-seed ulang tiap blok.
  - TC-GS-IMPORT-434 membaca System Log pada Detail User Rudi Hartanto (Client C) sedangkan TC absence lain (428 sampai 433) membaca Sari Dewi (Client A); sesuai akun aktor tiap TC.
  - Post Condition semua TC di spec ini "-" dan tidak ada keadaan lain yang perlu dipulihkan selain yang dikerjakan hook `after`.
