---
id: TC-FA-LBL-E2E-155-race-dua-sesi-penempelan-label-versus-delete-dan-bulk-delete
title: "Race Dua Sesi: Penempelan Label versus Delete dan Bulk Delete"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-464
  - TC-FA-LBL-472
  - TC-FA-LBL-473
  - TC-FA-LBL-474
coverage:
  web: automated
---

# Race Dua Sesi: Penempelan Label versus Delete dan Bulk Delete

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Konteks browser: dua konteks browser (kelas c): sesi 1 = Total Control Company Alpha (Pre-setup #1, `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`, login di hook `before` spec ini) dan sesi 2 = Total Control sesi 2 (Pre-setup #9, juga memegang role Update pada Manage Asset & TAG, `Fixture.assetLabeling.akun.totalControlSecond`, `Spectra.env.FA_TC2_PASSWORD`, login di hook `before` spec ini pada konteks browser kedua). Kedua sesi membuka tab Labels sebelum langkah pertama; halaman dibuka hook `beforeEach` suite untuk sesi 1 dan hook `before` untuk sesi 2. Konteks browser kedua ditutup di hook `after`; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` dan `Spectra.env.FA_TC2_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Dinamis (seed milik spec lewat fixture BE di hook `before`, bersuffix `{runId}-155`, Color `Fixture.assetLabeling.warnaSeed`; aset milik spec mengikuti pola `Laptop Dell - 3` Pre-setup #13 agar aset Pre-setup tidak berubah, S-06): aset Active `Race Asset {runId}-155` tanpa label; label bersih `Race Attach 464 {runId}-155`, `Race DA 472 {runId}-155`, `Race AD 473 {runId}-155`, `Race B1 474 {runId}-155`, `Race B2 474 {runId}-155` (Total Asset 0, bukan Default Label).
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.akun.totalControlSecond` | `totalControlSecond_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9) |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): dua konteks browser dengan sinkronisasi pemicu "hampir serentak" (kedua klik dijalankan pada tick yang sama; hasil menang-kalah ditentukan server), sesi API aktor dan fixture BE untuk seeding, pembersihan, dan pembacaan state, termasuk membaca jumlah entri Changelog Labels, System Log aktor, dan Activity Log (S-12).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label dan aset seed milik spec lewat fixture BE berdasarkan ID (relasi dilepas lebih dulu), tanpa berasumsi seed berhasil penuh.

## Test Steps

### TC-FA-LBL-464: Dua pengguna melampirkan label yang sama ke aset yang sama secara bersamaan

1. Sesi 1 dan sesi 2: buka Fixed Asset > Asset List, ketik Search `Race Asset {runId}-155`, tekan Enter, lalu buka Asset Detail baris itu
2. Kedua sesi: pilih `Race Attach 464 {runId}-155` pada dropdown penugasan label dan terapkan pada saat bersamaan
3. Verifikasi sesi 1 menerima respons sukses (toast `Success, Label has been added.`)
4. Verifikasi sesi 2 menerima respons sukses (toast `Success, Label has been added.`)
5. Sesi 1: muat ulang Asset Detail `Race Asset {runId}-155`
6. Verifikasi hanya satu chip `Race Attach 464 {runId}-155` pada aset (satu relasi)
7. Buka Fixed Asset > Settings > Asset Master > tab Labels pada sesi 1, lalu ketik Search `Race Attach 464 {runId}-155`, tekan Enter
8. Verifikasi Total Asset `Race Attach 464 {runId}-155` bernilai `1`

### TC-FA-LBL-472: Delete label bersih yang commit lebih dulu dari penempelan, penempelan menyusul gagal tanpa orphan

9. Sesi 1: ganti isi kotak search dengan `Race DA 472 {runId}-155`, tekan Enter, klik `⋯` pada baris itu, lalu klik `Delete` hingga dialog `Delete Label` terbuka
10. Sesi 2: buka Asset Detail `Race Asset {runId}-155`, buka dropdown penugasan label, dan pilih `Race DA 472 {runId}-155` tanpa menerapkan
11. Sesi 1: klik `[Delete]` hingga penghapusan tersimpan
12. Verifikasi toast `Success, label has been deleted.` di sesi 1
13. Verifikasi label `Race DA 472 {runId}-155` terhapus
14. Sesi 2: terapkan penugasan
15. Sesi 2: muat ulang Asset Detail `Race Asset {runId}-155`
16. Verifikasi `Race Asset {runId}-155` tidak memiliki label `Race DA 472 {runId}-155`
17. Verifikasi tidak ada relasi yatim `Race DA 472 {runId}-155` pada aset (dibaca lewat fixture BE)

### TC-FA-LBL-473: Penempelan yang commit lebih dulu dari Delete, Delete ditolak dengan hitungan terbaru

18. Catat baseline jumlah entri Delete untuk `Race AD 473 {runId}-155` di Changelog Labels, System Log, dan Activity Log lewat fixture BE
19. Sesi 1: ketik Search `Race AD 473 {runId}-155`, tekan Enter, klik `⋯` pada baris itu, lalu klik `Delete` hingga dialog `Delete Label` terbuka
20. Sesi 2: buka Asset Detail `Race Asset {runId}-155` dan lampirkan `Race AD 473 {runId}-155` hingga penempelan tersimpan
21. Sesi 1: klik `[Delete]`
22. Verifikasi dialog sesi 1 berganti `Cannot Delete Label` dengan baris `This label is assigned to 1 asset.`
23. Sesi 1: tutup dialog `Cannot Delete Label`
24. Verifikasi label `Race AD 473 {runId}-155` tidak terhapus (baris tetap tampil)
25. Verifikasi jumlah entri Delete untuk `Race AD 473 {runId}-155` di Changelog Labels, System Log, dan Activity Log sama dengan baseline langkah 18 (fixture BE)

### TC-FA-LBL-474: Bulk Delete, label menjadi dipakai oleh sesi lain tepat sebelum item itu diproses

26. Sesi 1: ketik Search `474 {runId}-155`, tekan Enter, centang baris `Race B1 474 {runId}-155` dan `Race B2 474 {runId}-155`, klik `Bulk Action`, lalu klik `Delete` hingga dialog `Delete Labels` terbuka
27. Sesi 2: buka Asset Detail `Race Asset {runId}-155` dan lampirkan `Race B2 474 {runId}-155` hingga penempelan tersimpan
28. Sesi 1: klik `[Delete]`
29. Verifikasi toast `Success, label has been deleted. Some items were skipped.`
30. Verifikasi label `Race B1 474 {runId}-155` terhapus (baris hilang dari tabel)
31. Verifikasi label `Race B2 474 {runId}-155` dilewati (baris tetap tampil)

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 9 (Edge Case Matrix & Concurrency Sisa) dan section 8. Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 7, 9, 19, 26 adalah Search untuk menemukan baris target; bukan bagian Expected TC.
- Langkah penghubung (S-03): langkah 5, 15, 18, 23 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- P-2: pada TC-FA-LBL-473 dan 474 sesi 2 hanya memicu penempelan label (pemicu state, bukan objek asersi) dan memakai konteks browser kedua yang sama dengan TC-FA-LBL-464 dan 472 yang mengasersi sesi 2; spec tetap kelas c.
- Asersi "tidak ada entri log" TC-FA-LBL-473 (langkah 25) adalah selisih jumlah entri Delete bernama bersuffix unik terhadap baseline langkah 18, dibaca lewat fixture BE (S-12), bukan kelas g; TC-FA-LBL-473 tidak ada di spec absence.
- Temuan untuk QA:
  - TC-FA-LBL-464, 472, 473, dan 474 bertanda Manual Only (d) dua sesi paralel; "pada saat bersamaan" pada TC-FA-LBL-464 butuh kemampuan sinkronisasi pemicu tim FE (Prerequisites).
  - TC-FA-LBL-472 menyebut "tidak ada relasi yatim" tanpa langkah observasi; spec membacanya lewat fixture BE (S-13).
  - TC-FA-LBL-473 Expected "tidak ada entri log" tidak menyebut surface; spec memakai Changelog Labels, System Log, dan Activity Log.
  - Precondition TC memakai aset Pre-setup `Laptop Dell - 3` dan menyebut sesi 2 memegang role Update pada Manage Asset & TAG; spec memakai aset milik spec dengan pola yang sama (S-06).
