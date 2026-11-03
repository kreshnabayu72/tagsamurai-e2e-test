---
id: TC-FA-PREF-E2E-004-navigasi-tab-preferences-tautan-langsung-entri-sidebar-form-company-dan-layout-tablet
title: "Navigasi Tab Preferences: Klik Tab, Tautan Langsung, Entri Sidebar, Form Company Langsung, dan Layout Tablet"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-15
  - TC-FA-PREF-16
  - TC-FA-PREF-17
  - TC-FA-PREF-601
  - TC-FA-PREF-67
coverage:
  web: automated
---

# Navigasi Tab Preferences: Klik Tab, Tautan Langsung, Entri Sidebar, Form Company Langsung, dan Layout Tablet

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Precondition TC-FA-PREF-15 (posisi di tab Chart of Accounts) dan TC-FA-PREF-16 dan 17 (posisi di halaman aplikasi lain) dibentuk oleh langkah penghubung (langkah 1, 6, dan 11).
- Data Pre-setup (hanya dibaca, tidak diubah): Preferences nilai awal PA-2, tidak terkunci, semua setting wajib terisi: Fiscal Year Start January; First Accounting Period March 2026; Default Capitalization Threshold 5.000.000; In-service Date Source Activation date. Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API).
- TC-FA-PREF-601 memakai seri fixture PC-1; nilai awal Preferences PC-1 setara PA-2. Seed ulang ke nilai awal PC-1 dilakukan lewat langkah penghubung (langkah 14), disediakan tim FE/BE.
- Tautan langsung ke Settings > Accounting > Preferences (langkah 7) disediakan tim FE; TC tidak menyebut alamatnya.
- Viewport lebar tablet (langkah 18) mengikuti breakpoint tablet design system; nilai pikselnya ditetapkan tim FE karena TC tidak menyebutnya. Viewport dipulihkan ke ukuran awal pada langkah 21.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-15: Memilih Tab Preferences dari tab lain

1. Klik Tab "Chart of Accounts"
2. Klik Tab "Preferences"
3. Verifikasi Tab "Preferences" aktif
4. Verifikasi Breadcrumb "Settings > Accounting > Preferences" tampil
5. Verifikasi Form Preferences memuat nilai tersimpan: Fiscal Year Start "January", First Accounting Period "March" "2026", Default Capitalization Threshold "Rp 5.000.000,00", In-service Date Source "Activation date"

### TC-FA-PREF-16: Tautan langsung Preferences

6. Pindah ke halaman aplikasi lain di luar Settings > Accounting
7. Buka tautan langsung ke Settings > Accounting > Preferences pada address bar
8. Verifikasi Tab "Preferences" aktif tanpa klik tab
9. Verifikasi Breadcrumb "Settings > Accounting > Preferences" tampil
10. Verifikasi Form Preferences memuat nilai tersimpan: Fiscal Year Start "January", First Accounting Period "March" "2026", Default Capitalization Threshold "Rp 5.000.000,00", In-service Date Source "Activation date"

### TC-FA-PREF-17: Entri sidebar Accounting

11. Pindah ke halaman aplikasi lain di luar Settings > Accounting
12. Klik entri sidebar "Accounting" untuk masuk Settings > Accounting
13. Verifikasi Tab "Preferences" berstatus aktif pada tab bar

### TC-FA-PREF-601: Form company client langsung tanpa pemilihan company

14. Seed ulang Preferences company ke nilai awal PC-1 hingga tersimpan
15. Muat ulang halaman dengan F5
16. Verifikasi Form Preferences company client langsung tampil
17. Verifikasi tidak ada kontrol pemilihan company

### TC-FA-PREF-67: Layout lebar tablet

18. Atur viewport ke lebar tablet
19. Verifikasi daftar anchor tampil sebagai baris di atas form (bukan kolom sticky di kiri)
20. Verifikasi field di dalam SectionCard tersusun satu kolom
21. Pulihkan viewport ke ukuran awal

## Notes

- Langkah penghubung (S-03): langkah 1 (membentuk precondition TC-FA-PREF-15), langkah 6 dan 11 (membentuk precondition halaman aplikasi lain), langkah 14 dan 15 (seed ulang seri PC-1 dan muat ulang agar form memuat nilai seed), serta langkah 21 (memulihkan viewport). Layar Preferences dibuka hook `beforeEach` suite, sehingga langkah TC "Buka Tab Preferences" tidak diulang.
- Urutan TC dalam spec: navigasi lebih dulu, TC-FA-PREF-601, lalu TC-FA-PREF-67 di akhir karena mengubah viewport. Spec tidak mengubah Preferences; form tidak dirty di akhir spec.
- TC-FA-PREF-18, 19, dan 20 (status `[Save changes]` dan `[Cancel]`) ada di spec 155.
- Temuan untuk QA:
  - TC-FA-PREF-15 dan 16 menulis "Form Preferences memuat nilai tersimpan" tanpa menyebut nilainya; spec mengasersi empat nilai wajib PA-2 sebagai wakil nilai tersimpan.
  - TC-FA-PREF-16 dan 17 menyebut precondition "halaman aplikasi lain" tanpa menamai halamannya, dan TC-FA-PREF-16 tidak menyebut alamat tautan langsung; keduanya disediakan tim FE.
  - TC-FA-PREF-67 menyebut "breakpoint tablet design system" tanpa nilai lebar.
  - TC-FA-PREF-601 memakai seri PC-1 sedangkan TC lain di spec ini memakai seri PA-2; spec mengasumsikan nilai awal keduanya setara (Catatan TC: seri fixture seed terisolasi).
