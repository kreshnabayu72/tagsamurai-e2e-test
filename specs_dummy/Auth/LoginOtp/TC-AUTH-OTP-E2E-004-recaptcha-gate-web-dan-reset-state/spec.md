---
id: TC-AUTH-OTP-E2E-004-recaptcha-gate-web-dan-reset-state
title: "Proteksi reCAPTCHA Gate Web, Evaluasi Token Sekali Pakai, dan Reset State"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-22
  - TC-AUTH-OTP-23
  - TC-AUTH-OTP-24
  - TC-AUTH-OTP-25
  - TC-AUTH-OTP-26
  - TC-AUTH-OTP-27
coverage:
  web: automated
---

# Proteksi reCAPTCHA Gate Web, Evaluasi Token Sekali Pakai, dan Reset State

## Prerequisites

- Belum login dan session kosong. Halaman `Auth > Login with OTP > Request OTP` (`/login/otp`) terbuka di browser.
- User `Dimas Hidayati` (`dimashidayati@qwertysystem.net`) profil BASE (Tabel Data Uji Pre-setup #2).
- User `Lestari Anggraini` (`lestarianggraini@qwertysystem.net`) profil PENDING (Pending Activation).
- User `Bayu Gunawan` (`bayugunawan@qwertysystem.net`) profil BASE (Tabel Data Uji Pre-setup #2).
- User `Intan Ramadhan` (`intanramadhan@qwertysystem.net`) profil BASE (Tabel Data Uji Pre-setup #2).
- Akun Total Control Global Settings disiapkan untuk memverifikasi pencatatan log bila diperlukan.

## Test Steps

### Blokir request tanpa mencentang reCAPTCHA

1. Buka halaman Request OTP di browser
2. Masukkan email valid `dimashidayati@qwertysystem.net` ke field Email
3. Biarkan widget reCAPTCHA dalam keadaan belum dicentang
4. Klik button [Request OTP]
5. Verifikasi caption error inline di bawah widget reCAPTCHA adalah "Please verify that you are not a robot"
6. Verifikasi tidak ada request OTP yang dikirim ke server dan halaman tetap pada Request OTP

### Hilangnya caption error saat reCAPTCHA dicentang

7. Tanpa mengubah input email, klik checkbox widget reCAPTCHA untuk menyelesaikan tantangan
8. Verifikasi caption error "Please verify that you are not a robot" otomatis hilang seketika saat widget berhasil dicentang

### Urutan evaluasi: Email dievaluasi sebelum reCAPTCHA di client

9. Buka kembali halaman Request OTP dalam sesi bersih
10. Biarkan field Email kosong
11. Centang widget reCAPTCHA hingga bertanda centang hijau
12. Klik button [Request OTP]
13. Verifikasi caption error "Email must not be empty" muncul di bawah field Email
14. Verifikasi tidak ada error pada slot reCAPTCHA
15. Masukkan format email salah `dimas@invalid` tanpa menyentuh ulang widget
16. Klik button [Request OTP]
17. Verifikasi caption error "Email format is incorrect" muncul di bawah field Email

### reCAPTCHA mendahului pemeriksaan status akun server (Defense in Depth)

18. Buka kembali halaman Request OTP
19. Masukkan email `lestarianggraini@qwertysystem.net` (user berstatus Pending Activation)
20. Biarkan widget reCAPTCHA tidak dicentang
21. Klik button [Request OTP]
22. Verifikasi caption "Please verify that you are not a robot" muncul di bawah widget reCAPTCHA
23. Verifikasi sistem tidak menampilkan pesan status akun "Your account has not been activated yet" karena pemeriksaan CAPTCHA menghadang sebelum panggilan backend dilakukan

### Invarian token sekali pakai dan reset state widget setelah penolakan/respons server

24. Masukkan email `bayugunawan@qwertysystem.net`
25. Centang widget reCAPTCHA
26. Simulasikan penolakan server (misalnya respon error atau trigger status) saat submit [Request OTP]
27. Verifikasi setelah respons server diterima, widget reCAPTCHA otomatis kembali ke keadaan belum dicentang (unchecked)
28. Verifikasi pengguna wajib menyelesaikan ulang tantangan reCAPTCHA sebelum dapat menekan button [Request OTP] kembali

## Notes

- Token Google reCAPTCHA bersifat one-time use (sekali pakai); setelah diverifikasi atau ditolak oleh server, token lama kadaluwarsa dan widget harus di-reset ke status awal (sesuai NC-09).
- Evaluasi form client-side selalu mengutamakan field Email sebelum mengevaluasi widget reCAPTCHA.
