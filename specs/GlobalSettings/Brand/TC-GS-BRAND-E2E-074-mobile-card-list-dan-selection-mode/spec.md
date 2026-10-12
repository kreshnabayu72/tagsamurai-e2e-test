---
id: TC-GS-BRAND-E2E-074-mobile-card-list-dan-selection-mode
title: "Mobile Android: Card List Brand dan Selection Mode untuk Bulk Delete"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-242
  - TC-GS-BRAND-243
coverage:
  mobile: automated
---

# Mobile Android: Card List Brand dan Selection Mode untuk Bulk Delete

## Prerequisites

- Mode: FE+BE (aplikasi Android terhadap backend nyata).
- Platform: aplikasi Android TAG Samurai Mobile (`coverage.mobile`); spec tidak berjalan di web.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini pada aplikasi Android; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Master Reference > Brand.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi), di-seed lewat API di hook `before`: `Mobile Co A {runId}-074` dan `Mobile Co B {runId}-074` (D-43; brand bebas relasi milik spec sendiri, sesuai TC-GS-BRAND-243). Aksi Delete pada TC-GS-BRAND-243 dikonfirmasi sampai hasil, sehingga kedua brand terhapus oleh spec.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Mobile Co A {runId}-074` dan `Mobile Co B {runId}-074` bila masih ada.
- Kemampuan teknis: gesture long-press pada card, tap, dan pembukaan bottom sheet di perangkat atau emulator Android.
- Tidak ada state global yang diubah.
- TC-GS-BRAND-242, 243: login sebagai Total Control pada aplikasi Android.

## Test Steps

### TC-GS-BRAND-242: Mobile: card list menggantikan tabel

1. Buka Master Reference > Brand di aplikasi Android
2. Verifikasi Breadcrumb `Master Reference > Brand`
3. Verifikasi Sub-tab `Brand (aktif) | Measurement`
4. Verifikasi Toolbar `[⋯]` (Column Visibility/Filter/Download/Changelog di bottom sheet)
5. Verifikasi Toolbar `[🔍]`
6. Verifikasi `[+ Brand]` di bawah toolbar
7. Verifikasi Card memuat Brand Name tebal
8. Verifikasi Card memuat angka Used By (Items) (link ke Detail)
9. Verifikasi Card memuat Last Updated
10. Verifikasi Card memuat `[⋯ Menu]`
11. Tap salah satu card
12. Verifikasi tap card membuka Detail

### TC-GS-BRAND-243: Mobile: long-press card masuk selection mode untuk Bulk Delete

13. Kembali ke daftar Brand
14. Verifikasi checkbox card tidak tampil sebelum selection mode
15. Long-press card `Mobile Co A {runId}-074`
16. Verifikasi checkbox card muncul saat selection mode aktif
17. Pilih card `Mobile Co B {runId}-074`
18. Jalankan Delete dari aksi seleksi
19. Verifikasi dialog `Delete Brands` tampil sebagai bottom sheet
20. Verifikasi dialog `Delete Brands` memuat tombol `[Cancel]`
21. Verifikasi dialog `Delete Brands` memuat tombol `[Delete]`
22. Klik [Delete] pada dialog
23. Verifikasi toast sukses: "Success, brand has been deleted."
24. Verifikasi card `Mobile Co A {runId}-074` hilang dari daftar
25. Verifikasi card `Mobile Co B {runId}-074` hilang dari daftar

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`. Spec mobile Android (`coverage.mobile: automated`). Preseden `Auth/LoginOtp` E2E-002 yang disebut konteks tidak ditemukan di folder `specs/` repo (hanya `docs/coverage/AuthLoginOtp.md`); bentuk frontmatter mengikuti spec framework mobile (`coverage.mobile: automated`, tanpa `web`).
- TC-GS-BRAND-242 (`UI Only`) tidak memerlukan data khusus; TC-GS-BRAND-243 memerlukan dua card Brand bebas relasi. Urutan: screening card list (242) dahulu, lalu selection mode (243).
- Langkah penghubung: langkah 13 (kembali ke daftar Brand dari Detail, tidak tertulis di Langkah Uji TC sumber).
- Langkah 14 (checkbox tidak tampil sebelum selection mode) berasal dari kalimat Expected Result a "Checkbox card muncul hanya saat selection mode".
- TC-GS-BRAND-243 mengonfirmasi Delete sampai hasil (toast sukses dan card hilang) sesuai TC sumber.
- Brand di TC sumber adalah Mobile Co A dan Mobile Co B (D-43), diberi suffix per run.
