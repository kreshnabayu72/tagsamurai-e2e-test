---
id: TC-FA-FAAL-E2E-064-android-toolbar-dan-guided-tooltip
title: "Android: Toolbar dan Guided Tooltip Mengikuti Tombol ⋯"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-36
coverage:
  mobile: automated
---

# Android: Toolbar dan Guided Tooltip Mengikuti Tombol ⋯

## Prerequisites

- Mode: FE+BE. Platform: aplikasi native Android Fixed Asset > Reports & Logs > Activity Log.
- Perangkat atau emulator Android dengan aplikasi Fixed Asset TAG Samurai terpasang dan driver perangkat yang mampu mengetuk dan membaca elemen UI; disediakan tim FE. Perangkat dipakai bersama sehingga suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control tanpa flag Guided Tooltip (Pre-setup #4) `totalControlNewGuide_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TCNEWGUIDE_PASSWORD`. Login di aplikasi Android di hook `before` spec ini; spec ini membuka halaman Activity Log sendiri di aplikasi karena hook `beforeEach` suite membuka halaman web. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TCNEWGUIDE_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Pengecualian atas butir "Flag Guided Tooltip" di `suite.md`: hook suite tidak men-set flag halaman Activity Log untuk akun Pre-setup #4; flag akun ini belum diset sebelum spec dijalankan (Pre-setup #4). Pemulihan flag ke keadaan belum diset sebelum spec, dan pemulihan nilai awal sesudah spec, disediakan tim FE/BE.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Data: tidak ada data log yang diasersi.

## Test Steps

### TC-FA-FAAL-36: Android: toolbar dan Guided Tooltip mengikuti tombol ⋯

1. Buka Fixed Asset > Dashboard pada aplikasi Android
2. Buka Reports & Logs > Activity Log pertama kali
3. Verifikasi toolbar memuat `[🔍]` inline dan `[⋯]`
4. Verifikasi Step 1 walkthrough menargetkan Card List
5. Lanjutkan walkthrough ke step 2
6. Verifikasi Step 2 menargetkan tombol `[⋯]` dengan Title `Filter & Search`
7. Verifikasi Step 2 Description `Use filters to narrow down the log. Available filters depend on which tab you're viewing.`
8. Lanjutkan walkthrough ke step 3
9. Verifikasi Step 3 menargetkan tombol `[⋯]` dengan Title `Download Log`
10. Verifikasi Step 3 Description `Export the activity log. The export respects your current filters and search.`
11. Selesaikan walkthrough pada step 3
12. Ketuk `[⋯]` pada toolbar
13. Verifikasi bottom sheet `[⋯]` memuat Column Visibility, Filter, dan Download

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec berjalan di aplikasi Android; `coverage.mobile: automated`. Kemampuan driver Android belum dipastikan tim FE; `coverage` dapat berubah menjadi `unsupported` bila tidak tersedia.
- Langkah penghubung (S-03): langkah 1 (menetapkan layar awal TC di Dashboard sesuai precondition TC), langkah 11 (menutup walkthrough supaya ketukan langkah 12 tidak tertahan overlay).
- Teks Description step 2 dan 3 mengikuti Expected b dan c TC-FA-FAAL-197 (Guided Tooltip web).
- TC-FA-FAAL-30 sampai 35 (Android Card List dengan akun Total Control default) ada di spec 008.
- Temuan untuk QA:
  - TC-FA-FAAL-36 tidak menyebut cara menutup walkthrough sesudah step 3 maupun label tombolnya.
  - TC-FA-FAAL-36 butir b tidak menyebut Title dan Description Step 1; spec hanya mengasersi targetnya (Card List).
