---
id: TC-GS-IMPORT-E2E-119-ai-reference-suggestion-accept-dan-dismiss-memulihkan-baris-ke-pending
title: "AI Reference Suggestion: Accept dan Dismiss memulihkan baris ke pending, Dismiss lalu sunting, dan Save"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-311
  - TC-GS-IMPORT-312
  - TC-GS-IMPORT-706
  - TC-GS-IMPORT-707
  - TC-GS-IMPORT-708
  - TC-GS-IMPORT-709
coverage:
  web: automated
---

# AI Reference Suggestion: Accept dan Dismiss memulihkan baris ke pending, Dismiss lalu sunting, dan Save

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import (Tab Brand); perpindahan ke Tab User Login dan User Non Login ditulis sebagai langkah penghubung.
- Kondisi awal tiap TC (Kontrak Fixture R1): Client C tanpa draft pada Sub-Tab yang diuji. Skrip reset draft Client C disediakan tim FE/BE; dijalankan di hook `before` dan sebagai langkah penghubung di antara TC.
- Layanan AI: mock deterministik mode normal (Data Dinamis D-40, tabel D-41 dan D-42); hook `before` memastikan mode normal dan hook `after` mengembalikannya ke normal.
- Data Pre-setup yang dibaca (tidak diubah): Division `Gudang`, `Engineering` dan Position `Senior Developer`, `Supervisor` di Client C (master data seperti Client A, R4).
- Data Dinamis (fixture baru `Fixture.import.aiRefAcceptDismiss119`; berkas upload disediakan tim QA, header dan baris sesuai berkas standar D-45):
  - `user-login-div-gudng.csv` (User Login): Siti Rahmawati, `siti.rahmawati@example.com`, Division `Gudng`, Position kosong (TC 311, 312, 709). Nilai pengganti TC 709: `Gudnag`.
  - `user-login-pos-develper.csv` (User Login): Siti Rahmawati, `siti.rahmawati@example.com`, Division `Engineering`, Position `Senior Develper` (TC 706).
  - `user-non-login-div-enginering.csv` (User Non Login): Ayu Lestari, `ayu.lestari@example.com`, Division `Enginering`, Position kosong, Represented By `budi.manager.c@example.com` (TC 707).
  - `user-non-login-pos-supervsor.csv` (User Non Login): Ayu Lestari, `ayu.lestari@example.com`, Division `Engineering`, Position `Supervsor`, Represented By `budi.manager.c@example.com` (TC 708).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset draft Client C pada Sub-Tab User Login dan User Non Login; kembalikan mock AI ke mode normal.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: input upload berkas; mock AI (D-40); skrip reset draft; fixture baca master data Division Client C (disediakan tim FE/BE, endpoint tidak dikarang).
- State global: mock layanan AI (dipulihkan di hook `after`); suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-IMPORT-311: Accept kandidat peringkat 1 pada sel Division Tab User Login

1. Buka Import > User Login
2. Klik [Upload File] di toolbar dan pilih berkas `user-login-div-gudng.csv`
3. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
4. Tunggu sampai toast `Success, row has been added.` tidak tampil lagi
5. Klik `[Accept]` pada badge `Did you mean 'Gudang'?` di sel Division baris #1
6. Verifikasi tidak ada toast baru sesudah klik `[Accept]`
7. Verifikasi sel Division baris #1 berisi `Gudang`
8. Verifikasi baris #1 berstatus `pending`
9. Verifikasi Staging Metric Cards: Total Rows 1
10. Verifikasi Staging Metric Cards: Ready to Import 1
11. Verifikasi Staging Metric Cards: Errors 0
12. Verifikasi footer menampilkan `[Import (1)]`
13. Verifikasi footer tidak menampilkan `[Cancel]` maupun `[Save]` (tidak ada sesi edit)

### TC-GS-IMPORT-706: Accept kandidat peringkat 1 pada sel Position Tab User Login

14. Reset draft Client C Tab User Login lewat skrip reset, lalu muat ulang halaman Import > User Login
15. Klik [Upload File] di toolbar dan pilih berkas `user-login-pos-develper.csv`
16. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
17. Tunggu sampai toast `Success, row has been added.` tidak tampil lagi
18. Klik `[Accept]` pada badge `Did you mean 'Senior Developer'?` di sel Position baris #1
19. Verifikasi tidak ada toast baru sesudah klik `[Accept]`
20. Verifikasi sel Position baris #1 berisi `Senior Developer`
21. Verifikasi baris #1 berstatus `pending`
22. Verifikasi Staging Metric Cards: Total Rows 1
23. Verifikasi Staging Metric Cards: Ready to Import 1
24. Verifikasi Staging Metric Cards: Errors 0
25. Verifikasi footer menampilkan `[Import (1)]`
26. Verifikasi footer tidak menampilkan `[Cancel]` maupun `[Save]` (tidak ada sesi edit)

### TC-GS-IMPORT-312: Dismiss menghilangkan badge dan baris tetap error

27. Reset draft Client C Tab User Login lewat skrip reset, lalu muat ulang halaman Import > User Login
28. Klik [Upload File] di toolbar dan pilih berkas `user-login-div-gudng.csv`
29. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
30. Tunggu sampai toast `Success, row has been added.` tidak tampil lagi
31. Klik `[Dismiss]` pada badge saran sel Division baris #1
32. Verifikasi tidak ada toast baru
33. Verifikasi badge hilang dari sel Division baris #1
34. Verifikasi baris #1 tetap `error`
35. Muat ulang halaman Import > User Login
36. Verifikasi Staging Table menampilkan baris #1 (halaman termuat)
37. Verifikasi badge saran tidak muncul lagi pada nilai sel yang sama
38. Verifikasi baris #1 tetap `error`
39. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "1 row"

### TC-GS-IMPORT-709: Save menyimpan sel yang di-Dismiss lalu disunting menjadi nilai yang tidak ditemukan

40. Reset draft Client C Tab User Login lewat skrip reset, lalu muat ulang halaman Import > User Login
41. Klik [Upload File] di toolbar dan pilih berkas `user-login-div-gudng.csv`
42. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
43. Klik `[Dismiss]` pada badge saran sel Division baris #1
44. Verifikasi badge saran hilang dari sel Division baris #1
45. Klik `⋯` pada baris #1 lalu pilih Edit
46. Ketik `Gudnag` pada sel Division lalu pilih `Use "Gudnag"`
47. Klik `[Save]`
48. Verifikasi toast sukses "Success, row has been updated."
49. Verifikasi sesi edit berakhir dan footer tidak menampilkan `[Cancel]` maupun `[Save]`
50. Verifikasi sel Division baris #1 menampilkan `Gudnag` dengan border `danger`
51. Verifikasi pesan sel "Division 'Gudnag' was not found. Check spelling, or create the missing division from this row."
52. Verifikasi baris #1 berstatus `error`
53. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "1 row"
54. Verifikasi (fixture baca master data Division Client C) Division `Gudang` ada sebagai pembanding
55. Verifikasi (fixture baca master data Division Client C) tidak ada Division `Gudnag`

### TC-GS-IMPORT-707: Accept kandidat peringkat 1 pada sel Division Tab User Non Login

56. Reset draft Client C Tab User Login lewat skrip reset, lalu buka Import > User Non Login
57. Klik [Upload File] di toolbar dan pilih berkas `user-non-login-div-enginering.csv`
58. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
59. Tunggu sampai toast `Success, row has been added.` tidak tampil lagi
60. Klik `[Accept]` pada badge `Did you mean 'Engineering'?` di sel Division baris #1
61. Verifikasi tidak ada toast baru sesudah klik `[Accept]`
62. Verifikasi sel Division baris #1 berisi `Engineering`
63. Verifikasi baris #1 berstatus `pending`
64. Verifikasi Staging Metric Cards: Total Rows 1
65. Verifikasi Staging Metric Cards: Ready to Import 1
66. Verifikasi Staging Metric Cards: Errors 0
67. Verifikasi footer menampilkan `[Import (1)]`
68. Verifikasi footer tidak menampilkan `[Cancel]` maupun `[Save]` (tidak ada sesi edit)

### TC-GS-IMPORT-708: Accept kandidat peringkat 1 pada sel Position Tab User Non Login

69. Reset draft Client C Tab User Non Login lewat skrip reset, lalu muat ulang halaman Import > User Non Login
70. Klik [Upload File] di toolbar dan pilih berkas `user-non-login-pos-supervsor.csv`
71. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
72. Tunggu sampai toast `Success, row has been added.` tidak tampil lagi
73. Klik `[Accept]` pada badge `Did you mean 'Supervisor'?` di sel Position baris #1
74. Verifikasi tidak ada toast baru sesudah klik `[Accept]`
75. Verifikasi sel Position baris #1 berisi `Supervisor`
76. Verifikasi baris #1 berstatus `pending`
77. Verifikasi Staging Metric Cards: Total Rows 1
78. Verifikasi Staging Metric Cards: Ready to Import 1
79. Verifikasi Staging Metric Cards: Errors 0
80. Verifikasi footer menampilkan `[Import (1)]`
81. Verifikasi footer tidak menampilkan `[Cancel]` maupun `[Save]` (tidak ada sesi edit)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`, TC-GS-IMPORT-311, 312, 706 sampai 709.
- Urutan TC sumber diubah: TC Tab User Login (311, 706, 312, 709) lebih dulu lalu Tab User Non Login (707, 708) supaya perpindahan Tab satu kali; TC 709 (sunting dan simpan) setelah TC Dismiss (S-10).
- Spec berisi 81 langkah, di atas sekitar 35 langkah. Alasan: enam TC, tiap TC berdiri sendiri dengan draft barunya dan seluruhnya satu kelas (AI Reference Suggestion, mock normal); kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 56 (pindah Tab), 14, 27, 40, 56, 69 (reset draft; sesudah reset pada 14, 27, 40, 69 halaman Import Tab itu dimuat ulang, pada 56 halaman berpindah Tab), 4, 17, 30, 59, 72 (menunggu toast lama hilang), 35 (muat ulang). Langkah 6, 19, 32, 61, 74 (`Verifikasi` tidak ada toast) ditulis tepat sesudah pemicu `[Accept]` atau `[Dismiss]`, sebelum `Verifikasi` artefak (8b butir 11).
- Langkah 36 adalah anchor positif halaman termuat sebelum asersi absence badge (8b butir 2). Langkah 54 adalah anchor positif sebelum asersi absence Division `Gudnag` (langkah 55).
- Pembagian TC lintas spec: TC-GS-IMPORT-307 sampai 310, 313 sampai 315, 317, 710, 711, 825 ada di spec 118; TC-GS-IMPORT-318, 320, 716, 826, 827 di spec 120; TC-GS-IMPORT-319, 713 sampai 715, 853, 933 di spec 121; Accept AI dari halaman basi saat committing di spec lain (kelas a).
- Temuan untuk QA:
  - TC-GS-IMPORT-709 Expected e ("Tidak ada Division `Gudnag` yang dibuat") tidak menyebut cara cek; spec memakai fixture baca master data Division yang disediakan tim FE/BE, endpoint tidak dikarang (S-11, S-13).
  - Berkas `user-login-div-gudng.csv`, `user-login-pos-develper.csv`, `user-non-login-div-enginering.csv`, `user-non-login-pos-supervsor.csv` didefinisikan hanya pada Data Uji TC pemakai; D-44 tidak memuatnya.
  - TC-GS-IMPORT-311 dan 312 Langkah Uji 3 "Tunggu sampai toast ... tidak tampil lagi" tanpa batas waktu tunggu.
