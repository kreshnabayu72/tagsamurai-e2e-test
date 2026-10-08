---
id: TC-AUTH-RST-E2E-020-pemulihan-account-lock
title: "Pemulihan status terkunci (15 menit, 1 jam, Requires Reset, dan Permanen) melalui Reset Password sukses"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-106
  - TC-AUTH-RST-107
  - TC-AUTH-RST-108
  - TC-AUTH-RST-109
  - TC-AUTH-RST-110
  - TC-AUTH-RST-116
  - TC-AUTH-RST-117
coverage:
  web: automated
---

# Pemulihan status terkunci (15 menit, 1 jam, Requires Reset, dan Permanen) melalui Reset Password sukses

## Prerequisites

- User belum login (guest); browser web berada di halaman `/login`.
- Environment uji terisolasi dengan akses mail-catcher.
- Akun uji terkonfigurasi pada berbagai tingkatan lock:
  - `agusprasetyo@qwertysystem.net` (terkunci 15 menit).
  - `rinawulandari@qwertysystem.net` (terkunci 1 jam).
  - `hendrawijaya@qwertysystem.net` (status Requires Reset akibat 9x gagal).
  - `yuniastuti@qwertysystem.net` (terkunci Permanen akibat eskalasi lock 1 jam selama 7 hari berturut-turut).

## Test Steps

### Pemulihan akun terkunci 15 menit

1. Coba login menggunakan `agusprasetyo@qwertysystem.net` di halaman Login
2. Verifikasi alert lock 15 menit tampil
3. Lakukan alur Reset Password penuh (Request -> mail-catcher -> Setup New Password) untuk akun Agus Prasetyo hingga sukses
4. Buka kembali halaman Login with Password
5. Masukkan email Agus Prasetyo dan password barunya
6. Selesaikan reCAPTCHA lalu klik tombol [Log in]
7. Verifikasi login langsung berhasil tanpa harus menunggu masa tunggu 15 menit berakhir

### Pemulihan akun terkunci 1 jam

8. Coba login menggunakan `rinawulandari@qwertysystem.net` di halaman Login
9. Verifikasi alert lock 1 jam tampil
10. Selesaikan alur Reset Password hingga sukses untuk Rina Wulandari
11. Buka halaman Login with Password lalu login menggunakan password baru Rina
12. Verifikasi login langsung berhasil tanpa menunggu 1 jam

### Pemulihan akun dengan status Requires Reset

13. Coba login menggunakan `hendrawijaya@qwertysystem.net`
14. Verifikasi alert "Your account is temporarily locked. Please [Reset password] to regain access." tampil
15. Klik tautan [Reset password] pada alert tersebut
16. Verifikasi browser berpindah ke halaman Reset Password dengan email Hendra terisi otomatis
17. Selesaikan alur Reset Password hingga sukses
18. Lakukan login menggunakan password baru Hendra
19. Verifikasi login langsung berhasil dan status Requires Reset dibersihkan penuh

### Pemulihan akun terkunci Permanen (Eskalasi 7 Hari)

20. Coba login menggunakan `yuniastuti@qwertysystem.net`
21. Verifikasi alert akun terkunci permanen tampil
22. Selesaikan alur Reset Password hingga sukses untuk Yuni Astuti
23. Lakukan login menggunakan password baru Yuni
24. Verifikasi login langsung berhasil dan status terkunci permanen telah terangkat

### Pembersihan counter kegagalan harian dan counter percobaan reset per email

25. Verifikasi di database bahwa `failed_count`, `lock_level`, dan rantai hari `consecutive_1h_days` telah di-reset ke 0 untuk akun-akun tersebut
26. Verifikasi counter percobaan reset per email (`password_reset_attempts_by_email`) untuk akun yang bersangkutan juga di-reset kembali ke 0
27. Lakukan satu kali salah password pada akun yang baru dipulihkan
28. Verifikasi counter mulai menghitung kembali dari 1 (kesalahan pertama normal tanpa langsung terkunci)

## Notes

- Sesuai PRD §9.2 F-AUTHRST-04, §9.7 baris 3, `RSTPWD-LOGIC-02a/b/c`, dan keputusan NC-16, submit reset password yang sukses membersihkan seluruh tingkatan lock progression akun (15m, 1h, requires-reset, permanen), counter kegagalan login, serta counter percobaan reset per email dalam satu transaksi atomik.
- Tautan [Reset password] pada alert status Requires Reset di Login mengarahkan langsung ke halaman Reset Password dengan prefilled email (`TC-AUTH-RST-116`).
