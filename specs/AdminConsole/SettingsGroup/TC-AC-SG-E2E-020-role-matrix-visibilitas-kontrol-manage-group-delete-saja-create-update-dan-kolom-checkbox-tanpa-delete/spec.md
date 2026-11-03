---
id: TC-AC-SG-E2E-020-role-matrix-visibilitas-kontrol-manage-group-delete-saja-create-update-dan-kolom-checkbox-tanpa-delete
title: "Role Matrix: Visibilitas Kontrol Manage group Delete Saja, Create + Update, dan Kolom Checkbox tanpa Delete"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-68
  - TC-AC-SG-69
  - TC-AC-SG-172
coverage:
  web: automated
---

# Role Matrix: Visibilitas Kontrol Manage group Delete Saja, Create + Update, dan Kolom Checkbox tanpa Delete

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage group Delete saja (akun aktor pertama); halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Role yang diuji:

| TC | Role | Akun (Pre-setup) | Env password | `[+] Group` | Kolom Checkbox | Isi Overlay Row Action |
|---|---|---|---|---|---|---|
| TC-AC-SG-68 | Manage group Delete saja | #6 `manageGroupD_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_MGD_PASSWORD` | Hidden | Show | "Delete" |
| TC-AC-SG-69, 172 | Manage group Create + Update | #7 `manageGroupCU_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_MGCU_PASSWORD` | Show | Hidden | "+ Add Subgroup", "Edit" |

- Data: `Pohon Uji Utama` entitas Principal (Pre-setup #16 dan #17, 14 group) dibaca saja; spec tidak menulis data.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data atau state global.

## Test Steps

### Blok akun Manage group Delete saja: TC-AC-SG-68

1. Verifikasi tombol `⋯` Show pada seluruh baris tabel dan seluruh node sidebar (seluruh tree, termasuk level 1)
2. Klik ikon `⋯` pada baris group `Region A` di tabel
3. Verifikasi Overlay Row Action hanya memuat "Delete"
4. Tutup Overlay Row Action dengan Esc
5. Klik ikon `⋯` pada node `Region A` di sidebar
6. Verifikasi Overlay Row Action node `Region A` (level 1) hanya memuat "Delete"
7. Tutup Overlay Row Action dengan Esc
8. Klik ikon `⋯` pada node `Room 301` di sidebar
9. Verifikasi Overlay Row Action node `Room 301` (level dalam) hanya memuat "Delete", sama dengan level 1 dan baris tabel (tanpa state per node)
10. Tutup Overlay Row Action dengan Esc
11. Verifikasi `[+] Group` Hidden
12. Verifikasi kolom Checkbox Show
13. Verifikasi pohon penuh, Search sidebar, popup drill-down, Download, Changelog, dan ikon Column Visibility tetap Show
14. Verifikasi seluruh 14 node tree tampil

### Blok akun Manage group Create + Update: TC-AC-SG-69 dan TC-AC-SG-172

15. Ganti akun: logout, lalu login sebagai Manage group Create + Update (`manageGroupCU_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_SG_MGCU_PASSWORD`)
16. Buka halaman `Settings > Group` lewat sidebar
17. Verifikasi tombol `⋯` Show pada seluruh baris tabel dan seluruh node sidebar (seluruh tree, termasuk level 1)
18. Klik ikon `⋯` pada baris group `Region A` di tabel
19. Verifikasi Overlay Row Action hanya memuat "+ Add Subgroup", "Edit"
20. Tutup Overlay Row Action dengan Esc
21. Klik ikon `⋯` pada node `Region A` di sidebar
22. Verifikasi Overlay Row Action node `Region A` (level 1) hanya memuat "+ Add Subgroup", "Edit"
23. Tutup Overlay Row Action dengan Esc
24. Klik ikon `⋯` pada node `Room 301` di sidebar
25. Verifikasi Overlay Row Action node `Room 301` (level dalam) hanya memuat "+ Add Subgroup", "Edit", sama dengan level 1 dan baris tabel (tanpa state per node)
26. Tutup Overlay Row Action dengan Esc
27. Verifikasi `[+] Group` Show
28. Verifikasi kolom Checkbox Hidden
29. Verifikasi pohon penuh, Search sidebar, popup drill-down, Download, Changelog, dan ikon Column Visibility tetap Show
30. Verifikasi seluruh 14 node tree tampil
31. Verifikasi header tabel tidak memuat kolom Checkbox (Hidden total)
32. Verifikasi Bulk Actions Bar tidak ada dan tidak dapat dipicu

## Notes

- Spec ditulis per blok akun karena langkah tiap role identik tetapi ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Manage group Create + Delete ada di spec 109.
- TC-AC-SG-172 memakai akun yang sama dengan TC-AC-SG-69 (Create + Update, Pre-setup #7) dan ditaruh pada blok akun itu (langkah 31 dan 32) agar tidak perlu ganti akun lagi.
- Langkah penghubung (S-03): langkah 4, 7, 10, 20, 23, dan 26 (menutup Overlay Row Action).
- Temuan untuk QA: lihat catatan pada spec 019 mengenai Expected butir a "seluruh baris tabel" yang berlaku juga untuk TC-AC-SG-68 dan TC-AC-SG-69.
