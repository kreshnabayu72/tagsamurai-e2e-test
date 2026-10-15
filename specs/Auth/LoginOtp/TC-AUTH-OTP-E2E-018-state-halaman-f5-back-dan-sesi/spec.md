---
id: TC-AUTH-OTP-E2E-018-state-halaman-f5-back-dan-sesi
title: "State Layar Verify OTP dan Confirm to Continue terhadap F5, Tombol Back/Forward, dan Sesi Email-Request"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-OTP-70
  - TC-AUTH-OTP-71
  - TC-AUTH-OTP-72
  - TC-AUTH-OTP-179
coverage:
  web: automated
---

# State Layar Verify OTP dan Confirm to Continue terhadap F5, Tombol Back/Forward, dan Sesi Email-Request

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Principal `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #11), berhak mempublikasikan versi Privacy Policy di `Admin Console > Settings > Privacy Policy`; password dari `Spectra.env.AC_PRINCIPAL_PP_PASSWORD`. Akun ini dipakai hook `before` untuk menerbitkan versi Privacy Policy, bukan oleh langkah uji. Browser langkah uji tanpa sesi login (halaman Login with OTP adalah halaman publik).
- Environment variable: `AC_PRINCIPAL_PP_PASSWORD` (akun aktor Principal), `OTP_PASSWORD` (password user uji yang dipasang saat seeding). Tidak ada password atau token di spec atau fixture. Nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-018`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-70: `Eko Permata` (`ekopermata+{runId}-018@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-71: `Ratna Fitriani` (`ratnafitriani+{runId}-018@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-179: `Dewi Harahap` (`dewiharahap+{runId}-018@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-72: `Taufik Susanti` (`taufiksusanti+{runId}-018@qwertysystem.net`), profil POLICY
  - Profil BASE: Activated, Active ON, sudah login sukses di web pada device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru ada; Agreement dan MFA tidak terpicu.
  - Profil POLICY: seperti BASE, tetapi Principal sudah mempublish versi Privacy Policy yang lebih baru dari versi yang terakhir disetujui user; hanya Agreement terpicu.
- Hook `before` menerbitkan versi Privacy Policy yang lebih baru (akun aktor Principal di atas, Pre-setup #11) lebih dulu, lalu men-seed user BASE dengan persetujuan versi terbaru itu dan user POLICY dengan persetujuan versi sebelumnya. Versi Privacy Policy yang telah diterbitkan adalah state global yang tidak ditarik kembali oleh hook `after`; efeknya, user BASE lain di environment yang disetujui sebelum penerbitan akan memicu Agreement pada login berikutnya. Karena versi Privacy Policy adalah state global, suite berjalan serial (`parallel: false`), tidak hanya karena jam digeser.
- Kemampuan teknis: mail-catcher lingkungan uji untuk membaca kode OTP dan menghitung jumlah email per alamat; reCAPTCHA mode uji di environment (centang tanpa tantangan); jam yang diatur (§6): pada TC-AUTH-OTP-70 jam server dan jam browser (countdown UI berjalan di jam klien) dimajukan bersama 60 detik untuk tiap iterasi langkah 8 (Resend ke-1 sampai ke-5), lalu UI menyegarkan tombol Resend; hook `after` memulihkan keduanya, dan suite yang memanipulasi jam berjalan serial. Pengecualian menunggu waktu nyata untuk jeda pendek (±30 detik, §6 Manipulasi jam) tanpa memajukan jam: langkah 3 (tunggu sekitar 30 detik) beserta pembacaan sisa countdown di langkah 7 (jam baru dimajukan mulai langkah 8), dan pembacaan sisa countdown di langkah 33 pada TC-AUTH-OTP-179.
- State yang berubah: TC-AUTH-OTP-71, TC-AUTH-OTP-179, dan TC-AUTH-OTP-72 diakhiri dengan login sukses; langkah logout dari Portal — Product Hub ada di antara TC dan hook `after` menutup sesi yang tersisa.

## Test Steps

### TC-AUTH-OTP-70: Muat ulang halaman (F5) pada layar Verify OTP

1. Buka halaman `Auth > Login with OTP > Request OTP` di browser tanpa sesi
2. Ketik `ekopermata+{runId}-018@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
3. Tunggu countdown Resend berjalan sekitar 30 detik
4. Tekan F5 pada browser
5. Verifikasi layar Verify OTP tetap tampil dengan Subtitle "Enter the 6-digit code sent to: ekopermata+{runId}-018@qwertysystem.net"
6. Verifikasi kotak digit kosong
7. Verifikasi countdown Resend melanjutkan sisa waktu dan tidak kembali ke "Resend code in (00:59)"
8. Ulangi 5 kali berturut-turut: tunggu countdown 60 detik selesai, lalu klik [Resend code]
9. Verifikasi area Resend menampilkan "Resend code in (09:59)" setelah Resend ke-5 (counter tidak ter-reset oleh F5)
10. Buka mail-catcher untuk `ekopermata+{runId}-018@qwertysystem.net`
11. Verifikasi tidak ada email OTP baru akibat F5: jumlah email di mail-catcher tepat 6 (1 dari Request OTP dan 5 dari Resend)

### TC-AUTH-OTP-71: Tombol Back browser dari layar Verify OTP

12. Buka halaman `Auth > Login with OTP > Request OTP` (buka ulang alamat halaman di browser yang sama)
13. Ketik `ratnafitriani+{runId}-018@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
14. Klik tombol Back pada browser
15. Verifikasi halaman Request OTP tampil dengan field Email berisi `ratnafitriani+{runId}-018@qwertysystem.net`
16. Verifikasi widget reCAPTCHA belum dicentang
17. Tekan tombol Forward browser sampai layar Verify OTP tampil
18. Ketik 6 digit kode OTP dari email (mail-catcher `ratnafitriani+{runId}-018@qwertysystem.net`; kode yang diterbitkan sebelumnya) pada kotak digit
19. Verifikasi kode lama diterima (tidak di-invalidasi oleh Back)
20. Verifikasi browser dialihkan ke Portal — Product Hub
21. Verifikasi sesi aktif untuk `Ratna Fitriani`
22. Periksa mail-catcher untuk `ratnafitriani+{runId}-018@qwertysystem.net` dan hitung jumlah email OTP
23. Verifikasi mail-catcher `ratnafitriani+{runId}-018@qwertysystem.net` tetap memuat 1 email OTP (baseline: 1 dari Request OTP pada langkah 13)

### TC-AUTH-OTP-179: Kembali ke layar Verify OTP lewat Back/Forward browser setelah Request OTP ditolak mengikuti state Resend sesi

24. Logout dari Portal — Product Hub dan buka halaman `Auth > Login with OTP > Request OTP`
25. Ketik `dewiharahap+{runId}-018@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
26. Klik tautan [Back to Login with Password]
27. Klik tautan [Log in with OTP]
28. Centang widget reCAPTCHA "I'm not a robot"
29. Klik button [Request OTP] (permintaan kedua ditolak karena cooldown 60 detik)
30. Verifikasi layar Request OTP tidak punya tautan khusus ke layar Verify OTP
31. Tekan tombol Back browser sampai layar Verify OTP tampil
32. Verifikasi layar Verify tampil lewat Back browser
33. Verifikasi area Resend pada layar Verify mengikuti sisa countdown sesi yang sama (bukan kembali ke "Resend code in (00:59)")
34. Ketik 6 digit kode OTP yang diterbitkan sebelumnya (mail-catcher `dewiharahap+{runId}-018@qwertysystem.net`) pada kotak digit
35. Verifikasi kode diterima
36. Verifikasi browser dialihkan ke Portal — Product Hub
37. Verifikasi sesi aktif untuk `Dewi Harahap`

### TC-AUTH-OTP-72: Muat ulang halaman (F5) pada layar Confirm to Continue selama token pra-autentikasi masih berlaku

38. Logout dari Portal — Product Hub dan buka halaman `Auth > Login with OTP > Request OTP`
39. Ketik `taufiksusanti+{runId}-018@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
40. Ketik 6 digit kode OTP dari email (mail-catcher `taufiksusanti+{runId}-018@qwertysystem.net`) pada kotak digit
41. Tekan F5 pada browser
42. Verifikasi layar Confirm to Continue tetap tampil
43. Verifikasi checkbox "I have read and agree to the Privacy Policy *" unchecked
44. Centang checkbox "I have read and agree to the Privacy Policy *"
45. Klik button [Continue ➔]
46. Verifikasi browser dialihkan ke Portal — Product Hub
47. Verifikasi sesi aktif untuk `Taufik Susanti`

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC menyimpang dari TC sumber (70, 71, 72, 179): TC-AUTH-OTP-70 (tanpa sesi login) lebih dulu, lalu TC-AUTH-OTP-71, TC-AUTH-OTP-179, dan TC-AUTH-OTP-72 yang berakhir login sukses; TC-AUTH-OTP-72 terakhir karena memakai profil POLICY (prinsip 3).
- Langkah 12, 24, dan 38 adalah langkah penghubung antar-TC (S-03, S-09): buka ulang halaman Request OTP dan, pada langkah 24 dan 38, logout dari sesi hasil TC sebelumnya. Langkah 2, 13, 25, dan 39 menggabungkan ketik email, centang reCAPTCHA, dan klik [Request OTP] menjadi satu baris karena persis sama dengan prasyarat TC. Langkah 8 menggabungkan lima iterasi tunggu 60 detik dan klik [Resend code] yang pada TC sumber ditulis berulang.
- Langkah 10 dan 11 mengubah penempatan pemeriksaan TC-AUTH-OTP-70 langkah 17 ("Periksa mail-catcher") menjadi hitungan pasti 6 email supaya "tidak ada email OTP baru akibat F5" dapat diasersi deterministik (S-14). Area Resend "(09:59)" diverifikasi di langkah 9, sebelum mail-catcher dibuka, supaya asersi layar tidak dibaca saat konteks berada di mail-catcher.
- Langkah 29 TC-AUTH-OTP-179 menolak Request OTP kedua karena cooldown 60 detik (Data Uji TC); alert penolakan "Too many requests. Please try again later." tidak ada di Expected TC ini sehingga tidak diasersi di sini, melainkan di spec 024 (TC-AUTH-OTP-90).
- Langkah 45 dan 46 TC-AUTH-OTP-72: "persetujuan tersimpan" tidak punya observable tersendiri di UI selain pengalihan ke Product Hub; persistensi persetujuan diuji di spec 032 (TC-AUTH-OTP-142).
- Temuan untuk QA: (1) TC-AUTH-OTP-70 langkah 5 menyebut "sekitar 30 detik" tanpa toleransi; spec menulis sama dan mengasersi hanya bahwa countdown tidak kembali ke "Resend code in (00:59)". (2) TC-AUTH-OTP-179 Expected c menyebut kode "yang diterbitkan sebelumnya" diterima, tanpa menyebut apakah Request OTP yang ditolak menerbitkan kode baru; spec memakai kode dari email pertama. (3) TC-AUTH-OTP-72 butir b menggabungkan "persetujuan tersimpan" dan pengalihan ke Product Hub; lihat Notes. (4) TC-AUTH-OTP-72 Expected b menyebut "persetujuan tersimpan" tanpa langkah observasinya; spec hanya mengasersi pengalihan dan sesi aktif. (5) TC-AUTH-OTP-72 memakai profil POLICY yang bergantung pada penerbitan versi Privacy Policy global; TC tidak menyebut cara memulihkan versi itu setelah pengujian.
