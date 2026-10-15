---
id: TC-AUTH-MFA-E2E-001-screening-choose-verification-method
title: "Screening Halaman Choose Verification Method"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-01
  - TC-AUTH-MFA-02
  - TC-AUTH-MFA-03
  - TC-AUTH-MFA-13
  - TC-AUTH-MFA-61
coverage:
  web: automated
---

# Screening Halaman Choose Verification Method

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): lima user profil FIRST (Tabel Data Uji Pre-setup #3: Activated, Active ON, belum pernah login di platform mana pun, Authenticator belum terdaftar), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-01: `Budi Santoso` (`budisantoso+{runId}-001@qwertysystem.net`)
  - TC-AUTH-MFA-02: `Siti Rahmawati` (`sitirahmawati+{runId}-001@qwertysystem.net`)
  - TC-AUTH-MFA-03: `Andi Wijaya` (`andiwijaya+{runId}-001@qwertysystem.net`)
  - TC-AUTH-MFA-13: `Hendra Gunawan` (`hendragunawan+{runId}-001@qwertysystem.net`)
  - TC-AUTH-MFA-61: `Novi Ariyanti` (`noviariyanti+{runId}-001@qwertysystem.net`)
- Hook `after`: hapus kelima user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah TC pertama dimulai di jendela privat baru.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: jendela privat; reCAPTCHA mode uji di environment; mail-catcher lingkungan uji untuk memastikan tidak ada email OTP terkirim (TC-AUTH-MFA-02), dengan baseline jumlah email untuk `sitirahmawati+{runId}-001@qwertysystem.net` dicatat sebelum aksi yang diamati; navigasi keyboard (tombol Tab) dan indikator fokus (TC-AUTH-MFA-13).
- Semua user berprofil FIRST, jadi tiap login melewati layar Confirm to Continue sebelum Choose Verification Method.

## Test Steps

### TC-AUTH-MFA-01: Screening halaman Choose Verification Method setelah Login with Password (web)

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `budisantoso+{runId}-001@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → layar Confirm to Continue tampil
6. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
7. Susuri halaman dari atas ke bawah tanpa mengklik apa pun
8. Verifikasi **Header**: Card `Elevated` terpusat di halaman
9. Verifikasi Logo TAG Samurai di bagian atas card
10. Verifikasi Title "Choose verification method"
11. Verifikasi Subtitle "Select how you'd like to verify your identity"
12. Verifikasi **Body**: RadioGroup dua opsi
13. Verifikasi Masing-masing opsi berupa Card yang dapat diklik
14. Verifikasi Belum ada opsi terpilih
15. Verifikasi Opsi 1: ikon MailLine
16. Verifikasi Opsi 1: judul "OTP via email"
17. Verifikasi Opsi 1: deskripsi "We'll send a 6-digit code to your email"
18. Verifikasi Opsi 2: ikon ShieldUserLine
19. Verifikasi Opsi 2: judul "Authenticator app"
20. Verifikasi Opsi 2: deskripsi "Use code from Google or Microsoft Authenticator"
21. Verifikasi Slot alert error di bawah opsi kosong
22. Verifikasi Tidak ada opsi Biometric, SMS, atau push notification
23. Verifikasi **Footer**: Button [Login] full-width (severity primary) tampil
24. Verifikasi Button [Login] berstatus disabled
25. Verifikasi Tidak ada button [Verify], tautan recovery code, dan Breadcrumb

### TC-AUTH-MFA-02: Button [Login] di Choose Verification Method disabled sampai satu opsi dipilih

26. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
27. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
28. Ketik `sitirahmawati+{runId}-001@qwertysystem.net` pada field Email
29. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
30. Centang widget reCAPTCHA "I'm not a robot"
31. Klik button [Log in] → layar Confirm to Continue tampil
32. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
33. Amati button [Login] tanpa memilih opsi
34. Verifikasi Button [Login] disabled
35. Catat jumlah email di mail-catcher untuk `sitirahmawati+{runId}-001@qwertysystem.net` sebagai baseline
36. Klik button [Login] yang disabled
37. Verifikasi Klik pada button tidak memicu aksi apa pun: tidak ada email OTP terkirim (jumlah email sama dengan baseline)
38. Verifikasi Klik pada button tidak memicu aksi apa pun: halaman tidak berpindah (tetap `Auth > MFA > Choose Verification Method`)
39. Klik opsi "OTP via email"
40. Amati button [Login]
41. Verifikasi Opsi "OTP via email" berstatus terpilih
42. Verifikasi Button [Login] enabled

### TC-AUTH-MFA-03: Memilih opsi lain di Choose Verification Method memindahkan pilihan (satu opsi terpilih)

43. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
44. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
45. Ketik `andiwijaya+{runId}-001@qwertysystem.net` pada field Email
46. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
47. Centang widget reCAPTCHA "I'm not a robot"
48. Klik button [Log in] → layar Confirm to Continue tampil
49. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
50. Klik opsi "OTP via email"
51. Verifikasi Hanya "OTP via email" terpilih
52. Verifikasi "Authenticator app" tidak terpilih
53. Verifikasi Button [Login] enabled
54. Klik opsi "Authenticator app"
55. Verifikasi Hanya "Authenticator app" terpilih
56. Verifikasi "OTP via email" tidak terpilih
57. Verifikasi Button [Login] enabled
58. Klik opsi "OTP via email" lagi
59. Verifikasi Hanya "OTP via email" terpilih
60. Verifikasi Button [Login] tetap enabled

### TC-AUTH-MFA-13: Accessibility — seluruh input dan tombol halaman Choose Verification Method dapat dijangkau dengan tombol Tab

61. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
62. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
63. Ketik `hendragunawan+{runId}-001@qwertysystem.net` pada field Email
64. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
65. Centang widget reCAPTCHA "I'm not a robot"
66. Klik button [Log in] → layar Confirm to Continue tampil
67. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
68. Tekan tombol Tab berulang dari awal halaman sampai fokus melewati elemen terakhir
69. Verifikasi Fokus berpindah berurutan melalui: kedua opsi (RadioGroup), lalu button [Login] hanya saat enabled
70. Verifikasi Setiap elemen yang menerima fokus menampilkan indikator fokus yang terlihat

### TC-AUTH-MFA-61: Label CTA halaman verifikasi seragam "Login" untuk login pertama dan login berikutnya

71. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
72. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
73. Ketik `noviariyanti+{runId}-001@qwertysystem.net` pada field Email
74. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
75. Centang widget reCAPTCHA "I'm not a robot"
76. Klik button [Log in] → layar Confirm to Continue tampil
77. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
78. Pilih opsi "OTP via email" pada halaman Choose Verification Method
79. Amati label button pada halaman Choose Verification Method
80. Verifikasi Button pada Choose Verification Method berlabel "Login" (bukan "Continue") pada login pertama
81. Klik button [Login] → halaman OTP Verification tampil
82. Amati label button pada halaman OTP Verification
83. Verifikasi Button pada OTP Verification berlabel "Login"
84. Klik button Text [Use a different method] → halaman Choose Verification Method tampil
85. Pilih opsi "Authenticator app", lalu klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
86. Verifikasi Button pada Enrollment Authenticator berlabel "Verify" (bukan "Login")

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal tiap TC setelah TC pertama; langkah 35 mencatat baseline jumlah email TC-AUTH-MFA-02; langkah 84–85 TC-AUTH-MFA-61) bukan asersi tambahan (S-03, S-12).
- Ukuran spec (smell sekitar 35 langkah): spec ini sekitar 61 langkah setelah langkah prefix login faktor-1 yang identik (buka Login with Password sampai klik [Log in]) tidak dihitung. Tidak dipecah karena kelima TC independen: tiap TC memakai user dan jendela privat sendiri, sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA: (1) TC-AUTH-MFA-61 butir c (label "Verify" pada Enrollment) tidak punya langkah menuju halaman Enrollment di Langkah Uji; langkah 84–85 ditambahkan sebagai langkah penghubung agar asersinya dapat dijalankan (S-14, S-15). (2) Post Condition tanpa langkah observasi dan tanpa Expected padanan tidak diasersi di spec (S-01, S-15): TC-AUTH-MFA-01 "Tidak ada sesi penuh; sesi pre-auth MFA aktif untuk `Budi Santoso`"; TC-AUTH-MFA-02 "Tidak ada email OTP terkirim ke `sitirahmawati@qwertysystem.net`" (setelah memilih opsi; klausa yang sama sebelum memilih adalah Expected a dan diasersi di langkah 37); TC-AUTH-MFA-03 "Tidak ada email OTP terkirim dan halaman tetap Choose Verification Method"; TC-AUTH-MFA-61 "Sesi pre-auth MFA aktif untuk `Novi Ariyanti`". Sesi pre-auth teramati sebagai halaman MFA tampil, yang sudah menjadi `Verifikasi` Expected. Perlu Expected atau langkah observasi di TC bila Post itu hendak diasersi.
