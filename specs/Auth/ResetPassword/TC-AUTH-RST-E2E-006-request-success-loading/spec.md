---
id: TC-AUTH-RST-E2E-006-request-success-loading
title: "Request Reset Sukses dan Loading pada Button Reset Password"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-12
  - TC-AUTH-RST-28
coverage:
  web: automated
---

# Request Reset Sukses dan Loading pada Button Reset Password

## Prerequisites

- Mode: FE+BE.
- Seeding: dua user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`, tanpa token reset aktif dan tanpa percobaan reset. Dua user dipakai supaya cooldown 60 detik per email tidak membuat Request kedua menjadi no-op. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: mail-catcher dengan pembacaan jumlah email per alamat (baseline sebelum aksi, dibandingkan sesudahnya); reCAPTCHA mode uji; jendela privat tanpa sesi login; penahanan respons endpoint Request dengan `Spectra.intercept` yang menahan respons lalu meneruskannya ke backend nyata.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-12, TC-AUTH-RST-28: User belum login (guest); browser web.
- TC-AUTH-RST-12: User `Budi Santoso` (`budisantoso+{runId}-006a@qwertysystem.net`) berstatus Active, tanpa token reset aktif.
- TC-AUTH-RST-28: User `Citra Dewi` (`citradewi+{runId}-006b@qwertysystem.net`) berstatus Active; respons server diperlambat.

## Test Steps

### TC-AUTH-RST-12: Request reset dengan email terdaftar, Active, dan reCAPTCHA terselesaikan

1. Buka jendela privat baru lalu buka halaman Reset Password (Request)
2. Catat jumlah email di mail-catcher untuk `budisantoso+{runId}-006a@qwertysystem.net` sebagai baseline
3. Ketik `budisantoso+{runId}-006a@qwertysystem.net` pada field Email
4. Selesaikan reCAPTCHA (centang "I'm not a robot")
5. Klik Button [Reset Password]
6. Verifikasi browser menuju halaman Email Sent!
7. Verifikasi tidak ada toast
8. Verifikasi pada halaman Email Sent!, Message tampil "We've sent a password reset link to budisantoso+{runId}-006a@qwertysystem.net. Please check your inbox and follow the instructions."
9. Buka email yang masuk di mail-catcher untuk `budisantoso+{runId}-006a@qwertysystem.net`
10. Verifikasi jumlah email di mail-catcher untuk `budisantoso+{runId}-006a@qwertysystem.net` bertambah 1 dibanding baseline
11. Verifikasi email memuat tautan reset (isi Subject dan Body diasersi di spec `TC-AUTH-RST-E2E-007-reset-email-content-and-link`)

### TC-AUTH-RST-28: Button Reset Password menampilkan loading dan disabled selama Request diproses

12. Buka halaman Reset Password (Request) di jendela privat baru
13. Ketik `citradewi+{runId}-006b@qwertysystem.net` pada field Email
14. Selesaikan reCAPTCHA (centang "I'm not a robot")
15. Pasang `Spectra.intercept` pada endpoint Request: tahan respons dan teruskan ke backend nyata setelah dilepas
16. Klik Button [Reset Password]
17. Amati Button [Reset Password] sebelum respons server tiba
18. Verifikasi Button [Reset Password] disabled selama proses
19. Verifikasi loading spinner memutar pada Button [Reset Password] selama proses
20. Lepaskan respons endpoint Request yang ditahan `Spectra.intercept` dan teruskan ke backend nyata
21. Verifikasi setelah respons tiba, browser menuju halaman Email Sent!

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`. Respons yang diperlambat tetap diteruskan ke backend nyata (bukan fault injection, bukan kelas b).
- Dua user dipakai karena TC-AUTH-RST-12 dan TC-AUTH-RST-28 di TC sumber memakai user yang sama; Request kedua dalam 60 detik menjadi no-op.
- Pembukaan halaman Reset Password baru antar-TC adalah langkah penghubung (S-03).
- Langkah mencatat jumlah email di mail-catcher sebelum aksi adalah baseline asersi "email reset masuk" (S-12, S-03).
- Langkah memasang `Spectra.intercept` pada endpoint Request sebelum klik [Reset Password] pada TC-AUTH-RST-28 adalah langkah penghubung (S-03); langkah melepas penahan memutus intercept sesudah asersi loading (S-09).
- Temuan untuk QA: Post Condition TC-AUTH-RST-12 (token active dan counter +1) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15). Post Condition TC-AUTH-RST-28 bernilai `-`.
