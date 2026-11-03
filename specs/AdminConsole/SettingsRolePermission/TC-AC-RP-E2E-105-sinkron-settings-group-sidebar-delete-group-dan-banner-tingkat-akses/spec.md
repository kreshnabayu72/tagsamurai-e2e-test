---
id: TC-AC-RP-E2E-105-sinkron-settings-group-sidebar-delete-group-dan-banner-tingkat-akses
title: "Sinkronisasi Settings > Group dan Settings > User: Rename dan Delete Group, Banner Tingkat Akses di Detail User, dan Group Baru"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-349
  - TC-AC-RP-350
  - TC-AC-RP-351
  - TC-AC-RP-352
coverage:
  web: automated
---

# Sinkronisasi Settings > Group dan Settings > User: Rename dan Delete Group, Banner Tingkat Akses di Detail User, dan Group Baru

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API).
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua (ganti akun eksplisit pada langkah 29): Read Only `readOnlyRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Dewi Anggraini`, Pre-setup #3), password dari `Spectra.env.AC_RP_RO_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal: `Default Group`, `Region A` dengan anak `Branch 1`, `Region Jawa` dengan anak `Jakarta` dan `Surabaya`, `Sumatera`), #12 (user Standard `Alex Tan`), #13, #14 (penugasan GM `Fajar Nugroho` di `Region Jawa` dan `Sumatera`), #15, #17 (approver dan toggle `Sumatera` OFF tersimpan), dan #26 (akses Settings > Group dan Settings > User).
- Data Dinamis (Tabel Data Uji Dinamis #2, TC-AC-RP-350): group `Gudang Baru+{runId}-105` dibuat di hook `before` lewat seeding API sesudah seluruh Total Control dan Read Only ditetapkan, tanpa penugasan Group Role; Distributor `Distributor Gudang+{runId}-105` ditempatkan di group itu lewat seeding API supaya ada data yang dibaca aktor Read Only. Keduanya dibersihkan di hook `after`. Kemampuan seeding disediakan tim BE/FE.
- Target aksi rename dan Delete group (TC-AC-RP-351, TC-AC-RP-352) adalah group Pre-setup `Sumatera` karena TC mengikat Expected ke baris dan penugasan Pre-setup yang tidak dapat dimiliki spec (S-06); pemulihannya ke keadaan Tabel Data Uji Pre-setup TC memakai kemampuan reset FE/BE (langkah 5 dan 15).
- Pemulihan baseline: data Pre-setup dan Data Dinamis yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC; kemampuan reset dinyatakan di `suite.md` (Pemulihan baseline automation); dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung "Pulihkan baseline" antar blok TC. Efek yang tidak dipulihkan: Modified By, Last Updated, dan audit trail (Changelog, System Log, Activity Log) bertambah.
- Kemampuan teknis: pembacaan state BE approver dan nilai toggle group yang sudah dihapus (disediakan tim FE/BE, langkah 13 dan 14); tidak ada endpoint yang dikarang.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Env var yang dipakai spec ini (`AC_RP_TC_PASSWORD`, `AC_RP_RO_PASSWORD`) baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.

## Test Steps

### TC-AC-RP-351: Sidebar Group Tree mencerminkan perubahan Settings > Group

1. Rename group `Sumatera` menjadi `Sumatera Utara` di Settings > Group
2. Buka halaman `Settings > Role & Permission`, lalu klik tab `Group Manager`
3. Verifikasi sidebar menampilkan `Sumatera Utara`
4. Verifikasi kolom Group menampilkan `Sumatera Utara`
5. Pulihkan baseline: group `Sumatera Utara` di-rename kembali menjadi `Sumatera`

### TC-AC-RP-352: Delete Group melepas GM, menghapus approver dan toggle group itu

6. Hapus group `Sumatera` di Settings > Group
7. Buka halaman `Settings > Role & Permission`, lalu klik tab `Group Manager`
8. Verifikasi baris `Fajar Nugroho` — `Region Jawa` tampil
9. Verifikasi baris `Fajar Nugroho` — `Sumatera` hilang
10. Verifikasi node `Sumatera` tidak lagi ada di sidebar
11. Klik tab `System`
12. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
13. Verifikasi approver `Sumatera` tidak lagi tersimpan (dibaca lewat kemampuan baca state BE)
14. Verifikasi nilai toggle `Sumatera` tidak lagi tersimpan (dibaca lewat kemampuan baca state BE)
15. Pulihkan baseline: group `Sumatera` beserta penugasan GM `Fajar Nugroho`, approver, dan toggle OFF-nya dikembalikan

### TC-AC-RP-349: Assign dan Remove tingkat akses tercermin sebagai banner di Detail User

16. Buka halaman `Settings > Role & Permission` (Tab Total Control aktif)
17. Klik `+ Assign`, centang `Alex Tan`, lalu klik `[Assign]`
18. Buka `Settings > User > Detail User` `Alex Tan` > Tab Role
19. Verifikasi banner tingkat akses Total Control tampil
20. Verifikasi Settings > User tidak menyediakan aksi assign atau remove tingkat akses
21. Buka halaman `Settings > Role & Permission`, klik `⋯` baris `Alex Tan` pada Tab Total Control, klik `Remove`, lalu klik `[Remove]`
22. Buka kembali `Settings > User > Detail User` `Alex Tan` > Tab Role
23. Verifikasi banner tingkat akses hilang
24. Verifikasi seluruh peran individual kosong

### TC-AC-RP-350: Grup baru otomatis tercakup TC dan RO tanpa baris Group Role

25. Buka halaman `Settings > Role & Permission` lalu klik tab `System`
26. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`
27. Klik node `Gudang Baru+{runId}-105`
28. Verifikasi Detail Role pada node `Gudang Baru+{runId}-105` menampilkan empty state (tidak ada baris dibuat otomatis)
29. Ganti akun: logout, lalu login sebagai Read Only `Dewi Anggraini` (`Spectra.env.AC_RP_RO_PASSWORD`)
30. Buka menu Distributor lalu buka data `Distributor Gudang+{runId}-105` di group `Gudang Baru+{runId}-105`
31. Verifikasi `Dewi Anggraini` dapat membaca data Distributor di group baru lewat otorisasi entity-wide

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan (S-10): TC-AC-RP-351 dan TC-AC-RP-352 (state group Pre-setup) di awal, TC-AC-RP-349 sesudahnya, dan TC-AC-RP-350 di akhir karena membutuhkan ganti akun ke Read Only sehingga ganti akun hanya sekali (S-07, S-10).
- Langkah penghubung (S-03, S-09): langkah 5 dan 15 (pemulihan baseline tanpa `Verifikasi`); halaman `Settings > Role & Permission` dibuka ulang sesudah perubahan di Settings > Group atau Settings > User.
- Pembanding absence (bagian 8b butir 2): baris `Fajar Nugroho` — `Region Jawa` tampil sebelum asersi baris `Fajar Nugroho` — `Sumatera` hilang pada tabel yang sama.
- Temuan untuk QA:
  - TC-AC-RP-350 Expected b "Read Only tetap dapat membaca data group baru" tidak menyebut data apa yang dibaca; group baru tanpa entitas tidak memberi hasil bermakna. Spec menempatkan satu Distributor milik spec di group baru lewat seeding supaya ada yang dibaca (penambahan atas TC, dicatat di sini; S-03 dan S-15). Langkah "buka data Distributor di group" tidak menyebut menu atau filter yang dipakai; spec memakai menu Distributor.
  - TC-AC-RP-352 Expected "approver dan nilai toggle `Sumatera` tidak lagi tersimpan" tidak memberi cara pengamatan di UI (node `Sumatera` sudah tidak ada); spec memakai kemampuan baca state BE yang disediakan tim FE/BE (S-11, S-13).
  - TC-AC-RP-349 Expected b "seluruh peran individual kosong" tidak menyebut surface selain Tab Role; spec mengasersi di Tab Role Detail User.
  - Post Condition semua TC tanpa langkah observasi tidak diasersi (S-01).
  - Mekanisme "dipulihkan automation baseline" (Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
