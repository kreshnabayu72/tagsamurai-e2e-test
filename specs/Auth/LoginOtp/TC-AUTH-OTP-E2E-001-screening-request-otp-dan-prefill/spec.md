---
id: TC-AUTH-OTP-E2E-001-screening-request-otp-dan-prefill
title: "Screening Halaman Request OTP, Prefill Email dari Login with Password, dan Tautan Use Password Instead"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-01
  - TC-AUTH-OTP-03
  - TC-AUTH-OTP-04
  - TC-AUTH-OTP-05
  - TC-AUTH-OTP-35
coverage:
  web: automated
---

# Screening Halaman Request OTP, Prefill Email dari Login with Password, dan Tautan Use Password Instead

## Prerequisites

- Mode: FE+BE (web). Tanpa sesi login; spec berjalan di konteks browser bersih. reCAPTCHA mode uji di environment (tidak dicentang pada spec ini).
- Environment variable: `OTP_PASSWORD` (password user uji Activated yang di-seed). Tidak ada password atau token di spec atau fixture. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Hook `before` (seeding API) membuat user profil BASE berikut dengan suffix per run, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-03: `Andi Wulandari` (`andiwulandari+{runId}-001@qwertysystem.net`), Activated, Active ON
  - TC-AUTH-OTP-35: `Galih Tanjung` (`galihtanjung+{runId}-001@qwertysystem.net`), Activated, Active ON
- TC-AUTH-OTP-01, 04, dan 05 tidak membuat atau memakai data user: layar hanya dibuka dan dibaca. Input uji `john@` pada TC-AUTH-OTP-04 ditulis literal (input yang tidak pernah di-submit).
- Tidak ada state global yang diubah.

## Test Steps

### TC-AUTH-OTP-01: Screening halaman Request OTP (web)

1. Buka halaman `Auth > Login with OTP > Request OTP` di browser
2. Susuri halaman dari atas ke bawah tanpa mengisi atau mengklik apa pun
3. Verifikasi halaman Request OTP tampil dengan Card terpusat pada canvas penuh
4. Verifikasi Logo TAG Samurai tampil di bagian atas card
5. Verifikasi Title "Log in with OTP"
6. Verifikasi Subtitle "We'll send a 6-digit verification code to your email"
7. Verifikasi field Email berlabel "Email"
8. Verifikasi field Email menampilkan placeholder "Enter your email"
9. Verifikasi field Email kosong
10. Verifikasi field Email tanpa caption error
11. Verifikasi widget Google reCAPTCHA v2 "I'm not a robot" tampil
12. Verifikasi widget reCAPTCHA dalam keadaan belum dicentang
13. Verifikasi widget reCAPTCHA tanpa caption error
14. Verifikasi tidak ada checkbox Agreement dan tidak ada kotak digit OTP
15. Verifikasi button [Request OTP] full-width
16. Verifikasi button [Request OTP] bervariant solid dengan severity primary
17. Verifikasi button [Request OTP] dalam keadaan enabled
18. Verifikasi tautan [Use password instead] tampil di bawah button
19. Verifikasi tautan [Use password instead] terpusat
20. Verifikasi tidak ada tautan [Edit email], tautan [Back to Login with Password], area Resend, button [Verify], dan button [Continue ➔]

### TC-AUTH-OTP-05: Halaman Request OTP dibuka langsung menampilkan field Email kosong dengan placeholder

21. Buka ulang halaman `Auth > Login with OTP > Request OTP` melalui alamat langsung di browser
22. Verifikasi field Email kosong dan menampilkan placeholder "Enter your email"
23. Verifikasi button [Request OTP] enabled
24. Verifikasi reCAPTCHA belum dicentang

### TC-AUTH-OTP-03: Email dari Login with Password terisi otomatis di halaman Request OTP

25. Buka halaman `Auth > Login with Password`
26. Ketik `andiwulandari+{runId}-001@qwertysystem.net` pada field Email
27. Klik tautan [Log in with OTP]
28. Verifikasi halaman `Auth > Login with OTP > Request OTP` tampil
29. Verifikasi field Email sudah terisi `andiwulandari+{runId}-001@qwertysystem.net`
30. Verifikasi field Email masih dapat diubah (enabled dan dapat diedit)
31. Verifikasi widget reCAPTCHA belum dicentang

### TC-AUTH-OTP-04: Email setengah jadi dari Login with Password terbawa apa adanya ke halaman Request OTP

32. Buka halaman `Auth > Login with Password`
33. Ketik `john@` pada field Email
34. Klik tautan [Log in with OTP]
35. Verifikasi halaman Request OTP tampil
36. Verifikasi field Email berisi `john@` apa adanya
37. Verifikasi tidak ada caption error pada field Email

### TC-AUTH-OTP-35: Tautan Use password instead membuka Login with Password dengan email terbawa

38. Buka halaman `Auth > Login with OTP > Request OTP` di browser
39. Ketik `galihtanjung+{runId}-001@qwertysystem.net` pada field Email
40. Klik tautan [Use password instead]
41. Verifikasi halaman `Auth > Login with Password` tampil dengan Title "Login with Password"
42. Verifikasi field Email berisi `galihtanjung+{runId}-001@qwertysystem.net`

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Urutan TC di spec: 01, 05, 03, 04, 35 (screening dan pembukaan langsung lebih dulu, lalu navigasi antar halaman). Urutan ini berbeda dari nomor TC sumber; tidak ada TC yang bergantung pada hasil TC lain.
- Langkah 25 dan 32 adalah langkah penghubung (membuka Login with Password agar TC-AUTH-OTP-03 dan TC-AUTH-OTP-04 mulai dari state bersih), tanpa asersi (S-03). Langkah 21 dan 38 adalah langkah TC sendiri (TC-AUTH-OTP-05 dan TC-AUTH-OTP-35).
- Asersi absence TC-AUTH-OTP-35 butir c ("tidak ada entri log baru di `Global Settings > Activity Log > Session` maupun `Global Settings > User > Detail > User Log`") dipindah ke E2E-047 (kelas g); spec ini hanya memuat asersi navigasi. Pembagian TC dicatat juga di Notes E2E-047.
- Temuan untuk QA:
  - TC-AUTH-OTP-01 precondition b menyebut user `Budi Santoso` (BASE), tetapi langkah dan Expected hanya membaca layar; spec tidak men-seed user itu.
  - TC-AUTH-OTP-03 Expected b "masih dapat diubah" tidak menyebut cara pembuktian; spec memverifikasi field berstatus enabled dan dapat diedit tanpa mengubah nilainya.
