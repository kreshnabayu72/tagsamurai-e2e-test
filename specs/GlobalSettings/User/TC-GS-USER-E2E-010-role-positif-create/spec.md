---
id: TC-GS-USER-E2E-010-role-positif-create
title: Role berhak Create berhasil membuat user
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-07
  - TC-GS-USER-13
  - TC-GS-USER-394
  - TC-GS-USER-586
coverage:
  web: automated
---

# Role berhak Create berhasil membuat user

## Prerequisites

Spec ini dijalankan untuk setiap role pada tabel. Langkahnya identik, hanya akun login yang berbeda. Kredensial akun diambil lewat `Spectra.env`, tidak ditulis di spec.

Role yang diuji:

| Role | Akun | Keterangan |
|---|---|---|
| Total Control | `totalControl2_automated_qaTeam1` | Total Control biasa, bukan Default User |
| Manage user and role (Full CRUD) | `manageUserRoleFull_automated_qaTeam1` | Bukan Total Control |
| Manage user and role (hanya Create) | `manageUserRoleCreateOnly_automated_qaTeam1` | Read baseline dan Create, tanpa Update dan Delete |

- Entity Client
- Division "Finance" ada di master data
- Custom Field "Blood Type" didefinisikan wajib, sehingga setiap create mengisinya
- Email user baru unik per role per run

## Test Steps

Lakukan langkah 1–7 untuk setiap role pada tabel "Role yang diuji".

1. Login sebagai role yang diuji, lalu buka sub-tab "Login User" di User List
2. Verifikasi `[+ User]` tampil dan aktif
3. Klik `[+ User]` untuk membuka modal Create
4. Isi First Name, Last Name, Email unik, Division "Finance", dan "Blood Type", lalu pilih Access "Global Settings"
5. Klik `[Submit]`
6. Verifikasi toast "User created successfully." muncul
7. Verifikasi baris user baru muncul di User List

## Notes

- Ini spec positif Create dari Role Matrix (`docs/e2e-conventions.md` bagian 3a). Pasangan negatifnya adalah `TC-GS-USER-E2E-015-role-negatif-create`.
- Role Total Control mengulang alur yang sudah ada di `TC-GS-USER-E2E-002` (TC-GS-USER-13). Tumpang tindih ini disengaja, karena Role Matrix membandingkan semua role pada langkah yang sama.
- Cara skrip menjalankan banyak role (perulangan di dalam satu `it()` atau beberapa kali run) diputuskan di tahap script.
- Lapisan frontend mencakup TC ini dengan payload izin yang di-mock (TC-GS-USER-FE-017, 024). TC-GS-USER-07 dan 13 berprioritas P0, jadi tumpang tindih disengaja (`docs/e2e-conventions.md` bagian 2).
- Semua user yang dibuat harus dihapus saat cleanup oleh akun yang berhak menghapus, walaupun spec gagal di tengah.
