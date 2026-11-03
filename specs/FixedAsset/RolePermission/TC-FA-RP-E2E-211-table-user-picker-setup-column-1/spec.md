---
id: TC-FA-RP-E2E-211-table-user-picker-setup-column-1
title: "Table User Picker: Setup Column (1/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-690
  - TC-FA-RP-691
  - TC-FA-RP-692
coverage:
  web: automated
---

# Table User Picker: Setup Column (1/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #41 (kandidat popup Assign Total Control, 12 kandidat: Citra Lestari, Dimas Pranata, Endah Susanti, Gunawan Halim, Hesti Rahma, Joko Santoso, Indra Kusuma, Dewi Anggraini, Maya Anggraeni, Yoga Pratama, Gilang Prakoso, Hana Permata). Pre-setup #36, #37, dan #17 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Spec ini tidak mengubah data; Pre-setup di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser dan dipulihkan tiap iterasi dengan centang ulang; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- Tabel Kolom Hideable-tampil (TC 692): `Name`, `Email`, `Position`, `Division`, `Status`.

## Test Steps

### Overlay Column Visibility (TC 690)

1. Klik `[+ Assign]`.
2. Klik header `(⋯)` kolom Column Visibility.
3. Verifikasi overlay memuat item `Setup Column...` di bagian bawah.
4. Verifikasi kolom bawaan tampil tercentang aktif: `Name`, `Email`, `Position`, `Division`, `Status`.
5. Verifikasi kolom curated tidak tercentang: `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Cost Center`, `Joined Date`, `Badge No`.
6. Verifikasi drag handle tersedia pada daftar.

### Popup Setup Column tiga zona (TC 691)

7. Klik `Setup Column...`.
8. Verifikasi zona Header: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, tombol `(X)`.
9. Verifikasi zona Body: daftar kolom dengan checkbox, drag handle, ikon Pin, dan Live Preview tabel.
10. Verifikasi zona Footer: tombol `[Reset to Default]` dan `[Save]` rata kanan; tidak ada `[Cancel]`.
11. Klik `(X)` untuk menutup popup Setup Column.

### Ceklis dan unceklis kolom Hideable-tampil (TC 692)

12. Untuk setiap kolom pada Tabel Kolom Hideable-tampil, lakukan langkah 13 sampai 22.
13. Klik header `(⋯)`, lalu klik `Setup Column...`.
14. Hapus centang kolom.
15. Verifikasi Live Preview tidak lagi menampilkan kolom.
16. Klik `[Save]`.
17. Verifikasi tabel tidak menampilkan kolom.
18. Muat ulang halaman (F5), klik `[+ Assign]` kembali, lalu buka kembali popup Setup Column.
19. Verifikasi kolom tetap tidak tampil pada tabel.
20. Verifikasi checkbox kolom tidak tercentang.
21. Centang kembali kolom, lalu klik `[Save]`.
22. Verifikasi kolom tampil kembali pada tabel.
23. Tutup popup Assign.

## Notes

- Alasan di atas 35 langkah: langkah 13 sampai 22 adalah blok berulang dengan parameter pada tabel Prerequisites (lima iterasi); seluruh blok berkelas fungsional sama, dataset sama, dan tiap iterasi berdiri sendiri karena centang dipulihkan di akhir iterasi. Langkah yang diulang: 13 sampai 22.
- Langkah penghubung (S-03): langkah 11 (menutup popup Setup Column tanpa menyimpan), 12 (kepala perulangan), dan 23 (menutup popup Assign).
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 692 tidak menyebut apakah popup Assign tetap terbuka sesudah `[Save]` Setup Column; spec mengasumsikan popup Assign tetap terbuka dan tabel kandidat terlihat di belakang popup Setup Column.
