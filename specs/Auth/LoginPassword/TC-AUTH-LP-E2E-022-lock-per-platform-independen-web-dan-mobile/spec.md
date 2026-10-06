---
id: TC-AUTH-LP-E2E-022-lock-per-platform-independen-web-dan-mobile
title: Independensi lock akun antara platform web dan aplikasi mobile
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-64
  - TC-AUTH-LP-65
coverage:
  web: automated
  mobile: automated
---

# Independensi lock akun antara platform web dan aplikasi mobile

## Prerequisites

- Pengujian memerlukan akses ke dua platform pengujian:
  - Platform Web: Browser web diarahkan ke URL `/login`.
  - Platform Mobile: Aplikasi native TAG Samurai Mobile (Android / iOS) terbuka di emulator / perangkat uji.
- User `mayaanggraini@qwertysystem.net` berstatus Activated dan Active dengan password `QaLogin#2026`.
- Tidak ada gate Agreement maupun MFA pada user ini di kedua platform.

## Test Steps

### User terkunci di web tetap dapat login di aplikasi mobile

1. Pada Platform Web: Buka halaman Login with Password
2. Masukkan email `mayaanggraini@qwertysystem.net` dan password salah `SalahPass#1` sebanyak 3 kali berturut-turut dengan menyelesaikan reCAPTCHA pada setiap submit
3. Verifikasi pada percobaan ke-3 Alert Danger menampilkan pesan bahwa akun terkunci selama 15 menit di web
4. Pada Platform Mobile: Buka layar Login with Password aplikasi TAG Samurai Mobile
5. Masukkan email `mayaanggraini@qwertysystem.net` dan password benar `QaLogin#2026`
6. Ketuk tombol [Log in]
7. Verifikasi login berhasil di aplikasi mobile dan aplikasi langsung menuju Portal — Product Hub
8. Verifikasi caption atau alert lock tidak muncul di mobile, membuktikan lock web tidak mengunci platform mobile

### User terkunci di mobile tetap dapat login di platform web

9. Lakukan logout dari aplikasi mobile dan kembali ke layar Login with Password mobile
10. Lakukan submit password salah sebanyak 3 kali berturut-turut pada aplikasi mobile hingga akun terkunci 15 menit di platform mobile
11. Verifikasi notifikasi / alert lock 15 menit tampil di layar mobile
12. Pada Platform Web: Buka halaman Login with Password (pastikan masa lock web sebelumnya sudah kedaluwarsa atau reset lewat hook)
13. Masukkan email `mayaanggraini@qwertysystem.net` dan password benar `QaLogin#2026`
14. Selesaikan reCAPTCHA lalu klik tombol [Log in]
15. Verifikasi login berhasil di web dan browser menuju Portal — Product Hub
16. Verifikasi pesan lock tidak muncul di web, membuktikan lock mobile tidak mengunci platform web

## Notes

- Sesuai PRD §9.2 F-AUTHLP-03 dan §11, progression lock dan penghitungan counter kegagalan dipisah per user × platform × hari kalender (`AUTHLP-LOGIC-02a`).
