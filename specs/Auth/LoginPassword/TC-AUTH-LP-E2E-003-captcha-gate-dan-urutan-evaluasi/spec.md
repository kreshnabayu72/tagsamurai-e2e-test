---
id: TC-AUTH-LP-E2E-003-captcha-gate-dan-urutan-evaluasi
title: Evaluasi Google reCAPTCHA v2 dan urutan validasi
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-24
  - TC-AUTH-LP-25
  - TC-AUTH-LP-26
coverage:
  web: automated
---

# Evaluasi Google reCAPTCHA v2 dan urutan validasi

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `jokosusilo@qwertysystem.net` berstatus Activated dan Active dengan hitungan gagal 0.
- Mode: mock untuk simulasi token reCAPTCHA expired.

## Test Steps

### Submit tanpa menyelesaikan widget reCAPTCHA

1. Buka halaman Login with Password di browser web
2. Masukkan email `jokosusilo@qwertysystem.net` pada field Email
3. Masukkan password `QaLogin#2026` pada field Password
4. Biarkan widget reCAPTCHA dalam keadaan Unsolved
5. Klik tombol [Log in]
6. Verifikasi caption "Please verify that you are not a robot" tampil tepat di bawah widget reCAPTCHA
7. Verifikasi widget reCAPTCHA tetap berstatus Unsolved
8. Verifikasi tidak ada sesi yang terbentuk dan browser tetap berada di halaman Login

### Urutan evaluasi Password kosong mendahului reCAPTCHA

9. Kosongkan field Password
10. Biarkan widget reCAPTCHA tetap Unsolved
11. Klik tombol [Log in]
12. Verifikasi caption inline "Password must not be empty" tampil di bawah field Password
13. Verifikasi caption "Please verify that you are not a robot" tidak tampil di bawah widget reCAPTCHA, membuktikan validasi Password kosong dievaluasi lebih dulu daripada reCAPTCHA

### Token reCAPTCHA kedaluwarsa

14. Masukkan kembali password `QaLogin#2026`
15. Selesaikan reCAPTCHA hingga tercentang
16. Simulasikan token reCAPTCHA kedaluwarsa (expired timeout dari library reCAPTCHA)
17. Klik tombol [Log in]
18. Verifikasi caption "Please verify that you are not a robot" tampil tepat di bawah widget reCAPTCHA
19. Verifikasi widget reCAPTCHA kembali ke status Unsolved

## Notes

- Sesuai NC-02, evaluasi Password kosong dilakukan sebelum reCAPTCHA.
- Uji bypass server-side (Defense-in-Depth) dan outage penyedia reCAPTCHA dipecah ke spec tersendiri E2E-025 (lihat `gap-spec/gap-spec.md` GAP-LP-E2E-009).
