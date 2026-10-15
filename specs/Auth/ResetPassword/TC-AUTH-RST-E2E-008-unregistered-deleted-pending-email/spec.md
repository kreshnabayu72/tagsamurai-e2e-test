---
id: TC-AUTH-RST-E2E-008-unregistered-deleted-pending-email
title: "Request dengan Email Tidak Terdaftar, Akun Dihapus, dan Email Pending"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-23
  - TC-AUTH-RST-24
  - TC-AUTH-RST-155
coverage:
  web: automated
---

# Request dengan Email Tidak Terdaftar, Akun Dihapus, dan Email Pending

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). User berstatus Activated (Joko Susilo dan Linda Sari) di-seed dengan password aktif `Spectra.env.RST_PASSWORD`. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: mail-catcher dengan pembacaan jumlah email per alamat (baseline sebelum aksi, dibandingkan sesudahnya); reCAPTCHA mode uji; jendela privat tanpa sesi login.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-23, TC-AUTH-RST-24, TC-AUTH-RST-155: User belum login (guest); browser web.
- TC-AUTH-RST-23: Email `belumterdaftar+{runId}-008@qwertysystem.net` tidak ada di database user.
- TC-AUTH-RST-24: User `Joko Susilo` (`jokosusilo+{runId}-008@qwertysystem.net`) berstatus Deleted (di-seed lalu dihapus lewat API di hook `before`).
- TC-AUTH-RST-155: User `Linda Sari` (`lindasari+{runId}-008@qwertysystem.net`) berstatus Active dan Activated; email baru `lindasari.baru+{runId}-008@qwertysystem.net` pending konfirmasi (perubahan email diinisiasi admin lewat API di hook `before`, belum dikonfirmasi).

## Test Steps

### TC-AUTH-RST-23: Email yang tidak terdaftar

1. Buka jendela privat baru lalu buka halaman Reset Password (Request)
2. Catat jumlah email di mail-catcher untuk `belumterdaftar+{runId}-008@qwertysystem.net` sebagai baseline
3. Ketik `belumterdaftar+{runId}-008@qwertysystem.net` pada field Email
4. Selesaikan reCAPTCHA (centang "I'm not a robot")
5. Klik Button [Reset Password]
6. Verifikasi caption inline di bawah field Email: "Email is not registered yet"
7. Verifikasi field Email berstatus Invalid
8. Verifikasi browser tetap di halaman Reset Password
9. Verifikasi input Email dipertahankan
10. Verifikasi jumlah email di mail-catcher untuk `belumterdaftar+{runId}-008@qwertysystem.net` sama dengan baseline

### TC-AUTH-RST-24: Email milik akun yang sudah dihapus

11. Muat ulang halaman Reset Password (F5)
12. Catat jumlah email di mail-catcher untuk `jokosusilo+{runId}-008@qwertysystem.net` sebagai baseline
13. Ketik `jokosusilo+{runId}-008@qwertysystem.net` pada field Email
14. Selesaikan reCAPTCHA (centang "I'm not a robot")
15. Klik Button [Reset Password]
16. Verifikasi caption inline di bawah field Email: "Email is not registered yet"
17. Verifikasi jumlah email di mail-catcher untuk `jokosusilo+{runId}-008@qwertysystem.net` sama dengan baseline

### TC-AUTH-RST-155: Email pending (baru) diperlakukan sebagai tidak terdaftar

18. Muat ulang halaman Reset Password (F5)
19. Catat jumlah email di mail-catcher untuk `lindasari.baru+{runId}-008@qwertysystem.net` sebagai baseline
20. Ketik `lindasari.baru+{runId}-008@qwertysystem.net` pada field Email
21. Selesaikan reCAPTCHA (centang "I'm not a robot")
22. Klik Button [Reset Password]
23. Verifikasi caption inline di bawah field Email: "Email is not registered yet"
24. Verifikasi browser tetap di halaman Reset Password
25. Verifikasi jumlah email di mail-catcher untuk `lindasari.baru+{runId}-008@qwertysystem.net` sama dengan baseline

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`. Semua kasus ditolak karena kondisi data target; tidak ada token yang tercipta.
- Asersi "tidak ada entri log" pada TC-AUTH-RST-23, 24, 155 diuji di spec `TC-AUTH-RST-E2E-043-absence-not-logged` (kelas g, prinsip 10).
- Muat ulang halaman antar-TC adalah langkah penghubung (S-03).
- Langkah mencatat jumlah email di mail-catcher sebelum aksi adalah baseline asersi "tidak ada email" (S-12, S-03).
- Temuan untuk QA: Post Condition TC-AUTH-RST-23, 24, 155 (tidak ada token dibuat) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
