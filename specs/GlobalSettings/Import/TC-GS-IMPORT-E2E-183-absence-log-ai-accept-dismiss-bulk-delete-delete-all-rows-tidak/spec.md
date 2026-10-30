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
- Pre-setup Client C: Division `Gudang` dan `Engineering` ada di master Division (dipakai langkah 7, 9, dan 10 sebagai hasil Accept; tidak diubah spec).
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
3. Tutup modal Changelog Import
4. Buka System Log pada Detail User Rudi Hartanto (Tab System Log) dan catat angka total pada teks Pagination sebagai baseline System Log
5. Buka Activity Log (Global Settings > Activity Log) pada tab User Action dan catat angka total pada teks Pagination sebagai baseline Activity Log
6. Buka halaman Import > User Login
7. Klik `[Accept]` pada badge saran Division baris #1
8. Klik `[Dismiss]` pada badge saran Division baris #2
9. Verifikasi sel Division baris #1 menampilkan `Gudang`
10. Verifikasi badge saran pada baris #2 hilang
11. Buka Changelog Import dan baca angka total pada teks Pagination
12. Verifikasi total Changelog Import sama dengan baseline langkah 2
13. Tutup modal Changelog Import
14. Buka System Log pada Detail User Rudi Hartanto (Tab System Log) dan baca angka total
15. Verifikasi total System Log sama dengan baseline langkah 4
16. Buka Activity Log pada tab User Action dan baca angka total
17. Verifikasi total Activity Log sama dengan baseline langkah 5

### TC-GS-IMPORT-753: Bulk Delete

18. Reset Client C ke tanpa draft pada Sub-Tab User Login dan Brand, lalu seed draft Brand `brand-c-3.csv` (3 baris: 1 `pending`, 2 `error`) lewat skrip fixture
19. Buka halaman Import > Brand
20. Buka Changelog Import dan catat angka total pada teks Pagination sebagai baseline Changelog
21. Tutup modal Changelog Import
22. Buka System Log pada Detail User Rudi Hartanto (Tab System Log) dan catat angka total sebagai baseline System Log
23. Buka Activity Log pada tab User Action dan catat angka total sebagai baseline Activity Log
24. Buka halaman Import > Brand
25. Centang baris #1
26. Centang baris #2
27. Klik `[Bulk Action ▾]`
28. Klik `[Delete]` pada overlay
29. Klik `[Delete]` pada dialog Delete Rows
30. Verifikasi toast sukses "Success, row has been deleted." tampil
31. Verifikasi kartu Total Rows menampilkan 1
32. Buka Changelog Import dan baca angka total pada teks Pagination
33. Verifikasi total Changelog Import sama dengan baseline langkah 20
34. Tutup modal Changelog Import
35. Buka System Log pada Detail User Rudi Hartanto (Tab System Log) dan baca angka total
36. Verifikasi total System Log sama dengan baseline langkah 22
37. Buka Activity Log pada tab User Action dan baca angka total
38. Verifikasi total Activity Log sama dengan baseline langkah 23

### TC-GS-IMPORT-754: Delete All Rows

39. Reset Client C ke tanpa draft pada Sub-Tab Brand, lalu seed draft Brand `brand-c-3.csv` (3 baris: 1 `pending`, 2 `error`) lewat skrip fixture
40. Buka halaman Import > Brand
41. Buka Changelog Import dan catat angka total pada teks Pagination sebagai baseline Changelog
42. Tutup modal Changelog Import
43. Buka System Log pada Detail User Rudi Hartanto (Tab System Log) dan catat angka total sebagai baseline System Log
44. Buka Activity Log pada tab User Action dan catat angka total sebagai baseline Activity Log
45. Buka halaman Import > Brand
46. Klik `[Delete All Rows]` pada baris pesan Error Summary Callout "Brand Name: Max. 120 characters"
47. Verifikasi toast sukses "Success, row has been deleted." tampil
48. Verifikasi kartu Total Rows menampilkan 1
49. Verifikasi Error Summary Callout tidak tampil
50. Buka Changelog Import dan baca angka total pada teks Pagination
51. Verifikasi total Changelog Import sama dengan baseline langkah 41
52. Tutup modal Changelog Import
53. Buka System Log pada Detail User Rudi Hartanto (Tab System Log) dan baca angka total
54. Verifikasi total System Log sama dengan baseline langkah 43
55. Buka Activity Log pada tab User Action dan baca angka total
56. Verifikasi total Activity Log sama dengan baseline langkah 44

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: asersi absence (g); setiap TC memuat aksi nyata (AI Accept dan Dismiss, Bulk Delete, Delete All Rows) dengan baseline tiga surface sendiri, sehingga memenuhi S-05. Mock AI hanya pemicu badge saran (P-5a).
- Alasan melewati sekitar 35 langkah (56 langkah nominal): tiga blok homogen satu kelas (absence log) yang berdiri sendiri dengan reset draft Client C di awal tiap blok. Sebagian besar langkah adalah blok baca-log berpola (buka surface, catat atau baca total, `Verifikasi` sama dengan baseline) yang tidak dihitung sebagai smell (bagian 3 konvensi). TC-GS-IMPORT-754 diletakkan terakhir (aksi yang menghapus data di akhir).
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 18, 39), pembukaan surface dan pencatatan baseline (langkah 2 sampai 5, 20 sampai 23, 41 sampai 44), penutupan modal Changelog Import sebelum surface berikutnya (langkah 3, 13, 21, 34, 42, 52), pembukaan halaman Import > Brand sebelum Changelog Import yang datang sesudah Activity Log (langkah 19, 40), pembacaan total, dan pembukaan Import > User Login atau Brand. Asersi absence (kesamaan total) didahului Verifikasi hasil aksi (langkah 9 dan 10; langkah 30 dan 31; langkah 47 dan 48) sebagai anchor positif yang terhubung ke pemicu.
- Temuan untuk QA:
  - TC-GS-IMPORT-434 menyebut layanan AI mock menghasilkan saran peringkat 1 "untuk nilai Data Uji"; spec memakai D-42 (`Gudng` menghasilkan `Gudang`, `Enginering` menghasilkan `Engineering`).
  - TC-GS-IMPORT-753 dan TC-GS-IMPORT-754 berbagi data `brand-c-3.csv` dan menyebut draft "direset sebelum TC"; spec mereset dan men-seed ulang tiap blok.
  - TC-GS-IMPORT-434 membaca System Log pada Detail User Rudi Hartanto (Client C) sedangkan TC absence lain (428 sampai 433) membaca Sari Dewi (Client A); sesuai akun aktor tiap TC.
  - Post Condition semua TC di spec ini "-" dan tidak ada keadaan lain yang perlu dipulihkan selain yang dikerjakan hook `after`.
