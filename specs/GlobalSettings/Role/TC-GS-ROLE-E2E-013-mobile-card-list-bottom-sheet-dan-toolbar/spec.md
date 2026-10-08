---
id: TC-GS-ROLE-E2E-013-mobile-card-list-bottom-sheet-dan-toolbar
title: "Tampilan Mobile Android: Card List Tab TC/RO/System, Bottom Sheet Picker/Changelog, dan Toolbar Mobile"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-285
  - TC-GS-ROLE-286
  - TC-GS-ROLE-287
  - TC-GS-ROLE-288
coverage:
  web: automated
---

# Tampilan Mobile Android: Card List Tab TC/RO/System, Bottom Sheet Picker/Changelog, dan Toolbar Mobile

## Prerequisites

- Aplikasi Android native; login sebagai Total Control
- Data Uji: Pre-setup #1 s/d #4, Doni Pratama
- Setup Hook: beforeEach: setMobileAndroidContext()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Aplikasi Android native
- Pre-setup #1–#4 tersedia
- Doni Pratama punya baris Import data (C,R)

## Test Steps

### Mobile — card Tab Total Control dan Tab Read Only (TC-GS-ROLE-285)

1. Buka Role & Permission > Tab Total Control di aplikasi mobile
2. Screening card Dewi Lestari
3. Tap [⋯] pada card Dewi Lestari
4. Ulangi langkah 2–3 di Tab Read Only pada card Rina Putri
5. Verifikasi Tabel tampil sebagai Card List, bukan tabel horizontal
6. Verifikasi Baris 1 card: thumbnail foto (circle) + Name tebal + icon [⋯]
7. Verifikasi Baris 2: "Staff · Finance" (Position · Division)
8. Verifikasi Baris 3: Status "Inactive"
9. Verifikasi [⋯] hanya berisi Remove
10. Verifikasi Tab Read Only: card Rina Putri baris 2 "HR Manager · HR", baris 3 "Inactive"; [⋯] berisi Remove

### Mobile — card Tab System dan toolbar mobile (TC-GS-ROLE-286)

11. Buka Tab Total Control, screening toolbar
12. Tap [⋯] toolbar
13. Tap [🔍]
14. Buka Tab System, screening card "Manage TAG" dan toolbar
15. Tap [⋯] toolbar Tab System
16. Tap [⋯] pada card "Manage TAG"
17. Login ke client uji B (Pre-setup #14: setiap role hanya dipegang Default User), buka Tab System di aplikasi mobile, screening card "Manage TAG"
18. Verifikasi Tab Total Control: icon [Changelog] tampil di header di samping [🔍] dan [⋯]; [+ Assign] tampil di bawah toolbar, di atas card list
19. Verifikasi [⋯] toolbar membuka bottom sheet: Column Visibility, Filter, Download
20. Verifikasi [🔍] membuka search bar inline
21. Verifikasi Card Tab System: baris 1 "Manage TAG" + [⋯]; baris 2 "[N] users" (N ≥ 2) sesuai kolom Users
22. Verifikasi Bottom sheet Tab System: Column Visibility dan Download, tanpa Filter; tidak ada [+ Assign]
23. Verifikasi [⋯] card berisi Detail
24. Verifikasi Client uji B: card "Manage TAG" baris 2 "1 user" (bentuk tunggal)

### Mobile — Popup Table User Picker dan Modal Changelog tampil sebagai bottom sheet (TC-GS-ROLE-287)

25. Tab Total Control: tap [+ Assign]
26. Tutup, tap [Changelog]
27. Buka Detail "Manage TAG", tap [+ Assign]
28. Verifikasi Popup Assign Total Control tampil sebagai bottom sheet
29. Verifikasi Modal "Changelog: Role & Permission > Total Control" tampil sebagai bottom sheet
30. Verifikasi Popup Assign Role di Detail tampil sebagai bottom sheet

### Mobile — Detail Import data menampilkan toggle Create dan Read saja (TC-GS-ROLE-288)

31. Buka Detail "Import data" di aplikasi mobile
32. Screening card Doni Pratama
33. Tap [⋯] pada card
34. Verifikasi Baris 1 card: thumbnail foto + Name
35. Verifikasi Toggle Create dan Read tampil; tidak ada baris toggle Update maupun Delete (bukan toggle disabled)
36. Verifikasi Toggle Read checked dan disabled
37. Verifikasi [⋯] berisi Remove

## Notes

- Memvalidasi alur skenario "Tampilan Mobile Android: Card List Tab TC/RO/System, Bottom Sheet Picker/Changelog, dan Toolbar Mobile".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.6 Card: Total Control / Read Only; global-settings/role/PRD/role.md §4.6 Card: Tab System; global-settings/role/PRD/role.md §4.6 Toolbar Mobile; global-settings/role/PRD/role.md §4.6; foundation/process/prd-process/prd-conventions.md §13.2; global-settings/role/PRD/role.md §4.6 Detail (Mobile); global-settings/role/PRD/role.md §2.1.
- Sumber pemetaan test case granular: TC-GS-ROLE-285, TC-GS-ROLE-286, TC-GS-ROLE-287, TC-GS-ROLE-288.
