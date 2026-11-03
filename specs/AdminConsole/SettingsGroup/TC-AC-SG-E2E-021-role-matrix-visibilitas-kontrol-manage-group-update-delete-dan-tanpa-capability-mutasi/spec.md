---
id: TC-AC-SG-E2E-021-role-matrix-visibilitas-kontrol-manage-group-update-delete-dan-tanpa-capability-mutasi
title: "Role Matrix: Visibilitas Kontrol Manage group Update + Delete dan tanpa Capability Mutasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-71
  - TC-AC-SG-72
coverage:
  web: automated
---

# Role Matrix: Visibilitas Kontrol Manage group Update + Delete dan tanpa Capability Mutasi

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage group Update + Delete (akun aktor pertama); halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Role yang diuji:

| TC | Role | Akun (Pre-setup) | Env password | `⋯` | `[+] Group` | Kolom Checkbox | Isi Overlay Row Action |
|---|---|---|---|---|---|---|---|
| TC-AC-SG-71 | Manage group Update + Delete | #9 `manageGroupUD_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_MGUD_PASSWORD` | Show | Hidden | Show | "Edit", "Delete" |
| TC-AC-SG-72 | Manage group aktif tanpa Create/Update/Delete | #10 `manageGroupNone_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_MGNONE_PASSWORD` | Hidden | Hidden | Hidden | tidak ada |

- Data: `Pohon Uji Utama` entitas Principal (Pre-setup #16 dan #17, 14 group) dibaca saja; spec tidak menulis data.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data atau state global.

## Test Steps

### Blok akun Manage group Update + Delete: TC-AC-SG-71

1. Verifikasi tombol `⋯` Show pada seluruh baris tabel dan seluruh node sidebar (seluruh tree, termasuk level 1)
2. Klik ikon `⋯` pada baris group `Region A` di tabel
3. Verifikasi Overlay Row Action hanya memuat "Edit", "Delete"
4. Tutup Overlay Row Action dengan Esc
5. Klik ikon `⋯` pada node `Region A` di sidebar
6. Verifikasi Overlay Row Action node `Region A` (level 1) hanya memuat "Edit", "Delete"
7. Tutup Overlay Row Action dengan Esc
8. Klik ikon `⋯` pada node `Room 301` di sidebar
9. Verifikasi Overlay Row Action node `Room 301` (level dalam) hanya memuat "Edit", "Delete", sama dengan level 1 dan baris tabel (tanpa state per node)
10. Tutup Overlay Row Action dengan Esc
11. Verifikasi `[+] Group` Hidden
12. Verifikasi kolom Checkbox Show
13. Verifikasi pohon penuh, Search sidebar, popup drill-down, Download, Changelog, dan ikon Column Visibility tetap Show
14. Verifikasi seluruh 14 node tree tampil

### Blok akun Manage group tanpa capability mutasi: TC-AC-SG-72

15. Ganti akun: logout, lalu login sebagai Manage group tanpa Create/Update/Delete (`manageGroupNone_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_SG_MGNONE_PASSWORD`)
16. Buka halaman `Settings > Group` lewat sidebar
17. Verifikasi tombol `⋯` Hidden pada baris tabel dan node sidebar (tidak dirender)
18. Verifikasi `[+] Group` Hidden
19. Verifikasi kolom Checkbox Hidden
20. Verifikasi pohon penuh, Search sidebar, popup drill-down, Download, Changelog, dan ikon Column Visibility tetap Show
21. Verifikasi seluruh 14 node tree tampil

## Notes

- Spec ditulis per blok akun karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (S-03): langkah 4, 7, dan 10 (menutup Overlay Row Action).
- Temuan untuk QA:
  - TC-AC-SG-72 langkah 3 dan 4 meminta klik `⋯` pada baris dan node, sedangkan Expected menyatakan tombol `⋯` Hidden (tidak dirender); klik tidak dapat dilakukan sehingga spec hanya mengasersi Hidden.
  - Lihat juga catatan pada spec 019 mengenai Expected butir a "seluruh baris tabel" yang berlaku untuk TC-AC-SG-71.
