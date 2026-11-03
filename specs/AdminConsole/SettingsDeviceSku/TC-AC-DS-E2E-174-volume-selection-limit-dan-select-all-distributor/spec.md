---
id: TC-AC-DS-E2E-174-volume-selection-limit-dan-select-all-distributor
title: "Volume Data: Selection Limit 100, Select All Melebihi Limit, dan Basis Hitung SKU Milik Distributor"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-82
  - TC-AC-DS-277
  - TC-AC-DS-278
  - TC-AC-DS-279
  - TC-AC-DS-595
coverage:
  web: automated
---

# Volume Data: Selection Limit 100, Select All Melebihi Limit, dan Basis Hitung SKU Milik Distributor

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah 26): Total Control Distributor PT Cakra Distribusi, Local Registration aktif (Dewi Lestari, Modified By `Dewi L`): `totalControlDist_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_DIST_PASSWORD` (Pre-setup #10).
- Data Pre-setup: SKU inti dan seed (#29, #30; total 129 SKU Principal), SKU Distributor (#31), Selection Limit (#36), modul stok (#39), seed 102 SKU Distributor `CAK-SEED-001` sampai `CAK-SEED-102` (#43, total 105 SKU milik Distributor; fixture BE disiapkan sebelum blok TC 595 dan dihapus di `after`).
- Data Dinamis: tidak ada.
- State global (`P-4`): Selection Limit entitas uji pada Plans & Licensing > Lifecycle Settings > System Limits diatur 100 (nilai awal 1000) lewat kemampuan fixture BE yang disediakan tim FE/BE; pada blok TC 279 diubah 120 oleh pelaku kedua (kemampuan atau akun disediakan tim FE) dan dikembalikan 100; dipulihkan ke 1000 di hook `after`. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-277: Seleksi manual ke-limit tambah satu diblok live dengan checkbox disabled dan tooltip

1. Pastikan Selection Limit bernilai 100 pada System Limits
2. Ubah jumlah data per halaman menjadi 100
3. Klik checkbox header
4. Verifikasi counter "100 SKUs selected" setelah checkbox header
5. Pindah ke halaman 2
6. Coba centang satu baris pada halaman 2
7. Verifikasi checkbox baris ke-101 (halaman 2) disabled dan tidak dapat dicentang
8. Arahkan kursor ke checkbox baris ke-101
9. Verifikasi tooltip "You've reached the maximum selection of 100 rows." tampil
10. Pindah ke halaman 1
11. Verifikasi baris ke-1 sampai ke-100 tetap tercentang
12. Verifikasi bar bulk tetap aktif
13. Klik `Unselect All`

### TC-AC-DS-278: Select All melebihi Selection Limit memotong seleksi ke limit dan menampilkan toast error

14. Ubah jumlah data per halaman menjadi 10, lalu klik tombol "Select All (129 records)"
15. Verifikasi muncul toast error: "Error, only the first 100 of 129 rows were selected. Narrow your filter to include the rest."
16. Tunggu 5 detik tanpa menutup toast
17. Verifikasi toast bertahan sampai ditutup manual
18. Verifikasi bar bulk tampil dengan counter "100 SKUs selected"
19. Verifikasi bar bulk dapat dipakai untuk 100 baris pertama
20. Tutup toast lalu klik `Unselect All`

### TC-AC-DS-279: Perubahan nilai Selection Limit di System Limits diikuti tanpa muat ulang

21. Dengan sesi kedua (pelaku perubahan System Limits) ubah Selection Limit menjadi 120 pada Plans & Licensing > Lifecycle Settings > System Limits hingga tersimpan
22. Kembali ke sesi pertama tanpa memuat ulang halaman, lalu klik "Select All (129 records)"
23. Verifikasi toast error: "Error, only the first 120 of 129 rows were selected. Narrow your filter to include the rest."
24. Verifikasi counter "120 SKUs selected" mengikuti nilai terbaru
25. Tutup toast, klik `Unselect All`, lalu kembalikan Selection Limit menjadi 100 lewat sesi kedua

### TC-AC-DS-82: Select All lintas halaman bagi Distributor hanya mencakup SKU milik Distributor

26. Logout lalu login sebagai Total Control Distributor PT Cakra Distribusi (`totalControlDist_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_DIST_PASSWORD`) dan buka halaman `Settings > Device > Device SKU`; siapkan Distributor dengan tepat 3 SKU milik sendiri (`LOC-NOR-01`, `LOC-NOR-02`, `LOC-NOR-03`) lewat fixture BE
27. Verifikasi tombol bertuliskan "Select All (3 records)" (jumlah baris milik Distributor, bukan 132)
28. Klik tombol "Select All (3 records)"
29. Verifikasi hanya `LOC-NOR-01`, `LOC-NOR-02`, dan `LOC-NOR-03` terpilih
30. Verifikasi tombol berubah menjadi "Unselect All"
31. Verifikasi tidak ada baris SKU Principal yang terpilih pada halaman manapun
32. Klik `Unselect All`

### TC-AC-DS-595: Select All oleh Distributor melebihi Selection Limit menghitung hanya SKU milik sendiri

33. Pastikan Selection Limit bernilai 100 pada System Limits dan seed 102 SKU Distributor `CAK-SEED-001` sampai `CAK-SEED-102` tersedia
34. Verifikasi tombol bertuliskan "Select All (105 records)" (jumlah SKU milik Distributor, bukan jumlah SKU Principal ditambah SKU milik sendiri)
35. Klik tombol "Select All (105 records)"
36. Verifikasi muncul toast error: "Error, only the first 100 of 105 rows were selected. Narrow your filter to include the rest."
37. Verifikasi bar bulk menampilkan counter "100 SKUs selected"
38. Verifikasi tidak ada baris SKU Principal yang terpilih
39. Tutup toast dan klik `Unselect All`

## Notes

- `P-4`: TC 277, 278, 279, dan 595 berbagi state global Selection Limit (System Limits) yang diubah berurutan; state awal tiap bagian ditulis di Prerequisites dan dipulihkan di hook `after`.
- Langkah penghubung tanpa `Verifikasi`: langkah 14 (ukuran halaman) dan langkah 26 (ganti akun eksplisit; sesi dikembalikan ke akun default suite di hook `after`), langkah 25 (mengembalikan limit 100), `Unselect All` agar seleksi tidak terbawa (S-09), dan langkah 33 (memastikan state).
- Spec berada di atas sekitar 35 langkah (39 langkah); alasan: semua blok satu kelas harness (e, Selection Limit) dan berdiri sendiri, kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC 82 langkah 2 menyebut klik tombol "Select All (3 records)" tanpa memilih satu baris dulu; bergantung pada kemunculan tombol itu di toolbar. TC 82 Precondition tidak menyebut Distributor hanya 3 SKU sendiri sedangkan TC 595 membutuhkan 105; spec menyiapkan keadaan berbeda lewat fixture BE per blok. TC 277 butir b mengacu "baris ke-101" pada halaman 2 dengan ukuran halaman 100; tooltip diverifikasi lewat hover. TC 278 dan 279 memakai total 129 SKU Pre-setup.
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
