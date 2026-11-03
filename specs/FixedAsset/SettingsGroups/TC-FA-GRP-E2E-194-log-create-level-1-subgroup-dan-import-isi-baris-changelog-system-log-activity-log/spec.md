---
id: TC-FA-GRP-E2E-194-log-create-level-1-subgroup-dan-import-isi-baris-changelog-system-log-activity-log
title: "Pencatatan Log Create: Isi Baris Changelog, System Log, dan Activity Log untuk Create Level 1, Create Subgroup, dan Create via Import"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-868
  - TC-FA-GRP-869
  - TC-FA-GRP-870
coverage:
  web: automated
---

# Pencatatan Log Create: Isi Baris Changelog, System Log, dan Activity Log untuk Create Level 1, Create Subgroup, dan Create via Import

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Akun importer: user ber-Global Role Import Data, `Fixture.groupsLog.importer.email`, password `Spectra.env.FA_GRP_IMPORTER_PASSWORD` (env baru; didaftarkan di tempat yang sama dengan `FA_TC_PASSWORD`); akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Ganti akun ke importer dilakukan eksplisit pada TC-870.
- Data Dinamis (nama bersuffix per run): group level 1 `Jakarta Hub {runId}-194` (Code `JKT-194`, Description `Main hub`, Function Assignable); subgroup `Meeting Room {runId}-194` di bawah Floor 2 (Head Office > Floor 2, Pre-setup No 9, dibaca dan tidak diubah); group `Branch C {runId}-194` dibuat via Import. Ketiga group dibuat oleh aksi di spec dan dihapus lewat API di hook `after` (tidak berasumsi seeding berhasil penuh). Kode `JKT-194` dibersihkan di hook `before` bila tersisa (R-13).
- Kemampuan teknis tambahan (disediakan tim FE/BE): berkas dan alur Import Group untuk importer (berkas memuat `Branch C {runId}-194`).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Changelog Group, System Log user aktor, dan Activity Log FAMS sebelum aksi (baseline, 8b butir 10); fixture "Pre-setup tambahan" di-seed lewat API di hook `before` dan dihapus di hook `after`.

## Test Steps

1. Catat baseline sebelum aksi: jumlah baris Changelog Group, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS yang memuat nama `Jakarta Hub {runId}-194` (baseline nol karena nama bersuffix unik)

### TC-868: Create level 1

2. Buka Fixed Asset > Settings > Groups
3. Klik [+] Group
4. Isi Group Name `Jakarta Hub {runId}-194`, Code `JKT-194`, Description `Main hub`, pilih Assignable
5. Klik [Submit]
6. Verifikasi toast sukses "Success, group has been created."
7. Buka Modal Changelog: Group
8. Filter Changelog dengan Group Name `Jakarta Hub {runId}-194`
9. Verifikasi baris Changelog: Action `Create`, Group Name `Jakarta Hub {runId}-194`, Field `Group Name`, Old `—`, New `Jakarta Hub {runId}-194`, Modified By aktor berformat `[First Name] [Last Initial]`
10. Verifikasi jumlah baris Changelog untuk `Jakarta Hub {runId}-194` bertambah tepat 1 per node per field yang berubah dibanding baseline (tidak duplikat, tidak ada baris untuk field yang tidak berubah atau node lain)
11. Tutup Modal Changelog
12. Buka Detail User aktor, klik Tab System Log
13. Verifikasi jumlah baris System Log aktor bertambah 1 dibanding baseline
14. Verifikasi baris System Log aktor baru (Note memuat `Jakarta Hub {runId}-194`): object `Groups`
15. Buka Activity Log FAMS
16. Verifikasi jumlah baris Activity Log FAMS yang memuat nama `Jakarta Hub {runId}-194` bertambah 1 dibanding baseline
17. Verifikasi baris Activity Log baru (Note memuat `Jakarta Hub {runId}-194`): kolom Modified By aktor

### TC-869: Create Subgroup

18. Catat baseline sebelum aksi: jumlah baris Changelog Group yang memuat nama `Meeting Room {runId}-194`, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS yang memuat nama `Meeting Room {runId}-194`
19. Buka Fixed Asset > Settings > Groups
20. Klik Head Office
21. Buka elipsis Floor 2, pilih Add Subgroup
22. Isi Group Name `Meeting Room {runId}-194`, pilih Function Assignable, klik [Submit]
23. Verifikasi toast sukses "Success, group has been created."
24. Buka Modal Changelog: Group
25. Filter Changelog dengan Group Name `Meeting Room {runId}-194`
26. Verifikasi baris Changelog: Action `Create`, Group Name `Head Office > Floor 2 > Meeting Room {runId}-194` (full path), Field `Group Name`, Old `—`, New `Meeting Room {runId}-194`, Modified By aktor berformat `[First Name] [Last Initial]`
27. Verifikasi jumlah baris Changelog untuk `Meeting Room {runId}-194` bertambah tepat 1 per node per field yang berubah dibanding baseline (tidak duplikat, tidak ada baris untuk field yang tidak berubah atau node lain)
28. Tutup Modal Changelog
29. Buka Detail User aktor, klik Tab System Log
30. Verifikasi jumlah baris System Log aktor bertambah 1 dibanding baseline
31. Verifikasi baris System Log aktor baru (Note memuat `Meeting Room {runId}-194`): object `Groups`
32. Buka Activity Log FAMS
33. Verifikasi jumlah baris Activity Log FAMS yang memuat nama `Meeting Room {runId}-194` bertambah 1 dibanding baseline
34. Verifikasi baris Activity Log baru (Note memuat `Meeting Room {runId}-194`): kolom Modified By aktor

### TC-870: Create via Import (akun importer)

35. Ganti akun: Logout, lalu login sebagai importer
36. Buka Fixed Asset > Settings > Groups
37. Catat baseline sebelum aksi: jumlah baris Changelog Group yang memuat nama `Branch C {runId}-194`, jumlah baris System Log importer, dan jumlah baris Activity Log FAMS yang memuat nama `Branch C {runId}-194`
38. Lakukan Import Group `Branch C {runId}-194`
39. Tunggu aksi selesai
40. Buka Fixed Asset > Settings > Groups
41. Buka Modal Changelog: Group
42. Filter Changelog dengan Group Name `Branch C {runId}-194`
43. Verifikasi baris Changelog: Action `Create` (tanpa penanda Import), Group Name `Branch C {runId}-194`, Field `Group Name`, Old `—`, New `Branch C {runId}-194`, Modified By importer berformat `[First Name] [Last Initial]`
44. Verifikasi jumlah baris Changelog untuk `Branch C {runId}-194` bertambah tepat 1 per node per field yang berubah dibanding baseline (tidak duplikat, tidak ada baris untuk field yang tidak berubah atau node lain)
45. Tutup Modal Changelog
46. Buka Detail User importer, klik Tab System Log
47. Verifikasi jumlah baris System Log importer bertambah 1 dibanding baseline
48. Verifikasi baris System Log importer baru (Note memuat `Branch C {runId}-194`): object `Groups`, identik dengan Create manual dan tanpa entri auto-assign creator
49. Buka Activity Log FAMS
50. Verifikasi jumlah baris Activity Log FAMS yang memuat nama `Branch C {runId}-194` bertambah 1 dibanding baseline
51. Verifikasi baris Activity Log baru (Note memuat `Branch C {runId}-194`): kolom Modified By importer

## Notes

- Baseline (S-12) dicatat per surface sebelum aksi tiap TC dan dicatat ulang tiap TC untuk System Log dan Activity Log yang dipakai ulang (langkah 18 dan 37); nama bersuffix unik memberi baseline nol untuk Changelog. Baris log dicari lewat Note atau nama bersuffix, bukan lewat urutan; asersi jumlah memakai selisih terhadap baseline.
- Langkah penghubung (S-03): Buka Fixed Asset > Settings > Groups sebelum aksi tiap blok dan sesudah Import (baseline dan log meninggalkan halaman Groups; S-14), mencatat baseline, Tunggu aksi selesai, menutup Modal Changelog, membuka Head Office dan elipsis Floor 2 pada TC-869, serta Ganti akun ke importer pada TC-870 (akun aktor pertama login di hook `before`; hook `after` memulihkan sesi ke akun default).
- Blok membaca log berpola (buka surface, cari entri, `Verifikasi` kolom log) tidak dihitung terhadap smell 35 langkah (bagian 3 prinsip 13). Langkah baseline dan pencarian baris adalah langkah penghubung (S-03, R-16).
- Asersi "tepat 1 baris" memakai baseline (S-12); kolom Modified By diasersi berformat `[First Name] [Last Initial]` (R-14).
- Spec memiliki 51 langkah, di atas smell 35 langkah. Alasan: tiga blok satu topik (isi baris log hasil Create) dengan pola baca-log yang sama; tiap TC berdiri sendiri.
- Temuan untuk QA:
  - TC-868 sampai 870 menulis "Lakukan aksi: TC Create Jakarta Hub" dan menyalin hasil dari TC-80 dan TC-126 (Jakarta Hub / JKT / Main hub dan Meeting Room di bawah Floor 2); spec menyalin langkah aksi dari TC-80 dan TC-126 (S-04) dengan nama bersuffix.
  - TC-870 "Group Import Branch C dibuat via Import" tidak punya langkah import dan tidak menyebut akun importer; spec menulis keduanya sebagai kemampuan yang disediakan tim FE/BE (S-13). Kolom System Log/Activity Log tidak diuraikan di TC selain "baris sama"; spec memverifikasi sebagaimana ditulis TC.
  - TC-870 tidak menyebut System Log user mana yang dibaca; spec membaca System Log importer (pelaku Create) dengan baseline importer sendiri (langkah 37).
