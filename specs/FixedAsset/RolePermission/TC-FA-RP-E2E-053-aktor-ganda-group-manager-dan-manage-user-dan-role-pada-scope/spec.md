---
id: TC-FA-RP-E2E-053-aktor-ganda-group-manager-dan-manage-user-dan-role-pada-scope
title: "Role Matrix: Aktor ganda Group Manager dan Manage user & role pada scope berbeda"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1026
coverage:
  web: automated
---

# Role Matrix: Aktor ganda Group Manager dan Manage user & role pada scope berbeda

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:
| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-FA-RP-1026 | Group Manager di `Helpdesk` sekaligus Manage user & role (Group, Update) di `Logistics Warehouse` (seed API) | tidak tertulis di Pre-setup TC | disediakan tim FE (tidak tertulis di Pre-setup TC) | `Spectra.env.FA_GMMUR_PASSWORD` |
- Login di hook `before` spec ini sebagai akun pada tabel; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`). Nama env `FA_GMMUR_PASSWORD` adalah usulan, belum ada di `suite.md`; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: #39 (Detail Role Group Role `Manage files` terisi: Ahmad Fauzi dan Dimas Pranata di `Data Center`, Budi Santoso di `Helpdesk`, Citra Lestari di `Head Office`, Endah Susanti di `Rack A1`, Fitri Handayani di `Dock 1`, serta baris pola Group Role pada setiap group) dan #18 (pohon group Company Alpha).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_GMMUR_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1026: Aktor ganda Group Manager dan Manage user & role pada scope berbeda: wewenang aditif per scope

1. Klik Tab `System`
2. Buka Detail Role `Manage files` pada section Group Role
3. Amati Sidebar Group Tree
4. Verifikasi node `Helpdesk`, `Logistics Warehouse`, dan `Dock 1` dapat dipilih
5. Verifikasi `IT Infrastructure` dan `Head Office` tampil non-selectable sebagai ancestor
6. Verifikasi `Data Center` dan `Rack A1` tidak dirender di Sidebar Group Tree
7. Klik `All Groups`
8. Verifikasi baris Budi Santoso (`Helpdesk`) dan Fitri Handayani (`Dock 1`) tampil
9. Verifikasi baris Ahmad Fauzi dan Dimas Pranata (`Data Center`), Citra Lestari (`Head Office`), dan Endah Susanti (`Rack A1`) tidak tampil
10. Verifikasi baris pola Group Role `Manage files` (Pre-setup #39) tampil hanya pada `Helpdesk`, `Logistics Warehouse`, dan `Dock 1` (lima baris per node, 15 baris)
11. Verifikasi baris pola Group Role `Manage files` tidak tampil pada `Data Center`, `Rack A1`, `IT Infrastructure`, dan `Head Office`
12. Amati checkbox CRUD baris Budi Santoso (`Helpdesk`) dan baris Fitri Handayani (`Dock 1`)
13. Verifikasi checkbox CRUD kedua baris Enabled; wewenang tiap peran berlaku di scope-nya sendiri (Group Manager di `Helpdesk`, Manage user & role di `Dock 1`)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 13 langkah.
- Langkah penghubung (S-03): langkah 1. Akun aktor pertama sudah login di hook `before` (S-07).
- Spec Role Matrix (bagian 3a) satu blok role: satu akun ganda yang tidak ada di Tabel Pre-setup TC; tidak ada ganti akun.
- Absence baris pada langkah 9 didahului langkah 8 yang membuktikan baris lain pada tabel yang sama sudah tampil; absence baris pola pada langkah 11 didahului langkah 10 yang membuktikan baris pola pada node lain sudah tampil (butir 8b.2).
- Temuan untuk QA:
  - TC-FA-RP-1026 precondition a: akun "satu akun Group Manager di `Helpdesk` sekaligus Manage user & role (Group, Update) di `Logistics Warehouse`" tidak ada di Pre-setup #1 sampai #11; email dan nama env password tidak tertulis di TC. Spec menulisnya "disediakan tim FE" tanpa akun karangan (S-13).
  - TC-FA-RP-1026 precondition b menyebut user berada di Tab System, sedangkan halaman dibuka di tab awal oleh hook `beforeEach`; langkah 1 adalah langkah penghubung.
