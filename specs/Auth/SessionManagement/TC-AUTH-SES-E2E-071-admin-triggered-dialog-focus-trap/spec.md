---
id: TC-AUTH-SES-E2E-071-admin-triggered-dialog-focus-trap
title: "Accessibility Focus Trap dan Role Alertdialog Dialog Lifecycle yang Dipicu Aksi Admin"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-306
  - TC-AUTH-SES-307
  - TC-AUTH-SES-308
coverage:
  web: automated
---

# Accessibility Focus Trap dan Role Alertdialog Dialog Lifecycle yang Dipicu Aksi Admin

## Prerequisites

- Mode: FE+BE.
- Akun aktor (Tabel Data Uji Pre-setup #1, #2, #4, #32), nilai `{namaCompany}` Client `Alpha Logistik`:
  - Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`: seeding user Client `Alpha Logistik` (hook `before`) dan penghapusan user di Browser Admin (TC-AUTH-SES-306). Browser Admin login sebagai akun ini di hook `before` (akun default suite, Pre-setup #1).
  - Total Control (Global Settings) dengan scope Client Suspend (Tabel Data Uji Pre-setup #32): seeding user Client Suspend (hook `before`, lewat API) dan penghapusan user itu di hook `after`.
  - Manage Global License `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_MGL_PASSWORD`: Force Logout di `PLATFORM SETTINGS > License > Concurrent User` Fixed Asset (TC-AUTH-SES-307). Browser License login sebagai akun ini di hook `before`.
  - Principal Admin Console `principalAdminConsole_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD`: Suspend dan Unsuspend Client Suspend (TC-AUTH-SES-308), login di Browser Admin lewat langkah ganti akun eksplisit.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control): tiga user profil BASE (user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-306: `Maya Setiawan` (`mayasetiawan+{runId}-071@qwertysystem.net`), Client `Alpha Logistik` (Pre-setup #5 dan #11)
  - TC-AUTH-SES-307: `Fajar Santoso` (`fajarsantoso+{runId}-071@qwertysystem.net`), Client `Alpha Logistik` (Pre-setup #5 dan #11), App Access Fixed Asset
  - TC-AUTH-SES-308: `Lestari Kusuma` (`lestarikusuma+{runId}-071@qwertysystem.net`), Client Suspend (Pre-setup #16, berstatus tidak Suspended saat spec mulai), seeding oleh akun aktor Total Control scope Client Suspend (Pre-setup #32)
- Sesi web aktif (status Active) tiap user di Browser A dibuat lewat login API oleh langkah seeding di awal TC masing-masing, bukan di hook `before`.
- Hook `after`: akhiri semua sesi seed (web dan sesi-produk), tutup konteks Browser A, Browser Admin, dan Browser License, pastikan Client Suspend tidak berstatus Suspended (Unsuspend lewat API oleh Principal Admin Console bila masih Suspended) sebelum user Client Suspend dihapus, kembalikan sesi Browser Admin ke akun aktor default suite (Total Control), hapus semua user seed. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh (user `Maya Setiawan` sudah dihapus pada TC-AUTH-SES-306).
- Environment variable: `GS_TC_PASSWORD`, `FA_MGL_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness c: multi-konteks): navigasi keyboard Tab dan Shift+Tab dengan pelacakan elemen yang sedang terfokus; pemeriksaan atribut DOM `role` pada dialog; konteks Browser A (Chrome on Windows), Browser Admin, dan Browser License bersamaan; reCAPTCHA mode uji di environment.
- Suite berjalan serial (`parallel: false`); state global yang diubah: status Client Suspend menjadi Suspended pada TC-AUTH-SES-308 (efek: Last Updated Client Suspend berubah; dipulihkan oleh langkah Unsuspend di akhir TC itu dan di hook `after`); user `Maya Setiawan` dihapus pada TC-AUTH-SES-306 (hapus di `after` tidak berasumsi user masih ada).
- Akun yang dipakai: user uji masing-masing TC di Browser A (bukan akun aktor); akun aktor Total Control di Browser Admin pada TC-AUTH-SES-306, akun Manage Global License di Browser License pada TC-AUTH-SES-307, akun Principal Admin Console di Browser Admin pada TC-AUTH-SES-308.

## Test Steps

### TC-AUTH-SES-306: Focus trap dan role alertdialog pada Dialog "Account no longer Active"

1. Buka konteks Browser A baru lalu buat sesi web aktif `Maya Setiawan` lewat login API (seeding BE) → sesi berstatus Active
2. Di Browser A buka Portal — Product Hub sebagai `mayasetiawan+{runId}-071@qwertysystem.net` → halaman Portal — Product Hub tampil
3. Di Browser Admin (akun aktor Total Control) buka `Global Settings > User`, cari `Maya Setiawan` (`mayasetiawan+{runId}-071@qwertysystem.net`), lalu hapus user tersebut sampai konfirmasi selesai
4. Pindah ke Browser A → Dialog "Account no longer Active" muncul
5. Tekan Tab dan Shift+Tab berulang kali (5 kali tiap arah) sambil mencatat elemen yang terfokus
6. Verifikasi Fokus keyboard hanya berpindah di dalam Dialog "Account no longer Active"
7. Periksa atribut peran dialog
8. Verifikasi Dialog memiliki `role="alertdialog"`

### TC-AUTH-SES-307: Focus trap dan role alertdialog pada Dialog "Log Out"

9. Buka konteks Browser A baru lalu buat sesi web aktif dan sesi-produk Fixed Asset Active `Fajar Santoso` lewat login API (seeding BE) → seat terpakai
10. Di Browser A buka Fixed Asset → halaman di dalam Fixed Asset tampil
11. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset), pilih `Fajar Santoso`, lalu klik [Force Logout] dan [Confirm Logout] pada dialog konfirmasi "Force Logout User"
12. Pindah ke Browser A → Dialog "Log Out" muncul
13. Tekan Tab dan Shift+Tab berulang kali (5 kali tiap arah) sambil mencatat elemen yang terfokus
14. Verifikasi Fokus keyboard hanya berpindah di dalam Dialog "Log Out"
15. Periksa atribut peran dialog
16. Verifikasi Dialog memiliki `role="alertdialog"`

### TC-AUTH-SES-308: Focus trap dan role alertdialog pada Dialog "Access Restricted"

17. Buka konteks Browser A baru lalu buat sesi web aktif `Lestari Kusuma` lewat login API (seeding BE) → sesi berstatus Active
18. Di Browser A buka Portal — Product Hub sebagai `lestarikusuma+{runId}-071@qwertysystem.net` → halaman Portal — Product Hub tampil
19. Di Browser Admin ganti akun: logout akun aktor Total Control, lalu login sebagai `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.AC_PRINCIPAL_PASSWORD` → halaman beranda Admin Console tampil
20. Di Browser Admin buka `Admin Console > Client`, buka menu elipsis Client Suspend dan pilih Suspend
21. Pindah ke Browser A → Dialog "Access Restricted" muncul
22. Tekan Tab dan Shift+Tab berulang kali (5 kali tiap arah) sambil mencatat elemen yang terfokus
23. Verifikasi Fokus keyboard hanya berpindah di dalam Dialog "Access Restricted"
24. Periksa atribut peran dialog
25. Verifikasi Dialog memiliki `role="alertdialog"`
26. Di Browser Admin buka `Admin Console > Client`, buka menu elipsis Client Suspend dan pilih Unsuspend (pemulihan status Client)

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness c (multi-konteks); seluruh dialog dipicu aksi admin.
- TC-AUTH-SES-251, 252, 305, 309, 310, 311, dan 312 ada di spec `TC-AUTH-SES-E2E-020-accessibility-focus-trap-dialog-lifecycle`.
- Urutan TC-AUTH-SES-306, 307, 308 sama dengan TC sumber. TC-AUTH-SES-308 paling akhir karena mengubah status Client Suspend (state global bersama), dipulihkan dengan Unsuspend di langkah 26 dan hook `after`. Pergantian akun aktor di Browser Admin (langkah 19) hanya terjadi pada TC-AUTH-SES-308; Browser Admin sudah login sebagai Total Control di hook `before`, sehingga TC-AUTH-SES-306 tidak punya langkah login. TC-AUTH-SES-307 memakai Browser License yang sudah login di hook `before`.
- Dependensi (S-04): langkah pemicu tiap dialog disalin dari TC dependensi tanpa asersi isi dialog: TC-AUTH-SES-306 dari TC-AUTH-SES-6, TC-AUTH-SES-307 dari TC-AUTH-SES-8, TC-AUTH-SES-308 dari TC-AUTH-SES-9.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): membuka konteks browser dan membuat sesi seed; membuka Portal — Product Hub dan Fixed Asset; ganti akun Browser Admin (langkah 19); mencatat elemen yang terfokus; memeriksa atribut peran; berpindah antar Browser A dan Admin; Unsuspend Client Suspend pada langkah 26.
- Temuan untuk QA: (1) TC-AUTH-SES-308 men-Suspend Client Suspend (Pre-setup #16) yang dipakai bersama spec lain; efeknya (write-lockdown) dipulihkan di langkah 26 dan hook `after`. (2) "Berulang kali (minimal 5 kali)" ditulis 5 kali tiap arah; TC tidak menyebut cara mengamati elemen terfokus, sehingga pelacakan fokus dan pemeriksaan `role` diputuskan di tahap script. (3) TC-AUTH-SES-306 menulis "hapus user tersebut sampai konfirmasi selesai" tanpa merinci dialog konfirmasi hapus. (4) TC-AUTH-SES-306 sampai 308 tidak menyebut widget reCAPTCHA pada langkah login; spec mengikuti TC dan mengandalkan reCAPTCHA mode uji.
