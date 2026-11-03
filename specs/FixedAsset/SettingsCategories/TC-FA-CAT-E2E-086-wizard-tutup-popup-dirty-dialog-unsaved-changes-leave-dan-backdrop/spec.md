---
id: TC-FA-CAT-E2E-086-wizard-tutup-popup-dirty-dialog-unsaved-changes-leave-dan-backdrop
title: "Wizard Consolidation: Menutup Popup dengan Centang Berubah, Dialog Unsaved Changes, [Leave], dan Backdrop"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-298
  - TC-FA-CAT-576
  - TC-FA-CAT-299
coverage:
  web: automated
---

# Wizard Consolidation: Menutup Popup dengan Centang Berubah, Dialog Unsaved Changes, [Leave], dan Backdrop

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPostT0 (Pre-setup #33), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #33 (CatPostT0, plan Starter cap 5, T-0 sudah lewat, belum pernah submit selection): 8 kategori `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`. Spec tidak menekan `[Save Selection]`, sehingga state client tidak berubah.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-298: Menutup popup dengan centang berbeda memunculkan dialog Unsaved Changes, [Cancel] mempertahankan popup dan centang

1. Klik `[Choose Categories]` pada Alert Category Consolidation
2. Centang `Keep usable` pada `Alpha Tech`
3. Klik `[Cancel]`
4. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
5. Verifikasi dialog memuat tombol `[Cancel]` dan `[Leave]`
6. Klik `[Cancel]` pada dialog
7. Verifikasi dialog tertutup
8. Verifikasi popup Consolidation tetap terbuka
9. Verifikasi centang `Keep usable` pada `Alpha Tech` tetap ada

### TC-FA-CAT-576: Menutup popup lewat icon (✕) lalu [Leave] menutup popup tanpa menyimpan

10. Klik icon (✕) pada popup
11. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]` tampil
12. Klik `[Leave]` pada dialog
13. Verifikasi dialog dan popup tertutup
14. Verifikasi Alert Category Consolidation tetap tampil
15. Klik `[Choose Categories]` lagi
16. Verifikasi seluruh checkbox `Keep usable` unchecked (tanpa centang sebelumnya)

### TC-FA-CAT-299: Menutup popup tanpa perubahan centang tidak memunculkan dialog dan backdrop tidak menutup

17. Klik area backdrop
18. Verifikasi popup tetap terbuka (backdrop tidak menutup popup)
19. Tekan `Esc`
20. Verifikasi popup tertutup
21. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tidak tampil (belum ada centang berbeda)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Urutan TC: TC-FA-CAT-298, TC-FA-CAT-576, TC-FA-CAT-299 (kasus tanpa submit memakai popup yang sama berulang; kasus menutup form di akhir, S-10). Langkah 2 TC-FA-CAT-576 (mencentang `Alpha Tech`) tidak diulang karena centang dari langkah 2 masih ada pada popup yang terbuka (dibuktikan langkah 8 dan 9).
- TC-FA-CAT-299 memakai popup yang dibuka ulang pada langkah 15 (seluruh checkbox unchecked, tidak ada perubahan centang).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1 dan 15 (membuka popup), 3 dan 10 (memicu penutupan), 17 dan 19 (aksi penutupan yang hasilnya diasersi pada langkah sesudahnya).
- Asersi absence langkah 21 memakai langkah 20 (popup tertutup) dan langkah 14 (Alert tampil) sebagai anchor positif pada halaman yang sama (8b.2).
- Temuan untuk QA:
  - TC-FA-CAT-576 mensyaratkan `Alpha Tech` dicentang sebagai langkah 2 dari keadaan popup baru; spec melanjutkan dari popup TC-FA-CAT-298 yang masih berisi centang itu.
