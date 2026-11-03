---
id: TC-AC-SG-E2E-108-role-matrix-visibilitas-kontrol-manage-group-update-saja
title: "Role Matrix: Visibilitas Kontrol Manage group Update Saja"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-67
coverage:
  web: automated
---

# Role Matrix: Visibilitas Kontrol Manage group Update Saja

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage group Update saja (`manageGroupU_automated_{namaCompany}@qwertysystem.net`, Pre-setup #5), password `Spectra.env.AC_SG_MGU_PASSWORD`; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Role yang diuji:

| TC | Role | Akun (Pre-setup) | Env password | `[+] Group` | Kolom Checkbox | Isi Overlay Row Action |
|---|---|---|---|---|---|---|
| TC-AC-SG-67 | Manage group Update saja | #5 | `Spectra.env.AC_SG_MGU_PASSWORD` | Hidden | Hidden | "Edit" |

- Data: `Pohon Uji Utama` entitas Principal (Pre-setup #16 dan #17, 14 group) dibaca saja; spec tidak menulis data.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data atau state global.

## Test Steps

### TC-AC-SG-67: Manage group Update saja

1. Verifikasi tombol `⋯` Show pada seluruh baris tabel dan seluruh node sidebar (seluruh tree, termasuk level 1)
2. Klik ikon `⋯` pada baris group `Region A` di tabel
3. Verifikasi Overlay Row Action hanya memuat "Edit"
4. Tutup Overlay Row Action dengan Esc
5. Klik ikon `⋯` pada node `Region A` di sidebar
6. Verifikasi Overlay Row Action node `Region A` (level 1) hanya memuat "Edit"
7. Tutup Overlay Row Action dengan Esc
8. Klik ikon `⋯` pada node `Room 301` di sidebar
9. Verifikasi Overlay Row Action node `Room 301` (level dalam) hanya memuat "Edit", sama dengan level 1 dan baris tabel (tanpa state per node)
10. Tutup Overlay Row Action dengan Esc
11. Verifikasi `[+] Group` Hidden
12. Verifikasi kolom Checkbox Hidden
13. Verifikasi pohon penuh, Search sidebar, popup drill-down, Download, Changelog, dan ikon Column Visibility tetap Show
14. Verifikasi seluruh 14 node tree tampil

## Notes

- Matriks visibilitas Manage group dibagi atas beberapa spec: CUD dan Create saja di spec 019, Delete saja dan Create + Update di spec 020, Create + Delete di spec 109, Update + Delete dan tanpa capability mutasi di spec 021.
- Langkah penghubung (S-03): langkah 4, 7, dan 10 (menutup Overlay Row Action).
- Temuan untuk QA: lihat catatan pada spec 019 mengenai Expected butir a "seluruh baris tabel" yang berlaku juga untuk TC-AC-SG-67.
