---
id: TC-AUTH-LP-E2E-009-pemulihan-lock-via-reset-password-dan-login-sukses
title: Pemulihan lock via Reset Password dan reset counter oleh login berhasil
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-61
  - TC-AUTH-LP-62
  - TC-AUTH-LP-63
  - TC-AUTH-LP-66
  - TC-AUTH-LP-67
  - TC-AUTH-LP-68
  - TC-AUTH-LP-152
coverage:
  web: automated
---

# Pemulihan lock via Reset Password dan reset counter oleh login berhasil

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `doniprasetyo@qwertysystem.net` berstatus Requires Reset.
- User `putraanugrah@qwertysystem.net` baru menyelesaikan alur Reset Password dari status Requires Reset.
- User `panjikusuma@qwertysystem.net` baru menyelesaikan alur Reset Password dari status Permanent.
- User `kevinhartanto@qwertysystem.net` berstatus aktif dengan hitungan gagal 0.
- User `lestariwulan@qwertysystem.net` berstatus aktif dengan hitungan gagal 0.
- User `zainalabidin@qwertysystem.net` berstatus aktif dengan hitungan gagal 0.
- User `salmanfarisi@qwertysystem.net` berstatus aktif dan memicu layar Confirm to Continue.

## Test Steps

### Pemulihan Requires Reset via alur Reset Password

1. Buka halaman Login with Password di browser web
2. Masukkan email `doniprasetyo@qwertysystem.net` dengan password lama `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik [Log in]
3. Verifikasi Alert Danger "Please reset your password" tampil
4. Klik tautan [Reset password] pada Alert Danger
5. Selesaikan proses reset password menggunakan token valid dan password baru `NewPass#2026`
6. Kembali ke halaman Login with Password
7. Masukkan email `doniprasetyo@qwertysystem.net` dan password baru `NewPass#2026`
8. Selesaikan reCAPTCHA lalu klik tombol [Log in]
9. Verifikasi login berhasil dan browser langsung menuju Portal — Product Hub

### Reset counter kegagalan dan rantai hari pasca-Reset Password

10. Buka kembali halaman Login with Password
11. Masukkan email `putraanugrah@qwertysystem.net` (yang baru reset password) dengan password salah `SalahPass#1`
12. Selesaikan reCAPTCHA lalu klik [Log in] (salah ke-1)
13. Verifikasi Alert Danger "Incorrect email or password" tampil
14. Ulangi submit password salah ke-2 dan ke-3
15. Verifikasi pada salah ke-3, akun terkunci 15 menit (bukan Requires Reset), membuktikan counter harian kembali ke 0
16. Masukkan email `panjikusuma@qwertysystem.net` (yang baru reset dari status Permanent) dengan password salah `SalahPass#1`
17. Selesaikan reCAPTCHA lalu klik [Log in]
18. Verifikasi Alert Danger "Incorrect email or password" tampil biasa dan Alert Permanent tidak tampil, membuktikan rantai hari berturut-turut dikosongkan

### Submit Password kosong dan tanpa reCAPTCHA tidak menambah counter gagal

19. Masukkan email `kevinhartanto@qwertysystem.net` dengan password salah `SalahPass#1` sebanyak dua kali berturut-turut
20. Verifikasi pada kedua submit Alert Danger "Incorrect email or password" tampil
21. Kosongkan field Password, selesaikan reCAPTCHA, lalu klik [Log in]
22. Verifikasi caption inline "Password must not be empty" tampil dan akun belum terkunci
23. Masukkan password salah `SalahPass#1` untuk ketiga kalinya, selesaikan reCAPTCHA, lalu klik [Log in]
24. Verifikasi akun baru terkunci 15 menit pada percobaan ini, membuktikan submit password kosong tidak dihitung
25. Uji skenario serupa pada user `lestariwulan@qwertysystem.net` dengan menyisipkan submit tanpa reCAPTCHA
26. Verifikasi submit tanpa reCAPTCHA tidak dihitung ke akumulasi gagal

### Login berhasil mengatur ulang hitungan gagal hari itu

27. Masukkan email `zainalabidin@qwertysystem.net` dengan password salah `SalahPass#1` sebanyak dua kali (gagal 1 dan 2)
28. Pada percobaan ke-3, masukkan password benar `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik [Log in]
29. Verifikasi login berhasil dan browser menuju Portal — Product Hub
30. Lakukan logout dan kembali ke halaman Login with Password
31. Masukkan email `zainalabidin@qwertysystem.net` dengan password salah `SalahPass#1` sebanyak dua kali
32. Verifikasi Alert Danger "Incorrect email or password" tampil biasa dan akun TIDAK terkunci 15 menit pada percobaan ke-1 atau ke-2 setelah login sukses

### Password benar yang berujung layar Confirm to Continue mengatur ulang counter

33. Masukkan email `salmanfarisi@qwertysystem.net` dengan password salah `SalahPass#1` sebanyak dua kali
34. Masukkan password benar `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik [Log in]
35. Verifikasi layar Confirm to Continue tampil
36. Tutup tab tanpa mengklik Continue, lalu buka halaman Login with Password di tab baru
37. Masukkan kembali email `salmanfarisi@qwertysystem.net` dengan password salah `SalahPass#1` sebanyak dua kali
38. Verifikasi akun tidak terkunci pada percobaan salah ke-1 dan ke-2, membuktikan password benar telah me-reset counter gagal meskipun Agreement belum disetujui

## Notes

- Reset Password sukses mereset seluruh counter failed attempt, lock level, dan riwayat consecutive days (`AUTHLP-LOGIC-02f`).
- Login berhasil mengatur ulang counter harian ke 0 (`NC-12`, TC-AUTH-LP-68, TC-AUTH-LP-152).
