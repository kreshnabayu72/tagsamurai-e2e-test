---
id: TC-FA-CAT-E2E-184-parent-menjadi-excess-saat-popup-subcategory-dan-edit-terbuka
title: "Kategori Menjadi Excess Saat Popup New Subcategory atau Popup Edit Terbuka: Dialog Konflik 409 (CRU Lock)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-168
  - TC-FA-CAT-210
  - TC-FA-CAT-600
coverage:
  web: automated
---

# Kategori Menjadi Excess Saat Popup New Subcategory atau Popup Edit Terbuka: Dialog Konflik 409 (CRU Lock)

## Prerequisites

- Mode: FE+BE (backend nyata; Fallback T-0 dipicu lewat kemampuan T-0 yang disediakan tim FE/BE, tanpa intercept).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPreT0 (Pre-setup #32), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #32 (CatPreT0, Professional dengan downgrade terjadwal ke Starter, T-0 belum tiba, cap plan aktif 100 dan cap plan baru 5, 8 kategori usable `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy` dengan waktu pembuatan terlama ke terbaru dalam urutan itu). Plan baru Starter (cap count 5, cap depth 1) sehingga `Theta Heavy` menjadi Excess saat T-0 tiba.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): memicu Fallback T-0 untuk CatPreT0 (menggeser jam server sehingga plan Starter diterapkan) sebagai pemicu bukan objek uji, memulihkan seed CatPreT0 ke keadaan sebelum T-0 (Pre-setup #32), membaca jumlah entri Changelog kategori sebelum dan sesudah aksi (baseline, S-12). Jam server dan jam browser diatur bersama; jam server dipulihkan bersama seed.
- Data Dinamis: Category Name `Late Child {runId}-184` dan `Cap Child {runId}-184` (ditolak, tidak tersimpan); Description `Late` (ditolak).
- State global yang diubah: jam server dan plan CatPreT0 (T-0). Pemulihan: langkah penghubung memulihkan seed CatPreT0 setelah tiap blok, dan hook `after` memulihkannya bila spec berhenti di tengah.
- Suite berjalan serial (`parallel: false`).
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-168: Add Subcategory di-Submit setelah parent menjadi Excess

1. Catat baseline jumlah entri Changelog kategori (N1)
2. Klik elipsis (⋯) pada baris `Theta Heavy` > `+ Add Subcategory`
3. Isi Category Name `Late Child {runId}-184`
4. Picu Fallback T-0 untuk CatPreT0 hingga `Theta Heavy` berstatus Excess (sesi B: kemampuan T-0, bukan sesi UI)
5. Klik `[Submit]`
6. Verifikasi dialog `This category was changed by someone else. Please review.` dengan tombol `[OK]` tampil (server menolak dengan 409)
7. Verifikasi dialog konflik (CRU Lock) tampil, bukan dialog blok D-01 sampai D-04
8. Klik `[OK]`
9. Verifikasi popup New Subcategory tertutup
10. Verifikasi `Theta Heavy` tampil Excess di tabel
11. Verifikasi `Theta Heavy` tampil Excess di sidebar
12. Verifikasi kategori `Late Child {runId}-184` tidak tersimpan: tidak ada anak di bawah `Theta Heavy`
13. Verifikasi jumlah entri Changelog sama dengan N1 (tidak ada log)
14. Pulihkan seed CatPreT0 ke keadaan sebelum T-0 lalu muat ulang halaman Categories

### TC-FA-CAT-210: Edit pada kategori yang menjadi Excess saat popup terbuka

15. Catat baseline jumlah entri Changelog kategori (N2)
16. Klik elipsis (⋯) pada baris `Theta Heavy` > `Edit`
17. Picu Fallback T-0 untuk CatPreT0 hingga `Theta Heavy` berstatus Excess (sesi B: kemampuan T-0, bukan sesi UI)
18. Ubah Description menjadi `Late`
19. Klik `[Save]`
20. Verifikasi dialog `This category was changed by someone else. Please review.` dengan tombol `[OK]` tampil (server menolak dengan 409)
21. Klik `[OK]`
22. Verifikasi popup Edit tertutup
23. Verifikasi `Theta Heavy` tampil Excess di tabel
24. Verifikasi `Theta Heavy` tampil Excess di sidebar
25. Klik elipsis (⋯) pada baris `Theta Heavy`
26. Verifikasi menu row action tidak memuat aksi `Edit` dan `+ Add Subcategory`
27. Tekan `Esc` untuk menutup menu
28. Verifikasi tidak ada perubahan Description `Late` tersimpan (dibaca dari state BE)
29. Verifikasi jumlah entri Changelog sama dengan N2 (tidak ada log)
30. Pulihkan seed CatPreT0 ke keadaan sebelum T-0 lalu muat ulang halaman Categories

### TC-FA-CAT-600: Parent menjadi Excess saat popup terbuka dan cap count serta depth juga tercapai

31. Catat baseline jumlah entri Changelog kategori (N3)
32. Klik elipsis (⋯) pada baris `Theta Heavy` > `+ Add Subcategory`
33. Isi Category Name `Cap Child {runId}-184`
34. Picu Fallback T-0 untuk CatPreT0: plan Starter diterapkan dan `Theta Heavy` menjadi Excess (jumlah 8 melebihi cap count 5 dan kedalaman `Cap Child` melebihi cap depth 1)
35. Klik `[Submit]`
36. Verifikasi dialog konflik baku `This category was changed by someone else. Please review.` dengan tombol `[OK]` tampil (server menolak dengan 409)
37. Verifikasi dialog bukan dialog blok count, depth, atau batas platform (D-01 sampai D-04)
38. Klik `[OK]`
39. Verifikasi popup New Subcategory tertutup
40. Verifikasi `Theta Heavy` tampil Excess di tabel
41. Verifikasi `Theta Heavy` tampil Excess di sidebar
42. Klik elipsis (⋯) pada baris `Theta Heavy`
43. Verifikasi menu row action tidak memuat aksi `Edit` dan `+ Add Subcategory`
44. Tekan `Esc` untuk menutup menu
45. Verifikasi kategori `Cap Child {runId}-184` tidak tersimpan: tidak ada anak di bawah `Theta Heavy`
46. Verifikasi jumlah entri Changelog sama dengan N3 (tidak ada baris log)
47. Pulihkan seed CatPreT0 ke keadaan sebelum T-0

## Notes

- Tiga blok berdiri sendiri, satu pola (kategori menjadi Excess saat form terbuka, dialog konflik CRU Lock), dan memakai seed CatPreT0 yang dipulihkan antar blok; kegagalan satu blok tidak menghilangkan makna blok lain. Karena itu jumlah langkah (47) melewati sekitar 35.
- Pemicu T-0 (kemampuan jam server) hanya membentuk kondisi uji dan bukan objek uji; tidak ada konteks UI kedua. TC-FA-CAT-528, 529, dan 301 ada di spec 044.
- Langkah penghubung (S-03, S-09): langkah 1, 15, 31 (baseline log, S-12), langkah 8, 21, 38 (menutup dialog hasil penolakan; TC menyebut popup ditutup setelah `[OK]`), langkah 14, 30, 47 (memulihkan seed), langkah 25, 27, 42, 44 (membuka dan menutup menu row action agar absence aksi teramati).
- Verifikasi absence aksi (langkah 26, 43) memakai anchor positif `Theta Heavy` tampil Excess (langkah 24, 41).
- Temuan untuk QA:
  - TC-FA-CAT-168 menulis precondition "T-0 tiba" sedangkan langkah 2 memicu T-0 (ambigu); spec mengikuti langkah (T-0 dipicu setelah popup terbuka) dan memakai seed sebelum T-0 (Pre-setup #32) seperti TC-FA-CAT-600.
  - TC-FA-CAT-168 dan 210 menyebut pemicu "Fallback T-0 atau Wizard Submit sesi B"; spec memakai Fallback T-0 saja (kemampuan T-0, bukan sesi UI kedua).
  - TC-FA-CAT-168, 210, 600 menyebut "dua sesi" padahal sesi B hanya memicu state.
  - Expected "tidak ada log" ketiga TC tidak menyebut surface log; spec memeriksa Changelog saja.
- Spec melewati 35 langkah (47 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri; nomor cadangan slice habis sehingga tidak dipecah lebih jauh.
