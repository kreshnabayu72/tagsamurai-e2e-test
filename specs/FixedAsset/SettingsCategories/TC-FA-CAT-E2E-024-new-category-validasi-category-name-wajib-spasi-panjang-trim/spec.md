---
id: TC-FA-CAT-E2E-024-new-category-validasi-category-name-wajib-spasi-panjang-trim
title: "New Category: Validasi Category Name Wajib, Hanya Spasi, Batas Panjang 120, dan Trim"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-77
  - TC-FA-CAT-78
  - TC-FA-CAT-80
  - TC-FA-CAT-85
  - TC-FA-CAT-79
coverage:
  web: automated
---

# New Category: Validasi Category Name Wajib, Hanya Spasi, Batas Panjang 120, dan Trim

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang dipaksa lewat `Spectra.intercept()`.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settingsCategories.totalControl` (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`, client CatMain (Pre-setup #20). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan; keputusan tim).
- Data Pre-setup: client CatMain (Pre-setup #20); hanya dibaca.
- Data milik spec: dua kategori level 1 yang dibuat lewat UI: `NamaB120` (TC-FA-CAT-85, spasi akhir dibuang) dan `NamaA120` (TC-FA-CAT-79). Keduanya tepat 120 karakter dan unik per run (S-12): `NamaB120` = `B` sebanyak (120 dikurangi panjang `-{runId}-024`) diikuti `-{runId}-024`; `NamaA120` = `A` sebanyak jumlah yang sama diikuti `-{runId}-024`. Hook `after` menghapus keduanya lewat API berdasarkan nama.
- Nilai bantu `VAL77` (Code) dan `Desc 77` (Description) hanya diketik pada TC-FA-CAT-77 untuk mengamati klausa "input lain dipertahankan"; tidak ada kategori yang tersimpan dengan nilai itu.
- Seed dan pemulihan lewat API, flag Guided Tooltip, dan hook suite lain: lihat `suite.md`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-77: Category Name kosong ditolak setelah Submit (New Category)

1. Klik `[+] Category` pada sidebar
2. Biarkan Category Name kosong, isi Code `VAL77` dan Description `Desc 77` (nilai bantu agar klausa "input lain dipertahankan" teramati; nilai ini tidak ada di Data Uji TC)
3. Klik `[Submit]`
4. Verifikasi error inline `Category name must not be empty` tampil setelah klik `[Submit]`
5. Verifikasi popup tetap terbuka
6. Verifikasi Code tetap `VAL77`
7. Verifikasi Description tetap `Desc 77`
8. Verifikasi tidak ada kategori tersimpan (toast sukses tidak tampil)
9. Kosongkan Code dan Description

### TC-FA-CAT-78: Category Name yang hanya berisi spasi diperlakukan kosong dan ditolak (New Category)

10. Isi Category Name dengan 5 karakter spasi
11. Klik `[Submit]`
12. Verifikasi error inline `Category name must not be empty` tampil
13. Verifikasi popup tetap terbuka
14. Verifikasi tidak ada kategori tersimpan (toast sukses tidak tampil)

### TC-FA-CAT-80: Category Name 121 karakter menampilkan error langsung tanpa memotong ketikan (New Category)

15. Isi Category Name dengan 121 karakter `A` tanpa menekan Submit
16. Verifikasi border field `severity="danger"` tampil langsung saat melebihi batas
17. Verifikasi pesan `Max. 120 characters` tampil langsung saat melebihi batas
18. Verifikasi seluruh 121 karakter tetap tertulis di field (ketikan tidak dipotong)
19. Klik `[Submit]`
20. Verifikasi Submit diblok: popup tetap terbuka
21. Verifikasi tidak ada kategori tersimpan (toast sukses tidak tampil)

### TC-FA-CAT-85: Panjang Category Name dihitung setelah trim: spasi tepi tidak menimbulkan error

22. Ganti isi Category Name dengan `NamaB120` diikuti 5 spasi di akhir
23. Verifikasi tidak ada error `Max. 120 characters` (kelebihan hanya spasi tepi)
24. Klik `[Submit]`
25. Verifikasi toast `Success, category has been created.` tampil
26. Ketik Search `NamaB120`, tekan Enter
27. Verifikasi kategori tersimpan sebagai `NamaB120` (120 karakter) tanpa spasi akhir

### TC-FA-CAT-79: Category Name tepat 120 karakter diterima (New Category)

28. Klik `[+] Category` pada sidebar
29. Isi Category Name dengan `NamaA120`
30. Verifikasi tidak ada error `Max. 120 characters`
31. Klik `[Submit]`
32. Verifikasi toast `Success, category has been created.` tampil
33. Ketik Search `NamaA120`, tekan Enter
34. Verifikasi kategori tersimpan penuh 120 karakter sebagai `NamaA120`

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan dan penggabungan form (S-10, prinsip 6): validasi diblokir (TC-FA-CAT-77, 78, 80) sebelum aksi sukses (TC-FA-CAT-85, 79). TC-FA-CAT-78, 80, dan 85 membuka popup baru pada langkah pertamanya; spec memakai satu sesi popup dari TC-FA-CAT-77 yang hanya berisi input yang diganti pada langkah 10, 15, dan 22. Jumlah buka form (langkah 1 dan 28) sama dengan jumlah kejadian menutup (Submit sukses langkah 24 dan 31).
- Langkah penghubung (S-03, R-12, R-16): langkah 9 (mengosongkan Code dan Description bantu), langkah 10 dan 15 sekaligus mengganti nilai input sehingga error inline sebelumnya tidak terbawa ke TC berikutnya; langkah 26 dan 33 (Search untuk menemukan baris target).
- Penyimpangan data (S-12, R-06): TC menyebut "120 karakter `A`" dan "120 karakter `B`"; spec memakai `NamaA120` dan `NamaB120` (tetap tepat 120 karakter, diakhiri `-{runId}-024`) agar unik per run.
- Temuan untuk QA:
  - TC-FA-CAT-77 dan TC-FA-CAT-78 menyebut "tidak ada kategori tersimpan" tanpa langkah observasi; spec mengasersi lewat popup yang tetap terbuka dan tidak adanya toast sukses.
  - TC-FA-CAT-77 butir b menyebut "input lain dipertahankan" tanpa Data Uji untuk input lain; spec mengisi Code `VAL77` dan Description `Desc 77` sebagai nilai bantu (langkah penghubung) agar klausa itu dapat diasersi.
  - TC-FA-CAT-79 dan TC-FA-CAT-85 menyebut nama 120 karakter murni `A` dan `B`; spec memakai nama 120 karakter berakhiran suffix run agar unik (S-12).
