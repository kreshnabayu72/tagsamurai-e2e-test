---
id: TC-AUTH-ACT-E2E-027-token-ttl-time-travel
title: "Masa Berlaku Token 24 Jam"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-ACT-86
  - TC-AUTH-ACT-87
  - TC-AUTH-ACT-105
  - TC-AUTH-ACT-124
coverage:
  web: automated
---

# Masa Berlaku Token 24 Jam

## Prerequisites

- Mode: FE+BE.
- Kemampuan teknis: time-travel jam server uji (memajukan waktu), jendela privat browser, dan API seeding untuk mengambil link aktivasi serta memicu Resend. Spec ini tidak memakai mail-catcher.
- Hook `before` (lewat API, email bersuffix per run): buat user Pending Activation dengan token Active dan ambil link aktivasinya:
  - TC-AUTH-ACT-86: `Bagas Sulistyo` (`bagassulistyo+{runId}-027@qwertysystem.net`).
  - TC-AUTH-ACT-87: `Fitri Basuki` (`fitribasuki+{runId}-027@qwertysystem.net`).
  - TC-AUTH-ACT-105: `Eko Gunawan` (`ekogunawan+{runId}-027@qwertysystem.net`), token A diterbitkan pada T0.
  - TC-AUTH-ACT-124: `Kirana Lestari` (`kiranalestari+{runId}-027@qwertysystem.net`).
- Semua token diterbitkan pada T0 (saat hook `before`); usia token dibentuk dengan memajukan jam server di langkah spec sesuai urutan di Notes.
- Hook `after`: kembalikan jam server uji ke waktu nyata dan hapus semua user yang dibuat spec ini. Hook ini tetap jalan walau spec gagal di tengah.
- Password diambil dari environment variable `ACT_PASSWORD` (`Spectra.env.ACT_PASSWORD`). Kredensial akun aktor Total Control (Global Settings) diambil dari environment variable `GS_TC_PASSWORD` (`Spectra.env.GS_TC_PASSWORD`).
- TC-AUTH-ACT-86, 87, 124: tanpa login (halaman publik). TC-AUTH-ACT-105: Resend oleh akun Total Control (Global Settings).

## Test Steps

### TC-AUTH-ACT-105 (bagian 1): Resend pada T0 + 23 jam

1. Ambil link A user `Eko Gunawan` lewat API seeding (diterbitkan pada T0, saat hook `before`)
2. Majukan jam server uji ke T0 + 23 jam
3. Lakukan Resend Activation Email untuk `Eko Gunawan` sbg Total Control (Global Settings) lewat API, lalu ambil link B lewat API seeding (token B diterbitkan pada T0 + 23 jam)

### TC-AUTH-ACT-87: Link berusia 23 jam 59 menit masih menampilkan form Set Password

4. Majukan jam server uji ke T0 + 23 jam 59 menit (token user `Fitri Basuki` berusia 23 jam 59 menit)
5. Buka link aktivasi user `Fitri Basuki` di jendela privat baru tanpa sesi login
6. Verifikasi `Auth > Account Activation > Set Password` tampil dengan Subtitle "Set a password to log in for fitribasuki+{runId}-027@qwertysystem.net."
7. Verifikasi Halaman Invalid Link tidak tampil

### TC-AUTH-ACT-124: Token kedaluwarsa saat form terbuka: submit diarahkan ke halaman Invalid Link

8. Pada jam server yang sama (T0 + 23 jam 59 menit, token user `Kirana Lestari` berusia 23 jam 59 menit), buka link aktivasi user `Kirana Lestari` di jendela privat baru → halaman `Auth > Account Activation > Set Password` tampil
9. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
10. Majukan jam server uji ke T0 + 24 jam 1 menit (token berusia lebih dari 24 jam)
11. Klik button "Set Password"
12. Verifikasi Tab form diarahkan ke `Auth > Account Activation > Invalid Link` varian Expired (Title "Activation Link Expired")
13. Verifikasi Tidak ada set password yang tersimpan; tidak ada toast
14. Verifikasi Status user `Kirana Lestari` tetap Pending Activation

### TC-AUTH-ACT-86: Link berusia lebih dari 24 jam menampilkan halaman Invalid Link varian Expired

15. Majukan jam server uji ke T0 + 25 jam (token user `Bagas Sulistyo` berusia 25 jam)
16. Buka link aktivasi user `Bagas Sulistyo` di jendela privat baru tanpa sesi login
17. Verifikasi Halaman `Auth > Account Activation > Invalid Link` varian Expired tampil: Title "Activation Link Expired", Body "This activation link has expired. Activation links are valid for 24 hours. Please contact your administrator to receive a new activation email."
18. Verifikasi Tidak ada button CTA (tidak ada "Go to Login") pada halaman dan form Set Password tidak ditampilkan

### TC-AUTH-ACT-105 (bagian 2): Link hasil Resend berlaku 24 jam sejak token baru diterbitkan

19. Majukan jam server uji ke T0 + 30 jam
20. Di jendela privat baru tanpa sesi login, buka link A
21. Verifikasi Link A menampilkan `Auth > Account Activation > Invalid Link` varian Expired
22. Di jendela privat yang sama, buka link B
23. Verifikasi Link B menampilkan `Auth > Account Activation > Set Password` (30 jam sejak T0 tetapi 7 jam sejak diterbitkan; masa berlaku dihitung dari penerbitan token B)
24. Verifikasi Token A Superseded; token B Active

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Kelas harness d (time-travel). Link diambil lewat API seeding, bukan mail-catcher, supaya spec hanya memakai satu harness.
- Jam server hanya maju. Semua token diterbitkan pada T0 (hook `before`), lalu langkah memajukan jam ke T0 + 23 jam (Resend TC-AUTH-ACT-105), T0 + 23 jam 59 menit (TC-AUTH-ACT-87 dan buka form TC-AUTH-ACT-124), T0 + 24 jam 1 menit (submit TC-AUTH-ACT-124), T0 + 25 jam (TC-AUTH-ACT-86), lalu T0 + 30 jam (cek akhir TC-AUTH-ACT-105). TC-AUTH-ACT-105 dipecah menjadi dua subjudul karena Resend dan cek link-nya berada di titik waktu berbeda.
- Resend pada TC-AUTH-ACT-105 dilakukan lewat API dengan kredensial Total Control, sehingga tidak ada pergantian sesi browser.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
