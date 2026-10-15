---
id: TC-AUTH-OTP-E2E-008-status-akun-pra-request
title: "Evaluasi Status Akun pada Request OTP: Email Belum Terdaftar, Belum Aktivasi, dan Inactive"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-19
  - TC-AUTH-OTP-20
  - TC-AUTH-OTP-21
coverage:
  web: automated
---

# Evaluasi Status Akun pada Request OTP: Email Belum Terdaftar, Belum Aktivasi, dan Inactive

## Prerequisites

- Mode: FE+BE (web). Tanpa sesi login; spec berjalan di konteks browser bersih. reCAPTCHA mode uji di environment.
- Environment variable: `OTP_PASSWORD` (password user uji yang sudah Activated). Tidak ada password atau token di spec atau fixture.
- Kemampuan teknis: mail-catcher lingkungan uji dapat dibaca untuk alamat yang diketik (membuktikan tidak ada email OTP terkirim).
- Hook `before` (seeding API) membuat user berikut dengan suffix per run, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-20: `Fajar Lubis` (`fajarlubis+{runId}-008@qwertysystem.net`), profil PENDING (Pending Activation, Active ON)
  - TC-AUTH-OTP-21: `Putri Suryani` (`putrisuryani+{runId}-008@qwertysystem.net`), profil INACTIVE (Activated, Toggle Global Active OFF)
- TC-AUTH-OTP-19 memakai `tidakterdaftar.xyz@qwertysystem.net` yang tidak ada di Global Settings > User; alamat ditulis literal karena submit-nya diblokir dan tidak ada data tercipta.
- Tidak ada state global yang diubah.

## Test Steps

### TC-AUTH-OTP-19: Request OTP dengan email yang belum terdaftar

1. Buka halaman `Auth > Login with OTP > Request OTP` di browser
2. Ketik `tidakterdaftar.xyz@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Verifikasi caption error di bawah field Email: "Email is not registered yet"
6. Verifikasi tidak ada email OTP terkirim
7. Verifikasi halaman tetap di Request OTP

### TC-AUTH-OTP-20: Request OTP dengan akun yang belum aktivasi

8. Buka ulang halaman `Auth > Login with OTP > Request OTP`
9. Ketik `fajarlubis+{runId}-008@qwertysystem.net` pada field Email
10. Centang widget reCAPTCHA "I'm not a robot"
11. Klik button [Request OTP]
12. Verifikasi caption error di bawah field Email: "Your account has not been activated"
13. Verifikasi tidak ada email OTP terkirim
14. Verifikasi halaman tetap di Request OTP

### TC-AUTH-OTP-21: Request OTP dengan akun yang inactive (Toggle Global OFF)

15. Buka ulang halaman `Auth > Login with OTP > Request OTP`
16. Ketik `putrisuryani+{runId}-008@qwertysystem.net` pada field Email
17. Centang widget reCAPTCHA "I'm not a robot"
18. Klik button [Request OTP]
19. Verifikasi caption error di bawah field Email: "Your account is inactive"
20. Verifikasi tidak ada email OTP terkirim
21. Verifikasi halaman tetap di Request OTP

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Langkah 8 dan 15 adalah langkah penghubung (membuka ulang halaman Request OTP agar tiap TC mulai dari field kosong dan widget reCAPTCHA belum dicentang), tanpa asersi (S-03).
- Asersi absence TC-AUTH-OTP-19 butir c ("tidak ada entri log baru di `Global Settings > Activity Log > Session` maupun `Global Settings > User > Detail > User Log`") dipindah ke E2E-040 (kelas g). Pembagian TC dicatat juga di Notes E2E-040.
- Spec ini tidak membuka Activity Log sehingga akun admin Total Control tidak dipakai. Pencatatan Failed untuk TC-AUTH-OTP-20 dan 21 dicakup oleh E2E-036 lewat TC-AUTH-OTP-117 dan 118.
- Temuan untuk QA:
  - TC-AUTH-OTP-20 dan 21 punya Post Condition "Percobaan dicatat sebagai Failed ... detail pada TC Logging" tanpa langkah observasi di TC ini; spec tidak mengasersikannya (S-01). Pencatatan Failed (Note `Account is not activated` dan `Account is inactive`) hanya teramati lewat TC-AUTH-OTP-117 dan 118 di E2E-036; mohon QA mengonfirmasi rujukan itu sebagai padanannya.
