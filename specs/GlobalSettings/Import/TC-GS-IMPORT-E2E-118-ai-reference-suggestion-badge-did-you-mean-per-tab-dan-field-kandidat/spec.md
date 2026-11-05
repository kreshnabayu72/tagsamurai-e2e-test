---
id: TC-GS-IMPORT-E2E-118-ai-reference-suggestion-badge-did-you-mean-per-tab-dan-field-kandidat
title: "AI Reference Suggestion: badge Did you mean per Tab dan field, kandidat peringkat 1, ambang skor, dan kondisi tanpa saran"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-307
  - TC-GS-IMPORT-308
  - TC-GS-IMPORT-309
  - TC-GS-IMPORT-310
  - TC-GS-IMPORT-313
  - TC-GS-IMPORT-314
  - TC-GS-IMPORT-315
  - TC-GS-IMPORT-317
  - TC-GS-IMPORT-710
  - TC-GS-IMPORT-711
  - TC-GS-IMPORT-825
coverage:
  web: automated
---

# AI Reference Suggestion: badge Did you mean per Tab dan field, kandidat peringkat 1, ambang skor, dan kondisi tanpa saran

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import (Tab Brand); perpindahan ke Tab User Login dan User Non Login ditulis sebagai langkah penghubung.
- Kondisi awal tiap TC (Kontrak Fixture R1): Client C tanpa draft pada Sub-Tab yang diuji. Skrip reset draft Client C disediakan tim FE/BE; dijalankan di hook `before` dan sebagai langkah penghubung di antara TC.
- Layanan AI: mock deterministik (Data Dinamis D-40, tabel D-42; mode kandidat berskor D-71) yang diatur tim QA/BE lewat hook uji. Mode normal untuk TC 307 sampai 710; mode tunda 3 detik (D-40) untuk TC 711; mode kandidat berskor D-71 untuk TC 825. Mode diubah di langkah kasus dan dikembalikan ke normal di hook `after`.
- Data Pre-setup yang dibaca (tidak diubah): Division `Gudang`, `Warehouse`, `Engineering`, Position `Senior Developer`, `Supervisor` di Client C (master data seperti Client A, R4).
- Data Dinamis (fixture baru `Fixture.import.aiReference118`; berkas upload disediakan tim QA):
  - Berkas User Login standar (D-45), 1 baris data Siti Rahmawati (`siti.rahmawati@example.com`), Position kosong, kecuali disebut lain: `user-login-div-gudng.csv` (Division `Gudng`; dipakai TC 307 dan 711), `user-login-pos-develper.csv` (Division `Engineering`, Position `Senior Develper`), `user-login-div-gudg.csv` (Division `Gudg`), `user-login-div-alpa.csv` (Division `Alpa Team`), `user-login-div-xyz.csv` (Division `Xyz`), `user-login-div-logistik.csv` (Division `Logistik`), `user-login-div-gudn.csv` (Division `Gudn`), `user-login-div-gudx.csv` (Division `Gudx`).
  - Berkas User Non Login standar (D-45), 1 baris data Ayu Lestari (`ayu.lestari@example.com`), Represented By `budi.manager.c@example.com`: `user-non-login-div-enginering.csv` (Division `Enginering`, Position kosong), `user-non-login-pos-supervsor.csv` (Division `Engineering`, Position `Supervsor`).
  - Master data tambahan TC 314 (D-43): Division `alpha team` dan `Beta Team` di Client C, dibuat lewat API di langkah TC 314 dan dihapus kembali di hook `after`. Nama literal tanpa suffix karena hasil urutan ascending tidak peka huruf besar-kecil bergantung pada nama itu dan nama itu sama persis dengan mock D-42 (pengecualian nama literal S-12: seeding idempotent, dilewati bila sudah ada, cleanup hanya menghapus yang dibuat spec ini, suite serial).
  - Jawaban mock D-42: `Gudng` -> `Gudang` 0,91; `Gudg` -> `Gudang` 0,91, `Warehouse` 0,86, `Engineering` 0,84; `Gudn` -> `Gudang` 0,80; `Alpa Team` -> `Beta Team` 0,88, `alpha team` 0,88; `Enginering` -> `Engineering` 0,95; `Senior Develper` -> `Senior Developer` 0,93; `Supervsor` -> `Supervisor` 0,92; `Xyz` dan `Logistik` -> tanpa kandidat. Mock D-71: `Gudx` -> `Gudang` 0,79.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): reset draft Client C pada Sub-Tab User Login dan User Non Login; hapus Division `alpha team` dan `Beta Team` bila dibuat spec ini; kembalikan mock AI ke mode normal.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: input upload berkas; mock AI (D-40, D-71); skrip reset draft; sesi API untuk membuat dan menghapus Division D-43.
- State global: mock layanan AI (dipulihkan di hook `after`); suite berjalan serial (`parallel: false`).

## Test Steps

### Tab User Login, mode mock normal

#### TC-GS-IMPORT-307: badge pada sel Division tidak ditemukan

1. Buka Import > User Login
2. Klik [Upload File] di Dropzone dan pilih berkas `user-login-div-gudng.csv`
3. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
4. Verifikasi baris #1 berstatus `error`
5. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "1 row"
6. Perhatikan sel Division pada baris #1
7. Verifikasi sel Division baris #1 menampilkan badge inline "Did you mean 'Gudang'?" disertai `[Accept]` dan `[Dismiss]`
8. Verifikasi baris #1 tetap `error`
9. Verifikasi sel Division tetap `Gudng`

#### TC-GS-IMPORT-308: badge pada sel Position tidak ditemukan

10. Reset draft Client C Tab User Login lewat skrip reset, lalu muat ulang halaman Import > User Login
11. Klik [Upload File] di Dropzone dan pilih berkas `user-login-pos-develper.csv`
12. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
13. Verifikasi baris #1 berstatus `error`
14. Verifikasi Error Summary Callout memuat "Position not found" dengan badge "1 row"
15. Perhatikan sel Position pada baris #1
16. Verifikasi sel Position baris #1 menampilkan badge inline "Did you mean 'Senior Developer'?" disertai `[Accept]` dan `[Dismiss]`
17. Verifikasi baris #1 tetap `error`
18. Verifikasi sel Position tetap `Senior Develper`

#### TC-GS-IMPORT-313: tiga kandidat memenuhi ambang, badge hanya peringkat 1

19. Reset draft Client C Tab User Login lewat skrip reset, lalu muat ulang halaman Import > User Login
20. Klik [Upload File] di Dropzone
21. Pilih berkas `user-login-div-gudg.csv` di file picker
22. Biarkan seluruh dropdown File Column pada nilai auto-match
23. Klik [Confirm Mapping]
24. Perhatikan sel Division baris #1
25. Verifikasi sel Division baris #1 menampilkan satu badge inline "Did you mean 'Gudang'?" disertai `[Accept]` dan `[Dismiss]`
26. Verifikasi badge tidak menampilkan `Warehouse`
27. Verifikasi badge tidak menampilkan `Engineering`

#### TC-GS-IMPORT-314: kandidat berkemiripan seri diurutkan ascending tidak peka huruf besar-kecil

28. Reset draft Client C Tab User Login lewat skrip reset
29. Buat Division `alpha team` dan `Beta Team` di Client C lewat sesi API hingga tersimpan (D-43), lalu muat ulang halaman Import > User Login
30. Klik [Upload File] di Dropzone dan pilih berkas `user-login-div-alpa.csv`
31. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
32. Perhatikan sel Division baris #1
33. Verifikasi sel Division baris #1 menampilkan badge inline "Did you mean 'alpha team'?" disertai `[Accept]` dan `[Dismiss]`
34. Verifikasi badge tidak menampilkan `Beta Team`

#### TC-GS-IMPORT-315: tanpa kandidat berkemiripan 0,8 atau lebih, tanpa badge

35. Reset draft Client C Tab User Login lewat skrip reset, lalu muat ulang halaman Import > User Login
36. Klik [Upload File] di Dropzone dan pilih berkas `user-login-div-xyz.csv`
37. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
38. Verifikasi baris #1 berstatus `error`
39. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "1 row"
40. Perhatikan sel Division baris #1
41. Verifikasi sel Division baris #1 tidak menampilkan badge saran

#### TC-GS-IMPORT-317: tanpa kandidat memadai, Create Missing tersedia di Callout dan menu row action

42. Reset draft Client C Tab User Login lewat skrip reset, lalu muat ulang halaman Import > User Login
43. Klik [Upload File] di Dropzone dan pilih berkas `user-login-div-logistik.csv`
44. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
45. Perhatikan sel Division baris #1 dan Error Summary Callout
46. Verifikasi sel Division baris #1 tidak menampilkan badge saran
47. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "1 row" dan `[Create Missing Divisions]`
48. Klik `⋯` pada baris #1
49. Verifikasi menu `⋯` baris #1 memuat `[Create Missing Divisions]`
50. Tutup menu `⋯` baris #1 (Esc)

#### TC-GS-IMPORT-710: kemiripan tepat 0,8 ditampilkan sebagai saran

51. Reset draft Client C Tab User Login lewat skrip reset, lalu muat ulang halaman Import > User Login
52. Klik [Upload File] di Dropzone dan pilih berkas `user-login-div-gudn.csv`
53. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
54. Verifikasi baris #1 berstatus `error`
55. Perhatikan sel Division baris #1
56. Verifikasi sel Division baris #1 menampilkan badge inline "Did you mean 'Gudang'?" disertai `[Accept]` dan `[Dismiss]`

### Tab User Non Login, mode mock normal

#### TC-GS-IMPORT-309: badge pada sel Division tidak ditemukan

57. Reset draft Client C Tab User Login lewat skrip reset, lalu muat ulang halaman Import > User Non Login
58. Klik [Upload File] di Dropzone dan pilih berkas `user-non-login-div-enginering.csv`
59. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
60. Verifikasi baris #1 berstatus `error`
61. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "1 row"
62. Perhatikan sel Division pada baris #1
63. Verifikasi sel Division baris #1 menampilkan badge inline "Did you mean 'Engineering'?" disertai `[Accept]` dan `[Dismiss]`
64. Verifikasi baris #1 tetap `error`
65. Verifikasi sel Division tetap `Enginering`

#### TC-GS-IMPORT-310: badge pada sel Position tidak ditemukan

66. Reset draft Client C Tab User Non Login lewat skrip reset, lalu muat ulang halaman Import > User Non Login
67. Klik [Upload File] di Dropzone dan pilih berkas `user-non-login-pos-supervsor.csv`
68. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
69. Verifikasi baris #1 berstatus `error`
70. Verifikasi Error Summary Callout memuat "Position not found" dengan badge "1 row"
71. Perhatikan sel Position pada baris #1
72. Verifikasi sel Position baris #1 menampilkan badge inline "Did you mean 'Supervisor'?" disertai `[Accept]` dan `[Dismiss]`
73. Verifikasi baris #1 tetap `error`
74. Verifikasi sel Position tetap `Supervsor`

### Tab User Login, mode mock lain

#### TC-GS-IMPORT-711: respons AI dalam 3 detik tetap bersaran

75. Reset draft Client C Tab User Non Login lewat skrip reset, lalu muat ulang halaman Import > User Login
76. Atur mock layanan AI ke mode tunda 3 detik (D-40)
77. Klik [Upload File] di Dropzone dan pilih berkas `user-login-div-gudng.csv`
78. Biarkan seluruh dropdown File Column pada nilai auto-match, klik [Confirm Mapping]
79. Tunggu 4 detik (jeda nyata pendek sesuai batas TC)
80. Perhatikan sel Division baris #1
81. Verifikasi sel Division baris #1 menampilkan badge inline "Did you mean 'Gudang'?" disertai `[Accept]` dan `[Dismiss]`
82. Verifikasi baris #1 tetap `error`

#### TC-GS-IMPORT-825: kandidat berskor 0,79 di bawah ambang, tanpa badge, Create Missing tersedia

83. Reset draft Client C Tab User Login lewat skrip reset, lalu muat ulang halaman Import > User Login
84. Atur mock layanan AI ke mode kandidat berskor (D-71)
85. Klik [Upload File] di Dropzone
86. Pilih berkas `user-login-div-gudx.csv` di file picker
87. Biarkan seluruh dropdown File Column pada nilai auto-match
88. Klik [Confirm Mapping]
89. Verifikasi baris #1 berstatus `error`
90. Perhatikan sel Division baris #1 dan Error Summary Callout
91. Verifikasi sel Division baris #1 tidak menampilkan badge saran
92. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "1 row" beserta `[Create Missing Divisions]`
93. Kembalikan mock layanan AI ke mode normal (D-71 dipulihkan)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`, TC-GS-IMPORT-307 sampai 310, 313 sampai 315, 317, 710, 711, 825.
- Urutan TC sumber: TC 311 dan 312 (Accept dan Dismiss) ada di spec 119; di spec ini pengelompokan menurut Tab dan mode mock (mode normal lebih dulu, mode tunda 3 detik dan D-71 sesudahnya) supaya mode mock diubah seminimal mungkin (S-10).
- Spec berisi 93 langkah, di atas sekitar 35 langkah. Alasan: sebelas TC, tiap TC berdiri sendiri dengan draft barunya dan memverifikasi satu kondisi badge; seluruhnya satu kelas (AI Reference Suggestion, mock deterministik) dan kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 57, 75 (pindah Tab), 10, 19, 28, 35, 42, 51, 66, 83 (reset draft; sesudah reset pada 10, 19, 35, 42, 51, 66, 83 halaman Import Tab itu dimuat ulang, sedangkan pemuatan ulang sesudah reset 28 dilakukan di langkah 29), 29 (seed D-43 lalu muat ulang halaman Import > User Login), 50 (tutup menu), 76 dan 84 (atur mode mock), 79 (jeda nyata 4 detik sesuai TC), 93 (pulihkan mock).
- Create Missing hanya diamati ketersediaannya pada TC 317 dan 825 (tidak dijalankan); perilaku Create Missing ada di spec 122 sampai 130.
- Pembagian TC lintas spec: TC-GS-IMPORT-311, 312, 706 sampai 709 ada di spec 119; TC-GS-IMPORT-318, 320, 716, 826, 827 di spec 120; TC-GS-IMPORT-319, 713 sampai 715, 853, 933 di spec 121.
- Temuan untuk QA:
  - Berkas `user-login-div-gudng.csv`, `user-login-pos-develper.csv`, `user-login-div-gudg.csv`, `user-login-div-alpa.csv`, `user-login-div-xyz.csv`, `user-login-div-logistik.csv`, `user-login-div-gudn.csv`, `user-login-div-gudx.csv`, `user-non-login-div-enginering.csv`, `user-non-login-pos-supervsor.csv` didefinisikan hanya pada Data Uji TC pemakai; D-44 tidak memuatnya.
  - TC-GS-IMPORT-313 menggabungkan Langkah Uji 1 sampai 4 secara terpisah (klik Upload File, pilih berkas, auto-match, Confirm Mapping) sedangkan TC lain menggabungkannya; tidak mengubah hasil.
  - TC-GS-IMPORT-314: urutan jawaban mock (`Beta Team` lebih dulu) disebut hanya di Data Uji; spec mengasersi hasil akhir `alpha team` tanpa mengasersi urutan jawaban mock.
  - TC-GS-IMPORT-711: "Tunggu 4 detik" adalah jeda nyata pendek yang melampaui batas ±30 detik tidak; dipertahankan sesuai TC.
  - TC-GS-IMPORT-317 dan 825 Expected menyebut `[Create Missing Divisions]` pada Error Summary Callout; label tombol mengikuti TC.
