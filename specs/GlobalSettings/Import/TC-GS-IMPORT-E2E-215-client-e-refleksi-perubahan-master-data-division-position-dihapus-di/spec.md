---
id: TC-GS-IMPORT-E2E-215-client-e-refleksi-perubahan-master-data-division-position-dihapus-di
title: "Client E: refleksi perubahan master data (Division/Position dihapus, di-rename, dibuat; Represented By dinonaktifkan) pada baris draft"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-522
  - TC-GS-IMPORT-523
  - TC-GS-IMPORT-524
  - TC-GS-IMPORT-525
  - TC-GS-IMPORT-527
  - TC-GS-IMPORT-807
  - TC-GS-IMPORT-808
coverage:
  web: automated
---

# Client E: refleksi perubahan master data (Division/Position dihapus, di-rename, dibuat; Represented By dinonaktifkan) pada baris draft

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memutasi master data Client E (state global) dan memulihkannya (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC_PASSWORD`.
- Pelaku kedua (pemicu via sesi API, bukan sesi UI): Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC2_PASSWORD` (nama env baru). Sesi API menghapus, me-rename, dan membuat Division dan Position serta menonaktifkan User Login; klien HTTP dan kontrak endpoint disediakan tim FE/BE (tidak tertulis di TC).
- Layar awal: hook `beforeEach` membuka Import > User Login Client E; Sub-Tab User Non Login dibuka di langkah.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Pre-setup Client E: Division `Engineering`, `Marketing`, `Finance`, `Warehouse`, `Gudang`; Position `Senior Developer`, `Finance Manager`, `Technician`, `Supervisor`, `Store Manager`; User Login aktif `rina.admin.e`, `budi.manager.e`, `dewi.anggraini.e` (@example.com). Division `Gudang` dan Position `Technician` tidak direferensikan user (Pre-setup Client E). Division `Logistik` dan Position `Store Supervisor` belum ada. Nama literal dipakai karena asersi bergantung pada nama dan teks error (pengecualian S-12 butir (ii)); Division/Position `Gudang`, `Technician`, `Logistik`, `Store Supervisor` dipulihkan atau dihapus oleh spec.
- Data Dinamis (draft Client E, disiapkan lewat skrip seed sebelum tiap TC; Client E direset tanpa draft, Kontrak Fixture R1):
  - D-62: draft User Login 3 baris `pending` dari `user-login-ref.csv`: Row # 1 Division `Gudang` dan Position `Technician`, Row # 2 Division `Warehouse` dan Access `Global Settings;Fixed Asset`, Row # 3 Division `Marketing`; dipakai TC-GS-IMPORT-522, 523, 524, 807.
  - D-63: draft User Non Login 3 baris `pending` dari `user-non-login-ref.csv`: Row # 1 Represented By `budi.manager.e@example.com`, Row # 2 dan 3 Represented By `dewi.anggraini.e@example.com`; dipakai TC-GS-IMPORT-525.
  - `user-login-logistik.csv` (header First Name; Last Name; Email; Division; Access; 1 baris, Email unik dengan suffix per run `+{runId}-215`, Division `Logistik`, Access `Global Settings`) untuk TC-GS-IMPORT-527; `user-login-position.csv` (header First Name; Last Name; Email; Division; Position; Access; 1 baris, Email unik dengan suffix per run, Division `Engineering`, Position `Store Supervisor`, Access `Global Settings`) untuk TC-GS-IMPORT-808. Draft dibuat lewat upload UI dan tidak di-commit.
- Urutan TC: 523, 807, 525, 527, 808, 522, 524 (penghapusan Division dan Position, TC-522 dan 524, paling akhir). Pemulihan dilakukan sebagai langkah aksi di akhir tiap blok (Kontrak Fixture R2) dan oleh hook `after` sebagai cadangan.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): Division `Gudang` dibuat ulang bila hilang atau dikembalikan dari `Gudang Pusat`; Position `Technician` dibuat ulang bila hilang atau dikembalikan dari `Technician Lead`; Division `Logistik` dan Position `Store Supervisor` dihapus; User Login `budi.manager.e@example.com` diaktifkan kembali; draft Client E dibuang.
- Kemampuan teknis: skrip seed D-62, D-63; skrip reset draft Client E; sesi API Admin kedua; pemilihan berkas.
- State global: master data Client E (dipulihkan), flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Division di-rename (TC-GS-IMPORT-523)

1. Admin kedua Client E (sesi API) me-rename Division `Gudang` menjadi `Gudang Pusat` hingga tersimpan
2. Tekan `F5` pada halaman Import
3. Verifikasi Row # 1 (Division `Gudang`) berstatus `error`
4. Verifikasi Staging Metric Cards: Ready to Import 2, Errors 1
5. Verifikasi Error Summary Callout memuat `Division not found` dengan badge "1 row"
6. Pulihkan: Admin kedua me-rename Division `Gudang Pusat` kembali menjadi `Gudang`, buat ulang draft D-62, muat ulang halaman

### Position di-rename (TC-GS-IMPORT-807)

7. Admin kedua Client E (sesi API) me-rename Position `Technician` menjadi `Technician Lead` hingga tersimpan
8. Tekan `F5` pada halaman Import
9. Verifikasi Row # 1 (Position `Technician`) berstatus `error`
10. Verifikasi Staging Metric Cards: Ready to Import 2, Errors 1
11. Verifikasi Error Summary Callout memuat `Position not found` dengan badge "1 row"
12. Pulihkan: Admin kedua me-rename Position `Technician Lead` kembali menjadi `Technician`, buat ulang draft D-62, muat ulang halaman

### Represented By dinonaktifkan (TC-GS-IMPORT-525)

13. Pindah ke Sub-Tab User Non Login, seed draft D-63 lewat skrip seed, muat ulang halaman
14. Admin kedua Client E (sesi API) menonaktifkan User Login `budi.manager.e@example.com` hingga tersimpan
15. Tekan `F5` pada halaman Import
16. Verifikasi Row # 1 berstatus `error`
17. Verifikasi Error Summary Callout memuat `Represented by must be an active User Login account` dengan badge "1 row"
18. Verifikasi Row # 2 dan 3 tetap `pending`
19. Verifikasi Staging Metric Cards: Ready to Import 2, Errors 1
20. Pulihkan: Admin kedua mengaktifkan kembali User Login `budi.manager.e@example.com`, buang draft User Non Login dan draft User Login (D-62) lewat skrip reset, muat ulang halaman, buka Sub-Tab User Login

### Division baru meresolve baris error (TC-GS-IMPORT-527)

21. Klik `[Upload File]` dan pilih `user-login-logistik.csv`
22. Klik `[Confirm Mapping]`
23. Verifikasi Row # 1 berstatus `error`
24. Verifikasi Error Summary Callout memuat `Division not found` dengan badge "1 row"
25. Admin kedua Client E (sesi API) membuat Division `Logistik` hingga tersimpan
26. Tekan `F5` pada halaman Import
27. Verifikasi Row # 1 pulih ke `pending`
28. Verifikasi Staging Metric Cards: Ready to Import 1, Errors 0
29. Verifikasi Error Summary Callout tidak tampil
30. Pulihkan: Admin kedua menghapus Division `Logistik`, buang draft User Login lewat skrip reset, muat ulang halaman

### Position baru meresolve baris error (TC-GS-IMPORT-808)

31. Klik `[Upload File]` dan pilih `user-login-position.csv`
32. Klik `[Confirm Mapping]`
33. Verifikasi Row # 1 berstatus `error`
34. Verifikasi Error Summary Callout memuat `Position not found` dengan badge "1 row"
35. Admin kedua Client E (sesi API) membuat Position `Store Supervisor` hingga tersimpan
36. Tekan `F5` pada halaman Import
37. Verifikasi Row # 1 pulih ke `pending`
38. Verifikasi Staging Metric Cards: Ready to Import 1, Errors 0
39. Verifikasi Error Summary Callout tidak tampil
40. Pulihkan: Admin kedua menghapus Position `Store Supervisor`, buang draft User Login lewat skrip reset

### Division dihapus (TC-GS-IMPORT-522)

41. Seed draft D-62 lewat skrip seed, lalu buka Import > User Login
42. Admin kedua Client E (sesi API) menghapus Division `Gudang` hingga tersimpan
43. Tekan `F5` pada halaman Import
44. Verifikasi Row # 1 berstatus `error`
45. Verifikasi Staging Metric Cards: Ready to Import 2, Errors 1
46. Verifikasi Error Summary Callout memuat `Division not found` dengan badge "1 row"
47. Klik row action `⋯` pada Row # 1
48. Verifikasi menu row action Row # 1 memuat `[Create Missing Divisions]`
49. Pulihkan: Admin kedua membuat ulang Division `Gudang`, buat ulang draft D-62, muat ulang halaman

### Position dihapus (TC-GS-IMPORT-524)

50. Admin kedua Client E (sesi API) menghapus Position `Technician` hingga tersimpan
51. Tekan `F5` pada halaman Import
52. Verifikasi Row # 1 (Position `Technician`) berstatus `error`
53. Verifikasi Staging Metric Cards: Ready to Import 2, Errors 1
54. Verifikasi Error Summary Callout memuat `Position not found` dengan badge "1 row"
55. Klik row action `⋯` pada Row # 1
56. Verifikasi menu row action Row # 1 memuat `[Create Missing Positions]`
57. Pulihkan: Admin kedua membuat ulang Position `Technician`, buang draft User Login lewat skrip reset

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 57 langkah, di atas 35 langkah. Alasan: tujuh blok berpola sama (mutasi master data Client E lewat sesi API, F5, baca status baris draft) pada satu client dan satu akun; tiap blok berdiri sendiri dan dipulihkan eksplisit (langkah 6, 12, 20, 30, 40, 49, 57), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- P-2: Admin kedua hanya memicu perubahan master data lewat sesi API; hasil diasersi hanya di sesi admin pertama.
- Langkah pemulihan (6, 12, 20, 30, 40, 49, 57) adalah aksi tanpa `Verifikasi` (S-09); hook `after` adalah cadangan. Langkah 13 dan 41 menyiapkan draft (penghubung, S-03). Langkah 20 juga membuang draft User Login D-62 yang tersisa dari blok sebelumnya agar upload langkah 21 tidak memicu Dialog Append to Draft (S-03).
- Urutan 523, 807, 525, 527, 808, 522, 524 menempatkan penghapusan Division dan Position (TC-522 dan 524) paling akhir; nomor TC di sourceTc tetap (S-05).
- Temuan untuk QA:
  - TC-GS-IMPORT-522, 523, 524, 807 Precondition bergantung pada TC dependensi TC-GS-IMPORT-759 (pembuat D-62); spec menyiapkan D-62 lewat skrip seed. TC-GS-IMPORT-525 bergantung pada TC-GS-IMPORT-760 (D-63), disiapkan dengan cara yang sama.
  - TC-GS-IMPORT-522 sampai 808 menghapus atau me-rename Division `Gudang` dan Position `Technician` yang merupakan data Pre-setup bersama (S-06); TC dan Kontrak Fixture R2 mensyaratkan pemulihan, sehingga spec memulihkannya dan menyatakan efeknya di Prerequisites.
  - TC-GS-IMPORT-527 dan 808 Data Uji menulis "Email unik"; spec memakai suffix per run.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
