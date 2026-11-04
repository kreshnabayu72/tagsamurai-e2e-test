---
id: TC-FA-TDC-E2E-116-dialog-bulk-esc-deactivate-activate-dan-delete-jamak
title: "Dialog Bulk Esc Deactivate Activate dan Delete Jamak"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-441
  - TC-FA-TDC-442
  - TC-FA-TDC-443
coverage:
  web: automated
---

# Dialog Bulk Esc Deactivate Activate dan Delete Jamak

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding dan pemulihan lewat API, serta flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dataset spec ini, `Fixture.fixedAssetTaxDepreciationClass.dataset116`, di-seed lewat API di hook `before` dan dipulihkan di hook `after`): tabel satu halaman berisi NB-OLD dan NB-OLD2 (Inactive), NB-3 dan NB-4 (Active, Used By 0), dan NB-2 (Active, Used By 3). Kode class ditulis literal sesuai TC tanpa suffix `{runId}-<NNN>` (S-12): Class Code maksimal 15 karakter sehingga suffix tidak muat (lihat Temuan untuk QA). Dialog hanya dibuka lalu ditutup dengan `Esc`; tidak ada data yang berubah. Data Dinamis: tidak ada.
- Kemampuan teknis: menekan `Esc`; Kemampuan baca jumlah entri Changelog (baseline sebelum aksi dan jumlah sesudahnya, S-12) disediakan tim FE/BE; endpoint tidak dikarang (S-13).
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-441: Tombol Esc menutup dialog Activate jamak

1. Catat baseline jumlah entri Changelog yang memuat class NB-OLD dan NB-OLD2 lewat kemampuan baca log
2. Centang checkbox baris NB-OLD dan NB-OLD2
3. Klik `Activate` pada Bulk Action Bar
4. Tekan tombol `Esc`
5. Verifikasi dialog menutup
6. Verifikasi tidak ada toast tampil
7. Verifikasi toggle `Active` baris NB-OLD dan NB-OLD2 tetap Off
8. Verifikasi seleksi dipertahankan
9. Verifikasi Bulk Action Bar dipertahankan
10. Verifikasi jumlah entri Changelog yang memuat class NB-OLD dan NB-OLD2 sama dengan baseline (tidak ada entri log baru)
11. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-442: Tombol Esc menutup dialog Delete jamak

12. Catat baseline jumlah entri Changelog yang memuat class NB-3 dan NB-4 lewat kemampuan baca log
13. Centang checkbox baris NB-3 dan NB-4
14. Klik `Delete` pada Bulk Action Bar
15. Tekan tombol `Esc`
16. Verifikasi dialog menutup
17. Verifikasi tidak ada toast tampil
18. Verifikasi baris NB-3 dan NB-4 tetap ada di tabel
19. Verifikasi seleksi dipertahankan
20. Verifikasi Bulk Action Bar dipertahankan
21. Verifikasi jumlah entri Changelog yang memuat class NB-3 dan NB-4 sama dengan baseline (tidak ada entri log baru)
22. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-443: Tombol Esc menutup dialog Deactivate campuran

23. Catat baseline jumlah entri Changelog yang memuat class NB-3 dan NB-2 lewat kemampuan baca log
24. Centang checkbox baris NB-3 dan NB-2
25. Klik `Deactivate` pada Bulk Action Bar
26. Tekan tombol `Esc`
27. Verifikasi dialog menutup
28. Verifikasi tidak ada toast tampil
29. Verifikasi toggle `Active` baris NB-3 dan NB-2 tetap On
30. Verifikasi seleksi dipertahankan
31. Verifikasi Bulk Action Bar dipertahankan
32. Verifikasi jumlah entri Changelog yang memuat class NB-3 dan NB-2 sama dengan baseline (tidak ada entri log baru)
33. Klik icon `×` di Bulk Action Bar

## Notes

- Urutan TC dalam spec: TC-FA-TDC-441, 442, 443 (urutan nomor).
- Langkah penghubung (S-03, S-09): langkah 11, 22 dan 33 (klik icon `×` agar seleksi TC berikutnya bersih); TC tidak menyebutnya.
- Klausa "tanpa perubahan data" pada Expected a diasersi lewat `Verifikasi` state toggle atau baris (TC tidak memberi langkah observasi tambahan); klausa "tidak ada entri log baru" diasersi sebagai selisih jumlah entri Changelog terhadap baseline per TC (S-12) lewat kemampuan baca log. Asersi jumlah, bukan absence kelas g (prinsip 13g). Toast diasersi tidak tampil tepat sesudah dialog menutup (8b.11).
- Temuan untuk QA:
  - Kalimat Expected "tidak ada entri log baru" tidak menyebut surface log dan sebagian TC tidak punya langkah observasinya; spec memakai Changelog (surface yang disebut TC-FA-TDC-433 sampai 439) dan membandingkan jumlah entri terhadap baseline (asersi jumlah, bukan absence kelas g; prinsip 13g).
  - TC-FA-TDC-441 sampai 443 tidak punya langkah observasi log; jumlah entri dibaca lewat kemampuan baca log tanpa membuka popup Changelog.
  - Email akun Total Control tidak tertulis di TC.
  - Class Code maksimal 15 karakter, sehingga suffix `{runId}-<NNN>` (S-12) tidak muat pada kode class milik spec; spec memakai kode literal TC pada dataset company khusus automation yang di-seed dan dipulihkan fixture. Perlu konfirmasi QA.
