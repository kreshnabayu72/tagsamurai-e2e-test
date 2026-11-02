---
id: TC-FA-GRP-E2E-201-absence-log-edit-no-op-aksi-batal-dan-kegagalan-tulis-log-rollback
title: "Absence Log: Edit No-Op dan Aksi Batal Tidak Menulis Baris, dan Kegagalan Tulis Activity Log Me-Rollback Mutasi"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-885
  - TC-FA-GRP-891
coverage:
  web: automated
---

# Absence Log: Edit No-Op dan Aksi Batal Tidak Menulis Baris, dan Kegagalan Tulis Activity Log Me-Rollback Mutasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (Pre-setup tambahan, di-seed lewat API di hook `before`, dihapus di hook `after`; nama bersuffix `{runId}-201`): `Edit Target {runId}-201` (Function Assignable, punya aset, Description `Desc awal`), `Del Empty {runId}-201`. Seeding lewat sesi API aktor mencatat baris Create di Changelog node itu; baris itu dipakai sebagai anchor positif (8b butir 2).
- Kemampuan teknis (disediakan tim FE/BE): penulisan Activity Log disimulasikan gagal (pemicu TC-891; mekanisme tidak ada di TC, PRD, atau LLD, S-13) dan dipulihkan di hook `after`; membaca jumlah baris Changelog Group, System Log aktor, dan Activity Log FAMS (baseline).

## Test Steps

### TC-885: Edit No-Op dan aksi batal tidak menulis baris

1. Catat baseline sebelum aksi, per surface dan per nama: jumlah baris Changelog Group yang memuat nama `Edit Target {runId}-201`; jumlah baris Changelog Group yang memuat nama `Del Empty {runId}-201`; jumlah baris System Log aktor; jumlah baris Activity Log FAMS yang memuat nama `Edit Target {runId}-201`; jumlah baris Activity Log FAMS yang memuat nama `Del Empty {runId}-201`
2. Buka elipsis `Edit Target {runId}-201`, pilih Edit, klik [Save] tanpa perubahan
3. Tunggu aksi selesai
4. Buka elipsis `Del Empty {runId}-201`, pilih Delete, klik [Cancel]
5. Buka elipsis `Edit Target {runId}-201`, pilih Edit, ubah Function menjadi None
6. Klik [Save]
7. Klik [Cancel] pada Dialog Change Function
8. Klik ✕ pada popup Edit Group
9. Verifikasi dialog `Unsaved changes` tampil
10. Klik [Leave] pada dialog `Unsaved changes`
11. Buka Modal Changelog: Group
12. Filter Changelog dengan Group Name `Edit Target {runId}-201`
13. Verifikasi baris Create hasil seeding `Edit Target {runId}-201` tampil di Changelog sebagai anchor
14. Verifikasi jumlah baris Changelog `Edit Target {runId}-201` sama dengan baseline
15. Filter Changelog dengan Group Name `Del Empty {runId}-201`
16. Verifikasi baris Create hasil seeding `Del Empty {runId}-201` tampil di Changelog sebagai anchor
17. Verifikasi jumlah baris Changelog `Del Empty {runId}-201` sama dengan baseline
18. Tutup Modal Changelog
19. Buka Detail User aktor, klik Tab System Log
20. Verifikasi jumlah baris System Log aktor sama dengan baseline (mencakup kedua nama)
21. Buka Activity Log FAMS
22. Verifikasi jumlah baris Activity Log yang memuat nama `Edit Target {runId}-201` sama dengan baseline
23. Verifikasi jumlah baris Activity Log yang memuat nama `Del Empty {runId}-201` sama dengan baseline

### TC-891: Kegagalan tulis Activity Log me-rollback mutasi

24. Catat baseline sebelum aksi: jumlah baris Changelog Group, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS yang memuat nama `Edit Target {runId}-201`
25. Aktifkan simulasi kegagalan penulisan Activity Log
26. Buka elipsis `Edit Target {runId}-201`, pilih Edit, ubah Description menjadi `Desc gagal`, klik [Save]
27. Verifikasi toast "Error, failed to update group."
28. Verifikasi Description `Edit Target {runId}-201` tidak berubah (tetap `Desc awal`)
29. Nonaktifkan simulasi kegagalan penulisan Activity Log
30. Klik ✕ pada popup Edit Group
31. Verifikasi dialog `Unsaved changes` tampil
32. Klik [Leave] pada dialog `Unsaved changes`
33. Buka Modal Changelog: Group
34. Filter Changelog dengan Group Name `Edit Target {runId}-201`
35. Verifikasi baris Create hasil seeding `Edit Target {runId}-201` tampil di Changelog sebagai anchor
36. Verifikasi jumlah baris Changelog `Edit Target {runId}-201` sama dengan baseline
37. Tutup Modal Changelog
38. Buka Detail User aktor, klik Tab System Log
39. Verifikasi jumlah baris System Log sama dengan baseline
40. Buka Activity Log FAMS
41. Verifikasi jumlah baris Activity Log sama dengan baseline

## Notes

- Spec 41 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.

- Baseline dicatat per nama dan per surface (Changelog `Edit Target`, Changelog `Del Empty`, System Log aktor, Activity Log tiap nama) dan dibandingkan dengan hitungan surface yang sama. Spec absence (kelas g): TC-885 dan TC-891 diasersi "tidak ada baris" dengan baseline jumlah baris sebelum aksi (S-12) dan anchor positif baris Create hasil seeding pada tiap surface bila tersedia; surface agregat (jumlah sebelum dan sesudah) dipakai karena pemicu tidak menambah baris.
- P-5 butir a: pemicu kegagalan penulisan log (TC-891) hanya membentuk kondisi yang diasersi tidak tercatat; TC-891 memakai baseline sendiri.
- Langkah penghubung (S-03): baseline, Tunggu aksi selesai, menutup popup Edit Group (✕ dan [Leave]) dan Modal Changelog, mengaktifkan dan menonaktifkan simulasi.
- Pemulihan form dirty (S-08): popup `Edit Group` yang dirty ditutup dengan ✕, `Verifikasi` dialog `Unsaved changes`, lalu [Leave] sebelum Modal Changelog dibuka (TC-885 sesudah Dialog Change Function dibatalkan; TC-891 sesudah toast error); hook `after` menghapus fixture dan mematikan simulasi.
- Temuan untuk QA:
  - TC-885 langkah 3 "Dialog Change Function → [Cancel] lalu tutup popup" tidak menyebut cara memicu dialog; spec memakai Function Assignable ke None pada node dengan aset (TC-173). TC-885 menutup popup dengan perubahan dirty tanpa menyebut dialog Unsaved changes; spec menambah ✕, Verifikasi dialog, dan [Leave] (S-08) sebagai langkah penutup form dirty.
  - Anchor positif untuk System Log dan Activity Log: TC tidak menyebut baris pembanding; spec mengandalkan baris Create hasil seeding dan jumlah baseline. Jika seeding lewat API tidak mencatat baris di surface itu, anchor diganti jumlah agregat sebelum dan sesudah.
