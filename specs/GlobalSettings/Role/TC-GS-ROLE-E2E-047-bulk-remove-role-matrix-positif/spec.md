---
id: TC-GS-ROLE-E2E-047-bulk-remove-role-matrix-positif
title: "Role Matrix Positif: Bulk Remove Baris Role Regular oleh Total Control dan Manage User and Role dengan Update"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-128
  - TC-GS-ROLE-132
coverage:
  web: automated
---

# Role Matrix Positif: Bulk Remove Baris Role Regular oleh Total Control dan Manage User and Role dengan Update

## Prerequisites

- Mode: FE+BE.
- Langkah tiap role berbeda (Detail dan baris target berbeda), sehingga spec ditulis per blok role, bukan perulangan (bagian 3a konvensi). Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables`.

Role yang diuji (Tabel Data Uji Pre-setup):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-ROLE-128 | Total Control | Ahmad Fauzi | `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-ROLE-132 | Manage user and role C/R/U/D | Hendra Wijaya | `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD` |

- Akun hook `before`: Ahmad Fauzi (Total Control, akun default suite). Hendra Wijaya login lewat langkah ganti akun 11; hook `after` mengembalikan sesi ke Ahmad Fauzi.
- Environment variable: `GS_TC_PASSWORD` (sudah terdaftar). Env baru yang belum terdaftar di `spectra.config.ts` dan `.env.example`: `GS_ROLE_MANAGE_CRUD_PASSWORD` (password Hendra Wijaya, Manage user and role C/R/U/D).
- Layar awal (hook `beforeEach`): Global Settings > Role & Permission > System > Detail `Manage hardware`. Hendra Wijaya membuka Detail `Manage TAG` lewat langkah 12.
- Data Pre-setup yang dipakai: Nina Kartika dan Wawan Setiawan (baris 11, kandidat tanpa access level), Agus Salim (baris 9, user tanpa role), Hendra Wijaya (baris 5; punya baris role Manage TAG).
- Given (hook `before`, lewat seeding API):
  - Detail `Manage hardware`: Nina Kartika dan Agus Salim di-assign baris Manage hardware (Given TC-GS-ROLE-128). Jumlah Users role `Manage hardware` di Tab System dicatat setelah seeding sebagai N (turunan seeding, bukan dibaca dari tabel satu halaman).
  - Detail `Manage TAG`: Wawan Setiawan dan Nina Kartika di-assign baris Manage TAG (hasil alur Assign Role, dependensi TC-GS-ROLE-94).
- Baris yang dihapus aksi spec adalah baris yang dibuat seeding di atas, sehingga Pre-setup kembali ke kondisi awal tanpa baris role. Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): hapus baris Manage hardware milik Nina Kartika dan Agus Salim serta baris Manage TAG milik Wawan Setiawan dan Nina Kartika yang masih ada.
- Kemampuan teknis: membaca kolom Users pada Tab System; logout dan login dua akun dalam satu spec.
- Kemampuan teknis (seeding): seeding API untuk akses level, baris role, dan data user disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD dan tidak dikarang di spec.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-GS-ROLE-128: Bulk Remove baris regular oleh Total Control

1. Centang baris `Nina Kartika`
2. Centang baris `Agus Salim`
3. Klik `Bulk Action`
4. Klik `Remove`
5. Klik `[Remove]`
6. Verifikasi toast sukses `Success, user has been removed.`
7. Verifikasi baris `Nina Kartika` dan `Agus Salim` hilang dari Detail `Manage hardware`
8. Verifikasi Bulk Action Bar tertutup
9. Buka Tab System
10. Verifikasi kolom Users role `Manage hardware` berkurang 2 (N dikurangi 2)

### TC-GS-ROLE-132: Bulk Remove oleh aktor Manage user and role dengan Update

11. Logout, lalu login sebagai Hendra Wijaya (Manage user and role C/R/U/D) dengan `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD`
12. Buka Global Settings > Role & Permission > System > Detail `Manage TAG`
13. Centang baris `Wawan Setiawan`
14. Centang baris `Nina Kartika`
15. Klik `Bulk Action`
16. Klik `Remove`
17. Verifikasi dialog konfirmasi Bulk Remove varian tanpa baris Total Control/Read Only tampil
18. Klik `[Remove]`
19. Verifikasi toast sukses `Success, user has been removed.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix positif (bagian 3a konvensi): aksi berhasil untuk Total Control dan satu role spesifik yang berhak (Manage user and role dengan Update). Langkah kedua role tidak identik (Detail dan baris target berbeda), sehingga ditulis per blok role.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): Buka Tab System (langkah 9; Langkah 4 TC-GS-ROLE-128) serta ganti akun ke Hendra Wijaya dan membuka Detail `Manage TAG` (langkah 11 dan 12).
- Baseline TC-GS-ROLE-128 Expected c: N (jumlah Users `Manage hardware`) dicatat dari seeding sebelum aksi; asersi memakai selisih 2, bukan angka absolut.
- Kombinasi role yang tidak punya TC sumber (Fajar Nugroho Read, Lina Marlina tanpa Update, Read Only) tidak ditambahkan.
- Temuan untuk QA:
  - TC-GS-ROLE-132 Expected a (`Dialog varian tanpa baris TC/RO`) tidak menyebut judul, body, atau tombol dialog; spec hanya mengasersi bahwa varian dialog tersebut tampil.
  - TC-GS-ROLE-132 Dependensi TC-GS-ROLE-94 (Wawan Setiawan dan Nina Kartika punya baris Manage TAG) dipenuhi lewat seeding API, bukan dengan menyalin langkah TC-GS-ROLE-94.
  - TC-GS-ROLE-132 tidak menyebut verifikasi hilangnya baris sesudah `[Remove]`; hanya toast yang diasersi (sesuai Expected b).
