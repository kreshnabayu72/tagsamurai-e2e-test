---
id: TC-GS-IMPORT-E2E-189-client-f-struktur-staging-table-kolom-badge-row-urutan-dan-ketiadaan
title: "Client F: struktur Staging Table (kolom, badge, Row #, urutan) dan ketiadaan Search/Filter/Sort/Column Visibility/unduh laporan, kontras warna"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-474
  - TC-GS-IMPORT-475
  - TC-GS-IMPORT-481
  - TC-GS-IMPORT-482
  - TC-GS-IMPORT-488
  - TC-GS-IMPORT-771
  - TC-GS-IMPORT-890
coverage:
  web: automated
---

# Client F: struktur Staging Table (kolom, badge, Row #, urutan) dan ketiadaan Search/Filter/Sort/Column Visibility/unduh laporan, kontras warna

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena state global dibagi antar spec (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client F (Hendra Wijaya) `totalControl_automated_qaTeam6@qwertysystem.net`, password `Spectra.env.GS_CLIENTF_TC_PASSWORD` (TC tidak menyebut password per akun, lihat Temuan untuk QA).
- Layar awal: hook `beforeEach` membuka Import > Brand Client F.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis D-10: draft Brand campuran Client F (5 `pending`, 3 `error`, 2 `duplicate`; Row # 1 `Nexus`, 2 `Orion`, 3 `Vertex`, 4 `Helios`, 5 `Samsung`, 6 `Pioneer`, 7 nama 121 karakter, 8 `Rocket 🚀`, 9 `Star ⭐`, 10 `Pioneer`), disiapkan oleh langkah 1 lewat skrip fixture (mekanisme skrip disediakan tim FE/BE). Nilai literal dipakai karena asersi bergantung pada urutan dan nama baris; Client F khusus draft campuran. Spec read-only, tidak ada mutasi draft.
- Cleanup (hook `after`): draft Brand Client F dibuang lewat skrip reset.
- Kemampuan teknis: skrip fixture reset Client F dan seed D-10 (langkah 1); pengukuran rasio kontras warna teks (util kontras atau axe) untuk TC-GS-IMPORT-488; klik kanan pada header kolom; hover/klik header.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps
1. Reset Client F ke tanpa draft dan seed draft Brand D-10 (campuran: 5 `pending`, 3 `error`, 2 `duplicate`) lewat skrip fixture, lalu muat ulang halaman Import > Brand

### Kolom dan badge (TC-GS-IMPORT-474, 475)

2. Verifikasi header kolom Staging Table `Checkbox | # | Brand Name | Status | Actions`
3. Verifikasi kolom Checkbox dan `#` pinned kiri
4. Verifikasi kolom Actions pinned kanan
5. Verifikasi tidak ada kolom `Created At`
6. Verifikasi header kolom tidak dapat diurutkan (tidak ada ikon sort)
7. Verifikasi badge `pending` primary pada Row # 1, 2, 3, 4, dan 10
8. Verifikasi badge `error` danger pada Row # 7, 8, dan 9
9. Verifikasi badge `duplicate` warning pada Row # 5 dan 6

### Urutan default dan ketiadaan Search/Filter/Sort (TC-GS-IMPORT-481, 482, 771)

10. Verifikasi baris berurut Row # ascending dengan Row # 1 `Nexus` di paling atas
11. Klik header kolom Brand Name
12. Verifikasi urutan baris tidak berubah
13. Verifikasi header Brand Name tidak memunculkan ikon sort
14. Verifikasi toolbar tidak memuat icon Search
15. Verifikasi toolbar tidak memuat icon Filter maupun dropdown filter status
16. Verifikasi header kolom tidak memuat ikon sort
17. Verifikasi kartu Errors, Ready to Import, dan Duplicates berstatus Enabled
18. Verifikasi Button `[Download Template]` bertulisan "Download Template" tanpa icon (gaya outline)
19. Verifikasi Button `[Upload File]` bertulisan "Upload File" tanpa icon (gaya filled, aksi utama, paling kanan di toolbar)
20. Verifikasi toolbar kanan hanya memuat Switch `Edit this page`, Button `[Download Template]`, dan Button `[Upload File]`
21. Verifikasi tiap baris pesan Error Summary Callout hanya memuat `[View Data]` dan `[Delete All Rows]`
22. Verifikasi tidak ada tombol unduh laporan kesalahan pada Callout

### Ketiadaan Column Visibility dan Setup Column (TC-GS-IMPORT-890)

23. Verifikasi toolbar tidak memuat kontrol kolom
24. Klik header kolom Actions di ujung kanan tabel
25. Verifikasi header kolom Actions tidak memuat icon `⋯` maupun kontrol lain
26. Verifikasi tidak ada overlay Column Visibility
27. Verifikasi tidak ada item "Setup Column..."
28. Klik kanan header kolom `Brand Name`
29. Verifikasi tidak ada menu atau checkbox untuk menyembunyikan kolom
30. Verifikasi kolom `Brand Name` dan `Status` tetap tampil

### Kontras warna (TC-GS-IMPORT-488)

31. Ukur rasio kontras teks sel Staging Table
32. Verifikasi rasio kontras teks sel Staging Table >= 4.5:1
33. Ukur rasio kontras teks badge `pending`, `error`, dan `duplicate`
34. Verifikasi rasio kontras teks badge `pending`, `error`, dan `duplicate` >= 4.5:1
35. Ukur rasio kontras angka dan label Staging Metric Cards
36. Verifikasi rasio kontras angka dan label Staging Metric Cards >= 4.5:1

## Notes

- Spec melewati sekitar 35 langkah (36 langkah). Seluruhnya satu topik dengan akun dan client yang sama; langkah pembuka seed eksplisit (suite.md, `beforeEach` hanya menyiapkan keadaan dasar) menambah langkah pada spec yang sudah mendekati batas, dan memecahnya hanya menambah login, hook, dan pembersihan tanpa menambah daya deteksi.
- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Semua TC berbagi dataset D-10 read-only dan akun yang sama; TC-GS-IMPORT-488 (kontras) paling akhir karena berupa pengukuran visual tanpa mengubah state.
- Langkah 1 menyiapkan D-10 dan memuat ulang halaman Import > Brand (langkah penghubung tanpa `Verifikasi`, S-03).
- Langkah 12 diasersi sebelum langkah berikutnya karena klik header tidak boleh mengubah urutan (S-14 urutan sebelum/sesudah klik).
- TC-GS-IMPORT-474 Expected d ("tidak dapat diurutkan") dan TC-GS-IMPORT-481 Expected b dicek terpisah pada langkah 6 dan 12-13.
- Temuan untuk QA:
  - TC-GS-IMPORT-488 tidak menyebut alat ukur kontras; spec mengasumsikan util kontras atau axe disediakan tim FE.
  - TC-GS-IMPORT-890 langkah 2 dan 3 (klik header Actions, klik kanan header `Brand Name`) tidak menyebut perilaku yang diharapkan bila browser membuka context menu native; asersi hanya pada ketiadaan menu aplikasi.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
