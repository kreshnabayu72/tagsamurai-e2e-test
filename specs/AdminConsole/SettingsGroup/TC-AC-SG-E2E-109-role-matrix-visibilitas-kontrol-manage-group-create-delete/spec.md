---
id: TC-AC-SG-E2E-109-role-matrix-visibilitas-kontrol-manage-group-create-delete
title: "Role Matrix: Visibilitas Kontrol Manage group Create + Delete"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-70
coverage:
  web: automated
---

# Role Matrix: Visibilitas Kontrol Manage group Create + Delete

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage group Create + Delete (`manageGroupCD_automated_{namaCompany}@qwertysystem.net`, Pre-setup #8), password `Spectra.env.AC_SG_MGCD_PASSWORD`; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Role yang diuji:

| TC | Role | Akun (Pre-setup) | Env password | `[+] Group` | Kolom Checkbox | Isi Overlay Row Action |
|---|---|---|---|---|---|---|
| TC-AC-SG-70 | Manage group Create + Delete | #8 | `Spectra.env.AC_SG_MGCD_PASSWORD` | Show | Show | "+ Add Subgroup", "Delete" |

- Data: `Pohon Uji Utama` entitas Principal (Pre-setup #16 dan #17, 14 group) dibaca saja; spec tidak menulis data.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data atau state global.

## Test Steps

### TC-AC-SG-70: Manage group Create + Delete

1. Verifikasi sedikitnya satu baris tabel dan satu node Sidebar Group Tree tampil
2. Verifikasi tombol `⋯` Show pada seluruh baris tabel dan seluruh node sidebar (seluruh tree, termasuk level 1)
3. Ketik Search `Region A`, tekan Enter
4. Klik ikon `⋯` pada baris group `Region A` di tabel
5. Verifikasi Overlay Row Action hanya memuat "+ Add Subgroup", "Delete"
6. Tutup Overlay Row Action dengan Esc
7. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
8. Klik ikon `⋯` pada node `Region A` di sidebar
9. Verifikasi Overlay Row Action node `Region A` (level 1) hanya memuat "+ Add Subgroup", "Delete"
10. Tutup Overlay Row Action dengan Esc
11. Klik ikon `⋯` pada node `Room 301` di sidebar
12. Verifikasi Overlay Row Action node `Room 301` (level dalam) hanya memuat "+ Add Subgroup", "Delete", sama dengan level 1 dan baris tabel (tanpa state per node)
13. Tutup Overlay Row Action dengan Esc
14. Verifikasi `[+] Group` Show
15. Verifikasi kolom Checkbox Show
16. Verifikasi pohon penuh, Search sidebar, popup drill-down, Download, Changelog, dan ikon Column Visibility tetap Show
17. Verifikasi seluruh 14 node tree tampil

## Notes

- Matriks visibilitas Manage group dibagi atas beberapa spec: CUD dan Create saja di spec 019, Update saja di spec 108, Delete saja dan Create + Update di spec 020, Update + Delete dan tanpa capability mutasi di spec 021.
- Langkah penghubung (S-03, R-16): langkah 3 dan 7 (Search `Region A` untuk menemukan baris target karena tabel All Groups terbagi dua halaman, lalu klik `(←)` pada kotak Search sesudah overlay ditutup), langkah 6, 10, dan 13 (menutup Overlay Row Action).
- Default Sidebar Group Tree: seluruh tree ter-expand (PRD §4.2b), sehingga spec ini tidak memuat langkah expand node. Langkah 1 menjadi anchor positif bagi asersi universal langkah 2 (bagian 8b butir 2).
- Temuan untuk QA: lihat catatan pada spec 019 mengenai Expected butir a "seluruh baris tabel" yang berlaku juga untuk TC-AC-SG-70.
