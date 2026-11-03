---
id: TC-FA-RP-E2E-007-screening-detail-role-matriks-crud-global-role-dan-group-role-3
title: "Screening Detail Role: matriks CRUD Global Role dan Group Role (3/4)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-23
  - TC-FA-RP-24
  - TC-FA-RP-25
  - TC-FA-RP-26
  - TC-FA-RP-27
coverage:
  web: automated
---

# Screening Detail Role: matriks CRUD Global Role dan Group Role (3/4)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup: #15 (pool pengguna), #18 (pohon group), #21 (pemegang Update Manage asset & TAG pada `IT Infrastructure`, dipakai TC-FA-RP-24). Spec hanya membaca; tidak mengubah data.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun dan nama group ditambahkan tim FE.
- Kemampuan teknis: hover untuk membaca tooltip dan memeriksa ikon menu. Spec tidak mengubah state global.

## Test Steps

### TC-FA-RP-23: Screening Detail Role Group Role berkolom CRUD R (`View asset value`)

1. Klik Tab `System`
2. Klik Role Name `View asset value` pada section Group Role
3. Verifikasi Breadcrumb tampil `Settings > Role & Permission > System > Detail`
4. Verifikasi segmen `System` dapat diklik (tautan)
5. Verifikasi Title `View asset value` diikuti sub-title `This role allows the user to view depreciation data for assets, including the depreciation dashboard and reports, within assigned groups.`
6. Verifikasi Sidebar Group Tree tampil di sisi kanan dengan `All Groups` aktif
7. Verifikasi kolom Group tampil
8. Verifikasi kolom matriks Create `—`, Read checkbox, Update `—`, Delete `—`
9. Verifikasi kolom Name, Group, Position, Division tampil
10. Verifikasi toolbar `Search | Filter | Download | Changelog | [+ Assign]`
11. Klik segmen `System` pada Breadcrumb

### TC-FA-RP-24: Screening Detail Role Manage asset & TAG

12. Klik Role Name `Manage asset & TAG` pada section Group Role
13. Klik node `IT Infrastructure` di Sidebar Group Tree
14. Verifikasi Title `Manage asset & TAG` dengan sub-title `This role allows the user to register assets, pair physical TAGs during registration, edit, and (for Unmanaged or Disposed records) delete asset data within assigned groups through the Asset Registration menu.`
15. Verifikasi kolom matriks Create checkbox, Read checkbox, Update checkbox, Delete checkbox
16. Verifikasi Panel `Approval Settings — Registration` memuat toggle `Require Approval for Registration` OFF dengan ikon info `ⓘ` di samping label toggle
17. Verifikasi tidak ada baris teks keterangan approver di bawah sub-label toggle
18. Arahkan kursor ke ikon info `ⓘ` di samping label toggle
19. Verifikasi tooltip ikon info tampil dengan teks `Approvers are users with Update access on Manage asset & TAG that covers this group, Group Managers over this group, and Total Control users. Grant Update access in the table below.`
20. Verifikasi panel tanpa tabel daftar approver, tanpa Checkbox, tanpa Actions, tanpa `[+ Assign]`, dan tanpa Remove
21. Verifikasi tabel penugasan user di bawah panel tetap tampil
22. Klik segmen `System` pada Breadcrumb

### TC-FA-RP-25: Breadcrumb Detail Role Global Role

23. Klik Role Name `Manage Open API` pada section Global Role
24. Verifikasi Breadcrumb tampil persis `Settings > Role & Permission > System > Detail`
25. Verifikasi segmen terakhir `Detail` bukan link
26. Klik segmen `System` pada Breadcrumb
27. Verifikasi segmen `System` membawa kembali ke Tab System

### TC-FA-RP-26: Breadcrumb Detail Role Group Role

28. Klik Role Name `Manage group` pada section Group Role
29. Verifikasi Breadcrumb tampil persis `Settings > Role & Permission > System > Detail`
30. Verifikasi segmen terakhir `Detail` bukan link
31. Klik segmen `System` pada Breadcrumb
32. Verifikasi segmen `System` membawa kembali ke Tab System

### TC-FA-RP-27: Role Name dan row action Detail membuka Detail Role yang sama

33. Klik Role Name `Manage files` pada section Group Role
34. Verifikasi halaman Detail Role `Manage files` tampil
35. Klik segmen `System` pada Breadcrumb
36. Klik `[⋯]` pada baris `Manage files`
37. Verifikasi menu `[⋯]` memuat satu aksi `Detail` (ikon FileInfoLine, severity dark), tanpa Edit atau Delete
38. Pilih `Detail` pada menu `[⋯]`
39. Verifikasi halaman Detail Role `Manage files` yang tampil sama dengan hasil langkah 34
40. Klik segmen `System` pada Breadcrumb

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-23, 24, 25, 26, 27). TC-FA-RP-19 sampai 22 ada di spec `TC-FA-RP-E2E-006-screening-detail-role-matriks-crud-global-role-dan-group-role-2`.
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab, klik Role Name, klik node, dan klik segmen `System` untuk kembali ke daftar role. Klik segmen `System` di TC-FA-RP-23 dan TC-FA-RP-27 adalah langkah penghubung; klik segmen `System` di TC-FA-RP-25 dan TC-FA-RP-26 adalah langkah TC yang hasilnya diasersi.
- Alasan di atas sekitar 35 langkah (40 langkah): seluruh blok satu topik (screening dan navigasi Detail Role) dan satu kelas fungsional, hanya aksi baca; tiap TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-RP-24 mengasersi teks tooltip yang bertanda `copy usulan, PRD 12 #1`; bergantung pada persetujuan PM.
  - TC-FA-RP-27 expected a menyatakan langkah 1 dan 3 membuka halaman yang sama; spec membandingkan lewat `Verifikasi` halaman Detail Role `Manage files` pada kedua jalur.
  - Post Condition TC-FA-RP-23 sampai 27 tidak memberi langkah observasi tambahan; tidak diasersi.
