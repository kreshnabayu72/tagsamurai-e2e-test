---
id: TC-GS-IMPORT-E2E-218-android-dropzone-memuat-download-template-dan-upload-file-langsung
title: "Android: Dropzone Memuat Download Template dan Upload File Langsung, Guided Tooltip Step 1 Tampil"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-972
coverage:
  mobile: automated
---

# Android: Dropzone Memuat Download Template dan Upload File Langsung, Guided Tooltip Step 1 Tampil

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`. Spec menulis `parallel: false` karena memakai perangkat Android bersama.
- Perangkat: Android native yang disediakan tim FE/BE (aplikasi TAG Samurai terpasang), Tab Brand. TC bertanda Manual Only (b) perangkat Android native; kebutuhan perangkat dicatat di sini.
- Akun: Total Control Client B (Bayu Santoso) `totalControl_automated_qaTeam2@qwertysystem.net`, `Spectra.env.GS_CLIENTB_TC_PASSWORD`; login di hook `before` pada aplikasi Android. Password tidak ditulis di spec atau fixture.
- Data: Client B tanpa draft Tab Brand (Kontrak Fixture R1; skrip reset disediakan tim FE/BE).
- Guided Tooltip: spec ini membuka walkthrough lewat `[?]`; flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` sehingga walkthrough otomatis tidak muncul, dan dipulihkan hook `after`; lihat `suite.md`.

## Test Steps

1. Buka halaman Import pada aplikasi Android
2. Perhatikan Dropzone
3. Verifikasi Dropzone memuat `[Download Template]` yang terlihat langsung
4. Verifikasi Dropzone memuat `[Upload File]` yang terlihat langsung
5. Verifikasi tidak ada toolbar
6. Verifikasi tidak ada bottom sheet `[⋯]`
7. Klik `[?]`
8. Perhatikan Step yang tampil pertama
9. Verifikasi Step 1 (`[Download Template]`, Title "Download Template") menyorot tombol di Dropzone dan tidak dilewati

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Spec berjalan di aplikasi Android; hanya `coverage.mobile` yang ditulis.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka halaman Import pada aplikasi), 2 dan 8 (mengamati sesuai Langkah Uji TC).
- Langkah 5 dan 6 (absence) memakai Dropzone langkah 3 dan 4 sebagai anchor positif.
- Temuan untuk QA:
  - TC-GS-IMPORT-972 bertanda Manual Only (b) perangkat Android native; sesuai konvensi hambatan perangkat bukan alasan mengeluarkan TC, sehingga spec tetap dibuat.
  - TC-GS-IMPORT-972 tidak menyebut cara membuka aplikasi dan login pada perangkat; spec memakai login hook `before` yang disediakan tim FE/BE.
