---
id: TC-AC-SG-E2E-023-manage-group-update-rename-level-satu-dan-dalam-tree-entity-wide
title: "Manage group Update: Rename Level 1 dan Dalam, Tree Penuh Entity-Wide"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-74
  - TC-AC-SG-76
coverage:
  web: automated
---

# Manage group Update: Rename Level 1 dan Dalam, Tree Penuh Entity-Wide

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage group Update saja (Pre-setup #5, `manageGroupU_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.AC_SG_MGU_PASSWORD`; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data: `Pohon Uji Utama` entitas Principal (Pre-setup #16 dan #17, 14 group). TC-AC-SG-74 hanya me-rename node milik spec (di-seed Fixture BE di hook `before`, entitas Principal): `Region C-{runId}-023` (level 1) dan `Head Office-{runId}-023` (level 1) dengan anak `IT Dept-{runId}-023`; nama TC diganti nama bersuffix karena target aksi tulis tidak memakai node Pre-setup bersama (S-06). TC-AC-SG-76 menuntut 14 node `Pohon Uji Utama` dan `Region A`, sehingga node yang di-rename adalah node Pre-setup `Region A` (pengecualian S-06). Node bersuffix `-023` tidak termasuk 14 node Pre-setup.
- Data Dinamis:

| TC | Nama di TC | Seed atau awal di spec | Nama baru di spec |
|---|---|---|---|
| TC-AC-SG-74 | `Region C` (level 1) | `Region C-{runId}-023` | `Region C Baru-{runId}-023` |
| TC-AC-SG-74 | `IT Dept` (anak `Head Office`) | `IT Dept-{runId}-023` (anak `Head Office-{runId}-023`) | `IT Dept Baru-{runId}-023` |
| TC-AC-SG-76 | `Region A` (level 1, Pre-setup) | `Region A` | `Region A Uji` lalu dikembalikan menjadi `Region A` |

- Pemulihan: hook `after` menghapus seluruh group milik spec lewat Fixture BE. Fixture BE (disediakan tim FE/BE, lihat `suite.md`) memulihkan `Pohon Uji Utama` ke baseline Pre-setup di hook `before` dan `after`. Efek: Last Updated dan Modified By node yang diubah dipulihkan oleh baseline Fixture BE; entri Changelog Group yang bertambah adalah audit trail permanen dan tidak dihapus.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-74: Rename level 1 dan level dalam

1. Ketik Search `Region C-{runId}-023`, tekan Enter
2. Klik ikon `⋯` pada baris `Region C-{runId}-023`, lalu pilih "Edit"
3. Ubah nama menjadi `Region C Baru-{runId}-023`, klik `[Save]`
4. Verifikasi toast sukses: "Success, group has been updated."
5. Ganti isi kotak Search tabel utama dengan `Region C Baru-{runId}-023`, tekan Enter
6. Verifikasi baris `Region C-{runId}-023` berubah menjadi `Region C Baru-{runId}-023`
7. Ganti isi kotak search dengan `IT Dept-{runId}-023`, tekan Enter
8. Klik ikon `⋯` pada baris `IT Dept-{runId}-023`, lalu pilih "Edit"
9. Ubah nama menjadi `IT Dept Baru-{runId}-023`, klik `[Save]`
10. Verifikasi toast sukses: "Success, group has been updated."
11. Ganti isi kotak Search tabel utama dengan `IT Dept Baru-{runId}-023`, tekan Enter
12. Verifikasi baris `IT Dept-{runId}-023` berubah menjadi `IT Dept Baru-{runId}-023`
13. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-76: Manage group bersifat entity-wide

14. Verifikasi seluruh 14 node `Pohon Uji Utama` (tanpa node bersuffix `-023` milik spec) tampil dan aktif pada Sidebar Group Tree
15. Verifikasi tidak ada node ancestor yang di-disable atau disembunyikan
16. Ketik Search `Region A`, tekan Enter
17. Klik ikon `⋯` pada baris `Region A`, lalu pilih "Edit"
18. Ubah nama menjadi `Region A Uji`, klik `[Save]`
19. Verifikasi toast sukses: "Success, group has been updated."
20. Verifikasi nama `Region A` (level 1) berubah menjadi `Region A Uji`
21. Klik ikon `⋯` pada baris `Region A Uji`, lalu pilih "Edit"
22. Ubah nama kembali menjadi `Region A`, klik `[Save]`
23. Verifikasi toast sukses: "Success, group has been updated."
24. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1, 7, dan 16 (Search untuk menemukan baris target, R-16), langkah 5 dan 11 (mengganti isi Search dengan nama baru karena Search nama lama tidak lagi memuat baris itu, R-16), langkah 13 dan 24 (reset Search, S-09).
- TC-AC-SG-74 Expected butir b "level 1 dan level dalam diizinkan sama" adalah kesimpulan dari langkah 4, 6, 10, dan 12 dan tidak teramati terpisah (S-03).
- TC-AC-SG-76 Expected butir b "tanpa pemeriksaan kecocokan node tertentu" adalah kesimpulan dari keberhasilan Edit pada level 1 (langkah 19); toast sukses dipakai sebagai penanda berhasil karena TC-AC-SG-74 mendefinisikan toast yang sama untuk Edit.
- Temuan untuk QA:
  - Sidebar Group Tree memuat 14 node Pre-setup `Pohon Uji Utama` ditambah 3 node seed spec (`Region C-{runId}-023`, `Head Office-{runId}-023`, `IT Dept-{runId}-023`) menjadi 17 node; asersi "14 node" (langkah 14) hanya menghitung nama Pre-setup dan tidak menghitung node bersuffix `-023`.
  - Nama baru `Region A` pada TC-AC-SG-76 langkah 3 tidak disebut ("ubah nama lalu `[Save]` (kembalikan nama)"); spec memakai `Region A Uji`.
