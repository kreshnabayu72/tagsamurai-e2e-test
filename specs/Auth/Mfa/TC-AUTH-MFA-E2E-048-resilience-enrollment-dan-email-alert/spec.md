---
id: TC-AUTH-MFA-E2E-048-resilience-enrollment-dan-email-alert
title: "Resilience Kegagalan Verifikasi Enrollment dan Pengiriman Email Alert"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-120
  - TC-AUTH-MFA-156
  - TC-AUTH-MFA-157
coverage:
  web: automated
---

# Resilience Kegagalan Verifikasi Enrollment dan Pengiriman Email Alert

## Prerequisites

- Mode: FE+BE (backend nyata; sebagian respons dipaksa lewat `Spectra.intercept()`, bukan seluruh API di-mock).
- Suite berjalan serial (`parallel: false`) karena spec ini mematikan email service untuk alert di lingkungan uji (TC-AUTH-MFA-156); hook `after` menyalakan kembali email service untuk alert.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`), password user `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-120: `Oscar Mahesa` (`oscarmahesa+{runId}-048@qwertysystem.net`), profil FIRST (Tabel Data Uji Pre-setup #3: Activated, Active ON, belum pernah login di platform mana pun, Authenticator belum terdaftar).
  - TC-AUTH-MFA-157: `Doni Kurniadi` (`donikurniadi+{runId}-048@qwertysystem.net`), profil NEWDEVE (Tabel Data Uji Pre-setup #5: Activated, Active ON, device browser uji B belum ada di daftar trusted device, Authenticator sudah terdaftar dengan secret yang dikenali aplikasi authenticator uji).
  - TC-AUTH-MFA-156: `Winda Prameswari` (`windaprameswari+{runId}-048@qwertysystem.net`), profil NEWDEVE.
- Hook `after`: lepas semua aturan intercept yang masih aktif, nyalakan kembali email service untuk alert di lingkungan uji (TC-AUTH-MFA-156), lalu hapus ketiga user. Hook ini tetap jalan walau spec gagal di tengah dan pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk ketiga TC. Tiap TC dimulai di jendela baru tanpa sesi login: jendela baru browser uji A (konteks bersih) untuk TC-AUTH-MFA-120, jendela privat baru browser uji B (ID device belum dikenali) untuk TC-AUTH-MFA-157 dan TC-AUTH-MFA-156.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - `Spectra.intercept()` parsial atas backend nyata: respons HTTP 500 menggantikan respons `POST /v2/iam/auth/mfa/authenticator/enroll/verify` (request tidak diteruskan ke backend, TC-AUTH-MFA-120); respons backend untuk request faktor-1 `POST /v2/iam/auth/login` ditahan sampai melewati batas timeout klien sementara request tetap diteruskan ke backend (TC-AUTH-MFA-157). Nama endpoint `authenticator/enroll/verify` dari `auth/mfa/API/openapi.yaml`; nama endpoint `POST /v2/iam/auth/login` dari `auth/login-password/API/openapi.yaml`.
  - Email service untuk email alert login tak biasa dapat dimatikan dan dinyalakan kembali di lingkungan uji (failure injection di sisi server, tidak dapat di-intercept di browser) tanpa memengaruhi jalur OTP faktor-2 (TC-AUTH-MFA-156). Pemulihan: dinyalakan kembali di langkah terakhir TC-AUTH-MFA-156 dan di hook `after`.
  - Mail-catcher lingkungan uji untuk membaca email OTP faktor-2 dan menghitung email alert login tak biasa.
  - Aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) untuk memindai QR code Enrollment dan menghasilkan kode (TC-AUTH-MFA-120).
  - Seeding state BE per user: profil FIRST yang belum pernah login di platform mana pun (TC-AUTH-MFA-120) dan profil NEWDEVE tanpa ID device browser uji B di daftar trusted device dengan Authenticator terdaftar dengan secret yang dikenal aplikasi authenticator uji (TC-AUTH-MFA-157, 156); mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - Pengamatan toast selama 10 detik dan dismiss toast manual lewat tombol tutup toast.
  - Jeda nyata: pengamatan toast 10 detik (TC-AUTH-MFA-120) dan penahanan respons login sampai timeout klien (TC-AUTH-MFA-157; durasi timeout klien belum didefinisikan di TC, lihat Temuan untuk QA).
  - reCAPTCHA mode uji di environment.
- Pemulihan state global: aturan intercept dilepas dan email service alert dinyalakan kembali di hook `after`. Spec tidak mengubah jam server, geo-IP, atau counter rate limit.

## Test Steps

### TC-AUTH-MFA-120: Verifikasi enrollment gagal 5xx lalu retry menampilkan secret yang sama dan berhasil

1. Di jendela baru browser uji A (konteks bersih, tanpa sesi login), buka halaman `Auth > Login with Password` → halaman Login with Password tampil
2. Ketik `oscarmahesa+{runId}-048@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → layar Confirm to Continue tampil
6. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
7. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
8. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
9. Catat secret key yang tampil pada halaman Enrollment Authenticator
10. Pindai QR code dengan aplikasi authenticator uji
11. Ketik 6 digit kode dari aplikasi authenticator uji pada kotak digit
12. Aktifkan intercept respons 5xx pada verifikasi enrollment (`POST /v2/iam/auth/mfa/authenticator/enroll/verify`), lalu klik button [Verify]
13. Verifikasi Toast error: "Error, failed to log in." tampil
14. Verifikasi Toast tampil di kanan bawah
15. Amati toast selama 10 detik
16. Verifikasi Toast tetap tampil dan tidak hilang otomatis sampai di-dismiss
17. Verifikasi Halaman tetap Enrollment Authenticator
18. Verifikasi QR code yang tampil sama dengan sebelum 5xx
19. Verifikasi Secret key yang tampil sama dengan yang dicatat
20. Verifikasi Enrollment belum aktif (Portal — Product Hub tidak tampil)
21. Verifikasi Keenam kotak digit tetap terisi
22. Dismiss toast manual
23. Hentikan intercept 5xx dan klik button [Verify] lagi dengan kode yang masih valid
24. Verifikasi Verifikasi berhasil
25. Verifikasi Browser dialihkan ke Portal — Product Hub

### TC-AUTH-MFA-157: Retry setelah timeout pada Login with Password tidak menghasilkan email alert ganda

26. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
27. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
28. Ketik `donikurniadi+{runId}-048@qwertysystem.net` pada field Email
29. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
30. Centang widget reCAPTCHA "I'm not a robot"
31. Catat jumlah email alert login tak biasa di mail-catcher `donikurniadi+{runId}-048@qwertysystem.net` sebagai baseline
32. Aktifkan penahanan respons server pada request faktor-1 (`POST /v2/iam/auth/login`, request tetap diteruskan ke backend), lalu klik button [Log in]
33. Tunggu sampai request timeout
34. Lepas penahanan respons, lalu klik button [Log in] lagi
35. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil setelah retry
36. Buka mail-catcher untuk `donikurniadi+{runId}-048@qwertysystem.net`
37. Verifikasi Tepat satu email alert baru diterima untuk attempt ini (tidak ada email ganda; selisih dari baseline satu email)

### TC-AUTH-MFA-156: Kegagalan pengiriman email alert tidak memblok login

38. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
39. Matikan email service untuk alert di lingkungan uji (failure injection; OTP faktor-2 tetap terkirim lewat jalur OTP)
40. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
41. Ketik `windaprameswari+{runId}-048@qwertysystem.net` pada field Email
42. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
43. Centang widget reCAPTCHA "I'm not a robot"
44. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
45. Verifikasi Halaman Choose Verification Method tampil walau email alert gagal terkirim
46. Pilih opsi "OTP via email" pada halaman Choose Verification Method
47. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `windaprameswari+{runId}-048@qwertysystem.net`
48. Ketik 6 digit kode OTP faktor-2 dari email pada kotak digit
49. Verifikasi Verifikasi OTP berhasil
50. Verifikasi Browser dialihkan ke Portal — Product Hub
51. Verifikasi Sesi web aktif untuk `Winda Prameswari`
52. Nyalakan kembali email service untuk alert di lingkungan uji

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Urutan TC menyimpang dari TC sumber (120, 156, 157): TC-AUTH-MFA-156 dipindah ke akhir karena mematikan email service alert (state global di lingkungan uji) dan dipulihkan pada langkah terakhir serta hook `after` (S-05, S-10).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal tiap TC setelah TC pertama, mencatat secret key, mengamati toast, dismiss toast, melepas intercept, mencatat baseline jumlah email alert, menyalakan kembali email service alert) bukan asersi tambahan (S-03).
- Jumlah langkah 52; langkah prefix login faktor-1 yang identik (langkah 1-6, 27-30, 40-44) tidak dihitung sehingga ±37 langkah, sedikit di atas smell ±35. Ketiga TC independen (user, intercept, dan email service sendiri) dan bagian sesudahnya tetap bermakna bila TC sebelumnya gagal, sehingga spec tidak dipecah.
- Temuan untuk QA: (1) TC-AUTH-MFA-120 butir b menyebut "QR code dan secret key yang sama" tanpa langkah pencatatan secret key sebelum 5xx; spec menambah langkah mencatat secret key. (2) TC-AUTH-MFA-120 tidak menyebut durasi pengamatan "tidak hilang otomatis sampai di-dismiss"; spec memakai 10 detik seperti TC-AUTH-MFA-201. (3) TC-AUTH-MFA-157 tidak menyebut apakah request yang ditahan diteruskan ke backend dan kapan penahanan dilepas; spec meneruskan request ke backend (agar email alert attempt pertama terkirim) dan melepas penahanan sebelum retry. (4) TC-AUTH-MFA-157 langkah 6 ("tahan respons server sampai timeout") tidak mendefinisikan nilai timeout klien; spec menahan sampai timeout klien tercapai dengan jeda nyata yang durasinya belum diketahui. (5) TC-AUTH-MFA-157 Post Condition "satu sesi pre-auth MFA aktif" dan TC-AUTH-MFA-156 Post Condition "pengiriman alert diulang oleh antrean retry" tidak punya cara pengecekan di Langkah Uji dan tidak diasersi. (6) TC-AUTH-MFA-156 butir b Post "satu sesi web aktif" hanya dicek lewat Portal tampil. (7) TC-AUTH-MFA-120 mencantumkan mail-catcher di Precondition tetapi Langkah Uji tidak membaca email. (8) TC-AUTH-MFA-120 Post Condition "Enrollment aktif sekali; tidak ada entri log ganda" tidak punya Expected padanan atau langkah observasi di TC (tidak ada langkah membaca log, dan Precondition tidak mencantumkan akun Total Control) dan tidak diasersi. (9) Mekanisme seeding state BE per user (profil FIRST/NEWDEVE: trusted device, Authenticator dengan secret dikenal) belum ada di Pre-setup TC (#20/#21). (10) TC-AUTH-MFA-120 tidak menyebut browser uji; browser mengikuti profil user (FIRST: browser uji A).
