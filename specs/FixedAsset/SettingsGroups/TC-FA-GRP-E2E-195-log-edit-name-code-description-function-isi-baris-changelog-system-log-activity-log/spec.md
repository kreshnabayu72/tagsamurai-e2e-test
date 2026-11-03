---
id: TC-FA-GRP-E2E-195-log-edit-name-code-description-function-isi-baris-changelog-system-log-activity-log
title: "Pencatatan Log Edit: Isi Baris Changelog, System Log, dan Activity Log untuk Edit Group Name, Code, Description, dan Function"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-871
  - TC-FA-GRP-872
  - TC-FA-GRP-873
  - TC-FA-GRP-874
coverage:
  web: automated
---

# Pencatatan Log Edit: Isi Baris Changelog, System Log, dan Activity Log untuk Edit Group Name, Code, Description, dan Function

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (Pre-setup tambahan, di-seed lewat API di hook `before`, dihapus di hook `after`; nama bersuffix `{runId}-195`): empat group level 1 terpisah, satu per TC: `Edit Target {runId}-195` (TC-871), `Edit Code {runId}-195` dengan Code `ET-195` (TC-872), `Edit Desc {runId}-195` dengan Description `Edit me` (TC-873), `Edit Func {runId}-195` dengan Function None (TC-874). Kode `ET-195` dan `ETR-195` dibersihkan di hook `before` bila tersisa (R-13).
- Perubahan: TC-871 Group Name menjadi `Edit Target Renamed {runId}-195`; TC-872 Code `ET-195` menjadi `ETR-195`; TC-873 Description `Edit me` menjadi `Updated notes`; TC-874 Function None menjadi Assignable.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Changelog Group, System Log user aktor, dan Activity Log FAMS sebelum aksi (baseline, 8b butir 10); fixture "Pre-setup tambahan" di-seed lewat API di hook `before` dan dihapus di hook `after`.

## Test Steps

### TC-871: Edit Group Name

1. Catat baseline sebelum aksi: jumlah baris Changelog Group yang memuat nama `Edit Target Renamed {runId}-195`, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS yang memuat nama `Edit Target {runId}-195` atau `Edit Target Renamed {runId}-195`
2. Buka Fixed Asset > Settings > Groups
3. Ketik Search `Edit Target {runId}-195`, tekan Enter
4. Buka elipsis `Edit Target {runId}-195`, pilih Edit
5. Ubah Group Name menjadi `Edit Target Renamed {runId}-195`, klik [Save]
6. Verifikasi toast sukses "Success, group has been updated."
7. Buka Modal Changelog: Group
8. Filter Changelog dengan Group Name `Edit Target Renamed {runId}-195`
9. Verifikasi baris Changelog: Action `Edit`, Group Name, Field `Group Name`, Old `Edit Target {runId}-195`, New `Edit Target Renamed {runId}-195`, Modified By aktor berformat `[First Name] [Last Initial]`
10. Verifikasi jumlah baris Changelog untuk `Edit Target Renamed {runId}-195` bertambah tepat 1 per node per field yang berubah dibanding baseline (tidak duplikat, tidak ada baris untuk field yang tidak berubah atau node lain)
11. Tutup Modal Changelog
12. Buka Detail User aktor, klik Tab System Log
13. Verifikasi jumlah baris System Log aktor bertambah 1 dibanding baseline
14. Verifikasi baris System Log aktor baru (Note memuat `Edit Target Renamed {runId}-195`): object `Groups`
15. Buka Activity Log FAMS
16. Verifikasi jumlah baris Activity Log FAMS yang memuat nama `Edit Target {runId}-195` atau `Edit Target Renamed {runId}-195` bertambah 1 dibanding baseline
17. Verifikasi baris Activity Log baru (Note memuat `Edit Target Renamed {runId}-195`): kolom Modified By aktor

### TC-872: Edit Code

18. Catat baseline sebelum aksi: jumlah baris Changelog Group yang memuat nama `Edit Code {runId}-195`, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS yang memuat nama `Edit Code {runId}-195`
19. Buka Fixed Asset > Settings > Groups
20. Ketik Search `Edit Code {runId}-195`, tekan Enter
21. Buka elipsis `Edit Code {runId}-195`, pilih Edit
22. Ubah Code menjadi `ETR-195`, klik [Save]
23. Verifikasi toast sukses "Success, group has been updated."
24. Buka Modal Changelog: Group
25. Filter Changelog dengan Group Name `Edit Code {runId}-195`
26. Verifikasi baris Changelog: Action `Edit`, Group Name, Field `Code`, Old `ET-195`, New `ETR-195`, Modified By aktor berformat `[First Name] [Last Initial]`
27. Verifikasi jumlah baris Changelog untuk `Edit Code {runId}-195` bertambah tepat 1 per node per field yang berubah dibanding baseline (tidak duplikat, tidak ada baris untuk field yang tidak berubah atau node lain)
28. Tutup Modal Changelog
29. Buka Detail User aktor, klik Tab System Log
30. Verifikasi jumlah baris System Log aktor bertambah 1 dibanding baseline
31. Verifikasi baris System Log aktor baru (Note memuat `Edit Code {runId}-195`): object `Groups`
32. Buka Activity Log FAMS
33. Verifikasi jumlah baris Activity Log FAMS yang memuat nama `Edit Code {runId}-195` bertambah 1 dibanding baseline
34. Verifikasi baris Activity Log baru (Note memuat `Edit Code {runId}-195`): kolom Modified By aktor

### TC-873: Edit Description

35. Catat baseline sebelum aksi: jumlah baris Changelog Group yang memuat nama `Edit Desc {runId}-195`, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS yang memuat nama `Edit Desc {runId}-195`
36. Buka Fixed Asset > Settings > Groups
37. Ketik Search `Edit Desc {runId}-195`, tekan Enter
38. Buka elipsis `Edit Desc {runId}-195`, pilih Edit
39. Ubah Description menjadi `Updated notes`, klik [Save]
40. Verifikasi toast sukses "Success, group has been updated."
41. Buka Modal Changelog: Group
42. Filter Changelog dengan Group Name `Edit Desc {runId}-195`
43. Verifikasi baris Changelog: Action `Edit`, Group Name, Field `Description`, Old `Edit me`, New `Updated notes`, Modified By aktor berformat `[First Name] [Last Initial]`
44. Verifikasi jumlah baris Changelog untuk `Edit Desc {runId}-195` bertambah tepat 1 per node per field yang berubah dibanding baseline (tidak duplikat, tidak ada baris untuk field yang tidak berubah atau node lain)
45. Tutup Modal Changelog
46. Buka Detail User aktor, klik Tab System Log
47. Verifikasi jumlah baris System Log aktor bertambah 1 dibanding baseline
48. Verifikasi baris System Log aktor baru (Note memuat `Edit Desc {runId}-195`): object `Groups`
49. Buka Activity Log FAMS
50. Verifikasi jumlah baris Activity Log FAMS yang memuat nama `Edit Desc {runId}-195` bertambah 1 dibanding baseline
51. Verifikasi baris Activity Log baru (Note memuat `Edit Desc {runId}-195`): kolom Modified By aktor

### TC-874: Edit Function

52. Catat baseline sebelum aksi: jumlah baris Changelog Group yang memuat nama `Edit Func {runId}-195`, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS yang memuat nama `Edit Func {runId}-195`
53. Buka Fixed Asset > Settings > Groups
54. Ketik Search `Edit Func {runId}-195`, tekan Enter
55. Buka elipsis `Edit Func {runId}-195`, pilih Edit
56. Pilih Function Assignable, klik [Save]
57. Verifikasi toast sukses "Success, group has been updated."
58. Buka Modal Changelog: Group
59. Filter Changelog dengan Group Name `Edit Func {runId}-195`
60. Verifikasi baris Changelog: Action `Edit`, Group Name, Field `Function`, Old `None`, New `Assignable`, Modified By aktor berformat `[First Name] [Last Initial]`
61. Verifikasi jumlah baris Changelog untuk `Edit Func {runId}-195` bertambah tepat 1 per node per field yang berubah dibanding baseline (tidak duplikat, tidak ada baris untuk field yang tidak berubah atau node lain)
62. Tutup Modal Changelog
63. Buka Detail User aktor, klik Tab System Log
64. Verifikasi jumlah baris System Log aktor bertambah 1 dibanding baseline
65. Verifikasi baris System Log aktor baru (Note memuat `Edit Func {runId}-195`): object `Groups`
66. Buka Activity Log FAMS
67. Verifikasi jumlah baris Activity Log FAMS yang memuat nama `Edit Func {runId}-195` bertambah 1 dibanding baseline
68. Verifikasi baris Activity Log baru (Note memuat `Edit Func {runId}-195`): kolom Modified By aktor

## Notes

- Baseline dicatat per surface sebelum aksi tiap TC (Changelog dicatat atas nama yang sama dengan filter asersi, yaitu nama baru pada TC-871; System Log dan Activity Log TC-871 mencakup nama lama dan nama baru); satu group per TC agar baseline dan baris tiap TC tidak bercampur (S-06, S-12).
- Langkah penghubung (S-03): mencatat baseline, Buka Fixed Asset > Settings > Groups sebelum aksi tiap blok (baseline dan log meninggalkan halaman Groups; S-14), serta menutup Modal Changelog. Client punya lebih dari 10 node level 1 dan ukuran halaman 10, sehingga group target tidak dijamin ada di halaman 1 All Groups: tiap `Buka elipsis` didahului `Ketik Search` nama bersufiks + Enter. Search tidak dikosongkan karena langkah berikutnya tidak memerlukan tabel penuh dan blok berikutnya diawali `Buka Fixed Asset > Settings > Groups` (S-03, R-16).
- Blok membaca log berpola (buka surface, cari entri, `Verifikasi` kolom log) tidak dihitung terhadap smell 35 langkah (bagian 3 prinsip 13). Langkah baseline dan pencarian baris adalah langkah penghubung (S-03, R-16).
- Baris System Log dan Activity Log dicari lewat Note atau nama bersuffix dan asersi jumlah memakai selisih 1 terhadap baseline (S-12); asersi "tepat 1 baris" memakai baseline (S-12); kolom Modified By diasersi berformat `[First Name] [Last Initial]` (R-14).
- Spec memiliki 68 langkah, di atas smell 35 langkah. Alasan: empat blok satu topik (isi baris log hasil Edit) dengan pola baca-log yang sama; tiap TC berdiri sendiri.
- Temuan untuk QA:
  - TC-871 sampai 874 menulis "Lakukan aksi" tanpa langkah; spec menyalin langkah Edit dari TC-161 (Name), TC-162 (Code), TC-163 (Description), dan TC-183 (Function None ke Assignable, tanpa dialog). Nama dan Code TC literal (`Edit Target`, `ET`) diberi suffix atau kode `-195` (S-12).
  - Kolom System Log/Activity Log tidak diuraikan di TC selain "baris sama"; spec memverifikasi sebagaimana ditulis TC.
