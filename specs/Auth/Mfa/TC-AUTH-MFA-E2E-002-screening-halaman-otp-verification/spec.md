---
id: TC-AUTH-MFA-E2E-002-screening-halaman-otp-verification
title: "Screening Halaman OTP Verification, Navigasi Kursor, dan Accessibility"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-04
  - TC-AUTH-MFA-14
  - TC-AUTH-MFA-56
  - TC-AUTH-MFA-65
  - TC-AUTH-MFA-67
  - TC-AUTH-MFA-87
coverage:
  web: automated
---
# Screening Halaman OTP Verification, Navigasi Kursor, dan Accessibility

## Prerequisites

- Browser dalam keadaan publik (tanpa sesi aktif / belum login).
- User `Dewi Lestari` (`dewilestari@qwertysystem.net`) profil FIRST.
- User `Lina Marlina` (`linamarlina@qwertysystem.net`) profil FIRST.
- User `Galih Saputro` (`galihsaputro@qwertysystem.net`) profil NEWDEV.
- Environment web uji siap menerima akses publik pada rute `/login` dan `/auth/mfa`.

## Test Steps

### Screening elemen UI halaman OTP Verification (MFA)

1. Buka halaman `Auth > Login with Password` (`/login`) di browser
2. Ketik `dewilestari@qwertysystem.net` pada field Email dan masukkan password valid
3. Centang widget reCAPTCHA dan klik button [Log in]
4. Pada halaman Choose Verification Method, pilih opsi "OTP via email" lalu klik button [Login]
5. Verifikasi halaman berpindah ke `Auth > MFA > OTP Verification`
6. Verifikasi card form tampil terpusat dengan logo TAG Samurai di bagian atas
7. Verifikasi title halaman adalah "Enter verification code"
8. Verifikasi subtitle halaman adalah "We sent a code to dewilestari@qwertysystem.net" (email tidak di-mask, sesuai NC-11)
9. Verifikasi 6 kotak input SegmentedInput tampil dalam keadaan kosong dengan fokus otomatis pada kotak 1
10. Verifikasi tombol Resend tampil dalam keadaan disabled dengan hitung mundur di dalam label ("Resend code in 59s" atau "Resend code in 60s")
11. Verifikasi button [Login] tampil (variant solid, severity primary)
12. Verifikasi button Text [Use a different method] tampil terpusat di bawah tombol [Login]
13. Verifikasi tidak ada tautan [Edit email] di halaman OTP Verification MFA

### Navigasi kursor otomatis dan fungsi tombol Backspace

14. Pada kotak input 1, ketik digit `1`
15. Verifikasi kotak 1 terisi `1` dan fokus kursor berpindah otomatis ke kotak 2
16. Ketik digit `2` pada kotak 2 dan verifikasi fokus berpindah otomatis ke kotak 3
17. Ketik digit `3` pada kotak 3 dan verifikasi fokus berpindah otomatis ke kotak 4
18. Tekan tombol Backspace satu kali saat berada di kotak 4 (kotak 4 masih kosong)
19. Verifikasi fokus berpindah kembali ke kotak 3 dan kotak 3 dikosongkan (angka `3` terhapus)
20. Tekan tombol Backspace lagi dan verifikasi fokus berpindah ke kotak 2 dan kotak 2 dikosongkan

### Aksesibilitas keyboard (a11y) dengan tombol Tab

21. Buka halaman OTP Verification untuk user `linamarlina@qwertysystem.net`
22. Tekan tombol Tab berulang kali dari awal dokumen
23. Verifikasi urutan fokus keyboard berpindah secara sekuensial: kotak 1 → kotak 2 → kotak 3 → kotak 4 → kotak 5 → kotak 6 → tombol Resend (saat enabled) → button [Login] → button Text [Use a different method]

### Navigasi tombol [Use a different method] kembali ke Choose Verification Method

24. Klik button Text [Use a different method]
25. Verifikasi halaman kembali ke `Auth > MFA > Choose Verification Method`
26. Verifikasi tidak ada opsi yang terpilih dan button [Login] disabled (kembali ke default §9.5)
27. Verifikasi sesi pre-auth MFA tetap aktif dan kode OTP faktor-2 yang terkirim masih berlaku

## Notes

- Sesuai konsensus NC-11, teks subtitle adalah `We sent a code to {email}`.
- Sesuai PRD §4.1 S-AUTHMFA-02, halaman OTP faktor-2 tidak memiliki tautan "Edit email" karena email penerima selalu email akun terdaftar.
- Navigasi Backspace mundur dari kotak kosong mengosongkan kotak sebelumnya dan memindahkan fokus ke kotak tersebut.
