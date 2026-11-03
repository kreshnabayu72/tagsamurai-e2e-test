---
id: TC-AC-SG-E2E-058-overlay-column-visibility-hide-unhide-kolom-terakhir-dan-reorder
title: "Overlay Column Visibility Tabel Utama: Hide dan Unhide, Kolom Terakhir, dan Reorder"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-210
  - TC-AC-SG-211
  - TC-AC-SG-212
  - TC-AC-SG-213
coverage:
  web: automated
---

# Overlay Column Visibility Tabel Utama: Hide dan Unhide, Kolom Terakhir, dan Reorder

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16), node `All Groups` terpilih, 14 group.
- Kelima kolom data (Group, Total User, Total Member, Modified By, Last Updated) tampil secara default dengan urutan bawaan. Spec ini mengubah visibilitas dan urutan kolom di browser: hook `before` dan `after` spec ini menghapus preferensi kolom tabel di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE; lihat `suite.md`).
- Kemampuan teknis: Fixture BE untuk baseline `Pohon Uji Utama`, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-AC-SG-210: Overlay Column Visibility dari header kolom Actions

1. Hover header kolom Actions
2. Verifikasi tooltip `Column Visibility` tampil
3. Verifikasi ikon header kolom Actions tampil untuk aktor Total Control
4. Klik header kolom Actions `⋯`
5. Verifikasi Overlay Column Visibility memuat checkbox untuk Group, Total User, Total Member, Modified By, dan Last Updated, semuanya tercentang
6. Verifikasi tiap item kolom memiliki handle drag
7. Verifikasi item `Setup Column...` tampil di bagian bawah panel

### TC-AC-SG-211: Hide dan unhide kolom lewat Overlay Column Visibility ter-apply langsung

8. Hapus centang kolom Total Member
9. Verifikasi kolom Total Member hilang dari tabel seketika
10. Verifikasi Overlay Column Visibility tidak memiliki tombol `[Save]`
11. Tutup Overlay Column Visibility
12. Klik header kolom Actions `⋯`
13. Centang kembali kolom Total Member
14. Verifikasi kolom Total Member tampil lagi di tabel

### TC-AC-SG-212: Kolom visible terakhir tidak dapat di-uncheck

15. Hapus centang Group, Total User, Total Member, dan Modified By
16. Hover checkbox Last Updated
17. Verifikasi checkbox Last Updated disabled dengan tooltip `At least one column must remain visible.`
18. Verifikasi tabel tetap menampilkan kolom Last Updated
19. Centang kembali Group, Total User, Total Member, dan Modified By

### TC-AC-SG-213: Reorder kolom lewat drag di Overlay Column Visibility

20. Seret kolom Modified By ke posisi paling atas pada daftar panel
21. Verifikasi urutan di panel: Modified By di posisi paling atas
22. Verifikasi urutan di tabel: Modified By menjadi kolom data pertama (setelah Checkbox)

## Notes

- Langkah penghubung (S-03): langkah 11 (menutup overlay setelah hide, bagian dari "Tutup panel" TC-211), langkah 12 dan 13 (centang kembali), langkah 19 (memulihkan kolom yang di-hide sebelum TC-213, S-09). Overlay tetap terbuka dari langkah 12 sampai akhir sehingga langkah "Klik header kolom Actions" TC-212 dan TC-213 tidak diulang.
- Langkah 3: TC-210 Expected b menyebut "untuk semua aktor berakses"; spec ini hanya mengasersi aktor Total Control, aktor lain diuji spec Role Matrix.
- Langkah 9 diasersi sebelum overlay ditutup (bagian 8b butir 5: Expected "seketika").
- Temuan untuk QA:
  - TC-AC-SG-211: Expected "tanpa tombol Save" tidak memiliki langkah observasi tersendiri; spec mengamati overlay sesudah langkah 8.
