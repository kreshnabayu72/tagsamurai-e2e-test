---
id: TC-AC-DC-E2E-026-add-screening-dan-berhasil
title: "Add Subcategory: Screening Input Inline dan Add Berhasil"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-62
  - TC-AC-DC-63
  - TC-AC-DC-64
  - TC-AC-DC-65
coverage:
  web: automated
---

# Add Subcategory: Screening Input Inline dan Add Berhasil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-026`): `Induk {runId}-026` (leaf, target Add pada TC-62, TC-63, TC-65) dan `Keluarga {runId}-026` dengan satu anak `Anak Awal {runId}-026` (node dalam keadaan collapse, target Add pada TC-64). Hook `after` menghapus `Induk {runId}-026` dan `Keluarga {runId}-026` beserta seluruh anaknya lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Kemampuan teknis: Search pada modal Changelog dipakai untuk menemukan entri berdasarkan nama bersuffix unik (baseline nol). Jeda pendek 5 detik pada TC-65 adalah pilihan spec untuk mengamati batas 4 detik toast.

## Test Steps

### Persiapan

1. Expand `Hardware` lalu `Handheld Reader`

### Screening input inline Add (TC-62)

2. Hover node `Induk {runId}-026`, klik aksi `+ Subcategory`
3. Verifikasi input inline Add muncul di bawah node `Induk {runId}-026` pada posisi anak baru
4. Verifikasi field "Category Name" kosong dengan placeholder "Enter category name"
5. Verifikasi field "Category Name" tanpa helper text
6. Verifikasi kursor langsung fokus di dalam input
7. Verifikasi tombol `[Submit]` dan `[Clear Field]` tampil
8. Verifikasi tidak ada tombol `[Cancel]`
9. Tekan Esc pada input yang masih bersih

### Add berhasil pada node user-created (TC-63)

10. Hover node `Induk {runId}-026`, klik aksi `+ Subcategory`
11. Ketik `Wearable Scanner {runId}-026` pada input, klik `[Submit]`
12. Verifikasi toast sukses "Success, category has been created."
13. Verifikasi input inline Add tertutup
14. Verifikasi node `Wearable Scanner {runId}-026` muncul sebagai anak `Induk {runId}-026`
15. Verifikasi node `Wearable Scanner {runId}-026` selectable (kotak centang tampil)
16. Verifikasi kotak centang node `Wearable Scanner {runId}-026` tidak tercentang
17. Verifikasi node `Wearable Scanner {runId}-026` tampil tidak bold
18. Klik ikon Changelog pada header Sidebar Category
19. Ketik Search `Wearable Scanner {runId}-026`, tekan Enter
20. Verifikasi satu entri dengan Action `Create` untuk Category `Wearable Scanner {runId}-026`
21. Verifikasi kolom Modified By entri tersebut `Budi S`
22. Klik `[×]` pada modal Changelog

### Parent otomatis ter-expand setelah Add (TC-64)

23. Hover node `Keluarga {runId}-026`, klik aksi `+ Subcategory`
24. Ketik `Pemindai Anak {runId}-026`, klik `[Submit]`
25. Verifikasi toast sukses "Success, category has been created."
26. Verifikasi node `Keluarga {runId}-026` ter-expand
27. Verifikasi node `Pemindai Anak {runId}-026` terlihat tanpa klik tambahan

### Toast sukses di kanan bawah dan hilang otomatis (TC-65)

28. Hover node `Induk {runId}-026`, klik aksi `+ Subcategory`
29. Ketik `Pemindai Meja {runId}-026`, klik `[Submit]`
30. Verifikasi toast berada di kanan bawah layar
31. Verifikasi toast sukses "Success, category has been created."
32. Tunggu 5 detik tanpa interaksi
33. Verifikasi toast sukses hilang sendiri

## Notes

- S-03, langkah penghubung: langkah 9 (Esc pada input bersih, tanpa dialog), langkah 22 (menutup modal Changelog). Search pada modal Changelog (langkah 19) menemukan entri berdasarkan nama bersuffix unik.
- Batas 4 detik toast (langkah 33) diamati lewat jendela 5 detik setelah toast terverifikasi tampil pada langkah 31.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 (`Rugged Scanner`, `Filter Induk`) sebagai induk Add dan Catatan TC menyebut automation baseline memulihkan data destruktif. Spec memakai node milik spec bersuffix `{runId}-026` sebagai induk dan hanya membaca node Pre-setup; teks asersi yang menyebut nama literal TC ditulis dengan nama bersuffix tersebut.
  - Post Condition TC-63 (nilai tersimpan dengan parent, opsi Category pada form Device Name, entri pada System Log dan Activity Log, konsumen read Device Allocation, Tag Stock, dan Hardware Stock) tidak diasersi karena TC tidak memberi langkah observasinya (S-01).
  - Kemampuan membuat node, menghapus node, dan Device Name lewat sesi API aktor tidak punya endpoint di TC; mekanismenya disediakan tim FE/BE tanpa endpoint karangan.
