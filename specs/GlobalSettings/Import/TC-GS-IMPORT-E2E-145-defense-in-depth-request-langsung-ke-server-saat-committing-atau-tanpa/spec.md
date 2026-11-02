---
id: TC-GS-IMPORT-E2E-145-defense-in-depth-request-langsung-ke-server-saat-committing-atau-tanpa
title: "Defense-in-depth: request langsung ke server saat committing atau tanpa draft ditolak (conflict atau not found), data tidak berubah"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-381
  - TC-GS-IMPORT-383
  - TC-GS-IMPORT-384
  - TC-GS-IMPORT-704
  - TC-GS-IMPORT-729
  - TC-GS-IMPORT-730
  - TC-GS-IMPORT-739
  - TC-GS-IMPORT-746
  - TC-GS-IMPORT-918
coverage:
  web: automated
---

# Defense-in-depth: request langsung ke server saat committing atau tanpa draft ditolak (conflict atau not found), data tidak berubah

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): draft Import dibagikan ke seluruh admin satu client, Client E dipakai bersama spec commit lain, dan spec mengubah state global (kontrol worker commit, mode mock AI, jam server); lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client E dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; tidak didefinisikan di PRD atau LLD selain yang disebut TC):
  - Klien HTTP yang mengirim request langsung ke server dengan token sesi Total Control Client E (Upload, AI Accept, AI Dismiss, memulai sesi edit, Accept, Create Missing Divisions, Create Missing Positions, Import, Discard Draft, Create Missing Options). Pengenal baris diambil dari respons pembacaan Staging Table.
  - Kontrol worker commit D-47 (mode 1: dijeda sebelum job mulai; mode 2: dijeda di dalam batch pertama sesudah uji ulang late-binding dan sebelum batch selesai) di lingkungan non-produksi. Tidak ada record master data yang tercipta karena worker dijeda sebelum batch selesai.
  - Skrip fixture reset Client E (D-47: hapus draft, lanjutkan worker, hapus hasil commit) dan seeding draft Client E.
  - Hook umur draft D-76 varian 1 (>=24 jam) untuk TC-746.
  - Mock layanan AI mode normal D-40 (tabel D-41 dan D-42) untuk TC-383, TC-704.
- Data Dinamis (milik spec ini; draft Client E dibuang oleh reset sehingga nama baris berkas literal sesuai Data Uji TC dan tidak ada record master data tercipta):
  - D-56 `brand-250-impor.csv`: 250 baris `Brand Impor 001` sampai `Brand Impor 250`, semua `pending`.
  - D-57 `brand-250-mixed.csv`: 248 `pending`, baris #5 `error` (Brand Name 121 karakter, nilai sumber Brand pertama tabel D-41, badge saran AI `Samsung Electronics Indonesia`), baris #20 `duplicate` (`Samsung`).
  - `brand-append-6.csv`: kolom Brand Name; `Nikon`, `Pentax`, `Olympus`, `Fujifilm`, `Leica`, `Sigma`.
  - D-44 `brand-ai-commit.csv`: kolom Brand Name; `Lenovo`, `Dell`, nilai sumber Brand D-41 (121 karakter).
  - D-45 `user-login-commit-logistik.csv` dan `user-login-commit-store-supervisor.csv` (3 baris, isi pada langkah TC-729 dan TC-730) serta D-86 `user-login-commit-shift.csv` (Shift `Pagi` baris #1, `Lembur` baris #2 dan #3).
  - Pre-setup Client E: Division 5 item dan Position 5 item (tanpa `Logistik` dan `Store Supervisor`); Custom Field `Shift` (Dropdown) dengan opsi `Pagi`, `Siang`, `Malam`.
- State global yang diubah: kontrol worker commit (dijeda), mode mock AI, draft dan job Client E. Pemulihan di hook `after` (tetap jalan walau spec gagal): lanjutkan worker commit, kembalikan mock AI ke normal, hapus draft Client E, pulihkan jam bila digeser, dan kembalikan sesi ke akun default suite.
- Cleanup antar blok TC: setiap blok diawali langkah reset Client E (aksi fixture tanpa `Verifikasi`).

## Test Steps

### TC-GS-IMPORT-381: Upload langsung saat committing ditolak 409

1. Reset Client E ke tanpa draft dan pulihkan worker commit (aksi fixture)
2. Seed draft Brand D-56 (250 baris `pending`) di Client E lewat skrip fixture
3. Muat ulang halaman Import > Brand
4. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
5. Klik `[Import (250)]`
6. Tunggu aksi selesai (permintaan mendapat respons)
7. Muat ulang halaman Import > Brand
8. Kirim permintaan Upload `brand-append-6.csv` langsung ke server dengan token Total Control Client E
9. Verifikasi respons permintaan Upload berstatus 409
10. Muat ulang halaman Import > Brand
11. Verifikasi Modal Column Mapping tidak terbuka
12. Verifikasi kartu Total Rows tetap 250

### TC-GS-IMPORT-383: AI Accept dan Dismiss langsung saat committing ditolak 409

13. Reset Client E ke tanpa draft dan pulihkan worker commit (aksi fixture)
14. Pastikan mock AI mode normal (D-40), lalu seed draft Brand D-57 di Client E lewat skrip fixture
15. Muat ulang halaman Import > Brand
16. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
17. Klik `[Import (248)]`
18. Tunggu aksi selesai (permintaan mendapat respons)
19. Muat ulang halaman Import > Brand
20. Kirim permintaan AI Accept untuk sel Brand Name baris #5 langsung ke server dengan token Total Control Client E
21. Verifikasi respons permintaan AI Accept berstatus 409
22. Kirim permintaan AI Dismiss untuk sel Brand Name baris #5 langsung ke server dengan token Total Control Client E
23. Verifikasi respons permintaan AI Dismiss berstatus 409
24. Muat ulang halaman Import > Brand
25. Verifikasi Brand Name baris #5 tetap bernilai `PT Samsung Electronics Indonesia Manufacturing and Distribution Company for Consumer Electronics and Home Appliances Prod` (121 karakter)
26. Verifikasi baris #5 tetap berstatus `error`
27. Verifikasi badge saran AI pada sel Brand Name baris #5 masih tampil

### TC-GS-IMPORT-384: Memulai sesi edit langsung saat committing ditolak 409

28. Reset Client E ke tanpa draft dan pulihkan worker commit (aksi fixture)
29. Seed draft Brand D-56 (250 baris `pending`) di Client E lewat skrip fixture
30. Muat ulang halaman Import > Brand
31. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
32. Klik `[Import (250)]`
33. Tunggu aksi selesai (permintaan mendapat respons)
34. Muat ulang halaman Import > Brand
35. Kirim permintaan memulai sesi edit untuk baris #1 langsung ke server dengan token Total Control Client E
36. Verifikasi respons permintaan memulai sesi edit berstatus 409
37. Muat ulang halaman Import > Brand
38. Verifikasi footer menampilkan `[Import (250)]` Disabled
39. Verifikasi footer tidak menampilkan `[Cancel]` dan `[Save]`
40. Verifikasi kartu Total Rows tetap 250

### TC-GS-IMPORT-746: Discard Draft langsung saat committing ditolak 409

41. Reset Client E ke tanpa draft dan pulihkan worker commit (aksi fixture)
42. Seed draft Brand D-56 (250 baris `pending`) di Client E lewat skrip fixture dengan hook umur draft D-76 varian 1 (`created_at` dimundurkan 25 jam)
43. Muat ulang halaman Import > Brand
44. Aktifkan kontrol worker commit mode 2 (dijeda di dalam batch pertama)
45. Klik `[Import (250)]`
46. Tunggu aksi selesai (permintaan mendapat respons)
47. Muat ulang halaman Import > Brand
48. Kirim permintaan Discard Draft langsung ke server dengan token Total Control Client E
49. Verifikasi respons permintaan Discard Draft berstatus 409
50. Muat ulang halaman Import > Brand
51. Verifikasi Unsaved Banner tampil
52. Verifikasi kartu Total Rows tetap 250

### TC-GS-IMPORT-739: Import langsung tanpa draft ditolak 404

53. Reset Client E ke tanpa draft dan pulihkan worker commit (aksi fixture)
54. Muat ulang halaman Import > Brand
55. Kirim permintaan Import untuk Tab Brand langsung ke server dengan token Total Control Client E
56. Verifikasi respons permintaan Import berstatus 404
57. Muat ulang halaman Import > Brand
58. Verifikasi Dropzone tampil
59. Verifikasi Unsaved Banner tidak tampil
60. Verifikasi `[Import (0)]` Disabled

### TC-GS-IMPORT-704: Accept langsung saat committing ditolak 409

61. Reset Client E ke tanpa draft dan pulihkan worker commit (aksi fixture)
62. Muat ulang halaman Import > Brand
63. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
64. Klik `[Upload File]` di toolbar dan pilih berkas `brand-ai-commit.csv`
65. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
66. Klik `[Import (2)]`
67. Tunggu aksi selesai (permintaan mendapat respons)
68. Kirim permintaan Accept untuk baris #3 langsung ke server dengan token Total Control Client E (pengenal baris dari respons pembacaan Staging Table)
69. Verifikasi respons permintaan Accept berstatus 409
70. Muat ulang halaman Import > Brand
71. Verifikasi sel Brand Name baris #3 tetap bernilai 121 karakter semula
72. Verifikasi baris #3 tetap berstatus `error`

### TC-GS-IMPORT-729: Create Missing Divisions langsung saat committing ditolak 409

73. Reset Client E ke tanpa draft dan pulihkan worker commit (aksi fixture)
74. Muat ulang halaman Import > User Login
75. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
76. Klik `[Upload File]` di toolbar dan pilih berkas `user-login-commit-logistik.csv` (baris #1 Bambang Hartono Division `Engineering`; baris #2 Citra Wulandari dan baris #3 Doni Kurniawan Division `Logistik`; Position kosong)
77. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
78. Klik `[Import (1)]`
79. Tunggu aksi selesai (permintaan mendapat respons)
80. Kirim permintaan Create Missing Divisions untuk kategori "Division not found" langsung ke server dengan token Total Control Client E
81. Verifikasi respons permintaan Create Missing Divisions berstatus 409
82. Buka Global Settings > User > Division
83. Verifikasi tabel Division menampilkan 5 baris
84. Verifikasi daftar Division tidak memuat `Logistik`

### TC-GS-IMPORT-730: Create Missing Positions langsung saat committing ditolak 409

85. Reset Client E ke tanpa draft dan pulihkan worker commit (aksi fixture)
86. Buka Global Settings > Import, pilih Sub-Tab User Login
87. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
88. Klik `[Upload File]` di toolbar dan pilih berkas `user-login-commit-store-supervisor.csv` (baris #1 Bambang Hartono Position kosong; baris #2 Citra Wulandari dan baris #3 Doni Kurniawan Position `Store Supervisor`; Division `Engineering`)
89. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
90. Klik `[Import (1)]`
91. Tunggu aksi selesai (permintaan mendapat respons)
92. Kirim permintaan Create Missing Positions untuk kategori "Position not found" langsung ke server dengan token Total Control Client E
93. Verifikasi respons permintaan Create Missing Positions berstatus 409
94. Buka Global Settings > User > Position
95. Verifikasi tabel Position menampilkan 5 baris
96. Verifikasi daftar Position tidak memuat `Store Supervisor`

### TC-GS-IMPORT-918: Create Missing Options selama committing Disabled dan request langsung ditolak 409

97. Reset Client E ke tanpa draft dan pulihkan worker commit (aksi fixture)
98. Buka Global Settings > Import, pilih Sub-Tab User Login
99. Aktifkan kontrol worker commit mode 1 (dijeda sebelum job mulai)
100. Klik `[Upload File]` di toolbar dan pilih berkas `user-login-commit-shift.csv`
101. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
102. Klik `[Import (1)]`
103. Verifikasi footer `[Import (1)]` tampil Disabled
104. Klik `⋯` pada baris #2
105. Arahkan kursor ke `[Create Missing Options]` pada menu `⋯`
106. Verifikasi `[Create Missing Options]` pada menu `⋯` baris #2 tampil Disabled dengan tooltip "Can't do this while an import is in progress."
107. Tutup menu `⋯`
108. Arahkan kursor ke `[Create Missing Options]` pada Error Summary Callout
109. Verifikasi `[Create Missing Options]` pada Error Summary Callout tampil Disabled dengan tooltip "Can't do this while an import is in progress."
110. Kirim permintaan Create Missing Options untuk kategori "Shift: Invalid option" langsung ke server dengan token Total Control Client E
111. Verifikasi respons permintaan Create Missing Options berstatus 409 Conflict
112. Buka Global Settings > User > Custom Field dan buka Value Setting `Shift`
113. Verifikasi Value Setting Shift Client E tetap `Pagi, Siang, Malam`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: defense-in-depth (a); kontrol worker commit D-47 hanya pemicu state `committing` (P-2) dan bukan objek uji.
- P-2: kontrol worker commit D-47 dan seeding draft lewat fixture adalah pemicu state, bukan objek asersi spec ini.
- Alasan melewati sekitar 35 langkah (113 langkah nominal, tiap blok 8 sampai 17 langkah): semua blok satu kelas (request langsung ke server saat `committing` atau tanpa draft), berdiri sendiri dengan reset Client E di awal tiap blok, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan blok mengikuti kebutuhan state: blok yang memakai Sub-Tab Brand lebih dulu, lalu blok User Login; tiap blok mereset Client E sendiri sehingga urutan tidak saling bergantung.
- Langkah penghubung (tanpa `Verifikasi`): langkah reset dan seeding (langkah 1, 2, 13, 14, 28, 29, 41, 42, 53, 61, 73, 85, 97); pembukaan Sub-Tab dan "Muat ulang halaman Import > <Sub-Tab>" sesudah reset (langkah 3, 15, 30, 43, 54, 62, 74; reset membuang atau mengganti draft sementara halaman Import dari blok sebelumnya masih terbuka, `suite.md`); langkah 107 menutup menu `⋯`; langkah 112 membuka Value Setting. Langkah 6, 18, 33, dan 46 (Tunggu aksi selesai: permintaan mendapat respons) memisahkan klik `[Import (250)]` atau `[Import (248)]` dari muat ulang halaman; langkah 67, 79, dan 91 (Tunggu aksi selesai: permintaan mendapat respons) memisahkan klik `[Import (N)]` dari permintaan langsung ke server pada langkah 68, 80, dan 92 (bagian 8b butir 8); bacaan Langkah TC "request langsung ke server" tetap dipertahankan.
- Langkah 11 memakai Verifikasi kartu Total Rows tampil sebagai anchor positif sebelum asersi absence Modal Column Mapping (butir 2 bagian 8b); langkah 83 dan 95 (jumlah baris tabel) adalah anchor positif untuk asersi absence `Logistik` dan `Store Supervisor`.
- Langkah 39 dan 59 adalah asersi absence atas elemen UI pada halaman yang sudah termuat sesudah muat ulang; elemen lain pada halaman (langkah 38 dan 58) tampil lebih dulu.
- Temuan untuk QA:
  - TC-GS-IMPORT-381, 383, 384, 739, 746, 918 bertanda FE Test `Need API`, sedangkan TC-GS-IMPORT-704, 729, 730 (pola identik: request langsung saat `committing` ditolak 409) bertanda `-` (hanya-BE). Ketiganya tetap menjadi spec FE+BE di sini. Seleksi hanya-BE tidak konsisten antar pola identik.
  - TC-GS-IMPORT-704, 729, 730 mengasersi UI (sel Brand Name baris #3 tetap 121 karakter; daftar Division dan Position tidak memuat nama baru) sehingga bukan murni kontrak API; spec mengasersinya sebagai state data setelah request langsung (butir 1 bagian 8b).
  - Expected TC-GS-IMPORT-384 b (footer `[Import (250)]` Disabled, tanpa `[Cancel]` dan `[Save]`) dan TC-GS-IMPORT-918 a sampai c (Disabled dengan tooltip) adalah perilaku FE selama `committing`, bukan akibat request langsung. Spec mengasersinya sesudah muat ulang atau sebelum request langsung sehingga tidak dikaitkan dengan respons request.
  - TC-GS-IMPORT-918 mencampur dua objek uji (Disabled dengan tooltip di UI dan request langsung ditolak 409) dalam satu TC; dipertahankan utuh di spec ini.
  - TC-GS-IMPORT-383 dan TC-GS-IMPORT-381 tidak merujuk D-47 pada kolom referensi; kontrol worker commit ditulis di Prerequisites.
  - TC-GS-IMPORT-729 dan TC-GS-IMPORT-730 tidak menyebut mode D-47 yang dimaksud; spec memakai mode 1 (dijeda sebelum job mulai) karena kondisi TC hanya mensyaratkan job tetap `committing`.
  - Post Condition TC-GS-IMPORT-381, 383, 384, 746 ("job tetap committing dengan worker dijeda") tidak punya langkah observasi tersendiri dan tidak diasersi (S-01); pemulihan worker dikerjakan hook `after`.
  - Mekanisme kontrol worker, klien HTTP, dan skrip reset Client E tidak didefinisikan di TC, PRD, atau LLD selain nama kemampuannya; disediakan tim FE/BE.
  - Penanda selesai untuk pemicu sesi API atau fixture tidak disebut di TC atau PRD; langkah "Tunggu aksi selesai" (langkah 6, 18, 33, 46, 67, 79, dan 91) memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati di surface aktor UI.
