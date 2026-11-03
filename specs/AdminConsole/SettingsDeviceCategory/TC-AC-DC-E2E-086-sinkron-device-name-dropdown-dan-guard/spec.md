---
id: TC-AC-DC-E2E-086-sinkron-device-name-dropdown-dan-guard
title: "Sinkron Category dengan Device Name: Semantik Dropdown, Filter Parent pada Device SKU, dan Guard Delete"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-234
  - TC-AC-DC-293
  - TC-AC-DC-300
  - TC-AC-DC-235
  - TC-AC-DC-236
coverage:
  web: automated
---

# Sinkron Category dengan Device Name: Semantik Dropdown, Filter Parent pada Device SKU, dan Guard Delete

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control #1 (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Budi Santoso), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture backend (disediakan tim FE/BE; endpoint tidak dikarang di spec ini). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: pohon Pre-setup #14 (`Hardware` > `Handheld Reader`) hanya dibaca sebagai induk node milik spec dan tidak diubah. Device Name Pre-setup #15 dan Device SKU Pre-setup #16 tidak diubah.
- Data Dinamis (suffix `{runId}-086`), dibuat lewat sesi API aktor di hook `before` di bawah `Handheld Reader`:
  - TC-AC-DC-234: `Pilih Uji {runId}-086` (leaf).
  - TC-AC-DC-293: `Induk Pilih {runId}-086` dengan dua anak leaf `Anak Pilih A {runId}-086` dan `Anak Pilih B {runId}-086`.
  - TC-AC-DC-300: `Filter Induk {runId}-086` dengan anak `Anak 1 Filter {runId}-086` (leaf), `Anak 2 Filter {runId}-086` (memiliki anak `Cucu Filter {runId}-086`), dan `Anak 3 Filter {runId}-086` (leaf); Device Name `FN-1 {runId}-086` (Category `Anak 1 Filter {runId}-086`), `FN-2 {runId}-086` (Category `Cucu Filter {runId}-086`), `FN-3 {runId}-086` (Category `Anak 3 Filter {runId}-086`); Device SKU `SKU-FN-1 {runId}-086`, `SKU-FN-2 {runId}-086`, `SKU-FN-3 {runId}-086` masing-masing pada `FN-1`, `FN-2`, `FN-3` bersuffix itu.
  - TC-AC-DC-235: `Hapus Uji {runId}-086` (leaf, target Delete yang diblok). Device Name `GUARD {runId}-086` dibuat spec lewat UI (langkah 21 sampai 24).
  - TC-AC-DC-236: `Dipakai Uji {runId}-086` (leaf) dan Device Name `HR-Uji {runId}-086` dengan Category `Dipakai Uji {runId}-086`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh; urutan: Device SKU, Device Name, lalu node): hapus lewat API semua Device SKU, Device Name (`GUARD {runId}-086`, `FN-1`, `FN-2`, `FN-3`, `HR-Uji` bersuffix) dan node bersuffix `{runId}-086` di atas bila masih ada.
- Kemampuan teknis (disediakan tim FE/BE; tanpa endpoint karangan): field wajib popup Create Device Name selain Name dan Category tidak disebut TC dan disediakan tim FE; kemampuan membedakan node non-selectable pada dropdown Category (atribut yang dapat diamati) disediakan tim FE.
- State global: tidak ada yang diubah.

## Test Steps

### TC-AC-DC-234: Dropdown Category Device Name: Hardware dan TAG tidak dapat dipilih, node lain dapat dipilih

1. Klik `+ Device Name` pada toolbar, buka dropdown Category, lalu expand `Hardware` dan `Handheld Reader` pada dropdown
2. Verifikasi `Hardware` dan `TAG` tampil non-selectable dan tidak dapat dipilih sebagai Category
3. Klik node `Pilih Uji {runId}-086` pada dropdown
4. Verifikasi field Category menampilkan "Pilih Uji {runId}-086" (node user-created dapat dipilih)

### TC-AC-DC-293: Dropdown Category Device Name: node yang punya anak dapat dipilih

5. Buka dropdown Category, lalu expand `Hardware` dan `Handheld Reader` pada dropdown
6. Klik node `Induk Pilih {runId}-086` yang punya anak
7. Verifikasi field Category menampilkan "Induk Pilih {runId}-086"
8. Verifikasi dropdown Category tertutup
9. Klik `[Clear Field]`
10. Tutup popup Create Device Name lewat `[×]`

### TC-AC-DC-300: Filter parent partial-check dan tercentang penuh pada daftar Device SKU

11. Pindah ke sub-tab `Device SKU`
12. Expand `Hardware`, `Handheld Reader`, dan `Filter Induk {runId}-086`
13. Klik node `Anak 1 Filter {runId}-086`
14. Verifikasi tabel Device SKU hanya menampilkan `SKU-FN-1 {runId}-086`
15. Verifikasi `Filter Induk {runId}-086` berstatus partial-check
16. Klik kotak `Filter Induk {runId}-086` yang partial-check
17. Verifikasi `Filter Induk {runId}-086` dan seluruh descendant-nya tercentang
18. Verifikasi tabel Device SKU menampilkan `SKU-FN-1 {runId}-086`, `SKU-FN-2 {runId}-086`, dan `SKU-FN-3 {runId}-086`

### TC-AC-DC-235: Device Name yang baru dibuat memblok Delete Category yang dirujuknya

19. Pindah ke sub-tab `Device Name`
20. Klik `+ Device Name` pada toolbar
21. Ketik Name "GUARD {runId}-086"
22. Buka dropdown Category, lalu expand `Hardware` dan `Handheld Reader` pada dropdown
23. Klik node `Hapus Uji {runId}-086` pada dropdown
24. Klik `[Submit]`
25. Expand `Hardware`, lalu expand `Handheld Reader` pada Sidebar Category
26. Hover node `Hapus Uji {runId}-086`, lalu klik aksi Delete
27. Verifikasi dialog blok "Cannot Delete Category" memuat bullet `GUARD {runId}-086` dan satu tombol `[OK]`
28. Klik `[OK]`
29. Verifikasi `Hapus Uji {runId}-086` tidak terhapus dan tetap tampil di Sidebar Category

### TC-AC-DC-236: Setelah Device Name pengacu dihapus, Delete Category berhasil

30. Ketik Search tabel Device Name `HR-Uji {runId}-086`, tekan Enter
31. Hapus Device Name `HR-Uji {runId}-086` dari tabel Device Name
32. Hover node `Dipakai Uji {runId}-086`, lalu klik aksi Delete
33. Verifikasi dialog konfirmasi "Delete Category" tampil (bukan dialog blok)
34. Klik `[Delete]` pada dialog konfirmasi
35. Verifikasi toast sukses "Success, category has been deleted."
36. Verifikasi `Dipakai Uji {runId}-086` terhapus dari Sidebar Category

## Notes

- Alasan 36 langkah (di atas sekitar 35): kelima blok memakai data milik tiap blok sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; semuanya menguji integrasi Category dengan Device Name dan Device SKU.
- Langkah penghubung (S-03): langkah 9 dan 10 (membersihkan dan menutup popup yang berisi pilihan Category sebelum blok berikutnya, S-09), langkah 11 dan 19 (pindah sub-tab yang diminta TC), langkah 25 (membuka cabang tree pada sidebar setelah pindah sub-tab), dan Search pada langkah 30 (menemukan baris Device Name target, R-16).
- Filter Category yang dipilih pada langkah 13 sampai 18 berlaku di halaman Device SKU dan tidak dipakai blok berikutnya yang berada di sub-tab Device Name. Search tabel Device Name pada langkah 30 tidak dipakai langkah sesudahnya.
- Anchor absence (bagian 8b butir 2): langkah 29 membuktikan sidebar termuat sebelum asersi yang bergantung padanya; pada langkah 36 toast sukses (langkah 35) menjadi anchor untuk node yang hilang.
- Pembagian TC lintas spec: Rename, node baru, dan node dihapus ada di spec 085; filter Category dasar dan Add lewat Device SKU ada di spec lain suite ini.
- Temuan untuk QA:
  - TC-AC-DC-234 Expected a ("tidak dapat dipilih") tidak menyebut cara membuktikannya. Spec mengasersi state non-selectable pada node `Hardware` dan `TAG` (atribut yang dapat diamati disediakan tim FE) tanpa mengklik node tersebut, karena klik pada node induk dapat mengubah state expand.
  - TC-AC-DC-235 langkah 2 ("buat Device Name `GUARD-1` dengan Category `Hapus Daun` lewat popup Create Device Name") tidak menyebut field wajib Device Name selain Category; nilai itu disediakan tim FE. Langkah 4 TC menyebut "dialog konfirmasi tampil" padahal Expected-nya dialog blok; spec mengikuti Expected.
  - TC-AC-DC-236 langkah 2 ("hapus `HR-100` dari tabel Device Name") tidak menyebut aksi baris dan dialog konfirmasi Device Name milik modul lain; spec menulis satu langkah.
  - TC memakai node, Device Name, dan Device SKU literal Pre-setup (#14, #15, #16: `Dipakai Leaf`, `Hapus Daun`, `Industrial Scanner`, `Filter Induk`, `SKU-FN-1`); spec memakai data bersuffix milik spec (keputusan data tulis).
