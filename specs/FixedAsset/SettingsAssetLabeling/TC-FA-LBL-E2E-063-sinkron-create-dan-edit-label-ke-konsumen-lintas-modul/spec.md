---
id: TC-FA-LBL-E2E-063-sinkron-create-dan-edit-label-ke-konsumen-lintas-modul
title: "Sync Matrix: Create dan Edit Label tersedia dan terefleksi di asset/, reports/, dan settings-asset-name/"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:sync-matrix/create-label
  - FALB:sync-matrix/edit-label
coverage:
  web: automated
---

# Sync Matrix: Create dan Edit Label tersedia dan terefleksi di asset/, reports/, dan settings-asset-name/

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Tidak ada ganti akun.
- Data uji `DU-70` (Label seed untuk uji konsumen lintas modul), bersuffix `{runId}-063`: nama awal label `Sync-{runId}-063` (dibuat langkah 1 sampai 4 sebagai objek uji Create), nama baru `SyncRenamed-{runId}-063`, warna awal dan warna baru dari palet preset PRD §4.3 (berbeda satu sama lain); satu aset Active seed dan satu Asset Name seed yang dibuat lewat API di hook `before`. Hook `after` melepas relasi label dari aset lalu menghapus aset, Asset Name, dan label milik spec lewat sesi API.
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding aset dan Asset Name serta membaca label; disediakan tim FE/BE. Halaman Asset List, Asset Detail, dan Panel Filter dimiliki modul `asset/` (`asset/PRD/asset.md` §4.1c dan §4.1d); Modal Edit Asset Name dengan dropdown Default Label dimiliki modul `settings-asset-name/` (§4.1).
- State global: spec membuat satu label dan mengubahnya; hook `after` membersihkan semuanya. Suite berjalan serial (`parallel: false`).

## Test Steps

### FALB:sync-matrix/create-label: Create Label: data baru tersedia di dropdown penugasan asset/ dan opsi Default Label settings-asset-name/

1. Klik `[+ Label]` pada toolbar tabel
2. Ketik Label Name `DU-70` (nama awal), pilih swatch preset warna awal `DU-70`
3. Klik `[Submit]`
4. Verifikasi toast `Success, label has been created.` tampil
5. Ketik Search `DU-70`, tekan Enter
6. Verifikasi baris label bernama awal `DU-70` tampil pada Labels List
7. Buka Asset Detail aset seed `DU-70` dari Asset List modul `asset/`
8. Klik `[+ Add Label]` pada seksi Labels
9. Verifikasi label bernama awal `DU-70` tampil sebagai opsi pada dropdown penugasan label
10. Pilih label bernama awal `DU-70` pada dropdown penugasan label
11. Verifikasi chip label bernama awal `DU-70` berlatar warna awal `DU-70` tampil pada seksi Labels Asset Detail
12. Buka tab Asset Name pada Settings > Asset Master
13. Ketik Search Asset Name seed `DU-70`, tekan Enter
14. Klik `[⋯]` pada baris Asset Name seed `DU-70`, pilih `Edit`
15. Klik dropdown Default Label pada Modal Edit Asset Name
16. Verifikasi label bernama awal `DU-70` tampil sebagai opsi pada dropdown Default Label
17. Klik `[✕]` pada header Modal Edit Asset Name

### FALB:sync-matrix/edit-label: Edit Label: nama dan warna terefleksi di chip Asset List, Asset Detail, dan Panel Filter asset/

18. Buka tab Labels pada Settings > Asset Master
19. Ketik Search `DU-70`, tekan Enter
20. Klik `[⋯]` pada baris label bernama awal `DU-70`, pilih `Edit`
21. Ganti Label Name dengan nama baru `DU-70`, pilih swatch preset warna baru `DU-70`
22. Klik `[Save]`
23. Verifikasi toast `Success, label has been updated.` tampil
24. Buka Asset List modul `asset/`, ketik Search aset seed `DU-70`, tekan Enter
25. Verifikasi kolom Labels pada baris aset seed `DU-70` menampilkan chip bernama baru `DU-70` berlatar warna baru `DU-70`
26. Buka Asset Detail aset seed `DU-70`
27. Verifikasi seksi Labels Asset Detail menampilkan chip bernama baru `DU-70` berlatar warna baru `DU-70` dan tidak menampilkan nama awal
28. Buka Asset List modul `asset/`, buka Panel Filter, dan klik dropdown Labels
29. Verifikasi opsi label bernama baru `DU-70` berlatar warna baru `DU-70` tampil pada dropdown Labels sedangkan nama awal tidak tampil

## Notes

- Langkah penghubung (S-03): langkah 5 dan 19 menemukan baris label target di Labels List yang dapat memuat lebih dari satu halaman (R-16); langkah 7, 12, 18, 24, 26, dan 28 berpindah halaman atau modul; langkah 10 menugaskan label ke aset seed hanya untuk membentuk precondition chip yang direfleksikan di langkah 25 sampai 27; langkah 17 menutup Modal Edit Asset Name tanpa perubahan; langkah 13 dan 24 menemukan Asset Name dan aset seed lewat Search.
- Anchor positif: toast Create (langkah 4) dan toast Edit (langkah 23) mendahului asersi sinkron; langkah 6 dan 9 membuktikan label baru tersedia sebelum dipakai di langkah 10; langkah 29 mengasersi nama awal tidak tampil setelah opsi nama baru tampil pada surface yang sama.
- Surface Create dan Edit yang diasersi: dropdown penugasan label di `asset/` (langkah 8 sampai 11), opsi Default Label di `settings-asset-name/` (langkah 14 sampai 16), chip badge di Asset List, Asset Detail, dan Panel Filter `asset/` (langkah 24 sampai 29).
- Temuan PRD: sync-matrix menyebut "filter multi-select di `reports/`" (Create) dan "Laporan" (Edit) sebagai surface terdampak, tetapi PRD ini hanya menyebut path modul `reports/` tanpa nama halaman atau filter, dan modul `reports/` tidak memiliki PRD di repositori dokumentasi; klausa `reports/` tidak diasersi.
- Temuan PRD: sync-matrix baris Edit Label menyebut "kolom dan filter Default Label di `settings-asset-transactional-policy/`" sebagai surface terdampak; modul itu di luar modul konsumen yang dibuka untuk spec ini (asset/, reports/, settings-asset-name/), sehingga refleksi di sana tidak diasersi.
- Temuan PRD: kolom Timing Create Label menyatakan "Realtime / Sync" tanpa batas waktu tampil; asersi tidak menunggu waktu tertentu dan mengandalkan toast hasil server sebagai anchor.
