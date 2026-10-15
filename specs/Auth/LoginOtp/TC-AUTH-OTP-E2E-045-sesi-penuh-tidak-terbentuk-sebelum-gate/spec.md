---
id: TC-AUTH-OTP-E2E-045-sesi-penuh-tidak-terbentuk-sebelum-gate
title: "Sesi Penuh Tidak Terbentuk sebelum Agreement Dikonfirmasi dan sebelum MFA Selesai"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-158
  - TC-AUTH-OTP-159
coverage:
  web: automated
---

# Sesi Penuh Tidak Terbentuk sebelum Agreement Dikonfirmasi dan sebelum MFA Selesai

## Prerequisites

- Mode: FE+BE.
- Password user uji dari `Spectra.env.OTP_PASSWORD` (hanya dipakai saat seeding user lewat API). Tidak ada password atau token di spec atau fixture.
- Akun aktor hook `before`: Principal `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #11), berhak mempublikasikan versi Privacy Policy di `Admin Console > Settings > Privacy Policy`; password dari `Spectra.env.AC_PRINCIPAL_PP_PASSWORD`. Akun ini dipakai hook `before` untuk menerbitkan versi Privacy Policy, bukan oleh langkah uji.
- Environment variable: `AC_PRINCIPAL_PP_PASSWORD`, `OTP_PASSWORD`.
- Kemampuan teknis: dua tab pada konteks browser yang sama (tab pertama menahan layar gate, tab lain membuka Portal — Product Hub langsung); mail-catcher lingkungan uji untuk membaca kode OTP 6 digit; reCAPTCHA mode uji.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-045`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-OTP-158: `Joko Kartika` (`jokokartika+{runId}-045@qwertysystem.net`), profil POLICY (seperti profil BASE, yaitu Activated, Active ON, sudah login web di device uji dalam 30 hari terakhir, tetapi Principal sudah mempublish versi Privacy Policy yang lebih baru dari versi yang terakhir disetujui user; hanya Agreement terpicu)
  - TC-AUTH-OTP-159: `Anisa Firmansyah` (`anisafirmansyah+{runId}-045@qwertysystem.net`), profil NEWDEV (seperti BASE, tetapi login dari browser atau device yang belum dikenali; Authenticator sudah terdaftar; hanya MFA terpicu)
- Konfigurasi: akun Principal di atas menerbitkan versi Privacy Policy terbaru sebelum `Joko Kartika` di-seed (hook `before`). Urutan hook `before`: Principal lebih dulu menerbitkan versi Privacy Policy, lalu user profil POLICY di-seed dengan persetujuan versi sebelumnya dan user profil NEWDEV (seperti BASE) di-seed dengan persetujuan versi terbaru. Versi yang diterbitkan adalah state global yang tidak ditarik kembali oleh hook `after`; suite berjalan serial (`parallel: false`).
- Tanpa login pada semua langkah uji: halaman Login with OTP adalah halaman publik, tidak ada sesi aktif di browser. Browser uji tidak dikenali sebagai device `Anisa Firmansyah` (Authenticator sudah terdaftar tetapi device baru).

## Test Steps

### TC-AUTH-OTP-158: Sesi penuh tidak terbentuk sebelum Agreement dikonfirmasi

1. Buka jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
2. Ketik `jokokartika+{runId}-045@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Ketik 6 digit kode OTP dari email pada kotak digit
6. Pada tab lain di jendela privat yang sama, buka Portal — Product Hub langsung
7. Verifikasi Portal — Product Hub tidak terbuka
8. Verifikasi browser dialihkan ke halaman login
9. Kembali ke tab pertama
10. Verifikasi layar Confirm to Continue dengan Title "Confirm to Continue" tetap tampil pada tab pertama
11. Tutup jendela privat

### TC-AUTH-OTP-159: Sesi penuh tidak terbentuk sebelum MFA selesai

12. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
13. Ketik `anisafirmansyah+{runId}-045@qwertysystem.net` pada field Email
14. Centang widget reCAPTCHA "I'm not a robot"
15. Klik button [Request OTP]
16. Ketik 6 digit kode OTP dari email pada kotak digit
17. Pada tab lain di jendela privat yang sama, buka Portal — Product Hub langsung
18. Verifikasi Portal — Product Hub tidak terbuka
19. Verifikasi browser dialihkan ke halaman login
20. Kembali ke tab pertama
21. Verifikasi halaman MFA `Enter authenticator code` tetap tampil pada tab pertama

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Kelas harness a (defense-in-depth: bypass gate sisi server). Spec ini 21 langkah.
- Langkah penghubung (S-03): berpindah antar tab, menutup jendela privat, dan membuka jendela privat baru ditulis sebagai aksi tanpa `Verifikasi`. Post Condition "tidak ada sesi aktif" tidak diasersi sebagai langkah tersendiri (S-01); padanannya adalah Expected a (Portal — Product Hub tidak terbuka dan dialihkan ke halaman login) pada langkah 7 dan 8 untuk TC-AUTH-OTP-158 serta 18 dan 19 untuk TC-AUTH-OTP-159; TC tidak menyebut cara lain memeriksa sesi.
- Layar Confirm to Continue dan halaman MFA pada Expected hanya diperiksa sebatas judul yang tertulis di TC; detail layar diasersi di spec screening dan handoff MFA.
- Temuan untuk QA: (1) Post Condition TC-AUTH-OTP-158 dan 159 ("tidak ada sesi aktif") tidak punya langkah pemeriksaan sendiri di TC; spec tidak mengasersinya terpisah dan hanya mengasersi Expected a (pengalihan ke halaman login pada tab kedua), yang menjadi padanannya. (2) TC-AUTH-OTP-159 tidak menyebut cara menyiapkan device baru untuk profil NEWDEV (browser atau profil yang belum dikenali); spec menyerahkannya ke seeding hook dan jendela privat baru.
