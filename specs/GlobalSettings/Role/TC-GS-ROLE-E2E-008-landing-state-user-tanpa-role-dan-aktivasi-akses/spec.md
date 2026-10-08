---
id: TC-GS-ROLE-E2E-008-landing-state-user-tanpa-role-dan-aktivasi-akses
title: "Landing State Halaman Global Settings User Tanpa Role dan Transisi Pemunculan Menu Pasca-Assign"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-21
  - TC-GS-ROLE-22
  - TC-GS-ROLE-282
coverage:
  web: automated
---

# Landing State Halaman Global Settings User Tanpa Role dan Transisi Pemunculan Menu Pasca-Assign

## Prerequisites

- Login sebagai Agus Salim (Access GS dicentang, tanpa role); sesi admin Ahmad Fauzi
- Data Uji: Agus Salim (Pre-setup #9)
- Setup Hook: dualContext: sessionA (Ahmad Fauzi), sessionB (Agus Salim)
- Login sbg Role: tanpa access level dan tanpa role (Agus Salim, Access Global Settings dicentang)
- Agus Salim login di sesi B pada landing state
- Login sbg Role: Total Control (Ahmad Fauzi) di sesi A
- Login sbg Role: Manage user and role C/R/U/D (Hendra Wijaya), tanpa access level

## Test Steps

### Landing page Global Settings untuk user tanpa access level dan tanpa role (TC-GS-ROLE-21)

1. Login
2. Buka card Global Settings di Portal
3. Screening sidebar dan area konten
4. Verifikasi Login sukses dan app Global Settings terbuka (tidak redirect ke Portal)
5. Verifikasi Sidebar kosong: User, Role & Permission, Import, TAG, Hardware, Brand, Measurement, File Manager, General Settings, Activity Log tidak tampil
6. Verifikasi Area konten: illustration + "You don't have access to any menu yet." + subtext "Contact your administrator to get access."
7. Verifikasi Tidak tampil "Unable to load this data." maupun [Try Again]

### Landing state hilang setelah user tanpa role mendapat role (TC-GS-ROLE-22)

8. Sesi A: Detail "Manage TAG" > [+ Assign] > centang Agus Salim > [Assign]
9. Sesi B: reload halaman
10. Verifikasi Sesi B setelah reload: sidebar menampilkan menu TAG
11. Verifikasi Pesan "You don't have access to any menu yet." tidak tampil lagi
12. Verifikasi Menu Role & Permission tetap tidak tampil (Agus tidak punya Manage user and role)

### Menu General Settings dan Activity Log tidak tampil untuk pemegang role individual tanpa access level (TC-GS-ROLE-282)

13. Buka Global Settings
14. Amati sidebar
15. Verifikasi Menu "User" dan "Role & Permission" tampil
16. Verifikasi Menu "General Settings" dan "Activity Log" tidak tampil

## Notes

- Memvalidasi alur skenario "Landing State Halaman Global Settings User Tanpa Role dan Transisi Pemunculan Menu Pasca-Assign".
- Aturan PRD terkait: global-settings/role/PRD/role.md §10.1; global-settings/role/PRD/role.md §9.2 [F-ROLE-08]; global-settings/role/PRD/role.md §2.1 catatan Activity Log dan General Settings.
- Sumber pemetaan test case granular: TC-GS-ROLE-21, TC-GS-ROLE-22, TC-GS-ROLE-282.
