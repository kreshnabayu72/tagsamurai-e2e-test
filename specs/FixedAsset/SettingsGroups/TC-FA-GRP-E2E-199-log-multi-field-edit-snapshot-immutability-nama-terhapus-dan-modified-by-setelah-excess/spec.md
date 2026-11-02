---
id: TC-FA-GRP-E2E-199-log-multi-field-edit-snapshot-immutability-nama-terhapus-dan-modified-by-setelah-excess
title: "Pencatatan Log: Edit Multi-Field Tidak Hilang/Duplikat, Snapshot Immutability Setelah Rename Dua Kali, Nama Group Terhapus Tetap Terbaca, dan Modified By/Last Updated Berubah Setelah Excess"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-884
  - TC-FA-GRP-886
  - TC-FA-GRP-887
  - TC-FA-GRP-892
coverage:
  web: automated
---

# Pencatatan Log: Edit Multi-Field Tidak Hilang/Duplikat, Snapshot Immutability Setelah Rename Dua Kali, Nama Group Terhapus Tetap Terbaca, dan Modified By/Last Updated Berubah Setelah Excess

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (Pre-setup tambahan, di-seed lewat API di hook `before`, dihapus di hook `after`; nama bersuffix `{runId}-199`): `Edit Multi {runId}-199` (Function Assignable, punya aset), `Snap {runId}-199`, `Del Empty {runId}-199`. Untuk TC-892: group `Warehouse C {runId}-199` yang sudah ditandai Excess oleh fallback T-0 (state dibentuk tim FE/BE lewat hook uji T-0 di hook `before`; kemampuan T-0 disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Changelog Group, System Log user aktor, dan Activity Log FAMS sebelum aksi (baseline, 8b butir 10); fixture "Pre-setup tambahan" di-seed lewat API di hook `before` dan dihapus di hook `after`.
- Penanda waktu aksi dicatat sesudah aksi; kolom Date log dibandingkan dengan waktu itu dengan toleransi satu menit; jam server dan jam browser sinkron.

## Test Steps

### TC-884: Log multi-field Edit

1. Catat baseline sebelum aksi: jumlah baris Changelog Group, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS yang memuat nama `Edit Multi {runId}-199`
2. Buka elipsis `Edit Multi {runId}-199`, pilih Edit
3. Ubah Group Name menjadi `Edit Multi Renamed {runId}-199`, Code menjadi `EMR-199`, Description menjadi `Multi notes`, dan Function menjadi None
4. Klik [Save]
5. Klik [Save] pada Dialog Change Function
6. Verifikasi toast sukses "Success, group has been updated."
7. Buka Modal Changelog: Group
8. Filter Changelog dengan Group Name `Edit Multi Renamed {runId}-199`
9. Verifikasi tepat 4 baris Edit (Group Name, Code, Description, Function) dengan Date sama dibanding baseline
10. Verifikasi tidak ada baris dobel
11. Tutup Modal Changelog

### TC-886: Snapshot immutability

12. Catat baseline sebelum aksi: jumlah baris Changelog Group yang memuat nama `Snap One {runId}-199` dan jumlah baris yang memuat nama `Snap Two {runId}-199` (dicatat per nama)
13. Rename `Snap {runId}-199` menjadi `Snap One {runId}-199`
14. Verifikasi toast sukses "Success, group has been updated."
15. Rename `Snap One {runId}-199` menjadi `Snap Two {runId}-199`
16. Verifikasi toast sukses "Success, group has been updated."
17. Buka Modal Changelog: Group
18. Filter Changelog dengan Group Name `Snap One {runId}-199`
19. Verifikasi baris pertama: Old `Snap {runId}-199`, New `Snap One {runId}-199` (Group Name kolom bernilai nama saat itu)
20. Verifikasi baris lama tidak berubah mengikuti nama terbaru
21. Filter Changelog dengan Group Name `Snap Two {runId}-199`
22. Verifikasi baris kedua: Old `Snap One {runId}-199`, New `Snap Two {runId}-199`
23. Verifikasi jumlah baris Changelog `Snap One {runId}-199` dan `Snap Two {runId}-199` masing-masing bertambah tepat 1 dibanding baseline
24. Tutup Modal Changelog

### TC-887: Nama group terhapus tetap terbaca

25. Buka elipsis `Del Empty {runId}-199`, pilih Delete
26. Klik [Delete]
27. Verifikasi toast sukses "Success, group has been deleted."
28. Buka Modal Changelog: Group
29. Filter Changelog dengan Group Name `Del Empty {runId}-199`
30. Verifikasi baris historis `Del Empty {runId}-199` tetap ada
31. Buka dropdown filter Group Name
32. Verifikasi opsi filter Group Name memuat `Del Empty {runId}-199`
33. Tutup Modal Changelog

### TC-892: Modified By dan Last Updated setelah Excess

34. Amati baris `Warehouse C {runId}-199` pada Groups List
35. Verifikasi Modified By baris `Warehouse C {runId}-199` bernilai `System`
36. Verifikasi Last Updated baris `Warehouse C {runId}-199` sama dengan waktu T-0 (format General Settings)

## Notes

- Spec 36 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.

- Baseline (S-12) dicatat sebelum aksi TC-884; TC-886 mencatat baseline per nama sebelum rename pertama dan memfilter dengan nama bersuffix lengkap (bukan kata kunci `Snap`), sehingga hitungan tidak bergantung pada run sebelumnya dan TC-887 memakai baris historis sebagai anchor positif. Langkah penghubung (S-03): baseline, filter Changelog, dan menutup Modal Changelog.
- Urutan: TC-884, 886, 887 (aksi mengubah/menghapus data) lalu TC-892 (hanya membaca); aksi hapus TC-887 ditaruh sebelum TC-892 karena TC-892 tidak bergantung pada node yang dihapus.
- Temuan untuk QA:
  - TC-884 memakai "Edit Edit Target: Name, Code, Description, Function sekaligus" tanpa nilai baru; spec menetapkan nilai baru di langkah. TC-886 dan 887 memakai nama literal (`Snap`, `Del Empty`) yang diberi suffix (S-12). TC-892 mensyaratkan Warehouse C Excess lewat fallback T-0; nilai waktu T-0 dibaca dari state yang dibentuk tim FE/BE.
  - TC-884 Expected b ("tidak ada baris dobel") ditulis sebagai asersi jumlah dengan baseline (S-12).
  - TC-886 tidak menyebut cara menyaring baris Changelog yang berganti nama; spec memfilter per nama (`Snap One`, `Snap Two`) dengan asumsi filter Group Name mencocokkan nama pada baris, dan menafsirkan "baris pertama" dan "baris kedua" sebagai baris hasil rename pertama dan kedua.
  - TC-886: filter Group Name diasumsikan mencocokkan nama group pada baris yang berganti nama. Dikonfirmasi pemilik TC.
