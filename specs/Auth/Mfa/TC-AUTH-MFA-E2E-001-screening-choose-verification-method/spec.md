---
id: TC-AUTH-MFA-E2E-001-screening-choose-verification-method
title: "Screening dan Interaksi Halaman Choose Verification Method"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-01
  - TC-AUTH-MFA-02
  - TC-AUTH-MFA-03
  - TC-AUTH-MFA-13
  - TC-AUTH-MFA-53
  - TC-AUTH-MFA-59
  - TC-AUTH-MFA-60
  - TC-AUTH-MFA-61
coverage:
  web: automated
---
# Screening dan Interaksi Halaman Choose Verification Method

## Prerequisites

- Browser dalam keadaan publik (tanpa sesi aktif / belum login).
- User `Budi Santoso` (`budisantoso@qwertysystem.net`) profil FIRST (login pertama kali).
- User `Siti Rahmawati` (`sitirahmawati@qwertysystem.net`) profil FIRST.
- User `Andi Wijaya` (`andiwijaya@qwertysystem.net`) profil FIRST.
- User `Hendra Gunawan` (`hendragunawan@qwertysystem.net`) profil FIRST.
- User `Ika Purwanti` (`ikapurwanti@qwertysystem.net`) profil NEWDEV.
- User `Tika Amelia` (`tikaamelia@qwertysystem.net`) profil IDLE (idle ≥30 hari).
- User `Arif Budiman` (`arifbudiman@qwertysystem.net`) profil NEWDEVE (login tak biasa).
- Environment web uji siap menerima akses publik pada rute `/login` dan `/auth/mfa`.

## Test Steps

### Screening elemen UI halaman Choose Verification Method

1. Buka halaman `Auth > Login with Password` (`/login`) di browser
2. Ketik `budisantoso@qwertysystem.net` pada field Email dan masukkan password valid
3. Centang widget reCAPTCHA "I'm not a robot" dan klik button [Log in]
4. Verifikasi halaman berpindah ke `Auth > MFA > Choose Verification Method` (`/auth/mfa`)
5. Verifikasi card form tampil terpusat di layar dengan logo TAG Samurai
6. Verifikasi title halaman adalah "Choose verification method"
7. Verifikasi subtitle halaman adalah "Select how you'd like to verify your identity"
8. Verifikasi Option Card 1 menampilkan icon `MailLine`, title "OTP via email", dan description "We'll send a 6-digit code to your email"
9. Verifikasi Option Card 2 menampilkan icon `ShieldUserLine`, title "Authenticator app", dan description "Use code from Google or Microsoft Authenticator"
10. Verifikasi kedua opsi dalam keadaan tidak terpilih secara default
11. Verifikasi button [Login] tampil melebar penuh (variant solid, severity primary) dalam keadaan disabled

### Interaksi pemilihan opsi dan validasi button disabled

12. Klik radio button / card opsi "OTP via email"
13. Verifikasi Option Card 1 terpilih dan button [Login] berubah status menjadi enabled
14. Klik radio button / card opsi "Authenticator app"
15. Verifikasi Option Card 2 terpilih dan Option Card 1 otomatis menjadi tidak terpilih (hanya tepat satu opsi yang dapat dipilih)
16. Verifikasi button [Login] tetap dalam keadaan enabled

### Aksesibilitas keyboard (a11y) dengan tombol Tab

17. Buka halaman Choose Verification Method untuk user `hendragunawan@qwertysystem.net`
18. Tekan tombol Tab berulang kali dari awal dokumen
19. Verifikasi fokus keyboard berpindah secara berurutan: Option Card 1 ("OTP via email") → Option Card 2 ("Authenticator app") → button [Login]
20. Tekan tombol Space saat fokus berada di Option Card 1 dan verifikasi opsi tersebut terpilih serta button [Login] menjadi enabled

### Keseragaman tampilan Choose Verification Method lintas alasan MFA

21. Login dengan user `tikaamelia@qwertysystem.net` (alasan MFA: idle ≥30 hari) hingga mencapai halaman Choose Verification Method
22. Verifikasi elemen UI, opsi yang tersedia (OTP via email dan Authenticator app), serta CTA [Login] identik tanpa perbedaan tata letak
23. Login dengan user `arifbudiman@qwertysystem.net` (alasan MFA: login tak biasa / unusual login) hingga mencapai halaman Choose Verification Method
24. Verifikasi elemen UI, opsi yang tersedia, serta CTA [Login] tetap identik tanpa perbedaan tata letak
25. Verifikasi label CTA pada tombol submit adalah "Login" (seragam untuk login pertama maupun login berikutnya)

## Notes

- Modul MFA adalah modul publik pra-autentikasi (tanpa role gate).
- Alasan MFA bersifat informational untuk server dan email alert; antarmuka Choose Verification Method selalu menyajikan opsi seragam.
- Sesuai PRD §4.2, button CTA menggunakan label "Login" (bukan [Submit] atau [Continue]).
