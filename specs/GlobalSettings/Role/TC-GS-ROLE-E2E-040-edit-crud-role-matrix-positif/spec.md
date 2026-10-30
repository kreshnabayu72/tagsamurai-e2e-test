---
id: TC-GS-ROLE-E2E-040-edit-crud-role-matrix-positif
title: "Role Matrix: Edit CRUD Positif oleh Total Control dan Manage user and role dengan Update"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-101
  - TC-GS-ROLE-102
  - TC-GS-ROLE-103
coverage:
  web: automated
---

# Role Matrix: Edit CRUD Positif oleh Total Control dan Manage user and role dengan Update

## Prerequisites

- Mode: FE+BE.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti pernyataan hook suite di `suite.md`.
- Akun aktor hook `before`: Ahmad Fauzi (Total Control, Pre-setup #1), email `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan di hook `before`; hook `beforeEach` membuka Global Settings > Role & Permission > Tab System. Karena spec berakhir di akun Hendra Wijaya, hook `after` mengembalikan sesi ke akun default suite (Ahmad Fauzi).
- Langkah tiap role berbeda (Detail role, user target, dan checkbox yang diubah), sehingga spec ditulis per blok role, bukan perulangan.

Role yang diuji (Tabel Data Uji Pre-setup):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-ROLE-101, TC-GS-ROLE-102 | Total Control | Ahmad Fauzi | `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-ROLE-103 | Manage user and role C/R/U/D | Hendra Wijaya | `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD` |

- Env baru yang harus didaftarkan di `executionConfig.environmentVariables` dan `.env.example`: `GS_ROLE_MANAGE_CRUD_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup #10: Doni Pratama (Staff, IT; bukan Total Control atau Read Only): Manage TAG Read checked dan Update unchecked, Manage files Read dan Delete checked. Target TC-GS-ROLE-101 dan TC-GS-ROLE-102.
- Data Given untuk TC-GS-ROLE-103 (disiapkan di hook `before` lewat seeding API, kemampuan disediakan tim FE/BE; dipakai sebagai precondition TC): Wawan Setiawan (Pre-setup #11) memiliki baris `Manage hardware` dengan Read checked; Wawan Setiawan tidak Total Control atau Read Only.
- Data yang diubah spec: Update baris `Manage TAG` Doni Pratama (menjadi checked), Delete baris `Manage files` Doni Pratama (menjadi unchecked), dan Create baris `Manage hardware` Wawan Setiawan (menjadi checked). Hook `after` memulihkan Update `Manage TAG` Doni Pratama ke unchecked, Delete `Manage files` Doni Pratama ke checked, dan menghapus baris `Manage hardware` Wawan Setiawan sehingga Wawan kembali menjadi kandidat Pre-setup #11.
- Kemampuan teknis: memuat ulang halaman; Logout dan login ulang di browser yang sama.
- State global: tidak ada yang diubah (suite berjalan serial, `suite.md`).

## Test Steps

### TC-GS-ROLE-101: Total Control mencentang Update pada target biasa

1. Klik Role Name `Manage TAG`
2. Centang Update baris Doni Pratama
3. Verifikasi toast sukses "Success, permissions have been updated."
4. Verifikasi tombol `[Save]` tidak tampil
5. Verifikasi tidak ada dialog yang tampil
6. Muat ulang halaman
7. Verifikasi Update baris Doni Pratama checked
8. Verifikasi Read baris Doni Pratama checked

### TC-GS-ROLE-102: Total Control menghapus centang Delete pada target biasa

9. Klik segmen `System` pada breadcrumb untuk membuka Tab System
10. Klik Role Name `Manage files`
11. Hapus centang Delete baris Doni Pratama
12. Verifikasi toast sukses "Success, permissions have been updated."
13. Muat ulang halaman
14. Verifikasi Delete baris Doni Pratama unchecked
15. Verifikasi Read baris Doni Pratama checked

### TC-GS-ROLE-103: Manage user and role dengan Update mencentang Create

16. Logout, lalu login sebagai Manage user and role C/R/U/D (Hendra Wijaya)
17. Buka Global Settings > Role & Permission > Tab System
18. Klik Role Name `Manage hardware`
19. Centang Create baris Wawan Setiawan
20. Verifikasi toast sukses "Success, permissions have been updated."
21. Muat ulang halaman
22. Verifikasi Create baris Wawan Setiawan checked

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC sumber.
- Spec Role Matrix positif (bagian 3a konvensi): aksi Edit CRUD berhasil untuk Total Control dan Manage user and role dengan Update. Kombinasi role lain tanpa TC sumber tidak ditambahkan.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Tab System lewat breadcrumb (langkah 9) serta Logout dan login ke akun berikutnya (langkah 16 dan 17).
- Langkah 4 dan 5 (tombol `[Save]` dan dialog tidak ada) didahului langkah 3 (toast sukses, tanda respons server selesai) sebagai anchor positif.
- Temuan untuk QA:
  - TC-GS-ROLE-101 Post Condition (log Edit Field Update, Doni Pratama dapat Audit/Combine/Separate TAG pada request berikutnya) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-GS-ROLE-102 dan TC-GS-ROLE-103 tidak punya Post Condition.
  - TC-GS-ROLE-103 langkah 1 hanya "Centang Create" dan Expected b "Create checked setelah reload" tanpa langkah reload di TC; spec menambah langkah muat ulang halaman (langkah 21) untuk mengamati Expected b.
