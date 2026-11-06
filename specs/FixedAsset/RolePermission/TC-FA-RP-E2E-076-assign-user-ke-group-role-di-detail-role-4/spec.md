---
id: TC-FA-RP-E2E-076-assign-user-ke-group-role-di-detail-role-4
title: "Assign User ke Group Role di Detail Role (4/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-253
  - TC-FA-RP-254
  - TC-FA-RP-262
  - TC-FA-RP-1142
coverage:
  web: automated
---

# Assign User ke Group Role di Detail Role (4/4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor (login akun pertama di hook `before`; akun berikutnya lewat langkah ganti akun eksplisit):

| Urutan | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| 1 | Group Manager (`IT Infrastructure`) | Fajar Nugroho (Pre-setup #5) | `groupManager_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |
| 2 | Manage user & role (Group, Update, `IT Infrastructure`) | Gita Maharani (Pre-setup #7) | `murGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GROUP_PASSWORD` |
| 3 | Default User | Admin Utama (Pre-setup #1) | `defaultUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #13 (Kevin Susanto Group Manager di `Data Center`; baris pola GM di `Data Center` dan `Rack A1`; baris non-pola: Group Role `Manage user & role` di `Data Center`, `Manage files` Read dan Delete di `Helpdesk`, Global Role `Manage accounting` hanya Read), #18 (pohon group), #33 (Seed Manage user & role Group: Gita Maharani di `IT Infrastructure`), #43 (Fajar Nugroho Group Manager di `IT Infrastructure`, Kevin Susanto di `Data Center`, Lina Marlina di `Head Office`), #12 (Maya Anggraeni Read Only), #15 (kolam pengguna Standard).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_DU_PASSWORD`, `FA_GM_PASSWORD`, `FA_MUR_GROUP_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-253: Aktor Group Manager: kandidat Group Manager disaring hanya pada node yang ia kelola sebagai GM

1. Klik Tab `System`
2. Buka Detail Role `Manage files`
3. Klik `[+ Assign]` dan pilih group `Data Center` (node GM Kevin Susanto)
4. Ketik Search `Kevin Susanto`, tekan Enter
5. Verifikasi Kevin Susanto tidak ada di daftar picker (empty state hasil Search)
6. Ubah group menjadi `Helpdesk` lalu ganti isi kotak search dengan `Kevin Susanto`, tekan Enter
7. Verifikasi Kevin Susanto ada di daftar picker karena `Helpdesk` bukan node GM-nya

### TC-FA-RP-262: Field Group popup bagi Group Manager: ancestor non-selectable dan node di luar cakupan tidak dirender

8. Tutup popup lewat `✕`
9. Klik `[+ Assign]` dan buka field Group
10. Verifikasi `Head Office` tampil sebagai ancestor non-selectable
11. Verifikasi `IT Infrastructure`, `Data Center`, `Rack A1`, dan `Helpdesk` dapat dipilih
12. Verifikasi `Logistics Warehouse` dan `Dock 1` tidak dirender
13. Tutup popup lewat `✕`

### TC-FA-RP-254: Aktor non Total Control: kandidat Read Only disaring dari popup Assign User ke Role

14. Logout dari akun Group Manager (Fajar Nugroho)
15. Login sebagai Manage user & role (Group, Update) (`murGroup_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_MUR_GROUP_PASSWORD`)
16. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `System`
17. Buka Detail Role `Manage files`
18. Klik `[+ Assign]` dan pilih `Data Center`
19. Ketik Search `Maya Anggraeni`, tekan Enter
20. Verifikasi Maya Anggraeni (Read Only) tidak ada di daftar (empty state hasil Search)
21. Tutup popup lewat `✕`

### TC-FA-RP-1142: Popup Assign User Group Role oleh Default User: target Group Manager tidak tampil pada node GM-nya maupun descendant, dan tampil di luar subtree

22. Logout dari akun Manage user & role (Gita Maharani)
23. Login sebagai Default User (`defaultUser_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_DU_PASSWORD`)
24. Buka Fixed Asset > Settings > Role & Permission lalu klik Tab `System`
25. Buka Detail Role `Manage files`
26. Klik `[+ Assign]` dan pilih group `Data Center`
27. Ketik Search `Kevin Susanto`, tekan Enter
28. Verifikasi Kevin Susanto tidak ada di daftar picker (node penugasan GM-nya sendiri; sudah memegang baris pola GM; eksklusi berlaku juga bagi aktor Default User; empty state hasil Search)
29. Ubah group menjadi `Rack A1` lalu ganti isi kotak search dengan `Kevin Susanto`, tekan Enter
30. Verifikasi Kevin Susanto tidak ada di daftar picker (`Rack A1` adalah descendant dalam subtree penugasan GM-nya dan memegang baris pola GM; empty state hasil Search)
31. Ubah group menjadi `Helpdesk` lalu ganti isi kotak search dengan `Kevin Susanto`, tekan Enter
32. Verifikasi Kevin Susanto ada di daftar picker (`Helpdesk` di luar subtree)
33. Tutup popup lewat `✕`
34. Klik segmen `System` pada breadcrumb
35. Buka Detail Role `Manage user & role`
36. Klik `[+ Assign]` dan pilih group `Rack A1`
37. Ketik Search `Kevin Susanto`, tekan Enter
38. Verifikasi Kevin Susanto ada di daftar picker (`Manage user & role` bukan bagian pola GM dan Kevin Susanto tidak memegang baris itu di `Rack A1`)
39. Tutup popup lewat `✕`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 39 langkah. Di atas 35 langkah karena spec memuat empat TC (253, 254, 262, 1142) dan TC-FA-RP-1142 menambah satu Verifikasi per klausa Expected dengan navigasi antar Detail Role; tidak ada pengulangan yang dapat diringkas. Melewati 35 karena spec memuat empat TC (253, 254, 262, 1142) dan TC-FA-RP-1142 menambah Verifikasi per klausa Expected (tidak ada di Data Center, tidak ada di Rack A1, ada di luar subtree, ada pada Manage user & role) dengan navigasi antar Detail Role; tidak ada pengulangan yang dapat diringkas.
- Langkah penghubung (S-03): langkah 1, 8, 13–16, 21–24, 33–34, 39. Akun aktor pertama sudah login di hook `before` (S-07).
- Penyimpangan urutan (S-05 catatan urutan): TC dikelompokkan per aktor: TC-FA-RP-253 dan 262 (Group Manager), TC-FA-RP-254 (Manage user & role Group), TC-FA-RP-1142 (Default User) agar ganti akun hanya dua kali (langkah 14–16 dan 22–24); login akun pertama di hook `before`.
- Absence di picker memakai empty state hasil Search sebagai anchor positif (butir 8b.2); absence node pada TC-FA-RP-262 memakai node lain yang tampil pada field Group sebagai pembanding.
- Temuan untuk QA:
  - TC-FA-RP-1142 dan TC-FA-RP-254: akun Manage user & role (Group, Update) dan Default User memakai akun Pre-setup #7 dan #1; TC hanya menyebut "Login sbg Role" tanpa rujukan Pre-setup.
  - TC-FA-RP-1142 langkah 6 tidak menyebut cara pindah dari Detail Role `Manage files` ke `Manage user & role`; spec memakai segmen `System` pada breadcrumb.
  - TC-FA-RP-262 Expected a-c tidak punya Search; seluruh node diamati pada field Group yang dibuka.
