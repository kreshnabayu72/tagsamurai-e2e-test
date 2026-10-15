---
id: TC-AUTH-MFA-E2E-005-validasi-dan-sukses-verifikasi-otp
title: "Validasi dan Sukses Verifikasi OTP Faktor Kedua"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-70
  - TC-AUTH-MFA-71
  - TC-AUTH-MFA-72
  - TC-AUTH-MFA-66
  - TC-AUTH-MFA-68
coverage:
  web: automated
---

# Validasi dan Sukses Verifikasi OTP Faktor Kedua

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): lima user profil NEWDEV (Tabel Data Uji Pre-setup #4: Activated, Active ON, sudah pernah login sukses di web, Authenticator belum terdaftar; TC pertama berjalan di browser awal; browser awal dan tiap jendela privat tanpa ID device tersimpan, dikenali sebagai browser uji B; login dari browser uji B memicu MFA karena ID device belum dikenali; tanpa layar Confirm to Continue), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-70: `Panji Laksono` (`panjilaksono+{runId}-005@qwertysystem.net`)
  - TC-AUTH-MFA-71: `Rosa Melinda` (`rosamelinda+{runId}-005@qwertysystem.net`)
  - TC-AUTH-MFA-72: `Ardi Susanto` (`ardisusanto+{runId}-005@qwertysystem.net`)
  - TC-AUTH-MFA-66: `Rangga Wirawan` (`ranggawirawan+{runId}-005@qwertysystem.net`)
  - TC-AUTH-MFA-68: `Ferry Gunadi` (`ferrygunadi+{runId}-005@qwertysystem.net`)
- Hook `after`: hapus kelima user (beserta sesi web dan trusted device yang terbentuk dari TC-AUTH-MFA-66 dan 68). Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah TC pertama dimulai di jendela privat baru.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture. Kode uji salah (`123`, `000000`) boleh literal karena submit-nya diblokir.
- Kemampuan teknis:
  - Jendela privat; reCAPTCHA mode uji di environment.
  - Mail-catcher lingkungan uji untuk membaca kode OTP faktor-2 (TC-AUTH-MFA-66, 68).
  - Pengisian clipboard dan tempel dengan Ctrl+V (TC-AUTH-MFA-68).
  - Seeding state BE per user: riwayat login web sukses dengan trusted device ber-ID device browser uji A untuk kelima user; mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.

## Test Steps

### TC-AUTH-MFA-70: Klik [Login] pada OTP Verification sebelum 6 digit terisi

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `panjilaksono+{runId}-005@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
6. Pilih opsi "OTP via email" pada halaman Choose Verification Method
7. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `panjilaksono+{runId}-005@qwertysystem.net`
8. Ketik 3 digit kode `123` pada kotak digit
9. Klik button [Login]
10. Verifikasi Tidak ada sesi yang dibuat (Portal tidak tampil)
11. Verifikasi Halaman tetap `Auth > MFA > OTP Verification`
12. Verifikasi Caption error di bawah kotak digit: "OTP must not be empty"

### TC-AUTH-MFA-71: Klik [Login] pada OTP Verification tanpa mengisi kode

13. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
14. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
15. Ketik `rosamelinda+{runId}-005@qwertysystem.net` pada field Email
16. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
17. Centang widget reCAPTCHA "I'm not a robot"
18. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
19. Pilih opsi "OTP via email" pada halaman Choose Verification Method
20. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `rosamelinda+{runId}-005@qwertysystem.net`
21. Klik button [Login] tanpa mengisi kotak digit
22. Verifikasi Tidak ada sesi yang dibuat (Portal tidak tampil)
23. Verifikasi Halaman tetap `Auth > MFA > OTP Verification`
24. Verifikasi Caption error di bawah kotak digit: "OTP must not be empty"

### TC-AUTH-MFA-72: Verifikasi OTP faktor-2 dengan kode salah

25. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
26. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
27. Ketik `ardisusanto+{runId}-005@qwertysystem.net` pada field Email
28. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
29. Centang widget reCAPTCHA "I'm not a robot"
30. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
31. Pilih opsi "OTP via email" pada halaman Choose Verification Method
32. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `ardisusanto+{runId}-005@qwertysystem.net`
33. Ketik 6 digit kode `000000` (berbeda dari kode di email) pada kotak digit; digit ke-6 menjalankan verifikasi otomatis
34. Verifikasi Caption error di bawah kotak digit: "Invalid code"
35. Verifikasi Tidak ada sesi yang dibuat (Portal tidak tampil)
36. Verifikasi Halaman tetap `Auth > MFA > OTP Verification`
37. Verifikasi Kotak digit dikosongkan
38. Verifikasi Fokus kembali ke kotak 1
39. Ketik ulang satu digit (`1`) pada kotak 1
40. Verifikasi Caption error hilang
41. Verifikasi Border error hilang

### TC-AUTH-MFA-66: Verifikasi OTP faktor-2 dengan kode benar berjalan otomatis pada digit ke-6 dan masuk Product Hub

42. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
43. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
44. Ketik `ranggawirawan+{runId}-005@qwertysystem.net` pada field Email
45. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
46. Centang widget reCAPTCHA "I'm not a robot"
47. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
48. Pilih opsi "OTP via email" pada halaman Choose Verification Method
49. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `ranggawirawan+{runId}-005@qwertysystem.net`
50. Ketik 6 digit kode OTP faktor-2 dari email `ranggawirawan+{runId}-005@qwertysystem.net` pada kotak digit
51. Verifikasi Tidak ada button [Login] yang diklik; verifikasi berjalan otomatis begitu digit ke-6 terisi
52. Verifikasi Browser dialihkan ke Portal — Product Hub (Portal tampil menandakan sesi web aktif untuk `Rangga Wirawan`)
53. Verifikasi Tidak ada toast sukses untuk verifikasi
54. Verifikasi Tidak ada layar konfirmasi tambahan

### TC-AUTH-MFA-68: Menempel 6 digit sekaligus memecah karakter ke enam kotak dan memverifikasi otomatis

55. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
56. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
57. Ketik `ferrygunadi+{runId}-005@qwertysystem.net` pada field Email
58. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
59. Centang widget reCAPTCHA "I'm not a robot"
60. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
61. Pilih opsi "OTP via email" pada halaman Choose Verification Method
62. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `ferrygunadi+{runId}-005@qwertysystem.net`
63. Salin 6 digit kode OTP faktor-2 dari email `ferrygunadi+{runId}-005@qwertysystem.net` ke clipboard
64. Klik kotak 1
65. Tempel dengan Ctrl+V
66. Verifikasi Keenam kotak terisi satu digit per kotak sesuai urutan kode
67. Verifikasi Verifikasi berjalan otomatis karena digit ke-6 terisi
68. Verifikasi Browser dialihkan ke Portal — Product Hub

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal tiap TC setelah TC pertama) bukan asersi tambahan (S-03).
- Penyimpangan urutan (S-05, S-10): TC sumber berurut 66, 68, 70, 71, 72; spec memakai 70, 71, 72 lebih dulu (validasi yang diblokir) lalu 66 dan 68 (aksi sukses) di akhir.
- Browser/jendela privat berbeda dipakai berurutan hanya untuk membentuk identitas device (browser uji B), tanpa asersi lintas jendela; bukan konteks kedua (tidak butuh butir P-2).
- Pembagian TC lintas spec: Post Condition pencatatan (Failed `Empty OTP` pada TC-AUTH-MFA-70 dan 71, Failed `Incorrect OTP` pada TC-AUTH-MFA-72, entri Success `Login with password` pada TC-AUTH-MFA-66) bertanda "detail pada TC Logging" dan tidak diasersi di spec fungsional ini (S-05). Post Condition TC-AUTH-MFA-70 "dihitung sebagai satu percobaan salah terhadap batas 5" juga tidak diasersi di sini; dicakup TC batas percobaan di spec lain.
- Ukuran spec (smell sekitar 35 langkah): spec ini sekitar 43 langkah setelah langkah prefix login faktor-1 yang identik (buka Login with Password sampai klik [Log in]) tidak dihitung. Tidak dipecah karena kelima TC independen: tiap TC memakai user dan jendela privat sendiri, sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA: (1) Post Condition tanpa langkah observasi dan tanpa Expected padanan tidak diasersi di spec (S-01, S-15): TC-AUTH-MFA-66 "Satu sesi web aktif untuk `Rangga Wirawan`" (sesi web teramati sebagai Portal tampil, sudah menjadi `Verifikasi` Expected b) dan "Browser uji B tercatat sebagai trusted device `Rangga Wirawan` untuk platform web"; TC-AUTH-MFA-68 "Satu sesi web aktif untuk `Ferry Gunadi`" (teramati sebagai Portal tampil, sudah menjadi `Verifikasi` Expected b). Perlu Expected atau langkah observasi di TC bila trusted device hendak diasersi. (2) TC-AUTH-MFA-72 Langkah 9 "Ketik ulang satu digit pada kotak 1" tidak menyebut digitnya; spec memakai `1` (S-15). (3) TC-AUTH-MFA-68 Langkah Uji menyebut menyalin kode dari email; dicatat sebagai kebutuhan clipboard dan mail-catcher di Prerequisites. (4) Mekanisme seed state BE (trusted device ber-ID device browser uji A) belum ada di Pre-setup (#20/#21); spec tidak menyebut endpoint karangan (S-11, S-13).
