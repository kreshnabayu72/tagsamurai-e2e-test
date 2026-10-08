---
id: TC-AUTH-MFA-E2E-004-screening-enrollment-authenticator
title: "Screening Halaman Enrollment Authenticator, Elemen Tiga Langkah, dan Navigasi Cancel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-07
  - TC-AUTH-MFA-16
  - TC-AUTH-MFA-58
  - TC-AUTH-MFA-113
  - TC-AUTH-MFA-114
  - TC-AUTH-MFA-115
  - TC-AUTH-MFA-116
coverage:
  web: automated
---
# Screening Halaman Enrollment Authenticator, Elemen Tiga Langkah, dan Navigasi Cancel

## Prerequisites

- Browser dalam keadaan publik (tanpa sesi aktif / belum login).
- User `Agus Setiawan` (`agussetiawan@qwertysystem.net`) profil FIRST (belum enroll Authenticator).
- User `Yuni Astuti` (`yuniastuti@qwertysystem.net`) profil FIRST.
- User `Joko Susilo` (`jokosusilo@qwertysystem.net`) profil FIRST.
- Environment web uji siap menerima akses publik pada rute `/login` dan `/login/otp`.

## Test Steps

### Screening elemen UI halaman Enrollment Authenticator

1. Buka halaman `Auth > Login with Password` (`/login`) di browser
2. Ketik `agussetiawan@qwertysystem.net` pada field Email dan masukkan password valid
3. Centang widget reCAPTCHA dan klik button [Log in]
4. Pada halaman Choose Verification Method, pilih opsi "Authenticator app" lalu klik button [Login]
5. Verifikasi halaman berpindah ke `Auth > MFA > Enrollment Authenticator` (`/auth/mfa/enroll`)
6. Verifikasi title halaman adalah "Set up authenticator app"
7. Verifikasi subtitle adalah "Secure your account with an authenticator app. You only need to scan the QR code once — after that, just enter the 6-digit code from the app whenever you're asked to verify."
8. Verifikasi Step 1 menampilkan heading "Download an authenticator app" dan teks instruksi rekomendasi aplikasi (Google Authenticator / Authy)
9. Verifikasi Step 2 menampilkan heading "Scan the QR code or copy the key"
10. Verifikasi image QR code dirender di bagian tengah dengan jelas
11. Verifikasi string secret key tampil dalam font monospace dengan spasi pemisah per 4 karakter
12. Verifikasi tombol CopyButton [Copy key] tampil di samping secret key
13. Verifikasi Step 3 menampilkan heading "Enter the 6-digit code" dan 6 kotak input SegmentedInput kosong
14. Verifikasi footer actions menampilkan button Text [Cancel] (severity contrast) dan button [Verify] (variant solid, severity primary)
15. Verifikasi semua Step 1, 2, dan 3 tampil sekaligus dalam satu card (tanpa stepper terpisah)

### Penolakan auto-submit pada digit ke-6 form Enrollment

16. Pada kotak digit Step 3, ketik berturut-turut 6 digit sembarang `1`, `2`, `3`, `4`, `5`, `6`
17. Verifikasi form TIDAK melakukan submit otomatis saat digit ke-6 terisi
18. Verifikasi tombol [Verify] tetap siap menerima klik manual pengguna

### Navigasi tombol [Cancel] kembali ke layar sebelumnya

19. Klik button Text [Cancel]
20. Verifikasi browser kembali ke halaman `Auth > MFA > Choose Verification Method`
21. Pilih kembali opsi "Authenticator app" dan klik [Login]
22. Verifikasi halaman Enrollment Authenticator terbuka kembali dan enrollment tetap belum aktif
23. Buka sesi baru dengan login via OTP untuk user `jokosusilo@qwertysystem.net` (faktor-1 OTP, belum enroll)
24. Verifikasi halaman langsung mendarat di Enrollment Authenticator
25. Klik button Text [Cancel] pada alur faktor-1 OTP ini
26. Verifikasi browser kembali ke halaman utama Login with OTP (`/login/otp`)

### Aksesibilitas keyboard (a11y) Tab navigation

27. Buka kembali halaman Enrollment Authenticator untuk user `yuniastuti@qwertysystem.net`
28. Tekan tombol Tab berulang kali dari awal card
29. Verifikasi urutan fokus keyboard: tombol [Copy key] → kotak digit 1 s.d. 6 → button Text [Cancel] → button [Verify]

## Notes

- Sesuai PRD §4.2, tombol aksi utama pada halaman enrollment menggunakan label `[Verify]` (bukan [Login] atau [Submit]).
- Tombol Cancel mengembalikan user ke Choose Verification Method (jika faktor-1 Password) atau ke halaman Login (jika faktor-1 OTP).
