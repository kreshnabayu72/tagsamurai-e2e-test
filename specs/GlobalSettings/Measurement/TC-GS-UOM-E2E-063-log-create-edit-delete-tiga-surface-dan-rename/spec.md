---
id: TC-GS-UOM-E2E-063-log-create-edit-delete-tiga-surface-dan-rename
title: "Pencatatan Log Create, Edit, Delete di Changelog, System Log, dan Activity Log serta Riwayat Rename"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-213
  - TC-GS-UOM-214
  - TC-GS-UOM-215
  - TC-GS-UOM-216
  - TC-GS-UOM-219
  - TC-GS-UOM-221
  - TC-GS-UOM-222
  - TC-GS-UOM-223
  - TC-GS-UOM-265
  - TC-GS-UOM-266
coverage:
  web: automated
---

# Pencatatan Log Create, Edit, Delete di Changelog, System Log, dan Activity Log serta Riwayat Rename

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Master Reference > Measurement.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel `seen` oleh hook suite (lihat `suite.md`, bagian Hook suite).
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi), semuanya bebas relasi dan milik spec ini. Entri log harus bersumber dari aksi di spec ini (tepat 1 entri per aksi), sehingga unit yang menjadi objek Edit dan Delete dibuat spec sendiri dan tidak memakai Population D-01:
  - `Span {runId}-063` / `sp` (D-13): dibuat spec lewat UI pada TC-GS-UOM-213.
  - `Gallon {runId}-063` / `gal`, `Ounce {runId}-063` / `oz`, `Pound {runId}-063` / `lb`, dan `Barrel {runId}-063` / `bbl` (D-08): di-seed lewat API di hook `before` (setara dependensi TC-GS-UOM-70, 71, 72, dan 55; pembuatannya bukan objek uji). Gallon di-rename menjadi `US Gallon {runId}-063` (TC-GS-UOM-214) lalu `Imperial Gallon {runId}-063` (TC-GS-UOM-221); Ounce diubah Symbol menjadi `oz.`; Pound diubah menjadi `Pound Mass {runId}-063` / `lbm`; Barrel dihapus spec lewat UI pada TC-GS-UOM-219.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API unit milik spec dengan nama yang masih ada (`Span`, `Gallon` atau `US Gallon` atau `Imperial Gallon`, `Ounce`, `Pound` atau `Pound Mass`, `Barrel`) bersuffix `{runId}-063`.
- Kemampuan teknis: akses Sesi aktor (Total Control) ke Detail User Sari Dewi > Tab System Log dan Global Settings > Activity Log.
- Tidak ada state global yang diubah.
- TC-GS-UOM-213, 214, 215, 216, 219, 221, 222, 223, 265, 266: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement.

## Test Steps

### TC-GS-UOM-213: Create mencatat entri Unit Name di Changelog

1. Klik [+ Unit], isi Unit Name `Span {runId}-063` dan Symbol `sp`, klik [Submit]
2. Tunggu aksi selesai (form tertutup)
3. Buka Changelog, ketik Search `Span {runId}-063`, tekan Enter
4. Verifikasi Changelog: baris Action `Create`, Unit Name `Span {runId}-063`, Field `Unit Name`, Old Value `—`, New Value `Span {runId}-063`, Modified By `Sari D`
5. Verifikasi hasil Search hanya memuat satu baris Create
6. Verifikasi hasil Search tidak memuat baris Field `Symbol` untuk `Span {runId}-063`
7. Tutup Changelog

### TC-GS-UOM-214: Edit Unit Name mencatat satu entri Field Unit Name

8. Ketik Search `Gallon {runId}-063`, tekan Enter, klik `⋯` pada baris tersebut > Edit, ubah Unit Name menjadi `US Gallon {runId}-063`, klik [Save]
9. Tunggu aksi selesai (modal tertutup)
10. Buka Changelog, ketik Search `Gallon {runId}-063`, tekan Enter
11. Verifikasi Changelog: baris Action `Edit`, Unit Name `US Gallon {runId}-063`, Field `Unit Name`, Old Value `Gallon {runId}-063`, New Value `US Gallon {runId}-063`
12. Verifikasi hasil Search tidak memuat baris Field `Symbol` untuk unit ini
13. Tutup Changelog

### TC-GS-UOM-215: Edit Symbol mencatat satu entri Field Symbol

14. Ganti isi kotak search dengan `Ounce {runId}-063`, tekan Enter, klik `⋯` pada baris tersebut > Edit, ubah Symbol menjadi `oz.`, klik [Save]
15. Tunggu aksi selesai (modal tertutup)
16. Buka Changelog, ketik Search `Ounce {runId}-063`, tekan Enter
17. Verifikasi Changelog: baris Action `Edit`, Field `Symbol`, Old Value `oz`, New Value `oz.`
18. Tutup Changelog

### TC-GS-UOM-216: Edit Unit Name dan Symbol mencatat dua entri terpisah

19. Ganti isi kotak search dengan `Pound {runId}-063`, tekan Enter, klik `⋯` pada baris tersebut > Edit, ubah Unit Name menjadi `Pound Mass {runId}-063` dan Symbol menjadi `lbm`, klik [Save]
20. Tunggu aksi selesai (modal tertutup)
21. Buka Changelog, ketik Search `Pound {runId}-063`, tekan Enter
22. Verifikasi Changelog: baris Field `Unit Name` dengan Old Value `Pound {runId}-063` dan New Value `Pound Mass {runId}-063`
23. Verifikasi Changelog: baris Field `Symbol` dengan Old Value `lb` dan New Value `lbm`
24. Tutup Changelog

### TC-GS-UOM-221: Entri lama tidak berubah setelah rename berikutnya

25. Ganti isi kotak search dengan `US Gallon {runId}-063`, tekan Enter, klik `⋯` pada baris tersebut > Edit, ubah Unit Name menjadi `Imperial Gallon {runId}-063`, klik [Save]
26. Tunggu aksi selesai (modal tertutup)
27. Buka Changelog, ketik Search `Gallon {runId}-063`, tekan Enter
28. Verifikasi entri lama tetap Old Value `Gallon {runId}-063` dan New Value `US Gallon {runId}-063`
29. Verifikasi entri baru Old Value `US Gallon {runId}-063` dan New Value `Imperial Gallon {runId}-063`
30. Tutup Changelog

### TC-GS-UOM-219: Delete mencatat satu entri dengan New Value strip

31. Ganti isi kotak search dengan `Barrel {runId}-063`, tekan Enter, klik `⋯` pada baris tersebut > Delete, klik [Delete] pada dialog
32. Tunggu aksi selesai (toast sukses tampil)
33. Buka Changelog, ketik Search `Barrel {runId}-063`, tekan Enter
34. Verifikasi Changelog: baris Action `Delete`, Unit Name `Barrel {runId}-063`, Field `Unit Name`, Old Value `Barrel {runId}-063`, New Value `—`
35. Verifikasi hasil Search hanya memuat satu baris Delete
36. Verifikasi hasil Search tidak memuat baris Field `Symbol` untuk `Barrel {runId}-063`
37. Tutup Changelog

### TC-GS-UOM-222 dan TC-GS-UOM-265: System Log Detail User aktor

38. Buka Global Settings > User > Detail Sari Dewi > Tab System Log, ketik Search `{runId}-063`, tekan Enter
39. Verifikasi System Log: kolom `Date | Action | Object | Name | Field | Old Value | New Value` tampil
40. Verifikasi System Log: tepat satu baris Create dengan Object `Measurement`, Name `Span {runId}-063`, Field `Unit Name`, Old Value `—`, New Value `Span {runId}-063`
41. Verifikasi System Log: tepat satu baris Edit dengan Object `Measurement`, Name `US Gallon {runId}-063`, Field `Unit Name`, Old Value `Gallon {runId}-063`, New Value `US Gallon {runId}-063`
42. Verifikasi System Log: tepat satu baris Edit dengan Object `Measurement`, Name `Ounce {runId}-063`, Field `Symbol`, Old Value `oz`, New Value `oz.`
43. Verifikasi System Log: tepat satu baris Delete dengan Object `Measurement`, Name `Barrel {runId}-063`, Field `Unit Name`, Old Value `Barrel {runId}-063`, New Value `—`

### TC-GS-UOM-223 dan TC-GS-UOM-266: Activity Log Global Settings

44. Buka Global Settings > Activity Log, pilih tab `User Action`, ketik Search `{runId}-063`, tekan Enter
45. Verifikasi Activity Log: tepat satu baris Edit dengan Object `Measurement`, Name `US Gallon {runId}-063`, Field `Unit Name`, Old Value `Gallon {runId}-063`, New Value `US Gallon {runId}-063`, Modified By `Sari D`
46. Verifikasi Activity Log: tepat satu baris Create dengan Object `Measurement`, Name `Span {runId}-063`, Field `Unit Name`, Old Value `—`, New Value `Span {runId}-063`, Modified By `Sari D`
47. Verifikasi Activity Log: tepat satu baris Edit dengan Object `Measurement`, Name `Ounce {runId}-063`, Field `Symbol`, Old Value `oz`, New Value `oz.`, Modified By `Sari D`
48. Verifikasi Activity Log: tepat satu baris Delete dengan Object `Measurement`, Name `Barrel {runId}-063`, Field `Unit Name`, Old Value `Barrel {runId}-063`, New Value `—`, Modified By `Sari D`

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Kelas harness: pencatatan log (tiga surface).
- Urutan TC di spec berbeda dari urutan sumber: Create (213), Edit Unit Name (214), Edit Symbol (215), Edit Unit Name dan Symbol (216), rename kedua (221, sesudah 214 karena 214 mengecek hasil rename pertama), Delete (219, paling akhir untuk aksi, prinsip 5), lalu pembacaan System Log dan Activity Log sekali per surface (222, 265 dan 223, 266) agar tiap surface dibuka sekali.
- Dependensi (TC-GS-UOM-70, 71, 72, 55/96) dijalankan sebagai langkah atau seeding di spec ini, bukan menumpang spec lain. Unit sumber yang bernama literal (Gallon, Ounce, Pound, Barrel) diganti unit milik spec bersuffix `{runId}-063` (S-06, S-12); nama pada Expected TC diganti nama bersuffix.
- TC-GS-UOM-222 menyebut Name `US Gallon` untuk entri Edit Gallon; spec mengasersi entri Edit rename pertama (Old `Gallon`, New `US Gallon`) pada langkah 41 dan 45, yang tetap utuh setelah rename kedua (TC-GS-UOM-221).
- Entri log dikenali lewat nama bersuffix `{runId}-063`; entri milik spec atau run lain diabaikan. Hitungan "tepat satu baris" memakai Search `{runId}-063` pada surface yang sedang terbuka (S-12, tanpa angka absolut total entri).
- Asersi "tidak ada baris Field `Symbol`" (langkah 6, 12, 36) adalah bagian isi pencatatan satu aksi (hasil Search yang sama dengan baris yang diasersi sebagai anchor), bukan asersi absence kelas g. Asersi absence (tanpa pencatatan) ada di spec `TC-GS-UOM-E2E-065-log-absence-no-op-case-only-dan-relasi-konsumen`.
- Langkah penghubung: langkah 2, 9, 15, 20, 26, dan 32 (menunggu aksi selesai sebelum membuka Changelog; S-12 butir 8), langkah 3, 10, 16, 21, 27, dan 33 (Search baris log milik unit), langkah 7, 13, 18, 24, 30, dan 37 (menutup Changelog), langkah 8, 14, 19, 25, dan 31 (Search baris target pada tabel; tabel memuat lebih dari satu halaman), langkah 38 dan 44 (navigasi ke System Log dan Activity Log, Search `{runId}-063`; langkah 44 juga memilih tab `User Action`).
- Spec memuat 48 langkah (melewati batas 35 langkah); seluruhnya satu kelas harness (pencatatan log), dengan blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) yang tidak dihitung ke batas (konvensi bagian 3, prinsip 13). Aksi dan baca log tiap TC berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-UOM-213 sampai 216, 219, dan 221 tidak menyebut toast sukses sebagai Expected; spec tidak mengasersi toast aksi dan memakai langkah "Tunggu aksi selesai".
  - TC-GS-UOM-222 dan 223 menyebut dependensi hanya TC-GS-UOM-70 sedangkan Expected 265 dan 266 membutuhkan pula Create Span, Edit Symbol Ounce, dan Delete Barrel; spec menjalankan keseluruhan aksi itu sebelum membaca System Log dan Activity Log.
  - TC-GS-UOM-222 tidak menyebut Modified By pada System Log (kolom System Log tidak memuat Modified By); sesuai TC.
  - TC-GS-UOM-223 dan 266 menulis "Buka Global Settings > Activity Log" tanpa menyebut tab; log mutasi Measurement ada di tab `User Action` (`global-settings/activity-log/PRD/activity-log.md` §4.1.2), sehingga langkah 44 memilih tab `User Action` sebelum Search. Isi `Verifikasi` langkah 45 sampai 48 tidak berubah.
