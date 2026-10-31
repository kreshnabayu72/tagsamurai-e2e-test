---
id: TC-GS-PROFILE-E2E-047-banner-pending-email-change-tanpa-permintaan-dan-admin
title: "Pending Email Change: Tanpa Permintaan Live dan Admin Mengubah Email"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-25
  - TC-GS-PROFILE-208
  - TC-GS-PROFILE-246
coverage:
  web: automated
---

# Pending Email Change: Tanpa Permintaan Live dan Admin Mengubah Email

## Prerequisites

- Mode: FE+BE.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Pelaku kedua admin (Pre-setup #6) memicu perubahan state lewat sesi API aktor yang tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE. Lihat `suite.md`, Hook suite 4.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Akun aktor pertama spec: Pre-setup #1 (Andi Pratama, Email `andipratama@qwertysystem.net`, Total Control) `totalControlProfile_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_TC_PASSWORD`. Ganti akun di tengah spec ke Pre-setup #8 (Citra Lestari, Activated, Email `citralestari@qwertysystem.net`, tanpa permintaan Email change live) `pendingEmailProfile_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_PENDING_PASSWORD`. Pelaku kedua admin: Pre-setup #6 (Hendra Wijaya) `adminActor_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_ADMIN_PASSWORD`, hanya lewat sesi API.
- Env var: `GS_PROFILE_TC_PASSWORD`, `GS_PROFILE_PENDING_PASSWORD`, `GS_PROFILE_ADMIN_PASSWORD`.
- Kondisi awal: Citra Lestari tanpa permintaan Email change live. Kemampuan sesi API admin untuk mengubah Email user dan membatalkan permintaan Email change disediakan tim BE/FE; endpoint tidak disebut TC dan ditentukan tim FE di tahap script.
- Pemulihan (R-08): langkah 13 membatalkan permintaan yang dibuat spec dan memulihkan Email Citra Lestari ke `citralestari@qwertysystem.net`; hook `after` mengulangi pemulihan itu bila spec gagal di tengah.
- State global yang diubah: permintaan Email change Citra Lestari. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-PROFILE-25: Tanpa permintaan live badge tidak tampil

1. Verifikasi badge `Active` tampil di Header
2. Verifikasi badge `Pending Email Confirmation` tidak tampil di Header

### TC-GS-PROFILE-208: Tanpa permintaan live banner dan teks bantu tidak tampil

3. Verifikasi nilai field Email di Section Identity adalah `andipratama@qwertysystem.net`
4. Verifikasi banner Pending Email Change tidak tampil
5. Verifikasi field Email tidak memiliki teks bantu pending

### TC-GS-PROFILE-246: Admin mengubah Email user, banner muncul di My Profile user tersebut

6. Pelaku kedua admin (Pre-setup #6) mengubah Email Citra Lestari menjadi `citra.baru@qwertysystem.net` lewat sesi API hingga permintaan Email change tersimpan
7. Tunggu aksi selesai
8. Logout dari akun Andi Pratama
9. Login sebagai Citra Lestari (Pre-setup #8)
10. Buka My Profile dari account menu navbar
11. Verifikasi banner tampil dengan teks `Pending email change to citra.baru@qwertysystem.net`
12. Verifikasi banner tidak memiliki tombol aksi
13. Pelaku kedua admin membatalkan permintaan Email change Citra Lestari lewat sesi API dan memulihkan Email ke `citralestari@qwertysystem.net`

## Notes

- Mode: FE+BE. Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan: screening tanpa permintaan live (TC-GS-PROFILE-25 dan 208) lebih dulu, lalu TC-GS-PROFILE-246 yang membuat permintaan dan berganti akun (S-07, langkah 8 dan 9 adalah Step ganti akun eksplisit).
- Pelaku kedua admin memakai sesi API (bukan konteks kedua), sehingga tidak memakai butir `P-2`.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 7 (tunggu aksi selesai sebelum ganti akun), 10 (membuka My Profile setelah login Citra), 13 (pemulihan state).
- Asersi tambahan di luar Expected TC (S-03): langkah 1 dan 3 adalah pembanding (anchor) untuk absence badge, banner, dan teks bantu (8b butir 2).
- Temuan untuk QA:
  - TC-GS-PROFILE-246 langkah 1 menyebut "Login sbg admin lalu ubah Email" lewat UI; spec memakai sesi API admin sebagai pemicu perubahan state (keputusan suite), dan tampilan di sesi UI Citra yang diasersi.
  - TC-GS-PROFILE-246 tidak menyebut pemulihan permintaan live dan Email Citra Lestari sesudah TC; spec menambahkan langkah 13.
