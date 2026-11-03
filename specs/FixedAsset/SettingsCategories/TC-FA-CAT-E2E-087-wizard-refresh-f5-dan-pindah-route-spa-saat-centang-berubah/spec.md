---
id: TC-FA-CAT-E2E-087-wizard-refresh-f5-dan-pindah-route-spa-saat-centang-berubah
title: "Wizard Consolidation: Refresh F5 dan Pindah Route SPA saat Centang Berubah"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-622
  - TC-FA-CAT-623
coverage:
  web: automated
---

# Wizard Consolidation: Refresh F5 dan Pindah Route SPA saat Centang Berubah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPostT0 (Pre-setup #33), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #33 (CatPostT0, plan Starter cap 5, T-0 sudah lewat, belum pernah submit selection): 8 kategori `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`. TC-FA-CAT-622 menyimpan seleksi satu centang (`Alpha Tech`) sehingga tujuh kategori menjadi Excess; langkah penghubung memulihkan Pre-setup #33 lewat fixture backend yang disediakan tim FE/BE sebelum TC-FA-CAT-623, dan hook `after` memulihkannya. Suite berjalan serial (`parallel: false`).
- Dialog `beforeunload` bawaan browser pada langkah 3 dan 9 ditangani oleh penguji (diamati lalu dibatalkan atau diterima); teks dialog ditentukan browser dan tidak diasersi.
- Menu tujuan pada langkah 14 dan 19: satu link menu lain pada sidebar navigasi aplikasi, dipilih spec karena TC tidak menyebut menunya.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-622: Refresh F5 saat centang berubah memunculkan konfirmasi bawaan browser dan tidak setelah Save Selection sukses

1. Klik `[Choose Categories]` pada Alert Category Consolidation
2. Centang `Keep usable` pada `Alpha Tech`
3. Tekan F5
4. Verifikasi konfirmasi bawaan browser (beforeunload) muncul karena centang `Keep usable` berbeda dari kondisi saat popup dibuka
5. Batalkan konfirmasi sehingga tetap di halaman
6. Klik `[Save Selection]`
7. Verifikasi toast sukses `Success, category consolidation has been updated.` tampil
8. Klik `[Choose Categories]` pada Alert Category Consolidation tanpa mengubah centang
9. Tekan F5
10. Verifikasi halaman Categories termuat ulang tanpa konfirmasi bawaan browser (Breadcrumb dan tabel tampil)

### TC-FA-CAT-623: Berpindah route SPA saat centang berubah dicegat dengan dialog Unsaved Changes

11. Pulihkan Pre-setup #33 lewat fixture dan muat ulang halaman Categories
12. Klik `[Choose Categories]` pada Alert Category Consolidation
13. Centang `Keep usable` pada `Alpha Tech`
14. Klik link menu lain pada sidebar navigasi
15. Verifikasi perpindahan route dicegat dan dialog `You have unsaved changes. Are you sure you want to leave?` tampil
16. Klik `[Cancel]` pada dialog
17. Verifikasi navigasi dibatalkan dan popup Consolidation tetap terbuka
18. Verifikasi centang `Keep usable` pada `Alpha Tech` tetap ada
19. Klik link menu lain pada sidebar navigasi lagi
20. Klik `[Leave]` pada dialog
21. Verifikasi navigasi dilanjutkan ke halaman menu tujuan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec 086 memuat TC-FA-CAT-298, 576, dan 299 (penutupan popup lewat tombol, icon, dan backdrop).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 5 (membatalkan konfirmasi), 8 (membuka popup), 11 (pemulihan fixture dan muat ulang).
- Temuan untuk QA:
  - TC-FA-CAT-622 langkah 4 menekan `[Save Selection]` dengan satu centang (`Alpha Tech`) sehingga mengubah state client; spec memulihkannya sebelum TC-FA-CAT-623.
  - TC-FA-CAT-623 tidak menyebut menu tujuan navigasi dan tidak memverifikasi bahwa seleksi tidak tersimpan setelah `[Leave]`; spec hanya mengasersi navigasi dilanjutkan.
