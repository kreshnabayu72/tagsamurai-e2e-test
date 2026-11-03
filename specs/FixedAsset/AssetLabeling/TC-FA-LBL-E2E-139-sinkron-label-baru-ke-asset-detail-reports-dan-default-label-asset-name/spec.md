---
id: TC-FA-LBL-E2E-139-sinkron-label-baru-ke-asset-detail-reports-dan-default-label-asset-name
title: "Sinkron Label Baru ke Asset Detail, Reports, dan Default Label Asset Name"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-412
  - TC-FA-LBL-413
  - TC-FA-LBL-414
coverage:
  web: automated
---

# Sinkron Label Baru ke Asset Detail, Reports, dan Default Label Asset Name

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Tidak ada ganti akun di tengah spec.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Pre-setup (hanya dibaca, tidak diubah): #13 aset `Laptop Dell - 1` (Asset Detail dan dropdown penugasan label), #14 Asset Name `Laptop Dell` (popup Edit dibuka tanpa disimpan), #12 katalog Company Alpha (Reports menampilkan filter Label).
- Data Dinamis (label dibuat lewat UI oleh spec, nama bersuffix `{runId}-139`): `Sync Label 412 {runId}-139`, `Sync Report 413 {runId}-139`, `Sync Default 414 {runId}-139`.
- Fixture: tidak ada kunci fixture khusus selain identitas akun `Fixture.assetLabeling.akun.totalControl`.
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): sesi API aktor dan fixture BE untuk seeding, pembersihan, dan pembacaan state; endpoint tidak ditulis di TC.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label, aset, dan Asset Name seed milik spec (termasuk yang sudah berganti nama atau dibuat lewat UI) lewat fixture BE berdasarkan ID atau nama bersuffix, tanpa berasumsi seed berhasil penuh.

## Test Steps

### TC-FA-LBL-412: Label baru tersedia di dropdown penugasan label pada Asset Detail

1. Klik `[+ Label]`
2. Isi Label Name dengan `Sync Label 412 {runId}-139`
3. Klik `[Submit]`, lalu tunggu aksi selesai (modal Create Label tertutup)
4. Buka Fixed Asset > Asset List, ketik Search `Laptop Dell - 1`, tekan Enter, lalu buka Asset Detail baris `Laptop Dell - 1`
5. Buka dropdown penugasan label
6. Verifikasi dropdown memuat opsi `Sync Label 412 {runId}-139` tanpa muat ulang manual

### TC-FA-LBL-413: Label baru tersedia di filter Label pada Reports

7. Buka Fixed Asset > Settings > Asset Master > tab Labels
8. Klik `[+ Label]`
9. Isi Label Name dengan `Sync Report 413 {runId}-139`
10. Klik `[Submit]`, lalu tunggu aksi selesai (modal Create Label tertutup)
11. Buka halaman Reports dan buka filter Label
12. Verifikasi filter multi-select Label memuat opsi `Sync Report 413 {runId}-139`

### TC-FA-LBL-414: Label baru tersedia sebagai opsi Default Label pada Asset Name

13. Buka Fixed Asset > Settings > Asset Master > tab Labels
14. Klik `[+ Label]`
15. Isi Label Name dengan `Sync Default 414 {runId}-139`
16. Klik `[Submit]`, lalu tunggu aksi selesai (modal Create Label tertutup)
17. Buka Fixed Asset > Settings > Asset Master > Asset Name, klik `⋯` pada baris Asset Name `Laptop Dell`, lalu klik `Edit`
18. Buka dropdown Default Label
19. Verifikasi dropdown memuat opsi `Sync Default 414 {runId}-139`
20. Verifikasi opsi `Sync Default 414 {runId}-139` belum terpilih
21. Klik icon `[✕]` untuk menutup popup Edit Asset Name tanpa mengubah apa pun

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 7 (Cross-Module Sync & Foundation Cascading). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03): langkah 4, 7, 13, 21 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- Reports: TC tidak menyebut laporan mana yang memuat filter Label; spec membuka halaman Reports dan filter Label sesuai TC.
- Temuan untuk QA:
  - TC-FA-LBL-412 sampai 414 tidak menyebut toast hasil Create; spec menunggu modal Create tertutup lalu langsung memeriksa konsumen.
  - TC-FA-LBL-412 menyebut "tanpa reload manual" tanpa mekanisme pengamatannya; spec membuka Asset Detail sesudah Create tanpa memuat ulang halaman secara eksplisit.
