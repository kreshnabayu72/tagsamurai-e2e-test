---
id: TC-AUTH-ACT-E2E-009-activation-success-and-navigation
title: "Aktivasi Berhasil, Halaman Activation Success, dan Navigasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-63
  - TC-AUTH-ACT-65
  - TC-AUTH-ACT-70
  - TC-AUTH-ACT-71
  - TC-AUTH-ACT-73
  - TC-AUTH-ACT-74
  - TC-AUTH-ACT-75
  - TC-AUTH-ACT-76
  - TC-AUTH-ACT-77
coverage:
  web: automated
---

# Aktivasi Berhasil, Halaman Activation Success, dan Navigasi

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
- TC-AUTH-ACT-73: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-73: User `Teguh Puspita` (`teguhpuspita+{runId}-009@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-73 data: Password dan Confirm Password: nilai `Spectra.env.ACT_PASSWORD`
- TC-AUTH-ACT-74: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-74: User `Laras Hidayat` (`larashidayat+{runId}-009@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-74 data: Password dan Confirm Password: nilai `Spectra.env.ACT_PASSWORD`
- TC-AUTH-ACT-75: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-75: User `Ilham Ramadhan` (`ilhamramadhan+{runId}-009@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-75 data: Password dan Confirm Password: nilai `Spectra.env.ACT_PASSWORD`
- TC-AUTH-ACT-76: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-76: User `Wulan Mulyadi` (`wulanmulyadi+{runId}-009@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-76 data: Password dan Confirm Password: nilai `Spectra.env.ACT_PASSWORD`
- TC-AUTH-ACT-77: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-77: User `Darma Wulandari` (`darmawulandari+{runId}-009@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-77 data: Password dan Confirm Password: nilai `Spectra.env.ACT_PASSWORD`

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
10. Verifikasi user `Wahyu Maharani` tidak lagi ditolak karena belum aktivasi

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

### TC-AUTH-ACT-73: Screening halaman Activation Success

30. Buka jendela privat baru (tanpa sesi login)
31. Buka link aktivasi user `Teguh Puspita` di browser → halaman `Auth > Account Activation > Set Password` tampil
32. Ketik nilai `Spectra.env.ACT_PASSWORD` di field Password dan field Confirm Password
33. Klik button "Set Password"
34. Susuri halaman Activation Success dari atas ke bawah tanpa klik apa pun
35. Verifikasi **Header**: Card (Elevated) single-column di tengah layar; ilustrasi sukses (success illustration) di atas
36. Verifikasi **Body**: Title "Account Activated"; Body "Your account is now active. You can log in with your new password."
37. Verifikasi **Footer**: CTA "Go to Login" enabled di dalam EmptyState; tidak ada aksi lain di halaman
38. Verifikasi Status user `Teguh Puspita` Activated dan token Consumed

### TC-AUTH-ACT-74: Klik Go to Login pada halaman sukses menuju Login with Password

39. Buka jendela privat baru (tanpa sesi login)
40. Buka link aktivasi user `Laras Hidayat` di browser → halaman `Auth > Account Activation > Set Password` tampil
41. Ketik nilai `Spectra.env.ACT_PASSWORD` di field Password dan field Confirm Password
42. Klik button "Set Password"
43. Klik CTA "Go to Login"
44. Verifikasi halaman Login with Password tampil
45. Verifikasi Tidak ada pemeriksaan atau pesan terkait sesi lain pada transisi
46. Verifikasi Status user `Laras Hidayat` Activated dan token Consumed

### TC-AUTH-ACT-75: Reload halaman Activation Success mengarahkan ke halaman Login

47. Buka jendela privat baru (tanpa sesi login)
48. Buka link aktivasi user `Ilham Ramadhan` di browser → halaman `Auth > Account Activation > Set Password` tampil
49. Ketik nilai `Spectra.env.ACT_PASSWORD` di field Password dan field Confirm Password
50. Klik button "Set Password"
51. Reload halaman Activation Success (F5)
52. Verifikasi Halaman Login tampil; halaman Activation Success tidak tampil kembali
53. Verifikasi Status user `Ilham Ramadhan` Activated dan token Consumed

### TC-AUTH-ACT-76: Tombol Back browser tidak membuka kembali halaman Activation Success

54. Buka jendela privat baru (tanpa sesi login)
55. Buka link aktivasi user `Wulan Mulyadi` di browser → halaman `Auth > Account Activation > Set Password` tampil
56. Ketik nilai `Spectra.env.ACT_PASSWORD` di field Password dan field Confirm Password
57. Klik button "Set Password"
58. Klik CTA "Go to Login" → halaman Login with Password tampil
59. Tekan tombol Back browser
60. Verifikasi Halaman Login tampil; halaman Activation Success tidak tampil kembali
61. Verifikasi Status user `Wulan Mulyadi` Activated dan token Consumed

### TC-AUTH-ACT-77: Akses langsung ke URL halaman Activation Success mengarahkan ke halaman Login

62. Buka jendela privat baru (tanpa sesi login)
63. Buka link aktivasi user `Darma Wulandari` di browser → halaman `Auth > Account Activation > Set Password` tampil
64. Ketik nilai `Spectra.env.ACT_PASSWORD` di field Password dan field Confirm Password
65. Klik button "Set Password"
66. Salin URL halaman Activation Success dari address bar
67. Tempel URL tersebut di tab baru dan buka
68. Verifikasi Halaman Login tampil di tab baru; halaman Activation Success tidak tampil
69. Verifikasi Status user `Darma Wulandari` Activated dan token Consumed

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Nilai batas (72 karakter, karakter spesial) ditempel ke aktivasi user terpisah supaya penyebab kegagalan jelas.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-AUTH-ACT-64 (respons submit ditahan 5 detik) diuji di spec `TC-AUTH-ACT-E2E-028-resilience-set-password-submit` karena butuh `Spectra.intercept` (kelas b, FE+BE dengan intercept parsial).
- TC-AUTH-ACT-74 terbagi lintas spec: asersi "tidak ada pencatatan dari Auth" (Post Condition) diuji di spec `TC-AUTH-ACT-E2E-017-zero-logging-absence` (kelas g, prinsip 10).
