---
id: TC-GS-PROFILE-E2E-066-defense-akses-lintas-user
title: "Defense-in-Depth: Akses Lintas User Ditolak 403 untuk Lihat Profil, Change Password, Edit Photo, Delete Photo, dan Access & Status"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-PROFILE-204
  - TC-GS-PROFILE-267
  - TC-GS-PROFILE-268
  - TC-GS-PROFILE-269
  - TC-GS-PROFILE-270
  - TC-GS-PROFILE-271
  - TC-GS-PROFILE-272
  - TC-GS-PROFILE-273
  - TC-GS-PROFILE-274
  - TC-GS-PROFILE-275
  - TC-GS-PROFILE-276
coverage:
  web: automated
---

# Defense-in-Depth: Akses Lintas User Ditolak 403 untuk Lihat Profil, Change Password, Edit Photo, Delete Photo, dan Access & Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor (ganti akun eksplisit): Total Control Pre-setup #1 (Andi Pratama) `totalControlProfile_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.GS_PROFILE_TC_PASSWORD`), login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. User Basic Pre-setup #4 (Budi Santoso) `userBasicProfile_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.GS_PROFILE_BASIC_PASSWORD`, App Access Fixed Asset saja). Target aksi lintas user: Pre-setup #10 (Fajar Nugroho), tidak login. Password baru uji `Spectra.env.PROFILE_PASSWORD_NEW` hanya dipakai pada submit yang ditolak. File uji Pre-setup #17: `valid-photo.png`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): `Spectra.intercept()` yang mengubah parameter user pada request tertentu menjadi ID user lain (ID user Pre-setup #10 dibaca lewat fixture BE); kemampuan membaca status respons server atas request yang diubah itu; kemampuan baca snapshot data Fajar Nugroho (foto profil aktif, status password, dan Last Updated) untuk memeriksa tidak ada mutasi; klien HTTP yang mengirim request langsung ke server memakai token sesi akun Pre-setup #4 (TC-204); fixture BE yang memasang foto profil aktif untuk akun #1 dan #4 di hook `before` spec ini (agar tombol [Delete] tersedia) dan memulihkannya ke keadaan tanpa foto di hook `after` spec ini.
- Tabel 1, aksi yang diuji (satu baris satu TC; langkah 2 sampai 8 dijalankan untuk baris selain Change Password, langkah 9 sampai 18 untuk baris Change Password):

| TC | Aktor | Request yang diubah | Aksi UI |
|---|---|---|---|
| TC-GS-PROFILE-267 | Pre-setup #1 | pemuatan My Profile | muat ulang halaman My Profile |
| TC-GS-PROFILE-271 | Pre-setup #1 | Edit Photo | hover Avatar, klik [Edit], pilih file `valid-photo.png` |
| TC-GS-PROFILE-273 | Pre-setup #1 | Delete Photo | hover Avatar, klik [Delete], klik [Remove] |
| TC-GS-PROFILE-275 | Pre-setup #1 | Access & Status | muat ulang halaman My Profile |
| TC-GS-PROFILE-269 | Pre-setup #1 | Change Password | klik [Change Password], isi Current Password `Spectra.env.GS_PROFILE_TC_PASSWORD`, New Password dan Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`, klik [Save] |
| TC-GS-PROFILE-268 | Pre-setup #4 | pemuatan My Profile | muat ulang halaman My Profile |
| TC-GS-PROFILE-272 | Pre-setup #4 | Edit Photo | hover Avatar, klik [Edit], pilih file `valid-photo.png` |
| TC-GS-PROFILE-274 | Pre-setup #4 | Delete Photo | hover Avatar, klik [Delete], klik [Remove] |
| TC-GS-PROFILE-276 | Pre-setup #4 | Access & Status | muat ulang halaman My Profile |
| TC-GS-PROFILE-270 | Pre-setup #4 | Change Password | klik [Change Password], isi Current Password `Spectra.env.GS_PROFILE_BASIC_PASSWORD`, New Password dan Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`, klik [Save] |

- State global yang diubah: foto profil aktif akun #1 dan #4 (dipasang dan dipulihkan spec). Tidak ada mutasi pada data Pre-setup #10 yang diharapkan; hal itu yang diasersi. Suite berjalan serial (`parallel: false`).
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.

## Test Steps

### Aktor Total Control Pre-setup #1 (TC-GS-PROFILE-267, 271, 273, 275, 269)

1. Catat snapshot data Fajar Nugroho sebagai baseline (kemampuan baca)

Untuk setiap baris Tabel 1 dengan Aktor Pre-setup #1 selain Change Password (langkah 2 sampai 8):

2. Pasang intercept yang mengubah parameter user pada request kolom "Request yang diubah" menjadi ID user Pre-setup #10
3. Lakukan aksi UI pada kolom "Aksi UI"
4. Verifikasi respons server atas request itu berstatus 403
5. Verifikasi toast error `You don't have permission to do this.` tampil
6. Verifikasi tidak ada pengalihan: halaman tetap My Profile
7. Verifikasi data Fajar Nugroho sama dengan snapshot baseline (tidak ada mutasi)
8. Lepas intercept, lalu muat ulang halaman My Profile

Baris Change Password Pre-setup #1 (TC-GS-PROFILE-269, langkah 9 sampai 18):

9. Pasang intercept yang mengubah parameter user pada request Change Password menjadi ID user Pre-setup #10
10. Lakukan aksi UI pada baris Change Password Pre-setup #1 Tabel 1
11. Verifikasi respons server atas request itu berstatus 403
12. Verifikasi toast error `You don't have permission to do this.` tampil
13. Verifikasi tidak ada pengalihan: halaman tetap My Profile
14. Verifikasi data Fajar Nugroho sama dengan snapshot baseline (tidak ada mutasi)
15. Klik ✕ pada modal Change Password
16. Verifikasi dialog `Unsaved Changes` tampil
17. Klik [Leave]
18. Lepas intercept

### Aktor User Basic Pre-setup #4 (TC-GS-PROFILE-268, 272, 274, 276, 270, 204)

19. Ganti akun: klik Logout, lalu login sebagai Pre-setup #4 dengan `Spectra.env.GS_PROFILE_BASIC_PASSWORD`, lalu buka My Profile lewat account menu navbar > My Profile
20. Untuk setiap baris Tabel 1 dengan Aktor Pre-setup #4 selain Change Password, jalankan langkah 2 sampai 8
21. Untuk baris Change Password Pre-setup #4 Tabel 1, jalankan langkah 9 sampai 18
22. Kirim request Access & Status langsung ke server untuk produk Admin Console memakai token sesi akun Pre-setup #4 (App Access Admin Console tidak dimiliki)
23. Verifikasi respons server berstatus 403 akses ditolak
24. Verifikasi respons tidak mengembalikan data produk

## Notes

- Alasan di atas sekitar 35 langkah (dihitung dengan ekspansi, bagian 3 prinsip 13 Alasan wajib): seluruh isi spec satu kelas harness (a, defense-in-depth) dengan pola identik aksi x aktor; langkah 2 sampai 8 diulang untuk 8 baris Tabel 1 dan langkah 9 sampai 18 untuk 2 baris, parameter tiap iterasi ada di Tabel 1. Kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna, dan memecah per aktor atau aksi hanya menambah login, hook, dan cleanup (kelas ringan satu spec per kelas per modul).
- K-1: TC-GS-PROFILE-204 dan TC-GS-PROFILE-267 sampai 276 adalah TC defense-in-depth dengan Expected respons API (status respons dan state data lewat kemampuan baca) yang tumpang tindih dengan kontrak BE; tetap di spec FE+BE karena TC granular tetap sumber dan tiap TC tepat satu spec. TC-GS-PROFILE-204 adalah request langsung ke server, sehingga hanya status respons dan isi respons yang diasersi (bagian 8b butir 1).
- Langkah penghubung (S-03): langkah 1 mencatat snapshot (baseline); langkah 8 dan 18 melepas intercept dan memulihkan halaman (S-09); langkah 15 sampai 17 menutup form Change Password yang dirty (S-08); langkah 19 mengganti akun.
- Urutan: baris Change Password terakhir pada tiap aktor karena modal Change Password yang terbuka perlu ditutup lewat langkah 15 sampai 17 sebelum halaman dipakai lagi; request langsung TC-GS-PROFILE-204 memakai sesi #4 sehingga berada di blok #4.
- Temuan untuk QA:
  - TC-GS-PROFILE-267 sampai 276 tidak menyebut aksi UI pemicu untuk "lihat profil" dan "fetch Access & Status"; spec memakai muat ulang halaman My Profile untuk keduanya, dengan intercept yang berbeda per request.
  - Pre-setup #1 tertulis tanpa foto sehingga tombol [Delete] pada TC-GS-PROFILE-273 tidak tersedia; spec memasang foto aktif akun #1 dan #4 lewat fixture BE di hook `before` spec (TC-GS-PROFILE-274 untuk #4 sama) dan memulihkannya di hook `after`.
  - TC-GS-PROFILE-267 sampai 276 tidak menyebut keadaan modal Change Password setelah 403; spec menutup modal lewat `✕` dan dialog `Unsaved Changes` (langkah 15 sampai 17) dengan asumsi modal tetap terbuka dengan isian terisi.
  - TC-GS-PROFILE-267 sampai 276 menyebut "tidak ada mutasi pada data Fajar Nugroho" tanpa cara cek; spec memakai kemampuan baca snapshot yang disediakan tim FE/BE.
  - TC-GS-PROFILE-204 tidak menyebut cara mengirim request langsung (klien HTTP dan token sesi); spec meminta kemampuan itu dari tim FE/BE.
