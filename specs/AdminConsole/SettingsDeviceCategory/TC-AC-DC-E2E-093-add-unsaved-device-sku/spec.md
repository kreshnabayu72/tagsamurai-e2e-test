---
id: TC-AC-DC-E2E-093-add-unsaved-device-sku
title: "Add Subcategory: Dialog Unsaved Changes pada Sub-tab Device SKU"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-273
coverage:
  web: automated
---

# Add Subcategory: Dialog Unsaved Changes pada Sub-tab Device SKU

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, nama bersuffix `{runId}-093`): `Induk {runId}-093` dengan satu anak `Anak Awal {runId}-093` (node lain sebagai sasaran klik dan pembanding). Hook `after` menghapus `Induk {runId}-093` beserta anaknya lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Nilai uji: `Draft Name` (tidak pernah disimpan sehingga tidak bersuffix).
- Kemampuan teknis (disediakan tim FE/BE; tanpa endpoint karangan): membaca jumlah total entri Changelog Category sebelum aksi (B273, langkah 3) karena Changelog adalah audit trail permanen (S-12); asersi memakai selisih terhadap B273.

## Test Steps

1. Buka sub-tab `Device SKU` pada Settings > Device
2. Expand `Hardware` lalu `Handheld Reader`
3. Baca dan catat jumlah entri Changelog Category sebagai B273 (kemampuan baca)
4. Hover node `Induk {runId}-093`, klik aksi `+ Subcategory`
5. Ketik `Draft Name`, klik node `Anak Awal {runId}-093`
6. Verifikasi dialog dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Leave]` dan `[Cancel]`
7. Klik `[Leave]`
8. Verifikasi input Add tertutup tanpa menyimpan
9. Verifikasi `Induk {runId}-093` hanya memuat anak `Anak Awal {runId}-093`
10. Klik ikon Changelog pada header Sidebar Category
11. Verifikasi tabel Changelog menampilkan sedikitnya satu baris
12. Verifikasi jumlah entri Changelog Category sama dengan B273 (kemampuan baca)
13. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 (membuka sub-tab Device SKU), langkah 2 (membuka cabang tree), langkah 13 (menutup modal Changelog).
- S-05: klausa "node `Draft Name` tidak dibuat dan tidak ada entri log" dinyatakan sebagai asersi jumlah dengan baseline B273 (langkah 3, 9, 12), bukan asersi absence kelas g. Langkah 11 (tabel Changelog menampilkan sedikitnya satu baris) menjadi anchor bahwa surface Changelog termuat sebelum langkah 12. Selisih jumlah total dibaca lewat kemampuan baca, bukan lewat Search, karena `Draft Name` tidak pernah disimpan dan tidak dapat dicari di Changelog.
- Pembagian TC lintas spec: TC-259, TC-260, dan TC-267 (Add pada sub-tab Device Name) ada di spec 036.
- Temuan untuk QA:
  - TC-273 memakai node literal Pre-setup #14 `Rugged Scanner` dan `Barcode Handheld`. Spec memakai `Induk {runId}-093` dan `Anak Awal {runId}-093` milik spec.
