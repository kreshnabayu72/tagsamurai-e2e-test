---
id: TC-AC-DC-E2E-008-filter-category-pilihan-node
title: "Filter Category pada Device Name: Pilih Node Leaf, Parent, Node Tengah, Dua Cabang, Pilihan Kosong, Handheld Reader, dan Node Tanpa Data"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-22
  - TC-AC-DC-23
  - TC-AC-DC-24
  - TC-AC-DC-26
  - TC-AC-DC-27
  - TC-AC-DC-28
  - TC-AC-DC-35
coverage:
  web: automated
---

# Filter Category pada Device Name: Pilih Node Leaf, Parent, Node Tengah, Dua Cabang, Pilihan Kosong, Handheld Reader, dan Node Tanpa Data

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup #14 (Pohon Uji Kategori) dan #15 (Device Name: `HR-100`, `TS-200`, `TS-210`, `FN-1`, `FN-2`, `FN-3`, `RB-01` sampai `RB-12`; 18 Device Name pada descendant `Handheld Reader`) hanya dibaca; spec tidak membuat, mengubah, atau menghapus data tersebut. Nilai literal diacu lewat `Fixture.settingsDeviceCategory.<kunci>` (`fixtures/settings-device-category.json`, belum ada; ditandai untuk tahap script).
- Device Name `IND-1` (Pre-setup Dinamis #6) tidak ada saat spec ini berjalan; Device Name itu hanya dibuat oleh spec 011 dan 012 dan dihapus oleh hook `after` spec tersebut.
- Pemulihan pohon ke keadaan Pre-setup #14 dijamin kemampuan fixture backend yang disediakan tim FE/BE (lihat `suite.md`).
- State yang diubah spec: pilihan filter Category (tersimpan per user); dikosongkan lewat `All Categories` setelah tiap TC dan oleh hook `after` sebagai cadangan.
- Kondisi awal tiap spec: halaman baru dibuka hook `beforeEach`, sehingga `Hardware` dan `TAG` collapsed, tidak ada pilihan filter Category, dan kotak pencarian tree kosong.
- Suite berjalan serial (`parallel: false`). Env var `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DC-22: Memilih node leaf menyaring tabel Device Name sesuai relasi langsung

1. Catat total baris tabel Device Name pada footer pagination (tanpa filter Category)
2. Expand `Hardware`, `Handheld Reader`, dan `Filter Induk`
3. Klik node `Filter Anak 1`
4. Verifikasi tabel Device Name hanya menampilkan `FN-1`
5. Verifikasi node `Filter Anak 1` tercentang dan tersorot
6. Verifikasi `Filter Induk` menampilkan partial-check
7. Klik baris `All Categories`

### TC-AC-DC-23: Memilih parent menyaring recursive-inclusive seluruh descendant tiga level

8. Centang kotak `Filter Induk`
9. Verifikasi tabel menampilkan tepat `FN-1` (pada `Filter Anak 1`), `FN-2` (pada `Filter Cucu` di bawah `Filter Anak 2`), dan `FN-3` (pada `Filter Anak 3`)
10. Verifikasi Device Name milik node lain (`HR-100`) tidak tampil
11. Verifikasi `Filter Induk` berstatus tercentang
12. Verifikasi `Handheld Reader` dan `Hardware` berstatus partial-check
13. Klik baris `All Categories`

### TC-AC-DC-24: Memilih node tengah menyaring descendant lebih dalam tanpa mengikutkan sibling

14. Centang kotak `Filter Anak 2`
15. Verifikasi tabel hanya menampilkan `FN-2` (Device Name pada `Filter Cucu`)
16. Verifikasi `FN-1` dan `FN-3` tidak tampil
17. Verifikasi `Filter Induk` berstatus partial-check
18. Klik baris `All Categories`

### TC-AC-DC-26: Memilih dua node berbeda cabang menampilkan gabungan datanya

19. Klik node `Dipakai Leaf`
20. Klik node `Filter Anak 1`
21. Verifikasi tabel menampilkan `HR-100` dan `FN-1` saja
22. Klik baris `All Categories`

### TC-AC-DC-27: Pilihan kosong menampilkan seluruh data

23. Klik node `Filter Anak 1`
24. Klik node `Filter Anak 1` lagi untuk membatalkan centang
25. Verifikasi tabel kembali menampilkan seluruh Device Name (total baris sama dengan catatan langkah 1)
26. Verifikasi tidak ada node berstatus tercentang atau partial-check

### TC-AC-DC-28: Node hardcoded perantara Handheld Reader selectable dan mencakup seluruh descendant

27. Centang kotak `Handheld Reader`
28. Verifikasi node `Handheld Reader` tercentang (selectable statis)
29. Verifikasi tabel menampilkan semua Device Name milik seluruh descendant `Handheld Reader` (`HR-100`, `TS-200`, `TS-210`, `FN-1`, `FN-2`, `FN-3`, dan `RB-01` sampai `RB-12`; total 18 baris pada footer pagination)
30. Klik baris `All Categories`

### TC-AC-DC-35: Pilihan node tanpa data menampilkan empty state Device Name untuk filter Category

31. Klik node `Hapus Daun` (tidak dirujuk Device Name mana pun)
32. Verifikasi tabel Device Name menampilkan empty state dengan ilustrasi, judul "No results found", dan deskripsi "Try adjusting your search or filter."
33. Verifikasi node `Hapus Daun` tetap tercentang
34. Klik baris `All Categories`

## Notes

- Langkah penghubung (S-03): klik `All Categories` (langkah 7, 13, 18, 22, 30, 34) melepas pilihan filter sebelum TC berikutnya (S-09); langkah 1 mencatat baseline untuk asersi "seluruh Device Name" (langkah 25).
- Node `Hapus Daun` pada TC-AC-DC-35 hanya diklik sebagai pilihan filter (dibaca); spec tidak menghapusnya (S-06).
- Spec ini sampai 34 langkah; tidak melewati batas sekitar 35 langkah.
- Temuan untuk QA: (1) Ukuran halaman default tabel Device Name tidak ditulis di TC; untuk 18 baris (TC-AC-DC-28) asersi memakai total pada footer pagination, bukan seluruh baris dalam satu halaman. (2) Asersi tabel bergantung pada Device Name literal Pre-setup #15 (`FN-1`, `HR-100`, dan seterusnya); bila nama literal itu berubah di lingkungan, asersi gagal tanpa dapat dibentuk ulang lewat spec ini karena nama literal dibaca saja.
