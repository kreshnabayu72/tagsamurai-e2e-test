---
id: TC-GS-PROFILE-E2E-056-sinkron-identitas-tag-dan-authenticator
title: "Sinkron Data Admin: Rename Position dan Division, Pair dan Unpair TAG, Reset Authenticator"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-217
  - TC-GS-PROFILE-260
  - TC-GS-PROFILE-261
  - TC-GS-PROFILE-262
  - TC-GS-PROFILE-263
coverage:
  web: automated
---

# Sinkron Data Admin: Rename Position dan Division, Pair dan Unpair TAG, Reset Authenticator

## Prerequisites

- Mode: FE+BE.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Pelaku kedua admin (Pre-setup #6) memicu perubahan state lewat sesi API aktor yang tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE. Lihat `suite.md`, Hook suite 4.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Akun aktor pertama spec: Pre-setup #1 (Andi Pratama, Total Control, Employee ID EMP-0001, Position `Finance Manager`, Division `Finance`, TAG `TAG-0001` terpasang, Authenticator Enrolled) `totalControlProfile_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_TC_PASSWORD`. Ganti akun ke Pre-setup #10 (Fajar Nugroho, tanpa TAG) `noPhotoProfile_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_NOPHOTO_PASSWORD`. Pelaku kedua admin: Pre-setup #6 (Hendra Wijaya) `adminActor_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_ADMIN_PASSWORD`, hanya lewat sesi API.
- Env var: `GS_PROFILE_TC_PASSWORD`, `GS_PROFILE_NOPHOTO_PASSWORD`, `GS_PROFILE_ADMIN_PASSWORD`.
- Kemampuan sesi API admin untuk rename Position dan Division di master, pair dan unpair TAG, dan Reset Authenticator, serta fixture BE untuk mendaftarkan kembali Authenticator Pre-setup #1 (enroll), disediakan tim BE/FE; endpoint tidak disebut TC dan ditentukan tim FE di tahap script. TAG `TAG-0010` tersedia dan belum terpasang di user mana pun (disediakan tim FE/BE; lihat Temuan untuk QA).
- Data Pre-setup yang diubah (S-06): nama Position `Finance Manager` (diubah lalu dipulihkan pada langkah 5), nama Division `Finance` (langkah 10), pasangan TAG Pre-setup #1 (langkah 16), enrollment Authenticator Pre-setup #1 (langkah 23), dan pasangan TAG-0010 pada Pre-setup #10 (langkah 32). Efeknya: Last Updated master Position dan Division serta entri audit trail master dan User ikut bertambah; hook `after` spec ini mengulang pemulihan yang sama bila spec gagal di tengah.
- State global yang diubah: data master Position dan Division, TAG, dan Authenticator Pre-setup #1 dan #10. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-PROFILE-260: Position direname admin

1. Pelaku kedua admin (Pre-setup #6) mengubah nama Position Andi Pratama di master Position dari `Finance Manager` menjadi `Senior Finance Manager` lewat sesi API hingga perubahan tersimpan
2. Tunggu aksi selesai
3. Muat ulang My Profile (F5)
4. Verifikasi Position di Section Identity adalah `Senior Finance Manager`
5. Pelaku kedua admin memulihkan nama Position menjadi `Finance Manager` lewat sesi API

### TC-GS-PROFILE-261: Division direname admin

6. Pelaku kedua admin mengubah nama Division Andi Pratama di master Division dari `Finance` menjadi `Corporate Finance` lewat sesi API hingga perubahan tersimpan
7. Tunggu aksi selesai
8. Muat ulang My Profile (F5)
9. Verifikasi Division di Section Identity adalah `Corporate Finance`
10. Pelaku kedua admin memulihkan nama Division menjadi `Finance` lewat sesi API

### TC-GS-PROFILE-263: Admin melakukan unpair TAG

11. Pelaku kedua admin melakukan unpair TAG Andi Pratama (`TAG-0001`) lewat sesi API hingga perubahan tersimpan
12. Tunggu aksi selesai
13. Muat ulang My Profile (F5)
14. Verifikasi User TAG menampilkan `No TAG paired`
15. Verifikasi User TAG tanpa tombol aksi
16. Pelaku kedua admin memasang kembali TAG `TAG-0001` ke Andi Pratama lewat sesi API

### TC-GS-PROFILE-217: Authenticator direset admin

17. Pelaku kedua admin melakukan Reset Authenticator Andi Pratama lewat sesi API hingga perubahan tersimpan
18. Tunggu aksi selesai
19. Muat ulang My Profile (F5)
20. Verifikasi Authenticator menampilkan teks muted `Not enrolled yet`
21. Verifikasi Authenticator tanpa badge
22. Verifikasi Authenticator tanpa teks petunjuk
23. Daftarkan kembali Authenticator Andi Pratama (enrolled) lewat fixture BE

### TC-GS-PROFILE-262: Admin melakukan pair TAG

24. Logout
25. Login sebagai Fajar Nugroho (Pre-setup #10)
26. Buka My Profile dari account menu navbar
27. Pelaku kedua admin memasang TAG `TAG-0010` ke Fajar Nugroho lewat sesi API hingga perubahan tersimpan
28. Tunggu aksi selesai
29. Muat ulang My Profile (F5)
30. Verifikasi User TAG menampilkan badge `Verified`
31. Verifikasi User TAG menampilkan TAG ID `TAG-0010`
32. Pelaku kedua admin melepas TAG `TAG-0010` dari Fajar Nugroho lewat sesi API

## Notes

- Mode: FE+BE. Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan: blok Andi Pratama (akun default suite) berurutan dari yang paling ringan (rename) ke yang paling merusak (Reset Authenticator, TC-GS-PROFILE-217 terakhir pada akun itu), lalu blok Fajar Nugroho dengan Step ganti akun eksplisit (langkah 24 dan 25). Urutan ini berbeda dari urutan nomor TC.
- Pelaku kedua admin memakai sesi API (bukan konteks kedua), sehingga tidak memakai butir `P-2`. TC menulis "Buka My Profile" sedangkan My Profile sudah dibuka hook `beforeEach`; spec memuat ulang halaman supaya nilai terbaru dibaca.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 2, 7, 12, 18, dan 28 (tunggu aksi selesai sebelum membaca di sesi UI), 5, 10, 16, 23, dan 32 (pemulihan state, R-08), 26 (membuka My Profile setelah login Fajar).
- Asersi tambahan di luar Expected TC (S-03): tidak ada.
- Temuan untuk QA:
  - TC-GS-PROFILE-217 memakai Pre-setup #1 (akun default suite) sebagai target Reset Authenticator tanpa menyatakan pemulihan enrollment; spec menambah langkah pemulihan 23 supaya login akun default pada spec berikutnya tidak terganggu.
  - TC-GS-PROFILE-260 dan 261 mengubah nama Position dan Division master Pre-setup yang juga dipakai user lain; TC tidak menyatakan pemulihan. Spec memulihkan nama pada langkah 5 dan 10 (S-06).
  - TC-GS-PROFILE-262 menyebut TAG `TAG-0010` tanpa mendaftarkannya di Tabel Data Uji Pre-setup; spec menulisnya sebagai TAG yang disediakan tim FE/BE.
  - TC-GS-PROFILE-263 menyatakan "tanpa tombol aksi" untuk User TAG; spec mengasersi tidak ada tombol aksi di blok User TAG.
