---
id: TC-AC-DC-E2E-034-add-unsaved-dialog-leave-cancel
title: "Add Subcategory: Dialog Unsaved Changes, Leave, Cancel, dan Esc pada Dialog"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-72
  - TC-AC-DC-73
  - TC-AC-DC-257
  - TC-AC-DC-265
coverage:
  web: automated
---

# Add Subcategory: Dialog Unsaved Changes, Leave, Cancel, dan Esc pada Dialog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, nama bersuffix `{runId}-034`): `Induk {runId}-034` dengan satu anak `Anak Awal {runId}-034` (node lain sebagai tujuan perpindahan dan pembanding). Hook `after` menghapus `Induk {runId}-034` beserta anaknya lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Nilai uji: `Draft Name` (tidak pernah disimpan sehingga tidak bersuffix).
- Kemampuan teknis: jumlah baris hasil Search pada modal Changelog dapat dibaca sebagai baseline sebelum aksi (disediakan tim FE/BE).

## Test Steps

### Baseline Changelog

1. Expand `Hardware` lalu `Handheld Reader`
2. Klik ikon Changelog pada header Sidebar Category
3. Ketik Search `{runId}-034`, tekan Enter
4. Catat jumlah baris hasil Search sebagai baseline (entri hasil seeding)
5. Klik `[×]` pada modal Changelog

### Leave menutup input tanpa menyimpan (TC-72)

6. Hover node `Induk {runId}-034`, klik aksi `+ Subcategory`
7. Ketik `Draft Name`, klik node `Anak Awal {runId}-034`
8. Verifikasi dialog dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Leave]` dan `[Cancel]`
9. Klik `[Leave]`
10. Verifikasi input inline Add tertutup tanpa menyimpan
11. Verifikasi node `Draft Name` tidak dibuat di bawah `Induk {runId}-034`

### Cancel mempertahankan input dan nilai (TC-73)

12. Hover node `Induk {runId}-034`, klik aksi `+ Subcategory`
13. Ketik `Draft Name`, klik node `Anak Awal {runId}-034`
14. Verifikasi dialog dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Leave]` dan `[Cancel]`
15. Klik `[Cancel]`
16. Verifikasi dialog tertutup
17. Verifikasi input inline Add tetap terbuka dengan nilai `Draft Name` dipertahankan

### Esc pada input yang berisi perubahan: Cancel (TC-257)

18. Tekan Esc pada input yang masih berisi `Draft Name`
19. Verifikasi dialog dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Leave]` dan `[Cancel]`
20. Klik `[Cancel]`
21. Verifikasi dialog tertutup
22. Verifikasi input inline Add tetap terbuka dengan nilai `Draft Name`

### Esc pada dialog setara Cancel (TC-265)

23. Hover node `Anak Awal {runId}-034`, klik aksi `+ Subcategory`
24. Verifikasi dialog dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Leave]` dan `[Cancel]`
25. Tekan Esc
26. Verifikasi dialog tertutup
27. Verifikasi input inline Add pada `Induk {runId}-034` tetap terbuka dengan nilai `Draft Name`
28. Klik `[Clear Field]`, tekan Esc

### Pemeriksaan akhir tidak ada node dan tidak ada entri baru

29. Verifikasi `Induk {runId}-034` hanya memuat anak `Anak Awal {runId}-034`
30. Klik ikon Changelog pada header Sidebar Category
31. Ketik Search `{runId}-034`, tekan Enter
32. Verifikasi jumlah baris hasil Search sama dengan baseline
33. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 (membuka cabang tree), langkah 5 dan 33 (menutup modal Changelog), langkah 28 (memulihkan input yang dirty ke keadaan bersih lalu menutupnya tanpa dialog).
- Urutan TC-257 dan TC-265 memakai input yang sama yang dibiarkan terbuka dengan `Draft Name` oleh TC-73, sehingga `Draft Name` tidak diketik ulang; semua TC dijalankan berurutan pada satu input terbuka tanpa menyimpan.
- S-05: klausa "tidak ada node baru dan tidak ada entri log" pada TC-72, TC-73, TC-257 dinyatakan sebagai asersi jumlah dengan baseline (langkah 4, 29, 32), bukan asersi absence kelas g.
- Temuan untuk QA:
  - TC-72 dan TC-73 menulis "berpindah ke node lain" tanpa menyebut aksi persisnya; spec memakai klik pada node `Anak Awal {runId}-034` (selaras dengan TC-273). Jika klik node memilih filter Category, pilihan itu terbawa; TC tidak menyebut efeknya.
  - TC memakai node literal Pre-setup #14 `Rugged Scanner` sebagai induk Add. Spec memakai `Induk {runId}-034` milik spec.
