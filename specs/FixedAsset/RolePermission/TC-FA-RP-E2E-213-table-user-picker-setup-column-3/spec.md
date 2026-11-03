---
id: TC-FA-RP-E2E-213-table-user-picker-setup-column-3
title: "Table User Picker: Setup Column (3/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-695
  - TC-FA-RP-696
coverage:
  web: automated
---

# Table User Picker: Setup Column (3/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #41 (kandidat popup Assign Total Control, 12 kandidat). Pre-setup #36, #37, dan #17 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Spec ini tidak mengubah data; Pre-setup di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser dan dipulihkan tiap iterasi dengan centang ulang; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- Tabel Kolom Curated-tersembunyi: `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Cost Center`, `Joined Date`, `Badge No`.

## Test Steps

### Ceklis dan unceklis kolom Curated-tersembunyi (TC 695)

1. Klik `[+ Assign]`.
2. Untuk setiap kolom pada Tabel Kolom Curated-tersembunyi, lakukan langkah 3 sampai 12.
3. Klik header `(⋯)`, lalu klik `Setup Column...`.
4. Centang kolom.
5. Verifikasi Live Preview menampilkan kolom.
6. Klik `[Save]`.
7. Verifikasi tabel menampilkan kolom.
8. Muat ulang halaman (F5), klik `[+ Assign]` kembali, lalu buka kembali popup Setup Column.
9. Verifikasi kolom tetap tampil pada tabel.
10. Verifikasi checkbox kolom tercentang.
11. Hapus centang kolom, lalu klik `[Save]`.
12. Verifikasi kolom tidak tampil lagi pada tabel.

### Geser urutan kolom Curated-tersembunyi (TC 696)

13. Untuk setiap kolom pada Tabel Kolom Curated-tersembunyi, lakukan langkah 14 sampai 20.
14. Klik header `(⋯)`, lalu klik `Setup Column...`.
15. Seret kolom ke posisi paling akhir pada daftar.
16. Verifikasi kolom berada di posisi paling akhir pada Live Preview.
17. Klik `[Save]`.
18. Verifikasi tabel memakai urutan kolom yang sama.
19. Muat ulang halaman (F5), klik `[+ Assign]` kembali, lalu buka kembali popup Setup Column.
20. Verifikasi urutan kolom tetap.
21. Klik `(X)` untuk menutup popup Setup Column.
22. Tutup popup Assign.

## Notes

- Alasan di atas 35 langkah: langkah 3 sampai 12 dan 14 sampai 20 adalah blok berulang dengan parameter pada tabel Prerequisites (tujuh iterasi tiap blok); seluruh blok berkelas fungsional sama, dataset sama, dan tiap iterasi berdiri sendiri karena centang dipulihkan di akhir iterasi TC 695. Langkah yang diulang: 3 sampai 12 dan 14 sampai 20.
- Langkah penghubung (S-03): langkah 2 dan 13 (kepala perulangan), 21 (menutup popup Setup Column tanpa menyimpan), dan 22 (menutup popup Assign). Urutan kolom hasil TC 696 tidak dipulihkan di dalam spec; hook `after` menghapus preferensi kolom.
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 695 dan 696 tidak menyebut apakah popup Assign tetap terbuka sesudah `[Save]` Setup Column; spec mengasumsikan popup Assign tetap terbuka.
  - TC 696 mengasersi posisi paling akhir pada Live Preview untuk kolom curated yang secara bawaan tidak tercentang, tanpa menyebut bahwa kolom lebih dulu ditampilkan; spec mengikuti TC.
