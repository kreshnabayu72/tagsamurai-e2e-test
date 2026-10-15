---
id: TC-AUTH-OTP-E2E-002-screening-verify-otp-dan-confirm
title: "Screening Halaman Verify OTP, Tautan Back to Login with Password, dan Layar Confirm to Continue"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-07
  - TC-AUTH-OTP-36
  - TC-AUTH-OTP-09
coverage:
  web: automated
---

# Screening Halaman Verify OTP, Tautan Back to Login with Password, dan Layar Confirm to Continue

## Prerequisites

- Mode: FE+BE (web). Tanpa sesi login; spec berjalan di konteks browser bersih. reCAPTCHA mode uji di environment.
- Environment variable: `OTP_PASSWORD` (password user uji Activated yang di-seed). Tidak ada password atau token di spec atau fixture.
- Kemampuan teknis: mail-catcher lingkungan uji dapat dibaca untuk membaca kode OTP 6 digit dari email yang masuk (dipakai TC-AUTH-OTP-09).
- Hook `before` (seeding API) membuat user berikut dengan suffix per run, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-07: `Dewi Puspita` (`dewipuspita+{runId}-002@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-36: `Citra Rahmawati` (`citrarahmawati+{runId}-002@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-09: `Nur Wibowo` (`nurwibowo+{runId}-002@qwertysystem.net`), profil FIRST (Activated, Active ON, belum pernah menyelesaikan login web, Authenticator belum terdaftar; login pertama terpakai pada TC ini)
- Tidak ada state global yang diubah.

## Test Steps

### TC-AUTH-OTP-07: Screening halaman Verify OTP setelah Request OTP berhasil

1. Buka halaman `Auth > Login with OTP > Request OTP` di browser
2. Ketik `dewipuspita+{runId}-002@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Verifikasi halaman Verify OTP tampil
6. Verifikasi teks "Resend code in (00:59)" tampil
7. Verifikasi teks "Resend code in (00:59)" dalam keadaan disabled (State A)
8. Verifikasi Title "Enter verification code"
9. Verifikasi Subtitle "Enter the 6-digit code sent to: dewipuspita+{runId}-002@qwertysystem.net" dengan email penuh (tidak di-mask)
10. Verifikasi tautan [Edit email] tampil di bawah Subtitle
11. Verifikasi 6 kotak digit kosong tampil dalam satu baris
12. Verifikasi kursor aktif pada kotak 1
13. Verifikasi slot caption error di bawah kotak digit kosong
14. Verifikasi button [Verify] tidak tampil
15. Verifikasi tautan [Back to Login with Password] tampil di bagian bawah
16. Verifikasi tautan [Back to Login with Password] terpusat
17. Verifikasi tidak ada field Email, widget reCAPTCHA, button [Request OTP], tautan [Use password instead], tautan "Reset Password", button [Continue ➔], dan checkbox Agreement

### TC-AUTH-OTP-36: Tautan Back to Login with Password dari halaman Verify OTP membuka Login with Password dengan email terbawa

18. Buka halaman `Auth > Login with OTP > Request OTP` di browser
19. Ketik `citrarahmawati+{runId}-002@qwertysystem.net` pada field Email
20. Centang widget reCAPTCHA "I'm not a robot"
21. Klik button [Request OTP]
22. Pada halaman Verify OTP klik tautan [Back to Login with Password]
23. Verifikasi halaman `Auth > Login with Password` tampil dengan Title "Login with Password"
24. Verifikasi field Email berisi `citrarahmawati+{runId}-002@qwertysystem.net`

### TC-AUTH-OTP-09: Screening layar Confirm to Continue setelah OTP benar pada login pertama

25. Buka halaman `Auth > Login with OTP > Request OTP` di browser
26. Ketik `nurwibowo+{runId}-002@qwertysystem.net` pada field Email
27. Centang widget reCAPTCHA "I'm not a robot"
28. Klik button [Request OTP]
29. Ambil kode OTP 6 digit dari email yang masuk ke mail-catcher untuk `nurwibowo+{runId}-002@qwertysystem.net`
30. Ketik 6 digit kode pada kotak digit sehingga verifikasi otomatis berjalan
31. Verifikasi layar Confirm to Continue tampil dengan Title "Confirm to Continue"
32. Verifikasi checkbox "I have read and agree to the Privacy Policy *" dalam keadaan unchecked
33. Verifikasi teks "Privacy Policy" pada checkbox berupa tautan ke halaman Privacy Policy
34. Verifikasi tidak ada caption error pada layar
35. Verifikasi button [Continue ➔] full-width (variant solid, severity primary)
36. Verifikasi button [Continue ➔] dalam keadaan enabled
37. Verifikasi tidak ada kotak digit OTP, field Email, widget reCAPTCHA, button [Request OTP], area Resend, tautan [Edit email], tautan [Use password instead], tautan [Back to Login with Password], dan button [Verify]

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Urutan TC di spec: 07, 36, 09 (sama dengan urutan layar: Verify OTP, navigasi kembali, lalu Confirm to Continue). TC-AUTH-OTP-07 selesai di layar Verify OTP tanpa verifikasi; kode OTP milik `Dewi Puspita` dan `Citra Rahmawati` dibiarkan tidak dipakai (tidak ada login selesai).
- Langkah 18 dan 25 adalah langkah penghubung (membuka halaman Request OTP agar TC berikutnya mulai dari state bersih), tanpa asersi (S-03).
- Asersi absence TC-AUTH-OTP-36 butir c ("tidak ada entri log untuk navigasi ini") dipindah ke E2E-047 (kelas g). Pembagian TC dicatat juga di Notes E2E-047.
- Temuan untuk QA:
  - TC-AUTH-OTP-07 Expected b.iv mengasersi "Resend code in (00:59)" tepat saat layar tampil; asersi ini sensitif terhadap waktu antara Request OTP dan pembacaan layar. Spec menempatkan kedua asersi countdown (langkah 6 dan 7) tepat setelah halaman Verify OTP tampil untuk memperkecil jeda; asersi tetap sensitif waktu.
  - TC-AUTH-OTP-09 hanya menyebut "6 digit kode dari email" tanpa menyebut cara membaca email; spec memakai mail-catcher lingkungan uji sesuai Pre-setup #9.
