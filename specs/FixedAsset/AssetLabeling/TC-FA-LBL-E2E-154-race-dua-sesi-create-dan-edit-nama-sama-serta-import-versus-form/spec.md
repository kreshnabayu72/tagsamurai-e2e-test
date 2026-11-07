---
id: TC-FA-LBL-E2E-154-race-dua-sesi-create-dan-edit-nama-sama-serta-import-versus-form
title: "Race Dua Sesi: Create dan Edit Nama Sama serta Import versus Form"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-465
  - TC-FA-LBL-466
  - TC-FA-LBL-467
  - TC-FA-LBL-477
coverage:
  web: automated
---

# Race Dua Sesi: Create dan Edit Nama Sama serta Import versus Form

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Konteks browser: dua konteks browser (kelas c): sesi 1 = Total Control Company Alpha (Pre-setup #1, `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`, login di hook `before` spec ini) dan sesi 2 = Total Control sesi 2 (Pre-setup #9, `Fixture.assetLabeling.akun.totalControlSecond`, `Spectra.env.FA_TC2_PASSWORD`, login di hook `before` spec ini pada konteks browser kedua). Kedua sesi membuka tab Labels sebelum langkah pertama; halaman dibuka hook `beforeEach` suite untuk sesi 1 dan hook `before` untuk sesi 2. Konteks browser kedua ditutup di hook `after`; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` dan `Spectra.env.FA_TC2_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Dinamis (seed milik spec lewat fixture BE di hook `before`, bersuffix `{runId}-154`, Color `Fixture.assetLabeling.warnaSeed`): label `Race Edit 465 {runId}-154` (TC-FA-LBL-465), `Race Rename 467 {runId}-154` (TC-FA-LBL-467). Label `Race Create 466`, `Race Same 467`, dan `Import Race 477` dibuat oleh aksi spec (nama bersuffix `{runId}-154`).
- Data TC-FA-LBL-477: berkas Import Asset Name berisi Asset Name `Import Item 477 {runId}-154` dengan Default Label `Import Race 477 {runId}-154` yang belum ada di katalog. Berkas dibuat per run oleh pembuat berkas Import (kemampuan Prerequisites di bawah) dan diunggah pada langkah 30. Hasil `[Create Missing Labels]` (langkah 34) adalah relasi Default Label antara Asset Name `Import Item 477 {runId}-154` dan label `Import Race 477 {runId}-154` (bila Import tidak ditolak karena nama sudah ada).
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.akun.totalControlSecond` | `totalControlSecond_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9) |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): dua konteks browser dengan sinkronisasi pemicu "hampir serentak" (kedua klik dijalankan pada tick yang sama; hasil menang-kalah ditentukan server), sesi API aktor dan fixture BE untuk seeding, pembersihan, dan pembacaan state; pembuat berkas Import Asset Name per run (berkas berisi Asset Name `Import Item 477 {runId}-154` dan Default Label `Import Race 477 {runId}-154`; format berkas mengikuti fitur Import Asset Name dan disediakan tim FE/BE, tanpa mengarang format di spec, S-13).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label seed dan label hasil aksi spec (termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID atau nama bersuffix, tanpa berasumsi seed berhasil penuh. Hasil Import TC-FA-LBL-477 dibersihkan lebih dulu: Asset Name `Import Item 477 {runId}-154` dihapus lewat fixture BE (melepas relasi Default Label), baru kemudian label `Import Race 477 {runId}-154` dihapus, karena label yang masih menjadi Default Label suatu Asset Name tidak dapat dihapus; cleanup berjalan juga bila Import tidak sampai selesai.

## Test Steps

### TC-FA-LBL-465: Dua admin menyimpan Edit pada label yang sama (last-write-wins)

1. Sesi 1 dan sesi 2: ketik Search `Race Edit 465 {runId}-154`, tekan Enter, klik `⋯` pada baris itu, lalu klik `Edit` hingga Popup Edit terbuka pada kedua sesi
2. Sesi 1: ganti isi Label Name dengan `Race One 465 {runId}-154`, lalu klik `[Save]`
3. Verifikasi toast `Success, label has been updated.` di sesi 1
4. Sesi 2: ganti isi Label Name dengan `Race Two 465 {runId}-154`, lalu klik `[Save]`
5. Verifikasi toast `Success, label has been updated.` di sesi 2
6. Verifikasi tidak ada dialog konflik di sesi 1 maupun sesi 2
7. Sesi 1: muat ulang tab Labels, lalu ganti isi kotak search dengan `Race Two 465 {runId}-154`, tekan Enter
8. Verifikasi nilai akhir label adalah `Race Two 465 {runId}-154`
9. Sesi 1: buka Modal Changelog, lalu ketik Search `465 {runId}-154`, tekan Enter
10. Verifikasi Changelog memuat entri Edit Field `Label Name` Old Value `Race Edit 465 {runId}-154` New Value `Race One 465 {runId}-154`
11. Verifikasi Changelog memuat entri Edit Field `Label Name` Old Value `Race One 465 {runId}-154` New Value `Race Two 465 {runId}-154`
12. Sesi 1: tutup Modal Changelog

### TC-FA-LBL-466: Dua admin membuat label dengan nama sama hampir serentak

13. Sesi 1 dan sesi 2: klik `[+ Label]` dan isi Label Name dengan `Race Create 466 {runId}-154`
14. Kedua sesi klik `[Submit]` hampir serentak
15. Verifikasi satu sesi menerima toast `Success, label has been created.`
16. Verifikasi sesi lainnya menerima inline error `Label name already exists`
17. Verifikasi modal Create Label pada sesi yang kalah tetap terbuka
18. Verifikasi tidak ada dialog konflik pada kedua sesi
19. Sesi 1: muat ulang tab Labels, lalu ganti isi kotak search dengan `Race Create 466 {runId}-154`, tekan Enter
20. Verifikasi hanya satu label `Race Create 466 {runId}-154` tersimpan
21. Pada sesi yang menerima inline error: klik `✕` pada header modal Create Label, lalu klik `[Leave]` pada dialog Unsaved Changes

### TC-FA-LBL-467: Create dan rename ke nama yang sama hampir serentak

22. Sesi 1: klik `[+ Label]` dan isi Label Name dengan `Race Same 467 {runId}-154`
23. Sesi 2: ganti isi kotak search dengan `Race Rename 467 {runId}-154`, tekan Enter, klik `⋯` pada baris itu, klik `Edit`, lalu ganti isi Label Name dengan `Race Same 467 {runId}-154`
24. Sesi 1 klik `[Submit]` dan sesi 2 klik `[Save]` hampir serentak
25. Verifikasi satu permintaan berhasil dengan toast sukses pada salah satu sesi
26. Verifikasi permintaan yang kalah menerima inline error `Label name already exists`
27. Sesi 1: muat ulang tab Labels, lalu ganti isi kotak search dengan `Race Same 467 {runId}-154`, tekan Enter
28. Verifikasi tidak ada dua label bernama `Race Same 467 {runId}-154` (hanya satu baris)
29. Pada sesi yang menerima inline error: klik `✕` pada header modal, lalu klik `[Leave]` pada dialog Unsaved Changes

### TC-FA-LBL-477: Create lewat Import dan Create lewat form pada nama sama

30. Sesi 2: di Import Asset Name, unggah berkas berisi Default Label `Import Race 477 {runId}-154` hingga pilihan `[Create Missing Labels]` tersedia
31. Sesi 1: klik `[+ Label]`
32. Sesi 1: isi Label Name dengan `Import Race 477 {runId}-154`
33. Sesi 1: klik `[Submit]`, lalu tunggu aksi selesai (modal Create Label tertutup)
34. Sesi 2: klik `[Create Missing Labels]`, lalu tunggu aksi selesai
35. Sesi 1: ganti isi kotak search dengan `Import Race 477 {runId}-154`, tekan Enter
36. Verifikasi hanya satu label `Import Race 477 {runId}-154` ada di katalog
37. Verifikasi Import tidak membuat label duplikat

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 9 (Edge Case Matrix & Concurrency Sisa) dan section 8. Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 7, 9, 19, 23, 27, 35 adalah Search untuk menemukan baris target; bukan bagian Expected TC.
- Langkah penghubung (S-03): langkah 12, 21, 29, 30 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- P-2 tidak dipakai: konteks browser kedua adalah objek asersi pada TC-FA-LBL-465 sampai 467 dan 477 (hasil di sesi 2 diasersi); spec ini kelas c (multi-konteks) murni.
- Pemulihan dialog (S-08): modal pada sesi yang kalah ditutup deterministik lewat `✕` dan `[Leave]`; sesi pemenang menutup modalnya otomatis setelah Create atau Save berhasil.
- Urutan sesi yang menang pada TC-FA-LBL-466 dan 467 ditentukan server (hampir serentak); `Verifikasi` memakai kalimat netral "salah satu sesi" dan "sesi yang kalah".
- Ukuran spec (37 langkah, di atas smell 35 langkah sedikit): keempat TC satu kelas (multi-konteks race nama), satu pasangan sesi, label seed milik masing-masing, dan tiap blok berdiri sendiri; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-FA-LBL-465 sampai 467 dan 477 bertanda Manual Only (d) dua sesi paralel; "hampir serentak" butuh kemampuan sinkronisasi pemicu tim FE (Prerequisites).
  - TC-FA-LBL-466 dan 467 tidak menyebut sesi mana yang menang; asersi dibuat netral terhadap urutan.
  - TC-FA-LBL-477 tidak menyebut mekanisme Import (halaman, berkas) dan apakah kedua aksi serentak; spec mengikuti langkah TC berurutan (sesi 1 Create, lalu sesi 2 Import) dan memakai kemampuan teknis tim FE/BE (S-13).
  - TC-FA-LBL-477 tidak menyebut nama Asset Name dalam berkas Import; spec memakai `Import Item 477 {runId}-154` milik spec. Penghapusan Asset Name hasil Import lewat fixture BE sebagai langkah cleanup menunggu konfirmasi tim FE/BE.
  - TC-FA-LBL-465 menyebut hasil "nilai akhir label adalah `Race Two 465`" tanpa langkah observasi; spec memeriksa lewat muat ulang tab Labels dan Search.
