---
id: TC-AUTH-MFA-E2E-044-konkurensi-multi-tab
title: "Konkurensi Multi-Tab dan Multi-Sesi pada Sesi Pre-auth MFA"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-136
  - TC-AUTH-MFA-177
  - TC-AUTH-MFA-197
  - TC-AUTH-MFA-202
  - TC-AUTH-MFA-203
coverage:
  web: automated
---

# Konkurensi Multi-Tab dan Multi-Sesi pada Sesi Pre-auth MFA

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`), password user `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-136: `Bobby Hartanto` (`bobbyhartanto+{runId}-044@qwertysystem.net`), profil NEWDEVE (Tabel Data Uji Pre-setup #5: Activated, Active ON, device browser uji B belum ada di daftar trusted device, Authenticator sudah terdaftar dengan secret yang dikenali aplikasi authenticator uji).
  - TC-AUTH-MFA-177: `Putri Santoso` (`putrisantoso+{runId}-044@qwertysystem.net`), profil NEWDEVE, dengan ID device browser uji A terdaftar sebagai trusted device (seed BE) sehingga login di browser uji A tanpa MFA dan membuat sesi web aktif; ID device browser uji B tidak terdaftar.
  - TC-AUTH-MFA-197: `Putri Rahmawati` (`putrirahmawati+{runId}-044@qwertysystem.net`), profil NEWDEVE (Tabel Data Uji Pre-setup #5).
  - TC-AUTH-MFA-202: `Budi Wijaya` (`budiwijaya+{runId}-044@qwertysystem.net`), profil NEWDEVE (Tabel Data Uji Pre-setup #5).
  - TC-AUTH-MFA-203: `Siti Wijaya` (`sitiwijaya+{runId}-044@qwertysystem.net`), profil FIRST (Tabel Data Uji Pre-setup #3: Activated, Active ON, belum pernah login di platform mana pun, Authenticator belum terdaftar).
- Hook `after`: hapus kelima user (beserta sesi web yang terbentuk). Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk kelima TC. TC-AUTH-MFA-136, 197, 202, dan 203 memakai satu jendela dengan dua tab (jendela privat browser uji B, ID device belum dikenali, untuk 136, 197, dan 202; jendela baru browser uji A, konteks bersih tanpa sesi login karena sesi browser uji A dihapus pada langkah 35, untuk 203). TC-AUTH-MFA-177 memakai dua browser: browser uji A (device dikenali) dan browser uji B (jendela privat, ID device belum dikenali). Pengecekan log memakai jendela sesi akun aktor Total Control (Global Settings) yang dibuka di hook `before` (kredensial `Spectra.env.GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Dua tab dalam satu jendela (privat untuk browser uji B), termasuk duplikasi tab (alamat halaman yang sama dengan penyimpanan sesi halaman tersalin), dan dua browser berbeda aktif bersamaan (TC-AUTH-MFA-177).
  - Pemicu dua aksi di dua tab dengan selisih waktu sekecil mungkin (klik [Login] atau [Verify] pada satu tab bersamaan dengan digit ke-6 atau klik pada tab lain).
  - Aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) untuk kode TOTP valid, termasuk kode valid berikutnya; untuk TC-AUTH-MFA-203 dipakai juga untuk memindai QR code Enrollment.
  - Mail-catcher lingkungan uji untuk email OTP faktor-2 (TC-AUTH-MFA-202, 203).
  - Penanda waktu (baseline) Activity Log Session yang dicatat sebelum kedua verifikasi dikirim, supaya asersi entri Success hanya membaca baris sesudah penanda (TC-AUTH-MFA-202, 203).
  - Seeding state BE per user: ID device browser uji A sebagai trusted device (TC-AUTH-MFA-177) dan Authenticator terdaftar dengan secret yang dikenali aplikasi authenticator uji (profil NEWDEVE: TC-AUTH-MFA-136, 177, 197, 202); mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - Pembacaan status enrollment Authenticator `Siti Wijaya` oleh sisi BE untuk Expected butir b TC-AUTH-MFA-203 (langkah 87); disediakan tim FE/BE karena tidak ada cara cek di UI atau Langkah Uji TC; endpoint/skrip tidak didefinisikan di TC, PRD, atau LLD.
  - reCAPTCHA mode uji di environment.
- Pemulihan state global: tidak ada (spec tidak mengubah jam server, geo-IP, email service, atau counter rate limit).

## Test Steps

### TC-AUTH-MFA-136: Dua sesi pre-auth bersamaan untuk user dan platform yang sama

1. Buka halaman `Auth > Login with Password` di browser (tab pertama) → halaman Login with Password tampil
2. Ketik `bobbyhartanto+{runId}-044@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
6. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
7. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
8. Buka tab kedua pada browser yang sama dan buka halaman `Auth > Login with Password` → halaman Login with Password tampil
9. Ketik `bobbyhartanto+{runId}-044@qwertysystem.net` pada field Email di tab kedua
10. Ketik `Spectra.env.MFA_PASSWORD` pada field Password di tab kedua
11. Centang widget reCAPTCHA "I'm not a robot" di tab kedua
12. Klik button [Log in] di tab kedua → halaman `Auth > MFA > Choose Verification Method` tampil
13. Kembali ke tab pertama, ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `bobbyhartanto+{runId}-044@qwertysystem.net` pada kotak digit, lalu klik button [Login]
14. Verifikasi Tab pertama ditolak (sesi pre-auth lama di-invalidate oleh login baru untuk user dan platform yang sama)
15. Verifikasi Halaman login tampil di tab pertama
16. Verifikasi Tidak ada caption pada halaman login di tab pertama
17. Pindah ke tab kedua, pilih opsi "Authenticator app", lalu klik button [Login] → halaman Authenticator Verification tampil
18. Ketik 6 digit kode TOTP valid berikutnya dari aplikasi authenticator uji pada kotak digit, lalu klik button [Login]
19. Verifikasi Tab kedua menyelesaikan MFA seperti biasa dan Portal — Product Hub tampil

### TC-AUTH-MFA-177: Login final via MFA saat sesi web lain aktif memunculkan Dialog Duplicate Login Attempt

20. Di browser uji A (device dikenali), buka halaman `Auth > Login with Password` → halaman Login with Password tampil
21. Ketik `putrisantoso+{runId}-044@qwertysystem.net` pada field Email
22. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
23. Centang widget reCAPTCHA "I'm not a robot"
24. Klik button [Log in] → Portal — Product Hub tampil (sesi web pertama aktif)
25. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device, sesi browser uji A langkah 24, dan jendela sesi akun aktor tetap), lalu pindah ke browser uji B: buka jendela privat baru (tanpa sesi login) dan buka halaman `Auth > Login with Password` → halaman Login with Password tampil
26. Ketik `putrisantoso+{runId}-044@qwertysystem.net` pada field Email
27. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
28. Centang widget reCAPTCHA "I'm not a robot"
29. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
30. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
31. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
32. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `putrisantoso+{runId}-044@qwertysystem.net` pada kotak digit, lalu klik button [Login]
33. Verifikasi Dialog "Duplicate Login Attempt" tampil di browser uji B (isi dan pilihan dialog dimiliki session-management dan diuji di sana)
34. Verifikasi Portal — Product Hub belum menampilkan sesi baru di browser uji B
35. Tutup semua jendela privat user uji dan hapus sesi login browser uji A dan browser uji B (ID device browser uji A tetap) supaya sesi web `Putri Santoso` tidak tersisa sebelum TC berikutnya

### TC-AUTH-MFA-197: Verifikasi faktor-2 bersamaan dari dua tab untuk sesi pre-auth yang sama menghasilkan satu sesi

36. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
37. Buka halaman `Auth > Login with Password` di browser (tab pertama) → halaman Login with Password tampil
38. Ketik `putrirahmawati+{runId}-044@qwertysystem.net` pada field Email
39. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
40. Centang widget reCAPTCHA "I'm not a robot"
41. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
42. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
43. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
44. Duplikasi tab (alamat halaman Authenticator Verification yang sama) sebagai tab kedua di browser uji B
45. Pindah ke tab pertama, ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `putrirahmawati+{runId}-044@qwertysystem.net` pada kotak digit, lalu klik button [Login]
46. Pindah ke tab kedua segera, ketik kode TOTP yang sama pada kotak digit, lalu klik button [Login]
47. Verifikasi Satu tab berhasil dan Portal — Product Hub tampil
48. Verifikasi Tab yang kalah diarahkan ke halaman login (sesi pre-auth sudah dikonsumsi)
49. Verifikasi Tidak ada caption pada halaman login di tab yang kalah
50. Verifikasi Tidak ada sesi kedua

### TC-AUTH-MFA-202: Verify OTP dan Verify Authenticator bersamaan pada sesi pre-auth yang sama menghasilkan satu sesi

51. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
52. Buka halaman `Auth > Login with Password` di browser (tab pertama) → halaman Login with Password tampil
53. Ketik `budiwijaya+{runId}-044@qwertysystem.net` pada field Email
54. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
55. Centang widget reCAPTCHA "I'm not a robot"
56. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
57. Duplikasi tab (alamat halaman Choose Verification Method yang sama) sebagai tab kedua di browser uji B, lalu kembali ke tab pertama
58. Di tab pertama pilih opsi "OTP via email", lalu klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `budiwijaya+{runId}-044@qwertysystem.net`
59. Ketik 5 digit pertama kode OTP faktor-2 dari email pada kotak digit di tab pertama (tanpa digit ke-6)
60. Pindah ke tab kedua, pilih opsi "Authenticator app", lalu klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil untuk sesi pre-auth yang sama
61. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `budiwijaya+{runId}-044@qwertysystem.net` pada kotak digit di tab kedua (tanpa klik [Login])
62. Catat penanda waktu (baseline) Activity Log Session sebelum kedua verifikasi dikirim
63. Kirim kedua verifikasi bersamaan: ketik digit ke-6 kode OTP di tab pertama dan klik button [Login] di tab kedua
64. Verifikasi Tepat satu tab berhasil dan Portal — Product Hub tampil
65. Verifikasi Tab yang kalah diarahkan ke halaman login (sesi pre-auth sudah dikonsumsi)
66. Verifikasi Tidak ada caption pada halaman login di tab yang kalah
67. Verifikasi Tidak ada sesi kedua
68. Pindah ke jendela sesi akun aktor Total Control (Global Settings), lalu buka `Global Settings > Activity Log > Session` dan cari entri sesudah penanda waktu untuk `Budi Wijaya`
69. Verifikasi Tepat satu entri baru sesudah penanda waktu dengan Status "Success" untuk `Budi Wijaya` (tidak ada entri Success kedua)

### TC-AUTH-MFA-203: Verify Enrollment dan Verify OTP bersamaan pada sesi pre-auth yang sama menghasilkan satu sesi

70. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih, tanpa sesi login)
71. Buka halaman `Auth > Login with Password` di browser (tab pertama) → halaman Login with Password tampil
72. Ketik `sitiwijaya+{runId}-044@qwertysystem.net` pada field Email
73. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
74. Centang widget reCAPTCHA "I'm not a robot"
75. Klik button [Log in] → layar Confirm to Continue tampil
76. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
77. Duplikasi tab (alamat halaman Choose Verification Method yang sama) sebagai tab kedua di jendela browser uji A yang sama, lalu kembali ke tab pertama
78. Di tab pertama pilih opsi "Authenticator app", lalu klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
79. Pindai QR code dengan aplikasi authenticator uji, lalu ketik 6 digit kode valid dari aplikasi authenticator uji pada kotak digit di tab pertama (tanpa klik [Verify])
80. Pindah ke tab kedua, pilih opsi "OTP via email", lalu klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `sitiwijaya+{runId}-044@qwertysystem.net`
81. Ketik 5 digit pertama kode OTP faktor-2 dari email pada kotak digit di tab kedua (tanpa digit ke-6)
82. Catat penanda waktu (baseline) Activity Log Session sebelum kedua verifikasi dikirim
83. Kirim kedua verifikasi bersamaan: klik button [Verify] di tab pertama dan ketik digit ke-6 kode OTP di tab kedua
84. Verifikasi Tepat satu tab berhasil dan Portal — Product Hub tampil
85. Verifikasi Tab yang kalah diarahkan ke halaman login
86. Verifikasi Tidak ada caption pada halaman login di tab yang kalah
87. Verifikasi Status enrollment Authenticator `Siti Wijaya` mengikuti tab pemenang: aktif jika tab Enrollment yang berhasil, belum aktif jika tab OTP yang berhasil (dibaca lewat pembacaan status enrollment oleh sisi BE)
88. Verifikasi Tidak ada sesi kedua
89. Pindah ke jendela sesi akun aktor Total Control (Global Settings), lalu buka `Global Settings > Activity Log > Session` dan cari entri sesudah penanda waktu untuk `Siti Wijaya`
90. Verifikasi Tepat satu entri baru sesudah penanda waktu dengan Status "Success" untuk `Siti Wijaya` (tidak ada entri Success kedua)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Pembagian TC lintas spec: Dialog "Duplicate Login Attempt" pada TC-AUTH-MFA-177 hanya diasersi tampil; perilaku dan hasil pilihan dialog diuji di modul `auth/session-management`.
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal tiap TC setelah TC pertama, pindah tab atau browser, mencatat penanda waktu baseline log, pindah ke jendela sesi akun aktor) bukan asersi tambahan (S-03). Langkah 35 (tutup semua jendela privat dan hapus sesi browser uji A dan B di akhir TC-AUTH-MFA-177) memulihkan konteks browser bersih: sesi web `Putri Santoso` di browser uji A tidak boleh tersisa sebelum TC-AUTH-MFA-203 membuka jendela baru browser uji A (S-09).
- Asersi entri Success pada TC-AUTH-MFA-202 dan TC-AUTH-MFA-203 hanya memakai Status; kolom Activity tidak diasersi karena Expected butir c TC-nya ("tidak ada entri Success kedua") tidak menyebutnya.
- Jumlah langkah melewati ±35 karena lima TC independen berprefix login faktor-1 yang identik (langkah prefix tidak dihitung); tiap TC memakai user sendiri dan bagian sesudahnya tetap bermakna bila TC sebelumnya gagal.
- Temuan untuk QA: (1) TC-AUTH-MFA-197 dan TC-AUTH-MFA-202 menyebut "Satu tab berhasil" tanpa menentukan tab mana; spec mengasersi tepat satu tab berhasil, bukan tab tertentu, karena hasilnya bergantung pada urutan di server. (2) TC-AUTH-MFA-202 Langkah 7 ("buka halaman Authenticator Verification untuk sesi pre-auth yang sama") dan TC-AUTH-MFA-203 Langkah 7 ("buka halaman Choose Verification Method untuk sesi pre-auth yang sama") tidak menyebut caranya; spec menduplikasi tab pada Choose Verification Method sebelum tab pertama memilih metode, sehingga urutan sedikit berbeda dari Langkah Uji (S-05, S-14). (3) TC-AUTH-MFA-202 dan TC-AUTH-MFA-203 menyebut "digit ke-6 OTP" pada langkah pemicu, tetapi Langkah sebelumnya menyuruh mengetik kode OTP penuh; spec mengetik 5 digit lebih dulu karena OTP auto-submit pada digit ke-6 (PRD §4.4 FI-04). (4) TC-AUTH-MFA-203 butir b ("Enrollment aktif hanya jika verifikasi pada tab Enrollment yang berhasil") bergantung pada tab pemenang dan tidak memberi cara cek status enrollment di UI maupun di Langkah Uji; spec menulis klausa bersyarat "hanya jika" sebagai kondisi yang dibaca (tab pemenang menentukan hasil: aktif bila tab Enrollment menang, belum aktif bila tab OTP menang) lewat kemampuan pembacaan status enrollment oleh sisi BE yang disediakan tim FE/BE (langkah 87), tanpa langkah pengecekan tambahan di UI. QA perlu menambah langkah observasi atau menyatakan cara cek status itu. (5) TC-AUTH-MFA-177 Precondition "device dikenali" untuk profil NEWDEVE (device baru) bertentangan dengan definisi profil; spec men-seed ID device browser uji A sebagai trusted device khusus untuk user ini. (6) TC-AUTH-MFA-197 Post Condition "Satu sesi web aktif" dan "Tepat satu entri Success login final", TC-AUTH-MFA-136 Post Condition "satu sesi pre-auth aktif", serta TC-AUTH-MFA-177 Post Condition "Sesi web pertama `Putri Santoso` tetap aktif sampai pilihan dialog dibuat" tidak punya Expected padanan maupun langkah observasi di Langkah Uji, sehingga tidak diasersi dan spec tidak menambah langkah observasi (muat ulang browser uji A, pembacaan Activity Log Session). (7) TC-AUTH-MFA-202 dan TC-AUTH-MFA-203 Post Condition "tepat satu entri Success login final" diasersi lewat Expected butir c ("tidak ada entri Success kedua") dengan baseline penanda waktu, dan TC-AUTH-MFA-202, 203 tidak punya akun Total Control di Precondition; spec memakai akun aktor hook untuk mengecek Activity Log Session. (8) Mekanisme seeding state BE (ID device browser uji A sebagai trusted device pada TC-AUTH-MFA-177, Authenticator terdaftar dengan secret yang dikenali aplikasi authenticator uji pada profil NEWDEVE) belum ada di Pre-setup TC (#20/#21 hanya memuat sebagian); spec tidak menyebut endpoint seeding.
