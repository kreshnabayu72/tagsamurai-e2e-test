---
id: TC-AUTH-OTP-E2E-030-resilience-verify-dan-agreement
title: "Ketahanan Verify OTP dan Konfirmasi Agreement terhadap Error Server dan Timeout"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-57
  - TC-AUTH-OTP-58
  - TC-AUTH-OTP-59
  - TC-AUTH-OTP-105
  - TC-AUTH-OTP-106
  - TC-AUTH-OTP-188
coverage:
  web: automated
---

# Ketahanan Verify OTP dan Konfirmasi Agreement terhadap Error Server dan Timeout

## Prerequisites

- Mode: FE+BE dengan intercept parsial (backend nyata; sesi dan persetujuan dibuktikan lewat perilaku UI). Respons dipaksa lewat `Spectra.intercept()` dengan body 500 `{"message": "Internal server error"}`:
  - TC-AUTH-OTP-57 dan TC-AUTH-OTP-59: `POST /v2/iam/auth/otp/verify` dipaksa HTTP 500 (pada TC-AUTH-OTP-59 intercept dilepas sebelum klik [Verify])
  - TC-AUTH-OTP-58: koneksi browser diputus (offline) sampai request timeout, lalu dipulihkan
  - TC-AUTH-OTP-105: `POST /v2/iam/auth/confirm-agreement` dipaksa HTTP 500 (path ini hanya dirujuk di openapi.yaml:745 sebagai target preAuthToken, tanpa path item; kebutuhan mock berasal dari TC-AUTH-OTP-105)
  - TC-AUTH-OTP-106: koneksi browser diputus (offline) pada klik [Continue ➔] pertama, lalu dipulihkan
  - TC-AUTH-OTP-188: tanpa intercept; kondisi diciptakan di backend (lihat fixture BE di bawah)
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1); password dari `Spectra.env.GS_TC_PASSWORD`. Hook `before` membuka browser admin dan login sebagai akun aktor itu; langkah uji hanya berpindah konteks ke browser itu. Dipakai juga untuk membaca kedua surface log pada TC-AUTH-OTP-188. Password user uji dari `Spectra.env.OTP_PASSWORD`. Tidak ada password atau token di spec atau fixture.
- Akun aktor hook `before`: Principal `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #11), berhak mempublikasikan versi Privacy Policy di `Admin Console > Settings > Privacy Policy`; password dari `Spectra.env.AC_PRINCIPAL_PP_PASSWORD`. Akun ini dipakai hook `before` untuk menerbitkan versi Privacy Policy, bukan oleh langkah uji.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PP_PASSWORD`, `OTP_PASSWORD`.
- Hook `before`: Principal menerbitkan versi Privacy Policy terbaru lebih dulu, baru kemudian semua user (profil BASE dan POLICY) di-seed (versi yang diterbitkan adalah state global yang tidak ditarik kembali oleh hook `after`). Hook `before` (seeding API) lalu membuat user berikut dengan suffix per run `+{runId}-030`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian; `after` juga melepas semua intercept dan memulihkan koneksi):
  - Profil BASE (Activated, Active ON, bukan login pertama, device dikenali, persetujuan Privacy Policy terbaru ada; Agreement dan MFA tidak terpicu):
    - TC-AUTH-OTP-57: `Rizky Nasution` (`rizkynasution+{runId}-030@qwertysystem.net`)
    - TC-AUTH-OTP-58: `Nur Halim` (`nurhalim+{runId}-030@qwertysystem.net`)
    - TC-AUTH-OTP-59: `Agus Pratama` (`aguspratama+{runId}-030@qwertysystem.net`)
  - Profil POLICY (seperti BASE, tetapi Principal (hook `before`) sudah menerbitkan versi Privacy Policy yang lebih baru dari versi yang terakhir disetujui user; hanya Agreement terpicu):
    - TC-AUTH-OTP-105: `Putri Kusuma` (`putrikusuma+{runId}-030@qwertysystem.net`)
    - TC-AUTH-OTP-106: `Dimas Saputra` (`dimassaputra+{runId}-030@qwertysystem.net`)
    - TC-AUTH-OTP-188: `Hari Wibisono` (`hariwibisono+{runId}-030@qwertysystem.net`)
- Fixture BE untuk TC-AUTH-OTP-188 (state global): kondisi "versi Privacy Policy aktif tidak ter-resolve atau belum ada versi terpublikasi" diciptakan di backend pada langkah 71 dan dipulihkan pada langkah 85; hook `after` memulihkan kondisi ini (versi Privacy Policy aktif kembali dapat ditentukan, sehingga profil POLICY lain tidak terpengaruh) walau spec gagal di tengah. Suite berjalan serial (`parallel: false`) karena fixture ini mengubah versi Privacy Policy aktif yang dibaca semua profil POLICY. Mekanisme penciptaan kondisi (fixture BE) tidak disebut di TC sumber dan disediakan tim FE/BE.
- Kemampuan teknis: intercept network di browser (HTTP 500 dan pemutusan koneksi sampai timeout); mail-catcher lingkungan uji untuk membaca kode OTP; versi Privacy Policy lebih baru dari versi yang terakhir disetujui tiap user profil POLICY (TC-AUTH-OTP-105, 106, dan 188) diterbitkan Principal di hook `before`; reCAPTCHA mode uji; setiap TC dimulai dari jendela privat tanpa sesi.

## Test Steps

### TC-AUTH-OTP-57: Auto-submit Verify OTP gagal karena server error 5xx

1. Buka halaman `Auth > Login with OTP > Request OTP` di browser tanpa sesi
2. Ketik `rizkynasution+{runId}-030@qwertysystem.net` pada field Email
3. Centang widget reCAPTCHA "I'm not a robot"
4. Klik button [Request OTP]
5. Atur respons Verify OTP menjadi server error 500
6. Ketik 6 digit kode OTP dari email pada kotak digit
7. Verifikasi toast error: "Error, failed to log in."
8. Verifikasi toast error tampil di kanan bawah layar
9. Verifikasi halaman tetap di Verify OTP
10. Verifikasi kotak digit aktif kembali
11. Verifikasi 6 digit tetap terisi untuk percobaan ulang manual
12. Verifikasi button [Verify] muncul di bawah kotak digit
13. Verifikasi tidak ada sesi yang dibuat: membuka Portal — Product Hub langsung di tab lain mengalihkan ke halaman login
14. Verifikasi tidak ada caption "Invalid code" pada kotak digit
15. Lepaskan intercept respons Verify OTP

### TC-AUTH-OTP-58: Auto-submit Verify OTP gagal karena timeout atau koneksi terputus

16. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
17. Ketik `nurhalim+{runId}-030@qwertysystem.net` pada field Email
18. Centang widget reCAPTCHA "I'm not a robot"
19. Klik button [Request OTP]
20. Putuskan koneksi internet pada browser uji
21. Ketik 6 digit kode OTP dari email pada kotak digit
22. Tunggu sampai request timeout
23. Verifikasi toast error: "Error, failed to log in."
24. Verifikasi kotak digit aktif kembali
25. Verifikasi 6 digit tetap terisi
26. Verifikasi button [Verify] muncul
27. Verifikasi tidak ada sesi yang dibuat: membuka Portal — Product Hub langsung di tab lain mengalihkan ke halaman login
28. Pulihkan koneksi internet pada browser uji

### TC-AUTH-OTP-59: Klik Verify fallback dengan kode lengkap setelah server pulih menyelesaikan login

29. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
30. Ketik `aguspratama+{runId}-030@qwertysystem.net` pada field Email
31. Centang widget reCAPTCHA "I'm not a robot"
32. Klik button [Request OTP]
33. Atur respons Verify OTP menjadi server error 500
34. Ketik 6 digit kode OTP dari email pada kotak digit
35. Verifikasi button [Verify] muncul
36. Pulihkan respons Verify OTP menjadi normal
37. Klik button [Verify] dengan 6 digit tetap terisi
38. Verifikasi verifikasi berhasil dan browser dialihkan ke Portal — Product Hub
39. Verifikasi sesi aktif untuk `Agus Pratama`
40. Verifikasi button [Verify] tidak tampil lagi
41. Logout dari Portal — Product Hub

### TC-AUTH-OTP-105: Konfirmasi Agreement gagal karena server error 5xx

42. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
43. Ketik `putrikusuma+{runId}-030@qwertysystem.net` pada field Email
44. Centang widget reCAPTCHA "I'm not a robot"
45. Klik button [Request OTP]
46. Ketik 6 digit kode OTP dari email pada kotak digit
47. Centang checkbox "I have read and agree to the Privacy Policy *"
48. Atur respons konfirmasi Agreement menjadi server error 500
49. Klik button [Continue ➔]
50. Verifikasi toast error: "Error, failed to log in."
51. Verifikasi layar Confirm to Continue tetap terbuka
52. Verifikasi checkbox tetap dicentang
53. Verifikasi retry manual dimungkinkan
54. Verifikasi tidak ada sesi yang dibuat: membuka Portal — Product Hub langsung di tab lain mengalihkan ke halaman login
55. Lepaskan intercept respons konfirmasi Agreement

### TC-AUTH-OTP-106: Konfirmasi Agreement gagal karena timeout atau koneksi terputus lalu berhasil diulang

56. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
57. Ketik `dimassaputra+{runId}-030@qwertysystem.net` pada field Email
58. Centang widget reCAPTCHA "I'm not a robot"
59. Klik button [Request OTP]
60. Ketik 6 digit kode OTP dari email pada kotak digit
61. Centang checkbox "I have read and agree to the Privacy Policy *"
62. Putuskan koneksi internet pada browser uji
63. Klik button [Continue ➔]
64. Verifikasi toast error: "Error, failed to log in."
65. Verifikasi layar Confirm to Continue tetap terbuka
66. Pulihkan koneksi internet pada browser uji
67. Klik button [Continue ➔]
68. Verifikasi browser dialihkan ke Portal — Product Hub
69. Verifikasi sesi aktif untuk `Dimas Saputra`
70. Logout dari Portal — Product Hub

### TC-AUTH-OTP-188: Verify OTP ditolak saat versi Privacy Policy aktif tidak dapat ditentukan

71. Ciptakan kondisi fixture BE: versi Privacy Policy aktif tidak ter-resolve (atau belum ada versi terpublikasi)
72. Ganti konteks ke browser admin (sudah login sebagai akun aktor Total Control (Global Settings) lewat hook `before`), buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk `Hari Wibisono`, lalu catat baris teratas masing-masing sebagai baseline
73. Buka jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
74. Ketik `hariwibisono+{runId}-030@qwertysystem.net` pada field Email
75. Centang widget reCAPTCHA "I'm not a robot"
76. Klik button [Request OTP]
77. Ketik 6 digit kode OTP dari email pada kotak digit
78. Verifikasi toast gagal: "Error, failed to log in."
79. Verifikasi layar Confirm to Continue tidak tampil
80. Verifikasi tidak ada sesi aktif: membuka Portal — Product Hub langsung di tab lain mengalihkan ke halaman login
81. Verifikasi digit OTP dipertahankan pada kotak digit
82. Ganti konteks ke browser admin dan muat ulang `Global Settings > Activity Log > Session` serta `Global Settings > User > Detail > User Log` untuk `Hari Wibisono`
83. Verifikasi tidak ada entri log baru di `Global Settings > Activity Log > Session` dibanding baseline
84. Verifikasi tidak ada entri log baru di `Global Settings > User > Detail > User Log` dibanding baseline
85. Pulihkan kondisi fixture BE: versi Privacy Policy aktif dapat ditentukan
86. Ganti konteks ke jendela privat tempat layar Verify OTP masih terbuka, lalu klik button [Verify] dengan 6 digit tetap terisi
87. Verifikasi kode yang sama masih dapat diverifikasi: layar Confirm to Continue tampil

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Spec ini melebihi sekitar 35 langkah karena memuat enam TC kelas fault injection (satu spec per kelas per modul, konvensi bagian 3 butir 13), masing-masing dengan login penuh dan user sendiri. Bagian sesudah tiap TC tidak bergantung pada hasil TC sebelumnya (user dan jendela privat terpisah), sehingga tetap bermakna walau bagian sebelumnya gagal. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. TC-AUTH-OTP-188 ditaruh paling akhir karena mengubah state global (versi Privacy Policy aktif).
- Pengecualian P-1 (state berat): asersi absence "tidak ada entri log baru di kedua surface" dari TC-AUTH-OTP-188 (Expected c; `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`) tetap di spec ini dan tidak dipindah ke spec absence E2E-040, karena bergantung pada fixture BE "versi Privacy Policy tidak ter-resolve" yang baru dibangun pada langkah 71. Langkah 72 (baseline) dan langkah 82 sampai 84 (muat ulang dan verifikasi) adalah penambahan di sekitar Expected c; TC sumber hanya memuat langkah membuka log tanpa baseline (S-03, S-14). Kegagalan jaringan atau server saat auto-submit (TC-AUTH-OTP-131) dinilai di spec 040.
- Langkah 15, 28, 41, 55, dan 70 adalah langkah penghubung (lepas intercept, pulihkan koneksi, logout) agar TC berikutnya mulai dari state bersih (S-03, S-09). Cara memverifikasi "tidak ada sesi yang dibuat" (langkah 13, 27, 54, dan 80) memakai pola yang sama dengan TC-AUTH-OTP-97 (membuka Portal — Product Hub di tab lain mengalihkan ke halaman login); TC-AUTH-OTP-57, 58, 105, dan 188 tidak menyebut mekanisme observasinya.
- Temuan untuk QA:
  - TC-AUTH-OTP-188 Expected d ("kode yang sama masih dapat diverifikasi") tidak punya langkah yang memicu verifikasi ulang. Spec menambah pemulihan fixture BE (langkah 85) dan klik [Verify] sesudahnya, dengan asumsi button [Verify] muncul seperti pada kegagalan 5xx TC-AUTH-OTP-57 dan layar Confirm to Continue tampil karena profil POLICY; mohon QA mengonfirmasi.
  - TC-AUTH-OTP-188 tidak menyebut mekanisme fixture BE untuk "versi Privacy Policy aktif tidak ter-resolve"; kebutuhan ini dicatat di Prerequisites dan disiapkan tim FE/BE.
  - TC-AUTH-OTP-57/58/105/188 tidak menyebut cara mengamati "tidak ada sesi yang dibuat" selain menyatakan hasilnya; spec memakai pola pembukaan Product Hub di tab lain.
