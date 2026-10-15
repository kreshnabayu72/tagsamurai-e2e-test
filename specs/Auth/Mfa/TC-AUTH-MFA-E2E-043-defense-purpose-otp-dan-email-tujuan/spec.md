---
id: TC-AUTH-MFA-E2E-043-defense-purpose-otp-dan-email-tujuan
title: "Defense-in-Depth: Purpose OTP Lintas Login with OTP dan MFA serta Email Tujuan OTP"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-191
  - TC-AUTH-MFA-206
  - TC-AUTH-MFA-210
  - TC-AUTH-MFA-192
coverage:
  web: automated
---

# Defense-in-Depth: Purpose OTP Lintas Login with OTP dan MFA serta Email Tujuan OTP

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): empat user profil NEWDEV (Tabel Data Uji Pre-setup #4: Activated, Active ON, device browser uji B belum ada di daftar trusted device, Authenticator belum terdaftar), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-192: `Dewi Rahmawati` (`dewirahmawati+{runId}-043@qwertysystem.net`)
  - TC-AUTH-MFA-191: `Andi Rahmawati` (`andirahmawati+{runId}-043@qwertysystem.net`)
  - TC-AUTH-MFA-206: `Kania Pratiwi` (`kaniapratiwi+{runId}-043@qwertysystem.net`)
  - TC-AUTH-MFA-210: `Dewi Anjani` (`dewianjani+{runId}-043@qwertysystem.net`)
- Hook `after`: hapus keempat user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk keempat TC. Tiap TC dimulai di jendela privat baru (browser uji B, ID device belum dikenali), dengan dua tab pada TC-AUTH-MFA-191, 206, dan 210. Pengecekan log memakai jendela sesi akun aktor Total Control (Global Settings) yang dibuka di hook `before` (kredensial `Spectra.env.GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Mail-catcher lingkungan uji untuk membaca email OTP faktor-2 MFA dan email OTP Login with OTP, membedakan keduanya lewat urutan kedatangan dan kode yang dicatat, melihat penerima setiap email, dan menghitung jumlah email OTP faktor-2 per alamat (baseline jumlah email sebelum aksi; TC-AUTH-MFA-192).
  - Dua tab dalam satu jendela privat.
  - Penanda waktu (baseline) Activity Log Session yang dicatat sebelum kode salah dimasukkan, supaya asersi entri log hanya membaca baris sesudah penanda (TC-AUTH-MFA-191, 206, 210).
  - Pembacaan hitungan percobaan salah sesi pre-auth oleh sisi BE (TC-AUTH-MFA-191 butir b; langkah 26 dan 32): mekanisme baca disediakan tim FE/BE karena hitungan itu tidak terlihat di UI; endpoint/skrip tidak didefinisikan di TC, PRD, atau LLD.
  - reCAPTCHA mode uji di environment.
- Pemulihan state global: tidak ada (spec tidak mengubah jam server, geo-IP, email service, atau counter rate limit).

## Test Steps

### TC-AUTH-MFA-192: OTP faktor-2 selalu dikirim ke email akun terdaftar dan alamat tidak dapat diubah dari halaman

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `dewirahmawati+{runId}-043@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
6. Pilih opsi "OTP via email" pada halaman Choose Verification Method
7. Catat jumlah email OTP faktor-2 di mail-catcher `dewirahmawati+{runId}-043@qwertysystem.net` dan di kotak masuk alamat lain sebagai baseline sebelum klik [Login]
8. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `dewirahmawati+{runId}-043@qwertysystem.net`
9. Periksa halaman OTP Verification untuk kontrol pengubah email (tautan atau field)
10. Verifikasi Tidak ada tautan [Edit email] atau field email pada halaman OTP Verification
11. Periksa mail-catcher `dewirahmawati+{runId}-043@qwertysystem.net` dan kotak masuk alamat lain di mail-catcher
12. Verifikasi Email OTP faktor-2 diterima di `dewirahmawati+{runId}-043@qwertysystem.net` (email akun terdaftar)
13. Verifikasi Jumlah email OTP faktor-2 di `dewirahmawati+{runId}-043@qwertysystem.net` bertambah satu dari baseline
14. Verifikasi Jumlah email OTP faktor-2 di kotak masuk alamat lain sama dengan baseline

### TC-AUTH-MFA-191: Kode OTP login-otp yang masih berlaku dipakai pada OTP Verification MFA

15. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
16. Buka halaman `Auth > Login with Password` di browser (tab A) → halaman Login with Password tampil
17. Ketik `andirahmawati+{runId}-043@qwertysystem.net` pada field Email
18. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
19. Centang widget reCAPTCHA "I'm not a robot"
20. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
21. Pilih opsi "OTP via email" pada halaman Choose Verification Method
22. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `andirahmawati+{runId}-043@qwertysystem.net`
23. Di tab B pada jendela yang sama, buka halaman `Auth > Login with OTP > Request OTP`, ketik `andirahmawati+{runId}-043@qwertysystem.net`, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP] → halaman Verify OTP tampil dan email OTP login terkirim
24. Catat kode OTP login-otp dari email OTP Login with OTP di mail-catcher (kode ini berbeda dari kode faktor-2)
25. Catat penanda waktu (baseline) Activity Log Session sebelum kode OTP login-otp dimasukkan
26. Catat hitungan percobaan salah sesi pre-auth `Andi Rahmawati` sebagai baseline (dibaca lewat kemampuan baca BE)
27. Kembali ke tab A (OTP Verification MFA) dan ketik 6 digit kode OTP login-otp tersebut pada kotak digit
28. Verifikasi Caption error di bawah kotak digit: "Invalid code"
29. Verifikasi Tidak ada sesi penuh yang dibuat
30. Pindah ke jendela sesi akun aktor Total Control (Global Settings), lalu buka `Global Settings > Activity Log > Session` dan cari entri sesudah penanda waktu untuk `Andi Rahmawati`
31. Verifikasi Percobaan dicatat: tepat satu entri baru sesudah penanda waktu dengan Status "Failed" dan Note "Incorrect OTP" untuk `Andi Rahmawati`
32. Verifikasi Percobaan tersebut dihitung sebagai percobaan salah: hitungan percobaan salah sesi pre-auth `Andi Rahmawati` bertambah satu dari baseline

### TC-AUTH-MFA-206: Kode OTP Login with OTP tidak berlaku sebagai kode faktor-2 di halaman OTP Verification MFA

33. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
34. Buka halaman `Auth > Login with OTP` di tab A, ketik `kaniapratiwi+{runId}-043@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP] → halaman Verify OTP tampil dan email OTP login terkirim
35. Catat kode pertama dari email OTP Login with OTP di mail-catcher tanpa memasukkannya
36. Buka halaman `Auth > Login with Password` di tab B → halaman Login with Password tampil
37. Ketik `kaniapratiwi+{runId}-043@qwertysystem.net` pada field Email
38. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
39. Centang widget reCAPTCHA "I'm not a robot"
40. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
41. Pilih opsi "OTP via email" pada halaman Choose Verification Method
42. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil
43. Catat penanda waktu (baseline) Activity Log Session sebelum kode OTP Login with OTP dimasukkan
44. Ketik 6 digit kode OTP Login with OTP yang dicatat pada kotak digit
45. Verifikasi Kode ditolak: caption "Invalid code" tampil di bawah kotak digit
46. Verifikasi Kotak digit dikosongkan
47. Verifikasi Tidak ada sesi dibuat
48. Verifikasi Halaman tetap di OTP Verification
49. Pindah ke jendela sesi akun aktor Total Control (Global Settings), lalu buka `Global Settings > Activity Log > Session` dan cari entri sesudah penanda waktu untuk `Kania Pratiwi`
50. Verifikasi Tampil 1 entri baru sesudah penanda waktu dengan Activity "Login", Status "Failed", Note "Incorrect OTP" untuk `Kania Pratiwi`

### TC-AUTH-MFA-210: Kode OTP faktor-2 MFA tidak berlaku pada Verify Login with OTP

51. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
52. Buka halaman `Auth > Login with Password` di tab A → halaman Login with Password tampil
53. Ketik `dewianjani+{runId}-043@qwertysystem.net` pada field Email
54. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
55. Centang widget reCAPTCHA "I'm not a robot"
56. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
57. Pilih opsi "OTP via email", klik button [Login] → halaman OTP Verification tampil dan email OTP faktor-2 terkirim; catat kodenya dari mail-catcher tanpa memasukkannya
58. Di tab B buka halaman `Auth > Login with OTP > Request OTP`, ketik `dewianjani+{runId}-043@qwertysystem.net`, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP] → halaman Verify OTP tampil
59. Catat penanda waktu (baseline) Activity Log Session sebelum kode OTP faktor-2 dimasukkan
60. Ketik 6 digit kode OTP faktor-2 yang dicatat pada kotak digit Verify OTP Login with OTP
61. Verifikasi Kode ditolak: caption "Invalid code" tampil di bawah kotak digit
62. Verifikasi Tidak ada sesi yang dibuat
63. Pindah ke jendela sesi akun aktor Total Control (Global Settings), lalu buka `Global Settings > Activity Log > Session` dan cari entri sesudah penanda waktu untuk `Dewi Anjani`
64. Verifikasi Tampil 1 entri baru sesudah penanda waktu dengan Activity "Login", Status "Failed", Note "Incorrect OTP" untuk `Dewi Anjani`

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Urutan TC menyimpang dari TC sumber (191, 206, 210, 192): TC-AUTH-MFA-192 dipindah ke awal karena hanya memeriksa halaman dan mail-catcher tanpa percobaan kode salah (S-05, S-10).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal tiap TC setelah TC pertama, mencatat kode OTP dari mail-catcher, mencatat penanda waktu baseline log, mencatat baseline hitungan percobaan salah pada TC-AUTH-MFA-191, mencatat baseline jumlah email pada TC-AUTH-MFA-192, pindah ke jendela sesi akun aktor) bukan asersi tambahan (S-03).
- P-2 (pemicu bukan objek uji): tab kedua pada TC-AUTH-MFA-191, 206, dan 210 hanya sarana menerbitkan atau menampung kode lintas-purpose (kode Login with OTP dipakai di MFA, atau kode faktor-2 dipakai di Verify Login with OTP); tidak ada asersi tentang perilaku satu tab setelah tab lain bertindak, sehingga tidak dipindah ke spec multi-konteks (kelas c).
- Asersi entri log pada TC-AUTH-MFA-191 hanya memakai Status dan Note sesuai TC ("Failed", "Incorrect OTP"); kolom Activity tidak diasersi karena TC-AUTH-MFA-191 tidak menyebutnya (TC-AUTH-MFA-206 dan TC-AUTH-MFA-210 menyebut Activity "Login" pada Expected).
- Jumlah langkah melewati ±35 karena empat TC independen berprefix login faktor-1 yang identik (langkah prefix tidak dihitung); tiap TC memakai user sendiri.
- Temuan untuk QA: (1) TC-AUTH-MFA-191 Langkah 8 tidak menyebut field Email, widget reCAPTCHA, dan button [Request OTP] pada halaman Request OTP; spec memakai rincian yang sama dengan TC-AUTH-MFA-210 Langkah 7. (2) TC-AUTH-MFA-191 tidak mencantumkan akun Total Control di Precondition walau butir b menyebut pencatatan Failed; spec memakai akun aktor hook untuk mengecek Activity Log Session. (3) TC-AUTH-MFA-191 butir b klausa "dihitung sebagai percobaan salah" tidak memberi cara cek di UI dan TC tidak menyebut langkah observasinya, sehingga diasersi pada langkah 32 lewat kemampuan baca BE (hitungan percobaan salah sesi pre-auth, baseline pada langkah 26) yang disediakan tim FE/BE tanpa endpoint karangan; QA perlu menambah Expected yang teramati di UI atau menetapkan cara baca hitungan itu. TC-AUTH-MFA-206 Post Condition "Hitungan percobaan salah sesi pre-auth bertambah 1" tidak punya cara pengecekan di Langkah Uji dan tidak diasersi (Post Condition). (4) TC-AUTH-MFA-192 Langkah 9 "mail-catcher email lain" tidak menyebut alamat mana; spec memeriksa kotak masuk alamat lain di mail-catcher yang sama. (5) TC-AUTH-MFA-206 dan TC-AUTH-MFA-210 menyebut tab A dan tab B tanpa menyebut jendela; spec memakai satu jendela privat dengan dua tab. (6) TC-AUTH-MFA-192 Post Condition "Satu kode OTP aktif untuk `Dewi Rahmawati`" tidak punya cara pengecekan di Langkah Uji dan tidak diasersi. (7) TC-AUTH-MFA-206 tidak menyebut browser uji; browser mengikuti profil user (NEWDEV: browser uji B).
