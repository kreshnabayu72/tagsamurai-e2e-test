---
id: TC-AC-DC-E2E-033-add-unsaved-clear-dan-esc
title: "Add Subcategory: Clear Field, Esc pada Input Bersih, Input Kembali Kosong, dan Esc dengan Perubahan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-69
  - TC-AC-DC-70
  - TC-AC-DC-263
  - TC-AC-DC-71
coverage:
  web: automated
---

# Add Subcategory: Clear Field, Esc pada Input Bersih, Input Kembali Kosong, dan Esc dengan Perubahan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, nama bersuffix `{runId}-033`): `Induk {runId}-033` dengan satu anak `Anak Awal {runId}-033` (pembanding). Hook `after` menghapus `Induk {runId}-033` beserta anaknya lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Nilai uji: `Temp Name` (TC-69), `Draft Name` (TC-263, TC-71); tidak ada yang disimpan sehingga tidak bersuffix.
- Kemampuan teknis: jumlah baris hasil Search pada modal Changelog dapat dibaca sebagai baseline sebelum aksi (disediakan tim FE/BE).

## Test Steps

### Baseline Changelog

1. Expand `Hardware` lalu `Handheld Reader`
2. Klik ikon Changelog pada header Sidebar Category
3. Ketik Search `{runId}-033`, tekan Enter
4. Catat jumlah baris hasil Search sebagai baseline (entri hasil seeding)
5. Klik `[×]` pada modal Changelog

### Clear Field mengosongkan input tanpa dialog (TC-69)

6. Hover node `Induk {runId}-033`, klik aksi `+ Subcategory`
7. Klik `[Submit]` dengan input kosong
8. Ketik `Temp Name`, klik `[Clear Field]`
9. Verifikasi input menjadi kosong
10. Verifikasi pesan error inline hilang
11. Verifikasi input inline Add tetap terbuka
12. Verifikasi fokus kembali ke input
13. Verifikasi tidak ada dialog konfirmasi

### Esc pada input bersih (TC-70)

14. Tekan Esc tanpa mengetik apa pun
15. Verifikasi input inline Add collapse
16. Verifikasi tidak ada dialog "You have unsaved changes. Are you sure you want to leave?"

### Nilai diketik lalu dihapus kembali ke kosong (TC-263)

17. Hover node `Induk {runId}-033`, klik aksi `+ Subcategory`
18. Ketik `Draft Name`, lalu hapus seluruh teks dengan Backspace sampai input kosong
19. Tekan Esc
20. Verifikasi input inline Add collapse
21. Verifikasi tidak ada dialog "You have unsaved changes. Are you sure you want to leave?"

### Esc pada input yang berisi perubahan: Leave (TC-71)

22. Hover node `Induk {runId}-033`, klik aksi `+ Subcategory`
23. Ketik `Draft Name`, tekan Esc
24. Verifikasi dialog dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Leave]` dan `[Cancel]`
25. Klik `[Leave]`
26. Verifikasi input inline Add collapse tanpa menyimpan

### Pemeriksaan akhir tidak ada node dan tidak ada entri baru

27. Expand `Induk {runId}-033`
28. Verifikasi `Induk {runId}-033` hanya memuat anak `Anak Awal {runId}-033`
29. Klik ikon Changelog pada header Sidebar Category
30. Ketik Search `{runId}-033`, tekan Enter
31. Verifikasi jumlah baris hasil Search sama dengan baseline
32. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 (membuka cabang tree), langkah 5 dan 32 (menutup modal Changelog), langkah 7 (Submit kosong untuk memunculkan error yang kemudian dibersihkan `[Clear Field]` pada TC-69).
- S-05: klausa "tidak ada node baru dan tidak ada entri log" pada TC-70, TC-263, dan TC-71 dinyatakan sebagai asersi jumlah dengan baseline (langkah 4, 28, 31), bukan asersi absence kelas g, karena semua kasus memakai suffix yang sama dan tidak ada kasus yang menyimpan node.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 `Rugged Scanner` sebagai induk Add. Spec memakai `Induk {runId}-033` milik spec.
  - TC-69 mengharapkan fokus kembali ke input setelah `[Clear Field]`; spec mengasersinya (langkah 12) tanpa langkah observasi tambahan.
