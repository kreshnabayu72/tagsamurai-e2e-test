---
id: TC-FA-TDC-E2E-025-aktor-update-only-bulk-activate-deactivate-dan-cancel-version-dari-alert
title: "Aktor Update-Only: Bulk Activate, Bulk Deactivate, dan Cancel Version dari Alert"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-85
  - TC-FA-TDC-86
  - TC-FA-TDC-87
  - TC-FA-TDC-301
coverage:
  web: automated
---

# Aktor Update-Only: Bulk Activate, Bulk Deactivate, dan Cancel Version dari Alert

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | Blok langkah |
|---|---|---|---|
| Update-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_UPDATEONLY_PASSWORD` | langkah 1 sampai 38 |

- Login di hook `before` spec ini sebagai Update-Only (Manage accounting); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan data lewat API (class, versi, Used By, tabel tanpa class), akun per role, dan perubahan capability role. Endpoint tidak dikarang (S-13).
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE): kode dan nilai kolom class Example Data. Nama env password di tabel "Role yang diuji" belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; penulis script mendaftarkannya.
- Data (kondisi awal): tabel berisi 9 class sesuai Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; 9 baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Hook `before` spec ini menyeed ulang kondisi itu lewat API dan hook `after` memulihkannya; Class Code dibatasi 15 karakter sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Akun aktor sudah tersedia dan memiliki akses tab (Read) ke Settings > Accounting > Tax Depreciation Class.
- Jam sistem uji: 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00); Fiscal Year Start Januari. Jam server dan jam browser diatur bersama lewat kendali jam suite (`suite.md`) dan dipulihkan di hook `after`. Jam diatur pada blok TC-FA-TDC-301 (langkah 22) dan dipulihkan di langkah 38 serta hook `after`.
- Kebutuhan data: NB-4 Active dengan Used By 0, NB-KHS Active dengan Used By 0, NB-OLD Inactive, dan class tambahan `NB-ARC` Inactive (di luar Example Data; TC-FA-TDC-86); class `KHS-C1` – Kelompok cancel uji: versi Current tanpa Effective From (Useful Life 8, Straight Line dan Declining Balance) dan satu versi Scheduled Effective From Jan 2027 (Useful Life 10, Straight Line dan Declining Balance), Used By 0 (TC-FA-TDC-301). Dengan NB-ARC dan KHS-C1 tabel berisi 11 baris sehingga baris KHS-C1 dibuka lewat Search.
- Flag Guided Tooltip halaman ini disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`; spec ini tidak mengubah state global kecuali yang tertulis di bawah.

## Test Steps


### Bulk seleksi campuran Active dan Inactive (TC-FA-TDC-87)

1. Centang baris NB-4 (Active, Used By 0) dan NB-OLD (Inactive)
2. Verifikasi Bulk Action Bar menampilkan `Deactivate` dan `Activate`
3. Klik aksi `Deactivate` pada Bulk Action Bar
4. Verifikasi dialog single `Deactivate Tax Depreciation Class` tampil dengan bullet `NB-4 – Bukan bangunan – Kelompok 4` saja
5. Klik `[Deactivate]`
6. Verifikasi toast sukses `Success, tax depreciation class has been deactivated.`
7. Verifikasi NB-OLD tetap Off dan tidak dihitung

### Bulk Activate (TC-FA-TDC-86)

8. Centang baris NB-OLD dan NB-ARC (keduanya Inactive)
9. Klik aksi `Activate` pada Bulk Action Bar
10. Verifikasi dialog `Activate Tax Depreciation Classes` tampil dengan bullet kedua class dan teks `Are you sure you want to activate them?`
11. Klik `[Activate]`
12. Verifikasi toast sukses `Success, tax depreciation class has been activated.`
13. Verifikasi toggle NB-OLD dan NB-ARC berubah On

### Bulk Deactivate (TC-FA-TDC-85)

14. Pulihkan NB-4 ke status Active lewat API hingga tersimpan, lalu muat ulang halaman
15. Centang baris NB-4 dan NB-KHS (keduanya Active, Used By 0)
16. Klik aksi `Deactivate` pada Bulk Action Bar
17. Verifikasi dialog `Deactivate Tax Depreciation Classes` tampil dengan bullet `NB-4 – Bukan bangunan – Kelompok 4` dan `NB-KHS – Kelompok khusus pernah diposting`, teks `Are you sure you want to deactivate them?`
18. Klik `[Deactivate]`
19. Verifikasi toast sukses `Success, tax depreciation class has been deactivated.`
20. Verifikasi toggle NB-4 dan NB-KHS berubah Off
21. Verifikasi seleksi di-reset

### Cancel version dari Alert (TC-FA-TDC-301)

22. Atur jam sistem uji ke 15 Okt 2026 10:00 WIB (jam server dan jam browser bersama)
23. Ketik Search `KHS-C1`, tekan Enter
24. Klik link Class Code `KHS-C1` pada tabel
25. Klik `[Cancel scheduled version]` pada Alert
26. Klik `[Cancel version]`
27. Verifikasi toast sukses `Success, scheduled version has been cancelled.`
28. Verifikasi Drawer Edit tetap terbuka
29. Verifikasi Alert versi Scheduled hilang
30. Klik tautan `View versions`
31. Verifikasi Modal Versions: baris `Jan 2027` berstatus `Cancelled`
32. Verifikasi Modal Versions: baris `—` berstatus `Current`
33. Tutup Modal Versions
34. Tutup Drawer dengan `[×]`
35. Verifikasi baris tabel `KHS-C1`: Useful Life `8` dan Effective From `—`
36. Hover sel Effective From baris `KHS-C1`
37. Verifikasi tooltip `Next version starts Jan 2027.` tidak ada lagi
38. Pulihkan jam sistem uji ke jam semula, lalu klik `(←)` pada kotak Search

## Notes

- Satu aktor (Update-Only) untuk seluruh spec; login di hook `before`, tidak ada ganti akun. Spec melewati sekitar 35 langkah. Alasan: seluruh blok satu aktor dan satu topik (aksi Update atas status dan versi), berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC diubah dari nomor (85, 86, 87) menjadi 87, 86, 85 karena TC-FA-TDC-87 menonaktifkan NB-4 sedangkan TC-FA-TDC-85 membutuhkan NB-4 Active; NB-4 dipulihkan lewat API sebelum TC-FA-TDC-85 (langkah penghubung). TC-FA-TDC-301 diletakkan terakhir karena membutuhkan jam sistem tertentu.
- Langkah penghubung (S-03): pemulihan NB-4 lewat API, Search `KHS-C1` untuk menemukan baris target (tabel 11 baris; R-16), menutup Modal Versions dan Drawer, serta mengatur dan memulihkan jam (langkah 22 dan 38); `(←)` pada Search di langkah 38 membersihkan Search (S-09).
- Temuan untuk QA:
  - Akun per role tidak punya nomor Pre-setup, email, atau company di TC; Prerequisites menandainya "disediakan tim FE" dan nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data milik spec di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - TC-301 butir d menyebut tooltip `Next version starts Jan 2027.` tidak ada lagi tanpa cara memicunya; spec memakai hover pada sel Effective From.
  - Post Condition TC-301 ("Class tetap memakai versi Current", entri log L-09 di section 5) tidak punya langkah observasi di TC; tidak diasersi (S-01). Entri log diasersi di spec pencatatan log.
  - TC-85 butir c "seleksi di-reset" diasersi sebagai tidak ada baris tercentang; TC-87 tidak menyebut keadaan seleksi sesudah aksi.
