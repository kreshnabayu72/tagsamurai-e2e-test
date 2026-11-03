---
id: TC-FA-LBL-E2E-176-label-default-terkunci-bulk-add-form-edit-aset-dan-form-register-asset
title: "Label Default Terkunci: Bulk Add, Form Edit Aset, dan Form Register Asset"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-433
  - TC-FA-LBL-500
  - TC-FA-LBL-523
coverage:
  web: automated
---

# Label Default Terkunci: Bulk Add, Form Edit Aset, dan Form Register Asset

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Extra (Pre-setup #56, juga memegang role Update pada Manage Asset & TAG sesuai precondition TC-FA-LBL-500 dan 523), `Fixture.assetLabeling.akun.totalControlExtra`, untuk TC-FA-LBL-500 dan TC-FA-LBL-523 (langkah 1 sampai 24): akun, `{namaCompany}`, dan password belum ada, disediakan tim FE (pola Pre-setup #56 `totalControl_automated_{namaCompany}@qwertysystem.net`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). TC-FA-LBL-433 memakai Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD` (langkah 26 sampai 35; ganti akun pada langkah 25).
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Pre-setup (hanya dibaca, form ditutup tanpa menyimpan): #14 Asset Name `Warehouse Item` dengan Default Label `Warehouse Priority` dan label `Seasonal Event` (#12) untuk TC-FA-LBL-433 (Company Alpha); label `Seasonal Event` untuk TC-FA-LBL-523 adalah salinan Pre-setup #12 di Company Extra (Pre-setup #56).
- Data Dinamis (seed milik spec di Company Extra lewat fixture BE di hook `before`, bersuffix `{runId}-176`, Color `Fixture.assetLabeling.warnaSeed`; pola Pre-setup #27 dimiliki spec agar data Pre-setup tidak berubah, S-06): Asset Name `Lock Item {runId}-176` dengan Default Label `Lock Default {runId}-176`; aset Active `Lock Asset {runId}-176` yang memiliki `Lock Default {runId}-176` ber-source default dan label manual `Manual Edit 523 {runId}-176`.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.akun.totalControlExtra` | belum ada, disediakan tim FE (pola Pre-setup #56 `totalControl_automated_{namaCompany}@qwertysystem.net`; `{namaCompany}` Company Extra belum diketahui) |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): sesi API aktor dan fixture BE untuk seeding, pembersihan, dan pembacaan state; endpoint tidak ditulis di TC.
- Form Register Asset dan form Edit Asset ditutup tanpa menyimpan; spec tidak mengubah data aset selain yang dinyatakan di langkah.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label, aset, dan Asset Name seed milik spec (termasuk yang sudah berganti nama atau dibuat lewat UI) lewat fixture BE berdasarkan ID atau nama bersuffix, tanpa berasumsi seed berhasil penuh.

## Test Steps

### TC-FA-LBL-500: Bulk Add Label atas aset yang sudah memiliki label itu sebagai default

1. Buka Fixed Asset > Settings > Asset Master > tab Labels, lalu ketik Search `Lock Default {runId}-176`, tekan Enter
2. Catat Total Asset `Lock Default {runId}-176` sebagai baseline
3. Buka Fixed Asset > Asset List, ketik Search `Lock Asset {runId}-176`, tekan Enter, lalu centang baris `Lock Asset {runId}-176`
4. Klik `[🏷 Add Label]`, pilih `Lock Default {runId}-176`, lalu terapkan
5. Verifikasi toast `Success, Label has been added.`
6. Verifikasi tidak ada error
7. Buka Asset Detail baris `Lock Asset {runId}-176`
8. Verifikasi chip `Lock Default {runId}-176` tetap satu
9. Verifikasi chip `Lock Default {runId}-176` tanpa ikon `✕` (relasi tetap default dan terkunci)
10. Buka Fixed Asset > Settings > Asset Master > tab Labels, lalu ketik Search `Lock Default {runId}-176`, tekan Enter
11. Verifikasi Total Asset `Lock Default {runId}-176` sama dengan baseline (tidak bertambah)

### TC-FA-LBL-523: Form Edit Aset, label Default terkunci dan label lain bebas ditambah dan dilepas

12. Buka Fixed Asset > Asset List, ketik Search `Lock Asset {runId}-176`, tekan Enter, lalu buka form Edit Asset untuk `Lock Asset {runId}-176`
13. Verifikasi `Lock Default {runId}-176` terisi tanpa ikon `✕`
14. Verifikasi `Lock Default {runId}-176` tidak dapat dilepas di form
15. Verifikasi `Manual Edit 523 {runId}-176` tampil dengan ikon `✕`
16. Lepas label manual `Manual Edit 523 {runId}-176` lewat `✕`
17. Verifikasi `Manual Edit 523 {runId}-176` terlepas
18. Tambahkan kembali label `Manual Edit 523 {runId}-176`
19. Verifikasi `Manual Edit 523 {runId}-176` tertambah kembali
20. Tambahkan label `Seasonal Event`
21. Verifikasi `Seasonal Event` tertambah
22. Lepas label `Seasonal Event` lewat `✕`
23. Verifikasi `Seasonal Event` terlepas
24. Klik `✕` pada header form Edit Asset untuk menutup form tanpa menyimpan

### TC-FA-LBL-433: Asset Registration, label Default terkunci dan label lain bebas ditambah

25. Ganti akun: Logout, login sebagai Total Control Company Alpha `Fixture.assetLabeling.akun.totalControl` (`Spectra.env.FA_LBL_TC_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
26. Buka form Register Asset, lalu pilih Asset Name `Warehouse Item`
27. Verifikasi label `Warehouse Priority` terisi otomatis pada field label
28. Verifikasi label `Warehouse Priority` tidak dapat dilepas di form
29. Tambahkan label `Seasonal Event`
30. Verifikasi label `Seasonal Event` dapat ditambah
31. Lepas label `Seasonal Event` lewat `✕`
32. Verifikasi label `Seasonal Event` dapat dilepas bebas
33. Klik `✕` pada header form Register Asset
34. Verifikasi dialog Unsaved Changes tampil
35. Klik `[Leave]` pada dialog Unsaved Changes

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 7 (Cross-Module Sync & Foundation Cascading). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 3, 10, 12 adalah Search untuk menemukan baris target; bukan bagian Expected TC.
- Langkah penghubung (S-03): langkah 2, 7, 24, 25, 26, 33, 35 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- Urutan: TC-FA-LBL-500 dan 523 memakai aset seed yang sama; TC-FA-LBL-500 (Bulk Add yang tidak mengubah apa pun) lebih dulu, lalu TC-FA-LBL-523 (form Edit Aset dengan pemulihan nilai tersimpan di akhir), lalu TC-FA-LBL-433 (form Register Asset tanpa menyimpan).
- Pemulihan form (S-09): pada TC-FA-LBL-523 form Edit Asset berakhir dengan nilai field sama seperti tersimpan (label manual dikembalikan, `Seasonal Event` dilepas lagi) sebelum ditutup.
- Temuan untuk QA:
  - TC-FA-LBL-500 Expected a "tanpa error" tidak menyebut bentuk error; spec memeriksa tidak adanya toast atau dialog error.
  - TC-FA-LBL-523 dan 433 tidak menyatakan apakah dialog Unsaved Changes muncul saat form ditutup setelah menambah dan melepas label; spec menutup form Edit Asset lewat `✕` (nilai field sudah kembali ke nilai tersimpan) dan form Register Asset lewat `✕` dengan `[Leave]`.
  - Precondition TC-FA-LBL-500 dan 523 memakai aset Pre-setup #27 (`Locked Item - 21`, Company Extra); spec memakai aset milik spec dengan pola yang sama di Company Extra (S-06).
  - Akun dan `{namaCompany}` Company Extra (TC-FA-LBL-500 dan 523, Pre-setup #56) belum ada dan menunggu konfirmasi tim FE; TC-FA-LBL-433 memakai Total Control Company Alpha (Pre-setup #14) sehingga spec memakai dua akun sesuai TC (ganti akun pada langkah 25 ke Company Alpha).
