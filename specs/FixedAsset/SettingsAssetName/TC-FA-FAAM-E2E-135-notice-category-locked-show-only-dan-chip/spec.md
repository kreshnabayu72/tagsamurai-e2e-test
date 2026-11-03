---
id: TC-FA-FAAM-E2E-135-notice-category-locked-show-only-dan-chip
title: "Notice Category Locked: Bentuk Jamak, Hitungan Seluruh Katalog, Show only these, Clear Filter, dan Chip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-687
  - TC-FA-FAAM-690
  - TC-FA-FAAM-691
  - TC-FA-FAAM-693
  - TC-FA-FAAM-694
coverage:
  web: automated
---

# Notice Category Locked: Bentuk Jamak, Hitungan Seluruh Katalog, Show only these, Clear Filter, dan Chip

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control client `AutoLocked` (Pre-setup #12c); email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password `Spectra.env.FA_TC_LOCKED_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (client `AutoLocked`, Pre-setup #12c; tidak diubah spec ini; `Fixture.faSettingsAssetName.autoLocked`, fixture baru belum ada): 30 `Seed Item 01` sampai `Seed Item 30` (Category `IT Equipment`, Total Asset 0) dan 3 Asset Name Category Locked `Lock Alpha`, `Lock Beta`, `Lock Gamma` (Category internal `Electronics`, Total Asset 0); hitungan Needs Update 3.
- Kemampuan teknis: pindah halaman dan klik tautan aksi pada Alert.
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-687: Notice Category Locked bentuk jamak tampil di atas tabel tanpa tombol tutup
1. Perhatikan area di bawah Table Tools dan di atas tabel
2. Verifikasi satu Alert Warning tampil di bawah Table Tools dan di atas tabel dengan teks `3 asset names need a category update.`
3. Verifikasi aksi tautan `Show only these` ada di dalam Alert
4. Verifikasi Alert tidak memiliki tombol tutup
5. Verifikasi tidak ada chip quick filter
### TC-FA-FAAM-690: Hitungan notice mengikuti seluruh katalog client dan tidak berubah oleh Search, Filter Panel, atau halaman
6. Ketik Search `Seed`, tekan Enter
7. Verifikasi baris `Seed Item 01` tampil di tabel
8. Verifikasi tabel tidak memuat Asset Name Category Locked (`Lock Alpha`, `Lock Beta`, `Lock Gamma`)
9. Verifikasi notice tetap `3 asset names need a category update.`
10. Klik icon Filter, pilih Category `IT Equipment`, lalu klik `[Apply]`
11. Verifikasi notice tetap `3 asset names need a category update.`
12. Pindah ke halaman 2
13. Verifikasi notice tetap `3 asset names need a category update.`
14. Klik `(←)` pada kotak Search
15. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
### TC-FA-FAAM-691: Show only these memasang quick filter Category Locked dan kembali ke halaman 1
16. Pindah ke halaman 2
17. Klik `Show only these` pada notice
18. Verifikasi tabel hanya memuat `Lock Alpha`, `Lock Beta`, `Lock Gamma` yang berbadge `Needs Update`
19. Verifikasi paginasi kembali ke halaman 1
20. Verifikasi chip `Needs Update` dengan `✕` tampil
21. Verifikasi notice berubah menjadi `Showing 3 asset names that need a category update.`
22. Verifikasi notice memuat aksi `Clear filter`
23. Klik `Clear filter`
### TC-FA-FAAM-693: Clear filter melepas hanya quick filter dan mempertahankan Search serta Filter Panel
24. Ketik Search `Lock`, tekan Enter
25. Klik icon Filter, pilih Category `Electronics`, lalu klik `[Apply]`
26. Klik `Show only these`
27. Klik `Clear filter`
28. Verifikasi notice kembali `3 asset names need a category update.`
29. Verifikasi chip `Needs Update` hilang
30. Verifikasi notice memuat aksi `Show only these`
31. Verifikasi Search box tetap berisi `Lock`
32. Verifikasi Filter Category `Electronics` tetap ter-Apply
33. Verifikasi paginasi di halaman 1
### TC-FA-FAAM-694: Tombol ✕ pada chip melepas hanya quick filter
34. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
35. Klik `Show only these`
36. Klik `✕` pada chip `Needs Update`
37. Verifikasi notice kembali `3 asset names need a category update.`
38. Verifikasi chip hilang
39. Verifikasi Search box tetap berisi `Lock`
40. Verifikasi paginasi di halaman 1
41. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): pemulihan konfigurasi kolom dan pembersihan Search, Filter, dan seleksi di antara blok (S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`): membersihkan Search dan Filter Panel serta `Clear filter` di antara blok (S-09). Pada TC-FA-FAAM-694 Search `Lock` dari TC-FA-FAAM-693 masih aktif dan dipakai sesuai langkah 1 TC (Search `Lock`); Filter Category `Electronics` dibersihkan lebih dulu karena TC-FA-FAAM-694 tidak memakainya.
- Asersi absence pada TC-FA-FAAM-690 (tabel tidak memuat Asset Name Category Locked) beranchor Verifikasi `Seed Item 01` tampil (bagian 8b butir 2).
- Verifikasi aksi `Clear filter` dan `Show only these` pada notice adalah klausa tersendiri atas teks Alert yang sama (S-01).
- Di atas smell 35 langkah. Spec berjumlah 41 langkah (melewati sekitar 35). Semua blok adalah notice dan quick filter Category Locked pada client `AutoLocked` yang sama dengan satu kelas harness dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: Pre-setup #12c berupa client tanpa baris akun Total Control (email tidak tertulis).
