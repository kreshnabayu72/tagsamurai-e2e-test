---
id: TC-AUTH-LP-E2E-017-pencatatan-audit-log-kegagalan-dan-kondisi-tidak-dicatat
title: Pencatatan kegagalan login di kedua surface log
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-105
  - TC-AUTH-LP-106
  - TC-AUTH-LP-107
  - TC-AUTH-LP-108
  - TC-AUTH-LP-109
  - TC-AUTH-LP-110
  - TC-AUTH-LP-111
  - TC-AUTH-LP-112
  - TC-AUTH-LP-113
  - TC-AUTH-LP-114
coverage:
  web: automated
---

# Pencatatan kegagalan login di kedua surface log

## Prerequisites

- Pengujian memerlukan dua sesi browser:
  - Sesi 1: Form Login with Password untuk submit skenario uji.
  - Sesi 2: Administrator Total Control (Global Settings) yang memantau `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`.
- User subjek terdaftar: `jokosusilo@qwertysystem.net`, `dewilestari@qwertysystem.net` (Pending), `agussetiawan@qwertysystem.net` (Inactive), `joniwidodo@qwertysystem.net` (gagal 1), `nuraini@qwertysystem.net` (lock 15m), `okapratama@qwertysystem.net` (lock 1h), `pritasari@qwertysystem.net` (requires reset), `qoriramadhan@qwertysystem.net` (permanent), `ratnadewi@qwertysystem.net` (consent not given).

## Test Steps

### Pencatatan kegagalan dengan Status Failed dan Note spesifik

1. Pada Sesi 1: Masukkan email `jokosusilo@qwertysystem.net`, kosongkan password, selesaikan reCAPTCHA, klik [Log in]
2. Pada Sesi 2: Verifikasi pada Activity Log > Session dan User Log tercatat 1 baris baru: Status `Failed`, Note `Empty password`
3. Pada Sesi 1: Masukkan email `jokosusilo@qwertysystem.net` dan password `QaLogin#2026` tanpa menyelesaikan reCAPTCHA, klik [Log in]
4. Pada Sesi 2: Verifikasi tercatat 1 baris baru: Status `Failed`, Note `Captcha not completed`
5. Pada Sesi 1: Masukkan email `dewilestari@qwertysystem.net` (Pending Activation), selesaikan reCAPTCHA, klik [Log in]
6. Pada Sesi 2: Verifikasi tercatat 1 baris baru: Status `Failed`, Note `Account is not activated`
7. Pada Sesi 1: Masukkan email `agussetiawan@qwertysystem.net` (Inactive), selesaikan reCAPTCHA, klik [Log in]
8. Pada Sesi 2: Verifikasi tercatat 1 baris baru: Status `Failed`, Note `Account is inactive`
9. Pada Sesi 1: Masukkan email `joniwidodo@qwertysystem.net` dengan password salah `SalahPass#1`, selesaikan reCAPTCHA, klik [Log in]
10. Pada Sesi 2: Verifikasi tercatat 1 baris baru: Status `Failed`, Note `Incorrect password`
11. Pada Sesi 1: Lakukan kegagalan password ke-3 pada akun `nuraini@qwertysystem.net` hingga memicu lock 15 menit
12. Pada Sesi 2: Verifikasi tercatat tepat 1 baris baru: Status `Failed`, Note `Locked 15 minutes` (tidak ada baris redundan `Incorrect password`)
13. Pada Sesi 1: Lakukan kegagalan password ke-6 pada akun `okapratama@qwertysystem.net` hingga memicu lock 1 jam
14. Pada Sesi 2: Verifikasi tercatat tepat 1 baris baru: Status `Failed`, Note `Locked 1 hour`
15. Pada Sesi 1: Lakukan kegagalan password ke-9 pada akun `pritasari@qwertysystem.net` hingga memicu Requires Reset
16. Pada Sesi 2: Verifikasi tercatat tepat 1 baris baru: Status `Failed`, Note `Locked requires reset`
17. Pada Sesi 1: Pada akun `qoriramadhan@qwertysystem.net` yang telah memenuhi eskalasi 7 hari, submit password salah di hari ke-8
18. Pada Sesi 2: Verifikasi tercatat tepat 1 baris baru: Status `Failed`, Note `Account locked`
19. Pada Sesi 1: Login menggunakan `ratnadewi@qwertysystem.net` sampai layar Confirm to Continue tampil, lalu klik [Continue ➔] tanpa mencentang checkbox
20. Pada Sesi 2: Verifikasi tercatat 1 baris baru: Status `Failed`, Note `Consent not given`

## Notes

- Aksi klik [Continue ➔] tanpa centang dicatat sebagai `Failed` dengan Note `Consent not given` (`NC-13`, TC-AUTH-LP-114).
- Verifikasi kondisi yang TIDAK dicatat pada kedua surface log (termasuk kondisi lock aktif, navigasi, perubahan versi policy, dan rate limit) dipecah ke spec tersendiri E2E-028 (lihat `gap-spec/gap-spec.md` GAP-LP-E2E-009).
