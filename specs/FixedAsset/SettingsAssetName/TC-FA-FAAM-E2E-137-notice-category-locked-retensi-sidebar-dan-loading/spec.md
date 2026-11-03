---
id: TC-FA-FAAM-E2E-137-notice-category-locked-retensi-sidebar-dan-loading
title: "Notice Category Locked: Retensi Pindah Tab, F5, Popup Detail, Sidebar, dan Hitungan Selama Loading"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-697
  - TC-FA-FAAM-698
  - TC-FA-FAAM-699
  - TC-FA-FAAM-700
  - TC-FA-FAAM-732
coverage:
  web: automated
---

# Notice Category Locked: Retensi Pindah Tab, F5, Popup Detail, Sidebar, dan Hitungan Selama Loading

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control client `AutoLocked` (Pre-setup #12c); email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password `Spectra.env.FA_TC_LOCKED_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (client `AutoLocked`, Pre-setup #12c; tidak diubah spec ini; `Fixture.faSettingsAssetName.autoLocked`, fixture baru belum ada): 30 `Seed Item 01` sampai `Seed Item 30` (Category `IT Equipment`, Total Asset 0) dan 3 Asset Name Category Locked `Lock Alpha`, `Lock Beta`, `Lock Gamma` (Category internal `Electronics`, Total Asset 0); hitungan Needs Update 3.
- Kemampuan teknis: `Spectra.intercept()` untuk menunda respons List 3 detik (dilepas segera setelah pengamatan), tekan F5, pindah tab Asset Master (`Labels` lalu `Asset Name`).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-697: Quick filter aktif dipertahankan saat pindah tab Asset Master lalu kembali
1. Klik `Show only these`
2. Klik tab `Labels`
3. Klik tab `Asset Name`
4. Verifikasi chip `Needs Update` tampil kembali
5. Verifikasi notice `Showing 3 asset names that need a category update.` tampil kembali
6. Verifikasi tabel hanya memuat tiga Asset Name `Needs Update`
### TC-FA-FAAM-698: Quick filter aktif dipertahankan setelah refresh F5
7. Tekan F5
8. Verifikasi chip `Needs Update` tetap tampil
9. Verifikasi notice `Showing 3 asset names that need a category update.` tetap tampil
10. Verifikasi tabel hanya memuat tiga Asset Name `Needs Update`
### TC-FA-FAAM-699: Menutup Popup Detail tidak melepas quick filter
11. Klik nama `Lock Alpha`
12. Klik icon `[✕]` Popup Detail
13. Verifikasi Popup Detail tertutup
14. Verifikasi chip `Needs Update` tetap tampil
15. Verifikasi notice `Showing 3 asset names that need a category update.` tetap tampil
16. Verifikasi tabel tetap memuat tiga Asset Name `Needs Update`
### TC-FA-FAAM-700: Klik ulang menu sidebar Asset Master mereset quick filter
17. Klik menu sidebar `Settings > Asset Master`
18. Verifikasi notice kembali `3 asset names need a category update.`
19. Verifikasi tabel memuat seluruh Asset Name tanpa quick filter: `Lock Alpha` dan `Seed Item 01` tampil
20. Verifikasi chip `Needs Update` hilang
### TC-FA-FAAM-732: Notice Category Locked tetap tampil dengan hitungan terakhir selama List dimuat ulang karena ganti halaman, Search, atau Filter
21. Verifikasi notice `3 asset names need a category update.` tampil
22. Tunda respons List 3 detik lewat intercept jaringan
23. Pindah ke halaman 2
24. Verifikasi selama respons List tertunda setelah pindah halaman notice tetap `3 asset names need a category update.`
25. Ketik Search `Seed`, tekan Enter
26. Verifikasi selama respons List tertunda setelah Search notice tetap `3 asset names need a category update.`
27. Klik icon Filter, pilih Category `IT Equipment`, lalu klik `[Apply]`
28. Verifikasi selama respons List tertunda setelah Filter notice tetap `3 asset names need a category update.`
29. Lepas intercept jaringan
30. Klik `(←)` pada kotak Search
31. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Urutan di spec: TC-FA-FAAM-697, 698, 699, lalu 700 (mereset quick filter), lalu TC-FA-FAAM-732 yang memulai dari keadaan tanpa quick filter; quick filter dari langkah `Show only these` pada TC-FA-FAAM-697 dipakai bersama TC-FA-FAAM-698 dan 699 (langkah 1 TC tersebut, memasang quick filter, dipenuhi oleh langkah pertama spec).
- Langkah penghubung (aksi tanpa `Verifikasi`): melepas intercept sesudah pengamatan terakhir (S-09) dan membersihkan Search dan Filter Panel di akhir spec.
- Intercept TC-FA-FAAM-732 hanya menahan respons untuk mengamati state UI (bukan kelas b); jendela tunda 3 detik adalah nilai TC.
- Asersi absence chip pada TC-FA-FAAM-700 (langkah 20) beranchor Verifikasi `Lock Alpha` dan `Seed Item 01` tampil pada langkah 19, yang mendahuluinya (bagian 8b butir 2).
- Temuan untuk QA: Pre-setup #12c berupa client tanpa baris akun Total Control (email tidak tertulis).
