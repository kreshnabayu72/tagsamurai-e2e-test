---
id: TC-AC-DC-E2E-029-add-validasi-wajib-dan-batas
title: "Add Subcategory: Validasi Nama Wajib, Batas 121 Karakter, Nama Reserved, dan Enter Tidak Men-submit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DC-79
  - TC-AC-DC-81
  - TC-AC-DC-90
  - TC-AC-DC-78
coverage:
  web: automated
---

# Add Subcategory: Validasi Nama Wajib, Batas 121 Karakter, Nama Reserved, dan Enter Tidak Men-submit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, nama bersuffix `{runId}-029`): `Induk {runId}-029` dengan satu anak `Anak Awal {runId}-029` (pembanding). Hook `after` menghapus `Induk {runId}-029` beserta anaknya lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Nilai uji: nama 121 karakter `Fixture.settingsDeviceCategory.name121` (TC-81, diblokir sehingga tidak tersimpan dan tidak bersuffix); `All Categories` dan `  all categories  ` (TC-90); `Enter Test` (TC-78).
- Kemampuan teknis: jumlah baris hasil Search pada modal Changelog dapat dibaca sebagai baseline sebelum aksi (disediakan tim FE/BE).

## Test Steps

### Baseline Changelog

1. Expand `Hardware` lalu `Handheld Reader`
2. Klik ikon Changelog pada header Sidebar Category
3. Ketik Search `{runId}-029`, tekan Enter
4. Catat jumlah baris hasil Search sebagai baseline (entri hasil seeding)
5. Klik `[×]` pada modal Changelog

### Nama kosong (TC-79)

6. Hover node `Induk {runId}-029`, klik aksi `+ Subcategory`
7. Klik `[Submit]` dengan input kosong
8. Verifikasi pesan error inline "Category name must not be empty" di bawah input
9. Verifikasi input tetap terbuka (state Invalid)
10. Verifikasi tidak ada toast

### Nama 121 karakter (TC-81)

11. Ketik nama 121 karakter pada input
12. Verifikasi pesan error inline "Max. 120 characters" tampil langsung saat melebihi batas
13. Klik `[Submit]`
14. Verifikasi tidak ada toast

### Nama All Categories direservasi (TC-90)

15. Klik `[Clear Field]`
16. Ketik `All Categories`, klik `[Submit]`
17. Verifikasi pesan error inline "'All Categories' is a reserved name and cannot be used"
18. Klik `[Clear Field]`
19. Ketik `  all categories  `, klik `[Submit]`
20. Verifikasi pesan error inline "'All Categories' is a reserved name and cannot be used"

### Enter tidak men-submit (TC-78)

21. Klik `[Clear Field]`
22. Ketik `Enter Test`, tekan Enter
23. Verifikasi tidak ada toast
24. Verifikasi input inline tetap terbuka dengan nilai `Enter Test`
25. Klik `[Clear Field]`, tekan Esc

### Pemeriksaan akhir tidak ada node dan tidak ada entri baru

26. Expand `Induk {runId}-029`
27. Verifikasi `Induk {runId}-029` hanya memuat anak `Anak Awal {runId}-029`
28. Klik ikon Changelog pada header Sidebar Category
29. Ketik Search `{runId}-029`, tekan Enter
30. Verifikasi jumlah baris hasil Search sama dengan baseline
31. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 (membuka cabang tree), langkah 5 dan 31 (menutup modal Changelog), langkah 15, 18, 21 (`[Clear Field]` sebagai pembersih error sebelum kasus berikutnya, R-12), langkah 25 (memulihkan input ke keadaan bersih lalu menutupnya tanpa dialog). Satu pembukaan input dipakai untuk seluruh kasus tanpa submit sukses.
- S-05: klausa "tidak ada node baru dan tidak ada entri log" pada TC-79, TC-81, TC-90, TC-78 dinyatakan sebagai asersi jumlah dengan baseline (langkah 4, 27, 30), bukan asersi absence kelas g, karena semua kasus memakai suffix yang sama dan tidak ada kasus yang berhasil membuat node.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 (`Rugged Scanner`) sebagai induk Add. Spec memakai `Induk {runId}-029` milik spec.
  - TC-78 meminta "tidak ada request create"; TC tidak memberi cara mengamati request, sehingga spec membuktikannya lewat tidak adanya toast (langkah 23), input tetap terbuka (langkah 24), dan jumlah entri Changelog tidak berubah (langkah 30).
  - TC-81 tidak menyebut apakah pesan "Max. 120 characters" tetap tampil setelah `[Submit]`; spec tidak mengasersinya.
