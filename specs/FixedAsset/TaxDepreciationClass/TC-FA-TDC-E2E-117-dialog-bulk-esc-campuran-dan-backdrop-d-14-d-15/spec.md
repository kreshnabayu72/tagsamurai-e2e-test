---
id: TC-FA-TDC-E2E-117-dialog-bulk-esc-campuran-dan-backdrop-d-14-d-15
title: "Dialog Bulk Esc Campuran dan Backdrop D-14 D-15"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-444
  - TC-FA-TDC-445
  - TC-FA-TDC-446
sourceRules: ["D-14", "FATDC-LOGIC-14k", "§[F-FATDC-05] Deactivate Tax Depreciation Class#b1", "D-15"]
smoke: []
dependsOn: []
trace:
  "D-14": 3
  "FATDC-LOGIC-14k": [6, 7, 19, 20, 21, 22, 29, 30, 34]
  "§[F-FATDC-05] Deactivate Tax Depreciation Class#b1": 11
  "D-15": 26
anchor: [5, 8, 10, 17, 18, 28, 31, 33]
coverage:
  web: automated
---

# Dialog Bulk Esc Campuran dan Backdrop D-14 D-15

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding dan pemulihan lewat API, serta flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dataset spec ini, `Fixture.fixedAssetTaxDepreciationClass.dataset117`, di-seed lewat API di hook `before` dan dipulihkan di hook `after`): tabel satu halaman berisi NB-3 (Active, Used By 0, tanpa Last Posted Tax Year) dan NB-2 (Active, Used By 3). Kode class ditulis literal sesuai TC tanpa suffix `{runId}-<NNN>` (S-12): Class Code maksimal 15 karakter sehingga suffix tidak muat (lihat Temuan untuk QA). Dialog hanya dibuka lalu ditutup dengan `Esc`; tidak ada data yang berubah. Data Dinamis: tidak ada.
- Kemampuan teknis: mengklik area backdrop di luar dialog; menekan `Esc`; Kemampuan baca jumlah entri Changelog (baseline sebelum aksi dan jumlah sesudahnya, S-12) disediakan tim FE/BE; endpoint tidak dikarang (S-13).
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-444: Klik backdrop tidak menutup dialog Deactivate campuran (D-14)

1. Centang checkbox baris NB-3 dan NB-2
2. Klik `Deactivate` pada Bulk Action Bar
3. Verifikasi dialog D-14 terbuka
4. Klik area gelap di luar dialog (backdrop)
5. Verifikasi dialog D-14 tetap terbuka
6. Verifikasi seleksi dipertahankan
7. Verifikasi Bulk Action Bar dipertahankan
8. Verifikasi tidak ada toast tampil
9. Tekan `Esc`
10. Verifikasi dialog menutup
11. Verifikasi toggle `Active` baris NB-3 dan NB-2 tetap On
12. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-445: Tombol Esc menutup dialog Delete campuran

13. Catat baseline jumlah entri Changelog yang memuat class NB-3 dan NB-2 lewat kemampuan baca log
14. Centang checkbox baris NB-3 dan NB-2
15. Klik `Delete` pada Bulk Action Bar
16. Tekan tombol `Esc`
17. Verifikasi dialog menutup
18. Verifikasi tidak ada toast tampil
19. Verifikasi baris NB-3 dan NB-2 tetap ada di tabel
20. Verifikasi seleksi dipertahankan
21. Verifikasi Bulk Action Bar dipertahankan
22. Verifikasi jumlah entri Changelog yang memuat class NB-3 dan NB-2 sama dengan baseline (tidak ada entri log baru)
23. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-446: Klik backdrop tidak menutup dialog Delete campuran (D-15)

24. Centang checkbox baris NB-3 dan NB-2
25. Klik `Delete` pada Bulk Action Bar
26. Verifikasi dialog D-15 terbuka
27. Klik area gelap di luar dialog (backdrop)
28. Verifikasi dialog D-15 tetap terbuka
29. Verifikasi seleksi dipertahankan
30. Verifikasi Bulk Action Bar dipertahankan
31. Verifikasi tidak ada toast tampil
32. Tekan `Esc`
33. Verifikasi dialog menutup
34. Verifikasi baris NB-3 dan NB-2 tetap ada di tabel
35. Klik icon `×` di Bulk Action Bar

## Notes

- Urutan TC dalam spec: TC-FA-TDC-444, 445, 446 (urutan nomor).
- Langkah penghubung (S-03, S-09): langkah 12, 23 dan 35 (klik icon `×` agar seleksi TC berikutnya bersih); TC tidak menyebutnya.
- Klik backdrop lalu `Esc` pada TC-FA-TDC-444 dan 446 mengikuti keputusan NC-19 (dikonfirmasi) di TC: backdrop tidak menutup dialog D-14 dan D-15. Tanda "dialog D-14 terbuka" pada langkah klik `Deactivate` di TC (dan "dialog D-15 terbuka" pada langkah klik `Delete`) ditulis sebagai `Verifikasi` tersendiri sebelum klik backdrop (R-02).
- Klausa "tanpa perubahan data" pada Expected a diasersi lewat `Verifikasi` state toggle atau baris (TC tidak memberi langkah observasi tambahan); klausa "tidak ada entri log baru" diasersi sebagai selisih jumlah entri Changelog terhadap baseline per TC (S-12) lewat kemampuan baca log. Asersi jumlah, bukan absence kelas g (prinsip 13g). Toast diasersi tidak tampil tepat sesudah dialog menutup (8b.11).
- Temuan untuk QA:
  - Kalimat Expected "tidak ada entri log baru" tidak menyebut surface log dan sebagian TC tidak punya langkah observasinya; spec memakai Changelog (surface yang disebut TC-FA-TDC-433 sampai 439) dan membandingkan jumlah entri terhadap baseline (asersi jumlah, bukan absence kelas g; prinsip 13g).
  - TC-FA-TDC-445 tidak punya langkah observasi log; jumlah entri dibaca lewat kemampuan baca log tanpa membuka popup Changelog.
  - Email akun Total Control tidak tertulis di TC.
  - Class Code maksimal 15 karakter, sehingga suffix `{runId}-<NNN>` (S-12) tidak muat pada kode class milik spec; spec memakai kode literal TC pada dataset company khusus automation yang di-seed dan dipulihkan fixture. Perlu konfirmasi QA.
