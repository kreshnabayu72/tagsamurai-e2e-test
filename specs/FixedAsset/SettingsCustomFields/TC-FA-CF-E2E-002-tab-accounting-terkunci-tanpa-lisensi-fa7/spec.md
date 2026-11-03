---
id: TC-FA-CF-E2E-002-tab-accounting-terkunci-tanpa-lisensi-fa7
title: "Tab Accounting Terkunci pada Client Tanpa Lisensi FA-7"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-3
  - TC-FA-CF-4
  - TC-FA-CF-51
coverage:
  web: automated
---

# Tab Accounting Terkunci pada Client Tanpa Lisensi FA-7

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Starter. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_STARTER_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Starter (Pre-setup #15): plan Starter yang tidak pernah memiliki lisensi FA-7; dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE). Spec hanya membaca dan tidak mengubah data.
- Kemampuan teknis: hover; fokus keyboard (Tab dan Shift+Tab).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-3: Tab Accounting disabled dengan icon gembok

1. Verifikasi tab `Accounting` tampil, disabled, dengan icon 🔒
2. Arahkan kursor ke tab `Accounting`
3. Verifikasi tooltip `Accounting fields require the Accounting & Depreciation feature. Upgrade your plan to unlock them.` tampil
4. Klik tab `Accounting`
5. Verifikasi klik tab `Accounting` tidak membuka tabel Accounting
6. Verifikasi tab `General` tetap aktif

### TC-FA-CF-4: Tooltip tab Accounting terkunci lewat fokus keyboard

7. Pindahkan kursor keluar dari tab `Accounting`
8. Tekan Tab berulang sampai fokus keyboard tiba pada tab `Accounting`
9. Verifikasi tooltip `Accounting fields require the Accounting & Depreciation feature. Upgrade your plan to unlock them.` tampil saat fokus keyboard berada pada tab `Accounting`

### TC-FA-CF-51: Tab Accounting tetap terkunci bagi Total Control

10. Pindahkan fokus keyboard keluar dari tab `Accounting`
11. Klik tab `Accounting`
12. Verifikasi tab `Accounting` tetap disabled dengan icon 🔒 bagi Total Control
13. Verifikasi klik tab `Accounting` tidak membuka tabel Accounting sehingga tidak ada jalur UI untuk membuat atau mengelola field Accounting, dan tab `General` tetap aktif

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Spec hanya membaca; subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 (melepas kursor dari tab agar tooltip hover hilang sebelum TC-FA-CF-4) dan langkah 10 (melepas fokus keyboard sebelum klik pada TC-FA-CF-51).
- Langkah 1 TC-FA-CF-3 (Expected a) diasersi sebelum hover karena menjelaskan state awal tab (disabled, icon gembok); urutan Expected mengikuti urutan state (8b butir 5).
- Langkah 13 menerjemahkan klausa kedua Expected TC-FA-CF-51 ("user tidak punya jalur UI untuk membuat atau mengelola field Accounting") ke satu `Verifikasi` teramati: tab tidak membuka tabel Accounting dan `General` tetap aktif.
- Temuan untuk QA:
  - Pre-setup TC tidak memuat email akun Total Control Company Starter (Tabel Data Uji Pre-setup #15 hanya mendeskripsikan Company); akun disediakan tim FE.
  - TC-FA-CF-3 Langkah Uji tidak menyebut cara melepas hover antara langkah 2 dan 3; spec menambahkan langkah penghubung 7 sebelum TC-FA-CF-4.
