---
id: TC-FA-TDC-E2E-119-matriks-bulk-deactivate-4b-4c-dan-5-collapse-ke-dialog-single
title: "Matriks Bulk Deactivate 4b 4c dan 5 Collapse ke Dialog Single"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-451
  - TC-FA-TDC-452
  - TC-FA-TDC-453
  - TC-FA-TDC-454
  - TC-FA-TDC-455
sourceRules: ["D-14", "FATDC-LOGIC-14f", "FATDC-LOGIC-14c", "D-02", "FATDC-LOGIC-14g", "D-01", "FATDC-LOGIC-14h", "§[F-FATDC-05] Deactivate Tax Depreciation Class#b3", "FATDC-LOGIC-14k"]
smoke: []
dependsOn: []
trace:
  "D-14": [3, 4, 5]
  "FATDC-LOGIC-14f": [4, 5]
  "FATDC-LOGIC-14c": [6, 13, 34]
  "D-02": [11, 12, 24, 25, 26]
  "FATDC-LOGIC-14g": 12
  "D-01": [18, 19, 31]
  "FATDC-LOGIC-14h": [24, 31]
  "§[F-FATDC-05] Deactivate Tax Depreciation Class#b3": 33
  "FATDC-LOGIC-14k": 35
coverage:
  web: automated
---

# Matriks Bulk Deactivate 4b 4c dan 5 Collapse ke Dialog Single

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding dan pemulihan lewat API, serta flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dataset spec ini, `Fixture.fixedAssetTaxDepreciationClass.dataset119`, di-seed lewat API di hook `before` dan dipulihkan di hook `after`): tabel satu halaman berisi NB-1 (Active, Used By 5), NB-2 (Active, Used By 3), NB-3 dan NB-4 (Active, Used By 0), NB-SL (Active), dan NB-OLD (Inactive). Hanya TC-FA-TDC-454 mengubah data (NB-4 menjadi Inactive; dipulihkan pada langkah 36). Kode class ditulis literal sesuai TC tanpa suffix `{runId}-<NNN>` (S-12): Class Code maksimal 15 karakter sehingga suffix tidak muat (lihat Temuan untuk QA). Data Dinamis: tidak ada.
- Kemampuan teknis: mencentang checkbox baris; memulihkan status NB-4 ke Active lewat API (sesi API aktor sesuai `suite.md`).
- State global yang diubah: status Active NB-4 (dipulihkan pada langkah 36 dan di hook `after`).

## Test Steps

### TC-FA-TDC-451: Matriks 4b: Bulk Deactivate seleksi campuran, subset Active sebagian dipakai

1. Centang checkbox baris NB-3, NB-2, dan NB-OLD
2. Klik `Deactivate` pada Bulk Action Bar
3. Verifikasi dialog berjudul "Deactivate Tax Depreciation Classes"
4. Verifikasi bagian "The following will be deactivated:" berisi `• NB-3 – Bukan bangunan – Kelompok 3`
5. Verifikasi bagian "The following cannot be deactivated and will be skipped:" berisi `• NB-2 – Bukan bangunan – Kelompok 2 — "used by asset classes"`
6. Verifikasi NB-OLD tidak tampil di kedua bagian
7. Klik `[Cancel]` pada dialog
8. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-452: Matriks 4c: Bulk Deactivate seleksi campuran, subset Active semua dipakai

9. Centang checkbox baris NB-1, NB-2, dan NB-OLD
10. Klik `Deactivate` pada Bulk Action Bar
11. Verifikasi dialog berjudul "Cannot Deactivate Tax Depreciation Classes"
12. Verifikasi dialog memuat `• NB-1 – Bukan bangunan – Kelompok 1 — "used by asset classes"` dan `• NB-2 – Bukan bangunan – Kelompok 2 — "used by asset classes"` saja
13. Verifikasi NB-OLD tidak tampil di dialog
14. Klik `[OK]` pada dialog blok
15. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-453: Matriks 5: Bulk Deactivate dari satu baris tercentang memakai dialog single

16. Centang checkbox baris NB-4
17. Klik `Deactivate` pada Bulk Action Bar
18. Verifikasi dialog "Deactivate Tax Depreciation Class" (judul tunggal) tampil dengan satu bullet `• NB-4 – Bukan bangunan – Kelompok 4`
19. Verifikasi kalimat dialog "Are you sure you want to deactivate it?"
20. Klik `[Cancel]` pada dialog
21. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-455: Bulk Deactivate satu-satunya class yang diblokir collapse ke dialog blok single

22. Centang checkbox baris NB-2 dan NB-OLD
23. Klik `Deactivate` pada Bulk Action Bar
24. Verifikasi dialog "Cannot Deactivate Tax Depreciation Class" (judul tunggal) tampil dengan bullet `• NB-2 – Bukan bangunan – Kelompok 2`
25. Verifikasi kalimat dialog "Used by 3 asset classes. Change them in Asset Class first."
26. Verifikasi footer dialog memuat satu tombol `[OK]`
27. Klik `[OK]` pada dialog blok
28. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-454: Matriks 5: Bulk Deactivate tepat satu class lolos dari seleksi campuran collapse ke dialog single

29. Centang checkbox baris NB-4 dan NB-OLD
30. Klik `Deactivate` pada Bulk Action Bar
31. Verifikasi dialog "Deactivate Tax Depreciation Class" (judul tunggal) tampil dengan satu bullet `• NB-4 – Bukan bangunan – Kelompok 4`
32. Klik `[Deactivate]` pada dialog
33. Verifikasi toggle `Active` baris NB-4 menjadi Off
34. Verifikasi toggle `Active` baris NB-OLD tetap Off
35. Verifikasi satu toast "Success, tax depreciation class has been deactivated." tampil
36. Pulihkan NB-4 ke Active lewat API hingga tersimpan

## Notes

- Urutan TC dalam spec: TC-FA-TDC-451, 452, 453, 455, 454. Dialog yang hanya dibuka lebih dulu (S-10); TC-FA-TDC-454 yang mengubah status ada di akhir.
- Langkah penghubung (S-03, S-09): langkah 8, 15, 21 dan 28 (klik icon `×` agar seleksi TC berikutnya bersih), langkah 7 dan 20 (membatalkan dialog yang hanya screening), langkah 14 dan 27 (`[OK]` menutup dialog blok), dan langkah 36 (memulihkan NB-4 ke Active).
- Di atas sekitar 35 langkah (36 langkah): seluruh TC satu topik (matriks Bulk Deactivate 4b, 4c, dan 5, kelas harness `-`); tiap blok berdiri sendiri, dialog dibatalkan atau ditutup sebelum blok berikut, dan satu-satunya blok yang mengubah data ada di akhir.
- Temuan untuk QA:
  - TC-FA-TDC-453 dan 454 sama-sama berlabel "Matriks 5" dan menguji dialog single; keduanya tetap ditulis karena tiap TC tepat satu spec.
  - TC-FA-TDC-455 tidak berlabel Matriks; mengikuti FATDC-LOGIC-14h.
  - Email akun Total Control tidak tertulis di TC.
  - Class Code maksimal 15 karakter, sehingga suffix `{runId}-<NNN>` (S-12) tidak muat pada kode class milik spec; spec memakai kode literal TC pada dataset company khusus automation yang di-seed dan dipulihkan fixture. Perlu konfirmasi QA.
