---
id: TC-FA-CAT-E2E-076-bulk-delete-checkbox-header-select-all-retensi-seleksi
title: "Bulk Delete: Checkbox Header, Select All Lintas Halaman, dan Retensi Seleksi saat Pindah Halaman, Search, Filter, dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-242
  - TC-FA-CAT-243
  - TC-FA-CAT-244
coverage:
  web: automated
---

# Bulk Delete: Checkbox Header, Select All Lintas Halaman, dan Retensi Seleksi saat Pindah Halaman, Search, Filter, dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMany (Pre-setup #24), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #24 (CatMany): 30 kategori L1 `Seed Cat 01` sampai `Seed Cat 30`. Spec hanya membaca dan mencentang; tidak ada aksi tulis. Pagination default 10 data per halaman (3 halaman).
- Seed client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-242: Checkbox header, select halaman aktif dan status indeterminate

1. Centang satu baris
2. Verifikasi checkbox header menampilkan status indeterminate (strip minus)
3. Klik checkbox header
4. Verifikasi 10 baris halaman aktif tercentang
5. Verifikasi counter `10 categories selected`
6. Klik checkbox header lagi
7. Verifikasi seluruh baris halaman aktif tidak tercentang
8. Verifikasi bar hilang

### TC-FA-CAT-243: Select All (N records) memilih lintas halaman dan berubah menjadi Unselect All

9. Klik `Select All (30 records)`
10. Pindah ke halaman 2
11. Verifikasi seluruh baris halaman 2 tercentang
12. Pindah ke halaman 3
13. Verifikasi seluruh baris halaman 3 tercentang
14. Verifikasi tombol berubah menjadi `Unselect All`
15. Hapus centang satu baris pada halaman 3
16. Verifikasi tombol kembali menjadi `Select All (29 records)`
17. Klik `Select All (29 records)`
18. Klik `Unselect All` setelah seleksi 100%
19. Verifikasi bar tertutup
20. Pindah ke halaman 1
21. Verifikasi tidak ada baris yang tercentang

### TC-FA-CAT-244: Seleksi bertahan saat pindah halaman, Search, Filter, dan Sort berubah

22. Centang checkbox baris `Seed Cat 01`
23. Pindah ke halaman 2 dan centang `Seed Cat 11`
24. Verifikasi counter `2 categories selected`
25. Ketik Search `Seed Cat 2`, tekan Enter
26. Verifikasi counter `2 categories selected`
27. Klik header `Category` hingga Sort menjadi Descending
28. Verifikasi counter `2 categories selected`
29. Klik `(←)` pada kotak Search
30. Pindah ke halaman 1
31. Verifikasi counter `2 categories selected`
32. Pindah ke halaman 2
33. Verifikasi `Seed Cat 11` tetap tercentang
34. Pindah ke halaman 3
35. Verifikasi `Seed Cat 01` tetap tercentang
36. Klik header `Category` hingga indikator Sort hilang, lalu klik icon (×) pada bar

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok satu kelas (fungsional seleksi Bulk Action), satu dataset read-only, dan berdiri sendiri.
- Langkah penghubung (tanpa `Verifikasi`, S-03/S-09): berpindah halaman, `Select All (29 records)` untuk mencapai seleksi 100%, klik `(←)` pada Search, pemulihan Sort dan pembatalan seleksi di akhir.
- Setelah Sort Descending pada 30 baris dengan 10 per halaman, `Seed Cat 11` berada di halaman 2 dan `Seed Cat 01` di halaman 3 (hasil turunan dari data Pre-setup #24).
- Temuan untuk QA:
  - TC-FA-CAT-243 meminta klik `Unselect All` setelah seleksi 100% tetapi tidak menyebut cara mencapai seleksi 100% sesudah satu centang dihapus; spec menambah klik `Select All (29 records)`.
  - TC-FA-CAT-244 menyebut Filter pada judul tetapi langkah dan Expected tidak memakai Filter; spec tidak menguji Filter.
