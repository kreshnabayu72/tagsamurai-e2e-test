---
name: Global Settings My Profile
id: suite-global-settings-my-profile
description: Spec e2e turunan tc-my-profile.md untuk Global Settings > My Profile
executionOrder: 1.0
parallel: false
---

# Suite: Global Settings My Profile

Suite ini mencakup halaman My Profile pada Global Settings: screening halaman (Header, Section Identity, Access & Status, Custom Field), Guided Tooltip, Change Password (Password Policy, lock bertingkat, reset counter), Edit Photo dan Delete Photo, Product Selector, Pending Email Change, Role Matrix, pencatatan log (Changelog, System Log, Activity Log, User Log), sinkronisasi lintas modul, Storage dan kuota, multi-sesi dan multi-tab, defense-in-depth, state tenant (plan dan status Client), serta ketahanan terhadap kegagalan server.

`parallel: false` karena spec mengubah state global (jam server, counter Change Password dan Login, password aktor Pre-setup, foto profil, kuota dan ledger Storage, status Client) dan memakai perangkat Android uji bersama.

Setiap spec tetap menyiapkan dan membersihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

## Hook suite

1. Login akun aktor default suite: hook `before` login akun aktor default suite (Pre-setup #1, Andi Pratama, Total Control, `Spectra.env.GS_PROFILE_TC_PASSWORD`). Spec yang memakai akun aktor pertama lain menulis akunnya di `## Prerequisites` dan login di hook `before` spec itu; hook `after` spec mengembalikan sesi ke akun default suite.
2. Halaman awal: hook `beforeEach` membuka My Profile (account menu navbar > My Profile) dan menunggu halaman termuat; spec yang tidak menguji navigasi tidak mengulang langkah buka.
3. Flag Guided Tooltip: hook `before` menyetel flag `guided_tooltip_seen_gs-my-profile` menjadi true untuk setiap akun aktor yang dipakai spec dalam suite (nilai awal tiap akun dicatat), dan hook `after` memulihkan nilai awal. Nama key itu ditulis TC (Pre-setup #1 dan #20); mekanisme penyetelannya disediakan tim FE/BE. Spec yang memakai Pre-setup #20 (flag belum ada) atau menguji flag itu sendiri (005, 006, 007, dan blok Guided Tooltip pada 009) dikecualikan: spec itu mengatur flag sesudah hook dan menulisnya di `## Prerequisites`.
4. Sesi API aktor: login API (password) untuk akun yang sama dengan sesi UI memakai token yang tidak dihitung sebagai sesi web, sehingga sesi UI tidak diusir. Pelaku kedua admin (Pre-setup #6, Hendra Wijaya, `Spectra.env.GS_PROFILE_ADMIN_PASSWORD`) memicu perubahan state lewat sesi API ini. Kemampuan itu disediakan tim BE/FE.
5. Jaring pengaman `Unsaved Changes`: hook `beforeEach` mengonfirmasi dialog `beforeunload` dan menutup dialog `Unsaved Changes` bila tampil dari spec sebelumnya. Itu bukan pengganti langkah pemulihan form di spec.
6. Reset counter: hook `beforeEach` mengatur counter Change Password dan counter Login akun Pre-setup #7 dan #18 ke 0 sebelum tiap spec. Spec yang menguji counter mengaturnya sesudah hook dan menulisnya di `## Prerequisites`. Mekanisme reset disediakan tim FE/BE.
7. Pemulihan state global: hook `after` memulihkan jam server dan jam browser ke waktu nyata, password akun Pre-setup #7, #18, dan #24 ke `Passw0rd!Old`, counter ke 0, foto profil akun Pre-setup #9 dan #10 ke keadaan awal, kuota dan ledger Storage Pre-setup #11 sampai #13, serta status Client Pre-setup #24 dan #25 ke Active. Fixture pemulihan disediakan tim FE/BE.

## Env var password aktor

Password akun aktor memakai pola `GS_PROFILE_<ROLE>_PASSWORD`; satu nama satu akun Pre-setup:
`GS_PROFILE_TC_PASSWORD` (#1), `GS_PROFILE_RO_PASSWORD` (#2), `GS_PROFILE_SYSROLE_PASSWORD` (#3), `GS_PROFILE_BASIC_PASSWORD` (#4), `GS_PROFILE_MULTI_PASSWORD` (#5), `GS_PROFILE_ADMIN_PASSWORD` (#6), `GS_PROFILE_PWD_PASSWORD` (#7, nilai `Passw0rd!Old`), `GS_PROFILE_PENDING_PASSWORD` (#8), `GS_PROFILE_PHOTO_PASSWORD` (#9), `GS_PROFILE_NOPHOTO_PASSWORD` (#10), `GS_PROFILE_STORAGEFULL_PASSWORD` (#11), `GS_PROFILE_STORAGENEAR_PASSWORD` (#12), `GS_PROFILE_NOQUOTA_PASSWORD` (#13), `GS_PROFILE_STARTER_PASSWORD` (#14), `GS_PROFILE_ENTERPRISE_PASSWORD` (#15), `GS_PROFILE_PWD12H_PASSWORD` (#18), `GS_PROFILE_NOTENROLLED_PASSWORD` (#19), `GS_PROFILE_FRESHGUIDE_PASSWORD` (#20), `GS_PROFILE_TEMP_PASSWORD` (#21), `GS_PROFILE_SAMSSIEM_PASSWORD` (#22), `GS_PROFILE_UNPROV_PASSWORD` (#23), `GS_PROFILE_SUSPENDED_PASSWORD` (#24), `GS_PROFILE_EXPIRED_PASSWORD` (#25).
Password baru hasil Change Password (`N3wPassw0rd!`, Data Dinamis #3) memakai `Spectra.env.PROFILE_PASSWORD_NEW`. Setiap nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

`## Prerequisites` tiap spec merujuk pernyataan 1 sampai 7 dengan satu baris dan tidak menulis ulang isinya.
