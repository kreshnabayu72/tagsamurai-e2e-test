---
id: TC-AUTH-MFA-E2E-021-enrollment-authenticator-lengkap
title: "Enrollment Authenticator Lengkap: Setup QR/Secret Manual, Verifikasi Kode, dan Login Final"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-11
  - TC-AUTH-MFA-106
  - TC-AUTH-MFA-107
  - TC-AUTH-MFA-108
  - TC-AUTH-MFA-121
  - TC-AUTH-MFA-122
coverage:
  web: automated
---
# Enrollment Authenticator Lengkap: Setup QR/Secret Manual, Verifikasi Kode, dan Login Final

## Prerequisites

- Browser dalam keadaan publik (tanpa sesi aktif).
- User `Dimas Prakoso` (`dimasprakoso@qwertysystem.net`) profil FIRST (belum enroll).
- User `Bayu Rahmawati` (`bayurahmawati@qwertysystem.net`) profil FIRST (belum enroll).
- User `Wulan Rahmawati` (`wulanrahmawati@qwertysystem.net`) profil FIRST (belum enroll).
- Aplikasi authenticator uji dengan kemampuan pendaftaran via QR dan secret key manual.

## Test Steps

### Setup via scan QR code, verifikasi kode, dan transisi ke login final

1. Buka halaman `Auth > Login with Password` (`/login`), login dengan kredensial `dimasprakoso@qwertysystem.net`
2. Pada Choose Verification Method, pilih "Authenticator app" lalu klik [Login]
3. Verifikasi halaman Enrollment Authenticator tampil
4. Pindai QR code menggunakan aplikasi authenticator uji
5. Ambil 6 digit kode verifikasi yang dihasilkan aplikasi
6. Masukkan kode tersebut pada kotak digit Step 3
7. Klik button [Verify]
8. Verifikasi button [Verify] sempat berstatus Submitting (disabled dengan spinner)
9. Verifikasi sistem menyelesaikan aktivasi enrollment dan LANGSUNG mengalihkan browser ke Portal — Product Hub
10. Verifikasi saat mendarat di Portal — Product Hub, toast sukses tampil di pojok layar: "Success, authenticator app has been added." (sesuai PRD §7 T-02)

### Pendaftaran berikutnya membuka Authenticator Verification (bukan Enrollment)

11. Lakukan logout dari Portal — Product Hub
12. Login kembali menggunakan user `dimasprakoso@qwertysystem.net` dari browser uji baru
13. Pilih opsi "Authenticator app" pada Choose Verification Method
14. Verifikasi halaman yang terbuka adalah `Auth > MFA > Authenticator Verification` (bukan halaman Enrollment) karena enrollment sudah aktif permanen

### Pendaftaran alternatif via Secret Key yang disalin (Copy key manual)

15. Buka sesi baru untuk user `bayurahmawati@qwertysystem.net` hingga mencapai halaman Enrollment
16. Klik tombol [Copy key]
17. Verifikasi string secret key tersalin ke clipboard
18. Masukkan secret key tersebut secara manual ke aplikasi authenticator uji
19. Salin 6 digit kode dari aplikasi authenticator dan tempelkan (Ctrl+V) ke kotak input Step 3
20. Verifikasi keenam kotak terisi rapi tanpa auto-submit
21. Klik button [Verify] dan verifikasi login final berhasil ke Portal — Product Hub

### Transisi pasca Login with OTP langsung mengaktifkan enrollment

22. Buka sesi baru dengan login via OTP untuk user `wulanrahmawati@qwertysystem.net` (belum enroll)
23. Setelah OTP lolos, verifikasi halaman langsung membuka Enrollment Authenticator
24. Masukkan kode verifikasi valid dari authenticator dan klik [Verify]
25. Verifikasi pendaftaran berhasil dan browser mendarat di Portal — Product Hub dengan toast T-02

## Notes

- Sesuai PRD §4.2, pendaftaran authenticator tidak memiliki layar konfirmasi perantara; setelah kode setup diverifikasi benar, user langsung dialihkan ke Portal dengan toast konfirmasi `"Success, authenticator app has been added."`.
- Tidak ada recovery codes yang dibuat atau ditawarkan pada alur ini (§10 Constraints).
