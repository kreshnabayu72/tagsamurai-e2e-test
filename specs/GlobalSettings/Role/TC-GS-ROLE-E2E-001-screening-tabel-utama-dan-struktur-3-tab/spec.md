---
id: TC-GS-ROLE-E2E-001-screening-tabel-utama-dan-struktur-3-tab
title: "Screening Struktur 3 Tab (Total Control, Read Only, System) dan Halaman Detail"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-01
  - TC-GS-ROLE-02
  - TC-GS-ROLE-03
  - TC-GS-ROLE-04
  - TC-GS-ROLE-05
  - TC-GS-ROLE-06
coverage:
  web: automated
---

# Screening Struktur 3 Tab (Total Control, Read Only, System) dan Halaman Detail

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia data Default User dan totalControl2 berstatus Total Control
- Tersedia data readOnlyGlobalSettings berstatus Read Only
- Tersedia target user Doni Pratama dengan role Import data (C, R) dan Manage TAG (R, U)

## Test Steps

1. Buka menu Global Settings > Role & Permission
2. Verifikasi Tab 'Total Control' aktif secara default dengan breadcrumb 'Role & Permission'
3. Verifikasi Toolbar memuat: Search, Filter, Download, Changelog, dan tombol [+ Assign]
4. Verifikasi Body tabel memuat kolom: Name (avatar bundled), Position, Division, Status, Modified By, Last Updated, Actions (⋯)
5. Verifikasi kedua user Total Control (Default User dan totalControl2) tampil pada tabel
6. Klik tab 'Read Only' pada navigasi sub-tab
7. Verifikasi struktur tabel identik dengan Tab Total Control tanpa kolom CRUD, dengan tombol [+ Assign] dan download
8. Klik tab 'System' pada navigasi sub-tab
9. Verifikasi Toolbar memuat Search, Filter, Download, Changelog tanpa tombol [+ Assign] atau [+ Add]
10. Verifikasi tabel Tab System menampilkan tepat 6 baris role fixed terurut alfabetis A-Z: Import data, Manage files, Manage hardware, Manage master reference, Manage TAG, Manage user and role
11. Klik Role Name 'Import data' pada baris tabel (atau klik row action ⋯ > Detail)
12. Verifikasi halaman Detail terbuka sebagai halaman terpisah memuat toolbar, tombol [+ Assign], dan tabel user assignment
13. Verifikasi tabel Detail 'Import data' hanya menampilkan 2 kolom CRUD (C, R) sesuai definisi role, bukan 4 kolom, dan Doni Pratama tercentang C dan R
14. Kembali ke Tab System dan buka Detail 'Manage user and role'
15. Verifikasi tabel menampilkan 4 kolom CRUD dinamis (C, R, U, D)
16. Kembali ke Tab System dan buka Detail 'Manage files'
17. Verifikasi tabel menampilkan hanya kolom CRUD (R, D)
18. Kembali ke Tab System dan buka Detail 'Manage TAG'
19. Verifikasi tabel menampilkan hanya kolom CRUD (R, U)
20. Kembali ke Tab System dan klik row action ⋯ > Detail pada baris 'Manage TAG'
21. Verifikasi jalur akses row action Detail membuka halaman yang identik dengan klik nama role

## Notes

- Tab System menampilkan 6 role hardcoded yang tidak pernah dihapus atau ditambah (role.md §2.1, §4.2).
- Kolom CRUD pada halaman Detail bersifat dinamis per role mengikuti kapabilitas yang berlaku (F-ROLE-02).
