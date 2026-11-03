---
id: TC-AC-DC-E2E-030-add-validasi-duplikat
title: "Add Subcategory: Validasi Nama Duplikat pada Parent yang Sama dan Nama Sama pada Parent Berbeda"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DC-86
  - TC-AC-DC-87
  - TC-AC-DC-88
  - TC-AC-DC-89
coverage:
  web: automated
---

# Add Subcategory: Validasi Nama Duplikat pada Parent yang Sama dan Nama Sama pada Parent Berbeda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware`, `Handheld Reader` (parent kasus duplikat), dan `Smart Fixed Reader` (parent berbeda pada TC-89). Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, nama bersuffix `{runId}-030`): `Nama Dasar {runId}-030` (leaf di bawah `Handheld Reader`, nama yang diduplikasi). Node `Nama Dasar {runId}-030` yang dibuat TC-89 di bawah `Smart Fixed Reader` juga dihapus di hook `after` lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Kemampuan teknis: jumlah baris hasil Search pada modal Changelog dapat dibaca sebagai baseline sebelum aksi (disediakan tim FE/BE).

## Test Steps

### Baseline Changelog

1. Expand `Hardware` lalu `Handheld Reader`
2. Klik ikon Changelog pada header Sidebar Category
3. Ketik Search `Nama Dasar {runId}-030`, tekan Enter
4. Catat jumlah baris hasil Search sebagai baseline (entri hasil seeding)
5. Klik `[×]` pada modal Changelog

### Duplikat terdeteksi saat mengetik (TC-86)

6. Hover node `Handheld Reader`, klik aksi `+ Subcategory`
7. Ketik `Nama Dasar {runId}-030`, tunggu 1 detik tanpa memindahkan fokus
8. Verifikasi pesan error inline "Category name already exists" tampil sekitar 500ms setelah berhenti mengetik, saat fokus masih di dalam input
9. Verifikasi input berstatus Invalid

### Duplikat case-insensitive setelah trim (TC-87)

10. Klik `[Clear Field]`
11. Ketik `  nama dasar {runId}-030  `, tunggu 1 detik
12. Verifikasi pesan error inline "Category name already exists"

### Submit nama duplikat (TC-88)

13. Klik `[Clear Field]`
14. Ketik `Nama Dasar {runId}-030`, langsung klik `[Submit]` sebelum validasi live selesai
15. Verifikasi pesan error inline "Category name already exists"
16. Verifikasi input inline tetap terbuka dengan nilai `Nama Dasar {runId}-030` dipertahankan
17. Klik `[Clear Field]`, tekan Esc

### Pemeriksaan tidak ada node dan tidak ada entri baru

18. Verifikasi hanya satu node `Nama Dasar {runId}-030` di bawah `Handheld Reader`
19. Klik ikon Changelog pada header Sidebar Category
20. Ketik Search `Nama Dasar {runId}-030`, tekan Enter
21. Verifikasi jumlah baris hasil Search sama dengan baseline
22. Klik `[×]` pada modal Changelog

### Nama sama pada parent berbeda (TC-89)

23. Hover node `Smart Fixed Reader`, klik aksi `+ Subcategory`
24. Ketik `Nama Dasar {runId}-030`, klik `[Submit]`
25. Verifikasi tidak ada pesan error duplikat
26. Verifikasi toast sukses "Success, category has been created."
27. Verifikasi node `Nama Dasar {runId}-030` muncul di bawah `Smart Fixed Reader`
28. Verifikasi node `Nama Dasar {runId}-030` di bawah `Handheld Reader` tetap ada dan tidak terpengaruh

## Notes

- S-03, langkah penghubung: langkah 1 (membuka cabang tree), langkah 5 dan 22 (menutup modal Changelog), langkah 10, 13, 17 (`[Clear Field]` sebagai pembersih error identik antar kasus, R-12; langkah 17 juga menutup input bersih tanpa dialog). Satu pembukaan input dipakai untuk TC-86, TC-87, TC-88.
- Urutan TC-89 (sukses) ditaruh di akhir spec agar validasi diblokir lebih dulu (S-10); pemeriksaan jumlah entri Changelog (langkah 18 sampai 21) ditaruh sebelum TC-89 agar entri Create TC-89 tidak mengubah baseline.
- S-05: klausa "`[Submit]` tidak membuat node, tidak ada entri log" pada TC-86 dan TC-88 dinyatakan sebagai asersi jumlah dengan baseline (langkah 4, 18, 21), bukan asersi absence kelas g.
- Temuan untuk QA:
  - TC menjadikan node literal Pre-setup #14 `Barcode Handheld` sebagai nama duplikat dan `Rugged Scanner` sebagai nama yang sama pada parent berbeda. Spec memakai node milik spec `Nama Dasar {runId}-030` sebagai nama yang diduplikasi sehingga asersi tidak bergantung pada nama literal.
  - TC-86 menyebut error tampil "sekitar 500ms" tanpa toleransi; spec mengasersi tampilnya error setelah jeda 1 detik tanpa mengukur 500ms secara presisi.
