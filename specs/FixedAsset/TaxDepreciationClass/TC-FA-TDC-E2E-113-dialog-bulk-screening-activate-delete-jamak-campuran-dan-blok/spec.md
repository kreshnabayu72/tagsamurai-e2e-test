---
id: TC-FA-TDC-E2E-113-dialog-bulk-screening-activate-delete-jamak-campuran-dan-blok
title: "Dialog Bulk Screening Activate Delete Jamak Campuran dan Blok"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-429
  - TC-FA-TDC-430
  - TC-FA-TDC-431
  - TC-FA-TDC-432
coverage:
  web: automated
---

# Dialog Bulk Screening Activate Delete Jamak Campuran dan Blok

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding dan pemulihan lewat API, serta flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dataset spec ini, `Fixture.fixedAssetTaxDepreciationClass.dataset113`, di-seed lewat API di hook `before` dan dipulihkan di hook `after`): tabel satu halaman berisi NB-OLD dan NB-OLD2 (Inactive, Used By 0), NB-3 dan NB-4 (Active, Used By 0, Last Posted Tax Year kosong), NB-2 (Used By 3, tanpa Last Posted Tax Year), NB-1 (Last Posted Tax Year 2026, Used By 5), dan NB-KHS (Last Posted Tax Year 2026, Used By 0). Kode class ditulis literal sesuai TC tanpa suffix `{runId}-<NNN>` (S-12): Class Code maksimal 15 karakter sehingga suffix tidak muat (lihat Temuan untuk QA). Semua dialog hanya dibuka lalu dibatalkan; tidak ada data yang berubah. Data Dinamis: tidak ada.
- Kemampuan teknis: mencentang checkbox baris; membaca isi dialog (judul, bullet, kalimat, tombol footer dan gayanya).
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-432: Screening dialog blok Delete jamak (semua diblokir)

1. Centang checkbox baris NB-1, NB-KHS, dan NB-2
2. Klik `Delete` pada Bulk Action Bar
3. Verifikasi header dialog berjudul "Cannot Delete Tax Depreciation Classes"
4. Verifikasi body dialog memuat `• NB-1 – Bukan bangunan – Kelompok 1 — "has posted fiscal depreciation"`, `• NB-KHS – Kelompok khusus pernah diposting — "has posted fiscal depreciation"`, dan `• NB-2 – Bukan bangunan – Kelompok 2 — "used by asset classes"`
5. Verifikasi body dialog ditutup kalimat "These classes cannot be deleted."
6. Verifikasi footer dialog memuat satu tombol `[OK]`
7. Klik `[OK]` pada dialog blok
8. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-429: Screening dialog Activate jamak

9. Centang checkbox baris NB-OLD dan NB-OLD2
10. Klik `Activate` pada Bulk Action Bar
11. Verifikasi header dialog berjudul "Activate Tax Depreciation Classes"
12. Verifikasi body dialog memuat bullet `• NB-OLD – Kelompok khusus lama` dan `• NB-OLD2 – Kelompok khusus lama 2`
13. Verifikasi body dialog memuat kalimat "Are you sure you want to activate them?"
14. Verifikasi footer dialog memuat tombol `[Cancel]` lalu `[Activate]`
15. Klik `[Cancel]` pada dialog
16. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-430: Screening dialog Delete jamak (semua lolos)

17. Centang checkbox baris NB-3 dan NB-4
18. Klik `Delete` pada Bulk Action Bar
19. Verifikasi header dialog berjudul "Delete Tax Depreciation Classes"
20. Verifikasi body dialog memuat bullet `• NB-3 – Bukan bangunan – Kelompok 3` dan `• NB-4 – Bukan bangunan – Kelompok 4`
21. Verifikasi body dialog memuat kalimat "This action cannot be undone. Are you sure you want to delete them?"
22. Verifikasi footer dialog memuat tombol `[Cancel]` lalu `[Delete]`
23. Verifikasi tombol `[Delete]` bergaya danger
24. Klik `[Cancel]` pada dialog
25. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-431: Screening dialog Delete campuran

26. Centang checkbox baris NB-3, NB-2, dan NB-KHS
27. Klik `Delete` pada Bulk Action Bar
28. Verifikasi header dialog berjudul "Delete Tax Depreciation Classes"
29. Verifikasi bagian pertama body dialog: label "The following will be deleted:" diikuti bullet `• NB-3 – Bukan bangunan – Kelompok 3`
30. Verifikasi bagian kedua body dialog: label "The following cannot be deleted and will be skipped:" diikuti `• NB-2 – Bukan bangunan – Kelompok 2 — "used by asset classes"` dan `• NB-KHS – Kelompok khusus pernah diposting — "has posted fiscal depreciation"`
31. Verifikasi body dialog ditutup kalimat "Are you sure you want to continue?"
32. Verifikasi footer dialog memuat tombol `[Cancel]` lalu `[Continue]`
33. Verifikasi tombol `[Continue]` bergaya danger
34. Klik `[Cancel]` pada dialog
35. Klik icon `×` di Bulk Action Bar

## Notes

- Urutan TC dalam spec: TC-FA-TDC-432, 429, 430, 431 (dialog blok lebih dulu; S-10). Keempatnya screening dialog tanpa aksi yang mengubah data.
- Langkah penghubung (S-03, S-09): langkah 15, 24 dan 34 (membatalkan dialog), langkah 7 (`[OK]` menutup dialog blok), dan langkah 8, 16, 25 dan 35 (klik icon `×` agar seleksi TC berikutnya bersih); TC tidak menyebutnya.
- Temuan untuk QA:
  - TC-FA-TDC-430 dan 431 menyebut `[Delete]` dan `[Continue]` "bergaya danger" tanpa atribut visual; spec mengasersi gaya danger sebagai klausa sendiri.
  - Email akun Total Control tidak tertulis di TC.
  - Class Code maksimal 15 karakter, sehingga suffix `{runId}-<NNN>` (S-12) tidak muat pada kode class milik spec; spec memakai kode literal TC pada dataset company khusus automation yang di-seed dan dipulihkan fixture. Perlu konfirmasi QA.
