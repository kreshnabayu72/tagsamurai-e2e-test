---
id: TC-FA-RP-E2E-147-tab-total-control-setup-column-3
title: "Tab Total Control: Setup Column (3/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-508
  - TC-FA-RP-509
coverage:
  web: automated
---

# Tab Total Control: Setup Column (3/5)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris), #37 (Tab Read Only empat baris), #22 (Custom Field `Cost Center`, `Joined Date`, `Badge No`). Spec ini tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column (centang dan urutan) disimpan di browser; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- Tabel Kolom Curated-tersembunyi: `Email`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Cost Center`, `Joined Date`, `Badge No`.

## Test Steps

### Ceklis dan unceklis kolom Curated-tersembunyi (TC 508)

1. Untuk setiap kolom pada Tabel Kolom Curated-tersembunyi, lakukan langkah 2 sampai 11.
2. Buka popup Setup Column.
3. Centang kolom.
4. Verifikasi Live Preview menampilkan kolom.
5. Klik `[Save]`.
6. Verifikasi tabel menampilkan kolom.
7. Muat ulang halaman (F5), lalu buka kembali popup Setup Column.
8. Verifikasi kolom tetap tampil pada tabel.
9. Verifikasi checkbox kolom tercentang.
10. Hapus centang kolom, lalu klik `[Save]`.
11. Verifikasi kolom tidak tampil lagi pada tabel.
12. Klik Tab `Read Only`.
13. Untuk setiap kolom pada Tabel Kolom Curated-tersembunyi pada Tab Read Only, ulangi langkah 2 sampai 11 (hasil identik dengan Tab Total Control).

### Geser urutan kolom Curated-tersembunyi (TC 509)

14. Klik Tab `Total Control`.
15. Untuk setiap kolom pada Tabel Kolom Curated-tersembunyi, lakukan langkah 16 sampai 24.
16. Buka popup Setup Column.
17. Centang kolom.
18. Seret kolom ke posisi paling akhir pada daftar.
19. Verifikasi kolom berada di posisi paling akhir pada Live Preview.
20. Klik `[Save]`.
21. Verifikasi tabel memakai urutan kolom yang sama dengan Live Preview.
22. Muat ulang halaman (F5).
23. Verifikasi urutan kolom tabel tetap.
24. Buka popup Setup Column, hapus centang kolom, lalu klik `[Save]`.
25. Klik Tab `Read Only`.
26. Untuk setiap kolom pada Tabel Kolom Curated-tersembunyi pada Tab Read Only, ulangi langkah 16 sampai 24 (hasil identik dengan Tab Total Control).

## Notes

- Alasan di atas 35 langkah: langkah 2 sampai 11 dan langkah 16 sampai 24 adalah blok berulang dengan parameter pada tabel Prerequisites (masing-masing delapan iterasi pada Tab Total Control dan delapan pada Tab Read Only); seluruh blok berkelas fungsional sama, dataset sama, dan tiap iterasi berdiri sendiri karena centang dipulihkan di akhir iterasi. Langkah yang diulang: 2 sampai 11 dan 16 sampai 24.
- Langkah penghubung (S-03): langkah 1, 2, 3, 5, 7, 10, 12 sampai 18, 20, 22, 24, 25, dan 26. Langkah 17 mencentang kolom Curated-tersembunyi sebelum digeser; langkah 24 memulihkan kolom ke keadaan tersembunyi (S-09).
- Temuan untuk QA:
  - TC 508 dan TC 509 menyebut Pre-setup #36 dan #37; kolom Custom Field `Cost Center`, `Joined Date`, `Badge No` memerlukan Custom Field aktif Company Alpha (Pre-setup #22).
