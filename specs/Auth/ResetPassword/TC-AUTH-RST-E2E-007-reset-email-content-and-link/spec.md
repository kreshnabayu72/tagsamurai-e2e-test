---
id: TC-AUTH-RST-E2E-007-reset-email-content-and-link
title: "Isi Email Reset dan Tautan yang Membuka Setup New Password"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-118
  - TC-AUTH-RST-145
coverage:
  web: automated
---

# Isi Email Reset dan Tautan yang Membuka Setup New Password

## Prerequisites

- Mode: FE+BE.
- Seeding: dua user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`, tanpa token reset aktif. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: mail-catcher dengan pembacaan jumlah email per alamat (baseline sebelum aksi, dibandingkan sesudahnya) yang dapat dibaca isi email (Subject, Body, tombol, tautan mentah) dan mengklik tombol di dalamnya; reCAPTCHA mode uji; jendela privat tanpa sesi login.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-118, TC-AUTH-RST-145: User belum login (guest); browser web.
- TC-AUTH-RST-118: User `Budi Santoso` (`budisantoso+{runId}-007a@qwertysystem.net`) berstatus Active.
- TC-AUTH-RST-145: User `Kartika Wati` (`kartikawati+{runId}-007b@qwertysystem.net`) berstatus Active; nama user di profil "Kartika Wati".

## Test Steps

### TC-AUTH-RST-118: Email reset memuat tautan yang membuka Setup New Password

1. Buka jendela privat baru lalu buka halaman Reset Password (Request)
2. Catat jumlah email di mail-catcher untuk `budisantoso+{runId}-007a@qwertysystem.net` sebagai baseline
3. Ketik `budisantoso+{runId}-007a@qwertysystem.net` pada field Email
4. Selesaikan reCAPTCHA (centang "I'm not a robot")
5. Klik Button [Reset Password]
6. Verifikasi jumlah email di mail-catcher untuk `budisantoso+{runId}-007a@qwertysystem.net` bertambah 1 dibanding baseline
7. Buka email yang masuk di mail-catcher untuk `budisantoso+{runId}-007a@qwertysystem.net`
8. Verifikasi email diterima oleh `budisantoso+{runId}-007a@qwertysystem.net`
9. Verifikasi email memuat satu tautan reset
10. Klik tautan reset di dalam email
11. Verifikasi tautan membuka Setup New Password dengan Subtitle "Set a new password to log in for budisantoso+{runId}-007a@qwertysystem.net."

### TC-AUTH-RST-145: Isi email reset sesuai template email Password Reset

12. Buka halaman Reset Password (Request) di jendela privat baru
13. Catat jumlah email di mail-catcher untuk `kartikawati+{runId}-007b@qwertysystem.net` sebagai baseline
14. Ketik `kartikawati+{runId}-007b@qwertysystem.net` pada field Email
15. Selesaikan reCAPTCHA (centang "I'm not a robot")
16. Klik Button [Reset Password]
17. Verifikasi jumlah email di mail-catcher untuk `kartikawati+{runId}-007b@qwertysystem.net` bertambah 1 dibanding baseline
18. Buka email yang masuk di mail-catcher untuk `kartikawati+{runId}-007b@qwertysystem.net`
19. Verifikasi Subject: "Reset your TAG Samurai password"
20. Verifikasi sapaan: "Hi Kartika Wati,"
21. Verifikasi paragraf pembuka: "We received a request to reset your password. Click the button below to set a new password."
22. Verifikasi Button berlabel "Confirm Email"
23. Verifikasi teks: "This link is valid for 24 hours and can only be used once."
24. Verifikasi teks: "If the button doesn't work, click the link below or copy and paste it into your browser:"
25. Verifikasi tautan mentah yang mengikuti teks itu sama dengan tautan pada button "Confirm Email"
26. Verifikasi teks: "To keep your data secure, please don't forward this email to anyone. If you didn't request this, you can safely ignore this email — your password will not be changed."
27. Verifikasi penutup: "— TAG Samurai"
28. Klik tombol [Confirm Email] pada Body email
29. Verifikasi browser membuka Setup New Password dengan Subtitle "Set a new password to log in for kartikawati+{runId}-007b@qwertysystem.net."

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`. Copy email mengikuti `foundation/product/business-rules/email-format.md` §5.2 dan §5.3 (label tombol "Confirm Email" memang dipertahankan di sana).
- Asersi tambahan di luar TC-AUTH-RST-145 tidak ada selain pertambahan jumlah email terhadap baseline (S-12). Isi email tidak dicakup di spec lain; spec lain hanya mengasersi keberadaan email dan tautan.
- Langkah membuka jendela privat baru (awal TC-AUTH-RST-118 dan TC-AUTH-RST-145), membuka email di mail-catcher, dan mengklik tautan atau tombol di email adalah langkah penghubung (S-03). Pencatatan baseline jumlah email sebelum klik [Reset Password] adalah langkah penghubung (S-12, S-03).
- TC-AUTH-RST-118 di TC sumber tidak punya dependensi; user dipisah dari TC-AUTH-RST-145 karena cooldown per email.
- Temuan untuk QA: Post Condition TC-AUTH-RST-145 (satu token reset aktif untuk `kartikawati+{runId}-007b@qwertysystem.net`; token belum dikonsumsi) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15). TC-AUTH-RST-118 tidak punya Post Condition (kolom bernilai `-`).
