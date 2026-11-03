---
id: TC-AC-DC-E2E-041-edit-batas-trim-dan-device-sku
title: "Edit Category: Batas 120 Karakter, Auto-trim, dan Edit lewat Sub-tab Device SKU"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-102
  - TC-AC-DC-104
  - TC-AC-DC-270
coverage:
  web: automated
---

# Edit Category: Batas 120 Karakter, Auto-trim, dan Edit lewat Sub-tab Device SKU

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-041`): `Pemindai {runId}-041` (leaf). Nama node berubah berurutan menjadi `N102` (TC-102), `Pemindai Pro {runId}-041` (TC-104), lalu `SKU Surface Edit {runId}-041` (TC-270); hook `after` menghapus node dengan nama terakhir itu lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Nilai uji: `N102` = awal teks `Fixture.settingsDeviceCategory.name120Edit` dipotong lalu diakhiri ` {runId}-041` sehingga panjang total tepat 120 karakter termasuk suffix (TC-102); `   Pemindai Pro {runId}-041   ` dengan 3 spasi di awal dan di akhir (TC-104).
- Kemampuan teknis: Search pada modal Changelog dipakai untuk menemukan entri berdasarkan nama bersuffix unik.

## Test Steps

### Nama tepat 120 karakter diterima (TC-102)

1. Expand `Hardware` lalu `Handheld Reader`
2. Hover node `Pemindai {runId}-041`, klik aksi Edit
3. Ganti isi input dengan `N102`, klik `[Save]`
4. Verifikasi tidak ada error inline
5. Verifikasi toast sukses "Success, category has been updated."
6. Verifikasi nama node tersimpan utuh 120 karakter

### Auto-trim spasi tepi (TC-104)

7. Tunggu toast sukses dari blok sebelumnya hilang otomatis
8. Hover node `N102`, klik aksi Edit
9. Ganti isi input dengan `   Pemindai Pro {runId}-041   `, klik `[Save]`
10. Verifikasi toast sukses "Success, category has been updated."
11. Verifikasi node tampil dengan nama `Pemindai Pro {runId}-041` tanpa spasi tepi
12. Klik ikon Changelog pada header Sidebar Category
13. Ketik Search `Pemindai Pro {runId}-041`, tekan Enter
14. Verifikasi entri `Edit` dengan New Value `Pemindai Pro {runId}-041` tanpa spasi tepi
15. Klik `[×]` pada modal Changelog

### Edit lewat sub-tab Device SKU (TC-270)

16. Buka sub-tab `Device SKU` pada Settings > Device
17. Expand `Hardware` lalu `Handheld Reader`
18. Hover node `Pemindai Pro {runId}-041`, klik aksi Edit
19. Ganti isi input dengan `SKU Surface Edit {runId}-041`, klik `[Save]`
20. Verifikasi toast sukses "Success, category has been updated."
21. Verifikasi node tampil dengan nama `SKU Surface Edit {runId}-041` pada sidebar Device SKU

## Notes

- S-03, langkah penghubung: langkah 1 dan 17 (membuka cabang tree), langkah 7 (menunggu toast lama hilang), langkah 15 (menutup modal Changelog), langkah 16 (membuka sub-tab Device SKU). Search pada modal Changelog (langkah 13) menemukan entri berdasarkan nama bersuffix unik.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 `Rugged Scanner` sebagai target Edit dan nama 120 karakter literal. Spec memakai node milik spec; nama 120 karakter TC-102 memakai suffix `{runId}-041` dalam hitungan 120 karakter, sehingga sebagian karakter akhir Data Uji TC diganti suffix.
  - Post Condition TC-270 (satu entri Edit pada Changelog) tidak diasersi karena TC tidak memberi langkah observasinya (S-01).
  - TC-102 tidak menyebut Changelog; spec tidak mengasersinya.
