---
id: TC-FA-RP-E2E-367-role-matrix-kontrol-baris-pola-gm-terkunci-bagi-manage-user-dan-role-group-update
title: "Role Matrix: kontrol baris pola GM terkunci pada node descendant dan tabel Role Transaksi bagi Manage user & role Group Update (2/2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-1195
coverage:
  web: automated
---

# Role Matrix: kontrol baris pola GM terkunci pada node descendant dan tabel Role Transaksi bagi Manage user & role Group Update (2/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage user & role (Group, Update) Gita Maharani; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite).
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (berkas belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-1195 | Manage user & role (Group, Update) di `IT Infrastructure` | Manage user & role Group | Gita Maharani (Pre-setup #7) | `murGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GROUP_PASSWORD` |

- Data Pre-setup yang dibaca: #7 (Gita Maharani, aktor; Group Role `Manage user & role` Read dan Update di `IT Infrastructure`), #5 (Fajar Nugroho, Group Manager `IT Infrastructure`), #13 (Kevin Susanto, target; Group Manager hanya di `Data Center`), #18 (pohon group Company Alpha), dan #19 (seed Role Transaksi Disposal pada `IT Infrastructure`). Kevin Susanto memegang baris pola GM di `Data Center` dan `Rack A1` (Group Role katalog selain `Manage user & role` dengan CRUD penuh sesuai kolom berlaku; Role Transaksi Asset Admin dan Approver pada tiap Jenis Transaksi) dan baris non-pola: Group Role `Manage user & role` di `Data Center` dan Group Role `Manage files` Read dan Delete di `Helpdesk`. Seed Group Manager yang menulis baris pola itu disediakan tim FE/BE (kemampuan seeding API, tanpa endpoint karangan).
- Kemampuan teknis: hover pada elemen Disabled atau Enabled untuk membaca tooltip.
- State global yang diubah: tidak ada. Spec tidak membuat, mengubah, atau menghapus data (tanpa data Dinamis); menu baris dibuka lalu ditutup dengan Esc tanpa menjalankan Remove. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_MUR_GROUP_PASSWORD` dan `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1195: baris pola GM pada descendant Disabled, baris non-pola Enabled (aktor Manage user & role Group Update Gita Maharani)

1. Klik Tab System
2. Klik Role Name `Manage files` pada section Group Role
3. Klik node `Rack A1` di Sidebar Group Tree
4. Ketik Search `Kevin Susanto`, tekan Enter
5. Hover checkbox Delete pada baris Kevin Susanto
6. Verifikasi checkbox Delete baris Kevin Susanto Disabled dengan tooltip `You don't have permission to edit.`
7. Klik `⋯` pada baris Kevin Susanto
8. Hover `Remove` pada menu baris
9. Verifikasi aksi `Remove` Disabled dengan tooltip `You don't have permission to edit.`
10. Tutup menu baris dengan Esc
11. Hover checkbox baris Kevin Susanto
12. Verifikasi checkbox baris Kevin Susanto Disabled dengan tooltip `You don't have permission to edit.`
13. Klik `(←)` pada kotak Search
14. Klik node `Helpdesk` di Sidebar Group Tree
15. Ketik Search `Kevin Susanto`, tekan Enter
16. Verifikasi baris Kevin Susanto non-pola di `Helpdesk` Enabled
17. Buka Fixed Asset > Settings > Role & Permission > System dan klik Role Name `Manage user & role` pada section Group Role
18. Klik node `Data Center` di Sidebar Group Tree
19. Ketik Search `Kevin Susanto`, tekan Enter
20. Verifikasi baris `Manage user & role` Kevin Susanto di `Data Center` Enabled
21. Buka Fixed Asset > Settings > Role & Permission > Transaction Role
22. Klik node `Rack A1` di Sidebar Group Tree
23. Klik sub-tab `Disposal`
24. Klik `⋯` pada baris Kevin Susanto di section Approver
25. Hover `Remove` pada menu baris
26. Verifikasi aksi `Remove` baris Approver pola Kevin Susanto Disabled dengan tooltip `You don't have permission to edit.`
27. Tutup menu baris dengan Esc

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 27 langkah.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`), sehingga aktor Manage user & role (Group, Update) ada di spec ini dan aktor Group Manager di spec 358. Spec memuat matriks visibilitas (Disabled dan Enabled pada satu daftar elemen), maka title tanpa kata "Positif" atau "Negatif"; `caseType` Negative mengikuti TC (Tipe Security).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): klik tab, buka Detail Role, klik node, buka tab Transaction Role dan sub-tab (langkah 1 sampai 3, 14, 17, 18, 21 sampai 23); hover untuk membaca tooltip (langkah 5, 8, 11, 25); membuka menu baris `⋯` (langkah 7 dan 24) dan menutupnya dengan Esc (langkah 10 dan 27); klik `(←)` pada kotak Search (langkah 13).
- Search (R-16, bagian 8b butir 9 dan 13): langkah 4, 15, dan 19 adalah langkah penghubung untuk menemukan baris Kevin Susanto, karena tabel Detail Role dapat memuat lebih dari satu halaman. Tabel Role Transaksi section Approver pada `Rack A1` tidak dicari lewat Search: section itu memuat baris pola Default User, Total Control, dan Group Manager (jumlahnya di bawah sepuluh baris, satu halaman).
- Asersi Disabled dan Enabled hanya diamati pada baris yang tampil di tabel; tidak ada asersi absence.
- Pembagian TC lintas spec: TC-FA-RP-1195 ada di spec ini (aktor Manage user & role, Group, Update; TC menyebut "diulang pada akun Manage user & role ... dengan hasil sama") dan spec 358 (aktor Group Manager). Spec 368 memuat TC-FA-RP-1196.
- Temuan untuk QA:
  - TC-FA-RP-1195 Expected b dan c tidak menyebut elemen yang dicek pada baris "Enabled" (langkah 16 dan 20); spec mengasersi Enabled pada baris tanpa memerinci elemen. Expected a menyebut tiga elemen (checkbox Delete, aksi `Remove`, checkbox baris) dan tooltip dibaca pada tiap elemen.
  - TC-FA-RP-1195 langkah 1 mengandaikan Detail Role `Manage files` sudah terbuka tanpa menyebut cara membukanya; spec memakai Tab System lalu klik Role Name. Cara membuka Detail Role `Manage user & role` (langkah 3) juga tidak disebut; spec memakai jalur yang sama.
  - Seed Kevin Susanto: Pre-setup #13 dan #43 menyebut Group Manager hanya di `Data Center`, sedangkan Pre-setup #38 menyebut Kevin Susanto Group Manager di `Data Center` dan `Helpdesk`. Spec memakai #13 dan #43 (baris `Helpdesk` adalah baris non-pola Group Role `Manage files` Read dan Delete); rekonsiliasi dengan #38 belum ada di TC.
  - Gita Maharani (Pre-setup #7) memegang `Manage user & role` Read dan Update di `IT Infrastructure`; TC tidak menyebut apakah akun ini dapat membuka Tab System dan Tab Transaction Role. Spec mengikuti TC (langkah sama dengan aktor Group Manager).
