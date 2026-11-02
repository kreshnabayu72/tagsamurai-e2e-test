---
id: TC-GS-PROFILE-E2E-069-state-tenant-client-suspended-dan-expired
title: "State Tenant: Client Suspended dan Expired Menolak Aksi Tulis, My Profile Tetap Dapat Dibaca"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-PROFILE-322
  - TC-GS-PROFILE-323
  - TC-GS-PROFILE-324
  - TC-GS-PROFILE-325
coverage:
  web: automated
---

# State Tenant: Client Suspended dan Expired Menolak Aksi Tulis, My Profile Tetap Dapat Dibaca

## Prerequisites

- Mode: FE+BE.
- Akun aktor (ganti akun eksplisit): Total Control Pre-setup #24 (Rudi Hartono, Client Suspended) `totalControlSuspended_automated_{namaCompany}@qwertysystem.net` (password aktif `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`; foto profil aktif `rudi-photo.jpg`; counter Change Password 0), login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Total Control Pre-setup #25 (Sari Dewanti, Client Expired) `totalControlExpired_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.GS_PROFILE_EXPIRED_PASSWORD`; foto profil aktif `sari-photo.jpg`). Password baru uji `Spectra.env.PROFILE_PASSWORD_NEW` (Data Dinamis #3) hanya dipakai pada submit yang ditolak. File uji Pre-setup #17: `valid-photo.png`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE yang menetapkan status Client #24 ke Suspended dan #25 ke Expired (status Client ditetapkan sebelum spec dan dipulihkan ke Active di hook `after` suite); login lewat sesi API aktor akun #24 dengan password lama (TC-322 butir e); kemampuan baca jumlah baris User Log akun #24 dengan Activity `Change Password` dan jumlah baris log `Field = Photo` di Changelog, System Log, dan Activity Log aktor akun #24 dan #25, serta jumlah entri Recycle Bin File Manager milik akun #24 dan #25, semuanya untuk baseline (S-12).
- State global: status Client #24 dan #25 (Suspended dan Expired selama spec; dipulihkan ke Active oleh hook `after` suite). Tidak ada perubahan data oleh spec ini karena semua aksi tulis ditolak. Suite berjalan serial (`parallel: false`).
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`, `Spectra.env.GS_PROFILE_PWD12H_PASSWORD`, `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`), counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.

## Test Steps

### TC-GS-PROFILE-325: Client Suspended, My Profile tetap dapat dibuka dan dibaca

1. Muat ulang halaman My Profile
2. Verifikasi halaman tampil dengan Avatar foto `rudi-photo.jpg`, Section Identity, Section Access & Status, dan Section Custom Field
3. Verifikasi tidak muncul state error load `S-02`
4. Verifikasi tidak muncul toast error

### TC-GS-PROFILE-323: Client Suspended, Edit Photo ditolak dan foto tidak berubah

5. Catat baseline akun #24: jumlah baris log `Field = Photo` G0 dan jumlah entri Recycle Bin R0 (kemampuan baca)
6. Hover Avatar, klik [Edit], pilih file `valid-photo.png`
7. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` tampil
8. Verifikasi Avatar tetap menampilkan foto aktif `rudi-photo.jpg`
9. Verifikasi jumlah entri Recycle Bin tetap R0 (tidak ada file baru tersimpan dan foto lama tidak di-soft-delete)
10. Verifikasi jumlah baris log `Field = Photo` tetap G0

### TC-GS-PROFILE-322: Client Suspended, Change Password ditolak dan password tidak berubah

11. Catat baseline akun #24: jumlah baris User Log Activity `Change Password` U0 (kemampuan baca)
12. Klik [Change Password]
13. Isi Current Password `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`, New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
14. Klik [Save]
15. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` tampil
16. Verifikasi tidak ada pengalihan: halaman My Profile tetap tampil
17. Verifikasi modal Change Password tetap terbuka dengan Current Password, New Password, dan Confirm New Password tetap terisi
18. Verifikasi [Save] kembali Enabled
19. Login lewat sesi API aktor akun #24 dengan password `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`
20. Verifikasi login dengan password lama berhasil (password tidak berubah)
21. Verifikasi jumlah baris User Log Activity `Change Password` tetap U0
22. Klik ✕ pada modal Change Password
23. Verifikasi dialog `Unsaved Changes` tampil
24. Klik [Leave]

### TC-GS-PROFILE-324: Client Expired, Delete Photo ditolak dan foto tidak berubah

25. Ganti akun: klik Logout, lalu login sebagai Pre-setup #25 dengan `Spectra.env.GS_PROFILE_EXPIRED_PASSWORD`, lalu buka My Profile lewat account menu navbar > My Profile
26. Catat baseline akun #25: jumlah baris log `Field = Photo` G1 dan jumlah entri Recycle Bin R1 (kemampuan baca)
27. Hover Avatar, klik [Delete]
28. Pada dialog Remove Photo klik [Remove]
29. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` tampil
30. Verifikasi Avatar tetap menampilkan foto aktif `sari-photo.jpg`
31. Verifikasi jumlah entri Recycle Bin tetap R1 (foto lama tidak di-soft-delete)
32. Verifikasi jumlah baris log `Field = Photo` tetap G1

## Notes

- Seluruh spec kelas h (write-lockdown Client Suspended dan Expired) dengan dua blok akun yang berdiri sendiri; ganti akun memakai Step eksplisit (langkah 25) dan blok #25 tetap bermakna walau blok #24 gagal. Plan tier Starter dan Enterprise ada di spec 068 karena bukan write-lockdown.
- Urutan: TC-GS-PROFILE-325 (baca) dahulu, lalu TC-GS-PROFILE-323 dan TC-GS-PROFILE-322 (aksi tulis yang ditolak), lalu blok akun #25.
- P-1: asersi "tidak ada baris log" (langkah 10, 21, 32 untuk TC-GS-PROFILE-322, 323, 324) tetap di spec ini karena konteksnya bergantung pada state berat Client Suspended atau Expired; tiap asersi memakai baseline sendiri (S-12) dan toast error langkah 7, 15, dan 29 sebagai anchor positif. TC-GS-PROFILE-322 sampai 324 tidak ada di `sourceTc` spec absence.
- Langkah penghubung (S-03): langkah 1 memuat ulang halaman sebagai pemicu baca; langkah 5, 11 dan 26 mencatat baseline; langkah 22 sampai 24 menutup form Change Password yang dirty (S-08); langkah 25 mengganti akun.
- Temuan untuk QA:
  - TC-GS-PROFILE-322 butir f menyebut "entri User Log Activity `Change Password`" tanpa menyebut surface pembaca; spec memakai kemampuan baca User Log akun #24 yang disediakan tim FE/BE (admin Client Suspended dapat dibaca lewat fixture).
  - TC-GS-PROFILE-322 sampai 324 menyebut akun hanya pada Pre-setup #24 dan #25; password akun #25 tidak masuk daftar pemulihan hook `after` suite karena tidak berubah (aksi ditolak).
  - TC-GS-PROFILE-325 menyebut `S-02` sebagai "state error load" tanpa teks; spec mengasersi state itu tidak tampil tanpa teks, karena teks error load (`Unable to load this data.`) berasal dari PRD, bukan butir Expected TC-325.
