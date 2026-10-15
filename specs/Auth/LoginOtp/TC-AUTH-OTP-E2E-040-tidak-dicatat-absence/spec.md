---
id: TC-AUTH-OTP-E2E-040-tidak-dicatat-absence
title: "Kondisi yang Tidak Dicatat di Surface Log: Penolakan Pra-Lookup, Kegagalan Server, Cooldown, dan Akun Terhapus"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-130
  - TC-AUTH-OTP-131
  - TC-AUTH-OTP-132
  - TC-AUTH-OTP-133
  - TC-AUTH-OTP-134
  - TC-AUTH-OTP-128
  - TC-AUTH-OTP-11
  - TC-AUTH-OTP-12
  - TC-AUTH-OTP-13
  - TC-AUTH-OTP-16
  - TC-AUTH-OTP-19
  - TC-AUTH-OTP-23
  - TC-AUTH-OTP-24
  - TC-AUTH-OTP-28
  - TC-AUTH-OTP-89
  - TC-AUTH-OTP-167
  - TC-AUTH-OTP-168
coverage:
  web: automated
---

# Kondisi yang Tidak Dicatat di Surface Log: Penolakan Pra-Lookup, Kegagalan Server, Cooldown, dan Akun Terhapus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Login di browser admin dilakukan di hook `before`. Akun ini juga dipakai langkah uji untuk menghapus user (TC-AUTH-OTP-133).
- Password user uji dari `Spectra.env.OTP_PASSWORD` (hanya dipakai saat seeding user lewat API). Tidak ada password atau token di spec atau fixture.
- Akun aktor hook `before`: Principal `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #11), berhak mempublikasikan versi Privacy Policy di `Admin Console > Settings > Privacy Policy`; password dari `Spectra.env.AC_PRINCIPAL_PP_PASSWORD`. Akun ini dipakai hook `before` untuk menerbitkan versi Privacy Policy, bukan oleh langkah uji.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PP_PASSWORD`, `OTP_PASSWORD`.
- Kemampuan teknis: dua konteks browser (browser admin dan jendela privat publik); mail-catcher lingkungan uji untuk membaca kode OTP 6 digit; reCAPTCHA mode uji; `Spectra.intercept()` untuk memaksa respons Resend dan Verify OTP server error 500 (TC-AUTH-OTP-130 dan 131; intercept parsial di atas backend nyata); percepatan jam server untuk melewati countdown Resend 60 detik pada TC-AUTH-OTP-130 (jam dipulihkan di hook `after`).
- Jam yang diatur (konvensi bagian 6): jam server dan jam browser (klien) dimajukan bersama, karena countdown Resend di UI berjalan di jam klien sehingga memajukan jam server saja tidak mengaktifkan [Resend code]. Hook `after` memulihkan kedua jam. Suite berjalan serial (`parallel: false`) karena jam server digeser dan versi Privacy Policy yang diterbitkan adalah state global.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-040`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian; user `Budi Permata` yang dihapus langkah uji dilewati saat cleanup). Jumlah baris awal Activity Log > Session dan User Log tiap user dicatat di hook sebagai baseline "tidak ada baris baru":
  - TC-AUTH-OTP-12, 13: `Budi Santoso` (`budisantoso+{runId}-040@qwertysystem.net`), profil BASE (Activated, Active ON, sudah login web di device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru sudah ada). Email uji TC-AUTH-OTP-12 `budisantoso+{runId}-040.qwertysystem.net` (tanpa `@`), TC-AUTH-OTP-13 `budisantoso+{runId}-040@qwertysystem.c`
  - TC-AUTH-OTP-28: `Yoga Simanjuntak` (`yogasimanjuntak+{runId}-040@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-89: `Irfan Rahmawati` (`irfanrahmawati+{runId}-040@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-130: `Ayu Ramadhan` (`ayuramadhan+{runId}-040@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-131: `Fikri Simanjuntak` (`fikrisimanjuntak+{runId}-040@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-132: `Kartika Mulyadi` (`kartikamulyadi+{runId}-040@qwertysystem.net`), profil POLICY (seperti BASE, tetapi Principal sudah mempublish versi Privacy Policy yang lebih baru dari versi yang terakhir disetujui user; hanya Agreement terpicu)
  - TC-AUTH-OTP-133: `Budi Permata` (`budipermata+{runId}-040@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-134: `Siti Fitriani` (`sitifitriani+{runId}-040@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-128: `Sinta Anggraini` (`sintaanggraini+{runId}-040@qwertysystem.net`), profil POLICY
- Email tanpa user (tidak terdaftar di Global Settings > User): `tidakterdaftar.xyz+{runId}-040@qwertysystem.net` (TC-AUTH-OTP-19), `belumada.user+{runId}-040@qwertysystem.net` (TC-AUTH-OTP-24), `batasemail121@ccccccccccccccccccccccccccccccccccccccccccccccc.dddddddddddddddddddddddddddddddddddddddddd.qwertysystem.net` (TC-AUTH-OTP-16, 121 karakter), `xxxxxxxxxxxxxxxxxxxx@eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee.fffffffffffffffffffffffffffffffffffffffff.qwertysystem.net` (TC-AUTH-OTP-168, 121 karakter), dan 121 karakter `y` tanpa `@` (TC-AUTH-OTP-167); kedua alamat panjang ditulis literal tanpa suffix karena submit-nya ditolak dan tidak ada data tercipta, dengan local-part maksimal 64 karakter dan tiap label domain maksimal 63 karakter.
- Konfigurasi: akun Principal di atas menerbitkan versi Privacy Policy terbaru (tidak ditarik kembali oleh hook `after`) sebelum `Kartika Mulyadi` dan `Sinta Anggraini` di-seed (hook `before`). Urutan hook `before`: Principal lebih dulu menerbitkan versi Privacy Policy, lalu user profil BASE di-seed dengan persetujuan versi terbaru dan user profil POLICY di-seed dengan persetujuan versi sebelumnya.

## Test Steps

### Bagian A: Penolakan validasi dan lookup tidak menulis log (TC-AUTH-OTP-11, 12, 13, 16, 167, 168, 19, 23, 24)

1. Di browser admin Total Control (Global Settings), buka `Global Settings > Activity Log > Session` dan catat baris teratas sebagai baseline; buka `Global Settings > User > Detail > User Log` untuk `Budi Santoso` dan catat jumlah barisnya
2. Ganti konteks ke jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
3. TC-AUTH-OTP-11: biarkan field Email kosong, centang widget reCAPTCHA "I'm not a robot", klik button [Request OTP]
4. TC-AUTH-OTP-12: ketik `budisantoso+{runId}-040.qwertysystem.net` pada field Email, centang widget reCAPTCHA, klik button [Request OTP]
5. TC-AUTH-OTP-13: ganti isi field Email menjadi `budisantoso+{runId}-040@qwertysystem.c`, centang widget reCAPTCHA, klik button [Request OTP]
6. TC-AUTH-OTP-16: ganti isi field Email menjadi `batasemail121@ccccccccccccccccccccccccccccccccccccccccccccccc.dddddddddddddddddddddddddddddddddddddddddd.qwertysystem.net`, centang widget reCAPTCHA, klik button [Request OTP]
7. TC-AUTH-OTP-167: ganti isi field Email menjadi 121 karakter `y` tanpa tanda @, centang widget reCAPTCHA, klik button [Request OTP]
8. TC-AUTH-OTP-168: ganti isi field Email menjadi `xxxxxxxxxxxxxxxxxxxx@eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee.fffffffffffffffffffffffffffffffffffffffff.qwertysystem.net` (tidak terdaftar di Global Settings > User), centang widget reCAPTCHA, klik button [Request OTP]
9. TC-AUTH-OTP-19: ganti isi field Email menjadi `tidakterdaftar.xyz+{runId}-040@qwertysystem.net`, centang widget reCAPTCHA, klik button [Request OTP]
10. Muat ulang halaman Request OTP sehingga field Email kosong dan widget reCAPTCHA tidak tercentang
11. TC-AUTH-OTP-23: kosongkan field Email, biarkan widget reCAPTCHA tidak dicentang, klik button [Request OTP]
12. Muat ulang halaman Request OTP sehingga field Email kosong dan widget reCAPTCHA tidak tercentang
13. TC-AUTH-OTP-24: ketik `belumada.user+{runId}-040@qwertysystem.net` pada field Email, biarkan widget reCAPTCHA tidak dicentang, klik button [Request OTP]
14. Ganti konteks ke browser admin, muat ulang `Global Settings > Activity Log > Session` dan User Log `Budi Santoso`
15. Verifikasi TC-AUTH-OTP-11: tidak ada entri log baru untuk email kosong di `Global Settings > Activity Log > Session`
16. Verifikasi TC-AUTH-OTP-12: tidak ada entri log baru untuk email tanpa tanda @ di `Global Settings > Activity Log > Session`
17. Verifikasi TC-AUTH-OTP-12: tidak ada entri log baru untuk email tanpa tanda @ di `Global Settings > User > Detail > User Log` `Budi Santoso`
18. Verifikasi TC-AUTH-OTP-13: tidak ada entri log baru untuk email dengan 1 karakter setelah titik di `Global Settings > Activity Log > Session`
19. Verifikasi TC-AUTH-OTP-13: tidak ada entri log baru untuk email dengan 1 karakter setelah titik di User Log `Budi Santoso`
20. Verifikasi TC-AUTH-OTP-16: tidak ada entri log baru untuk email 121 karakter di `Global Settings > Activity Log > Session`
21. Verifikasi TC-AUTH-OTP-167: tidak ada entri log baru untuk email 121 karakter tanpa tanda @ di `Global Settings > Activity Log > Session`
22. Verifikasi TC-AUTH-OTP-168: tidak ada entri log baru untuk email 121 karakter yang tidak terdaftar di `Global Settings > Activity Log > Session`
23. Verifikasi TC-AUTH-OTP-19: tidak ada entri log baru untuk email yang belum terdaftar di `Global Settings > Activity Log > Session`
24. Verifikasi TC-AUTH-OTP-23: tidak ada entri log baru untuk Email kosong dan reCAPTCHA kosong di `Global Settings > Activity Log > Session`
25. Verifikasi TC-AUTH-OTP-24: tidak ada entri log baru untuk email belum terdaftar dan reCAPTCHA kosong di `Global Settings > Activity Log > Session`

### Bagian B: Request OTP berhasil dan Edit email dengan email kosong tidak menulis log (TC-AUTH-OTP-28, 89)

26. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
27. TC-AUTH-OTP-28: ketik `yogasimanjuntak+{runId}-040@qwertysystem.net` pada field Email, centang widget reCAPTCHA, klik button [Request OTP]
28. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
29. TC-AUTH-OTP-89: ketik `irfanrahmawati+{runId}-040@qwertysystem.net` pada field Email, centang widget reCAPTCHA, klik button [Request OTP]
30. Klik tautan [Edit email]
31. Kosongkan field Email, centang widget reCAPTCHA, klik button [Request OTP]
32. Ganti konteks ke browser admin, buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk `Yoga Simanjuntak` lalu `Irfan Rahmawati`
33. Verifikasi TC-AUTH-OTP-28: tidak ada entri log baru untuk Request OTP yang berhasil di `Global Settings > Activity Log > Session`
34. Verifikasi TC-AUTH-OTP-28: tidak ada entri log baru untuk Request OTP yang berhasil di `Global Settings > User > Detail > User Log` `Yoga Simanjuntak`
35. Verifikasi TC-AUTH-OTP-89: tidak ada entri log baru untuk percobaan Edit email dengan email kosong di `Global Settings > Activity Log > Session`
36. Verifikasi TC-AUTH-OTP-89: tidak ada entri log baru untuk percobaan Edit email dengan email kosong di `Global Settings > User > Detail > User Log` `Irfan Rahmawati`

### Bagian C: Kegagalan server, konfirmasi Agreement sukses, akun terhapus, dan cooldown (TC-AUTH-OTP-130, 131, 132, 133, 134)

37. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
38. TC-AUTH-OTP-130: ketik `ayuramadhan+{runId}-040@qwertysystem.net` pada field Email, centang widget reCAPTCHA, klik button [Request OTP]
39. Majukan jam server dan jam browser 60 detik sehingga countdown Resend selesai
40. Atur intercept respons Resend menjadi server error 500
41. Klik [Resend code]
42. Verifikasi toast error: "Error, failed to send the code."
43. Hapus intercept respons Resend
44. Pulihkan jam server dan jam browser ke waktu nyata
45. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
46. TC-AUTH-OTP-131: ketik `fikrisimanjuntak+{runId}-040@qwertysystem.net` pada field Email, centang widget reCAPTCHA, klik button [Request OTP]
47. Atur intercept respons Verify OTP menjadi server error 500
48. Ketik 6 digit kode OTP dari email pada kotak digit
49. Verifikasi toast error: "Error, failed to log in."
50. Hapus intercept respons Verify OTP
51. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
52. TC-AUTH-OTP-132: ketik `kartikamulyadi+{runId}-040@qwertysystem.net` pada field Email, centang widget reCAPTCHA, klik button [Request OTP]
53. Ketik 6 digit kode OTP dari email pada kotak digit
54. Centang checkbox "I have read and agree to the Privacy Policy *"
55. Klik button [Continue ➔]
56. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
57. TC-AUTH-OTP-133: ketik `budipermata+{runId}-040@qwertysystem.net` pada field Email, centang widget reCAPTCHA, klik button [Request OTP]
58. Ganti konteks ke browser admin, hapus user `Budi Permata` di `Global Settings > User`
59. Muat ulang `Global Settings > Activity Log > Session` dan catat baris teratas sebagai baseline TC-AUTH-OTP-133 (setelah penghapusan user, sebelum kode diketik)
60. Ganti konteks ke jendela privat, ketik 6 digit kode OTP dari email pada kotak digit
61. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
62. TC-AUTH-OTP-134: ketik `sitifitriani+{runId}-040@qwertysystem.net` pada field Email, centang widget reCAPTCHA, klik button [Request OTP]
63. Klik tautan [Back to Login with Password]
64. Klik tautan [Log in with OTP]
65. Centang widget reCAPTCHA "I'm not a robot"
66. Klik button [Request OTP]
67. Verifikasi Alert inline di atas button [Request OTP]: "Too many requests. Please try again later."
68. Ganti konteks ke browser admin, buka `Global Settings > Activity Log > Session`
69. Verifikasi TC-AUTH-OTP-130: tidak ada entri log baru untuk Resend yang gagal di `Global Settings > Activity Log > Session`
70. Verifikasi TC-AUTH-OTP-131: tidak ada entri log baru untuk kegagalan server saat auto-submit Verify OTP di `Global Settings > Activity Log > Session`
71. Verifikasi TC-AUTH-OTP-132: hanya satu baris baru untuk `Kartika Mulyadi` di `Global Settings > Activity Log > Session`, dengan Note `Login with OTP` Status `Success`
72. Verifikasi TC-AUTH-OTP-132: tidak ada baris dengan Note terkait konfirmasi Agreement untuk `Kartika Mulyadi` di `Global Settings > Activity Log > Session`
73. Verifikasi TC-AUTH-OTP-133: tidak ada baris baru dibanding baseline langkah 59 untuk Verify OTP akun yang sudah dihapus di `Global Settings > Activity Log > Session` karena tidak ada subjek user
74. Verifikasi TC-AUTH-OTP-134: tidak ada entri log baru untuk Request OTP yang ditolak karena cooldown untuk `Siti Fitriani` di `Global Settings > Activity Log > Session`
75. Buka `Global Settings > User > Detail > User Log` untuk `Ayu Ramadhan`
76. Verifikasi TC-AUTH-OTP-130: tidak ada entri log baru untuk Resend yang gagal di User Log `Ayu Ramadhan`
77. Buka `Global Settings > User > Detail > User Log` untuk `Fikri Simanjuntak`
78. Verifikasi TC-AUTH-OTP-131: tidak ada entri log baru untuk kegagalan server saat auto-submit Verify OTP di User Log `Fikri Simanjuntak`
79. Buka `Global Settings > User > Detail > User Log` untuk `Kartika Mulyadi`
80. Verifikasi TC-AUTH-OTP-132: hanya satu baris baru di User Log `Kartika Mulyadi`, dengan Note `Login with OTP` Status `Success`
81. Verifikasi TC-AUTH-OTP-132: tidak ada baris dengan Note terkait konfirmasi Agreement di User Log `Kartika Mulyadi`
82. Buka `Global Settings > User > Detail > User Log` untuk `Siti Fitriani`
83. Verifikasi TC-AUTH-OTP-134: tidak ada entri log baru untuk Request OTP yang ditolak karena cooldown di User Log `Siti Fitriani`

### Bagian D: Konfirmasi Agreement tidak mencatat Success lebih awal dan tidak menambah Note lain (TC-AUTH-OTP-128)

84. Ganti konteks ke jendela privat baru (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
85. TC-AUTH-OTP-128: ketik `sintaanggraini+{runId}-040@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", klik button [Request OTP]
86. Ketik 6 digit kode OTP dari email pada kotak digit
87. Ganti konteks ke browser admin, buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk `Sinta Anggraini` (sebelum Continue)
88. Verifikasi TC-AUTH-OTP-128: sebelum Continue tidak ada baris Success `Login with OTP` untuk percobaan ini (jumlah baris sama dengan baseline hook) di `Global Settings > Activity Log > Session`
89. Verifikasi TC-AUTH-OTP-128: sebelum Continue tidak ada baris Success `Login with OTP` untuk percobaan ini (jumlah baris sama dengan baseline hook) di `Global Settings > User > Detail > User Log`
90. Ganti konteks ke jendela privat, centang checkbox "I have read and agree to the Privacy Policy *"
91. Klik button [Continue ➔]
92. Ganti konteks ke browser admin, segarkan kedua surface log
93. Verifikasi TC-AUTH-OTP-128: tidak ada baris dengan Note lain untuk konfirmasi Agreement

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Kelas harness g (asersi absence). `sourceTc` memuat TC murni absence (TC-AUTH-OTP-130 sampai 134) dan sisi-absence dari TC fungsional (TC-AUTH-OTP-11, 12, 13, 16, 19, 23, 24, 28, 89, 167, 168), sesuai prinsip 10 dan S-05. Asersi absence dari TC fungsional itu dipindah dari spec fungsional E2E-006 (TC-AUTH-OTP-11, 12, 13, 16, 167, 168), E2E-008 (TC-AUTH-OTP-19), E2E-009 (TC-AUTH-OTP-23, 24), E2E-010 (TC-AUTH-OTP-28), dan E2E-017 (TC-AUTH-OTP-89); bagian fungsionalnya (caption, toast, perpindahan layar, email) diasersi di spec itu, bukan di sini, dan pembagian ini dicatat di Notes spec tersebut.
- Asersi absence TC-AUTH-OTP-128 (butir a dan d: tidak ada baris Success sebelum Continue, tidak ada baris Note lain untuk konfirmasi Agreement) dipindah dari E2E-039 (prinsip 13g); butir b dan c (tepat satu baris Success) tetap diasersi di E2E-039 dan pembagian ini dicatat juga di Notes E2E-039. Pemicu Agreement diulang di Bagian D karena asersi sebelum Continue butuh layar Confirm to Continue yang terbuka.
- Asersi absence TC fungsional lain (TC-AUTH-OTP-35, 36, 86, 30, 62, 140, 68, 78, 90, 31, 32, 157) ada di E2E-047; pemicu state berat tetap di spec asalnya (E2E-027 dan E2E-028).
- Spec ini 93 langkah, jauh di atas smell sekitar 35 langkah (prinsip 13), karena memuat 17 TC. Dipertahankan karena tiap bagian (A, B, C, D) berdiri sendiri dengan user dan jendela privat terpisah, soft assertion berlaku, dan seluruh spec satu kelas (absence). Dalam Bagian A pemicu penolakan dijalankan berurutan di satu jendela privat dan log diperiksa sekali memakai baseline baris teratas yang dicatat di langkah 1; hanya penolakan tanpa subjek user yang diasersi lewat Activity Log Session (TC-AUTH-OTP-133 memakai baseline sendiri dari langkah 59), sedangkan TC-AUTH-OTP-12 dan 13 juga lewat User Log `Budi Santoso` (S-03, S-14).
- Pemicu fungsional pada Bagian A sampai C (caption penolakan, mail-catcher kosong, perpindahan layar) tidak diasersi di spec ini; hanya toast TC-AUTH-OTP-130, TC-AUTH-OTP-131, dan Alert TC-AUTH-OTP-134 yang diasersi karena tertulis di Expected Result TC absence tersebut.
- Urutan TC di dalam spec mengikuti pengelompokan penolakan tanpa user, lalu Request berhasil, lalu kegagalan server, bukan urutan nomor TC granular; TC-AUTH-OTP-133 ditaruh sebelum TC-AUTH-OTP-134 karena menghapus user miliknya sendiri (S-05, S-06).
- Pengecualian P-2 (pemicu bukan objek uji): intercept respons 500 pada TC-AUTH-OTP-130 (Resend) dan TC-AUTH-OTP-131 (Verify OTP) hanya memicu kegagalan server; objek asersinya adalah ketiadaan entri log, dan intercept dilepas segera setelah toast diverifikasi (langkah 43 dan 50). Penolakan cooldown TC-AUTH-OTP-134 dan Alert-nya diasersi karena tertulis di Expected TC. Penggeseran jam server dan browser (langkah 39) hanya memenuhi countdown Resend dan dipulihkan ke waktu nyata pada langkah 44 (hook `after` tetap menjadi cadangan). Pembacaan User Log dilakukan per user setelah semua asersi Activity Log Session (langkah 75 sampai 83) agar tiap asersi didahului langkah yang membuka halamannya (S-14).
- Langkah penghubung (S-03): ganti konteks antara jendela privat dan browser admin, memasang dan menghapus intercept respons 500, majukan jam server dan jam browser, muat ulang halaman Request OTP agar reCAPTCHA kembali tidak tercentang (TC-AUTH-OTP-23 dan 24), dan muat ulang log ditulis sebagai aksi tanpa `Verifikasi`.
- Temuan untuk QA: (1) TC-AUTH-OTP-131 berjudul "kegagalan jaringan atau server" tetapi langkah dan Expected hanya mencakup server error 500, tidak ada skenario timeout atau jaringan terputus. (2) TC-AUTH-OTP-134 berjudul "cooldown atau kuota sesi", tetapi langkah hanya menguji cooldown 60 detik; penolakan karena kuota habis tidak punya langkah pemeriksaan log. (3) TC-AUTH-OTP-11, 23, dan 24 kini menyatakan tidak ada user yang terdampak sehingga tidak ada User Log; spec memeriksa hanya Activity Log Session untuk ketiganya. TC-AUTH-OTP-12, 13, 16, 19, 167, dan 168 masih menulis `Global Settings > User > Detail > User Log` tanpa menyebut user mana yang diperiksa untuk email yang tidak punya user; spec memeriksa Activity Log Session untuk semuanya dan User Log hanya untuk user BASE yang jelas (`Budi Santoso`). (4) TC-AUTH-OTP-167 masih memakai 121 karakter `y` tanpa `@` (bentuk lama); spec mengikuti TC.
 (5) Nama tampilan `Sinta Anggraini` sama dengan user seeding TC-AUTH-OTP-128 di E2E-039 (TC memberi nama tetap; hanya email yang bersuffix per run), sehingga baris Activity Log Session bisa tertukar bila ada user lain bernama sama; baseline per user dicatat di hook.