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
  - TC-AUTH-LP-100
  - TC-AUTH-LP-139
coverage:
  web: automated
---

# Evaluasi Google reCAPTCHA v2 dan urutan validasi

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `jokosusilo@qwertysystem.net` berstatus Activated dan Active dengan hitungan gagal 0.
- Mode: mock untuk simulasi token reCAPTCHA expired, network intercept bypass token, dan error outage server penyedia reCAPTCHA.

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

### Bypass submit tanpa token reCAPTCHA ditolak oleh server (Defense-in-Depth)

20. Aktifkan intersepsi jaringan pada endpoint login
21. Buat request login dengan membuang field token reCAPTCHA dari payload HTTP POST
22. Teruskan request ke backend
23. Verifikasi respons backend menolak request dengan status penolakan autentikasi
24. Verifikasi caption "Please verify that you are not a robot" tetap tampil di UI dan tidak ada sesi yang dibuat

### Penanganan outage penyedia reCAPTCHA

25. Simulasikan layanan verifikasi Google reCAPTCHA tidak dapat dihubungi oleh backend (503 Service Unavailable / Network Failure)
26. Selesaikan reCAPTCHA di UI lalu klik tombol [Log in]
27. Verifikasi toast error "Error, failed to log in." tampil di layar
28. Verifikasi login tidak berhasil dan user tidak dialihkan ke Portal

## Notes

- Sesuai NC-02, evaluasi Password kosong dilakukan sebelum reCAPTCHA.
- Penolakan reCAPTCHA kosong di sisi backend diverifikasi melalui skenario Defense-in-Depth (TC-AUTH-LP-139).
- Kegagalan server penyedia reCAPTCHA dimodelkan sebagai kegagalan sistem internal dengan toast generik (TC-AUTH-LP-100).
