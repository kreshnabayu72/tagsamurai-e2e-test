---
id: TC-AUTH-LP-E2E-007-lock-progression-tahap-1-jam-dan-requires-reset
title: Lock progression tahap 1 jam, status Requires Reset, dan defense-in-depth
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-44
  - TC-AUTH-LP-45
  - TC-AUTH-LP-46
  - TC-AUTH-LP-47
  - TC-AUTH-LP-48
  - TC-AUTH-LP-49
  - TC-AUTH-LP-50
  - TC-AUTH-LP-51
  - TC-AUTH-LP-52
  - TC-AUTH-LP-140
coverage:
  web: automated
---

# Lock progression tahap 1 jam, status Requires Reset, dan defense-in-depth

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `rinaputri@qwertysystem.net` telah menyelesaikan tahap lock 15 menit (counter gagal = 3) dan waktu lock 15 menit telah berakhir.
- Pengaturan General Settings entitas: Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` dan Time Format `HH:mm`.
- Kemampuan penyesuaian waktu server uji untuk melewati batas waktu lock 1 jam.

## Test Steps

### Kegagalan ke-4 dan ke-5 (Window 2)

1. Buka halaman Login with Password di browser web
2. Masukkan email `rinaputri@qwertysystem.net` dan password salah `SalahPass#1`
3. Selesaikan reCAPTCHA lalu klik [Log in] (percobaan ke-4)
4. Verifikasi Alert Danger "Incorrect email or password" tampil di atas tombol [Log in] dan tidak mengunci akun
5. Masukkan kembali password salah `SalahPass#1`, selesaikan reCAPTCHA, lalu klik [Log in] (percobaan ke-5)
6. Verifikasi Alert Danger "Incorrect email or password" tetap tampil dan belum memicu lock

### Kegagalan ke-6 memicu Lock 1 Jam

7. Masukkan kembali password salah `SalahPass#1`, selesaikan reCAPTCHA, lalu klik [Log in] (percobaan ke-6)
8. Verifikasi Alert Danger di atas tombol [Log in] menampilkan pesan: "Too many failed login attempts. Your account is locked for 1 hour. You can try again at {time}."
9. Verifikasi nilai `{time}` menunjukkan jam berakhirnya lock (tepat 1 jam setelah kegagalan ke-6)
10. Verifikasi tautan [Reset password] tidak tampil di dalam Alert Danger
11. Verifikasi field Email, Password, dan tombol [Log in] tetap enabled
12. Masukkan password yang benar `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik [Log in]
13. Verifikasi login tetap ditolak dengan pesan lock 1 jam yang sama dan nilai `{time}` tidak bertambah

### Defense-in-Depth: Bypass request langsung saat lock aktif ditolak server

14. Aktifkan intersepsi jaringan pada browser
15. Kirim request HTTP POST login secara langsung dengan kredensial benar `QaLogin#2026` saat lock 1 jam masih aktif
16. Verifikasi backend merespons HTTP 200 dengan `outcome: locked` dan `error_code: LOCKED_1H` (penolakan lock tidak menggunakan status 4xx; `openapi.yaml` `/auth/login`)
17. Buka URL Portal — Product Hub secara manual dan verifikasi browser ditolak kembali ke halaman Login

### Kegagalan ke-7 dan ke-8 (Window 3)

18. Sesuaikan waktu server uji melewati batas waktu lock 1 jam berakhir
19. Muat ulang halaman login
20. Masukkan email `rinaputri@qwertysystem.net` dan password salah `SalahPass#1`, selesaikan reCAPTCHA, lalu klik [Log in] (percobaan ke-7)
21. Verifikasi Alert Danger "Incorrect email or password" tampil di atas tombol [Log in]
22. Masukkan kembali password salah `SalahPass#1`, selesaikan reCAPTCHA, lalu klik [Log in] (percobaan ke-8)
23. Verifikasi Alert Danger "Incorrect email or password" tampil dan belum memicu status Requires Reset

### Kegagalan ke-9 memicu status Requires Reset

24. Masukkan kembali password salah `SalahPass#1`, selesaikan reCAPTCHA, lalu klik [Log in] (percobaan ke-9)
25. Verifikasi Alert Danger di atas tombol [Log in] menampilkan pesan: "Please reset your password"
26. Verifikasi tautan [Reset password] tampil tepat satu baris di bawah teks Alert
27. Verifikasi field Email, Password, dan tombol [Log in] tetap enabled
28. Masukkan password benar `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik tombol [Log in]
29. Verifikasi login tetap ditolak dengan pesan "Please reset your password" beserta tautan [Reset password]

### Navigasi via tautan [Reset password] pada Alert

30. Klik tautan [Reset password] yang berada di bawah teks Alert Danger
31. Verifikasi browser membuka halaman Reset Password
32. Verifikasi field Email pada halaman Reset Password otomatis terisi dengan `rinaputri@qwertysystem.net`

## Notes

- Progression lock pada hari yang sama mengikuti siklus: 3x gagal = lock 15m; 6x gagal = lock 1 jam; 9x gagal = Requires Reset (`AUTHLP-LOGIC-02a`, `02b`, `02c`).
- Status Requires Reset mengunci akun secara permanen pada hari tersebut sampai user berhasil melakukan reset password melalui modul Reset Password (`AUTHLP-LOGIC-02f`).
