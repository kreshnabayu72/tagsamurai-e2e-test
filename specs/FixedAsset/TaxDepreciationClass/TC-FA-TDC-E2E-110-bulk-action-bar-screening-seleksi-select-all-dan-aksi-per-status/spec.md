---
id: TC-FA-TDC-E2E-110-bulk-action-bar-screening-seleksi-select-all-dan-aksi-per-status
title: "Bulk Action Bar Screening Seleksi Select All dan Aksi per Status"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-413
  - TC-FA-TDC-414
  - TC-FA-TDC-415
  - TC-FA-TDC-416
  - TC-FA-TDC-417
  - TC-FA-TDC-418
  - TC-FA-TDC-419
coverage:
  web: automated
---

# Bulk Action Bar Screening Seleksi Select All dan Aksi per Status

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding dan pemulihan lewat API, serta flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dataset spec ini, `Fixture.fixedAssetTaxDepreciationClass.dataset110`, di-seed lewat API di hook `before` dan dipulihkan di hook `after`; nama kunci ditetapkan tim FE): TC-FA-TDC-413 sampai 417 memakai tabel 10 class dalam satu halaman: NB-3 dan NB-4 berstatus Active, NB-OLD dan NB-OLD2 berstatus Inactive, ditambah NB-1, NB-2, NB-SL, BLD-P, dan BLD-NP berstatus Active (N pada `Select All ([N] records)` = 10 dari seeding). TC-FA-TDC-418 dan 419 memakai tabel 25 class dengan 10 baris per halaman: dataset yang sama ditambah 15 class yang di-seed lewat API pada langkah 25 (N = 25). Kode class ditulis literal sesuai TC tanpa suffix `{runId}-<NNN>` (S-12): Class Code maksimal 15 karakter sehingga suffix tidak muat (lihat Temuan untuk QA). Data Dinamis: tidak ada.
- Kemampuan teknis: seeding class tambahan lewat API di tengah spec; mencentang checkbox baris dan header; membaca counter dan tombol Bulk Action Bar; berpindah halaman Pagination.
- State global yang diubah: jumlah class pada dataset (dipulihkan hook `after` ke dataset awal). Tidak ada state global lain.

## Test Steps

### TC-FA-TDC-413: Screening Bulk Action Bar setelah dua baris dicentang

1. Centang checkbox baris NB-3
2. Centang checkbox baris NB-4
3. Verifikasi Bulk Action Bar tampil di sisi kiri toolbar
4. Verifikasi counter Bulk Action Bar bernilai `2 class selected`
5. Verifikasi Bulk Action Bar memuat tombol aksi `Deactivate` dan `Delete`
6. Verifikasi tombol `Select All ([N] records)` tampil dengan [N] sama dengan total baris tabel (N = 10 dari seeding)
7. Verifikasi icon `×` (clear selection) tampil di ujung kanan bar
8. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-414: Bulk Action Bar hilang saat tidak ada baris tercentang

9. Centang checkbox baris NB-3
10. Hapus centang checkbox baris NB-3
11. Verifikasi Bulk Action Bar hilang
12. Verifikasi toolbar kembali menampilkan Search, Filter, Download, Changelog, dan `+ Class`
13. Verifikasi checkbox header kolom berstatus unchecked

### TC-FA-TDC-415: Aksi Bulk Action Bar untuk seleksi hanya class Active

14. Centang checkbox baris NB-3 dan NB-4
15. Verifikasi Bulk Action Bar memuat `Deactivate` dan `Delete`
16. Verifikasi Bulk Action Bar tidak memuat `Activate`
17. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-416: Aksi Bulk Action Bar untuk seleksi hanya class Inactive

18. Centang checkbox baris NB-OLD dan NB-OLD2
19. Verifikasi Bulk Action Bar memuat `Activate` dan `Delete`
20. Verifikasi Bulk Action Bar tidak memuat `Deactivate`
21. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-417: Aksi Bulk Action Bar untuk seleksi campuran Active dan Inactive

22. Centang checkbox baris NB-4 dan NB-OLD
23. Verifikasi Bulk Action Bar memuat `Deactivate`, `Activate`, dan `Delete`
24. Klik icon `×` di Bulk Action Bar
25. Tambahkan 15 class lewat API sehingga tabel memuat 25 class, lalu muat ulang tabel

### TC-FA-TDC-418: Checkbox header hanya memilih baris pada halaman aktif

26. Centang checkbox header kolom pada halaman 1
27. Verifikasi 10 baris halaman 1 tercentang
28. Verifikasi Bulk Action Bar menampilkan counter bernilai 10
29. Pindah ke halaman 2
30. Verifikasi pada halaman 2 tidak ada baris yang tercentang
31. Verifikasi seleksi 10 baris dari halaman 1 tetap dipertahankan (counter tetap 10)
32. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-419: Select All lintas halaman lalu berubah menjadi Unselect All

33. Centang checkbox satu baris agar Bulk Action Bar tampil
34. Klik `Select All (25 records)` pada Bulk Action Bar
35. Verifikasi seluruh 25 baris terpilih lintas halaman
36. Verifikasi counter bernilai 25
37. Verifikasi tombol berubah menjadi `Unselect All (25 records)`
38. Klik `Unselect All (25 records)`

## Notes

- Urutan TC dalam spec: TC-FA-TDC-413, 414, 415, 416, 417, 418, 419. Blok 413 sampai 417 berjalan di tabel satu halaman sehingga baris target tampil tanpa Search (8b.13); blok 418 dan 419 butuh 25 class.
- Langkah penghubung (S-03, S-09): langkah 8, 17, 21, 24 dan 32 (klik icon `×` agar seleksi blok berikutnya bersih; TC tidak menyebutnya); langkah 25 (seeding 15 class lewat API dan muat ulang tabel; TC-FA-TDC-418 dan 419 mensyaratkan 25 class); langkah 33 (mencentang satu baris agar Bulk Action Bar tampil, karena bar hilang bila tidak ada baris tercentang dan `Select All` hanya tersedia di bar; langkah 1 TC-FA-TDC-419 tidak menyebut cara bar muncul); langkah terakhir (`Unselect All`) membersihkan seleksi TC-FA-TDC-419.
- Di atas sekitar 35 langkah (38 langkah): satu topik (Bulk Action Bar tabel utama, kelas harness `-`, tanpa aksi yang mengubah data); seleksi dibersihkan di akhir tiap blok (langkah 8, 17, 21, 24, 32, 38). Blok 413 sampai 417 berdiri sendiri pada tabel 10 baris. Langkah 25 (seeding 15 class lewat API) menyambung ke blok 418 dan 419: keduanya bergantung pada tabel 25 class dari langkah 25 (`Select All (25 records)` pada langkah 34), sehingga kegagalan langkah 25 menggugurkan kedua blok itu, tetapi tidak blok 413 sampai 417.
- Temuan untuk QA:
  - TC-FA-TDC-413 menyebut `[N]` tanpa nilai; N diturunkan dari seeding (10 pada blok pertama, 25 pada TC-FA-TDC-418 dan 419).
  - TC-FA-TDC-419 langkah 1 (`Select All`) tidak menyebut cara memunculkan Bulk Action Bar; spec mencentang satu baris lebih dulu (langkah 33). Pola sama dengan TC-FA-TDC-420, 421 (spec 111), 459 (spec 120), 905 dan 907 (spec 122).
  - Email akun Total Control tidak tertulis di TC.
  - Class Code maksimal 15 karakter, sehingga suffix `{runId}-<NNN>` (S-12) tidak muat pada kode class milik spec; spec memakai kode literal TC pada dataset company khusus automation yang di-seed dan dipulihkan fixture. Perlu konfirmasi QA.
