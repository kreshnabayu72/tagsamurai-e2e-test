---
id: TC-AUTH-RST-E2E-030-lock-recovery-15m-1h-requires-reset
title: "Pemulihan Lock 15 Menit, 1 Jam, dan Requires Reset lewat Reset Password"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-106
  - TC-AUTH-RST-107
  - TC-AUTH-RST-108
coverage:
  web: automated
---

# Pemulihan Lock 15 Menit, 1 Jam, dan Requires Reset lewat Reset Password

## Prerequisites

- Mode: FE+BE (dengan fixture lock BE).
- Seeding: tiga user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password aktif `Spectra.env.RST_PASSWORD` dan tanpa gate Agreement dan MFA (fixture BE); level lock tiap user diatur fixture BE. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`.
- Kemampuan teknis: fixture BE untuk lock progression per user; mail-catcher dengan pembacaan jumlah email per alamat; reCAPTCHA mode uji; jendela privat tanpa sesi login.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat suite.md); mekanisme reset disediakan tim FE/BE.
- Hook `after` menutup semua jendela privat, menghapus sesi browser, dan mengembalikan sesi ke akun default suite.
- TC-AUTH-RST-106, TC-AUTH-RST-107, TC-AUTH-RST-108: User belum login (guest); browser web; data Password baru: `Spectra.env.RST_PASSWORD_NEW` pada Password dan Confirm Password.
- TC-AUTH-RST-106: User `Agus Prasetyo` (`agusprasetyo+{runId}-030a@qwertysystem.net`) Active dengan lock 15 menit.
- TC-AUTH-RST-107: User `Rina Wulandari` (`rinawulandari+{runId}-030b@qwertysystem.net`) Active dengan lock 1 jam.
- TC-AUTH-RST-108: User `Hendra Wijaya` (`hendrawijaya+{runId}-030c@qwertysystem.net`) Active dengan lock wajib reset (requires-reset).

## Test Steps

### TC-AUTH-RST-106: Reset sukses membersihkan lock 15 menit

1. Buka jendela privat baru lalu buka halaman Reset Password (Request)
2. Catat jumlah email di mail-catcher untuk `agusprasetyo+{runId}-030a@qwertysystem.net` sebagai baseline
3. Ketik `agusprasetyo+{runId}-030a@qwertysystem.net`, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password]
4. Verifikasi Request pada akun terkunci diproses: browser menuju halaman Email Sent!
5. Verifikasi jumlah email di mail-catcher untuk `agusprasetyo+{runId}-030a@qwertysystem.net` bertambah 1 dibanding baseline (email reset masuk)
6. Buka tautan reset dari email lalu ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password, kemudian klik Button [Reset Password]
7. Verifikasi browser menuju halaman Password Reset Successful
8. Klik Button [Go to Login Page]
9. Login dengan Email `agusprasetyo+{runId}-030a@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD_NEW` (selesaikan reCAPTCHA)
10. Verifikasi login berhasil
11. Verifikasi tidak ada caption lock
12. Verifikasi tidak ada Alert lock
13. Verifikasi browser menuju Portal — Product Hub
14. Keluar dari akun (logout), lalu tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-RST-107: Reset sukses membersihkan lock 1 jam

15. Buka jendela privat baru lalu buka halaman Reset Password (Request)
16. Catat jumlah email di mail-catcher untuk `rinawulandari+{runId}-030b@qwertysystem.net` sebagai baseline
17. Ketik `rinawulandari+{runId}-030b@qwertysystem.net`, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password]
18. Verifikasi Request pada akun terkunci diproses: browser menuju halaman Email Sent!
19. Verifikasi jumlah email di mail-catcher untuk `rinawulandari+{runId}-030b@qwertysystem.net` bertambah 1 dibanding baseline (email reset masuk)
20. Buka tautan reset dari email lalu ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password, kemudian klik Button [Reset Password]
21. Verifikasi browser menuju halaman Password Reset Successful
22. Klik Button [Go to Login Page]
23. Login dengan Email `rinawulandari+{runId}-030b@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD_NEW` (selesaikan reCAPTCHA)
24. Verifikasi login berhasil
25. Verifikasi tidak ada caption lock
26. Verifikasi tidak ada Alert lock
27. Verifikasi browser menuju Portal — Product Hub
28. Keluar dari akun (logout), lalu tutup semua jendela privat dan hapus sesi browser terkait

### TC-AUTH-RST-108: Reset sukses membersihkan lock requires-reset

29. Buka jendela privat baru lalu buka halaman Reset Password (Request)
30. Catat jumlah email di mail-catcher untuk `hendrawijaya+{runId}-030c@qwertysystem.net` sebagai baseline
31. Ketik `hendrawijaya+{runId}-030c@qwertysystem.net`, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password]
32. Verifikasi Request pada akun terkunci diproses: browser menuju halaman Email Sent!
33. Verifikasi jumlah email di mail-catcher untuk `hendrawijaya+{runId}-030c@qwertysystem.net` bertambah 1 dibanding baseline (email reset masuk)
34. Buka tautan reset dari email lalu ketik `Spectra.env.RST_PASSWORD_NEW` pada field Password dan field Confirm Password, kemudian klik Button [Reset Password]
35. Verifikasi browser menuju halaman Password Reset Successful
36. Klik Button [Go to Login Page]
37. Login dengan Email `hendrawijaya+{runId}-030c@qwertysystem.net` dan Password `Spectra.env.RST_PASSWORD_NEW` (selesaikan reCAPTCHA)
38. Verifikasi login berhasil
39. Verifikasi tidak ada caption lock
40. Verifikasi tidak ada Alert lock
41. Verifikasi browser menuju Portal — Product Hub

## Notes

- Sumber: `auth/reset-password/TestCases/tc-reset-password.md`. Tiga level lock memakai tiga user terpisah.
- Jendela privat ditutup dan sesi browser dihapus di akhir blok TC-AUTH-RST-106 dan TC-AUTH-RST-107 supaya blok berikutnya tidak mewarisi sesi Portal; hook `after` menutup jendela yang tersisa (S-09).
- Temuan untuk QA: Post Condition TC-AUTH-RST-106, 107, 108 (lock progression none dan counter kegagalan 0) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
- Lock permanen dan counter eskalasi diuji di spec `TC-AUTH-RST-E2E-031-lock-recovery-permanent-counters`.
- Jumlah langkah 41 melampaui ±35: alasan satu topik (pemulihan lock lewat Reset Password) dan satu kelas, tiga level lock (15 menit, 1 jam, requires reset) berurutan; 21 langkah Verifikasi akibat pemecahan per klausa (S-01), 20 langkah aksi dan penghubung (baseline email, logout, jendela privat), tanpa prefix login berulang.
