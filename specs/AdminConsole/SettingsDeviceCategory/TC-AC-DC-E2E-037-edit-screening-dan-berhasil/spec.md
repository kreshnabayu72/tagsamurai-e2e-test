---
id: TC-AC-DC-E2E-037-edit-screening-dan-berhasil
title: "Edit Category: Screening Input Inline dan Edit Berhasil"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-98
  - TC-AC-DC-99
  - TC-AC-DC-308
  - TC-AC-DC-100
coverage:
  web: automated
---

# Edit Category: Screening Input Inline dan Edit Berhasil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware`, `Handheld Reader`, dan `Rugged Scanner` (sibling terakhir pembanding urutan). Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-037`): `Pemindai {runId}-037` (leaf; TC-98 dan TC-99, diubah menjadi `Zebra Mobile {runId}-037`); `Kunci Cari {runId}-037` (leaf; TC-308, diubah menjadi `Zebra Dua {runId}-037`); `Industri {runId}-037` dengan dua anak `Anak X {runId}-037` dan `Anak Y {runId}-037` (TC-100, diubah menjadi `Industri Ubah {runId}-037`); Device Name `TS-A {runId}-037` (Category `Anak X {runId}-037`) dan `TS-B {runId}-037` (Category `Anak Y {runId}-037`). Hook `after` menghapus Device Name milik spec, lalu node `Zebra Mobile {runId}-037`, `Zebra Dua {runId}-037`, dan `Industri Ubah {runId}-037` beserta anaknya lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Kemampuan teknis: pembuatan Device Name `TS-A` dan `TS-B` lewat sesi API aktor (kolom wajib selain Category tidak disebut TC; disediakan tim FE/BE tanpa endpoint karangan). Search pada modal Changelog dan Search tabel Device Name dipakai sebagai langkah penghubung untuk menemukan entri atau baris berdasarkan nama bersuffix unik.

## Test Steps

### Screening input inline Edit (TC-98)

1. Expand `Hardware` lalu `Handheld Reader`
2. Hover node `Pemindai {runId}-037`, klik aksi Edit
3. Verifikasi input inline muncul menggantikan label node `Pemindai {runId}-037`
4. Verifikasi field "Category Name" terisi nama saat ini `Pemindai {runId}-037`
5. Verifikasi kursor langsung fokus di dalam input
6. Verifikasi tombol `[Save]` dan `[Clear Field]` tampil
7. Verifikasi tidak ada tombol `[Cancel]`
8. Klik `[Clear Field]`
9. Verifikasi placeholder "Enter category name" tampil pada input yang dikosongkan

### Edit nama berhasil dan urutan A-Z diperbarui (TC-99)

10. Ganti isi input dengan `Zebra Mobile {runId}-037`, klik `[Save]`
11. Verifikasi toast sukses "Success, category has been updated."
12. Verifikasi input tertutup
13. Verifikasi node tampil dengan nama `Zebra Mobile {runId}-037`
14. Verifikasi node `Zebra Mobile {runId}-037` pindah ke posisi alfabetisnya sebagai sibling terakhir di bawah `Handheld Reader`, setelah `Rugged Scanner`
15. Verifikasi parent node `Zebra Mobile {runId}-037` tetap `Handheld Reader`
16. Klik ikon Changelog pada header Sidebar Category
17. Ketik Search `Zebra Mobile {runId}-037`, tekan Enter
18. Verifikasi satu entri dengan Action `Edit` untuk Category `Zebra Mobile {runId}-037`
19. Klik `[×]` pada modal Changelog

### Pencarian tree aktif lalu Edit nama tidak cocok query (TC-308)

20. Ketik Search tree `Kunci Cari {runId}-037` pada TreeSearchInput, tekan Enter
21. Hover node `Kunci Cari {runId}-037`, klik aksi Edit
22. Ganti isi input dengan `Zebra Dua {runId}-037`, klik `[Save]`
23. Verifikasi toast sukses "Success, category has been updated."
24. Verifikasi kotak TreeSearchInput masih berisi `Kunci Cari {runId}-037`
25. Verifikasi node `Zebra Dua {runId}-037` terlihat dengan parent `Handheld Reader` ter-expand walau tidak cocok dengan query
26. Klik `(←)` pada TreeSearchInput

### Rename node yang memiliki anak (TC-100)

27. Expand `Hardware` lalu `Handheld Reader`
28. Hover node `Industri {runId}-037`, klik aksi Edit
29. Ganti isi input dengan `Industri Ubah {runId}-037`, klik `[Save]`
30. Verifikasi toast sukses "Success, category has been updated."
31. Expand node `Industri Ubah {runId}-037`
32. Verifikasi node `Industri Ubah {runId}-037` tetap memiliki anak `Anak X {runId}-037` dan `Anak Y {runId}-037`
33. Ketik Search tabel Device Name `TS-`, tekan Enter
34. Verifikasi Device Name `TS-A {runId}-037` dan `TS-B {runId}-037` tetap terkait dengan node `Anak X {runId}-037` dan `Anak Y {runId}-037`

## Notes

- S-03, langkah penghubung: langkah 1, 27 (membuka cabang tree), langkah 19 (menutup modal Changelog), langkah 20 (Search tree untuk menjalankan pencarian aktif), langkah 26 (mengosongkan TreeSearchInput sebelum kasus berikutnya), langkah 33 (Search tabel Device Name untuk menemukan baris target). Search pada modal Changelog (langkah 17) menemukan entri berdasarkan nama bersuffix unik. Setelah langkah 9, input diganti isinya pada langkah 10 sehingga tidak perlu memulihkan nilai awal.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 (`Rugged Scanner`, `Industrial Scanner`) dan Device Name `TS-200`, `TS-210` sebagai target Edit. Spec memakai node dan Device Name milik spec bersuffix `{runId}-037`; asersi urutan TC-99 tetap bergantung pada nama literal `Rugged Scanner` sebagai sibling terakhir.
  - TC-100 tidak menyebut cara mengamati keterkaitan Device Name dengan node; spec memakai kolom Category pada hasil Search tabel Device Name.
  - Post Condition TC-99 (nama tersimpan, entri pada System Log dan Activity Log, nama tercermin di Device SKU dan dropdown, konsumen read) tidak diasersi karena TC tidak memberi langkah observasinya (S-01).
  - TC-99 menyebut "satu entri Edit tercatat di Changelog" sebagai Expected; spec mengasersinya lewat Search nama bersuffix unik.
