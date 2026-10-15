---
id: TC-AUTH-OTP-E2E-029-resilience-request-dan-resend
title: "Ketahanan Request OTP dan Resend terhadap Error Server dan Timeout"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-31
  - TC-AUTH-OTP-32
  - TC-AUTH-OTP-83
  - TC-AUTH-OTP-93
  - TC-AUTH-OTP-183
coverage:
  web: automated
---

# Ketahanan Request OTP dan Resend terhadap Error Server dan Timeout

## Prerequisites

- Mode: FE+BE dengan intercept parsial (backend nyata; kode OTP dan jumlah resend dibuktikan lewat perilaku UI dan mail-catcher). Respons dipaksa lewat `Spectra.intercept()`; Request OTP dan Resend sama-sama memakai `POST /v2/iam/auth/otp/request` (`openapi.yaml`), jadi intercept dipasang per langkah dan dilepas sesudahnya. Body 500 yang dipakai: `{"message": "Internal server error"}` (contoh 500 di `openapi.yaml`).
  - TC-AUTH-OTP-31: `POST /v2/iam/auth/otp/request` dipaksa HTTP 500
  - TC-AUTH-OTP-32: koneksi browser diputus (offline) sampai request timeout, lalu dipulihkan
  - TC-AUTH-OTP-83: `POST /v2/iam/auth/otp/request` (aksi Resend) dipaksa HTTP 500 satu kali, lalu respons dipulihkan normal
  - TC-AUTH-OTP-93: `POST /v2/iam/auth/otp/request` (Request OTP pada sesi yang sama) dipaksa HTTP 500 satu kali
  - TC-AUTH-OTP-183: `POST /v2/iam/auth/otp/request` (aksi Resend) dipaksa HTTP 500 satu kali, lalu dipulihkan
- Akun aktor seeding: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Password user uji dari `Spectra.env.OTP_PASSWORD`. Tidak ada password atau token di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`, `OTP_PASSWORD`.
- Hook `before` (seeding API) membuat user profil BASE berikut (Activated, Active ON, bukan login pertama, device dikenali, persetujuan Privacy Policy terbaru ada; Agreement dan MFA tidak terpicu) dengan suffix per run `+{runId}-029`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian; `after` juga melepas semua intercept, memulihkan koneksi, dan mengembalikan jam server dan jam browser ke waktu nyata):
  - TC-AUTH-OTP-31: `Ratna Utami` (`ratnautami+{runId}-029@qwertysystem.net`)
  - TC-AUTH-OTP-32: `Taufik Safitri` (`taufiksafitri+{runId}-029@qwertysystem.net`)
  - TC-AUTH-OTP-83: `Tiara Simanjuntak` (`tiarasimanjuntak+{runId}-029@qwertysystem.net`)
  - TC-AUTH-OTP-93: `Fikri Siregar` (`fikrisiregar+{runId}-029@qwertysystem.net`)
  - TC-AUTH-OTP-183: `Rina Puspita` (`rinapuspita+{runId}-029@qwertysystem.net`)
- Kemampuan teknis: intercept network di browser (HTTP 500 dan pemutusan koneksi sampai timeout); mail-catcher lingkungan uji untuk membaca kode OTP dan memeriksa ada tidaknya email baru; reCAPTCHA mode uji; setiap TC dimulai dari jendela privat tanpa sesi.
- Jam yang diatur (konvensi bagian 6): countdown Resend di UI berjalan di jam browser, sehingga setiap langkah "Tunggu countdown 60 detik selesai" di TC dipenuhi oleh langkah "Majukan jam server dan jam browser 60 detik" dengan memajukan jam server dan jam browser 60 detik bersama, lalu menunggu UI menyegarkan state tombol Resend.
- State global: jam server, jam browser, dan intercept; semuanya dipulihkan di hook `after`. Karena kedua jam digeser, suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AUTH-OTP-31: Request OTP gagal karena server error 5xx

1. Buka halaman `Auth > Login with OTP > Request OTP` di browser tanpa sesi
2. Ketik `ratnautami+{runId}-029@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Atur respons Request OTP menjadi server error 500
5. Klik button [Request OTP]
6. Verifikasi toast error: "Error, failed to send the code."
7. Verifikasi toast error tampil di kanan bawah layar
8. Verifikasi halaman tetap di Request OTP
9. Verifikasi field Email masih terisi `ratnautami+{runId}-029@qwertysystem.net`
10. Verifikasi button [Request OTP] aktif kembali
11. Lepaskan intercept respons Request OTP

### TC-AUTH-OTP-32: Request OTP gagal karena timeout atau koneksi internet terputus

12. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
13. Ketik `taufiksafitri+{runId}-029@qwertysystem.net` pada field Email
14. Centang widget reCAPTCHA "I'm not a robot"
15. Putuskan koneksi internet pada browser uji
16. Klik button [Request OTP]
17. Tunggu sampai request timeout
18. Verifikasi toast error: "Error, failed to send the code."
19. Verifikasi halaman tetap di Request OTP
20. Verifikasi field Email masih terisi `taufiksafitri+{runId}-029@qwertysystem.net`
21. Verifikasi button [Request OTP] aktif kembali
22. Pulihkan koneksi internet pada browser uji

### TC-AUTH-OTP-83: Resend gagal karena server error 5xx tidak menambah jumlah resend dan tidak memulai cooldown

23. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
24. Ketik `tiarasimanjuntak+{runId}-029@qwertysystem.net` pada field Email
25. Centang widget reCAPTCHA "I'm not a robot"
26. Klik button [Request OTP]
27. Majukan jam server dan jam browser 60 detik sehingga countdown Resend selesai
28. Klik [Resend code]
29. Ulangi langkah 27 sampai 28 sebanyak 3 kali lagi sehingga total 4 Resend berhasil
30. Majukan jam server dan jam browser 60 detik sehingga countdown Resend selesai
31. Atur respons Resend menjadi server error 500
32. Klik [Resend code]
33. Verifikasi toast error: "Error, failed to send the code."
34. Verifikasi button [Resend code] tetap enabled
35. Pulihkan respons Resend menjadi normal
36. Klik [Resend code]
37. Verifikasi toast sukses: "Success, the code has been sent."
38. Verifikasi area Resend menampilkan "Resend code in (09:59)" (Resend ini adalah resend ke-5, bukan ke-6; kegagalan sebelumnya tidak dihitung)
39. Verifikasi area Resend dalam keadaan disabled

### TC-AUTH-OTP-93: Request OTP pada sesi yang sama diterima lalu gagal kirim karena server error

40. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
41. Ketik `fikrisiregar+{runId}-029@qwertysystem.net` pada field Email
42. Centang widget reCAPTCHA "I'm not a robot"
43. Klik button [Request OTP]
44. Ambil 6 digit kode OTP dari email yang masuk ke mail-catcher (kode ini dipakai di langkah 55)
45. Majukan jam server dan jam browser 60 detik sehingga countdown Resend selesai
46. Atur respons Request OTP menjadi server error 500
47. Klik tautan [Back to Login with Password]
48. Klik tautan [Log in with OTP]
49. Centang widget reCAPTCHA "I'm not a robot"
50. Klik button [Request OTP]
51. Verifikasi toast error: "Error, failed to send the code."
52. Verifikasi layar tetap di Request OTP
53. Verifikasi tidak ada email OTP baru di mail-catcher `fikrisiregar+{runId}-029@qwertysystem.net`
54. Tekan tombol Back browser sampai layar Verify OTP tampil
55. Ketik 6 digit kode OTP yang diterbitkan sebelumnya (langkah 44) pada kotak digit
56. Verifikasi kode lama tetap valid: browser dialihkan ke Portal — Product Hub
57. Verifikasi sesi aktif untuk `Fikri Siregar`
58. Logout dari Portal — Product Hub
59. Lepaskan intercept respons Request OTP

### TC-AUTH-OTP-183: Kode lama tetap valid setelah Resend gagal karena server error 5xx

60. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
61. Ketik `rinapuspita+{runId}-029@qwertysystem.net` pada field Email
62. Centang widget reCAPTCHA "I'm not a robot"
63. Klik button [Request OTP]
64. Ambil 6 digit kode OTP dari email yang masuk ke mail-catcher (kode ini dipakai di langkah 72)
65. Majukan jam server dan jam browser 60 detik sehingga countdown Resend selesai
66. Atur respons Resend menjadi server error 500
67. Klik [Resend code]
68. Verifikasi toast error: "Error, failed to send the code."
69. Verifikasi toast error tampil di kanan bawah layar
70. Verifikasi tidak ada email OTP baru di mail-catcher `rinapuspita+{runId}-029@qwertysystem.net`
71. Pulihkan respons Resend menjadi normal
72. Ketik 6 digit kode OTP dari langkah 64 pada kotak digit
73. Verifikasi kode lama diterima (Resend yang gagal tidak meng-invalidate kode): browser dialihkan ke Portal — Product Hub
74. Verifikasi sesi aktif untuk `Rina Puspita`

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Spec ini melebihi sekitar 35 langkah karena memuat lima TC kelas fault injection (satu spec per kelas per modul, konvensi bagian 3 butir 13) dengan satu login penuh dan satu kuota resend per TC. Tiap TC memakai user dan jendela privat sendiri, sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. TC-83 wajib mengulang tunggu countdown 60 detik (langkah 27 sampai 30); jumlah resend sebelum kegagalan adalah 4 sehingga Resend sukses sesudahnya adalah resend ke-5.
- Asersi absence pencatatan "tidak ada entri log baru untuk percobaan ini" di `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` dari TC-AUTH-OTP-31 (Expected d) dan TC-AUTH-OTP-32 (Expected c) dipindah ke spec `TC-AUTH-OTP-E2E-047-tidak-dicatat-absence-penolakan-navigasi-dan-kegagalan` (kelas g, S-05); pembagian TC dicatat juga di Notes spec 047.
- Langkah 11, 22, 58, dan 59 adalah langkah penghubung (lepas intercept, pulihkan koneksi, logout) agar TC berikutnya mulai dari state bersih (S-03, S-09). Langkah 44 dan 64 (mengambil kode dari mail-catcher sebelum Resend atau Request ulang) serta langkah 53 dan 70 (periksa mail-catcher) mengikuti ungkapan "kode yang diterbitkan sebelumnya" dan langkah "Periksa mail-catcher" pada TC sumber.
- Urutan periksa mail-catcher berbeda dari TC sumber: TC-AUTH-OTP-93 langkah 13 dan TC-AUTH-OTP-183 langkah 10 menaruh "Periksa mail-catcher" di akhir, sesudah kode lama diketik. Spec memindahkannya ke langkah 53 dan 70, tepat setelah toast error kegagalan, supaya "tidak ada email OTP baru" diperiksa pada kondisi gagal kirim sebelum kode lama dipakai.
- Temuan untuk QA:
  - TC-AUTH-OTP-93 langkah 6 menulis "Atur respons Request OTP menjadi server error 500" sebelum klik [Back to Login with Password]; spec mengikuti urutan itu (intercept dipasang di langkah 46, dipakai di langkah 50).
  - TC-AUTH-OTP-93 dan TC-AUTH-OTP-183 tidak menyebut cara memperoleh "kode yang diterbitkan sebelumnya"; spec menambah langkah mengambil kode dari mail-catcher sebelum kegagalan.
  - TC-AUTH-OTP-83 dan TC-AUTH-OTP-183 tidak menyebut apakah widget reCAPTCHA perlu dicentang untuk Resend; spec tidak mencentang karena sumber tidak menyebutnya.
  - NC-11 (keputusan user 2026-10-06) menetapkan countdown dihitung dari timestamp server dan bertahan setelah refresh. Pada TC-83, TC-93, dan TC-183 TC tidak menyatakan jam yang dibaca penghitung mundur di UI, sehingga jam browser dimajukan bersama jam server agar hasil tidak bergantung pada jawabannya. Mohon QA memastikan jam yang dipakai penghitung mundur.
