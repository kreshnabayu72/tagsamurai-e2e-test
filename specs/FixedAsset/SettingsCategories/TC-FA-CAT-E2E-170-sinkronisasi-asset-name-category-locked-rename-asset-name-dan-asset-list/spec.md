---
id: TC-FA-CAT-E2E-170-sinkronisasi-asset-name-category-locked-rename-asset-name-dan-asset-list
title: "Sinkronisasi ke Modul Konsumen: Category Locked di Asset Name, Rename pada Asset Name dan Asset List"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-481
  - TC-FA-CAT-484
  - TC-FA-CAT-572
coverage:
  web: automated
---

# Sinkronisasi ke Modul Konsumen: Category Locked di Asset Name, Rename pada Asset Name dan Asset List

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data milik spec (di-seed hook `before` lewat API; kemampuan seed disediakan tim FE/BE; dibersihkan hook `after`: Asset Name, aset, lalu kategori), nama berakhiran `{runId}-170`, client CatMain:
  - TC-FA-CAT-481: `Furniture Sync {runId}-170` (Code `FS170`, leaf) dengan Asset Name `Office Chair {runId}-170` menunjuknya. `Chairs {runId}-170` (Code `CHR170`) dibuat spec.
  - TC-FA-CAT-484: `Tools Sync {runId}-170` (Code `TS170`, leaf) dengan Asset Name `Drill Set {runId}-170` menunjuknya. Entri Changelog Create `Tools Sync {runId}-170` dari seeding dipakai sebagai entri lama (dipastikan tim FE/BE, lihat Temuan untuk QA).
  - TC-FA-CAT-572: `Tools Asset {runId}-170` (Code `TA170`, leaf) dengan Asset Name `Drill Asset {runId}-170` menunjuknya dan satu aset Active ber-Asset Name itu.
  - Pre-setup #21 dan #22 tidak diubah; target tulis memakai data milik spec (S-06).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): membaca jumlah entri Changelog Asset Name sebelum dan sesudah aksi (baseline; audit trail permanen, bagian 8b butir 10).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-481: Add Subcategory pada leaf yang ditunjuk Asset Name

1. Catat baseline jumlah entri Changelog Asset Name `Office Chair {runId}-170`
2. Klik elipsis (⋯) pada baris `Furniture Sync {runId}-170` > `+ Add Subcategory`
3. Klik `[Add Subcategory]` pada heads-up
4. Isi Category Name `Chairs {runId}-170` dan Code `CHR170`
5. Klik `[Submit]`
6. Tunggu aksi selesai (popup New Subcategory tertutup)
7. Buka Fixed Asset > Settings > Asset Master > Asset Name
8. Ketik Search `Office Chair {runId}-170`, tekan Enter
9. Verifikasi baris `Office Chair {runId}-170` berstatus Category Locked (badge `Needs Update`) pada muat halaman pertama tanpa muat ulang tambahan
10. Verifikasi jumlah entri Changelog Asset Name `Office Chair {runId}-170` sama dengan baseline (Asset Name tidak menulis log akibat transisi itu)

### TC-FA-CAT-484: Rename kategori pada kolom Category Asset Name

11. Klik menu Categories pada Fixed Asset > Settings
12. Klik elipsis (⋯) pada baris `Tools Sync {runId}-170` > `Edit`
13. Ganti isi Category Name dengan `Tools Renamed {runId}-170`
14. Klik `[Save]`
15. Tunggu aksi selesai (popup Edit tertutup)
16. Buka Fixed Asset > Settings > Asset Master > Asset Name
17. Ketik Search `Drill Set {runId}-170`, tekan Enter
18. Verifikasi kolom Category baris `Drill Set {runId}-170` menampilkan `Tools Renamed {runId}-170`
19. Klik menu Categories pada Fixed Asset > Settings
20. Buka Modal Changelog
21. Ketik Search `Tools Sync {runId}-170` pada Modal Changelog, tekan Enter
22. Verifikasi entri Changelog lama menampilkan nama saat itu `Tools Sync {runId}-170`
23. Tutup Modal Changelog

### TC-FA-CAT-572: Rename kategori di Asset List

24. Klik elipsis (⋯) pada baris `Tools Asset {runId}-170` > `Edit`
25. Ganti isi Category Name dengan `Tools Asset Renamed {runId}-170`
26. Klik `[Save]`
27. Tunggu aksi selesai (popup Edit tertutup)
28. Buka Fixed Asset > Asset > Asset List
29. Ketik Search `Drill Asset {runId}-170`, tekan Enter
30. Verifikasi Category aset ber-Asset Name `Drill Asset {runId}-170` menampilkan `Tools Asset Renamed {runId}-170`
31. Buka Filter Category pada Asset List
32. Verifikasi opsi Filter Category memuat `Tools Asset Renamed {runId}-170`
33. Verifikasi opsi Filter Category tidak memuat `Tools Asset {runId}-170`
34. Tutup Filter Category dengan `Esc`

## Notes

- Spec berisi tiga TC pertama dari kelompok sinkronisasi Asset Name; TC-FA-CAT-485, TC-FA-CAT-482, dan TC-FA-CAT-483 ada di spec 200.
- `P-1` (state berat): asersi absence log Asset Name (langkah 10, Expected b TC-FA-CAT-481) tetap di spec ini karena kondisinya bergantung pada transisi Category Locked yang baru dibangun langkah 2 sampai 6 dan seeding Asset Name yang menunjuk leaf; spec absence 168 tidak memuat aksi Add Subcategory pada leaf ber-Asset Name. Langkah 10 memakai baseline (langkah 1) dan anchor langkah 9 (baris Asset Name tampil).
- Langkah penghubung (S-03): langkah 1 (baseline), langkah 6, 15, 27 (menunggu aksi selesai sebelum pindah surface), langkah 8, 17, 29 (Search untuk menemukan baris target), langkah 11 dan 19 (kembali ke Categories), langkah 21 (Search pada Modal Changelog untuk menemukan entri lama), langkah 23 dan 34 (menutup modal dan filter).
- Langkah 9: "tanpa menunggu reload manual lebih lama dari satu kali muat halaman" dipenuhi dengan `Verifikasi` langsung sesudah muat halaman Asset Name pada langkah 7 tanpa muat ulang tambahan.
- Entri Changelog lama pada langkah 22 adalah entri Create dari seeding yang memuat nama `Tools Sync {runId}-170`; entri Edit hasil rename pada langkah 14 tidak dipakai sebagai entri lama.
- Temuan untuk QA:
  - TC-FA-CAT-484 Expected b menyebut entri Changelog lama tetapi langkah TC tidak membuka Changelog; langkah 19 sampai 23 ditambahkan mengikuti Expected dan mengandalkan seeding yang menulis entri Create.
  - TC-FA-CAT-572 berjudul "Asset List dan Reports" tetapi langkah dan Expected hanya Asset List; Reports tidak diasersi.
  - TC-FA-CAT-481 menyebut Code `CHR` tidak ada; spec memakai `CHR170` agar unik. TC-FA-CAT-572 tidak menyebut aset ber-Asset Name `Drill Set`; spec memakai satu aset milik spec yang disediakan tim FE/BE.
  - TC-FA-CAT-481 Expected b ("Asset Name tidak menulis log") tidak menyebut surface log Asset Name; spec memakai Changelog Asset Name.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
