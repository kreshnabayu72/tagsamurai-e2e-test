---
id: TC-AC-DC-E2E-012-filter-category-tri-state-bottom-up
title: "Filter Category Tri-State Bottom-Up: Parent Tercentang Penuh bila Seluruh Anak Dipilih dan Node ber-Device Name yang Mendapat Anak"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-297
  - TC-AC-DC-298
  - TC-AC-DC-301
coverage:
  web: automated
---

# Filter Category Tri-State Bottom-Up: Parent Tercentang Penuh bila Seluruh Anak Dipilih dan Node ber-Device Name yang Mendapat Anak

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup #14 (Pohon Uji Kategori) dan #15 (Device Name `FN-1`, `FN-2`, `FN-3`, `TS-200`, `TS-210`) hanya dibaca; spec tidak membuat, mengubah, atau menghapus data tersebut. Nilai literal diacu lewat `Fixture.settingsDeviceCategory.<kunci>` (`fixtures/settings-device-category.json`, belum ada; ditandai untuk tahap script).
- Data Dinamis milik spec (dibuat lewat sesi API aktor oleh hook `before`; kemampuan disediakan tim BE/FE, nilai field wajib Device Name lain disediakan tim FE; dihapus lewat API oleh hook `after` tanpa mengasumsikan setup berhasil penuh):
  - Node `Dipakai Leaf {runId}-012` (leaf di bawah `Handheld Reader`) dengan Device Name `HR-{runId}-012` (Category node itu); target aksi Add Subcategory pada TC-AC-DC-298 (pengganti `Dipakai Leaf` Pre-setup, S-06).
  - Node anak `Anak Parent {runId}-012` dibuat lewat UI pada TC-AC-DC-298 dan dihapus oleh hook `after`.
  - Device Name `IND-1-{runId}-012` dengan Category `Industrial Scanner` (node Pre-setup yang punya anak) dibuat lewat API pada langkah 22 (Pre-setup Dinamis #6).
- Pemulihan pohon ke keadaan Pre-setup #14 dijamin kemampuan fixture backend yang disediakan tim FE/BE (lihat `suite.md`).
- State yang diubah spec: pilihan filter Category (tersimpan per user); dikosongkan lewat `All Categories` setelah tiap TC dan oleh hook `after` sebagai cadangan.
- Kondisi awal tiap spec: halaman baru dibuka hook `beforeEach`, sehingga `Hardware` dan `TAG` collapsed, tidak ada pilihan filter Category, dan kotak pencarian tree kosong.
- Suite berjalan serial (`parallel: false`). Env var `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DC-297: Parent berstatus tercentang penuh bila seluruh descendant dipilih satu per satu

1. Expand `Hardware`, `Handheld Reader`, `Filter Induk`, dan `Filter Anak 2`
2. Klik node `Filter Anak 1`
3. Klik node `Filter Cucu`
4. Verifikasi `Filter Anak 2` tercentang penuh
5. Verifikasi `Filter Induk` partial-check
6. Klik node `Filter Anak 3`
7. Verifikasi `Filter Induk` berstatus tercentang penuh
8. Verifikasi tabel Device Name menampilkan `FN-1`, `FN-2`, dan `FN-3`
9. Klik baris `All Categories`

### TC-AC-DC-298: Node ber-Device Name sendiri yang mendapat anak menjadi tidak tercentang sehingga Device Name-nya tidak tampil

10. Catat total baris tabel Device Name pada footer pagination (tanpa filter Category)
11. Centang kotak `Dipakai Leaf {runId}-012` dan kotak `Filter Anak 1`
12. Verifikasi tabel menampilkan `HR-{runId}-012` dan `FN-1`
13. Hover node `Dipakai Leaf {runId}-012`
14. Klik aksi `+ Subcategory`
15. Ketik `Anak Parent {runId}-012` pada input inline Add
16. Klik `[Submit]`
17. Verifikasi `Anak Parent {runId}-012` muncul di bawah `Dipakai Leaf {runId}-012` dalam keadaan tidak tercentang
18. Verifikasi `Dipakai Leaf {runId}-012` menjadi tidak tercentang (tidak ada descendant-nya yang terpilih)
19. Verifikasi tabel hanya menampilkan `FN-1` dan `HR-{runId}-012` tidak tampil
20. Hapus centang `Filter Anak 1`
21. Verifikasi tidak ada node tercentang dan tabel menampilkan seluruh Device Name (total baris sama dengan catatan langkah 10)

### TC-AC-DC-301: Parent menjadi tercentang penuh setelah kedua anak dipilih satu per satu dan menampilkan Device Name milik parent

22. Buat Device Name `IND-1-{runId}-012` dengan Category `Industrial Scanner` lewat sesi API aktor hingga tersimpan, lalu muat ulang halaman dengan F5
23. Expand `Hardware`, `Handheld Reader`, dan `Industrial Scanner`
24. Centang kotak `Rugged`
25. Verifikasi `Industrial Scanner` partial-check
26. Verifikasi tabel hanya menampilkan `TS-200`
27. Centang kotak `Rugged Kit`
28. Verifikasi `Industrial Scanner` berstatus tercentang penuh
29. Verifikasi tabel menampilkan `IND-1-{runId}-012`, `TS-200`, dan `TS-210`
30. Klik baris `All Categories`

## Notes

- Urutan TC dalam spec: TC-AC-DC-297, 298, 301. TC-AC-DC-301 dijalankan terakhir karena Device Name `IND-1` hanya boleh ada pada TC itu (Pre-setup Dinamis #6); dibuat pada langkah 22 sebelum TC-AC-DC-301 (S-10).
- Langkah penghubung (S-03): langkah 10 mencatat baseline; `All Categories` (langkah 9, 30) melepas pilihan (S-09); langkah 22 memuat ulang halaman agar tree dan tabel memuat Device Name baru dan state expand kembali ke kondisi awal; setelah langkah 16 node `Anak Parent {runId}-012` tetap ada sampai dihapus hook `after`.
- Temuan untuk QA: (1) TC-AC-DC-298 memakai `Dipakai Leaf` Pre-setup (Device Name `HR-100`) sebagai target aksi tulis Add Subcategory; spec memakai node bersuffix milik sendiri dan Device Name `HR-{runId}-012`, sehingga asersi "tabel `HR-100`" ditulis dengan nama bersuffix. Node `Anak Parent` juga bersuffix. (2) Data Dinamis #6 menyebut `IND-1` dibuat automation baseline; spec membuat Device Name milik sendiri bersuffix. (3) Sort alfabet node bersuffix `Dipakai Leaf {runId}-012` jatuh setelah `Dipakai Leaf`; posisi relatif dibaca dari tree, tidak diasersi.
