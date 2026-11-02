---
id: TC-AC-SU-E2E-022-role-matrix-group-role-target-group-manager-dan-sidebar-tanpa-restriksi
title: "Role Matrix: Group Role Target Group Manager untuk Manage user and role dan Total Control serta Sidebar Group tanpa Restriksi Node"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-66
  - TC-AC-SU-67
  - TC-AC-SU-78
coverage:
  web: automated
---

# Role Matrix: Group Role Target Group Manager untuk Manage user and role dan Total Control serta Sidebar Group tanpa Restriksi Node

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage user and role Update (U=true, Pre-setup #4) `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_UPDATE_PASSWORD`.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_MUR_UPDATE_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan pemilik repo (nama ditetapkan penulis spec). Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini sebagai Manage user and role (Update, U=true); halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Role yang diuji:

| TC | Role | Akun |
|---|---|---|
| TC-AC-SU-66, 78 | Manage user and role (U=true) | Pre-setup #4 |
| TC-AC-SU-67 | Total Control | Pre-setup #2 |

- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-66, 67, 78 | `Region A` | `Region A {runId}-022` | - | Group akar |
| TC-AC-SU-66, 78 | `Region B` | `Region B {runId}-022` | - | Group akar |
| TC-AC-SU-78 | `Branch 1` | `Branch 1 {runId}-022` | - | anak `Region A {runId}-022` |
| TC-AC-SU-66, 67 | `Dedi Kurnia` | `Dedi Kurnia {runId}-022` | `dedikurnia+{runId}-022@qwertysystem.net` | Group Manager `Region A {runId}-022`; `Manage allocation` punya assignment di `Region A {runId}-022`; `Manage partner` hanya di `Region B {runId}-022`; `Manage active client` tanpa assignment |
| TC-AC-SU-78 | `Jane Smith` | `Jane Smith {runId}-022` | `janesmith+{runId}-022@qwertysystem.net` | Group Role aktif di `Branch 1 {runId}-022` |
| TC-AC-SU-78 | `John Doe` | `John Doe {runId}-022` | `johndoe+{runId}-022@qwertysystem.net` | Group Role aktif di `Region B {runId}-022` |

- Group Role aktor Manage user and role (Pre-setup #4) diubah lewat Fixture BE agar hanya ada di `Region B {runId}-022` (TC-AC-SU-78; S-06 pengecualian, data aktor tidak dapat dimiliki spec) dan dipulihkan ke keadaan awal di hook `before`, `after`, dan langkah akhir blok; efeknya pada Last Updated dan Modified By akun aktor dicatat sebagai efek spec ini.
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-66: Group Role target GM, aktor Manage user and role

1. Ketik Search `Dedi Kurnia {runId}-022`, tekan Enter
2. Klik Name `Dedi Kurnia {runId}-022`
3. Klik Tab Role
4. Klik sub-tab Group Role
5. Verifikasi banner `This user is a Group Manager for: Region A {runId}-022.`
6. Verifikasi sub-tab tidak punya switch
7. Verifikasi `[Assign Group]` dan `[Detail]` enabled di semua baris
8. Klik `[Assign Group]` baris `Manage allocation`
9. Hover CRUD baris `Region A {runId}-022` pada popup
10. Verifikasi CRUD baris `Region A {runId}-022` tampil namun disabled dengan tooltip `You don't have permission to edit.`
11. Hover `[🗑]` baris `Region A {runId}-022` pada popup
12. Verifikasi `[🗑]` baris `Region A {runId}-022` tampil namun disabled dengan tooltip `You don't have permission to edit.`
13. Tutup popup Assign Group Role
14. Klik `[Assign Group]` baris `Manage partner`
15. Verifikasi baris `Region B {runId}-022` editable
16. Tutup popup Assign Group Role
17. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User

### TC-AC-SU-78: Sidebar Group tanpa restriksi node untuk Manage user and role

18. Atur Group Role akun aktor hanya di `Region B {runId}-022` lewat Fixture BE
19. Muat ulang halaman dengan F5
20. Verifikasi semua node Sidebar Group tampil
21. Verifikasi semua node Sidebar Group dapat diklik
22. Ketik Search `{runId}-022`, tekan Enter
23. Klik node `Region A {runId}-022`
24. Verifikasi `Jane Smith {runId}-022` (Group Role di `Branch 1 {runId}-022`, descendant `Region A {runId}-022`) tampil
25. Verifikasi `John Doe {runId}-022` (Group Role di `Region B {runId}-022`) tidak tampil
26. Klik node `Region A {runId}-022` untuk membatalkan pilihan
27. Pulihkan Group Role akun aktor ke keadaan awal lewat Fixture BE
28. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SU-67: Group Role target GM, aktor Total Control

29. Logout dari akun aktor saat ini
30. Login sebagai Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`)
31. Ketik Search `Dedi Kurnia {runId}-022`, tekan Enter
32. Klik Name `Dedi Kurnia {runId}-022`
33. Klik Tab Role
34. Klik sub-tab Group Role
35. Verifikasi tabel Group Role tidak punya kolom Active
36. Verifikasi tabel Group Role tidak punya switch di tiap baris
37. Verifikasi `[Assign Group]` dan `[Detail]` enabled, termasuk baris `Manage allocation`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16; berlaku juga untuk Search sesudahnya), langkah 13 dan 16 (tutup popup), langkah 17 (kembali ke daftar), langkah 18 (pengaturan aktor sebagai precondition TC-AC-SU-78), langkah 26 (pulihkan state, S-09).
- Alasan blok per akun (bagian 3a, `[KEPUTUSAN 2026-10-30]`): ganti akun menuntut Step eksplisit; aktor Manage user and role dipakai untuk TC-AC-SU-66 dan 78 berurutan sebelum ganti akun ke Total Control.
- Ukuran spec (37 langkah, di atas smell sekitar 35 langkah): Role Matrix satu permukaan (Group Role / Sidebar) dengan dua akun; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-SU-66 langkah 4 ("Tutup popup, klik `[Assign Group]` baris `Manage partner`") dan TC-AC-SU-67 butir "termasuk baris `Manage allocation`": TC tidak menyebut cara menutup popup; spec memakai `✕`.
  - TC-AC-SU-78 mensyaratkan aktor Manage user and role yang Group Role-nya hanya di `Region B`; spec mengatur ulang Group Role akun Pre-setup #4 lewat Fixture BE dan memulihkannya (lihat Prerequisites).
  - Nama user TC (`Region A`, `Region B`, `Branch 1`, `Dedi Kurnia`, `Jane Smith`, `John Doe`) dipakai sebagai nama bersuffix `{runId}-022` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
