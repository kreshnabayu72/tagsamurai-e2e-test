---
id: TC-AUTH-RST-E2E-004-recaptcha-gate-web
title: "Gate reCAPTCHA pada Halaman Request di Web"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-19
  - TC-AUTH-RST-20
  - TC-AUTH-RST-22
coverage:
  web: automated
---

# Gate reCAPTCHA pada Halaman Request di Web

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`; email `+{runId}-004`. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: reCAPTCHA mode uji yang kedaluwarsa mengikuti jam browser (TC-AUTH-RST-20 memajukan jam browser sebanyak masa berlaku token reCAPTCHA di environment sampai widget berstatus expired); jendela privat tanpa sesi login; mail-catcher dengan pembacaan jumlah email per alamat (baseline sebelum aksi, dibandingkan sesudahnya).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- State global yang diubah: jam browser (dimajukan pada TC-AUTH-RST-20). Suite berjalan serial (`parallel: false`). Pemulihan: jam browser dipulihkan pada langkah terakhir spec dan di hook `after` (tetap berjalan walau spec gagal di tengah).
- TC-AUTH-RST-19, TC-AUTH-RST-20, TC-AUTH-RST-22: User belum login (guest); browser web.
- TC-AUTH-RST-22, TC-AUTH-RST-19, TC-AUTH-RST-20: User `Budi Santoso` (`budisantoso+{runId}-004@qwertysystem.net`) berstatus Active.

## Test Steps

### TC-AUTH-RST-22: Email kosong dan reCAPTCHA belum dicentang sekaligus

1. Buka jendela privat baru lalu buka halaman Reset Password (Request)
2. Catat jumlah email di mail-catcher untuk `budisantoso+{runId}-004@qwertysystem.net` sebagai baseline
3. Klik Button [Reset Password]
4. Verifikasi caption inline di bawah field Email: "Email must not be empty"
5. Verifikasi caption "Please verify that you are not a robot" tampil di bawah widget reCAPTCHA pada saat yang sama
6. Verifikasi browser tetap di halaman Reset Password
7. Verifikasi jumlah email di mail-catcher untuk `budisantoso+{runId}-004@qwertysystem.net` sama dengan baseline

### TC-AUTH-RST-19: Email valid dan reCAPTCHA belum dicentang

8. Muat ulang halaman Reset Password (F5)
9. Catat jumlah email di mail-catcher untuk `budisantoso+{runId}-004@qwertysystem.net` sebagai baseline
10. Ketik `budisantoso+{runId}-004@qwertysystem.net` pada field Email
11. Klik Button [Reset Password]
12. Verifikasi caption inline: "Please verify that you are not a robot"
13. Verifikasi browser tetap di halaman Reset Password
14. Verifikasi jumlah email di mail-catcher untuk `budisantoso+{runId}-004@qwertysystem.net` sama dengan baseline

### TC-AUTH-RST-20: Token reCAPTCHA kedaluwarsa

15. Muat ulang halaman Reset Password (F5)
16. Catat jumlah email di mail-catcher untuk `budisantoso+{runId}-004@qwertysystem.net` sebagai baseline
17. Ketik `budisantoso+{runId}-004@qwertysystem.net` pada field Email
18. Selesaikan reCAPTCHA (centang "I'm not a robot")
19. Majukan jam browser sebanyak masa berlaku token reCAPTCHA di environment sampai widget reCAPTCHA berstatus expired (token tidak berlaku lagi)
20. Klik Button [Reset Password]
21. Verifikasi caption inline: "Please verify that you are not a robot"
22. Verifikasi jumlah email di mail-catcher untuk `budisantoso+{runId}-004@qwertysystem.net` sama dengan baseline
23. Pulihkan jam browser ke waktu saat ini

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Urutan di spec: TC-AUTH-RST-22, lalu TC-AUTH-RST-19, dan TC-AUTH-RST-20 paling akhir karena memajukan jam browser. Muat ulang halaman antar-TC dan pemulihan jam browser adalah langkah penghubung (S-03, S-09).
- Asersi "tidak ada entri log" pada TC-AUTH-RST-19 diuji di spec `TC-AUTH-RST-E2E-043-absence-not-logged` (kelas g).
- Langkah mencatat jumlah email di mail-catcher sebelum aksi adalah baseline asersi "tidak ada email terkirim" (S-12, S-03). Pada TC-AUTH-RST-22 field Email kosong, sehingga baseline diambil pada alamat user spec ini.
- Temuan untuk QA: Post Condition TC-AUTH-RST-19, 20, 22 ("tidak ada token baru") serta "tidak ada entri log" TC-AUTH-RST-20 dan 22 tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
- Temuan untuk QA: TC-AUTH-RST-20 tidak menyebut cara memicu token kedaluwarsa; spec memajukan jam browser (bagian 6). Bila widget reCAPTCHA mode uji tidak mengikuti jam browser, pemicu pengganti (token reCAPTCHA yang dipaksa expired) perlu disepakati dengan tim FE/BE (S-15).
