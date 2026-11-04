---
id: TC-FA-TDC-E2E-118-matriks-bulk-deactivate-1-sampai-4a
title: "Matriks Bulk Deactivate 1 sampai 4a"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-447
  - TC-FA-TDC-448
  - TC-FA-TDC-449
  - TC-FA-TDC-450
coverage:
  web: automated
---

# Matriks Bulk Deactivate 1 sampai 4a

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding dan pemulihan lewat API, serta flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dataset spec ini, `Fixture.fixedAssetTaxDepreciationClass.dataset118`, di-seed lewat API di hook `before` dan dipulihkan di hook `after`): tabel satu halaman berisi NB-1 (Active, Used By 5), NB-2 (Active, Used By 3), NB-3 dan NB-4 (Active, Used By 0), NB-SL (Active), dan NB-OLD (Inactive). NB-3 dan NB-4 menjadi target aksi tulis (milik dataset spec ini). Kode class ditulis literal sesuai TC tanpa suffix `{runId}-<NNN>` (S-12): Class Code maksimal 15 karakter sehingga suffix tidak muat (lihat Temuan untuk QA). Data Dinamis: tidak ada.
- Kemampuan teknis: mencentang checkbox baris; memulihkan status NB-3 dan NB-4 ke Active lewat API di tengah spec (sesi API aktor sesuai `suite.md`).
- State global yang diubah: status Active NB-3 dan NB-4 (dipulihkan pada langkah 24 dan di hook `after`).

## Test Steps

### TC-FA-TDC-449: Matriks 3: Bulk Deactivate semua class dipakai Asset Class diblokir

1. Centang checkbox baris NB-1 dan NB-2
2. Klik `Deactivate` pada Bulk Action Bar
3. Klik `[OK]` pada dialog D-02 jamak
4. Verifikasi toggle `Active` baris NB-1 dan NB-2 tetap On
5. Verifikasi tidak ada toast tampil
6. Verifikasi seleksi dipertahankan
7. Verifikasi Bulk Action Bar dipertahankan
8. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-450: Matriks 4a: Bulk Deactivate seleksi campuran, subset Active semua lolos

9. Centang checkbox baris NB-3, NB-4, dan NB-OLD
10. Klik `Deactivate` pada Bulk Action Bar
11. Verifikasi dialog "Deactivate Tax Depreciation Classes" memuat bullet `• NB-3 – Bukan bangunan – Kelompok 3` dan `• NB-4 – Bukan bangunan – Kelompok 4` saja
12. Verifikasi bullet NB-OLD tidak tampil di dialog dan tidak dihitung
13. Verifikasi kalimat dialog "Are you sure you want to deactivate them?"
14. Klik `[Cancel]` pada dialog
15. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-447: Matriks 1: Bulk Deactivate semua class Active lolos guard

16. Centang checkbox baris NB-3 dan NB-4
17. Klik `Deactivate` pada Bulk Action Bar
18. Klik `[Deactivate]` pada dialog D-01 jamak
19. Verifikasi dialog menutup
20. Verifikasi toggle `Active` baris NB-3 dan NB-4 menjadi Off
21. Verifikasi satu toast "Success, tax depreciation class has been deactivated." tampil
22. Verifikasi Bulk Action Bar hilang
23. Verifikasi seleksi di-reset ke 0 setelah aksi ter-commit
24. Pulihkan NB-3 dan NB-4 ke Active lewat API hingga tersimpan, lalu muat ulang tabel

### TC-FA-TDC-448: Matriks 2: Bulk Deactivate sebagian class dipakai Asset Class

25. Centang checkbox baris NB-3, NB-4, dan NB-2
26. Klik `Deactivate` pada Bulk Action Bar
27. Klik `[Continue]` pada dialog D-14
28. Verifikasi toggle `Active` baris NB-3 dan NB-4 menjadi Off
29. Verifikasi toggle `Active` baris NB-2 tetap On
30. Verifikasi satu toast "Success, tax depreciation class has been deactivated. Some items were skipped (used by asset classes)." tampil
31. Verifikasi Bulk Action Bar hilang
32. Verifikasi seleksi di-reset ke 0

## Notes

- Urutan TC dalam spec: TC-FA-TDC-449, 450, 447, 448. Dialog blok dan screening lebih dulu (S-10); aksi yang mengubah status berjalan sesudahnya.
- Langkah penghubung (S-03, S-09): langkah 8 dan 15 (klik icon `×` agar seleksi TC berikutnya bersih) dan langkah 14 (membatalkan dialog; TC-FA-TDC-450 hanya screening); langkah 24 memulihkan NB-3 dan NB-4 ke Active supaya TC-FA-TDC-448 memenuhi precondition (Active, Used By 0).
- Temuan untuk QA:
  - Post Condition TC-FA-TDC-447 (status tersimpan Inactive; log L-04 per class di tiga surface) dan TC-FA-TDC-448 (log L-04 hanya NB-3 dan NB-4) tidak punya langkah observasi di TC dan tidak diasersi (S-01); log "diperiksa di section 5" ditangani spec pencatatan.
  - TC-FA-TDC-449 Expected b "Tidak ada toast" ditulis sebagai `Verifikasi` tepat sesudah `[OK]` menutup dialog; Post Condition "tidak ada log baru" tidak diasersi (tanpa langkah observasi).
  - TC-FA-TDC-450 Expected b "tidak dihitung" tidak menyebut objek penghitungan; spec mengikuti teks TC.
  - Email akun Total Control tidak tertulis di TC.
  - Class Code maksimal 15 karakter, sehingga suffix `{runId}-<NNN>` (S-12) tidak muat pada kode class milik spec; spec memakai kode literal TC pada dataset company khusus automation yang di-seed dan dipulihkan fixture. Perlu konfirmasi QA.
