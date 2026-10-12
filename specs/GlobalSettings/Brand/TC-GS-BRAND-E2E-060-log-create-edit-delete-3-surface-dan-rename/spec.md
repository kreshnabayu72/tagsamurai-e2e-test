---
id: TC-GS-BRAND-E2E-060-log-create-edit-delete-3-surface-dan-rename
title: "Pencatatan Log Create, Edit, Delete Brand di Changelog, System Log, dan Activity Log serta Riwayat Rename"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-206
  - TC-GS-BRAND-207
  - TC-GS-BRAND-208
  - TC-GS-BRAND-214
coverage:
  web: automated
---

# Pencatatan Log Create, Edit, Delete Brand di Changelog, System Log, dan Activity Log serta Riwayat Rename

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Master Reference > Brand.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi):
  - `Tidal Co {runId}-060` (D-11): dibuat spec lewat UI pada TC-GS-BRAND-206 (setara dependensi TC-GS-BRAND-56), lalu di-rename menjadi `Tidal Group {runId}-060` (TC-GS-BRAND-207, setara dependensi TC-GS-BRAND-70) dan `Tidal One {runId}-060` (TC-GS-BRAND-214, setara dependensi TC-GS-BRAND-88). Dibuat spec sendiri karena entri log harus bersumber dari aksi di spec ini (tepat 1 entri per surface).
  - `Xenon Bebas {runId}-060` (D-17): brand bebas relasi, di-seed lewat API di hook `before`, dihapus lewat UI pada TC-GS-BRAND-208 (setara dependensi TC-GS-BRAND-95).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API brand `Tidal Co`, `Tidal Group`, `Tidal One` (nama yang masih ada) dan `Xenon Bebas` bersuffix `{runId}-060` bila masih ada.
- Tidak ada state global yang diubah.
- TC-GS-BRAND-206, 207, 208, 214: login sebagai Total Control dan berada di Global Settings > Master Reference > Brand.

## Test Steps

### TC-GS-BRAND-206: Log Create Brand tercatat di Changelog, System Log, dan Activity Log

1. Klik [+ Brand], isi Brand Name `Tidal Co {runId}-060`, klik [Submit]
2. Verifikasi toast sukses: "Success, brand has been created."
3. Buka Changelog Brand
4. Verifikasi Changelog: Action `Create`, Brand Name `Tidal Co {runId}-060`, Field `Brand Name`, Old Value `—`, New Value `Tidal Co {runId}-060`, Modified By `Sari D`; tepat 1 entri Create untuk brand ini
5. Buka Global Settings > User > Detail Sari Dewi > Tab System Log
6. Verifikasi System Log Detail User Sari Dewi: Action `Create`, Object `Brand`, Name `Tidal Co {runId}-060`, Field `Brand Name`, Old `—`, New `Tidal Co {runId}-060`; tepat 1 entri Create untuk brand ini
7. Buka Global Settings > Activity Log
8. Verifikasi Activity Log Global Settings: Action `Create`, Object `Brand`, Name `Tidal Co {runId}-060`, Field `Brand Name`, Old `—`, New `Tidal Co {runId}-060`, Modified By `Sari D`; tepat 1 entri Create untuk brand ini
9. Buka Global Settings > Master Reference > Brand

### TC-GS-BRAND-207: Log Edit Brand tercatat di 3 surface

10. Buka Global Settings > Master Reference > Brand, Search `Tidal Co {runId}-060` pada tabel Brand, edit baris tersebut menjadi `Tidal Group {runId}-060`, klik [Save]
11. Verifikasi toast sukses: "Success, brand has been updated."
12. Buka Changelog Brand
13. Verifikasi Changelog: Action `Edit`, Brand Name `Tidal Group {runId}-060`, Field `Brand Name`, Old Value `Tidal Co {runId}-060`, New Value `Tidal Group {runId}-060`, Modified By `Sari D`; tepat 1 entri Edit untuk perubahan ini
14. Buka Tab System Log Sari Dewi
15. Verifikasi System Log Detail User Sari Dewi: Action `Edit`, Object `Brand`, Name `Tidal Group {runId}-060`, Field `Brand Name`, Old `Tidal Co {runId}-060`, New `Tidal Group {runId}-060`; tepat 1 entri Edit untuk perubahan ini
16. Buka Activity Log
17. Verifikasi Activity Log Global Settings: Action `Edit`, Object `Brand`, Name `Tidal Group {runId}-060`, Field `Brand Name`, Old `Tidal Co {runId}-060`, New `Tidal Group {runId}-060`, Modified By `Sari D`; tepat 1 entri Edit untuk perubahan ini
18. Buka Global Settings > Master Reference > Brand

### TC-GS-BRAND-214: Entri log lama tidak berubah setelah rename kedua

19. Buka Global Settings > Master Reference > Brand, Search `Tidal Group {runId}-060` pada tabel Brand, edit baris tersebut menjadi `Tidal One {runId}-060`, klik [Save]
20. Buka Changelog, Search `Tidal`
21. Verifikasi entri Edit pertama tetap Old `Tidal Co {runId}-060` → New `Tidal Group {runId}-060`
22. Verifikasi entri Edit kedua Old `Tidal Group {runId}-060` → New `Tidal One {runId}-060`
23. Verifikasi entri Create tetap Brand Name `Tidal Co {runId}-060`

### TC-GS-BRAND-208: Log Delete Brand tercatat di 3 surface

24. Buka Global Settings > Master Reference > Brand, Search `Xenon Bebas {runId}-060` pada tabel Brand, klik `⋯` pada baris tersebut > Delete → dialog `Delete Brand` tampil, klik [Delete]
25. Verifikasi toast sukses: "Success, brand has been deleted."
26. Buka Changelog Brand
27. Verifikasi Changelog: Action `Delete`, Brand Name `Xenon Bebas {runId}-060`, Field `Brand Name`, Old Value `Xenon Bebas {runId}-060`, New Value `—`, Modified By `Sari D`; tepat 1 entri Delete untuk brand ini
28. Buka Tab System Log Sari Dewi
29. Verifikasi System Log Detail User Sari Dewi: Action `Delete`, Object `Brand`, Name `Xenon Bebas {runId}-060`, Field `Brand Name`, Old `Xenon Bebas {runId}-060`, New `—`; tepat 1 entri Delete untuk brand ini
30. Buka Activity Log
31. Verifikasi Activity Log Global Settings: Action `Delete`, Object `Brand`, Name `Xenon Bebas {runId}-060`, Field `Brand Name`, Old `Xenon Bebas {runId}-060`, New `—`, Modified By `Sari D`; tepat 1 entri Delete untuk brand ini
32. Buka Global Settings > Master Reference > Brand

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC di spec: Create (206), Edit (207), rename kedua (214), lalu Delete (208). Delete ditaruh paling akhir (prinsip 5), dan 214 harus sesudah 207 karena 207 mengecek "tepat 1 entri" untuk rename pertama sebelum rename kedua menambah entri.
- Dependensi (TC-GS-BRAND-56, 70, 88, 95) dijalankan sebagai langkah di spec ini, bukan bergantung pada spec lain. Data `Xenon Bebas` di-seed lewat API karena pembuatannya bukan objek uji.
- Entri log yang dicari di Changelog, System Log, dan Activity Log dikenali lewat nama bersuffix `{runId}-060`; entri milik spec atau run lain diabaikan.
- Langkah penghubung: langkah 9, 18, dan 32 (kembali ke tabel Brand dari Activity Log; hitungan "tepat 1 entri" diasersikan pada tiap surface yang sedang terbuka: langkah 4, 6, 8, 13, 15, 17, 27, 29, 31), serta langkah 10, 19, dan 24 (kembali ke tab Brand dari surface log sebelum aksi berikutnya) tidak tertulis di Langkah Uji TC sumber. Pada ketiga langkah itu baris target dicari dulu lewat Search nama brand pada tabel Brand (tabel A-Z, page size 10, dan Client A punya lebih dari satu halaman brand, sehingga baris bersuffix `{runId}-060` tidak dijamin ada di halaman 1); Search ini bagian dari langkah aksi yang sama dan juga tidak tertulis di Langkah Uji TC sumber.
- Asersi "tidak ada entri log" tidak dimuat di spec ini; diuji di spec `TC-GS-BRAND-E2E-062-log-absence-no-op-skip-cancel-dan-import`.
- TC-GS-BRAND-214 Langkah Uji 1 menulis "via TC rename kedua"; spec menjabarkannya sebagai langkah 19.
