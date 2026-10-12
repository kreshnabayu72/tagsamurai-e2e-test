---
id: TC-GS-BRAND-E2E-052-changelog-filter-chip-x-uncheck-dan-overflow
title: "Changelog Brand: Chip Filter (X), Uncheck Opsi, dan Overflow +N more"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-281
  - TC-GS-BRAND-282
  - TC-GS-BRAND-283
coverage:
  web: automated
---

# Changelog Brand: Chip Filter (X), Uncheck Opsi, dan Overflow +N more

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > Master Reference > Brand.
- Akun seeding tambahan (hanya untuk seeding API di hook `before`, bukan login UI):
  - Create+Read, Rina Marlina (`Rina M`), `createOnly_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_CREATE_PASSWORD`.
  - Update+Read, Agus Wijaya (`Agus W`), `updateOnly_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_UPDATE_PASSWORD`.
- Environment variable: `GS_TC_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Seeding (lewat API di hook `before`, urutan sebagai berikut):
  - Population D-01 oleh Sari Dewi: 12 brand dengan nama literal `Apex Tools`, `Bolt Systems`, `Cedar Supply`, `Delta Instruments`, `Echo Devices`, `Falcon Gear`, `Granite Works`, `Harbor Tech`, `Iris Optics`, `Juniper Labs`, `Keystone Mfg`, `Linear Dynamics` (setara TC-GS-BRAND-1). Menghasilkan entri Create oleh `Sari D`; 10 nama pertama dipakai TC-GS-BRAND-283.
  - `Apex Tools {runId}-052` dan `Bolt Systems {runId}-052` dibuat oleh Sari Dewi (entri Create oleh `Sari D` yang unik per run; dipakai TC-GS-BRAND-281 dan 282 agar asersi "satu baris" tidak terganggu entri Population dari run atau spec lain).
  - `Mosaic Brands {runId}-052` dibuat oleh Rina Marlina (entri Create oleh `Rina M`, setara TC-GS-BRAND-36).
  - `Mosaic Brands {runId}-052` diubah namanya oleh Agus Wijaya menjadi `Mosaic Group {runId}-052` (entri Edit oleh `Agus W`, setara TC-GS-BRAND-37).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus oleh Sari Dewi lewat API 12 brand Population, `Apex Tools {runId}-052`, `Bolt Systems {runId}-052`, dan `Mosaic Group {runId}-052`. Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: viewport desktop lebar 1280 px (diatur di hook `before`); klik `(X)` pada chip filter; mengetahui jumlah chip yang tampil pada field Brand Name.
- Precondition TC-GS-BRAND-281, 282: login sebagai Total Control; entri Changelog Population (Create oleh Sari D), Mosaic Brands (Create oleh Rina M) dan Edit Mosaic Brands oleh Agus W tersedia. TC-GS-BRAND-283: entri Create untuk 12 brand Population tersedia; viewport desktop lebar 1280 px.
- State global yang dipulihkan: ukuran viewport dikembalikan ke bawaan di hook `after`.

## Test Steps

### TC-GS-BRAND-283: Overflow chip pada field Brand Name filter Changelog diringkas menjadi +N more

1. Klik icon Changelog di halaman Global Settings > Master Reference > Brand → modal Changelog tampil
2. Klik Filter → Filter Panel tampil
3. Pilih 10 opsi Brand Name: `Apex Tools`, `Bolt Systems`, `Cedar Supply`, `Delta Instruments`, `Echo Devices`, `Falcon Gear`, `Granite Works`, `Harbor Tech`, `Iris Optics`, `Juniper Labs`
4. Amati field Brand Name
5. Verifikasi chip ditampilkan sebanyak yang muat pada lebar field
6. Verifikasi sisanya diringkas dalam satu chip `+N more`
7. Verifikasi jumlah chip tampil ditambah N sama dengan 10
8. Verifikasi field tidak melebar keluar panel
9. Verifikasi field tidak digulir horizontal

### TC-GS-BRAND-281: Menghapus chip filter Changelog lewat (X) pada field Action, Brand Name, dan Modified By

10. Kosongkan seluruh pilihan Brand Name (sisa TC-GS-BRAND-283)
11. Pilih Action `Create` dan `Edit`
12. Pilih Brand Name `Apex Tools {runId}-052` dan `Bolt Systems {runId}-052`
13. Pilih Modified By `Sari D` dan `Rina M`
14. Klik `(X)` pada chip `Edit` (field Action)
15. Klik `(X)` pada chip `Bolt Systems {runId}-052` (field Brand Name)
16. Klik `(X)` pada chip `Rina M` (field Modified By)
17. Verifikasi field Action: chip `Edit` hilang
18. Verifikasi field Action: chip `Create` tetap
19. Verifikasi field Brand Name: chip `Bolt Systems {runId}-052` hilang
20. Verifikasi field Brand Name: chip `Apex Tools {runId}-052` tetap
21. Verifikasi field Modified By: chip `Rina M` hilang
22. Verifikasi field Modified By: chip `Sari D` tetap
23. Buka dropdown Action, amati checkbox
24. Verifikasi checkbox `Edit` ter-uncheck
25. Buka dropdown Brand Name, amati checkbox
26. Verifikasi checkbox `Bolt Systems {runId}-052` ter-uncheck
27. Buka dropdown Modified By, amati checkbox
28. Verifikasi checkbox `Rina M` ter-uncheck
29. Klik [Apply]
30. Verifikasi tabel hanya memuat satu baris: Create `Apex Tools {runId}-052` oleh Sari D

### TC-GS-BRAND-282: Meng-uncheck opsi di dalam dropdown filter Changelog menghapus chip pada field Action, Brand Name, dan Modified By

31. Klik Filter, kosongkan seluruh pilihan field Action, Brand Name, dan Modified By (sisa TC-GS-BRAND-281)
32. Pilih Action `Create` dan `Edit`
33. Pilih Brand Name `Apex Tools {runId}-052` dan `Bolt Systems {runId}-052`
34. Pilih Modified By `Sari D` dan `Rina M`
35. Buka dropdown Action dan uncheck `Edit`
36. Buka dropdown Brand Name dan uncheck `Bolt Systems {runId}-052`
37. Buka dropdown Modified By dan uncheck `Rina M`
38. Verifikasi field Action: chip `Edit` hilang
39. Verifikasi field Action: chip `Create` tetap
40. Verifikasi field Brand Name: chip `Bolt Systems {runId}-052` hilang
41. Verifikasi field Brand Name: chip `Apex Tools {runId}-052` tetap
42. Verifikasi field Modified By: chip `Rina M` hilang
43. Verifikasi field Modified By: chip `Sari D` tetap
44. Klik [Apply]
45. Verifikasi tabel hanya memuat satu baris: Create `Apex Tools {runId}-052` oleh Sari D

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-BRAND-283, 281, 282. Alasan: TC-GS-BRAND-283 hanya mengamati field tanpa [Apply] (screening lebih dulu, bagian 3 konvensi), sedangkan 281 dan 282 meng-Apply filter; modal Changelog dibuka sekali untuk ketiganya.
- Langkah penghubung (aksi tanpa `Verifikasi`, membersihkan state filter dari TC sebelumnya): langkah 10 dan 31.
- Langkah 30 dan 45 (satu baris Create) memakai `Apex Tools {runId}-052` bersuffix per run, sehingga Changelog Client A yang dipakai bersama tidak membuat jumlah baris bergantung pada run atau spec lain. TC-GS-BRAND-283 memakai nama Population literal karena hanya mengamati chip.
- Nama Mosaic bersuffix `{runId}-052` supaya tidak bentrok dengan spec lain yang memakai D-04 (TC-GS-BRAND-36); entri Changelog yang dipakai hanya untuk menyediakan opsi `Rina M` dan Action `Edit`.
