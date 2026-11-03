---
id: TC-AC-SG-E2E-101-konkurensi-dua-admin-perubahan-saat-delete-menunggu-konfirmasi-dan-member-baru-saat-bulk
title: "Konkurensi Dua Admin: Perubahan saat Delete Menunggu Konfirmasi dan Member Baru saat Bulk Delete"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-383
  - TC-AC-SG-384
  - TC-AC-SG-394
coverage:
  web: automated
---

# Konkurensi Dua Admin: Perubahan saat Delete Menunggu Konfirmasi dan Member Baru saat Bulk Delete

## Prerequisites

- Mode: FE+BE.
- Sesi A (akun aktor pertama, sesi UI): Total Control entitas Distributor Race, `totalControlRaceA_automated_{namaCompany}@qwertysystem.net` (Pre-setup #32), password `Spectra.env.AC_SG_RACEA_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Sesi B (sesi API aktor, hanya memicu perubahan state; Pre-setup #39): Total Control entitas Distributor Race, `totalControlRaceB_automated_{namaCompany}@qwertysystem.net` (Pre-setup #32), password `Spectra.env.AC_SG_RACEB_PASSWORD`. Login API (password) memakai token yang tidak dihitung sebagai sesi web sehingga sesi UI Sesi A tidak terusir (suite.md).
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE di hook `before` pada entitas Distributor Race, dihapus atau dipulihkan hook `after`; setiap nama bersuffix `{runId}-101`; Pre-setup #32 tidak diubah):
  - TC-AC-SG-383: `Race Induk A {runId}-101` (tanpa entitas) dengan anak `Race Induk A Anak {runId}-101` sehingga dialog Delete berupa dialog warning.
  - TC-AC-SG-384: `Race Induk B {runId}-101` dan `Race Lain B {runId}-101` (level 1, tanpa entitas); satu Client `Client Race {runId}-101` (Active, belum di-assign) yang di-assign Sesi B pada langkah 11.
  - TC-AC-SG-394: `Race Induk C {runId}-101` dengan anak `Race Induk C Anak {runId}-101` (tanpa entitas); satu Client `Client Race Anak {runId}-101` (Active, belum di-assign) yang di-assign Sesi B pada langkah 20.
- User untuk penugasan Group Role pada TC-AC-SG-383: `Joko Susilo` dengan Group Role `Manage partner` (user Pre-setup #21 dipakai sebagai penerima penugasan; entitas dan nama role tidak ditentukan TC, disediakan tim FE).
- Baseline audit trail permanen: jumlah total entri Changelog Group dicatat sebelum aksi TC-AC-SG-394 (kemampuan baca disediakan tim FE/BE).
- Kemampuan teknis: Fixture BE dan sesi API aktor untuk memicu perubahan oleh Sesi B (disediakan tim FE/BE tanpa endpoint karangan di spec).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SG-383: Subgroup baru tanpa entitas ditambahkan saat node menunggu konfirmasi Delete: penghapusan tetap berjalan tanpa konfirmasi ulang

1. Pada Sesi A, klik ikon `⋯` pada node `Race Induk A {runId}-101` di sidebar lalu `Delete`
2. Pada Sesi B (API), tambahkan subgroup `Anak Baru {runId}-101` (tanpa entitas) ke `Race Induk A {runId}-101` hingga tersimpan
3. Pada Sesi B (API), tugaskan Group Role `Manage partner` pada `Joko Susilo` ke `Race Induk A {runId}-101` hingga tersimpan
4. Pada Sesi A, klik `[Delete]` pada dialog
5. Verifikasi Sesi A tidak menampilkan dialog konfirmasi ulang
6. Verifikasi toast sukses: "Success, group has been deleted."
7. Verifikasi `Race Induk A {runId}-101`, `Race Induk A Anak {runId}-101`, dan `Anak Baru {runId}-101` tidak ada lagi di Sidebar Group Tree (tidak ada node yatim)

### TC-AC-SG-384: Baris terpilih mendapat member baru saat Submit Bulk Delete

8. Pada Sesi A, ketik Search `{runId}-101`, tekan Enter
9. Pada Sesi A, centang kolom Checkbox pada baris `Race Induk B {runId}-101` dan `Race Lain B {runId}-101`
10. Pada Sesi A, pilih `Bulk Action` > `Delete` pada Bulk Actions Bar sehingga dialog Delete Groups terbuka
11. Pada Sesi B (API), assign Client `Client Race {runId}-101` ke `Race Lain B {runId}-101` hingga tersimpan
12. Pada Sesi A, klik `[Delete]` pada dialog
13. Verifikasi toast: "Success, group has been deleted. Some items were skipped (still has members)."
14. Verifikasi `Race Lain B {runId}-101` tetap ada (dipindah ke status skipped)
15. Verifikasi `Race Induk B {runId}-101` tidak ada lagi (operasi lain tidak digagalkan)

### TC-AC-SG-394: Entitas menempel pada subgroup saat node menunggu konfirmasi Delete: guard dievaluasi ulang dan dialog blok tampil

16. Pada Sesi A, buka halaman Settings > Group lewat sidebar, lalu klik ikon Changelog pada toolbar
17. Pada Sesi A, catat jumlah total entri Modal "Changelog: Group" sebagai baseline BC
18. Pada Sesi A, tutup Modal Changelog dengan `✕`
19. Pada Sesi A, klik ikon `⋯` pada node `Race Induk C {runId}-101` di sidebar lalu `Delete` (dialog warning D-04)
20. Pada Sesi B (API), assign Client `Client Race Anak {runId}-101` ke `Race Induk C Anak {runId}-101` hingga tersimpan
21. Pada Sesi A, klik `[Delete]` pada dialog
22. Verifikasi dialog D-04 ditutup
23. Verifikasi dialog blok D-03 tampil: Title "Cannot Delete Group", body bullet `Race Induk C {runId}-101` dan "This group or its subgroups still have members. Remove all members before deleting." dengan satu tombol `[OK]`
24. Verifikasi tidak ada toast sukses
25. Pada Sesi A, klik `[OK]` pada dialog blok
26. Verifikasi `Race Induk C {runId}-101` dan `Race Induk C Anak {runId}-101` tetap ada
27. Pada Sesi A, klik ikon Changelog pada toolbar
28. Verifikasi jumlah total entri Modal "Changelog: Group" sama dengan BC (tidak ada entri log dari aksi yang diblok)
29. Pada Sesi A, tutup Modal Changelog dengan `✕`

## Notes

- Kelas c (multi-konteks, dua admin). Sesi B hanya memicu perubahan state lewat sesi API dan seluruh hasil diasersi di Sesi A, sehingga konteks kedua UI tidak dipakai dan butir P-2 tidak diperlukan (bagian 3 prinsip 13, P-2 `[KEPUTUSAN 2026-10-30]`).
- Langkah penghubung (S-03, R-16, tanpa `Verifikasi`): langkah 8 (Search `{runId}-101` untuk menemukan baris target), langkah 16 sampai 18 (baseline Changelog dan penutupan modal), dan langkah 29.
- Asersi tidak ada toast sukses (langkah 24) diletakkan segera setelah dialog blok tampil dan sebelum `[OK]` (bagian 8b butir 11); dialog blok tampil (langkah 23) menjadi anchor positif. Asersi tidak ada entri log (langkah 28) memakai baseline agregat BC (S-05, bagian 8b butir 2) dan anchor aksi diblok pada langkah 23; state kontensi dibangun Sesi B pada langkah 20 (P-1: state yang bergantung pada urutan konkurensi tidak dapat diulang di spec absence).
- Hook `after` memulihkan pohon dan Client milik spec lewat Fixture BE. Sisa dialog atau popup tidak ada pada akhir spec.
- Temuan untuk QA:
  - TC-AC-SG-383 langkah 2 menulis "menugaskan satu Group Role ke `Race Induk`" tanpa nama user dan nama role; spec memakai `Joko Susilo` dan `Manage partner` (disediakan tim FE).
  - TC-AC-SG-383 menyebut dialog Delete awal sebagai "dialog warning" untuk `Race Induk` tanpa menyatakan penyebabnya; spec men-seed anak `Race Induk A Anak` agar dialog warning tampil.
  - TC-AC-SG-394 Expected butir b "tidak ada entri log" tanpa langkah observasi baseline; spec mencatat jumlah total entri Changelog sebelum aksi.
  - TC-AC-SG-384 dan TC-AC-SG-394 menyebut "meng-assign satu Client" tanpa nama Client; spec men-seed Client milik spec.
