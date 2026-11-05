---
id: TC-GS-IMPORT-E2E-062-android-guided-tooltip-melewati-step-1-download-template-masuk-bottom
title: "Android: Guided Tooltip Saat Ada Draft Melewati Step 1 (Download Template Masuk Bottom Sheet)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-25
coverage:
  mobile: automated
---

# Android: Guided Tooltip Saat Ada Draft Melewati Step 1 (Download Template Masuk Bottom Sheet)

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`. Spec menulis `parallel: false` karena memakai perangkat Android bersama.
- Perangkat: Android native yang disediakan tim FE/BE (aplikasi TAG Samurai terpasang), Tab Brand. TC bertanda Manual Only (b) perangkat Android native; kebutuhan perangkat dicatat di sini.
- Akun: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`; login di hook `before` pada aplikasi Android. Password tidak ditulis di spec atau fixture.
- Data: draft Brand 12 baris pada Client A (Data Dinamis D-01; draft dasar Client A dipulihkan hook `beforeEach` suite).
- Guided Tooltip: spec ini membuka walkthrough lewat `[?]`; flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` sehingga walkthrough otomatis tidak muncul, dan dipulihkan hook `after`; lihat `suite.md`.

## Test Steps

1. Buka halaman Import pada aplikasi Android
2. Klik `[?]`
3. Verifikasi Step 2 (`[Upload File]`, Title "Upload File") tampil sebagai Step pertama
4. Verifikasi Step 1 (`[Download Template]`) dilewati
5. Klik `[Next]`
6. Verifikasi Step 3 (Staging Metric Cards, Title "Staging Summary") tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Spec berjalan di aplikasi Android; hanya `coverage.mobile` yang ditulis.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka halaman Import pada aplikasi).
- Temuan untuk QA:
  - TC-GS-IMPORT-25 bertanda Manual Only (b) perangkat Android native; sesuai konvensi hambatan perangkat bukan alasan mengeluarkan TC, sehingga spec tetap dibuat.
  - TC-GS-IMPORT-25 tidak menyebut cara membuka aplikasi dan login pada perangkat; spec memakai login hook `before` yang disediakan tim FE/BE.
