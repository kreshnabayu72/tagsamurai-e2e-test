---
id: TC-FA-PREF-E2E-141-deferred-depreciation-in-disposal-month-aset-dijual-15-agustus-dan-perubahan-setting
title: "[DEFERRED] Depreciation in Disposal Month pada aset dijual 15 Agustus dan perubahan setting terhadap pelepasan terposting"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-441
  - TC-FA-PREF-442
  - TC-FA-PREF-443
  - TC-FA-PREF-444
coverage:
  web: automated
---

# [DEFERRED] Depreciation in Disposal Month pada aset dijual 15 Agustus dan perubahan setting terhadap pelepasan terposting

## Prerequisites

- Mode: FE+BE.
- Kelas harness: fungsional (alur lintas modul; TC `[DEFERRED]` pada modul pemilik dan konsumen yang belum disusun).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1; Chart of Accounts PC-5; PC-16: aset 'disposal - 21' (dijual 15 Agustus 2026, belum diposting) untuk TC-FA-PREF-441 dan 442, pelepasan 'disposal - 22' yang sudah diposting untuk TC-FA-PREF-443, pelepasan 'disposal - 23' yang menunggu posting (PC-7) untuk TC-FA-PREF-444. Data modul Disposal Posting dan Depreciation Run disediakan tim FE setelah modul tersedia. Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed pelepasan dengan status posting yang ditentukan dan tanggal jual; seed dan pemulihan Preferences; posting pelepasan dan penjalanan penyusutan lewat UI modul Disposal Posting dan Depreciation Run.
- State global yang diubah: Depreciation in Disposal Month company dan status posting pelepasan; dikembalikan ke nilai awal PC-1 oleh langkah pemulihan terakhir dan hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-441: Up to previous month pada aset dijual 15 Agustus

1. Seed Depreciation in Disposal Month tersimpan "Up to previous month" dan aset 'disposal - 21' dijual pada 15 Agustus 2026 dengan pelepasan belum diposting hingga tersimpan
2. Posting pelepasan 'disposal - 21' pada modul Disposal Posting
3. Jalankan penyusutan bulan Agustus 2026 pada Depreciation Run
4. Verifikasi hasil Depreciation Run aset 'disposal - 21' tidak menyusutkan Agustus 2026
5. Verifikasi penyusutan aset 'disposal - 21' berhenti di Juli 2026

### TC-FA-PREF-442: Including disposal month pada aset dijual 15 Agustus

6. Seed Depreciation in Disposal Month tersimpan "Including disposal month" dan aset 'disposal - 21' dijual pada 15 Agustus 2026 dengan pelepasan belum diposting hingga tersimpan
7. Posting pelepasan 'disposal - 21' pada modul Disposal Posting
8. Jalankan penyusutan bulan Agustus 2026 pada Depreciation Run
9. Verifikasi hasil Depreciation Run aset 'disposal - 21' masih menyusutkan Agustus 2026

### TC-FA-PREF-443: Perubahan setting tidak berlaku untuk pelepasan yang sudah diposting

10. Seed Depreciation in Disposal Month tersimpan "Up to previous month" dan pelepasan 'disposal - 22' sudah diposting hingga tersimpan
11. Buka Fixed Asset > Settings > Accounting > Preferences
12. Pilih "Including disposal month" pada Select Depreciation in Disposal Month
13. Klik [Save changes]
14. Tunggu aksi selesai
15. Buka hasil penyusutan pelepasan 'disposal - 22' pada Depreciation Run
16. Verifikasi penyusutan pelepasan 'disposal - 22' tetap memakai Up to previous month

### TC-FA-PREF-444: Perubahan setting berlaku untuk pelepasan yang diposting setelah Save

17. Seed Depreciation in Disposal Month tersimpan "Up to previous month" dan pelepasan 'disposal - 23' menunggu posting hingga tersimpan
18. Buka Fixed Asset > Settings > Accounting > Preferences
19. Pilih "Including disposal month" pada Select Depreciation in Disposal Month
20. Klik [Save changes]
21. Klik [Save] pada dialog Save Changes
22. Tunggu aksi selesai
23. Posting pelepasan 'disposal - 23' pada Disposal Posting
24. Buka hasil penyusutan pelepasan 'disposal - 23' pada Depreciation Run
25. Verifikasi penyusutan pelepasan 'disposal - 23' memakai Including disposal month
26. Pulihkan Depreciation in Disposal Month ke "Up to previous month" dan status posting pelepasan ke nilai awal lewat seed hingga tersimpan

## Notes

- Langkah penghubung (S-03): langkah 11 dan 18 (membuka layar Preferences sesudah seed), langkah 14 dan 22 ("Tunggu aksi selesai", bagian 8b butir 8, karena langkah berikutnya berpindah modul), langkah 26 (pemulihan, S-09, R-08).
- TC-FA-PREF-441 dan 442 memakai aset 'disposal - 21' yang sama; seed ulang pada langkah 6 membentuk precondition TC kedua tanpa bergantung hasil posting TC pertama.
- Temuan untuk QA:
  - TC-FA-PREF-444 tidak menyebut dialog Save Changes pada Save perubahan Depreciation in Disposal Month, padahal precondition memuat pelepasan menunggu posting (PC-7) dan TC-FA-PREF-507 (perubahan yang sama) menyatakan dialog tampil dengan baris dampak pelepasan menunggu posting. Spec menulis klik [Save] pada dialog (langkah 21) tanpa mengasersi isi dialog. TC-FA-PREF-443 tidak memuat pelepasan menunggu posting sehingga spec tidak menulis dialog.
  - TC-FA-PREF-441 sampai 444 tidak menyebut nama menu penjalanan penyusutan, nilai tanggal sistem, atau lokasi hasil penyusutan per aset pada Depreciation Run; spec memakai teks TC apa adanya.
  - Post Condition TC-FA-PREF-441 sampai 444 ("Penyusutan bulan pelepasan mengikuti setting", "Pelepasan yang sudah diposting tidak berubah", "Setting baru berlaku untuk pelepasan yang diposting setelah Save") adalah kesimpulan dari Expected dan tidak diasersi terpisah (S-01).
