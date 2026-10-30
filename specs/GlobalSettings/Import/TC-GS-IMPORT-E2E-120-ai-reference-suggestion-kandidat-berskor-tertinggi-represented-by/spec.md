---
id: TC-GS-IMPORT-E2E-120-ai-reference-suggestion-kandidat-berskor-tertinggi-represented-by
title: "AI Reference Suggestion: kandidat berskor tertinggi, Represented By, Accept tidak membuat record, rename Position setelah staging"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-318
  - TC-GS-IMPORT-320
  - TC-GS-IMPORT-716
  - TC-GS-IMPORT-826
  - TC-GS-IMPORT-827
coverage:
  web: automated
---

# AI Reference Suggestion: kandidat berskor tertinggi, Represented By, Accept tidak membuat record, rename Position setelah staging

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`.
- Pelaku kedua (TC-GS-IMPORT-716): Admin kedua Client C (Oki Setiawan) `totalControlSecond_automated_qaTeam3@qwertysystem.net` hanya lewat sesi API sebagai pemicu rename Position (P-2), password `Spectra.env.GS_CLIENTC_TC2_PASSWORD` (disediakan tim FE).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import; sub-tab dipilih di `## Test Steps`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Pre-setup Client C (tidak diubah spec ini kecuali rename Position pada TC-GS-IMPORT-716 yang dipulihkan): User Login `budi.manager.c@example.com` aktif; Division `Engineering`, `Marketing`, `Finance`, `Warehouse`, `Gudang`; Position `Store Manager`, `Senior Developer`, `Finance Manager`, `Technician`, `Supervisor`. Client C tanpa draft Tab User Login dan User Non Login sebelum tiap TC (fixture reset, Kontrak Fixture R1).
- Data Dinamis (berkas disediakan tim QA, fixture baru `Fixture.import.berkas`): `user-non-login-rep-typo.csv` (1 baris: Ayu Lestari, `ayu.lestari@example.com`, Division `Engineering`, Position kosong, Represented By `budi.manager.c@example.co`), `user-login-div-gudng.csv` (1 baris: Siti Rahmawati, `siti.rahmawati@example.com`, Division `Gudng`), `user-login-technician.csv` (1 baris: Siti Rahmawati, Division `Engineering`, Position `Technician`), `user-login-div-gdng.csv` (1 baris, Division `Gdng`), `user-login-div-gdn5.csv` (1 baris, Division `Gdn5`). Nama dan nilai berkas literal sesuai TC karena menentukan jawaban mock AI (D-42, D-71).
- Kemampuan teknis: mock layanan AI deterministik (D-11, D-40) mode normal dan mode "kandidat dengan skor" (D-71), diatur lewat hook uji non-produksi; pembacaan pagination Division; fixture reset draft client (Kontrak Fixture R1); sesi API Admin kedua untuk rename Position.
- State global yang diubah: mode mock AI (dikembalikan ke normal di akhir TC-GS-IMPORT-827 dan di hook `after`), nama Position `Technician` (dipulihkan setelah TC-GS-IMPORT-716 dan di hook `after`). Suite berjalan serial (`parallel: false`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset draft User Login dan User Non Login Client C, kembalikan Position `Senior Technician` menjadi `Technician`, kembalikan mock AI ke mode normal.

## Test Steps

### TC-GS-IMPORT-318: Represented By mirip akun aktif menampilkan saran tanpa Create Missing, Accept memulihkan baris

1. Pilih sub-tab User Non Login
2. Klik [Upload File] di toolbar dan pilih berkas `user-non-login-rep-typo.csv`
3. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
4. Verifikasi baris #1 berstatus `error`
5. Verifikasi sel Represented By baris #1 menampilkan badge "Did you mean 'budi.manager.c@example.com'?" dengan `[Accept]` dan `[Dismiss]`
6. Verifikasi Error Summary Callout memuat "Represented by must be an active User Login account" dengan badge "1 row"
7. Verifikasi baris pesan Represented By pada Error Summary Callout tidak memuat tombol `[Create Missing Divisions]` maupun `[Create Missing Positions]`
8. Klik `[Accept]` pada badge saran di sel Represented By baris #1
9. Verifikasi sel Represented By baris #1 menampilkan `budi.manager.c@example.com`
10. Verifikasi sel Represented By baris #1 tanpa border `danger`
11. Verifikasi badge saran pada sel Represented By baris #1 hilang
12. Verifikasi baris #1 berstatus `pending`
13. Reset draft User Non Login Client C lewat fixture reset

### TC-GS-IMPORT-320: Accept tidak pernah membuat record baru

14. Buka Global Settings > User > Division dan catat jumlah item pada pagination
15. Verifikasi tabel Division menampilkan 5 baris
16. Buka Import dan pilih sub-tab User Login
17. Klik [Upload File] di toolbar dan pilih berkas `user-login-div-gudng.csv`
18. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
19. Klik `[Accept]` pada badge `Did you mean 'Gudang'?` di sel Division baris #1
20. Tunggu aksi selesai (permintaan mendapat respons)
21. Buka Global Settings > User > Division dan perhatikan daftar Division
22. Verifikasi tabel Division menampilkan 5 baris
23. Verifikasi tabel Division tidak memuat `Gudng`
24. Reset draft User Login Client C lewat fixture reset

### TC-GS-IMPORT-716: Position di-rename setelah staging, baris menjadi error dan menampilkan saran Reference

25. Buka Import > User Login
26. Klik [Upload File] di toolbar dan pilih berkas `user-login-technician.csv`
27. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
28. Verifikasi baris #1 berstatus `pending`
29. Verifikasi Staging Metric Cards: Total Rows 1, Ready to Import 1, Errors 0
30. Admin kedua Client C (sesi API): ubah Position Name `Technician` menjadi `Senior Technician` hingga tersimpan
31. Muat ulang halaman Import > User Login
32. Verifikasi baris #1 berstatus `error`
33. Verifikasi sel Position baris #1 menampilkan badge "Did you mean 'Senior Technician'?" disertai `[Accept]` dan `[Dismiss]`
34. Verifikasi Error Summary Callout memuat "Position not found" dengan badge "1 row"
35. Verifikasi baris pesan "Position not found" memuat `[Create Missing Positions]`
36. Admin kedua Client C (sesi API): kembalikan Position Name `Senior Technician` menjadi `Technician` hingga tersimpan, lalu reset draft User Login Client C lewat fixture reset dan muat ulang halaman Import > User Login

### TC-GS-IMPORT-826: Badge memakai kandidat berskor tertinggi yang memenuhi ambang, Accept menerapkan peringkat 1

37. Atur mock layanan AI ke mode "kandidat dengan skor" (D-71)
38. Klik [Upload File] di toolbar
39. Pilih berkas `user-login-div-gdng.csv` di file picker
40. Biarkan seluruh dropdown File Column pada nilai auto-match
41. Klik [Confirm Mapping]
42. Verifikasi baris #1 berstatus `error`
43. Verifikasi sel Division baris #1 menampilkan satu badge inline "Did you mean 'Marketing'?" disertai `[Accept]` dan `[Dismiss]`
44. Verifikasi badge tidak menampilkan `Warehouse` maupun `Gudang`
45. Klik `[Accept]` pada badge `Did you mean 'Marketing'?` di sel Division baris #1
46. Verifikasi sel Division baris #1 berisi `Marketing`
47. Verifikasi baris #1 berstatus `pending`
48. Verifikasi Staging Metric Cards: Total Rows 1 (Active), Ready to Import 1, Errors 0 (Disabled), Duplicates 0 (Disabled)
49. Reset draft User Login Client C lewat fixture reset, lalu muat ulang halaman Import > User Login

### TC-GS-IMPORT-827: Lima kandidat memenuhi ambang menghasilkan satu badge kandidat berskor tertinggi, Accept menerapkannya

50. Klik [Upload File] di toolbar
51. Pilih berkas `user-login-div-gdn5.csv` di file picker
52. Biarkan seluruh dropdown File Column pada nilai auto-match
53. Klik [Confirm Mapping]
54. Verifikasi baris #1 berstatus `error`
55. Verifikasi sel Division baris #1 menampilkan satu badge inline "Did you mean 'Engineering'?" disertai `[Accept]` dan `[Dismiss]`
56. Verifikasi badge tidak menampilkan `Finance`, `Gudang`, `Warehouse`, maupun `Marketing`
57. Klik `[Accept]` pada badge `Did you mean 'Engineering'?` di sel Division baris #1
58. Verifikasi sel Division baris #1 berisi `Engineering`
59. Verifikasi baris #1 berstatus `pending`
60. Verifikasi Staging Metric Cards: Total Rows 1 (Active), Ready to Import 1, Errors 0 (Disabled), Duplicates 0 (Disabled)
61. Kembalikan mock layanan AI ke mode normal, lalu reset draft User Login Client C lewat fixture reset

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Subjudul `###` memetakan langkah ke id TC.
- Urutan: TC-GS-IMPORT-318, 320, 716 (mock mode normal) lalu 826, 827 (mode D-71), supaya mode mock berubah sekali. Rename Position TC-GS-IMPORT-716 dipulihkan di langkah 36 sebelum TC berikutnya (R2).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 16, 25 (memilih atau membuka sub-tab), 13, 24, 36, 49, 61 (reset draft dan pemulihan state, S-09; sesudah reset pada 36 dan 49 halaman Import > User Login dimuat ulang, pada 24 halaman Import dibuka sesudahnya), 14 (mencatat jumlah awal Division), 30 dan 36 (pemicu Admin kedua), 37 dan 61 (mode mock), 20 (Tunggu aksi selesai (permintaan mendapat respons) sesudah `[Accept]` dan sebelum pindah ke Global Settings > User > Division; penanda aman karena TC tidak menyebut penanda teramati). Langkah 21 membuka Division untuk observasi.
- P-2: Admin kedua Client C hanya memicu rename Position lewat sesi API pada TC-GS-IMPORT-716; sesi UI kedua tidak diasersi. TC sumber memakai tab peramban kedua dengan akun yang sama (langkah 3-6 TC) lewat UI Position; spec memakai sesi API Admin kedua sesuai keputusan 2026-10-21 (pelaku kedua yang hanya memicu).
- Staging Metric Cards pada langkah 48 dan 60 diverifikasi sebagai satu daftar utuh (kartu sejenis).
- Spec melewati sekitar 35 langkah (60 langkah): lima blok berdiri sendiri, satu kelas harness (mock AI), tiap blok memakai draft dan reset sendiri; kegagalan satu blok tidak menghilangkan makna blok lain.
- Pembagian TC lintas spec: TC-GS-IMPORT-318 dan 716 ada di spec ini; TC-GS-IMPORT-319, 713, 714, 715 (Tab tanpa Reference Suggestion) ada di spec 121. TC-GS-IMPORT-322 (rename Division lalu commit) ada di spec 140.
- Temuan untuk QA:
  - TC-GS-IMPORT-320 tidak menulis penanda selesainya `[Accept]` sebelum pindah ke Global Settings > User > Division; langkah 20 memakai penanda "permintaan mendapat respons" tanpa menebak hasil UI.
  - TC-GS-IMPORT-716: langkah 3-5 TC memakai tab peramban kedua dengan akun yang sama lewat UI, padahal Kontrak Fixture R5 menyediakan `Admin kedua Client C`; spec memakai Admin kedua sesi API (P-2). Cara rename Position lewat API tidak ditulis di TC (disediakan tim FE/BE, tanpa endpoint karangan).
  - Berkas `user-non-login-rep-typo.csv`, `user-login-div-gudng.csv`, `user-login-technician.csv`, `user-login-div-gdng.csv`, dan `user-login-div-gdn5.csv` tidak didefinisikan di Data Dinamis; isinya diturunkan dari kolom Data Uji TC.
  - Mekanisme reset draft client (Kontrak Fixture R1) tidak ditulis konkret; disediakan tim FE/BE.
  - TC-GS-IMPORT-320: Post Condition (draft berisi 1 baris `pending` dengan Division `Gudang`) tidak punya langkah observasi sehingga tidak diasersi.
  - TC-GS-IMPORT-716: Post Condition (Position berganti nama, draft berisi 1 baris `error`) tidak punya langkah observasi tersendiri dan tidak diasersi.
