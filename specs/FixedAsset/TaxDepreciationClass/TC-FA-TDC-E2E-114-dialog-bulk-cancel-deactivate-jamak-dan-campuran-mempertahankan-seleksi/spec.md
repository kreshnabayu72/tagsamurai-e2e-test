---
id: TC-FA-TDC-E2E-114-dialog-bulk-cancel-deactivate-jamak-dan-campuran-mempertahankan-seleksi
title: "Dialog Bulk Cancel Deactivate Jamak dan Campuran Mempertahankan Seleksi"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-433
  - TC-FA-TDC-434
sourceRules: ["FATDC-LOGIC-14k", "FATDC-LOGIC-08h", "§3.6#p1", "§4.1#r7", "L-04"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-14k": [6, 9, 20, 23]
  "FATDC-LOGIC-08h": [7, 21]
  "§3.6#p1": [8, 22]
  "§4.1#r7": [11, 25]
  "L-04": [12, 26]
anchor: [5, 19]
coverage:
  web: automated
---

# Dialog Bulk Cancel Deactivate Jamak dan Campuran Mempertahankan Seleksi

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding dan pemulihan lewat API, serta flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dataset spec ini, `Fixture.fixedAssetTaxDepreciationClass.dataset114`, di-seed lewat API di hook `before` dan dipulihkan di hook `after`): tabel satu halaman berisi NB-3 dan NB-4 (Active, Used By 0) dan NB-2 (Active, Used By 3). Kode class ditulis literal sesuai TC tanpa suffix `{runId}-<NNN>` (S-12): Class Code maksimal 15 karakter sehingga suffix tidak muat (lihat Temuan untuk QA). Dialog hanya dibuka lalu dibatalkan; tidak ada data yang berubah. Data Dinamis: tidak ada.
- Kemampuan teknis: Kemampuan baca jumlah entri Changelog (baseline sebelum aksi dan jumlah sesudahnya, S-12) disediakan tim FE/BE; endpoint tidak dikarang (S-13).
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-433: Cancel pada dialog Deactivate jamak mempertahankan seleksi

1. Catat baseline jumlah entri Changelog yang memuat class NB-3 dan NB-4 lewat kemampuan baca log
2. Centang checkbox baris NB-3 dan NB-4
3. Klik `Deactivate` pada Bulk Action Bar
4. Klik `[Cancel]` pada dialog
5. Verifikasi dialog menutup
6. Verifikasi tidak ada toast tampil
7. Verifikasi toggle `Active` baris NB-3 dan NB-4 tetap On
8. Verifikasi Bulk Action Bar tetap tampil
9. Verifikasi seleksi sebelumnya dipertahankan (counter `2 class selected`)
10. Klik ikon Changelog di toolbar
11. Verifikasi popup Changelog tampil
12. Verifikasi jumlah entri Changelog yang memuat class NB-3 dan NB-4 sama dengan baseline (tidak ada entri baru)
13. Tutup popup Changelog
14. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-434: Cancel pada dialog Deactivate campuran mempertahankan seleksi

15. Catat baseline jumlah entri Changelog yang memuat class NB-3 dan NB-2 lewat kemampuan baca log
16. Centang checkbox baris NB-3 dan NB-2
17. Klik `Deactivate` pada Bulk Action Bar
18. Klik `[Cancel]` pada dialog
19. Verifikasi dialog menutup
20. Verifikasi tidak ada toast tampil
21. Verifikasi toggle `Active` baris NB-3 dan NB-2 tetap On
22. Verifikasi Bulk Action Bar tetap tampil
23. Verifikasi seleksi sebelumnya dipertahankan (counter `2 class selected`)
24. Klik ikon Changelog di toolbar
25. Verifikasi popup Changelog tampil
26. Verifikasi jumlah entri Changelog yang memuat class NB-3 dan NB-2 sama dengan baseline (tidak ada entri baru)
27. Tutup popup Changelog
28. Klik icon `×` di Bulk Action Bar

## Notes

- Urutan TC dalam spec: TC-FA-TDC-433, 434 (urutan nomor).
- Langkah penghubung (S-03, S-09): langkah 14 dan 28 (klik icon `×` agar seleksi TC berikutnya bersih) dan langkah `Tutup popup Changelog` (TC tidak menyebutnya).
- Klausa "tanpa perubahan data" pada Expected a diasersi lewat `Verifikasi` state toggle atau baris pada Expected b; klausa "Changelog tidak memuat entri baru untuk baris terpilih" diasersi sebagai selisih jumlah entri terhadap baseline per TC (S-12), dengan popup Changelog tampil sebagai anchor (8b.2). Asersi jumlah, bukan absence kelas g (prinsip 13g). Toast diasersi tidak tampil tepat sesudah dialog menutup (8b.11).
- Temuan untuk QA:
  - Kalimat Expected "tidak ada entri log baru" tidak menyebut surface log dan sebagian TC tidak punya langkah observasinya; spec memakai Changelog (surface yang disebut TC-FA-TDC-433 sampai 439) dan membandingkan jumlah entri terhadap baseline (asersi jumlah, bukan absence kelas g; prinsip 13g).
  - TC-FA-TDC-433 dan 434 tidak menyebut cara menutup popup Changelog; spec menambah `Tutup popup Changelog` sebagai langkah penghubung.
  - Email akun Total Control tidak tertulis di TC.
  - Class Code maksimal 15 karakter, sehingga suffix `{runId}-<NNN>` (S-12) tidak muat pada kode class milik spec; spec memakai kode literal TC pada dataset company khusus automation yang di-seed dan dipulihkan fixture. Perlu konfirmasi QA.
