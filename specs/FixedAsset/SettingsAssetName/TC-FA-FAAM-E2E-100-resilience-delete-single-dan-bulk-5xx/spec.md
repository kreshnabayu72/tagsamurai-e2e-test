---
id: TC-FA-FAAM-E2E-100-resilience-delete-single-dan-bulk-5xx
title: "Resilience Delete: Gagal 5xx Single, Bulk Semua Gagal, Request Bulk Gagal, dan Bulk Sebagian Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-270
  - TC-FA-FAAM-291
  - TC-FA-FAAM-292
  - TC-FA-FAAM-293
coverage:
  web: automated
---

# Resilience Delete: Gagal 5xx Single, Bulk Semua Gagal, Request Bulk Gagal, dan Bulk Sebagian Gagal

## Prerequisites

- Mode: FE+BE (backend nyata dengan `Spectra.intercept()` parsial; bukan `Mode: mock` karena asersi menyangkut state server: record tetap ada, entri Changelog, dan sebagian item terhapus).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; seed API per TC mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Dinamis (suffix `{runId}-100`, seed di hook `before`, cleanup di hook `after` untuk yang tersisa); Search `{runId}-100` menampilkan kelima baris dalam satu halaman:
  - `Warehouse Pallet 270 {runId}-100`: salinan Pre-setup #13 (Total Asset 0), target Delete yang digagalkan intercept (TC-FA-FAAM-270).
  - `Bulk Clean A {runId}-100` dan `Bulk Clean B {runId}-100`: salinan Pre-setup #13c (Total Asset 0), target bulk yang digagalkan seluruhnya (TC-FA-FAAM-292 dan TC-FA-FAAM-293).
  - `Bulk Clean A 291 {runId}-100` dan `Bulk Clean B 291 {runId}-100`: salinan Pre-setup #13c (Total Asset 0); `Bulk Clean A 291 {runId}-100` terhapus dan `Bulk Clean B 291 {runId}-100` tetap karena kegagalan server (TC-FA-FAAM-291).
- Kemampuan teknis: `Spectra.intercept()` memaksa respons 5xx pada request Delete Asset Name atau Bulk Delete Asset Name (hanya request tulis itu; request daftar dan Changelog tidak di-intercept) dan melepasnya segera setelah pemicu (S-09); pencocokan request bulk per item mengikuti kontrak Bulk Delete yang tidak diuraikan TC (lihat Temuan untuk QA). Disediakan tim BE/FE: membaca jumlah entri Changelog tanpa mengubahnya (baseline N0, dicatat sebelum aksi pertama).
- State global: tidak ada yang diubah spec ini; intercept dilepas di tiap blok dan hook `after` tetap memastikan tidak ada intercept tersisa.

## Test Steps

1. Catat jumlah entri Changelog sebagai N0 lewat kemampuan baca
2. Ketik Search `{runId}-100`, tekan Enter

### TC-FA-FAAM-270: Delete gagal 5xx, toast error dan baris tetap

3. Klik `⋯` baris `Warehouse Pallet 270 {runId}-100` lalu `Delete`
4. Aktifkan intercept: respons request Delete Asset Name dipaksa 500
5. Klik `[Delete]`
6. Verifikasi toast `Error, failed to delete asset name.` tampil
7. Verifikasi baris `Warehouse Pallet 270 {runId}-100` tetap ada
8. Lepas intercept

### TC-FA-FAAM-292: Semua item gagal server, toast error dan tidak ada yang terhapus

9. Centang baris `Bulk Clean A {runId}-100`, `Bulk Clean B {runId}-100`
10. Klik `Bulk Action` lalu `Delete`
11. Aktifkan intercept: respons kegagalan server dipaksa untuk kedua item
12. Klik `[Delete]`
13. Verifikasi toast `Error, failed to delete asset name.` tampil
14. Verifikasi kedua baris `Bulk Clean A {runId}-100` dan `Bulk Clean B {runId}-100` tetap
15. Verifikasi tabel di-refresh
16. Lepas intercept
17. Klik icon `×`

### TC-FA-FAAM-293: Request Bulk Delete gagal 5xx, bar dan seleksi dipertahankan

18. Centang baris `Bulk Clean A {runId}-100`, `Bulk Clean B {runId}-100`
19. Klik `Bulk Action` lalu `Delete`
20. Aktifkan intercept: respons 500 dipaksa untuk seluruh request Bulk Delete
21. Klik `[Delete]`
22. Verifikasi toast `Error, failed to delete asset name.` tampil
23. Verifikasi bar bulk dan seleksi dipertahankan (bar tampil, kedua baris tetap tercentang)
24. Verifikasi tabel di-refresh
25. Lepas intercept
26. Klik icon `×`

### TC-FA-FAAM-291: Kegagalan server pada satu item, item lain tetap terhapus dan toast campuran

27. Centang baris `Bulk Clean A 291 {runId}-100`, `Bulk Clean B 291 {runId}-100`
28. Klik `Bulk Action` lalu `Delete`
29. Aktifkan intercept: kegagalan server dipaksa hanya untuk item `Bulk Clean B 291 {runId}-100`
30. Klik `[Delete]`
31. Verifikasi toast `Success, asset name has been deleted. Some items were skipped.` tampil
32. Verifikasi `Bulk Clean A 291 {runId}-100` terhapus (hilang dari daftar)
33. Verifikasi `Bulk Clean B 291 {runId}-100` tetap di daftar
34. Verifikasi tabel di-refresh
35. Lepas intercept
36. Baca jumlah entri Changelog lewat kemampuan baca
37. Verifikasi jumlah entri Changelog sama dengan N0 + 1 (hanya Delete `Bulk Clean A 291 {runId}-100`; tanpa entri log untuk item gagal)

## Notes

- Mode: FE+BE dengan intercept. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): baseline N0 (langkah 1, S-12), Search untuk menemukan baris target (R-16, langkah 2), melepas intercept segera sesudah pemicu (langkah 8, 16, 25, 35; S-09), dan membatalkan seleksi (langkah 17, 26; S-09). Intercept dilepas sesudah toast diasersi karena respons 5xx sudah diproses.
- Asersi "tanpa entri log" TC-FA-FAAM-270 dan "tanpa baris log untuk item gagal" TC-FA-FAAM-291 diamati sekali pada langkah 36 dan 37: satu-satunya entri baru sejak baseline N0 adalah Delete `Bulk Clean A 291 {runId}-100`, sehingga tidak ada entri dari kegagalan di TC-FA-FAAM-270, TC-FA-FAAM-292, TC-FA-FAAM-293, dan item gagal TC-FA-FAAM-291.
- Alasan melewati sekitar 35 langkah (37 langkah): seluruh blok berkelas harness sama (fault injection `Spectra.intercept()` pada Delete dan Bulk Delete, kelas ringan yang digabung per modul menurut bagian 3 prinsip 13), memakai satu Search `{runId}-100`, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; Expected tiap blok tetap diasersi per klausa (S-01).
- Temuan untuk QA:
  - TC-FA-FAAM-291 langkah 3 ("kegagalan server hanya untuk `Bulk Clean B 291`") dan TC-FA-FAAM-292 langkah 3 ("kedua item") tidak menyebut apakah Bulk Delete mengirim satu request per item atau satu request berisi daftar item; cara intercept mencocokkan item mengikuti kontrak Bulk Delete yang disediakan tim BE/FE.
  - TC-FA-FAAM-270 tidak menyebut apakah dialog Delete tertutup sesudah toast error; spec tidak mengasersi keadaan dialog dan menganggap langkah berikutnya dijalankan pada List tanpa dialog terbuka.
  - TC-FA-FAAM-270 Expected c ("Tanpa entri log") tidak punya langkah observasi di TC; spec mengamatinya kumulatif pada langkah 36 dan 37.
  - TC-FA-FAAM-292 dan TC-FA-FAAM-293 memakai `Bulk Clean A` dan `Bulk Clean B` Pre-setup; spec memakai salinan bersuffix karena kedua TC tidak menghapus data dan nama literal akan bentrok dengan spec lain.
