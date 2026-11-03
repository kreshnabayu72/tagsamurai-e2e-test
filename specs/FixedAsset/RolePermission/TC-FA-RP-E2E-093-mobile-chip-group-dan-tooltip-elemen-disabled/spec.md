---
id: TC-FA-RP-E2E-093-mobile-chip-group-dan-tooltip-elemen-disabled
title: "Mobile: chip Group dan tooltip elemen Disabled"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1028
  - TC-FA-RP-1099
coverage:
  mobile: automated
---

# Mobile: chip Group dan tooltip elemen Disabled

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi native Android (PRD §4.6); tampilan berupa card list. Perangkat atau emulator Android dengan aplikasi native TAG Samurai Fixed Asset terpasang, serta kemampuan mengetuk elemen UI. Perangkat Android uji dipakai bersama sehingga suite berjalan serial (`parallel: false`).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Login di aplikasi Android di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama).
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #18 (pohon Group Company Alpha), #21 (seed pemegang Update Manage asset & TAG), dan #36 (Tab Total Control terisi, memuat Admin Utama). Spec tidak mengubah data.
- Jeda nyata: langkah 15 menunggu paling lama 30 detik sampai tooltip hilang otomatis (TC tidak menyebut durasi tooltip; 30 detik adalah batas jeda pendek nyata pilihan spec, bagian 6).

## Test Steps

### TC-FA-RP-1028: Mobile: chip Group menentukan tampil atau Hidden toggle dan ikon info keterangan approver registrasi

1. Buka Fixed Asset > Settings > Role & Permission > System di aplikasi Android, lalu buka Detail Role `Manage asset & TAG`
2. Pastikan chip Group `All Groups` terpilih
3. Verifikasi card prompt `Select a group from the sidebar to view and manage its approval settings.` tampil
4. Verifikasi toggle `Require Approval for Registration` dan ikon info Hidden
5. Pilih chip Group `IT Infrastructure`
6. Verifikasi toggle `Require Approval for Registration` dan ikon info tampil
7. Ketuk ikon info `ⓘ` di samping label toggle
8. Verifikasi tooltip dengan teks `Approvers are users with Update access on Manage asset & TAG that covers this group, Group Managers over this group, and Total Control users. Grant Update access in the table below.`
9. Verifikasi tooltip tanpa tabel daftar approver

### TC-FA-RP-1099: Mobile: tap pada elemen Disabled menampilkan tooltip yang hilang otomatis, bukan toast

10. Buka Tab `Total Control` di aplikasi Android
11. Ketuk `[⋯]` pada card Admin Utama
12. Ketuk `Remove` yang Disabled
13. Verifikasi tooltip `Default User cannot be modified.` tampil
14. Verifikasi tidak ada toast
15. Tunggu paling lama 30 detik sampai tooltip hilang
16. Verifikasi tooltip hilang otomatis tanpa interaksi

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-1028, TC-FA-RP-1099).
- Langkah penghubung (S-03): membuka halaman di aplikasi Android; memilih chip Group `All Groups` (langkah 2); menunggu tooltip hilang (langkah 15).
- Automation TC: Manual Only (b) native Android; hambatan teknis bukan alasan mengeluarkan TC dari spec (bagian 2). `coverage.mobile` diusulkan `automated`.
- Langkah 9 (tooltip tanpa tabel daftar approver) diasersi setelah tooltip tampil (langkah 8) sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-RP-1028 tidak menyebut apakah Detail Role `Manage asset & TAG` berada di section Group Role; spec membukanya lewat Detail Role dengan chip Group.
  - TC-FA-RP-1099 tidak menyebut durasi tooltip hilang otomatis; spec memakai batas tunggu 30 detik (S-15).
  - Copy tooltip dan card prompt bertanda `copy usulan, PRD 12 #1` (keputusan NC-02) diasersi literal sesuai TC; bergantung pada persetujuan PM.
