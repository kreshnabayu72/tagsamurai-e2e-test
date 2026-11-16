---
id: TC-FA-TDC-E2E-121-matriks-bulk-delete-9-sampai-11
title: "Matriks Bulk Delete 9 sampai 11"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-462
  - TC-FA-TDC-463
  - TC-FA-TDC-464
  - TC-FA-TDC-465
  - TC-FA-TDC-466
sourceRules: ["F-FATDC-13.k10", "FATDC-LOGIC-14k", "§3.6#p1", "D-15", "F-FATDC-13.k9", "T-06b", "S-07a", "§3.6#r10", "F-FATDC-13.k8"]
smoke: []
dependsOn: []
trace:
  "F-FATDC-13.k10": [4, 5]
  "FATDC-LOGIC-14k": [6, 28, 36]
  "§3.6#p1": [7, 27, 35]
  "D-15": [11, 12, 17]
  "F-FATDC-13.k9": 18
  "T-06b": 24
  "S-07a": [25, 34]
  "§3.6#r10": 26
  "F-FATDC-13.k8": 33
coverage:
  web: automated
---

# Matriks Bulk Delete 9 sampai 11

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding dan pemulihan lewat API, serta flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dataset spec ini, `Fixture.fixedAssetTaxDepreciationClass.dataset121`, di-seed lewat API di hook `before` dan dipulihkan di hook `after`): tabel satu halaman berisi NB-1 (Last Posted Tax Year 2026, Used By 5), NB-KHS (Last Posted Tax Year 2026, Used By 0), NB-2 (Used By 3, tanpa Last Posted Tax Year), serta NB-3 dan NB-4 (Active, Used By 0, tanpa Last Posted Tax Year). NB-3 dan NB-4 menjadi target hapus (milik dataset spec ini). Kode class ditulis literal sesuai TC tanpa suffix `{runId}-<NNN>` (S-12): Class Code maksimal 15 karakter sehingga suffix tidak muat (lihat Temuan untuk QA). Data Dinamis: tidak ada.
- Kemampuan teknis: mencentang checkbox baris; seeding ulang class NB-3 lewat API di tengah spec (sesi API aktor sesuai `suite.md`).
- State global yang diubah: class NB-3 dan NB-4 terhapus (dipulihkan di hook `after` ke dataset awal).

## Test Steps

### TC-FA-TDC-466: Matriks 11: Bulk Delete semua class terkena Guard 1 dan atau Guard 2 diblokir

1. Centang checkbox baris NB-1, NB-KHS, dan NB-2
2. Klik `Delete` pada Bulk Action Bar
3. Klik `[OK]` pada dialog D-04 jamak
4. Verifikasi baris NB-1, NB-KHS, dan NB-2 tetap ada di tabel
5. Verifikasi tidak ada toast tampil
6. Verifikasi seleksi dipertahankan
7. Verifikasi Bulk Action Bar dipertahankan
8. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-464: Matriks 10b: Bulk Delete sebagian class terkena Guard 1

9. Centang checkbox baris NB-3 dan NB-KHS
10. Klik `Delete` pada Bulk Action Bar
11. Verifikasi dialog D-15 memuat bagian "The following will be deleted:" berisi `• NB-3 – Bukan bangunan – Kelompok 3`
12. Verifikasi bagian "The following cannot be deleted and will be skipped:" berisi `• NB-KHS – Kelompok khusus pernah diposting — "has posted fiscal depreciation"`
13. Klik `[Cancel]` pada dialog
14. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-465: Matriks 10c: Bulk Delete class terkena Guard 1 dan Guard 2 menampilkan anotasi Guard 1

15. Centang checkbox baris NB-3 dan NB-1
16. Klik `Delete` pada Bulk Action Bar
17. Verifikasi dialog D-15 bagian "The following cannot be deleted and will be skipped:" memuat `• NB-1 – Bukan bangunan – Kelompok 1 — "has posted fiscal depreciation"`
18. Verifikasi anotasi "used by asset classes" tidak tampil untuk NB-1
19. Klik `[Cancel]` pada dialog
20. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-463: Matriks 10a: Bulk Delete sebagian class terkena Guard 2

21. Centang checkbox baris NB-3 dan NB-2
22. Klik `Delete` pada Bulk Action Bar
23. Klik `[Continue]` pada dialog D-15
24. Verifikasi satu toast "Success, tax depreciation class has been deleted. Some items were skipped (posted or used by asset classes)." tampil
25. Verifikasi baris NB-3 tidak ada di tabel
26. Verifikasi baris NB-2 tetap ada di tabel
27. Verifikasi Bulk Action Bar hilang
28. Verifikasi seleksi di-reset ke 0
29. Seed ulang class NB-3 (Active, Used By 0, tanpa Last Posted Tax Year) lewat API hingga tersimpan, lalu muat ulang tabel

### TC-FA-TDC-462: Matriks 9: Bulk Delete semua class lolos Guard 1 dan Guard 2

30. Centang checkbox baris NB-3 dan NB-4
31. Klik `Delete` pada Bulk Action Bar
32. Klik `[Delete]` pada dialog D-06 jamak
33. Verifikasi satu toast "Success, tax depreciation class has been deleted." tampil
34. Verifikasi baris NB-3 dan NB-4 tidak ada di tabel
35. Verifikasi Bulk Action Bar hilang
36. Verifikasi seleksi di-reset ke 0

## Notes

- Urutan TC dalam spec: TC-FA-TDC-466, 464, 465, 463, 462. Dialog blok dan screening lebih dulu; aksi hapus di akhir (S-10): TC-FA-TDC-463 menghapus NB-3, lalu NB-3 di-seed ulang sebelum TC-FA-TDC-462.
- Langkah penghubung (S-03, S-09): langkah 8, 14 dan 20 (klik icon `×` agar seleksi TC berikutnya bersih), langkah 13 dan 19 (membatalkan dialog yang hanya screening), dan langkah 29 (seed ulang NB-3 untuk precondition TC-FA-TDC-462).
- Pada TC-FA-TDC-463 dan 462, toast sukses `Verifikasi` lebih dulu dari "baris tidak ada di tabel" karena toast menjadi anchor respons server selesai (8b.2); urutan Expected TC (baris lebih dulu) ditukar.
- Di atas sekitar 35 langkah (36 langkah): satu topik (matriks Bulk Delete 9 sampai 11, kelas harness `-`); seleksi dibersihkan di akhir tiap blok dan blok yang hanya membuka dialog (466, 464, 465) berdiri sendiri. Satu langkah penghubung menyambung blok: langkah 29 (seed ulang NB-3 setelah blok TC-FA-TDC-463 menghapusnya) menjadi precondition blok TC-FA-TDC-462 (langkah 30 sampai 36), sehingga blok 462 bergantung pada langkah 29.
- Temuan untuk QA:
  - Post Condition TC-FA-TDC-462 dan 463 (class terhapus permanen; log L-05 "diperiksa di section 5") dan TC-FA-TDC-466 ("tidak ada log baru") tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - TC-FA-TDC-466 Expected b "Tidak ada toast" diasersi tepat sesudah `[OK]` menutup dialog.
  - Email akun Total Control tidak tertulis di TC.
  - Class Code maksimal 15 karakter, sehingga suffix `{runId}-<NNN>` (S-12) tidak muat pada kode class milik spec; spec memakai kode literal TC pada dataset company khusus automation yang di-seed dan dipulihkan fixture. Perlu konfirmasi QA.
