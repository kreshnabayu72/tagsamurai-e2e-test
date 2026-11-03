---
id: TC-FA-FAAM-E2E-093-delete-single-sukses-aset-deleted-disposed-dan-scope
title: "Delete Single: Konfirmasi Menghapus, Aset Deleted dan Disposed, Klik Ganda, dan Scope Custom Field"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-262
  - TC-FA-FAAM-267
  - TC-FA-FAAM-271
  - TC-FA-FAAM-275
coverage:
  web: automated
---

# Delete Single: Konfirmasi Menghapus, Aset Deleted dan Disposed, Klik Ganda, dan Scope Custom Field

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; seed API per TC mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Dinamis (suffix `{runId}-093`, seed di hook `before`, cleanup di hook `after` untuk yang tersisa):
  - `Warehouse Pallet 262 {runId}-093`: salinan Pre-setup #13 (Non-TAG, Total Asset 0), dihapus TC-FA-FAAM-262; fixture `Fixture.faAssetName.warehousePallet`.
  - `Snapshot Item {runId}-093`: salinan Pre-setup #14j, hanya dirujuk 2 aset Deleted dan 1 aset Disposed (Total Asset 0), dihapus TC-FA-FAAM-267.
  - `Warehouse Pallet 271 {runId}-093`: salinan Pre-setup #13 (Total Asset 0), dihapus TC-FA-FAAM-271.
  - `Scope Only Item 275 {runId}-093`: salinan Pre-setup #27b (Total Asset 0), satu-satunya anggota scope custom field `Scope Only Field 275 {runId}-093` (Text, Global `Finance`, status Active) dan memiliki satu baris policy transaksi di settings-asset-transactional-policy; dihapus TC-FA-FAAM-275.
- Kemampuan teknis (disediakan tim BE/FE): membaca jumlah entri Changelog tanpa mengubahnya (baseline N1 sebelum aksi TC-FA-FAAM-271); membaca nama pada record aset Deleted dan Disposed lewat fixture BE (TC-FA-FAAM-267).
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-262: Konfirmasi Delete menghapus record, baris hilang, toast sukses

1. Ketik Search `Warehouse Pallet 262 {runId}-093`, tekan Enter
2. Klik `⋯` baris `Warehouse Pallet 262 {runId}-093` lalu `Delete`
3. Klik `[Delete]`
4. Verifikasi toast `Success, asset name has been deleted.` tampil
5. Verifikasi baris `Warehouse Pallet 262 {runId}-093` hilang dari List
6. Buka Changelog dan baca entri teratas
7. Verifikasi entri teratas Changelog: Action `Delete`, Field `Asset Name`, Old `Warehouse Pallet 262 {runId}-093`, New `—`
8. Tutup Changelog

### TC-FA-FAAM-267: Aset Deleted dan Disposed tidak menahan Delete

9. Ganti isi kotak search dengan `Snapshot Item {runId}-093`, tekan Enter
10. Klik `⋯` baris `Snapshot Item {runId}-093` lalu `Delete`
11. Verifikasi dialog konfirmasi `Delete Asset Name` (D-01) tampil untuk `Snapshot Item {runId}-093` (Total Asset 0)
12. Klik `[Delete]`
13. Verifikasi toast `Success, asset name has been deleted.` tampil
14. Baca nama pada tiga record aset (dua Deleted, satu Disposed) lewat fixture BE
15. Verifikasi nama pada ketiga record aset tetap `Snapshot Item {runId}-093`

### TC-FA-FAAM-271: Klik ganda Delete hanya menghapus sekali

16. Tunggu toast lama hilang otomatis
17. Ganti isi kotak search dengan `Warehouse Pallet 271 {runId}-093`, tekan Enter
18. Catat jumlah entri Changelog sebagai N1 lewat kemampuan baca
19. Klik `⋯` baris `Warehouse Pallet 271 {runId}-093` lalu `Delete`
20. Klik `[Delete]` dua kali cepat
21. Verifikasi tepat satu toast `Success, asset name has been deleted.` tampil
22. Buka Changelog
23. Verifikasi jumlah entri Changelog sama dengan N1 + 1 dan entri teratas Action `Delete` dengan Old `Warehouse Pallet 271 {runId}-093`
24. Tutup Changelog

### TC-FA-FAAM-275: Delete menyertakan dependen, scope custom field menjadi kosong

25. Ganti isi kotak search dengan `Scope Only Item 275 {runId}-093`, tekan Enter
26. Klik `⋯` baris `Scope Only Item 275 {runId}-093` lalu `Delete`
27. Klik `[Delete]`
28. Tunggu aksi selesai (dialog tertutup)
29. Buka custom field `Scope Only Field 275 {runId}-093` di Custom Fields
30. Verifikasi himpunan scope custom field kosong (kolom Scope tampil `—`)
31. Verifikasi nilai Global Asset Name `Scope Only Item 275 {runId}-093` dibuang dari custom field
32. Verifikasi status Active custom field tidak berubah
33. Buka settings-asset-transactional-policy
34. Verifikasi sedikitnya satu baris policy lain tampil
35. Verifikasi baris policy milik `Scope Only Item 275 {runId}-093` hilang

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (R-16, langkah 1, 9, 17, 25), menunggu toast lama hilang (langkah 16, R-12 untuk hitungan "tepat satu toast"), mencatat baseline N1 (langkah 18, S-12), menutup Changelog (langkah 8, 24), dan "Tunggu aksi selesai" sebelum berpindah surface (langkah 28, bagian 8b butir 8).
- Seluruh data yang dihapus adalah salinan milik spec; Pre-setup #13, #14j, dan #27b tidak diubah (S-06).
- Asersi absence pada langkah 5 memakai toast sukses langkah 4 sebagai anchor (bagian 8b butir 2); absence pada langkah 35 memakai langkah 34 sebagai anchor.
- Temuan untuk QA:
  - TC-FA-FAAM-262 Post Condition (Model per Brand, baris policy transaksi, dan scope custom field ikut dihapus atau dilepas) tidak punya langkah observasi di TC dan tidak diasersi di spec ini; pelepasan scope dan policy diasersi oleh TC-FA-FAAM-275.
  - TC-FA-FAAM-267 Expected b (record aset Deleted dan Disposed menyimpan nama sebagai snapshot) tidak memberi cara observasi di TC; spec memakai kemampuan baca record aset lewat fixture BE yang disediakan tim BE/FE.
  - TC-FA-FAAM-275 Expected a tidak menyebut tempat nilai "Global Asset Name" teramati dan Expected b tidak menyebut jalur menu settings-asset-transactional-policy maupun keberadaan baris policy sebelum Delete; spec membuka halaman custom field dan halaman policy berdasarkan nama modul pada TC dan menjamin baris policy lewat seeding.
  - TC-FA-FAAM-275 tidak menyebut status awal custom field; spec memakai Active dari seeding.
