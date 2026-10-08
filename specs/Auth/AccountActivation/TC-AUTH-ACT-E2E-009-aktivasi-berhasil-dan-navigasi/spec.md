---
id: TC-AUTH-ACT-E2E-009-aktivasi-berhasil-dan-navigasi
title: "Aktivasi Berhasil dengan Password Valid dan Nilai Batas"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-63
  - TC-AUTH-ACT-65
  - TC-AUTH-ACT-70
  - TC-AUTH-ACT-71
coverage:
  web: automated
---

# Aktivasi Berhasil dengan Password Valid dan Nilai Batas

## Prerequisites

- Seeding: setiap user Pending Activation dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`). Link aktivasi (token Active) diambil dari respons seeding API. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}` (contoh `budiaditya+{runId}-009@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`, `ACT_PASSWORD`, `ACT_PASSWORD_72`, `ACT_PASSWORD_SPECIAL`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: pemantauan request jaringan; jendela privat untuk konteks akun aktor; reload halaman (F5); tombol Back browser; menyalin URL dari address bar dan membukanya di tab baru; reCAPTCHA mode uji di environment.
- TC-AUTH-ACT-63: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-63: User `Wahyu Maharani` (`wahyumaharani+{runId}-009@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-63 data: Password dan Confirm Password: nilai `Spectra.env.ACT_PASSWORD`
- TC-AUTH-ACT-65: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-65: User `Joko Octaviani` (`jokooctaviani+{runId}-009@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-65 data: Password dan Confirm Password: nilai `Spectra.env.ACT_PASSWORD`
- TC-AUTH-ACT-70: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-70: User `Citra Cahyani` (`citracahyani+{runId}-009@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-70 data: Password dan Confirm Password: nilai `Spectra.env.ACT_PASSWORD_72` (tepat 72 karakter, memenuhi seluruh Password Policy)
- TC-AUTH-ACT-71: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-71: User `Reza Rahmawati` (`rezarahmawati+{runId}-009@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-71 data: Password dan Confirm Password: nilai `Spectra.env.ACT_PASSWORD_SPECIAL` (memuat karakter spesial `!@?&` dan memenuhi seluruh Password Policy)

## Test Steps

### TC-AUTH-ACT-63: Set Password dengan password valid mengaktifkan akun dan menampilkan halaman Activation Success

1. Buka link aktivasi user `Wahyu Maharani` di browser → halaman `Auth > Account Activation > Set Password` tampil
2. Ketik nilai `Spectra.env.ACT_PASSWORD` di field Password dan field Confirm Password
3. Klik button "Set Password"
4. Verifikasi `Auth > Account Activation > Activation Success` tampil dengan Title "Account Activated", Body "Your account is now active. You can log in with your new password.", dan CTA "Go to Login"
5. Verifikasi Tidak ada toast pada transisi ke halaman Activation Success
6. Verifikasi Token aktivasi user `Wahyu Maharani` berstatus Consumed dan status user `Wahyu Maharani` Activated
7. Ganti akun: buka jendela privat baru, login sebagai akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` dan selesaikan reCAPTCHA, lalu buka `Global Settings > User`
8. Verifikasi badge Pending Activation user `Wahyu Maharani` hilang di `Global Settings > User`
9. Ganti akun: logout dari akun aktor, buka `Auth > Login`, lalu login dengan email `wahyumaharani+{runId}-009@qwertysystem.net` dan password nilai `Spectra.env.ACT_PASSWORD`, selesaikan reCAPTCHA, lalu klik [Log in]
10. Verifikasi Pesan "Your account has not been activated" tidak tampil dan halaman `Auth > Login > Login with Password` ditinggalkan (user diarahkan ke Confirm Agreement, MFA, atau Portal — Product Hub sesuai konfigurasi akun)

### TC-AUTH-ACT-65: Klik ganda cepat pada Set Password hanya memproses satu request

11. Buka jendela privat baru (tanpa sesi login)
12. Buka link aktivasi user `Joko Octaviani` di browser → halaman `Auth > Account Activation > Set Password` tampil
13. Ketik nilai `Spectra.env.ACT_PASSWORD` di field Password dan field Confirm Password
14. Pantau request jaringan, lalu klik button "Set Password" dua kali dengan cepat
15. Verifikasi Hanya satu request set password yang dikirim ke server
16. Verifikasi `Auth > Account Activation > Activation Success` tampil satu kali tanpa pesan error atau halaman Invalid Link
17. Verifikasi Token aktivasi user `Joko Octaviani` Consumed dan status user Activated (satu kali)

### TC-AUTH-ACT-70: Password tepat 72 karakter diterima dan mengaktifkan akun

18. Buka jendela privat baru (tanpa sesi login)
19. Buka link aktivasi user `Citra Cahyani` di browser → halaman `Auth > Account Activation > Set Password` tampil
20. Ketik nilai `Spectra.env.ACT_PASSWORD_72` (tepat 72 karakter) di field Password dan field Confirm Password
21. Klik button "Set Password"
22. Verifikasi `Auth > Account Activation > Activation Success` tampil dengan Title "Account Activated", Body "Your account is now active. You can log in with your new password.", dan CTA "Go to Login"
23. Verifikasi Status user `Citra Cahyani` Activated dan token Consumed

### TC-AUTH-ACT-71: Password berisi karakter spesial `!@?&` diterima dan mengaktifkan akun

24. Buka jendela privat baru (tanpa sesi login)
25. Buka link aktivasi user `Reza Rahmawati` di browser → halaman `Auth > Account Activation > Set Password` tampil
26. Ketik nilai `Spectra.env.ACT_PASSWORD_SPECIAL` di field Password dan field Confirm Password
27. Klik button "Set Password"
28. Verifikasi `Auth > Account Activation > Activation Success` tampil dengan Title "Account Activated", Body "Your account is now active. You can log in with your new password.", dan CTA "Go to Login"
29. Verifikasi Status user `Reza Rahmawati` Activated dan token Consumed

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Nilai batas (72 karakter, karakter spesial) ditempel ke aktivasi user terpisah supaya penyebab kegagalan jelas.
- Halaman Activation Success dan navigasi sesudahnya (TC-AUTH-ACT-73 sampai 77) dipisah ke `TC-AUTH-ACT-E2E-032-halaman-activation-success-dan-navigasi` supaya spec ini fokus ke proses aktivasi.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-AUTH-ACT-64 (respons submit ditahan 5 detik) diuji di spec `TC-AUTH-ACT-E2E-028-ketahanan-submit-set-password` karena butuh `Spectra.intercept` (kelas b, FE+BE dengan intercept parsial).
