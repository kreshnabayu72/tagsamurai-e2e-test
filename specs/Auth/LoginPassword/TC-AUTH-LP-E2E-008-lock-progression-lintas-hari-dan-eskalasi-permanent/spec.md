---
id: TC-AUTH-LP-E2E-008-lock-progression-lintas-hari-dan-eskalasi-permanent
title: Lock progression lintas hari dan eskalasi 7 hari berturut-turut menjadi Permanent
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-53
  - TC-AUTH-LP-54
  - TC-AUTH-LP-55
  - TC-AUTH-LP-56
  - TC-AUTH-LP-57
  - TC-AUTH-LP-58
  - TC-AUTH-LP-59
  - TC-AUTH-LP-60
coverage:
  web: automated
---

# Lock progression lintas hari dan eskalasi 7 hari berturut-turut menjadi Permanent

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `hendrawijaya@qwertysystem.net` pernah lock 15m kemarin (hari kalender sebelumnya).
- User `lindasari@qwertysystem.net` pernah lock 1 jam kemarin (hari kalender sebelumnya).
- User `miralestari@qwertysystem.net` terkunci pada pukul 23:55 dan jam server melewati tengah malam ke 00:05.
- User `candrabayu@qwertysystem.net` memiliki riwayat lock 1 jam selama 6 hari berturut-turut, namun pada hari ke-7 hanya mencapai lock 15 menit.
- User `ekasurya@qwertysystem.net` memiliki riwayat lock 1 jam selama 7 hari berturut-turut (`consecutive_1h_days=7`).
- Kontrol jam server uji / manipulasi timestamp database melalui hook atau API automation.

## Test Steps

### Reset harian setelah lock 15 menit dan 1 jam

1. Buka halaman Login with Password di browser web
2. Masukkan email `hendrawijaya@qwertysystem.net` dan password salah `SalahPass#1`, selesaikan reCAPTCHA, lalu klik [Log in] (percobaan salah ke-1 hari ini)
3. Verifikasi Alert Danger "Incorrect email or password" tampil di atas tombol [Log in]
4. Ulangi percobaan salah ke-2 dan verifikasi Alert Danger "Incorrect email or password" tetap tampil
5. Masukkan percobaan salah ke-3
6. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil, membuktikan hitungan harian diatur ulang ke tahap awal (15m, bukan 1 jam)
7. Masukkan email `lindasari@qwertysystem.net` dan lakukan percobaan salah sebanyak 3 kali
8. Verifikasi pada percobaan salah ke-3, akun terkunci 15 menit (kembali ke tahap 1), membuktikan lock 1 jam kemarin tidak melanjutkan counter hari berikutnya

### Lock aktif tetap berlaku melewati tengah malam

9. Masukkan email `miralestari@qwertysystem.net` yang terkunci pukul 23:55 dengan waktu server di pukul 00:05
10. Masukkan password benar `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik [Log in]
11. Verifikasi login tetap ditolak dengan pesan Alert Danger lock 15 menit aktif
12. Majukan jam server uji hingga pukul 00:11 (lock kedaluwarsa)
13. Masukkan password salah `SalahPass#1`, selesaikan reCAPTCHA, lalu klik [Log in]
14. Verifikasi Alert Danger "Incorrect email or password" tampil (hitungan hari baru dimulai dari percobaan ke-1)

### Status Requires Reset tidak direset oleh pergantian hari

15. Ambil akun yang berstatus Requires Reset dari hari sebelumnya
16. Masukkan email akun tersebut dengan password benar `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik [Log in]
17. Verifikasi login tetap ditolak dengan pesan "Please reset your password" beserta tautan [Reset password], membuktikan status Requires Reset tidak gugur karena pergantian hari

### Rantai hari berturut-turut putus jika absen lock 1 jam

18. Masukkan email `candrabayu@qwertysystem.net` yang pada hari ke-7 hanya mencapai lock 15m
19. Masukkan password salah `SalahPass#1` pada hari ke-8, selesaikan reCAPTCHA, lalu klik [Log in]
20. Verifikasi Alert Danger "Incorrect email or password" tampil biasa dan akun TIDAK langsung berstatus Permanent, membuktikan rantai eskalasi telah terputus

### Eskalasi 7 hari berturut-turut lock 1 jam menjadi Permanent

21. Masukkan email `ekasurya@qwertysystem.net` yang telah memenuhi lock 1 jam selama 7 hari kalender berturut-turut
22. Pada hari ke-8, masukkan password salah `SalahPass#1` untuk pertama kali, selesaikan reCAPTCHA, lalu klik [Log in]
23. Verifikasi Alert Danger di atas tombol [Log in] menampilkan pesan: "For security reasons, your account has been locked. Please reset your password to regain access."
24. Verifikasi tautan [Reset password] tampil di bawah teks Alert Danger
25. Verifikasi pesan lock 15 menit maupun 1 jam tidak tampil
26. Masukkan password yang benar `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik tombol [Log in]
27. Verifikasi login tetap ditolak dengan pesan Alert Danger Permanent yang sama
28. Klik tautan [Reset password] pada Alert Danger
29. Verifikasi halaman Reset Password terbuka dengan field Email terisi `ekasurya@qwertysystem.net`

## Notes

- Pergantian hari kalender mengikuti Time Zone General Settings entitas (`AUTHLP-LOGIC-02g`).
- Lock yang aktif melewati tengah malam tetap harus diselesaikan durasinya (`AUTHLP-LOGIC-02h`).
- Hanya kegagalan mencapai tahap 1 jam yang dihitung ke akumulasi hari berturut-turut (`AUTHLP-LOGIC-02d`, `02i`).
