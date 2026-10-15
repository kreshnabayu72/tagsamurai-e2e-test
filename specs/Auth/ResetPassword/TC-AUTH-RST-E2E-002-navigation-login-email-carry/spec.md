---
id: TC-AUTH-RST-E2E-002-navigation-login-email-carry
title: "Navigasi Login with Password dan Reset Password serta Pembawaan Email"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-04
  - TC-AUTH-RST-05
  - TC-AUTH-RST-116
coverage:
  web: automated
---

# Navigasi Login with Password dan Reset Password serta Pembawaan Email

## Prerequisites

- Mode: FE+BE.
- Seeding: dua user subjek (`Budi Santoso` dan `Hendra Wijaya`) dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`; email memakai suffix per run `+{runId}-002`. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: jendela privat tanpa sesi login; fixture BE untuk menetapkan lock requires-reset pada user; reCAPTCHA mode uji di environment; pengamatan request jaringan ke endpoint Request (memastikan tidak ada request keluar).
- TC-AUTH-RST-04, TC-AUTH-RST-05, TC-AUTH-RST-116: User belum login (guest); browser web.
- TC-AUTH-RST-04, TC-AUTH-RST-05: User `Budi Santoso` (`budisantoso+{runId}-002@qwertysystem.net`) berstatus Active dan Activated.
- TC-AUTH-RST-116: User `Hendra Wijaya` (`hendrawijaya+{runId}-002@qwertysystem.net`) berstatus Active dengan lock wajib reset (requires-reset, di-set fixture BE).

## Test Steps

### TC-AUTH-RST-04: Email di Login with Password terbawa ke halaman Reset Password

1. Buka jendela privat baru (tanpa sesi login) lalu buka halaman Login with Password
2. Ketik `budisantoso+{runId}-002@qwertysystem.net` pada field Email
3. Klik tautan [Reset here]
4. Verifikasi browser menuju halaman Reset Password (Request)
5. Verifikasi field Email terisi `budisantoso+{runId}-002@qwertysystem.net`
6. Verifikasi field Email tidak read-only (dapat diubah)

### TC-AUTH-RST-05: Email di Reset Password terbawa saat klik link Log in with password

7. Buka jendela privat baru lalu buka halaman Reset Password (Request)
8. Mulai pengamatan request jaringan ke endpoint Request
9. Ketik `budisantoso+{runId}-002@qwertysystem.net` pada field Email
10. Klik link "Log in with password"
11. Verifikasi browser menuju halaman Login with Password
12. Verifikasi field Email pada halaman Login with Password terisi `budisantoso+{runId}-002@qwertysystem.net`
13. Verifikasi field Email pada halaman Login with Password dapat diubah
14. Verifikasi tidak ada permintaan reset yang dikirim

### TC-AUTH-RST-116: Alert lock requires-reset di Login mengarahkan ke alur Reset Password

15. Buka jendela privat baru lalu buka halaman Login with Password
16. Login dengan Email `hendrawijaya+{runId}-002@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD` (selesaikan reCAPTCHA)
17. Verifikasi Alert Danger tampil: "Please reset your password" dengan tautan [Reset password]
18. Klik tautan [Reset password] di bawah teks Alert
19. Verifikasi browser menuju halaman Reset Password
20. Verifikasi field Email terisi `hendrawijaya+{runId}-002@qwertysystem.net`

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Asersi "tidak ada entri log" pada TC-AUTH-RST-05 (Expected c) diuji di spec `TC-AUTH-RST-E2E-043-absence-not-logged` (kelas g, prinsip 10) lewat aksi nyata yang sama (ketik email, klik link "Log in with password") dengan baseline log sendiri. Id TC-AUTH-RST-05 tetap di `sourceTc` spec ini; rujukan dicatat di Notes kedua spec (S-05).
- Langkah membuka jendela privat baru di awal TC-AUTH-RST-04, TC-AUTH-RST-05 (langkah 7), dan TC-AUTH-RST-116 adalah langkah penghubung antar-TC (S-03). Pada TC-AUTH-RST-05 langkah itu memberi halaman Reset Password dengan field Email kosong sebelum email diketik. Langkah 8 (mulai pengamatan request jaringan ke endpoint Request) juga langkah penghubung (S-03): pengamatan harus aktif sebelum aksi di langkah 9 dan 10 agar asersi langkah 14 dapat membuktikan tidak ada request keluar.
- TC-AUTH-RST-116 memakai password `Spectra.env.RST_PASSWORD` (TC menulis "Password apa pun"); user berstatus lock requires-reset sehingga login ditolak sebelum evaluasi password.
