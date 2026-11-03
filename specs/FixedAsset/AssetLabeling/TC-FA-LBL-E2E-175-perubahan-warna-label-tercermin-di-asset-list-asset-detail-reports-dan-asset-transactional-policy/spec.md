---
id: TC-FA-LBL-E2E-175-perubahan-warna-label-tercermin-di-asset-list-asset-detail-reports-dan-asset-transactional-policy
title: "Perubahan Warna Label Tercermin di Asset List, Asset Detail, Reports, dan Asset Transactional Policy"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-419
  - TC-FA-LBL-496
  - TC-FA-LBL-497
coverage:
  web: automated
---

# Perubahan Warna Label Tercermin di Asset List, Asset Detail, Reports, dan Asset Transactional Policy

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Tidak ada ganti akun di tengah spec.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Dinamis (seed milik spec lewat fixture BE di hook `before`, bersuffix `{runId}-175`; pola Pre-setup #13 dan #14 dimiliki spec agar `Last Updated` aset Pre-setup tidak berubah, S-06): Asset Name `Hue Item {runId}-175`, aset Active `Hue Asset {runId}-175` yang tertempel ketiga label, dan label `Hue 419 {runId}-175` (TC-FA-LBL-419), `Hue 496 {runId}-175` (TC-FA-LBL-496), `Hue 497 {runId}-175` (TC-FA-LBL-497), seluruhnya Color `Fixture.assetLabeling.warnaSeed` dan menjadi Default Label Asset Name itu.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color awal label seed) |
  | `Fixture.assetLabeling.hexHijau` | `#10B981` (Color baru) |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): sesi API aktor dan fixture BE untuk seeding, pembersihan, dan pembacaan state; endpoint tidak ditulis di TC.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label, aset, dan Asset Name seed milik spec (termasuk yang sudah berganti nama atau dibuat lewat UI) lewat fixture BE berdasarkan ID atau nama bersuffix, tanpa berasumsi seed berhasil penuh.

## Test Steps

### Ubah warna ketiga label di tab Labels (dipakai TC-FA-LBL-419, TC-FA-LBL-496, TC-FA-LBL-497)

1. Ketik Search `Hue 419 {runId}-175`, tekan Enter
2. Klik `⋯` pada baris `Hue 419 {runId}-175`, lalu klik `Edit`
3. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
4. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexHijau`
5. Klik `[Save]`, lalu tunggu aksi selesai (modal Edit Label tertutup)
6. Ganti isi kotak search dengan `Hue 496 {runId}-175`, tekan Enter
7. Klik `⋯` pada baris `Hue 496 {runId}-175`, lalu klik `Edit`
8. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
9. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexHijau`
10. Klik `[Save]`, lalu tunggu aksi selesai (modal Edit Label tertutup)
11. Ganti isi kotak search dengan `Hue 497 {runId}-175`, tekan Enter
12. Klik `⋯` pada baris `Hue 497 {runId}-175`, lalu klik `Edit`
13. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
14. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexHijau`
15. Klik `[Save]`, lalu tunggu aksi selesai (modal Edit Label tertutup)

### TC-FA-LBL-419: Perubahan warna label berlaku seragam pada chip Asset List dan Asset Detail

16. Buka Fixed Asset > Asset List, lalu ketik Search `Hue Asset {runId}-175`, tekan Enter
17. Verifikasi chip `Hue 419 {runId}-175` di Asset List berlatar `Fixture.assetLabeling.hexHijau`
18. Verifikasi teks chip `Hue 419 {runId}-175` di Asset List berwarna kontras otomatis
19. Buka Asset Detail baris `Hue Asset {runId}-175`
20. Verifikasi chip `Hue 419 {runId}-175` di Asset Detail berlatar `Fixture.assetLabeling.hexHijau`
21. Verifikasi teks chip `Hue 419 {runId}-175` di Asset Detail berwarna kontras otomatis

### TC-FA-LBL-496: Perubahan warna label tercermin langsung di Reports

22. Buka Reports tanpa menyunting data aset
23. Verifikasi chip `Hue 496 {runId}-175` di Reports berlatar `Fixture.assetLabeling.hexHijau`
24. Verifikasi teks chip `Hue 496 {runId}-175` di Reports berwarna kontras otomatis

### TC-FA-LBL-497: Perubahan warna label tercermin langsung di Asset Transactional Policy

25. Buka Fixed Asset > Settings > Asset Transactional Policy tanpa menyunting data aset
26. Verifikasi chip `Hue 497 {runId}-175` di Asset Transactional Policy berlatar `Fixture.assetLabeling.hexHijau`
27. Verifikasi teks chip `Hue 497 {runId}-175` di Asset Transactional Policy berwarna kontras otomatis

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 7 (Cross-Module Sync & Foundation Cascading). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 6, 11, 16 adalah Search untuk menemukan baris target; bukan bagian Expected TC.
- Langkah penghubung (S-03): langkah 19, 22, 25 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- Urutan (bagian 3): ketiga perubahan warna dikerjakan berurutan di tab Labels lebih dulu, lalu tiap konsumen dibuka sekali; tiap TC mengasersi konsumennya sendiri.
- Temuan untuk QA:
  - TC-FA-LBL-496 dan 497 menyebut chip di Reports dan Asset Transactional Policy tanpa menyebut kolom atau laporan; spec memeriksa chip pada halaman yang dibuka.
  - Precondition TC memakai aset `Laptop Dell - 1` Pre-setup #13; spec memakai aset milik spec dengan pola yang sama (S-06).
