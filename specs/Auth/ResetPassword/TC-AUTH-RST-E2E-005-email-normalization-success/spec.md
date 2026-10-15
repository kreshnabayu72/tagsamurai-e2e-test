---
id: TC-AUTH-RST-E2E-005-email-normalization-success
title: "Normalisasi Email pada Request: Trim, Huruf Besar, dan Plus-Addressing"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-RST-13
  - TC-AUTH-RST-14
  - TC-AUTH-RST-146
coverage:
  web: automated
---

# Normalisasi Email pada Request: Trim, Huruf Besar, dan Plus-Addressing

## Prerequisites

- Mode: FE+BE.
- Seeding: tiga user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), masing-masing Activated dan Active dengan password `Spectra.env.RST_PASSWORD`, tanpa token reset aktif dan tanpa percobaan reset. Tiga user terpisah dipakai supaya cooldown 60 detik per email tidak membuat Request berikutnya menjadi no-op. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: mail-catcher (membaca email reset dan tautannya) dengan pembacaan jumlah email per alamat (baseline sebelum aksi, dibandingkan sesudahnya); reCAPTCHA mode uji; jendela privat tanpa sesi login.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-13, TC-AUTH-RST-14, TC-AUTH-RST-146: User belum login (guest); browser web.
- TC-AUTH-RST-13: User `Budi Santoso` (`budisantoso+{runId}-005a@qwertysystem.net`) berstatus Active; data: Email `  budisantoso+{runId}-005a@qwertysystem.net  ` (spasi di awal dan akhir).
- TC-AUTH-RST-14: User `Citra Dewi` (`citradewi+{runId}-005b@qwertysystem.net`) berstatus Active, terdaftar dengan huruf kecil; data: Email `CitraDewi+{runId}-005b@QwertySystem.net`.
- TC-AUTH-RST-146: User `Nadia Kusuma` (`nadiakusuma+tag{runId}-005@qwertysystem.net`) berstatus Active, terdaftar dengan email ber-plus-addressing; data: Email `nadiakusuma+tag{runId}-005@qwertysystem.net`.

## Test Steps

### TC-AUTH-RST-13: Email dengan spasi di awal dan akhir di-trim

1. Buka jendela privat baru lalu buka halaman Reset Password (Request)
2. Catat jumlah email di mail-catcher untuk `budisantoso+{runId}-005a@qwertysystem.net` sebagai baseline
3. Ketik `  budisantoso+{runId}-005a@qwertysystem.net  ` (dengan spasi di awal dan akhir) pada field Email
4. Selesaikan reCAPTCHA (centang "I'm not a robot")
5. Klik Button [Reset Password]
6. Verifikasi browser menuju halaman Email Sent!
7. Verifikasi tidak ada toast
8. Verifikasi Message memuat `budisantoso+{runId}-005a@qwertysystem.net` tanpa spasi tambahan
9. Verifikasi jumlah email di mail-catcher untuk `budisantoso+{runId}-005a@qwertysystem.net` bertambah 1 dibanding baseline

### TC-AUTH-RST-14: Email berhuruf besar untuk user yang terdaftar dengan huruf kecil

10. Buka halaman Reset Password (Request) di jendela privat baru
11. Catat jumlah email di mail-catcher untuk `citradewi+{runId}-005b@qwertysystem.net` sebagai baseline
12. Ketik `CitraDewi+{runId}-005b@QwertySystem.net` pada field Email
13. Selesaikan reCAPTCHA (centang "I'm not a robot")
14. Klik Button [Reset Password]
15. Verifikasi browser menuju halaman Email Sent!
16. Verifikasi tidak ada toast
17. Verifikasi Message tampil "We've sent a password reset link to CitraDewi+{runId}-005b@QwertySystem.net. Please check your inbox and follow the instructions." (email persis seperti diketik setelah trim)
18. Verifikasi jumlah email di mail-catcher untuk akun `citradewi+{runId}-005b@qwertysystem.net` bertambah 1 dibanding baseline

### TC-AUTH-RST-146: Email ber-plus-addressing diproses dan Message menampilkan email persis seperti diketik

19. Buka halaman Reset Password (Request) di jendela privat baru
20. Catat jumlah email di mail-catcher untuk `nadiakusuma+tag{runId}-005@qwertysystem.net` sebagai baseline
21. Ketik `nadiakusuma+tag{runId}-005@qwertysystem.net` pada field Email
22. Selesaikan reCAPTCHA (centang "I'm not a robot")
23. Klik Button [Reset Password]
24. Verifikasi caption "Email format is incorrect" tidak tampil
25. Verifikasi browser menuju halaman Email Sent!
26. Verifikasi tidak ada toast
27. Verifikasi Message tampil "We've sent a password reset link to nadiakusuma+tag{runId}-005@qwertysystem.net. Please check your inbox and follow the instructions."
28. Verifikasi jumlah email di mail-catcher untuk `nadiakusuma+tag{runId}-005@qwertysystem.net` bertambah 1 dibanding baseline

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- TC-AUTH-RST-13 dan TC-AUTH-RST-14 di TC sumber memakai user yang sama (`budisantoso`); di spec dipisah ke dua user karena Request kedua untuk email yang sama dalam 60 detik menjadi no-op (cooldown). TC-AUTH-RST-146 bergantung pada TC-AUTH-RST-12 di TC; langkah alur dasarnya disalin utuh di sini (S-04).
- Pembukaan halaman Reset Password baru di jendela privat antar-TC adalah langkah penghubung (S-03).
- Langkah mencatat jumlah email di mail-catcher sebelum aksi adalah baseline asersi "email reset masuk" (bertambah 1 dibanding baseline); langkah itu adalah langkah penghubung (S-12, S-03).
- Temuan untuk QA: Post Condition TC-AUTH-RST-14 dan TC-AUTH-RST-146 (token reset aktif baru terbit) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
