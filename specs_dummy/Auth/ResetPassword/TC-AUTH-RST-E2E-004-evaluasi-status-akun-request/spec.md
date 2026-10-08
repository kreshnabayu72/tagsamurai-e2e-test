---
id: TC-AUTH-RST-E2E-004-evaluasi-status-akun-request
title: "Evaluasi akun saat Request Reset: email tidak terdaftar, akun dihapus, akun inactive, dan status Client"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-23
  - TC-AUTH-RST-24
  - TC-AUTH-RST-25
  - TC-AUTH-RST-26
  - TC-AUTH-RST-27
coverage:
  web: automated
---

# Evaluasi akun saat Request Reset: email tidak terdaftar, akun dihapus, akun inactive, dan status Client

## Prerequisites

- User belum login (guest); browser web berada di halaman `/reset-password`.
- Environment uji terisolasi khusus pengujian otomatis.
- Data uji akun terkonfigurasi:
  - `belumterdaftar@qwertysystem.net` (tidak terdaftar di sistem).
  - `jokosusilo@qwertysystem.net` (akun telah dihapus / soft-deleted).
  - `tonokurniawan@qwertysystem.net` (akun berstatus Inactive / nonaktif).
  - `rudihartono@qwertysystem.net` (akun aktif milik Client berstatus Suspended / read-only).
  - `mayaputri@qwertysystem.net` (akun aktif milik Client berpaket Starter).
- Admin pemantau log `superAdminGlobalSettings_automated_qaTeam1@qwertysystem.net` memiliki akses ke Activity Log Session dan User Log.

## Test Steps

### Request dengan email tidak terdaftar

1. Buka halaman Reset Password di browser web
2. Masukkan email "belumterdaftar@qwertysystem.net" pada field Email
3. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Reset Password]
4. Verifikasi caption inline "Email is not registered yet" tampil di bawah field Email
5. Verifikasi browser tetap berada di halaman Reset Password dan tidak berpindah ke halaman Email Sent!
6. Buka Activity Log > Session dan User Log menggunakan sesi admin
7. Verifikasi tidak ada pencatatan entri baru sama sekali untuk request email yang tidak terdaftar (anti-enumerasi)

### Request dengan email akun yang sudah dihapus (Deleted)

8. Buka kembali halaman Reset Password sebagai guest
9. Masukkan email "jokosusilo@qwertysystem.net" pada field Email
10. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Reset Password]
11. Verifikasi caption inline "Email is not registered yet" tampil di bawah field Email (diperlakukan identik dengan email tidak terdaftar)
12. Verifikasi tidak ada entri baru yang dicatat di Activity Log maupun User Log

### Request dengan email akun Inactive

13. Buka halaman Reset Password sebagai guest
14. Masukkan email "tonokurniawan@qwertysystem.net" pada field Email
15. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Reset Password]
16. Verifikasi Alert Danger tampil di atas tombol [Reset Password] dengan teks "Your account is inactive"
17. Verifikasi tombol [Reset Password] tetap enabled dan input email dipertahankan
18. Buka Activity Log > Session dan User Log menggunakan sesi admin
19. Verifikasi tercatat entri baru dengan Activity "Reset Password", Status "Failed", dan Note "Account is inactive"

### Request oleh user pada Client berstatus Suspended

20. Buka halaman Reset Password sebagai guest
21. Masukkan email "rudihartono@qwertysystem.net" pada field Email
22. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Reset Password]
23. Verifikasi request diproses normal menuju halaman Email Sent!
24. Verifikasi status client suspended (read-only) tidak memblokir fungsionalitas pemulihan password akun

### Request oleh user pada Client paket Starter

25. Buka kembali halaman Reset Password sebagai guest
26. Masukkan email "mayaputri@qwertysystem.net" pada field Email
27. Selesaikan verifikasi reCAPTCHA lalu klik tombol [Reset Password]
28. Verifikasi request diproses normal menuju halaman Email Sent!
29. Verifikasi fitur Reset Password tidak dibatasi oleh tiering paket lisensi (tidak ada plan gating)

## Notes

- Sesuai PRD §9.4.2 baris 2-4 dan `RSTPWD-LOGIC-04g`, pesan "Email is not registered yet" ditampilkan secara eksplisit di UI namun tidak dicatat pada audit log untuk mencegah enumerasi akun (`RSTPWD-LOGIC-04h`).
- Sesuai PRD §9.10 dan §9.4.1 D2, fitur Reset Password berada pada zona publik pra-autentikasi sehingga Client berstatus Suspended maupun plan Starter tidak dibatasi.
