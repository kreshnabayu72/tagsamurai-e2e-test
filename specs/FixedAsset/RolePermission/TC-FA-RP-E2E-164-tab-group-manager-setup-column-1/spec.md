---
id: TC-FA-RP-E2E-164-tab-group-manager-setup-column-1
title: "Tab Group Manager: Setup Column (1/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-551
  - TC-FA-RP-552
  - TC-FA-RP-553
coverage:
  web: automated
---

# Tab Group Manager: Setup Column (1/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #38 (Tab Group Manager enam baris) dan #18 (pohon group). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser dan dipulihkan tiap iterasi dengan centang ulang; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- Tabel Kolom Hideable-tampil (TC-FA-RP-553): `Name`, `Group`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated`.

## Test Steps

### Overlay Column Visibility (TC-FA-RP-551)

1. Klik Tab `Group Manager`
2. Klik header `(⋯)` kolom Column Visibility
3. Verifikasi overlay memuat item `Setup Column...` di bagian bawah
4. Verifikasi kolom bawaan tampil tercentang aktif: `Name`, `Group`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated`
5. Verifikasi kolom curated tidak tercentang: `Email`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Cost Center`, `Joined Date`, `Badge No`
6. Verifikasi drag handle tersedia pada daftar

### Popup Setup Column tiga zona (TC-FA-RP-552)

7. Klik `Setup Column...`
8. Verifikasi zona Header: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, tombol `(X)`
9. Verifikasi zona Body: daftar kolom dengan checkbox, drag handle, ikon Pin, dan Live Preview tabel
10. Verifikasi zona Footer: tombol `[Reset to Default]` dan `[Save]` rata kanan; tidak ada `[Cancel]`
11. Klik `(X)` untuk menutup popup

### Ceklis dan unceklis kolom kelas Hideable-tampil (TC-FA-RP-553)

12. Untuk setiap baris pada Tabel Kolom Hideable-tampil, lakukan langkah 13 sampai 22
13. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
14. Hapus centang kolom
15. Verifikasi Live Preview tidak lagi menampilkan kolom
16. Klik `[Save]`
17. Verifikasi tabel tidak menampilkan kolom
18. Muat ulang halaman (F5), lalu buka kembali popup Setup Column
19. Verifikasi kolom tetap tidak tampil pada tabel
20. Verifikasi checkbox kolom tidak tercentang
21. Centang kembali kolom, lalu klik `[Save]`
22. Verifikasi kolom tampil kembali pada tabel

## Notes

- Alasan di atas 35 langkah (dengan ekspansi): langkah 13 sampai 22 adalah blok berulang dengan parameter pada Tabel Kolom Hideable-tampil (tujuh iterasi); nominal 22 langkah, ekspansi 82. Seluruh blok berkelas fungsional sama, dataset sama (Pre-setup #38), dan tiap iterasi berdiri sendiri karena centang dipulihkan di akhir iterasi. Langkah yang diulang: 13 sampai 22.
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab (langkah 1); membuka overlay dan popup (langkah 2, 7, 13); menutup popup dengan `(X)` (langkah 11); membuka kembali popup setelah F5 digabung pada langkah 18 sesuai TC.
- Temuan untuk QA:
  - TC-FA-RP-551 Expected b menyebut kolom bawaan tampil tercentang tanpa urutan; spec mengasersi himpunan kolom tanpa urutan.
  - TC-FA-RP-553 Expected tiap kolom tidak menyebut halaman tabel; Pre-setup #38 hanya enam baris sehingga seluruhnya satu halaman.
