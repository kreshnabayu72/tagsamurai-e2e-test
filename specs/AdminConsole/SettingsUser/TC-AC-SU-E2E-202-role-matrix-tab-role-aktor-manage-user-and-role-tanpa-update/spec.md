---
id: TC-AC-SU-E2E-202-role-matrix-tab-role-aktor-manage-user-and-role-tanpa-update
title: "Role Matrix: Tab Role, Aktor Manage user and role tanpa Update"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-65
coverage:
  web: automated
---

# Role Matrix: Tab Role, Aktor Manage user and role tanpa Update

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage user and role Read saja (U=false, Pre-setup #5) `manageUserRoleRead_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_READ_PASSWORD`.
- Env var `AC_MUR_READ_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan pemilik repo (nama ditetapkan penulis spec). Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini sebagai Manage user and role (Read saja, U=false); halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Role yang diuji:

| TC | Role | Akun |
|---|---|---|
| TC-AC-SU-65 | Manage user and role (U=false) | Pre-setup #5 |

- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-65 | `Region A` | `Region A {runId}-202` | - | Group |
| TC-AC-SU-65 | `Rudi Hartono` | `Rudi Hartono {runId}-202` | `rudihartono+{runId}-202@qwertysystem.net` | tanpa tingkat akses (kosong); Group Role `Manage allocation` aktif di `Region A {runId}-202` |

- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-65: Tab Role, aktor Manage user and role tanpa Update

1. Ketik Search `Rudi Hartono {runId}-202`, tekan Enter
2. Klik Name `Rudi Hartono {runId}-202`
3. Hover switch dan checkbox C/U/D baris `Manage group` pada sub-tab Global Role
4. Verifikasi switch dan C/U/D tampil
5. Verifikasi switch dan C/U/D disabled dengan tooltip `You don't have permission to edit.`
6. Klik sub-tab Group Role
7. Verifikasi `[Detail]` tampil
8. Verifikasi `[Assign Group]` tidak dirender
9. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
10. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16), langkah kembali ke daftar lewat Breadcrumb, langkah 10 (reset Search). Layar awal dibuka hook `beforeEach` suite; sub-tab Global Role aktif secara default pada Tab Role.
- Pembagian TC Role Matrix Tab Role: TC-AC-SU-62 di spec 021, TC-AC-SU-63 dan 64 di spec 201, TC-AC-SU-65 di spec ini.
- Temuan untuk QA:
  - TC-AC-SU-65 mensyaratkan `Rudi Hartono` punya Group Role `Manage allocation` aktif di `Region A`; spec men-seed record itu.
  - Nama user TC (`Region A`, `Rudi Hartono`) dipakai sebagai nama bersuffix `{runId}-202` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
