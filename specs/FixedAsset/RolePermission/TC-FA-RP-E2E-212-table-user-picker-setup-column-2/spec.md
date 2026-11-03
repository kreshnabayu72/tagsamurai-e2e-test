---
id: TC-FA-RP-E2E-212-table-user-picker-setup-column-2
title: "Table User Picker: Setup Column (2/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-693
  - TC-FA-RP-694
coverage:
  web: automated
---

# Table User Picker: Setup Column (2/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #41 (kandidat popup Assign Total Control, 12 kandidat). Pre-setup #36, #37, dan #17 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Spec ini tidak mengubah data; Pre-setup di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser; urutan dan pin kolom dipulihkan di akhir tiap iterasi pin, dan hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- Tabel Kolom Hideable-tampil: `Name`, `Email`, `Position`, `Division`, `Status`.

## Test Steps

### Geser urutan kolom Hideable-tampil (TC 693)

1. Klik `[+ Assign]`.
2. Untuk setiap kolom pada Tabel Kolom Hideable-tampil, lakukan langkah 3 sampai 9.
3. Klik header `(⋯)`, lalu klik `Setup Column...`.
4. Seret kolom ke posisi paling akhir pada daftar.
5. Verifikasi kolom berada di posisi paling akhir pada Live Preview.
6. Klik `[Save]`.
7. Verifikasi tabel memakai urutan kolom yang sama.
8. Muat ulang halaman (F5), klik `[+ Assign]` kembali, lalu buka kembali popup Setup Column.
9. Verifikasi urutan kolom tetap.
10. Klik `(X)` untuk menutup popup Setup Column.

### Pin dan unpin kolom Hideable-tampil (TC 694)

11. Untuk setiap kolom pada Tabel Kolom Hideable-tampil, lakukan langkah 12 sampai 23.
12. Klik header `(⋯)`, lalu klik `Setup Column...`.
13. Klik ikon Pin pada kolom.
14. Verifikasi ikon Pin aktif pada Live Preview.
15. Klik `[Save]`.
16. Scroll tabel horizontal.
17. Verifikasi kolom membeku (sticky).
18. Muat ulang halaman (F5), lalu klik `[+ Assign]` kembali.
19. Buka popup Setup Column.
20. Verifikasi kolom tetap ter-pin.
21. Klik ikon Pin kolom itu lagi, lalu klik `[Save]`.
22. Scroll tabel horizontal.
23. Verifikasi pembekuan terlepas.
24. Tutup popup Assign.

## Notes

- Alasan di atas 35 langkah: langkah 3 sampai 9 dan 12 sampai 23 adalah blok berulang dengan parameter pada tabel Prerequisites (lima iterasi tiap blok); seluruh blok berkelas fungsional sama, dataset sama, dan tiap iterasi berdiri sendiri karena pin dilepas di akhir iterasi. Langkah yang diulang: 3 sampai 9 dan 12 sampai 23.
- Langkah penghubung (S-03): langkah 2 dan 11 (kepala perulangan), 10 (menutup popup Setup Column tanpa menyimpan), 22 (scroll untuk mengamati pembekuan terlepas, S-14), dan 24 (menutup popup Assign). Urutan kolom hasil TC 693 tidak dipulihkan karena TC 694 tidak bergantung pada urutan; hook `after` menghapus preferensi kolom.
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 693 dan 694 tidak menyebut apakah popup Assign tetap terbuka sesudah `[Save]` Setup Column; spec mengasumsikan popup Assign tetap terbuka.
