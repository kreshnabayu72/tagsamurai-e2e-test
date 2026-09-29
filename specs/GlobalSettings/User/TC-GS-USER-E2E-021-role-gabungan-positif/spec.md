---
id: TC-GS-USER-E2E-021-role-gabungan-positif
title: Semua role berhak menjalankan aksi yang menjadi haknya
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-09
  - TC-GS-USER-586
  - TC-GS-USER-07
  - TC-GS-USER-79
  - TC-GS-USER-82
  - TC-GS-USER-394
  - TC-GS-USER-395
  - TC-GS-USER-585
  - TC-GS-USER-584
  - TC-GS-USER-396
coverage:
  web: automated
---

# Semua role berhak menjalankan aksi yang menjadi haknya

## Prerequisites

Spec ini varian B untuk A/B testing dengan tim FE. Isinya menggabungkan spec positif Role Matrix (010–014) menjadi satu spec yang disusun per role. Tiap role login sekali, lalu menjalankan semua aksi yang menjadi haknya secara berurutan, dengan aksi Delete paling akhir. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

Role yang diuji dan aksinya:

| Role | Akun | Aksi yang dijalankan |
|---|---|---|
| Manage user and role (Full CRUD) | `manageUserRoleFull_automated_qaTeam1` | Create, Edit, Remove Access, Toggle Active, Delete |
| Total Control | `totalControl2_automated_qaTeam1` | Semua kontrol tampil dan aktif, aksi pada target Total Control aktif |
| Default User | `totalControlGlobalSettings_automated_qaTeam1` | Aksi pada target Total Control aktif |
| Manage user and role (hanya Create) | `manageUserRoleCreateOnly_automated_qaTeam1` | Create |
| Manage user and role (hanya Update) | `manageUserRoleUpdateOnly_automated_qaTeam1` | Edit, Remove Access, Toggle Active |
| Manage user and role (hanya Delete) | `manageUserRoleDeleteOnly_automated_qaTeam1` | Delete |

Target masing-masing role:

| Role | Target Edit | Target Remove Access | Target Toggle Active | Target Delete |
|---|---|---|---|---|
| Full CRUD | "Reza Pratama" | "Elisa Wijaya" | "Taufan Nugroho" | "Doddy Kusuma" |
| Hanya Update | "Rangga Pratama" | "Erna Wijaya" | "Tirta Nugroho" | — |
| Hanya Delete | — | — | — | "Danu Kusuma" |

- Entity Client
- Setiap target Edit dan Delete adalah User Basic biasa tanpa borrowed asset dan tanpa pending approval, dengan Position "Staff" untuk target Edit
- Setiap target Remove Access punya Access `[Global Settings, FAMS]`, tanpa aset atau approval di FAMS
- Setiap target Toggle Active adalah User Basic biasa yang aktif di semua produk
- Bukan Total Control, Read Only, Default User, maupun akun yang login untuk semua target di atas
- User "Siti Rahmawati" adalah Total Control biasa, bukan Default User dan bukan akun yang login
- Division "Finance" dan Position "Supervisor" ada di master data
- Custom Field "Blood Type" didefinisikan wajib, sehingga setiap create mengisinya
- Reset Authenticator adalah aksi yang endpoint-nya masih ditunda di modul. Spec ini hanya memverifikasi aksi itu aktif atau tidak aktif dan tidak pernah menjalankannya

## Test Steps

### Full CRUD

1. Login sebagai Full CRUD, lalu buka sub-tab "Login User" di User List
2. Verifikasi `[+ User]` tampil dan aktif
3. Klik `[+ User]`, isi First Name, Last Name, Email unik, Division "Finance", dan "Blood Type", pilih Access "Global Settings", lalu klik `[Submit]`
4. Verifikasi toast "User created successfully." muncul dan baris user baru muncul di User List
5. Buka Modal Edit "Reza Pratama", ubah Position menjadi "Supervisor", lalu klik `[Save]`
6. Verifikasi toast "Success, user has been updated." muncul dan baris "Reza Pratama" menampilkan Position "Supervisor"
7. Buka Modal Edit "Elisa Wijaya", hilangkan centang `FAMS` di field Access, lalu klik `[Save]`
8. Verifikasi tidak ada dialog tambahan, toast "Success, user has been updated." muncul, dan Access "Elisa Wijaya" menjadi `[Global Settings]`
9. Klik Toggle Active [Global] pada baris "Taufan Nugroho" untuk mematikannya
10. Verifikasi dialog "Deactivate User" muncul dengan isi "• Taufan Nugroho\nThis will deactivate user across all products. Are you sure you want to deactivate it?"
11. Klik `[Deactivate]` pada dialog
12. Verifikasi toast "Success, user has been deactivated." muncul dan Toggle Active [Global] "Taufan Nugroho" menjadi OFF
13. Klik `Delete` pada baris "Doddy Kusuma"
14. Verifikasi dialog "Delete User" muncul dengan isi "• Doddy Kusuma\nHistorical transaction data will be preserved.\nThis action cannot be undone. Are you sure you want to delete it?"
15. Klik `[Delete]` pada dialog
16. Verifikasi toast "Success, user has been deleted." muncul dan baris "Doddy Kusuma" tidak lagi muncul di User List

### Total Control

17. Login sebagai Total Control, lalu buka sub-tab "Login User" di User List
18. Verifikasi `[+ User]`, checkbox baris, row action `Edit`, `Delete`, `Resend`, dan Toggle Active [Global] semuanya tampil dan aktif
19. Pada baris "Siti Rahmawati", verifikasi Toggle Active [Global] dan row action `Delete` aktif
20. Buka Modal Edit "Siti Rahmawati" dan verifikasi checkbox Access, yang menjadi titik masuk Remove Access, aktif
21. Klik `✕` untuk menutup modal
22. Verifikasi row action `Reset Authenticator` pada baris "Siti Rahmawati" aktif

### Default User

23. Login sebagai Default User, lalu buka sub-tab "Login User" di User List
24. Pada baris "Siti Rahmawati", verifikasi Toggle Active [Global] dan row action `Delete` aktif
25. Buka Modal Edit "Siti Rahmawati" dan verifikasi checkbox Access aktif
26. Klik `✕` untuk menutup modal
27. Verifikasi row action `Reset Authenticator` pada baris "Siti Rahmawati" aktif

### Hanya Create

28. Login sebagai role hanya Create, lalu buka sub-tab "Login User" di User List
29. Klik `[+ User]`, isi First Name, Last Name, Email unik, Division "Finance", dan "Blood Type", pilih Access "Global Settings", lalu klik `[Submit]`
30. Verifikasi toast "User created successfully." muncul dan baris user baru muncul di User List

### Hanya Update

31. Login sebagai role hanya Update, lalu buka sub-tab "Login User" di User List
32. Buka Modal Edit "Rangga Pratama", ubah Position menjadi "Supervisor", lalu klik `[Save]`
33. Verifikasi toast "Success, user has been updated." muncul dan baris "Rangga Pratama" menampilkan Position "Supervisor"
34. Buka Modal Edit "Erna Wijaya", hilangkan centang `FAMS` di field Access, lalu klik `[Save]`
35. Verifikasi tidak ada dialog tambahan, toast "Success, user has been updated." muncul, dan Access "Erna Wijaya" menjadi `[Global Settings]`
36. Klik Toggle Active [Global] pada baris "Tirta Nugroho" untuk mematikannya
37. Verifikasi dialog "Deactivate User" muncul, lalu klik `[Deactivate]`
38. Verifikasi toast "Success, user has been deactivated." muncul dan Toggle Active [Global] "Tirta Nugroho" menjadi OFF

### Hanya Delete

39. Login sebagai role hanya Delete, lalu buka sub-tab "Login User" di User List
40. Klik `Delete` pada baris "Danu Kusuma"
41. Verifikasi dialog "Delete User" muncul, lalu klik `[Delete]`
42. Verifikasi toast "Success, user has been deleted." muncul dan baris "Danu Kusuma" tidak lagi muncul di User List

## Notes

- Ini varian B (satu spec positif per Role Matrix) untuk A/B testing dengan tim FE. Varian A adalah spec 010–014. Keduanya mencakup TC yang sama. Setelah tim FE memilih, varian yang tidak dipakai dihapus. Nama target sengaja berbeda dari varian A supaya kedua varian bisa dijalankan di environment yang sama tanpa saling mengubah data.
- Role Total Control tidak menjalankan Create, Edit, Remove Access, Toggle Active, dan Delete di sini, karena aksi itu sudah dicek di spec `TC-GS-USER-E2E-002` (Create), `TC-GS-USER-E2E-005` (Delete), `TC-GS-USER-E2E-008` (Toggle Active), dan `TC-GS-USER-E2E-009` (Remove Access).
- Urutan di dalam tiap role: Delete paling akhir, sesuai `docs/e2e-conventions.md` bagian 3, prinsip 5.
- Remove Access tidak punya row action. Titik masuknya adalah checkbox Access di Modal Edit (`GAP-239`).
- Tumpang tindih dengan lapisan frontend disengaja untuk TC berprioritas P0 (`docs/e2e-conventions.md` bagian 2). TC-GS-USER-584, 585, dan 586 belum punya padanan frontend.
- Kegagalan keras (elemen tidak ditemukan, halaman tidak terbuka) pada satu role menghentikan spec, sehingga role sesudahnya tidak terperiksa. Karena itu role dengan prioritas tertinggi ada di awal.
- Cara skrip menjalankan banyak role di dalam satu spec diputuskan di tahap script.
- User yang dibuat di langkah 3 dan 29 harus dihapus saat cleanup, walaupun spec gagal di tengah. Target Edit, Remove Access, dan Toggle Active harus dikembalikan atau di-seed ulang setelah run.
