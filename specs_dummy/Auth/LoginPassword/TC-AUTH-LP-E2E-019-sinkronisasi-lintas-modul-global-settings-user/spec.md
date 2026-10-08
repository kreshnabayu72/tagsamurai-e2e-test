---
id: TC-AUTH-LP-E2E-019-sinkronisasi-lintas-modul-global-settings-user
title: Sinkronisasi realtime perubahan status akun dari Global Settings > User
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-131
  - TC-AUTH-LP-132
  - TC-AUTH-LP-133
  - TC-AUTH-LP-134
coverage:
  web: automated
---

# Sinkronisasi realtime perubahan status akun dari Global Settings > User

## Prerequisites

- Pengujian memerlukan dua sesi browser:
  - Sesi 1: Form Login with Password untuk submit login.
  - Sesi 2: Administrator Total Control pada modul `Global Settings > User`.
- User subjek: `yuniastuti@qwertysystem.net` (Activated, Active), `bambangirawan@qwertysystem.net` (Activated, Active), `eniraharyu@qwertysystem.net` (Pending Activation dengan link aktivasi yang masih aktif).

## Test Steps

### Perubahan status Toggle Global OFF langsung memblokir login

1. Pada Sesi 2: Buka menu `Global Settings > User`, cari user "Yuni Astuti"
2. Matikan toggle switch pada kolom Toggle Global sehingga berstatus OFF (Deactivate), lalu konfirmasi dialog
3. Pada Sesi 1: Buka halaman Login with Password
4. Masukkan email `yuniastuti@qwertysystem.net` dan password `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik tombol [Log in]
5. Verifikasi sistem secara instan menampilkan Alert Danger "Your account is inactive" di atas tombol [Log in] tanpa delay
6. Verifikasi tidak ada sesi yang terbentuk dan browser tetap berada di halaman Login

### Perubahan status Toggle Global ON langsung memulihkan akses login

7. Pada Sesi 2: Nyalakan kembali toggle switch Toggle Global untuk "Yuni Astuti" sehingga berstatus ON (Activate)
8. Pada Sesi 1: Masukkan kembali password `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik tombol [Log in]
9. Verifikasi Alert Danger "Your account is inactive" tidak tampil lagi
10. Verifikasi login langsung berhasil dan browser menuju Portal — Product Hub

### Penghapusan user di Global Settings diperlakukan sebagai Email belum terdaftar

11. Pada Sesi 2: Cari user "Bambang Irawan" di `Global Settings > User`, klik menu aksi (⋯), pilih Delete User, lalu konfirmasi penghapusan
12. Pada Sesi 1: Logout dari Sesi 1 dan buka kembali halaman Login with Password
13. Masukkan email `bambangirawan@qwertysystem.net` dan password `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik tombol [Log in]
14. Verifikasi sistem menampilkan caption inline "Email is not registered yet" di bawah field Email
15. Verifikasi sistem memperlakukan email tersebut seolah-olah belum pernah ada di database

### Aktivasi akun yang berhasil langsung membuka akses login

16. Pada Sesi 1: Masukkan email `eniraharyu@qwertysystem.net` (berstatus Pending Activation) dan password `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik [Log in]
17. Verifikasi Alert Danger "Your account has not been activated" tampil
18. Selesaikan alur modul Account Activation menggunakan link aktivasi resmi untuk `eniraharyu@qwertysystem.net` dan buat password baru `QaLogin#2026`
19. Kembali ke halaman Login with Password
20. Masukkan email `eniraharyu@qwertysystem.net` dan password baru `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik [Log in]
21. Verifikasi Alert "Your account has not been activated" tidak tampil lagi
22. Verifikasi layar Confirm to Continue langsung tampil (sebagai login pertama)

## Notes

- Sinkronisasi perubahan status user dari modul `Global Settings > User` dan `Account Activation` bersifat instan tanpa bergantung pada scheduled sync (`PRD §9.7`).
