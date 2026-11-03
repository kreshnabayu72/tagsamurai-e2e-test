---
id: TC-FA-LBL-E2E-057-volume-bulk-action-bar-select-all-selection-limit-dan-seleksi-lintas-halaman-bagian-1-3
title: "Volume: Bulk Action Bar, Select All, Selection Limit, dan Seleksi Lintas Halaman (bagian 1/3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-178
  - TC-FA-LBL-179
  - TC-FA-LBL-181
  - TC-FA-LBL-182
coverage:
  web: automated
---

# Volume: Bulk Action Bar, Select All, Selection Limit, dan Seleksi Lintas Halaman (bagian 1/3)

## Prerequisites

- Mode: FE+BE. Backend nyata pada Company Volume (Pre-setup #10); tidak ada respons yang di-mock atau di-intercept.
- Akun aktor: Total Control Volume (Pre-setup #10, Company Volume), `Fixture.assetLabeling.akun.totalControlVolume`; email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE. Password `Spectra.env.FA_TC_VOLUME_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. `fixtures/asset-labeling.json` belum ada dan disediakan tim FE.
- Hook suite `before`, `beforeEach`, dan `after` (lihat `suite.md`) berlaku. Hook `after` spec ini mengembalikan sesi ke akun default suite (Total Control Company Alpha) dan memulihkan Selection Limit ke nilai awal.
- Data Pre-setup (hanya dibaca, tidak diubah): Company Volume (#10) dengan 120 label `Project Tag 1` sampai `Project Tag 120` (log Create tersedia). Data Dinamis: tidak ada. Page size awal tabel 10 baris.
- Selection Limit di atas 120, diatur di hook `before` spec ini bila nilai awalnya 120 atau kurang dan dipulihkan di hook `after`. Kemampuan mengubah dan memulihkan System Limits disediakan tim FE (TC, PRD, dan LLD tidak menyebut akun pelaku perubahannya).
- Kelas harness e (volume data, 120 label): spec ini hanya memuat TC volume Company Volume dan tidak memuat TC kelas harness lain.
- State global: Selection Limit di System Limits (lihat butir sebelumnya); suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LBL-178: Screening Bulk Action Bar: 4 elemen dan counter singular/plural

1. Centang satu baris
2. Verifikasi Bulk Action Bar muncul di atas tabel rata kiri dengan urutan: tombol `Bulk Action`, teks counter, tombol `Select All (120 records)`, ikon `×`
3. Verifikasi counter `1 Label selected`
4. Centang baris kedua
5. Verifikasi counter `2 Labels selected`
6. Hapus centang baris kedua
7. Verifikasi counter `1 Label selected`
8. Klik ikon `×`

### TC-FA-LBL-179: Checkbox header: pilih halaman aktif dan status indeterminate

9. Klik checkbox header
10. Verifikasi 10 baris halaman aktif tercentang
11. Verifikasi Checkbox header checked
12. Verifikasi counter `10 Labels selected`
13. Pindah ke halaman 2
14. Verifikasi baris di halaman 2 tidak tercentang
15. Kembali ke halaman 1
16. Hapus centang satu baris
17. Verifikasi Checkbox header indeterminate
18. Verifikasi counter `9 Labels selected`
19. Klik checkbox header sampai seluruh centang hilang
20. Verifikasi seluruh centang hilang
21. Verifikasi Bulk Action Bar hilang

### TC-FA-LBL-182: Ikon × membatalkan seluruh seleksi dan menutup bar

22. Centang dua baris
23. Klik ikon `×`
24. Verifikasi seluruh seleksi dibatalkan dan centang hilang
25. Verifikasi Bulk Action Bar hilang

### TC-FA-LBL-181: Hapus centang satu baris setelah semua terpilih mengembalikan tombol menjadi Select All dengan N-1

26. Centang satu baris
27. Klik `Select All (120 records)`
28. Hapus centang satu baris
29. Verifikasi Bulk Action Bar tetap tampil
30. Verifikasi counter `119 Labels selected`
31. Verifikasi tombol kembali menjadi `Select All (119 records)`
32. Klik ikon `×`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 8 dan langkah penutup TC-FA-LBL-181 membersihkan seleksi (S-09); langkah 15 mengembalikan tabel ke halaman 1 sebelum langkah hapus centang.
- Urutan TC dalam spec: TC-FA-LBL-182 mendahului TC-FA-LBL-181; TC-FA-LBL-181 terakhir karena memakai Select All server dengan Selection Limit di atas 120. TC-FA-LBL-180 (Select All server lintas halaman) ada di spec 058 dan TC-FA-LBL-183 serta TC-FA-LBL-184 (Selection Limit 100) ada di spec 164.
- Temuan untuk QA:
  - TC-FA-LBL-179 langkah 3 ("Klik checkbox header sampai kosong") tidak menyebut jumlah klik dari keadaan indeterminate; spec mengikuti redaksi TC pada langkah 19 dan menjadikan hilangnya seluruh centang sebagai Verifikasi.
  - TC-FA-LBL-179 Expected a ("baris di halaman lain tidak tercentang") tidak punya langkah pindah halaman di Langkah Uji; spec menambahkan pindah ke halaman 2 dan kembali sebagai penghubung.
  - Nilai awal Selection Limit tidak disebut untuk TC-FA-LBL-178, TC-FA-LBL-179, dan TC-FA-LBL-182; spec memakai nilai di atas 120 yang dibutuhkan TC-FA-LBL-181 untuk seluruh spec.
  - Email akun `Total Control Volume` tidak tertulis di Pre-setup #10.
