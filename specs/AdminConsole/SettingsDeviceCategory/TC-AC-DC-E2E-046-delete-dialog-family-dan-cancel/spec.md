---
id: TC-AC-DC-E2E-046-delete-dialog-family-dan-cancel
title: "Delete Category: Dialog Konfirmasi Family dan Cancel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-128
  - TC-AC-DC-132
coverage:
  web: automated
---

# Delete Category: Dialog Konfirmasi Family dan Cancel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-046`): family `Keluarga {runId}-046` dengan anak `Anak A {runId}-046` (leaf) dan `Anak B {runId}-046`, serta cucu `Cucu {runId}-046` di bawah `Anak B {runId}-046`; tidak ada Device Name pengacu dan family tidak pernah dihapus oleh spec ini. Hook `after` menghapus `Keluarga {runId}-046` beserta seluruh descendant lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Kemampuan teknis: jumlah baris hasil Search pada modal Changelog dapat dibaca sebagai baseline sebelum aksi (disediakan tim FE/BE).

## Test Steps

### Baseline Changelog

1. Expand `Hardware` lalu `Handheld Reader`
2. Klik ikon Changelog pada header Sidebar Category
3. Ketik Search `{runId}-046`, tekan Enter
4. Catat jumlah baris hasil Search sebagai baseline (entri hasil seeding)
5. Klik `[×]` pada modal Changelog

### Dialog konfirmasi Delete family (TC-128)

6. Hover node `Keluarga {runId}-046`, klik aksi Delete
7. Verifikasi judul dialog "Delete Category" tanpa tanda tanya
8. Verifikasi isi dialog diawali bullet `Keluarga {runId}-046` (hanya nama node yang diklik) lalu kalimat "Deleting this category will also delete all its subcategories. Are you sure you want to delete it? This action cannot be undone."
9. Verifikasi dua tombol `[Cancel]` dan `[Delete]`
10. Verifikasi node `Keluarga {runId}-046` dan subcategory-nya belum terhapus

### Cancel tidak menghapus apa pun (TC-132)

11. Klik `[Cancel]`
12. Verifikasi dialog tertutup
13. Expand `Keluarga {runId}-046`, `Anak B {runId}-046`
14. Verifikasi `Keluarga {runId}-046` dan seluruh descendant (`Anak A {runId}-046`, `Anak B {runId}-046`, `Cucu {runId}-046`) masih ada di tree
15. Verifikasi tidak ada toast
16. Klik ikon Changelog pada header Sidebar Category
17. Ketik Search `{runId}-046`, tekan Enter
18. Verifikasi jumlah baris hasil Search sama dengan baseline
19. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 dan 13 (membuka cabang tree), langkah 5 dan 19 (menutup modal Changelog).
- S-05: klausa "tidak ada entri log" pada TC-132 dinyatakan sebagai asersi jumlah dengan baseline (langkah 4 dan 18), bukan asersi absence kelas g.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 `Hapus Keluarga` (beserta `Hapus Keluarga Anak A`, `Hapus Keluarga Anak B`, `Hapus Keluarga Cucu`) sebagai target Delete dan menyebut Device Name Pre-setup #15 sebagai precondition tanpa memakainya pada langkah atau Expected. Spec memakai family milik spec bersuffix `{runId}-046` dan tidak memakai Device Name Pre-setup #15.
