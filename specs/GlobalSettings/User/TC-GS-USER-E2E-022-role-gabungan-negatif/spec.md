---
id: TC-GS-USER-E2E-022-role-gabungan-negatif
title: Semua role tanpa hak tidak dapat menjalankan aksi yang bukan haknya
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-486
  - TC-GS-USER-08
  - TC-GS-USER-85
  - TC-GS-USER-581
  - TC-GS-USER-582
  - TC-GS-USER-583
  - TC-GS-USER-339
  - TC-GS-USER-84
  - TC-GS-USER-80
  - TC-GS-USER-81
  - TC-GS-USER-83
  - TC-GS-USER-86
  - TC-GS-USER-10
  - TC-GS-USER-12
  - TC-GS-USER-11
coverage:
  web: automated
---

# Semua role tanpa hak tidak dapat menjalankan aksi yang bukan haknya

## Prerequisites

Spec ini varian B untuk A/B testing dengan tim FE. Isinya menggabungkan spec negatif Role Matrix (015–020) menjadi satu spec yang disusun per role. Tiap role login sekali, lalu mengamati semua elemen yang relevan. Spec ini tidak mengubah data. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

Role yang diuji dan keadaan elemen pada baris target biasa:

| Role | Akun | `[+ User]` | Edit | Toggle Active | Delete | Resend | Pair/Unpair TAG |
|---|---|---|---|---|---|---|---|
| Read Only | `readOnlyGlobalSettings_automated_qaTeam1` | Hidden | Hidden | Disabled, tooltip "You don't have permission to edit" | Hidden | Hidden | Tidak diverifikasi |
| Hanya Create | `manageUserRoleCreateOnly_automated_qaTeam1` | Tampil | Disabled, tooltip "You don't have permission to edit" | Disabled, tooltip "You don't have permission to edit" | Disabled, tooltip "You don't have permission to edit" | Hidden | Hidden |
| Hanya Update | `manageUserRoleUpdateOnly_automated_qaTeam1` | Hidden | Tampil dan aktif | Tampil dan aktif | Disabled, tooltip "You don't have permission to edit" | Tampil dan aktif | Tampil dan aktif |
| Hanya Delete | `manageUserRoleDeleteOnly_automated_qaTeam1` | Hidden | Disabled, tooltip "You don't have permission to edit" | Disabled, tooltip "You don't have permission to edit" | Tampil dan aktif | Hidden | Hidden |

Role lain yang diuji:

| Role | Akun | Yang diamati |
|---|---|---|
| Manage user and role (Full CRUD) | `manageUserRoleFull_automated_qaTeam1` | Aksi pada target Total Control diblokir |
| Total Control | `totalControl2_automated_qaTeam1` | Default User dan akun sendiri terlindungi |
| Default User | `totalControlGlobalSettings_automated_qaTeam1` | Akun sendiri terlindungi |
| No Role | `noRoleGlobalSettings_automated_qaTeam1` | Menu hidden, landing state, direct URL 403 |

- Entity Client
- Ada minimal satu target User Basic biasa (bukan Total Control, Read Only, Default User, atau akun yang login) di User List
- User "Siti Rahmawati" adalah Total Control biasa, bukan Default User dan bukan akun yang login
- Akun `noRoleGlobalSettings_automated_qaTeam1` punya Access yang mencakup Global Settings, tetapi belum diberi role apa pun dan bukan Total Control maupun Read Only
- URL User List diketahui
- Reset Authenticator adalah aksi yang endpoint-nya masih ditunda di modul. Spec ini hanya memverifikasi aksi itu tidak aktif dan tidak pernah menjalankannya

## Test Steps

### Read Only

1. Login sebagai Read Only
2. Verifikasi item sidebar `User` tampil
3. Buka sub-tab "Login User" di User List
4. Pada baris target biasa, verifikasi tiap elemen sesuai baris "Read Only" pada tabel keadaan elemen
5. Verifikasi row action `Reset Authenticator` Hidden dan checkbox baris Hidden

### Hanya Create

6. Login sebagai role hanya Create, lalu buka sub-tab "Login User" di User List
7. Pada baris target biasa, verifikasi tiap elemen sesuai baris "Hanya Create" pada tabel keadaan elemen

### Hanya Update

8. Login sebagai role hanya Update, lalu buka sub-tab "Login User" di User List
9. Pada baris target biasa, verifikasi tiap elemen sesuai baris "Hanya Update" pada tabel keadaan elemen

### Hanya Delete

10. Login sebagai role hanya Delete, lalu buka sub-tab "Login User" di User List
11. Pada baris target biasa, verifikasi tiap elemen sesuai baris "Hanya Delete" pada tabel keadaan elemen

### Full CRUD terhadap target Total Control

12. Login sebagai Full CRUD, lalu buka sub-tab "Login User" di User List
13. Pada baris "Siti Rahmawati", verifikasi checkbox, tombol row action `(⋯)`, dan detail/read tetap tampil dan aktif, tidak Hidden
14. Verifikasi Toggle Active [Global] Disabled dengan tooltip "Only Default User or Total Control can edit users with Total Control or Read Only access."
15. Verifikasi row action `Delete` Disabled dengan tooltip yang sama
16. Buka Modal Edit "Siti Rahmawati" dan verifikasi checkbox Access, yang menjadi titik masuk Remove Access, Disabled dengan tooltip yang sama
17. Klik `✕` untuk menutup modal
18. Verifikasi row action `Reset Authenticator` Disabled dengan tooltip yang sama

### Total Control terhadap Default User dan akun sendiri

19. Login sebagai Total Control, lalu buka sub-tab "Login User" di User List
20. Pada baris Default User, verifikasi Toggle Active [Global], row action `Delete`, checkbox Access di Modal Edit, dan row action `Reset Authenticator` semuanya Disabled dengan tooltip "Default User cannot be modified."
21. Pada baris akun sendiri, verifikasi Toggle Active [Global], row action `Delete`, checkbox Access di Modal Edit, dan row action `Reset Authenticator` semuanya Disabled dengan tooltip "You can't manage your own account from here."
22. Verifikasi tooltip pada keempat aksi persis sama untuk masing-masing target, dan tooltip Default User tidak pernah tertukar dengan tooltip akun sendiri

### Default User terhadap akun sendiri

23. Login sebagai Default User, lalu buka sub-tab "Login User" di User List
24. Pada baris Default User, yang merupakan akun sendiri, verifikasi Toggle Active [Global], row action `Delete`, checkbox Access di Modal Edit, dan row action `Reset Authenticator` semuanya Disabled dengan tooltip "You can't manage your own account from here."

### No Role

25. Login sebagai No Role
26. Verifikasi login berhasil
27. Verifikasi sidebar Global Settings menampilkan 0 menu dan item sidebar `User` Hidden
28. Verifikasi area konten menampilkan illustration dan pesan akses kosong
29. Ketik atau tempel URL User List langsung di address bar, tanpa klik menu
30. Verifikasi server membalas 403 Forbidden
31. Verifikasi toast error "You don't have permission to do this." muncul
32. Verifikasi UI di-refresh sehingga elemen yang tidak berhak tetap tersembunyi
33. Verifikasi halaman tidak dialihkan ke halaman unauthorized yang terpisah

## Notes

- Ini varian B (satu spec negatif per Role Matrix) untuk A/B testing dengan tim FE. Varian A adalah spec 015–020. Keduanya mencakup TC yang sama.
- Keadaan tiap elemen mengikuti tabel gerbang UI `user.md` §4.8: `[+ User]` digerbang Create, `Edit`, Toggle Active, `Resend`, dan `Pair/Unpair TAG` digerbang Update, dan `Delete` digerbang Delete. Disabled bila role tidak berhak tetapi elemennya masih terlihat, Hidden untuk Read Only dan untuk elemen yang tidak punya padanan tampilan.
- `Pair/Unpair TAG` untuk Read Only tidak diverifikasi karena TC-GS-USER-08 dan 85 tidak menyebutnya, sedangkan TC-GS-USER-581, 582, dan 583 menyebutnya untuk capability holder.
- Remove Access tidak punya row action. Titik masuknya adalah checkbox Access di Modal Edit (`GAP-239`). Untuk Read Only, Remove Access tidak tersedia karena `Edit` Hidden.
- TC-GS-USER-10 dan TC-GS-USER-12 diperlakukan sebagai kondisi akun yang sama (Access mencakup Global Settings, tanpa role). Ekspektasi TC-GS-USER-11 mengikuti default `error-handling-convention.md` bagian 2, karena PRD modul diam soal ini.
- Urutan role: Read Only lebih dulu karena berisi TC P0, dan No Role paling akhir karena membutuhkan navigasi ke URL langsung.
- Kegagalan keras pada satu role menghentikan spec, sehingga role sesudahnya tidak terperiksa.
- Cara skrip menjalankan banyak role di dalam satu spec diputuskan di tahap script.
- Lapisan frontend mencakup sebagian TC ini dengan payload izin yang di-mock (TC-GS-USER-FE-018, 020, 021, 022, 023, 154, 155, 157, 158, 159, 160). TC-GS-USER-486 dan 581–583 belum punya padanan frontend. Tumpang tindih disengaja untuk TC berprioritas P0 (`docs/e2e-conventions.md` bagian 2).
- Spec ini tidak membuat atau mengubah data, jadi tidak butuh cleanup.
