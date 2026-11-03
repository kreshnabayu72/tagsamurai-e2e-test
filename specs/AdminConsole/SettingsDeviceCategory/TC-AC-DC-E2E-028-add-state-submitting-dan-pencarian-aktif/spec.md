---
id: TC-AC-DC-E2E-028-add-state-submitting-dan-pencarian-aktif
title: "Add Subcategory: State Submitting, Klik Ganda Submit, dan Pencarian Tree Aktif"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-95
  - TC-AC-DC-96
  - TC-AC-DC-306
coverage:
  web: automated
---

# Add Subcategory: State Submitting, Klik Ganda Submit, dan Pencarian Tree Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, nama bersuffix `{runId}-028`): `Induk {runId}-028` (leaf di bawah `Handheld Reader`). Node hasil Add spec (`Pemindai Lambat {runId}-028`, `Pemindai Ganda {runId}-028`, `Wearable Scanner {runId}-028`) ikut terhapus saat hook `after` menghapus `Induk {runId}-028` beserta anaknya lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Kemampuan teknis: `Spectra.intercept()` menahan respons endpoint create Category selama 3 detik pada TC-95 (penundaan jaringan, bukan kegagalan) dan dilepas segera sesudahnya. Search pada modal Changelog dipakai untuk menemukan entri berdasarkan nama bersuffix unik.

## Test Steps

### State Submitting (TC-95)

1. Expand `Hardware` lalu `Handheld Reader`
2. Tahan respons endpoint create Category selama 3 detik
3. Hover node `Induk {runId}-028`, klik aksi `+ Subcategory`
4. Ketik `Pemindai Lambat {runId}-028`, klik `[Submit]`
5. Verifikasi input Category Name dalam state disabled selama respons tertunda
6. Verifikasi tombol `[Submit]` dan `[Clear Field]` dalam state disabled selama respons tertunda
7. Verifikasi indikator loading tampil selama respons tertunda
8. Lepas tahanan respons endpoint create Category
9. Verifikasi toast sukses "Success, category has been created."
10. Verifikasi input inline Add tertutup

### Klik ganda cepat pada Submit (TC-96)

11. Tunggu toast lama hilang otomatis (toast sukses dari blok sebelumnya)
12. Hover node `Induk {runId}-028`, klik aksi `+ Subcategory`
13. Ketik `Pemindai Ganda {runId}-028`, klik `[Submit]` dua kali dengan sangat cepat
14. Verifikasi hanya satu node `Pemindai Ganda {runId}-028` terbentuk di bawah `Induk {runId}-028`
15. Verifikasi hanya satu toast sukses "Success, category has been created."
16. Klik ikon Changelog pada header Sidebar Category
17. Ketik Search `Pemindai Ganda {runId}-028`, tekan Enter
18. Verifikasi hanya satu entri `Create` untuk Category `Pemindai Ganda {runId}-028`
19. Klik `[×]` pada modal Changelog

### Pencarian tree aktif lalu Add dengan nama tidak cocok query (TC-306)

20. Ketik Search tree `Induk {runId}-028` pada TreeSearchInput, tekan Enter
21. Hover node `Induk {runId}-028`, klik aksi `+ Subcategory`
22. Ketik `Wearable Scanner {runId}-028`, klik `[Submit]`
23. Verifikasi toast sukses "Success, category has been created."
24. Verifikasi kotak TreeSearchInput masih berisi `Induk {runId}-028`
25. Verifikasi node `Wearable Scanner {runId}-028` terlihat di bawah `Induk {runId}-028` (parent ter-expand) walau tidak cocok dengan query

## Notes

- S-03, langkah penghubung: langkah 1 (membuka cabang tree), langkah 2 dan 8 (memasang dan melepas tahanan respons), langkah 11 (menunggu toast lama hilang agar hitungan "hanya satu toast" bermakna, R-12), langkah 19 (menutup modal Changelog), langkah 20 (Search tree untuk menjalankan pencarian aktif). Search pada modal Changelog (langkah 17) menemukan entri berdasarkan nama bersuffix unik.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 (`Rugged Scanner`) sebagai induk Add dan query pencarian tree. Spec memakai node milik spec bersuffix `{runId}-028`; query TC-306 menjadi `Induk {runId}-028` dan nama baru tidak mengandung query itu.
  - Nilai "dua klik cepat" pada TC-96 tidak menyebut selang antar klik; spec memakai dua klik berurutan tanpa jeda buatan.
