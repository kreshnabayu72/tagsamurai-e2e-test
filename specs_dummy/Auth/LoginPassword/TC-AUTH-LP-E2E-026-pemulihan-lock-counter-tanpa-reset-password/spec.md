---
id: TC-AUTH-LP-E2E-026-pemulihan-lock-counter-tanpa-reset-password
title: Pemulihan lock counter oleh login berhasil tanpa Reset Password
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-66
  - TC-AUTH-LP-67
  - TC-AUTH-LP-68
  - TC-AUTH-LP-152
  - TC-AUTH-LP-163
coverage:
  web: automated
---

# Pemulihan lock counter oleh login berhasil tanpa Reset Password

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `kevinhartanto@qwertysystem.net` berstatus aktif dengan hitungan gagal 0.
- User `lestariwulan@qwertysystem.net` berstatus aktif dengan hitungan gagal 0.
- User `zainalabidin@qwertysystem.net` berstatus aktif dengan hitungan gagal 0.
- User `salmanfarisi@qwertysystem.net` berstatus aktif dan memicu layar Confirm to Continue.
- Kemampuan memajukan waktu server uji lewat fixture BE untuk melewati lock 15 menit dan 1 jam pada hari kalender yang sama.

## Test Steps

### Submit Password kosong dan tanpa reCAPTCHA tidak menambah counter gagal

1. Buka halaman Login with Password di browser web
2. Masukkan email `kevinhartanto@qwertysystem.net` dengan password salah `SalahPass#1` sebanyak dua kali berturut-turut
3. Verifikasi pada kedua submit Alert Danger "Incorrect email or password" tampil
4. Kosongkan field Password, selesaikan reCAPTCHA, lalu klik [Log in]
5. Verifikasi caption inline "Password must not be empty" tampil dan akun belum terkunci
6. Masukkan password salah `SalahPass#1` untuk ketiga kalinya, selesaikan reCAPTCHA, lalu klik [Log in]
7. Verifikasi akun baru terkunci 15 menit pada percobaan ini, membuktikan submit password kosong tidak dihitung
8. Uji skenario serupa pada user `lestariwulan@qwertysystem.net` dengan menyisipkan submit tanpa reCAPTCHA
9. Verifikasi submit tanpa reCAPTCHA tidak dihitung ke akumulasi gagal

### Login berhasil mengatur ulang hitungan gagal hari itu

10. Masukkan email `zainalabidin@qwertysystem.net` dengan password salah `SalahPass#1` sebanyak dua kali (gagal 1 dan 2)
11. Pada percobaan ke-3, masukkan password benar `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik [Log in]
12. Verifikasi login berhasil dan browser menuju Portal — Product Hub
13. Lakukan logout dan kembali ke halaman Login with Password
14. Masukkan email `zainalabidin@qwertysystem.net` dengan password salah `SalahPass#1` sebanyak dua kali
15. Verifikasi Alert Danger "Incorrect email or password" tampil biasa dan akun TIDAK terkunci 15 menit pada percobaan ke-1 atau ke-2 setelah login sukses

### Password benar yang berujung layar Confirm to Continue mengatur ulang counter

16. Masukkan email `salmanfarisi@qwertysystem.net` dengan password salah `SalahPass#1` sebanyak dua kali
17. Masukkan password benar `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik [Log in]
18. Verifikasi layar Confirm to Continue tampil
19. Tutup tab tanpa mengklik Continue, lalu buka halaman Login with Password di tab baru
20. Masukkan kembali email `salmanfarisi@qwertysystem.net` dengan password salah `SalahPass#1` sebanyak dua kali
21. Verifikasi akun tidak terkunci pada percobaan salah ke-1 dan ke-2, membuktikan password benar telah me-reset counter gagal meskipun Agreement belum disetujui

### Password benar setelah tahap 1 jam lewat mereset data lock harian tanpa mengubah hitungan hari

22. Majukan waktu server uji dan/atau reset fixture sehingga tahap lock 15 menit sebelumnya telah berakhir dan hitungan gagal `zainalabidin@qwertysystem.net` kembali ke 0 (precondition `TC-AUTH-LP-163`)
23. Masukkan password salah `SalahPass#1` tiga kali berturut-turut (selesaikan reCAPTCHA pada setiap submit) lalu verifikasi Alert Danger lock 15 menit tampil pada salah ke-3
24. Majukan waktu server uji hingga lock 15 menit berakhir
25. Masukkan password salah `SalahPass#1` tiga kali lagi (percobaan ke-4 s/d ke-6) lalu verifikasi Alert Danger lock 1 jam tampil pada percobaan ke-6
26. Majukan waktu server uji hingga lock 1 jam berakhir, masih pada hari kalender yang sama
27. Masukkan password benar `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik [Log in]
28. Verifikasi login berhasil dan browser menuju Portal — Product Hub
29. Lakukan logout lalu buka kembali halaman Login with Password
30. Masukkan password salah `SalahPass#1` tiga kali berturut-turut (salah baru ke-1 s/d ke-3)
31. Verifikasi salah baru ke-1 dan ke-2 menampilkan Alert Danger "Incorrect email or password" biasa, lalu pada salah baru ke-3 Alert Danger lock 15 menit tampil (bukan lock 1 jam atau Requires Reset), membuktikan tahap lock harian di-reset oleh password benar di langkah 28
32. Verifikasi lewat data lock fixture BE: hitungan hari berturut-turut tetap 1 (tahap 1 jam hari itu dihitung sekali per hari kalender dan tidak menjadi 2) serta status akun tetap bukan Requires Reset/Permanent

## Notes

- Login berhasil mengatur ulang counter harian ke 0; password benar pada hari lock juga mereset hitungan gagal dan tahap lock harian, tetapi hitungan hari berturut-turut dan tahap lintas hari TIDAK ikut di-reset — keduanya hanya ter-reset oleh Reset Password (`AUTHLP-LOGIC-02l`, `TC-AUTH-LP-68`, `TC-AUTH-LP-152`, `TC-AUTH-LP-163`).
- Submit password kosong dan tanpa reCAPTCHA tidak dihitung ke akumulasi gagal (`TC-AUTH-LP-66`, `TC-AUTH-LP-67`).
- Spec ini dipecah dari E2E-009 agar alur pemulihan via modul Reset Password (berat, lintas modul) terpisah dari semantik reset counter oleh login berhasil (lihat `gap-spec/gap-spec.md` GAP-LP-E2E-009).