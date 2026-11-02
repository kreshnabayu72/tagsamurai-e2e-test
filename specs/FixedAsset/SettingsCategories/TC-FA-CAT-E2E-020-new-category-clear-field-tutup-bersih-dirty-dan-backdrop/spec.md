---
id: TC-FA-CAT-E2E-020-new-category-clear-field-tutup-bersih-dirty-dan-backdrop
title: "New Category: Clear Field, Tutup Popup Bersih dan Terisi (Unsaved Changes), serta Klik Backdrop"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-62
  - TC-FA-CAT-64
  - TC-FA-CAT-65
  - TC-FA-CAT-66
  - TC-FA-CAT-67
coverage:
  web: automated
---

# New Category: Clear Field, Tutup Popup Bersih dan Terisi (Unsaved Changes), serta Klik Backdrop

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang dipaksa lewat `Spectra.intercept()`.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settingsCategories.totalControl` (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`, client CatMain (Pre-setup #20). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan; keputusan tim).
- Data Pre-setup: client CatMain (Pre-setup #20); hanya dibaca. Tidak ada kategori yang tersimpan oleh spec ini (semua popup ditutup tanpa Submit), sehingga tidak ada cleanup data.
- Seed dan pemulihan lewat API, flag Guided Tooltip, dan hook suite lain: lihat `suite.md`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-62: [Clear Field] popup New Category mengosongkan field dan menghapus error tanpa dialog

1. Klik `[+] Category` pada sidebar
2. Isi Category Name `Temp`, Code `TMP`, Description `Temp desc`
3. Centang `Stay on this form after submitting`
4. Kosongkan Category Name lalu klik `[Submit]`
5. Verifikasi error inline `Category name must not be empty` tampil
6. Isi ulang Category Name `Temp`
7. Klik `[Clear Field]`
8. Verifikasi Category Name, Code, dan Description kosong dan placeholder tampil kembali
9. Verifikasi border merah dan pesan `Category name must not be empty` hilang
10. Verifikasi popup tetap terbuka, kursor fokus ke Category Name, dan tidak ada dialog Unsaved Changes
11. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
12. Hilangkan centang `Stay on this form after submitting`, lalu klik icon close (✕)

### TC-FA-CAT-64: Menutup popup New Category tanpa isian tidak memunculkan dialog Unsaved Changes

13. Klik `[+] Category` pada sidebar
14. Klik icon close (✕)
15. Verifikasi popup langsung tertutup dan dialog Unsaved Changes tidak muncul
16. Klik `[+] Category` pada sidebar
17. Tekan `Esc`
18. Verifikasi popup langsung tertutup dan dialog Unsaved Changes tidak muncul

### TC-FA-CAT-67: Klik backdrop popup New Category tidak menutup form baik bersih maupun terisi

19. Klik `[+] Category` pada sidebar
20. Klik area backdrop di luar popup
21. Verifikasi popup tetap terbuka
22. Isi Category Name `Backdrop Cat`
23. Klik area backdrop di luar popup lagi
24. Verifikasi popup tetap terbuka
25. Verifikasi input `Backdrop Cat` dipertahankan dan dialog Unsaved Changes tidak muncul

### TC-FA-CAT-65: Menutup popup New Category yang terisi memunculkan dialog Unsaved Changes dan [Cancel] mempertahankan form

26. Ubah isi Category Name menjadi `Dirty Cat`
27. Klik icon close (✕)
28. Verifikasi dialog tampil dengan body `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` serta `[Leave]` (severity warning)
29. Pada dialog klik `[Cancel]`
30. Verifikasi dialog tertutup, popup tetap terbuka, dan input `Dirty Cat` dipertahankan

### TC-FA-CAT-66: Dialog Unsaved Changes pada popup New Category: [Leave] menutup popup tanpa menyimpan

31. Ubah isi Category Name menjadi `Leave Cat`
32. Tekan `Esc`
33. Verifikasi `Esc` memunculkan dialog Unsaved Changes yang sama dengan icon close (✕)
34. Pada dialog klik `[Leave]`
35. Verifikasi popup tertutup
36. Verifikasi kategori `Leave Cat` tidak tersimpan: tidak ada di tabel dan sidebar (anchor positif: halaman Categories tampil dengan sidebar)

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan dan penggabungan form (S-10, prinsip 6): TC-FA-CAT-67 diletakkan sebelum TC-FA-CAT-65 dan TC-FA-CAT-66; ketiganya memakai satu sesi popup yang sama (popup dari langkah 19 berlanjut sampai langkah 36) dan langkah isinya mengganti nilai Category Name (langkah 26 dan 31). Jumlah buka form (langkah 1, 13, 16, 19) sama dengan jumlah kejadian menutup (langkah 12, 15, 18, 35).
- Langkah penghubung (S-03): langkah 12 (menutup popup bersih sesudah TC-FA-CAT-62: mencabut centang Stay dan menutup; tanpa asersi), langkah 26 dan 31 (mengganti nilai input).
- TC-FA-CAT-62 membuka popup dengan field yang diisi lalu dikosongkan oleh `[Clear Field]`; penutupan di langkah 12 tidak diasersi dialognya karena TC sumber tidak menyebutnya.
- Temuan untuk QA:
  - TC-FA-CAT-62 tidak menyebut apakah popup yang sudah di-Clear Field dianggap bersih saat ditutup; spec menutupnya tanpa asersi dialog.
  - TC-FA-CAT-66 Expected b menyebut kategori `Leave Cat` "tidak ada di tabel dan sidebar" tanpa langkah pencarian; spec mengasersi lewat tampilan halaman Categories dengan sidebar sesudah popup tertutup tanpa menambah pencarian.
  - TC-FA-CAT-65 dan TC-FA-CAT-66 tidak memberi suffix `{runId}` pada nama karena nama tidak pernah tersimpan; tidak ada kolisi data.
- Spec melewati 35 langkah (36 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri; nomor cadangan slice habis sehingga tidak dipecah lebih jauh.
