---
id: TC-FA-PREF-E2E-013-android-dialog-d03-d04-bottom-sheet-dan-tooltip-disabled
title: "Android: dialog D-03 dan D-04 sebagai bottom sheet, tooltip elemen Disabled bagi Read Only"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-72
  - TC-FA-PREF-606
  - TC-FA-PREF-607
coverage:
  mobile: automated
---

# Android: dialog D-03 dan D-04 sebagai bottom sheet, tooltip elemen Disabled bagi Read Only

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi native Android (bukan browser web); emulator atau perangkat Android dengan aplikasi mobile terpasang disediakan tim FE. Perangkat dipakai bersama, sehingga spec berjalan serial (`parallel: false`).
- Role yang diuji:

  | TC | Role | Pre-setup | Email | Env var password |
  |---|---|---|---|---|
  | TC-FA-PREF-606, TC-FA-PREF-607 | Total Control | PA-4 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
  | TC-FA-PREF-72 | Read Only | PA-4 | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |
- Login akun aktor pertama (Total Control, company `PT Contoh Konstruksi`) di aplikasi Android di hook `before` spec ini. Pengecualian atas `suite.md`: hook `beforeEach` web suite tidak membuka layar untuk spec ini; langkah membuka Tab Preferences ditulis di langkah. Ganti akun ke Read Only memakai langkah logout dan login eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Env var `FA_TC_PASSWORD` dan `FA_RO_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data awal (seed di hook `before`): Preferences company dalam nilai awal (PC-1, setara PA-2): Fiscal Year Start January, In-service Date Source Activation date; tidak terkunci; belum ada posting penyusutan; semua periode Open; Asset Class IT Equipment tersedia.
- Pemicu TC-FA-PREF-606: posting penyusutan pertama pada Asset Class IT Equipment dibuat lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`) setelah dialog Save Changes terbuka. Pemulihan: seed ulang PC-1 (tanpa posting penyusutan) lewat API pada langkah penghubung dan di hook `after`. Kemampuan penandaan posting penyusutan pertama disediakan tim FE/BE.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).

## Test Steps

### TC-FA-PREF-606: Dialog Cannot Save Preferences (D-03) sebagai bottom sheet

1. Buka Tab Preferences pada aplikasi Android
2. Ubah Select Fiscal Year Start dari "January" menjadi "July"
3. Ketuk `[Save changes]` sampai dialog Save Changes tampil
4. Lewat sesi API aktor, tandai posting penyusutan pertama pada Asset Class IT Equipment hingga tersimpan
5. Ketuk `[Save]` pada dialog Save Changes
6. Verifikasi dialog "Cannot Save Preferences" tampil sebagai bottom sheet (bukan dialog tengah layar)
7. Verifikasi body dialog: "Fiscal Year Start and First Accounting Period are locked because depreciation has been posted or a period has been closed. The page has been reloaded with the latest lock status."
8. Verifikasi dialog hanya memuat tombol `[OK]`
9. Ketuk `[OK]`
10. Seed ulang Preferences company ke PC-1 (tanpa posting penyusutan) lewat API lalu buka ulang Tab Preferences pada aplikasi Android

### TC-FA-PREF-607: Dialog Unsaved Changes (D-04) sebagai bottom sheet

11. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
12. Tinggalkan halaman dengan mengetuk entri navigasi aplikasi selain Accounting
13. Verifikasi dialog D-04 tampil sebagai bottom sheet (bukan dialog tengah layar)
14. Verifikasi dialog D-04 tanpa Title
15. Verifikasi body dialog: "You have unsaved changes. Are you sure you want to leave?"
16. Verifikasi tombol `[Cancel]` dan `[Leave]` tampil
17. Ketuk `[Leave]`

### TC-FA-PREF-72: Tooltip elemen Disabled bagi Read Only

18. Logout dari akun Total Control pada aplikasi Android
19. Login sebagai Read Only (`readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_RO_PASSWORD`)
20. Buka Tab Preferences pada aplikasi Android
21. Ketuk Select Fiscal Year Start yang Disabled
22. Verifikasi tooltip "You don't have permission to edit." tampil
23. Verifikasi tidak ada toast yang tampil
24. Verifikasi tooltip "You don't have permission to edit." hilang otomatis

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan blok: TC-FA-PREF-72 (Read Only) ditaruh di akhir supaya akun pertama (Total Control) login di hook `before` dan hanya ada satu pergantian akun (S-07, S-10).
- Langkah penghubung (S-03): "Ketuk `[OK]`" dan seed ulang PC-1 setelah TC-FA-PREF-606; "Ketuk `[Leave]`" setelah TC-FA-PREF-607 (menutup form dirty secara deterministik dan membuang perubahan, S-08, S-09); pasangan logout dan login di awal blok TC-FA-PREF-72.
- Asersi absence toast pada TC-FA-PREF-72 diletakkan segera setelah pemicu dengan tooltip sebagai anchor positif (8b butir 11).
- Spec berjalan di aplikasi mobile saja; `coverage.web` tidak ditulis (bagian 8).
- Temuan untuk QA:
  - TC-FA-PREF-606 Post Condition ("Preferences company belum berubah") dan TC-FA-PREF-607 Post Condition ("In-service Date Source tetap Activation date") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01).
  - TC-FA-PREF-72, 606, dan 607 tidak menyebut nama env var password; nama `FA_TC_PASSWORD` dan `FA_RO_PASSWORD` diusulkan spec dan perlu keputusan tim.
  - TC-FA-PREF-606 menulis pemicu "Lewat fixture BE" tanpa menyebut sesi API; spec memakai sesi API aktor (butir "Sesi API aktor" di `suite.md`).
