---
id: TC-AUTH-RST-E2E-045-android-reset-screen
title: "Layar Reset Password Android: Tanpa reCAPTCHA, Button Terjangkau, Request, dan Atribut Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-06
  - TC-AUTH-RST-150
  - TC-AUTH-RST-07
  - TC-AUTH-RST-102
coverage:
  mobile: automated
  web: automated
---

# Layar Reset Password Android: Tanpa reCAPTCHA, Button Terjangkau, Request, dan Atribut Log

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek `Budi Santoso` (`budisantoso+{runId}-045@qwertysystem.net`) dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`, tanpa percobaan reset. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: aplikasi native Android TAG Samurai Mobile (perangkat atau emulator) dengan keyboard layar; browser Chrome di Windows untuk Request web (TC-AUTH-RST-102); mail-catcher; reCAPTCHA mode uji untuk web; jendela admin (membaca Global Settings > User > Detail > User Log); pengaturan jam server dan jam browser Chrome di Windows bersama (cooldown ditegakkan di server; countdown pada layar Email Sent! tidak diamati di Android).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- State global yang diubah: jam server dan jam browser Chrome di Windows. Suite berjalan serial (`parallel: false`). Pemulihan: kedua jam dipulihkan di hook `after` (tetap berjalan walau spec gagal di tengah).
- TC-AUTH-RST-06, TC-AUTH-RST-150, TC-AUTH-RST-07: User belum login; aplikasi native Android TAG Samurai Mobile.
- TC-AUTH-RST-102: Request sukses dari browser Chrome di Windows dan dari aplikasi Android untuk `budisantoso+{runId}-045@qwertysystem.net`; admin `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Total Control).

## Test Steps

### TC-AUTH-RST-06: Screening layar Reset Password di aplikasi Android tidak merender reCAPTCHA

1. Buka layar Reset Password di aplikasi Android
2. Susuri layar dari atas ke bawah
3. Verifikasi logo tampil
4. Verifikasi Title "Reset Password" tampil
5. Verifikasi Subtitle "Enter your email and we'll send you a link to reset your password." tampil
6. Verifikasi field Email dengan label "Email" tampil
7. Verifikasi field Email dengan placeholder "Enter your email" tampil
8. Verifikasi Button [Reset Password] lebar penuh tampil
9. Verifikasi link "Log in with password" tampil di bawah button
10. Verifikasi **Must NOT**: widget reCAPTCHA dan caption "Please verify that you are not a robot" tidak dirender

### TC-AUTH-RST-150: Button utama berlabuh di bawah formulir dan tetap terjangkau saat keyboard terbuka

11. Amati posisi Button [Reset Password] sebelum keyboard muncul
12. Verifikasi Button [Reset Password] lebar penuh
13. Verifikasi Button [Reset Password] berlabuh di bagian bawah formulir
14. Ketuk field Email sehingga keyboard terbuka
15. Amati posisi Button [Reset Password] dan field Email dengan keyboard terbuka
16. Verifikasi Button [Reset Password] tetap terlihat
17. Verifikasi Button [Reset Password] dapat diketuk tanpa menutup keyboard
18. Verifikasi field Email tidak tertutup keyboard

### TC-AUTH-RST-07: Request reset dari aplikasi Android tanpa reCAPTCHA diproses sukses

19. Catat jumlah email di mail-catcher untuk `budisantoso+{runId}-045@qwertysystem.net` sebagai baseline M1
20. Ketik `budisantoso+{runId}-045@qwertysystem.net` pada field Email
21. Ketuk Button [Reset Password]
22. Verifikasi aplikasi menampilkan layar Email Sent!
23. Verifikasi tidak ada toast
24. Periksa mail-catcher untuk `budisantoso+{runId}-045@qwertysystem.net`
25. Verifikasi jumlah email untuk `budisantoso+{runId}-045@qwertysystem.net` bertambah tepat 1 dibanding baseline M1

### TC-AUTH-RST-102: Atribut entri log: IP Address dan Device / Browser

26. Majukan jam server dan jam browser Chrome di Windows 61 detik sejak Request dari aplikasi Android
27. Di browser Chrome di Windows, buka halaman Reset Password (Request), ketik `budisantoso+{runId}-045@qwertysystem.net`, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password]
28. Pulihkan jam server dan jam browser Chrome di Windows ke waktu nyata
29. Buka jendela privat admin; login sebagai akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` (selesaikan reCAPTCHA), lalu buka Global Settings > User > Detail > User Log untuk user "Budi Santoso"
30. Periksa kolom IP Address dan Device / Browser pada dua entri Request
31. Verifikasi kolom IP Address memuat alamat IP request pada kedua entri
32. Verifikasi kolom Device / Browser entri web memuat "Chrome on Windows"
33. Verifikasi kolom Device / Browser entri Android memuat "TAG Samurai App on Android"

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md` (TC-AUTH-RST-150 dan 102 Manual Only; kebutuhan perangkat ditulis di Prerequisites).
- Urutan: TC-AUTH-RST-06 dan 150 tanpa aksi lebih dulu; TC-AUTH-RST-07 membuat token; TC-AUTH-RST-102 menunggu cooldown lalu memakai email yang sama dari web supaya kedua Request tercatat. Langkah 28 memulihkan jam sebelum admin membuka User Log (S-09). Login admin di langkah TC-AUTH-RST-102 (langkah 29, jendela privat admin dibuka pada langkah yang sama) adalah pembukaan konteks admin yang eksplisit (S-07).
- Temuan untuk QA: TC-AUTH-RST-102 menulis dua Request tanpa menyebut jeda; spec menambah jeda 61 detik (jam dimajukan, konvensi bagian 6) karena Request kedua dalam 60 detik menjadi no-op dan tidak dicatat (S-15).
