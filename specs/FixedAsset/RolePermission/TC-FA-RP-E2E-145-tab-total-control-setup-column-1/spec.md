---
id: TC-FA-RP-E2E-145-tab-total-control-setup-column-1
title: "Tab Total Control: Setup Column (1/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-503
  - TC-FA-RP-504
  - TC-FA-RP-505
coverage:
  web: automated
---

# Tab Total Control: Setup Column (1/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris) dan #37 (Tab Read Only empat baris). Spec ini tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser dan dipulihkan tiap iterasi dengan centang ulang; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- Tabel Kolom Hideable-tampil (TC 505): `Name`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated`.

## Test Steps

### Overlay Column Visibility (TC 503)

1. Klik header `(⋯)` kolom Column Visibility.
2. Verifikasi overlay memuat item `Setup Column...` di bagian bawah.
3. Verifikasi kolom bawaan tampil tercentang aktif: `Name`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated`.
4. Verifikasi kolom curated tidak tercentang: `Email`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Cost Center`, `Joined Date`, `Badge No`.
5. Verifikasi drag handle tersedia pada daftar.

### Popup Setup Column tiga zona (TC 504)

6. Klik `Setup Column...`.
7. Verifikasi zona Header: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, tombol `(X)`.
8. Verifikasi zona Body: daftar kolom dengan checkbox, drag handle, ikon Pin, dan Live Preview tabel.
9. Verifikasi zona Footer: tombol `[Reset to Default]` dan `[Save]` rata kanan; tidak ada `[Cancel]`.
10. Klik `(X)` untuk menutup popup.

### Ceklis dan unceklis kolom Hideable-tampil (TC 505)

11. Untuk setiap kolom pada Tabel Kolom Hideable-tampil, lakukan langkah 12 sampai 21.
12. Buka popup Setup Column.
13. Hapus centang kolom.
14. Verifikasi Live Preview tidak lagi menampilkan kolom.
15. Klik `[Save]`.
16. Verifikasi tabel tidak menampilkan kolom.
17. Muat ulang halaman (F5), lalu buka kembali popup Setup Column.
18. Verifikasi kolom tetap tidak tampil pada tabel.
19. Verifikasi checkbox kolom tidak tercentang.
20. Centang kembali kolom, lalu klik `[Save]`.
21. Verifikasi kolom tampil kembali pada tabel.
22. Klik Tab `Read Only`.
23. Untuk setiap kolom pada Tabel Kolom Hideable-tampil pada Tab Read Only, ulangi langkah 12 sampai 21 (hasil identik dengan Tab Total Control).
24. Klik Tab `Total Control`.

## Notes

- Alasan di atas 35 langkah: langkah 12 sampai 21 adalah blok berulang dengan parameter pada tabel Prerequisites (enam iterasi pada Tab Total Control dan enam pada Tab Read Only); seluruh blok berkelas fungsional sama, dataset sama, dan tiap iterasi berdiri sendiri karena centang dipulihkan di akhir iterasi. Langkah yang diulang: 12 sampai 21.
- Langkah penghubung (S-03): langkah 1, 6, 10, 11, 12, 13, 15, 17, 20, 22, 23, dan 24. Langkah 10 menutup popup tanpa menyimpan; langkah 22 dan 24 berpindah tab; langkah 17 menggabungkan F5 dan pembukaan ulang popup sesuai TC.
- Langkah 11 dan 23 tidak menambah asersi; asersi tiap iterasi ada di langkah 14, 16, 18, 19, dan 21 (S-01: satu `Verifikasi` per klausa Expected a sampai f dan g).
- Temuan untuk QA:
  - Label overlay Column Visibility pada TC 503 menyebut daftar kolom bawaan tercentang tetapi tidak menyebut urutan; spec mengasersi himpunan kolom tanpa urutan.
