---
id: TC-FA-RP-E2E-129-penugasan-otomatis-pembuat-group
title: Penugasan otomatis pembuat Group
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-442
  - TC-FA-RP-443
  - TC-FA-RP-444
  - TC-FA-RP-445
  - TC-FA-RP-446
coverage:
  web: automated
---

# Penugasan otomatis pembuat Group

## Prerequisites

- Mode: FE+BE
- Akun (identitas Pre-setup dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE):

| Urutan | Akun | Pre-setup | Email | Env password |
|---|---|---|---|---|
| 1 (hook `before`) | Group Manager, Fajar Nugroho | #5 | `groupManager_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |
| 2 | Manage user & role (Group, Update), Gita Maharani | #7 | `murGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GROUP_PASSWORD` |
| 3 | Default User, Admin Utama | #1 | `defaultUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` |
| 4 | Total Control, Siti Rahmawati | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login akun urutan 1 di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup: #18 (pohon Group Company Alpha, dipakai `IT Infrastructure` sebagai induk Subgroup), #43 (Fajar Nugroho Group Manager di `IT Infrastructure`). Gita Maharani memegang `Manage group` Create di `IT Infrastructure` (precondition TC 443; baris ini tidak tertulis di Pre-setup TC, disediakan tim FE lewat seeding API di hook `before`).
- Data Dinamis (nilai bersuffix `{runId}` dan nomor spec 129): Subgroup `Server Room {runId}-129`, `Floor Lab {runId}-129`, `TC Created {runId}-129`, `DU Created {runId}-129`. Hook `after` menghapus keempat Subgroup lewat API (kemampuan disediakan tim FE/BE).
- Kemampuan teknis: seeding API Pre-setup; penghapusan Group dinamis lewat API.

## Test Steps

### Pembuatan Subgroup oleh tiga aktor

1. Buka Fixed Asset > Settings > Groups.
2. Buat Subgroup `Server Room {runId}-129` di bawah `IT Infrastructure` lewat row action `Add Subgroup`.
3. Tunggu aksi selesai (Subgroup `Server Room {runId}-129` muncul di pohon Group).
4. Ganti akun: logout, lalu login sebagai Manage user & role (Group, Update) Gita Maharani.
5. Buka Fixed Asset > Settings > Groups dan buat Subgroup `Floor Lab {runId}-129` di bawah `IT Infrastructure`.
6. Tunggu aksi selesai (Subgroup `Floor Lab {runId}-129` muncul di pohon Group).
7. Ganti akun: logout, lalu login sebagai Default User Admin Utama.
8. Buka Fixed Asset > Settings > Groups dan buat Subgroup `DU Created {runId}-129` di bawah `IT Infrastructure`.
9. Buka Fixed Asset > Settings > Role & Permission > System, buka Detail Role `Manage group`, lalu klik node `IT Infrastructure`.
10. Verifikasi sedikitnya satu baris tampil pada `Manage group` di node `IT Infrastructure`.
11. Klik node `DU Created {runId}-129`.
12. Verifikasi tidak ada baris penugasan khusus pembuat pada `Manage group` di node `DU Created {runId}-129`: Admin Utama hanya tampil sebagai baris pola Default User (CRUD penuh sesuai kolom berlaku, sama seperti Default User di node lain).

### Verifikasi penugasan otomatis dan pembuat Total Control

13. Ganti akun: logout, lalu login sebagai Total Control Siti Rahmawati.
14. Buka Fixed Asset > Settings > Role & Permission > System, buka Detail Role `Manage group`, lalu klik node `Server Room {runId}-129`.
15. Verifikasi baris Fajar Nugroho muncul pada `Manage group` di node `Server Room {runId}-129` dengan Create, Read, Update, Delete tercentang.
16. Verifikasi Modified By baris Fajar Nugroho berformat `Fajar N`.
17. Klik node `Floor Lab {runId}-129`.
18. Verifikasi baris Gita Maharani muncul pada `Manage group` di node `Floor Lab {runId}-129` dengan Create, Read, Update, Delete tercentang.
19. Buka Fixed Asset > Settings > Groups dan buat Subgroup `TC Created {runId}-129` di bawah `IT Infrastructure`.
20. Buka Fixed Asset > Settings > Role & Permission > System, buka Detail Role `Manage group`, lalu klik node `IT Infrastructure`.
21. Verifikasi sedikitnya satu baris tampil pada `Manage group` di node `IT Infrastructure`.
22. Klik node `TC Created {runId}-129`.
23. Verifikasi tidak ada baris Siti Rahmawati pada `Manage group` di node `TC Created {runId}-129`.

### Penugasan pembuat berperilaku sebagai baris reguler

24. Klik node `Server Room {runId}-129`.
25. Hapus centang Delete pada baris Fajar Nugroho.
26. Verifikasi toast `Success, permissions have been updated.`
27. Klik `[⋯]` pada baris Fajar Nugroho, pilih `Remove`, lalu klik `[Remove]`.
28. Verifikasi toast `Success, user has been removed.`
29. Verifikasi tidak ada dialog blokir khusus pembuat yang tampil.

## Notes

- Langkah penghubung (S-03): langkah 1, 3, 5, 6, 8, 9, 11, 14, 17, 19, 20, 22, 24 (navigasi atau menunggu aksi selesai tanpa Verifikasi); langkah 21 adalah pembanding absence (8b butir 2) untuk langkah 23; langkah 10 membuktikan tabel `Manage group` termuat sebelum langkah 12 (langkah 12 bukan absence karena Admin Utama tampil sebagai baris pola Default User).
- Urutan TC berubah: TC 442 dan 443 diverifikasi sesudah TC 445 supaya tiga aktor pembuat (Group Manager, pemegang Manage group, Default User) berganti akun satu kali tiap aktor; TC 442 dan 443 butuh Total Control untuk membaca Detail Role, TC 445 diperiksa langsung oleh Default User (Admin Utama) yang membuatnya. TC 446 sesudah TC 442 karena memakai baris Fajar Nugroho hasil TC 442.
- TC 444 hanya punya Expected absence atas baris Detail Role dan TC 445 Expected atas baris Detail Role (bukan absence log), sehingga tetap di spec fungsional ini.
- Temuan untuk QA:
  - Post Condition TC 442 ("log `Assign` tercatat, lihat Section 5") tidak punya langkah observasi di TC dan tidak diasersi.
  - TC 443 precondition c (Gita Maharani memegang `Manage group` Create di `IT Infrastructure`) tidak ada di Pre-setup #1 sampai #44; baris itu ditulis disediakan tim FE.
  - TC 446 mengedit CRUD baris pembuat yang berstatus Group Manager (di `IT Infrastructure`, node induk `Server Room`); TC 460 menunjukkan bahwa unchecklist pada baris Group Manager bisa memunculkan dialog D-05 (auto-revert), sedangkan TC 446 mengharapkan toast sukses langsung. Perlu konfirmasi QA apakah baris di node turunan berbeda perilakunya.
  - TC 445 Expected a membedakan baris pola Default User dari "penugasan khusus pembuat" tanpa indikator di UI untuk membedakannya; langkah 12 mengasersi tampilan baris Admin Utama sesuai teks TC. Bagian Role Transaksi dan penyalinan baris dari `IT Infrastructure` (Expected a akhir dan b) tidak punya langkah di spec ini.
  - TC 443 Expected b menyebut Approver Pandu Wijaya pada sub-tab `Disposal` di `Floor Lab {n}` (Pre-setup #19: Pandu hanya pada sub-tab `Disposal`). Spec tidak mengasersi bagian itu karena tidak punya langkah penyalinan Role Transaksi.
  - Data Dinamis TC menamai Subgroup `Server Room {n}` dengan `{n}` = nomor TC; spec memakai suffix `{runId}-129` agar unik per run (S-12).
