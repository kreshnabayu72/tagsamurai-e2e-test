---
id: TC-FA-CAT-E2E-051-edit-validasi-category-name
title: "Edit Category: Validasi Category Name (Kosong, Spasi, Batas 120 Karakter, Trim)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-177
  - TC-FA-CAT-178
  - TC-FA-CAT-179
  - TC-FA-CAT-180
  - TC-FA-CAT-538
  - TC-FA-CAT-531
coverage:
  web: automated
---

# Edit Category: Validasi Category Name (Kosong, Spasi, Batas 120 Karakter, Trim)

## Prerequisites

- Mode: FE+BE (backend nyata; nilai tersimpan diasersi lewat tabel, Changelog, dan pembacaan state BE).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data milik spec (seed lewat API di hook `before`, disediakan tim FE/BE): kategori L1 leaf `Furniture {runId}-051` (Code `FURN051`, Total Asset 0) menjadi target Edit (S-06). Blok TC-FA-CAT-179, 180, dan 531 menyimpan perubahan Category Name (`NamaE120`, `Furniture Trim {runId}-051`, `NamaE120`). `NamaE120` tepat 120 karakter dan unik per run (S-12): `E` sebanyak (120 dikurangi panjang `-{runId}-051`) diikuti `-{runId}-051`. Pemulihan `Furniture {runId}-051` (Name, Code, Description) ke nilai seed lewat API dijalankan sebagai langkah penghubung sesudah tiap blok yang menyimpan; hook `after` menghapus kategori itu. Hook `before` juga membersihkan kategori ber-Code literal `FURN051` yang tersisa dari run sebelumnya sebelum seed. Data Pre-setup #20 tidak diubah. Efek: entri Changelog CatMain bertambah (audit trail permanen; hanya selisih terhadap baseline yang diasersi); suite berjalan serial.
- Flag Guided Tooltip halaman Categories: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Kemampuan teknis: membaca jumlah entri Changelog kategori sebelum dan sesudah aksi (baseline, S-12) dan membaca state BE kategori `Furniture {runId}-051`; disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`).
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-177: Category Name dikosongkan ditolak setelah Save

1. Klik elipsis (⋯) pada baris `Furniture {runId}-051` > `Edit`
2. Kosongkan Category Name
3. Klik `[Save]`
4. Verifikasi error inline `Category name must not be empty` tampil setelah `[Save]`
5. Verifikasi popup tetap terbuka
6. Verifikasi nilai tersimpan `Furniture {runId}-051` tidak berubah (dibaca dari state BE)

### TC-FA-CAT-178: Category Name hanya spasi ditolak sebagai kosong

7. Isi Category Name dengan `Furniture {runId}-051` untuk menghapus error inline sebelumnya
8. Isi Category Name dengan 5 spasi
9. Klik `[Save]`
10. Verifikasi error inline `Category name must not be empty` tampil
11. Verifikasi tidak ada perubahan tersimpan (dibaca dari state BE)

### TC-FA-CAT-179: Category Name tepat 120 karakter diterima

12. Isi Category Name dengan `NamaE120`
13. Klik `[Save]`
14. Verifikasi toast `Success, category has been updated.` tampil
15. Pulihkan `Furniture {runId}-051` ke nilai seed lewat API dan muat ulang halaman Categories

### TC-FA-CAT-180: Category Name disimpan ter-trim

16. Catat baseline jumlah entri Changelog kategori (N1)
17. Klik elipsis (⋯) pada baris `Furniture {runId}-051` > `Edit`
18. Isi Category Name `  Furniture Trim {runId}-051  ` (dua spasi di awal dan akhir)
19. Klik `[Save]`
20. Verifikasi nilai tersimpan `Furniture Trim {runId}-051` tanpa spasi tepi
21. Klik icon Changelog di Table Tools
22. Verifikasi jumlah entri Changelog bertambah satu dari N1 dan entri baru mencatat New Value `Furniture Trim {runId}-051`
23. Tutup modal Changelog
24. Pulihkan `Furniture {runId}-051` ke nilai seed lewat API dan muat ulang halaman Categories

### TC-FA-CAT-538: Category Name 121 karakter menampilkan error langsung

25. Klik elipsis (⋯) pada baris `Furniture {runId}-051` > `Edit`
26. Isi Category Name dengan 121 karakter `E`
27. Verifikasi border field `severity="danger"` tampil langsung saat melebihi batas
28. Verifikasi pesan `Max. 120 characters` tampil langsung saat melebihi batas
29. Verifikasi seluruh 121 karakter tetap tertulis di field (ketikan tidak dipotong)
30. Klik `[Save]`
31. Verifikasi Save diblok: popup tetap terbuka
32. Verifikasi nilai tersimpan `Furniture {runId}-051` tidak berubah (dibaca dari state BE)

### TC-FA-CAT-531: Panjang Category Name dihitung setelah trim

33. Isi Category Name dengan `NamaE120` diikuti 5 spasi di akhir
34. Klik `[Save]`
35. Verifikasi pesan `Max. 120 characters` tidak tampil
36. Verifikasi toast `Success, category has been updated.` tampil
37. Verifikasi nilai tersimpan `NamaE120` (120 karakter) tanpa spasi akhir (dibaca dari state BE)
38. Pulihkan `Furniture {runId}-051` ke nilai seed lewat API

## Notes

- Mode: FE+BE. Enam blok berdiri sendiri (validasi Category Name pada popup Edit satu baris) sehingga jumlah langkah (38) sedikit melewati sekitar 35; kegagalan satu blok tidak menghilangkan makna blok lain.
- Popup Edit dipakai berulang tanpa dibuka ulang pada blok TC-FA-CAT-178, 179 (dibuka dari TC-FA-CAT-177) dan 531 (dari TC-FA-CAT-538), karena kasus yang diblok tidak menutup popup; popup dibuka ulang bila ada alasan state (sesudah Save sukses).
- Langkah penghubung (S-03, S-09, R-12): langkah 7 (mengisi `Furniture {runId}-051` agar error inline `must not be empty` terhapus sebelum kasus identik berikutnya), langkah 15, 24, 38 (memulihkan `Furniture {runId}-051`; langkah 15 dan 24 disusul muat ulang halaman Categories agar daftar memakai nama seed sebelum langkah 17 dan 25), langkah 16 (baseline log, S-12), langkah 21 dan 23 (membuka dan menutup Changelog), langkah 12 dan 33 (melanjutkan di popup yang masih terbuka).
- Langkah 31 menafsirkan "Save diblok" sebagai popup tetap terbuka setelah `[Save]` diklik; TC-FA-CAT-538 tidak menyebut keadaan tombol.
- Temuan untuk QA:
  - TC-FA-CAT-177 sampai 180, 531, dan 538 menyebut baris `Furniture` Pre-setup sebagai target Edit; spec memakai kategori milik spec `Furniture {runId}-051` (S-06) agar data Pre-setup tidak berubah. TC-FA-CAT-179 dan 531 menyebut `120 karakter E` murni; spec memakai nama 120 karakter berakhiran suffix run agar unik (S-12); `  Furniture Trim  ` pada TC-FA-CAT-180 diberi suffix run.
  - TC-FA-CAT-179 dan 531 menyebut "diterima" tanpa langkah observasi nilai tersimpan; langkah 14 memakai toast Expected, langkah 37 memakai Expected b TC-FA-CAT-531.
  - TC-FA-CAT-538 Expected c "Save diblok" tidak menyebut apakah tombol disabled atau klik ditolak; spec mengasersi popup tetap terbuka.
  - TC-FA-CAT-180 tidak menyebut cara membaca "nilai tersimpan"; spec memakai baris tabel dan entri Changelog.
- Spec melewati 35 langkah (38 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri.
