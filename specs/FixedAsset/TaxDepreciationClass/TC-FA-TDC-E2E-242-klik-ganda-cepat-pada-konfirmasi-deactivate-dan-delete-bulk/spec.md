---
id: TC-FA-TDC-E2E-242-klik-ganda-cepat-pada-konfirmasi-deactivate-dan-delete-bulk
title: "Klik Ganda Cepat pada Konfirmasi Deactivate dan Delete Bulk"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-488
  - TC-FA-TDC-487
coverage:
  web: automated
---

# Klik Ganda Cepat pada Konfirmasi Deactivate dan Delete Bulk

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data milik spec (disediakan tim FE; class di luar Example Data disediakan lewat seed API): class NB-3 dan NB-4 Active dengan Used By 0 dan Last Posted Tax Year kosong (target bulk Deactivate, TC-FA-TDC-488, lalu bulk Delete, TC-FA-TDC-487; NB-3 dan NB-4 dihapus oleh spec ini). Tabel berisi tidak lebih dari 10 class dalam satu halaman Pagination, sehingga baris target tidak dicari lewat Search. Class Code dibatasi 15 karakter menurut TC sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA); hook `before` menyeed ulang kondisi awal lewat API dan hook `after` menyeed ulang NB-3 dan NB-4 yang dihapus. Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan class lewat API; klik ganda cepat (dua klik berurutan tanpa jeda) pada tombol dialog; pengamatan jumlah request bulk Deactivate dan bulk Delete yang terkirim lewat `Spectra.intercept()` (hanya mengamati dan meneruskan request; endpoint tidak dikarang); kemampuan baca jumlah entri Changelog (Status dan Delete untuk NB-3 dan NB-4; baseline dicatat sebelum aksi dan dibandingkan sesudahnya, 8b.10, S-12).
- State global yang diubah: intercept pengamat jaringan pada sesi browser (dilepas di hook `after` sebagai cadangan); status dan keberadaan NB-3 dan NB-4 (dipulihkan di hook `after`).

## Test Steps

### TC-FA-TDC-488: Klik ganda cepat pada tombol Deactivate dialog bulk hanya memproses satu request

1. Catat baseline jumlah entri Status Changelog dan jumlah entri Delete Changelog untuk class NB-3 dan class NB-4
2. Centang checkbox baris NB-3 dan NB-4
3. Klik `Deactivate` pada Bulk Action Bar
4. Klik ganda cepat `[Deactivate]` pada dialog D-01 jamak
5. Verifikasi tombol `[Deactivate]` non-aktif dengan spinner setelah klik pertama
6. Verifikasi hanya satu request bulk Deactivate yang terkirim
7. Verifikasi satu toast sukses `Success, tax depreciation class has been deactivated.` tampil
8. Klik ikon Changelog di toolbar
9. Verifikasi jumlah entri Status Changelog NB-3 bertambah tepat satu dibanding baseline langkah 1
10. Verifikasi jumlah entri Status Changelog NB-4 bertambah tepat satu dibanding baseline langkah 1
11. Tutup modal Changelog

### TC-FA-TDC-487: Klik ganda cepat pada tombol Delete dialog bulk hanya memproses satu request

12. Centang checkbox baris NB-3 dan NB-4
13. Klik `Delete` pada Bulk Action Bar
14. Klik ganda cepat `[Delete]` pada dialog D-06 jamak
15. Verifikasi tombol `[Delete]` non-aktif dengan spinner setelah klik pertama
16. Verifikasi hanya satu request bulk Delete yang terkirim
17. Verifikasi satu toast sukses `Success, tax depreciation class has been deleted.` tampil
18. Verifikasi toast netral `This tax depreciation class is no longer available.` tidak tampil
19. Klik ikon Changelog di toolbar
20. Verifikasi jumlah entri Delete Changelog NB-3 bertambah tepat satu dibanding baseline langkah 1
21. Verifikasi jumlah entri Delete Changelog NB-4 bertambah tepat satu dibanding baseline langkah 1
22. Tutup modal Changelog

## Notes

- Urutan TC: 488, 487 (aksi yang menghapus data, TC-FA-TDC-487, di akhir). Klik ganda cepat pada konfirmasi single ada di spec 104.
- Langkah penghubung (S-03): langkah 1 (baseline Changelog yang dibandingkan pada langkah 9, 10, 20, dan 21; kelas entri yang dibandingkan berbeda per langkah) serta langkah 11 dan 22 (menutup modal Changelog). Langkah 12 mencentang NB-3 dan NB-4 kembali sesuai langkah 1 TC-FA-TDC-487; spec mengandalkan seleksi yang direset setelah bulk action sukses (lihat Temuan untuk QA).
- Spinner pada langkah 5 dan 15 diasersi lebih dulu daripada hasil lain karena state sementara (8b.5). Absence toast netral pada langkah 18 didahului toast sukses langkah 17 sebagai anchor (8b.2, 8b.11).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC; nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis terpisah; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter, sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal TC dan menyeed ulang lewat hook. Perlu konfirmasi QA.
  - TC-FA-TDC-488 dan TC-FA-TDC-487 Expected a ("Hanya satu request ... terkirim") tidak menyebut cara mengamati jumlah request; spec memakai `Spectra.intercept()` sebagai pengamat tanpa mengarang endpoint (S-13).
  - TC tidak menyebut apakah seleksi dan Bulk Action Bar direset sesudah bulk action sukses; spec mengasumsikan direset sehingga langkah 12 mencentang kembali baris NB-3 dan NB-4. TC-FA-TDC-487 tidak menyebut status NB-3 dan NB-4 saat dihapus; sesudah TC-FA-TDC-488 keduanya Inactive.
