---
id: TC-FA-TDC-E2E-112-dialog-bulk-screening-deactivate-jamak-campuran-dan-blok
title: "Dialog Bulk Screening Deactivate Jamak Campuran dan Blok"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-426
  - TC-FA-TDC-427
  - TC-FA-TDC-428
coverage:
  web: automated
---

# Dialog Bulk Screening Deactivate Jamak Campuran dan Blok

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding dan pemulihan lewat API, serta flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dataset spec ini, `Fixture.fixedAssetTaxDepreciationClass.dataset112`, di-seed lewat API di hook `before` dan dipulihkan di hook `after`): tabel satu halaman berisi NB-1 (Active, Used By 5), NB-2 (Active, Used By 3), NB-3, NB-4, dan NB-SL (Active, Used By 0). Kode class ditulis literal sesuai TC tanpa suffix `{runId}-<NNN>` (S-12): Class Code maksimal 15 karakter sehingga suffix tidak muat (lihat Temuan untuk QA). Semua dialog hanya dibuka lalu dibatalkan; tidak ada data yang berubah. Data Dinamis: tidak ada.
- Kemampuan teknis: mencentang checkbox baris; membaca isi dialog (judul, bullet, kalimat, tombol footer dan gayanya).
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-428: Screening dialog blok Deactivate jamak (semua diblokir)

1. Centang checkbox baris NB-1 dan NB-2
2. Klik `Deactivate` pada Bulk Action Bar
3. Verifikasi header dialog berjudul "Cannot Deactivate Tax Depreciation Classes"
4. Verifikasi body dialog memuat `• NB-1 – Bukan bangunan – Kelompok 1 — "used by asset classes"` dan `• NB-2 – Bukan bangunan – Kelompok 2 — "used by asset classes"`
5. Verifikasi body dialog ditutup kalimat "These classes cannot be deactivated."
6. Verifikasi footer dialog memuat satu tombol `[OK]`
7. Klik `[OK]` pada dialog blok
8. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-426: Screening dialog Deactivate jamak (semua lolos)

9. Centang checkbox baris NB-3 dan NB-4
10. Klik `Deactivate` pada Bulk Action Bar
11. Verifikasi header dialog berjudul "Deactivate Tax Depreciation Classes"
12. Verifikasi body dialog memuat bullet `• NB-3 – Bukan bangunan – Kelompok 3` dan `• NB-4 – Bukan bangunan – Kelompok 4` tanpa diringkas
13. Verifikasi body dialog memuat kalimat "Are you sure you want to deactivate them?"
14. Verifikasi tidak ada Alert peringatan pada dialog
15. Verifikasi footer dialog memuat tombol `[Cancel]` lalu `[Deactivate]`
16. Verifikasi tombol `[Deactivate]` bergaya danger
17. Klik `[Cancel]` pada dialog
18. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-427: Screening dialog Deactivate campuran

19. Centang checkbox baris NB-3, NB-4, dan NB-2
20. Klik `Deactivate` pada Bulk Action Bar
21. Verifikasi header dialog berjudul "Deactivate Tax Depreciation Classes"
22. Verifikasi bagian pertama body dialog: label "The following will be deactivated:" diikuti bullet `• NB-3 – Bukan bangunan – Kelompok 3` dan `• NB-4 – Bukan bangunan – Kelompok 4`
23. Verifikasi bagian kedua body dialog: label "The following cannot be deactivated and will be skipped:" diikuti `• NB-2 – Bukan bangunan – Kelompok 2 — "used by asset classes"`
24. Verifikasi body dialog ditutup kalimat "Are you sure you want to continue?"
25. Verifikasi footer dialog memuat tombol `[Cancel]` lalu `[Continue]`
26. Verifikasi tombol `[Continue]` bergaya danger
27. Klik `[Cancel]` pada dialog
28. Klik icon `×` di Bulk Action Bar

## Notes

- Urutan TC dalam spec: TC-FA-TDC-428, 426, 427 (dialog blok lebih dulu, lalu dialog lolos dan campuran; S-10). Ketiganya screening dialog tanpa aksi yang mengubah data.
- Langkah penghubung (S-03, S-09): langkah 17 dan 27 (membatalkan dialog; TC tidak menutupnya), langkah 7 (`[OK]` menutup dialog blok), dan langkah 8, 18 dan 28 (klik icon `×` agar seleksi TC berikutnya bersih).
- Temuan untuk QA:
  - TC-FA-TDC-426 Expected c dan TC-FA-TDC-427 Expected e menyebut `[Deactivate]` dan `[Continue]` "bergaya danger" tanpa menyebut atribut visual yang diasersi; spec mengasersi gaya danger sebagai klausa sendiri.
  - Email akun Total Control tidak tertulis di TC.
  - Class Code maksimal 15 karakter, sehingga suffix `{runId}-<NNN>` (S-12) tidak muat pada kode class milik spec; spec memakai kode literal TC pada dataset company khusus automation yang di-seed dan dipulihkan fixture. Perlu konfirmasi QA.
