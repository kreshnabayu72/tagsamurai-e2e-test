---
id: TC-FA-RP-E2E-166-tab-group-manager-setup-column-3
title: "Tab Group Manager: Setup Column (3/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-556
  - TC-FA-RP-557
coverage:
  web: automated
---

# Tab Group Manager: Setup Column (3/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #38 (Tab Group Manager enam baris) dan #18 (pohon group). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- Tabel Kolom curated-tersembunyi (TC-FA-RP-556 dan TC-FA-RP-557): `Email`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`.

## Test Steps

### Ceklis dan unceklis kolom kelas Curated-tersembunyi (TC-FA-RP-556)

1. Klik Tab `Group Manager`
2. Untuk setiap baris pada Tabel Kolom curated-tersembunyi, lakukan langkah 3 sampai 12
3. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
4. Centang kolom
5. Verifikasi Live Preview menampilkan kolom
6. Klik `[Save]`
7. Verifikasi tabel menampilkan kolom
8. Muat ulang halaman (F5), lalu buka kembali popup Setup Column
9. Verifikasi kolom tetap tampil pada tabel
10. Verifikasi checkbox kolom tercentang
11. Hapus centang kolom, lalu klik `[Save]`
12. Verifikasi kolom tidak tampil lagi pada tabel

### Geser urutan kolom kelas Curated-tersembunyi (TC-FA-RP-557)

13. Untuk setiap baris pada Tabel Kolom curated-tersembunyi, lakukan langkah 14 sampai 21
14. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
15. Centang kolom agar tampil pada Live Preview
16. Seret kolom ke posisi paling akhir pada daftar
17. Verifikasi kolom berada di posisi paling akhir pada Live Preview
18. Klik `[Save]`
19. Verifikasi tabel memakai urutan kolom yang sama dengan Live Preview
20. Muat ulang halaman (F5)
21. Verifikasi urutan kolom tetap

## Notes

- Alasan di atas 35 langkah (dengan ekspansi): langkah 3 sampai 12 dan 14 sampai 21 adalah blok berulang dengan parameter pada Tabel Kolom curated-tersembunyi (lima iterasi tiap blok); nominal 21 langkah, ekspansi 2 + 5 x 10 + 1 + 5 x 8 = 93. Seluruh blok berkelas fungsional sama, dataset sama (Pre-setup #38), dan tiap iterasi berdiri sendiri. Langkah yang diulang: 3 sampai 12 dan 14 sampai 21.
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab (langkah 1); membuka popup (langkah 3, 14); langkah 15 mencentang kolom agar tampil sebelum diseret; langkah 16 menyeret kolom.
- Temuan untuk QA:
  - TC-FA-RP-556 Expected tiap kolom tidak menyebut halaman tabel; Pre-setup #38 hanya enam baris sehingga seluruhnya satu halaman.
