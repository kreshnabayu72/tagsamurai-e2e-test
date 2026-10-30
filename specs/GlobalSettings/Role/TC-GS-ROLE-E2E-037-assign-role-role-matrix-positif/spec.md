---
id: TC-GS-ROLE-E2E-037-assign-role-role-matrix-positif
title: "Role Matrix: Assign Role Positif oleh Total Control dan Manage user and role dengan Update"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-94
  - TC-GS-ROLE-96
coverage:
  web: automated
---

# Role Matrix: Assign Role Positif oleh Total Control dan Manage user and role dengan Update

## Prerequisites

- Mode: FE+BE.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti pernyataan hook suite di `suite.md`.
- Akun aktor hook `before`: Ahmad Fauzi (Total Control, Pre-setup #1), email `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login Ahmad Fauzi dilakukan di hook `before`; hook `beforeEach` membuka Global Settings > Role & Permission > Tab System. Karena spec berakhir di akun Hendra Wijaya, hook `after` mengembalikan sesi ke akun default suite (Ahmad Fauzi).
- Langkah tiap role berbeda (Detail role, user target, dan hal yang diperiksa), sehingga spec ditulis per blok role, bukan perulangan.

Role yang diuji (Tabel Data Uji Pre-setup):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-ROLE-94 | Total Control | Ahmad Fauzi | `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-ROLE-96 | Manage user and role C/R/U/D | Hendra Wijaya | `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD` |

- Env baru yang harus didaftarkan di `executionConfig.environmentVariables` dan `.env.example`: `GS_ROLE_MANAGE_CRUD_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tidak diubah kecuali dicatat di bawah): Wawan Setiawan dan Nina Kartika (Pre-setup #11, kandidat: Active, Access Global Settings dicentang, tanpa access level, tanpa baris role); Hendra Wijaya punya baris role Manage user and role C, R, U, D (Pre-setup #5).
- Data yang diubah spec: baris `Manage TAG` untuk Wawan Setiawan dan Nina Kartika, serta baris `Manage files` untuk Nina Kartika. Hook `after` menghapus ketiga baris itu lewat seeding API (kemampuan disediakan tim FE/BE) sehingga keduanya kembali ke kondisi kandidat Pre-setup #11.
- Kemampuan teknis: Logout dan login ulang di browser yang sama; seeding API untuk menghapus baris role (disediakan tim FE/BE).
- State global: tidak ada yang diubah (suite berjalan serial, `suite.md`).

## Test Steps

### TC-GS-ROLE-94: Total Control meng-assign Manage TAG ke beberapa user

1. Catat jumlah Users baris `Manage TAG` di Tab System (N94)
2. Klik Role Name `Manage TAG`
3. Klik `[+ Assign]`
4. Centang Wawan Setiawan
5. Centang Nina Kartika
6. Klik `[Assign]`
7. Verifikasi toast sukses "Success, role has been assigned."
8. Verifikasi baris Wawan Setiawan tampil di Detail `Manage TAG` dengan Read checked dan disabled
9. Verifikasi Update baris Wawan Setiawan unchecked
10. Verifikasi baris Nina Kartika tampil di Detail `Manage TAG` dengan Read checked dan disabled
11. Verifikasi Update baris Nina Kartika unchecked
12. Verifikasi kolom Create dan Delete tidak tampil (Hidden)
13. Klik segmen `System` pada breadcrumb untuk membuka Tab System
14. Verifikasi Users baris `Manage TAG` sama dengan N94 ditambah 2

### TC-GS-ROLE-96: Manage user and role dengan Update meng-assign Role

15. Logout, lalu login sebagai Manage user and role C/R/U/D (Hendra Wijaya)
16. Buka Global Settings > Role & Permission > Tab System
17. Klik Role Name `Manage files`
18. Klik `[+ Assign]`
19. Verifikasi Nina Kartika tampil di pool popup Assign Role
20. Verifikasi Hendra Wijaya tidak ada di pool popup Assign Role
21. Centang Nina Kartika
22. Klik `[Assign]`
23. Verifikasi toast sukses "Success, role has been assigned."
24. Verifikasi baris Nina Kartika tampil di Detail `Manage files`
25. Verifikasi Read baris Nina Kartika checked
26. Verifikasi Delete baris Nina Kartika unchecked

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC sumber untuk report per langkah.
- Spec Role Matrix positif (bagian 3a konvensi): aksi Assign Role berhasil untuk Total Control dan Manage user and role dengan Update. Langkah tiap role berbeda, sehingga ditulis per blok role. Kombinasi role lain tanpa TC sumber tidak ditambahkan.
- Langkah penghubung (tanpa awalan `Verifikasi`): mencatat jumlah Users awal (langkah 1), membuka Tab System lewat breadcrumb (langkah 13), serta Logout dan login ke akun berikutnya (langkah 15 dan 16). Baseline N94 dicatat sebelum aksi karena TC-GS-ROLE-94 Expected d menyatakan "bertambah 2".
- Verifikasi Hendra Wijaya tidak ada di pool (langkah 20) didahului langkah 19 sebagai anchor positif pada surface yang sama.
- Temuan untuk QA:
  - TC-GS-ROLE-94 Post Condition (log Assign per user, menu TAG tampil untuk kedua user pada request berikutnya) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-GS-ROLE-96: Post Condition kosong; TC tidak menyebut kondisi awal Nina Kartika (diasumsikan kandidat Pre-setup #11 tanpa baris `Manage files`).
  - TC-GS-ROLE-94 tidak menyebut cara membaca jumlah Users awal; spec mencatatnya dari Tab System sebelum aksi.
