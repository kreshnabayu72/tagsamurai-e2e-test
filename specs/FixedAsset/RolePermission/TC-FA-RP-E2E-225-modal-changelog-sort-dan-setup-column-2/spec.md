---
id: TC-FA-RP-E2E-225-modal-changelog-sort-dan-setup-column-2
title: "Modal Changelog: Sort dan Setup Column (2/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-735
  - TC-FA-RP-736
coverage:
  web: automated
---

# Modal Changelog: Sort dan Setup Column (2/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #42 (Changelog Tab Total Control, enam entri seed). Pre-setup #24 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Seeding enam entri seed #42 dijamin fixture backend yang disediakan tim FE/BE di hook `before`. Changelog adalah audit trail permanen yang tidak dipulihkan: entri lain dapat ada di antara entri seed. Spec ini tidak mengubah data.
- Konfigurasi kolom Setup Column disimpan di browser dan dipulihkan tiap iterasi dengan centang ulang; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- Tabel Kolom Hideable-tampil (TC 736): `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`, `Modified By`.

## Test Steps

### Screening popup Setup Column tiga zona (TC 735)

1. Klik ikon Changelog pada toolbar.
2. Klik header `(⋯)` kolom Column Visibility.
3. Klik `Setup Column...`.
4. Verifikasi zona Header: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, tombol `(X)`.
5. Verifikasi zona Body: daftar kolom dengan checkbox, drag handle, ikon Pin, dan Live Preview tabel.
6. Verifikasi zona Footer: tombol `[Reset to Default]` dan `[Save]` rata kanan; tidak ada `[Cancel]`.
7. Klik `(X)` untuk menutup popup Setup Column.

### Ceklis dan unceklis kolom Hideable-tampil (TC 736)

8. Untuk setiap kolom pada Tabel Kolom Hideable-tampil, lakukan langkah 9 sampai 18.
9. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`.
10. Hapus centang kolom.
11. Verifikasi Live Preview tidak lagi menampilkan kolom.
12. Klik `[Save]`.
13. Verifikasi tabel tidak menampilkan kolom.
14. Muat ulang halaman (F5), klik ikon Changelog pada toolbar kembali, lalu buka kembali popup Setup Column.
15. Verifikasi kolom tetap tidak tampil pada tabel.
16. Verifikasi checkbox kolom tidak tercentang.
17. Centang kembali kolom, lalu klik `[Save]`.
18. Verifikasi kolom tampil kembali pada tabel.
19. Tutup modal Changelog.

## Notes

- Alasan di atas 35 langkah: langkah 9 sampai 18 adalah blok berulang dengan parameter pada tabel Prerequisites (tujuh iterasi); seluruh blok berkelas fungsional sama, dataset sama, dan tiap iterasi berdiri sendiri karena centang dipulihkan di akhir iterasi. Langkah yang diulang: 9 sampai 18.
- Langkah penghubung (S-03): langkah 7 (menutup popup Setup Column tanpa menyimpan), 8 (kepala perulangan), dan 19 (menutup modal Changelog).
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 736 tidak menyebut apakah modal Changelog tetap terbuka sesudah `[Save]` Setup Column; spec mengasumsikan modal tetap terbuka dan tabel terlihat di belakang popup Setup Column.
