---
id: TC-AC-SG-E2E-024-manage-group-delete-menghapus-group-lewat-checkbox-bulk-dan-delete
title: "Manage group Delete: Menghapus Group lewat Checkbox Bulk dan Delete"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-75
coverage:
  web: automated
---

# Manage group Delete: Menghapus Group lewat Checkbox Bulk dan Delete

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage group Delete saja pada entitas `Distributor Hapus Utama` (Pre-setup #21 dan #6). Email dan password akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE, password `Spectra.env.AC_SG_HAPUSMGD_PASSWORD`.
- Login di hook `before` spec ini sebagai akun tersebut; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data seed milik spec (entitas `Distributor Hapus Utama`, di-seed Fixture BE di hook `before`, tanpa entitas): `Hapus Bulk 1-{runId}-024` dan `Hapus Bulk 2-{runId}-024` (nama TC `Hapus Bulk 1` dan `Hapus Bulk 2` memakai suffix per run karena target hapus adalah data milik spec, S-06 dan S-12).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan baseline entitas `Distributor Hapus Utama`) disediakan tim FE/BE (lihat `suite.md`).
- Pemulihan: hook `after` memulihkan baseline `Distributor Hapus Utama` lewat Fixture BE.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-75: Delete-Only menghapus group lewat checkbox bulk

1. Ketik Search `{runId}-024`, tekan Enter
2. Verifikasi kolom Checkbox Show
3. Centang kolom Checkbox baris `Hapus Bulk 1-{runId}-024`
4. Centang kolom Checkbox baris `Hapus Bulk 2-{runId}-024`
5. Verifikasi Bulk Actions Bar menampilkan "2 Groups selected"
6. Klik `Bulk Action` pada Bulk Actions Bar, lalu pilih `Delete`
7. Verifikasi dialog "Delete Groups" tampil
8. Klik `[Delete]` pada dialog
9. Verifikasi toast sukses: "Success, group has been deleted."
10. Verifikasi baris `Hapus Bulk 1-{runId}-024` dan `Hapus Bulk 2-{runId}-024` hilang dari tabel
11. Verifikasi node `Hapus Bulk 1-{runId}-024` dan `Hapus Bulk 2-{runId}-024` hilang dari Sidebar Group Tree
12. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16) dan langkah 12 (reset Search, S-09).
- Langkah 10 memakai toast sukses langkah 9 sebagai anchor absence baris (bagian 8b butir 2).
- Temuan untuk QA:
  - Email dan password akun Manage group Delete saja pada `Distributor Hapus Utama` tidak tertulis di Pre-setup; #6 adalah akun Delete-Only entitas Principal, sedangkan data yang dihapus ada di `Distributor Hapus Utama` (#21). Pendaftaran nama env `AC_SG_HAPUSMGD_PASSWORD` mengikuti `suite.md`.
  - Pre-setup #21 memuat `Hapus Bulk 1` sampai `Hapus Bulk 6`; spec memakai dua node milik spec dengan nama TC bersuffix, bukan node Pre-setup.
