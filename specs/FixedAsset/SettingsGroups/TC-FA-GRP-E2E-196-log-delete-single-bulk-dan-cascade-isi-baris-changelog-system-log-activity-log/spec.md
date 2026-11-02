---
id: TC-FA-GRP-E2E-196-log-delete-single-bulk-dan-cascade-isi-baris-changelog-system-log-activity-log
title: "Pencatatan Log Delete: Isi Baris untuk Delete Single, Bulk Delete, Delete Cascade, dan Bulk Delete Cascade (Hanya Group yang Berhasil)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-875
  - TC-FA-GRP-876
  - TC-FA-GRP-882
  - TC-FA-GRP-883
coverage:
  web: automated
---

# Pencatatan Log Delete: Isi Baris untuk Delete Single, Bulk Delete, Delete Cascade, dan Bulk Delete Cascade (Hanya Group yang Berhasil)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (Pre-setup tambahan, di-seed lewat API di hook `before`; nama bersuffix `{runId}-196`; semua dihapus oleh aksi spec kecuali yang di-skip): `Del Empty {runId}-196`, `Bulk E1 {runId}-196` dan `Bulk E2 {runId}-196` (kosong), cascade `Cascade D {runId}-196` > `Cascade E {runId}-196` > `Cascade F {runId}-196` (kosong), `Bulk P {runId}-196` > `Bulk C {runId}-196` (kosong). Warehouse A (Pre-setup No 9, beraset) dipilih pada TC-883 dan di-skip (tidak berubah). Sisa fixture dihapus di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Changelog Group, System Log user aktor, dan Activity Log FAMS sebelum aksi (baseline, 8b butir 10); fixture "Pre-setup tambahan" di-seed lewat API di hook `before` dan dihapus di hook `after`.

## Test Steps

### TC-875: Delete single

1. Catat baseline sebelum aksi: jumlah baris Changelog Group, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS yang memuat nama `Del Empty {runId}-196`
2. Buka elipsis `Del Empty {runId}-196`, pilih Delete
3. Klik [Delete]
4. Verifikasi toast sukses "Success, group has been deleted."
5. Buka Modal Changelog: Group
6. Filter Changelog dengan Group Name `Del Empty {runId}-196`
7. Verifikasi baris Changelog: Action `Delete`, Group Name, Field `Group Name`, Old `Del Empty {runId}-196`, New `—`, Modified By aktor berformat `[First Name] [Last Initial]`
8. Verifikasi jumlah baris Changelog untuk `Del Empty {runId}-196` bertambah tepat 1 per node per field yang berubah dibanding baseline (tidak duplikat, tidak ada baris untuk field yang tidak berubah atau node lain)
9. Tutup Modal Changelog
10. Buka Detail User aktor, klik Tab System Log
11. Verifikasi jumlah baris System Log aktor bertambah 1 dibanding baseline
12. Verifikasi baris System Log aktor baru (Note memuat `Del Empty {runId}-196`): object `Groups`
13. Buka Activity Log FAMS
14. Verifikasi jumlah baris Activity Log FAMS yang memuat nama `Del Empty {runId}-196` bertambah 1 dibanding baseline
15. Verifikasi baris Activity Log baru (Note memuat `Del Empty {runId}-196`): kolom Modified By aktor

### TC-876: Bulk Delete

16. Catat baseline sebelum aksi: jumlah baris Changelog Group, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS yang memuat nama `Bulk E1 {runId}-196` dan `Bulk E2 {runId}-196` (baseline Changelog dicatat per nama)
17. Centang `Bulk E1 {runId}-196` dan `Bulk E2 {runId}-196`, pilih Bulk Action Delete
18. Klik [Delete]
19. Verifikasi toast sukses "Success, group has been deleted."
20. Buka Modal Changelog: Group
21. Filter Changelog dengan Group Name `Bulk E1 {runId}-196`
22. Verifikasi baris Changelog: Action `Delete`, Group Name, Field `Group Name`, Old `Bulk E1 {runId}-196`, New `—`, Modified By aktor berformat `[First Name] [Last Initial]`
23. Filter Changelog dengan Group Name `Bulk E2 {runId}-196`
24. Verifikasi baris Changelog sama untuk `Bulk E2 {runId}-196` dengan Date sama dengan baris Bulk E1
25. Verifikasi jumlah baris Changelog bertambah tepat 1 per node per field dibanding baseline (tidak duplikat, tidak ada baris untuk node lain)
26. Tutup Modal Changelog
27. Buka Detail User aktor, klik Tab System Log
28. Verifikasi jumlah baris System Log aktor bertambah dibanding baseline (satu per group atau satu per aksi; TC tidak menentukan)
29. Verifikasi baris System Log aktor baru (Note memuat `Bulk E1 {runId}-196` dan `Bulk E2 {runId}-196`): object `Groups`
30. Buka Activity Log FAMS
31. Verifikasi jumlah baris Activity Log FAMS yang memuat nama `Bulk E1 {runId}-196` dan `Bulk E2 {runId}-196` bertambah dibanding baseline (satu per group atau satu per aksi; TC tidak menentukan)
32. Verifikasi baris Activity Log baru (Note memuat `Bulk E1 {runId}-196` dan `Bulk E2 {runId}-196`): kolom Modified By aktor

### TC-882: Delete cascade

33. Catat baseline sebelum aksi: jumlah baris Changelog Group, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS yang memuat nama `Cascade D {runId}-196`, `Cascade E {runId}-196`, dan `Cascade F {runId}-196` (baseline Changelog dicatat per nama)
34. Buka elipsis `Cascade D {runId}-196`, pilih Delete
35. Klik [Delete]
36. Verifikasi toast sukses "Success, group has been deleted."
37. Buka Modal Changelog: Group
38. Filter Changelog dengan Group Name `Cascade D {runId}-196`
39. Verifikasi baris Changelog: Action `Delete`, Group Name `Cascade D {runId}-196`, Modified By aktor berformat `[First Name] [Last Initial]`
40. Filter Changelog dengan Group Name `Cascade E {runId}-196`
41. Verifikasi baris Changelog: Action `Delete`, Group Name `Cascade E {runId}-196`, Modified By aktor berformat `[First Name] [Last Initial]`
42. Filter Changelog dengan Group Name `Cascade F {runId}-196`
43. Verifikasi baris Changelog: Action `Delete`, Group Name `Cascade F {runId}-196`, Modified By aktor berformat `[First Name] [Last Initial]`
44. Verifikasi jumlah baris Changelog tiap nama (Cascade D, Cascade E, Cascade F) bertambah tepat 1 dibanding baseline masing-masing (tidak ada baris lain untuk node ini)
45. Tutup Modal Changelog

### TC-883: Bulk Delete cascade, hanya group yang berhasil

46. Catat baseline sebelum aksi: jumlah baris Changelog Group, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS yang memuat nama `Bulk P {runId}-196`, `Bulk C {runId}-196`, dan `Warehouse A` (baseline Changelog dicatat per nama)
47. Centang `Bulk P {runId}-196` dan Warehouse A, pilih Bulk Action Delete
48. Klik [Continue]
49. Verifikasi toast "Success, group has been deleted. Some items were skipped."
50. Buka Modal Changelog: Group
51. Filter Changelog dengan Group Name `Bulk P {runId}-196`
52. Verifikasi baris Action `Delete` untuk Bulk P
53. Filter Changelog dengan Group Name `Bulk C {runId}-196`
54. Verifikasi baris Action `Delete` untuk Bulk C
55. Filter Changelog dengan Group Name `Warehouse A`
56. Verifikasi jumlah baris Changelog Warehouse A tidak bertambah dibanding baseline (di-skip)
57. Tutup Modal Changelog

## Notes

- Baseline dicatat per surface sebelum aksi tiap TC. TC-882 dan TC-883 hanya memverifikasi Changelog sesuai Expected TC (System Log dan Activity Log tidak disebut).
- Langkah penghubung (S-03): mencatat baseline, memfilter Changelog, dan menutup Modal Changelog.
- Blok membaca log berpola (buka surface, cari entri, `Verifikasi` kolom log) tidak dihitung terhadap smell 35 langkah (bagian 3 prinsip 13). Langkah baseline dan pencarian baris adalah langkah penghubung (S-03, R-16).
- Baris System Log dan Activity Log dicari lewat kolom Note yang memuat nama group bersuffix (penanda baris sesuai TC) dan asersi jumlah memakai selisih terhadap baseline (S-12). Filter Changelog TC-882 memakai nama bersuffix lengkap tiap node (bukan kata kunci `Cascade`) dengan selisih 1 per nama, sehingga hitungan tidak bergantung pada run sebelumnya. Asersi "tepat 1 baris" memakai baseline (S-12); kolom Modified By diasersi berformat `[First Name] [Last Initial]` (R-14).
- Spec memiliki 57 langkah, di atas smell 35 langkah. Alasan: empat blok satu topik (isi baris log hasil Delete) dengan pola baca-log yang sama; tiap TC berdiri sendiri dan aksi hapus berada di tiap blok.
- Temuan untuk QA:
  - TC-875, 876, 882, dan 883 menyalin hasil dari TC-219 (Delete single), TC-254 (Bulk Delete homogen), TC-222 (cascade), dan TC-256 (Bulk Delete campuran); spec menyalin langkah aksi dari TC tersebut (S-04). TC-883 tidak menyebut dialog sebelum [Continue]; spec mengikuti TC.
  - Asersi "tidak ada baris untuk Warehouse A" (TC-883 Expected b) memakai baseline jumlah baris Changelog Warehouse A, dan toast sukses sebagai anchor penyelesaian aksi (8b butir 2).
  - TC-876 tidak menyebut apakah Bulk Delete menulis satu baris per group atau satu per aksi di System Log dan Activity Log; spec hanya mengasersi jumlah bertambah.
