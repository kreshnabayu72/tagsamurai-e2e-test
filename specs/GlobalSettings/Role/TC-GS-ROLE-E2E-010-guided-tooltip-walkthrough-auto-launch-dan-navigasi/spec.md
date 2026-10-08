---
id: TC-GS-ROLE-E2E-010-guided-tooltip-walkthrough-auto-launch-dan-navigasi
title: "Guided Tooltip Walkthrough: Auto-Launch Kunjungan Pertama, Langkah 1-3, dan Penutupan Done"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-26
  - TC-GS-ROLE-27
  - TC-GS-ROLE-28
coverage:
  web: automated
---

# Guided Tooltip Walkthrough: Auto-Launch Kunjungan Pertama, Langkah 1-3, dan Penutupan Done

## Prerequisites

- Login sebagai Total Control; flag gs-role-permission belum diset
- Data Uji: User fresh visit
- Setup Hook: beforeEach: clearTourFlag()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Flag guided tooltip `gs-role-permission` belum pernah diset untuk user ini
- Flag guided tooltip belum diset
- User membuka halaman langsung ke Tab System (URL Role & Permission > System)

## Test Steps

### Guided tooltip muncul otomatis pada kunjungan pertama di Tab Total Control (TC-GS-ROLE-26)

1. Buka Global Settings > Role & Permission
2. Screening step 1
3. Verifikasi Walkthrough mulai dari Step 1 di Tab Total Control
4. Verifikasi Step 1 menyorot Tabs: Title "Access Level Navigation", Description "Switch between access levels and individual roles to configure user permissions."
5. Verifikasi [Back] tidak tampil pada Step 1

### Guided tooltip Step 2 dan Step 3 lalu Done (TC-GS-ROLE-27)

6. Buka Role & Permission
7. Klik [Next]
8. Screening step 2
9. Klik [Next]
10. Screening step 3
11. Klik [Done]
12. Reload halaman
13. Verifikasi Step 2 menyorot ikon Search Tab Total Control: Title "Search", Description "Quickly search by name to find a specific entry. What you can search depends on the tab you are on."
14. Verifikasi Step 3 menyorot header kolom Actions [⋯]: Title "Table Actions", Description "Manage which columns are shown from the header actions menu, and use the row action menu for actions on each row. Available actions depend on the tab you are on."
15. Verifikasi Pada Step 3 tombol [Next] berubah menjadi [Done]
16. Verifikasi [Done] menutup walkthrough
17. Verifikasi Setelah reload walkthrough tidak muncul otomatis

### Guided tooltip dimulai di tab yang sedang aktif tanpa berpindah tab (TC-GS-ROLE-28)

18. Buka URL Role & Permission > System langsung
19. Screening Step 1
20. Klik [Next] ke Step 2 lalu Step 3, amati tab aktif dan breadcrumb di tiap step
21. Klik [Done]
22. Verifikasi Halaman terbuka di Tab System dan walkthrough mulai dari Step 1 di Tab System (tidak dialihkan ke Tab Total Control)
23. Verifikasi Step 2 menyorot ikon Search Tab System (placeholder "Search role...")
24. Verifikasi Step 3 menyorot header kolom Actions [⋯] Tab System
25. Verifikasi Selama walkthrough Tab System tetap aktif dan breadcrumb tetap "Role & Permission > System"; tidak ada route navigation maupun dialog otomatis

## Notes

- Memvalidasi alur skenario "Guided Tooltip Walkthrough: Auto-Launch Kunjungan Pertama, Langkah 1-3, dan Penutupan Done".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.7; foundation/functions/guided-tooltip.md; foundation/functions/guided-tooltip.md Aturan Terkunci #1; foundation/functions/guided-tooltip.md Aturan Terkunci #2.
- Sumber pemetaan test case granular: TC-GS-ROLE-26, TC-GS-ROLE-27, TC-GS-ROLE-28.
