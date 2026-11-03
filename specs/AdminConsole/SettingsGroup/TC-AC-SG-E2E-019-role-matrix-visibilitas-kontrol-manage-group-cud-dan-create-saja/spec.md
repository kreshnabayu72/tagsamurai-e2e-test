---
id: TC-AC-SG-E2E-019-role-matrix-visibilitas-kontrol-manage-group-cud-dan-create-saja
title: "Role Matrix: Visibilitas Kontrol Manage group Create, Update, Delete dan Create Saja"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-65
  - TC-AC-SG-66
coverage:
  web: automated
---

# Role Matrix: Visibilitas Kontrol Manage group Create, Update, Delete dan Create Saja

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage group Create, Update, Delete (akun aktor pertama); halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Role yang diuji:

| TC | Role | Akun (Pre-setup) | Env password | `[+] Group` | Kolom Checkbox | Isi Overlay Row Action |
|---|---|---|---|---|---|---|
| TC-AC-SG-65 | Manage group Create, Update, Delete | #3 `manageGroupCUD_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_MGCUD_PASSWORD` | Show | Show | "+ Add Subgroup", "Edit", "Delete" |
| TC-AC-SG-66 | Manage group Create saja | #4 `manageGroupC_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_MGC_PASSWORD` | Show | Hidden | "+ Add Subgroup" |

- Data: `Pohon Uji Utama` entitas Principal (Pre-setup #16 dan #17, 14 group) dibaca saja; spec tidak menulis data.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data atau state global.

## Test Steps

### Blok akun Manage group Create, Update, Delete: TC-AC-SG-65

1. Verifikasi tombol `⋯` Show pada seluruh baris tabel dan seluruh node sidebar (seluruh tree, termasuk level 1)
2. Ketik Search `Region A`, tekan Enter
3. Klik ikon `⋯` pada baris group `Region A` di tabel
4. Verifikasi Overlay Row Action hanya memuat "+ Add Subgroup", "Edit", "Delete"
5. Tutup Overlay Row Action dengan Esc
6. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
7. Klik ikon `⋯` pada node `Region A` di sidebar
8. Verifikasi Overlay Row Action node `Region A` (level 1) hanya memuat "+ Add Subgroup", "Edit", "Delete"
9. Tutup Overlay Row Action dengan Esc
10. Klik ikon `⋯` pada node `Room 301` di sidebar
11. Verifikasi Overlay Row Action node `Room 301` (level dalam) hanya memuat "+ Add Subgroup", "Edit", "Delete", sama dengan level 1 dan baris tabel (tanpa state per node)
12. Tutup Overlay Row Action dengan Esc
13. Verifikasi `[+] Group` Show
14. Verifikasi kolom Checkbox Show
15. Verifikasi pohon penuh, Search sidebar, popup drill-down, Download, Changelog, dan ikon Column Visibility tetap Show
16. Verifikasi seluruh 14 node tree tampil

### Blok akun Manage group Create saja: TC-AC-SG-66

17. Ganti akun: logout, lalu login sebagai Manage group Create saja (`manageGroupC_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_SG_MGC_PASSWORD`)
18. Buka halaman `Settings > Group` lewat sidebar
19. Verifikasi tombol `⋯` Show pada seluruh baris tabel dan seluruh node sidebar (seluruh tree, termasuk level 1)
20. Ketik Search `Region A`, tekan Enter
21. Klik ikon `⋯` pada baris group `Region A` di tabel
22. Verifikasi Overlay Row Action hanya memuat "+ Add Subgroup"
23. Tutup Overlay Row Action dengan Esc
24. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
25. Klik ikon `⋯` pada node `Region A` di sidebar
26. Verifikasi Overlay Row Action node `Region A` (level 1) hanya memuat "+ Add Subgroup"
27. Tutup Overlay Row Action dengan Esc
28. Klik ikon `⋯` pada node `Room 301` di sidebar
29. Verifikasi Overlay Row Action node `Room 301` (level dalam) hanya memuat "+ Add Subgroup", sama dengan level 1 dan baris tabel (tanpa state per node)
30. Tutup Overlay Row Action dengan Esc
31. Verifikasi `[+] Group` Show
32. Verifikasi kolom Checkbox Hidden
33. Verifikasi pohon penuh, Search sidebar, popup drill-down, Download, Changelog, dan ikon Column Visibility tetap Show
34. Verifikasi seluruh 14 node tree tampil

## Notes

- Spec ditulis per blok akun karena langkah tiap role identik tetapi ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Manage group Update saja ada di spec 108, Create + Delete di spec 109.
- Langkah penghubung (S-03, R-16): langkah 2 dan 20 (Search `Region A` untuk menemukan baris target karena tabel All Groups terbagi dua halaman), langkah 6 dan 24 (klik `(←)` pada kotak Search sesudah overlay ditutup), langkah 5, 9, 12, 23, 27, dan 30 (menutup Overlay Row Action).
- Temuan untuk QA: TC-AC-SG-65 dan TC-AC-SG-66 Expected butir a menyebut "seluruh baris tabel", sedangkan langkah hanya membuka `⋯` pada tiga lokasi; spec mengasersi `⋯` Show pada seluruh baris dan node sebagai satu Verifikasi dan membuka overlay pada `Region A` (tabel dan sidebar) serta `Room 301` (sidebar).
