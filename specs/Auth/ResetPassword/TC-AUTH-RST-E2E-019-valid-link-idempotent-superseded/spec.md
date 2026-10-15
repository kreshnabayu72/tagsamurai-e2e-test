---
id: TC-AUTH-RST-E2E-019-valid-link-idempotent-superseded
title: "Tautan Valid Idempotent dan Penggantian Token oleh Request Baru"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-54
  - TC-AUTH-RST-57
coverage:
  web: automated
---

# Tautan Valid Idempotent dan Penggantian Token oleh Request Baru

## Prerequisites

- Mode: FE+BE.
- Seeding: dua user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`. Token reset aktif milik TC-AUTH-RST-54 (user `budisantoso+{runId}-019a`) dan token A milik TC-AUTH-RST-57 (user `citradewi+{runId}-019b`, email 1) diterbitkan di hook `before` lewat API Request (tautan diambil dari mail-catcher). User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: mail-catcher (dua email berurutan dan tautan masing-masing); reCAPTCHA mode uji; jendela privat tanpa sesi login; pengatur jam server uji dan jam browser/perangkat (digeser bersama 61 detik supaya Request pertama TC-AUTH-RST-57 sudah lebih dari 60 detik lalu).
- State global yang diubah: jam server uji dan jam browser/perangkat. Suite berjalan serial (`parallel: false`). Pemulihan: keduanya dikembalikan ke waktu nyata di hook `after` (tetap berjalan walau spec gagal di tengah).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-54, TC-AUTH-RST-57: User belum login (guest); browser web.
- TC-AUTH-RST-54: User `Budi Santoso` (`budisantoso+{runId}-019a@qwertysystem.net`) Active dengan token reset aktif; password aktif `Spectra.env.RST_PASSWORD`.
- TC-AUTH-RST-57: User `Citra Dewi` (`citradewi+{runId}-019b@qwertysystem.net`) Active dengan token A aktif dari Request pertama di hook `before` (tautan A di email 1).

## Test Steps

### TC-AUTH-RST-54: Membuka tautan valid berulang kali merender Setup New Password

1. Buka jendela privat baru lalu buka tautan reset milik `budisantoso+{runId}-019a@qwertysystem.net` dari mail-catcher
2. Verifikasi Setup New Password tampil dengan Subtitle "Set a new password to log in for budisantoso+{runId}-019a@qwertysystem.net."
3. Tutup halaman lalu buka tautan yang sama sekali lagi
4. Verifikasi Setup New Password tampil dengan Subtitle "Set a new password to log in for budisantoso+{runId}-019a@qwertysystem.net."

### TC-AUTH-RST-57: Request baru meng-invalidate token sebelumnya

5. Majukan jam server dan jam browser 61 detik sehingga Request pertama untuk `citradewi+{runId}-019b@qwertysystem.net` (token A, email 1) sudah lebih dari 60 detik lalu
6. Buka halaman Reset Password (Request) di jendela privat baru
7. Ketik `citradewi+{runId}-019b@qwertysystem.net` pada field Email
8. Selesaikan reCAPTCHA (centang "I'm not a robot")
9. Klik Button [Reset Password]
10. Buka tautan token A dari email 1
11. Verifikasi Halaman 404 tampil dengan Title "Reset Link Expired"
12. Verifikasi Halaman 404 tampil dengan Message "This password reset link has expired. Reset links are valid for 24 hours."
13. Buka tautan token B dari email 2
14. Verifikasi Setup New Password tampil dengan Subtitle "Set a new password to log in for citradewi+{runId}-019b@qwertysystem.net."

## Notes

- Mode: FE+BE. Sumber: `auth/reset-password/TestCases/tc-reset-password.md`.
- Asersi "tidak ada entri log baru" TC-AUTH-RST-54 (Expected butir b) diasersi di spec `TC-AUTH-RST-E2E-043-absence-not-logged` lewat aksi nyata (membuka tautan valid dua kali) dengan baseline log sendiri; TC-AUTH-RST-54 tetap di `sourceTc` spec ini dan rujukannya dicatat di Notes kedua spec (S-05). "Token tetap active" tidak diasersi di spec ini (tidak ada langkah observasi token di TC).
- TC-AUTH-RST-57 menyiapkan Request pertama (token A) lewat seeding API di hook `before` dan memajukan jam server dan jam browser 61 detik pada langkah 5 supaya Request di langkah 9 bukan no-op cooldown; TC sumber bergantung pada TC-AUTH-RST-12.
- Langkah penghubung (S-03): membuka jendela privat baru (langkah 1 dan 6) bukan asersi TC.
- Temuan untuk QA: Post Condition TC-AUTH-RST-57 butir b ("Hanya satu token berstatus active untuk user (token B)") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
