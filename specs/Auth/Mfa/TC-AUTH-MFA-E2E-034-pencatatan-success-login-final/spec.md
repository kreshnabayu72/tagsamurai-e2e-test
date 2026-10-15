---
id: TC-AUTH-MFA-E2E-034-pencatatan-success-login-final
title: "Pencatatan Success Login Final MFA dan Kolom Entri Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-165
  - TC-AUTH-MFA-166
  - TC-AUTH-MFA-172
  - TC-AUTH-MFA-173
coverage:
  web: automated
---

# Pencatatan Success Login Final MFA dan Kolom Entri Log

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): empat user profil NEWDEVE (Tabel Data Uji Pre-setup #5: Activated, Active ON, seperti BASE tetapi ID device browser uji B belum ada di daftar trusted device, Authenticator sudah terdaftar; secret-nya dimuat ke aplikasi authenticator uji), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-165: `Wira Kusuma` (`wirakusuma+{runId}-034@qwertysystem.net`)
  - TC-AUTH-MFA-166: `Yoshua Simanjuntak` (`yoshuasimanjuntak+{runId}-034@qwertysystem.net`)
  - TC-AUTH-MFA-172: `Siti Santoso` (`sitisantoso+{runId}-034@qwertysystem.net`)
  - TC-AUTH-MFA-173: `Andi Santoso` (`andisantoso+{runId}-034@qwertysystem.net`)
- Aktor observer log: akun aktor Total Control (Global Settings) di atas login di browser kedua pada hook `before` dan membaca `Global Settings > Activity Log > Session` serta `Global Settings > User > Detail > User Log`. Browser pertama dipakai sebagai user uji tanpa login (halaman publik) dan dibuka di jendela privat baru tiap TC (browser uji B, ID device belum dikenali). Browser uji A (ID device dikenali) adalah profil browser reguler yang persisten, bukan jendela privat; spec ini hanya memakainya sebagai asal login sukses sebelumnya pada seeding, tidak pada langkah uji.
- Hook `after`: hapus keempat user dan tutup browser kedua. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua sesi browser bersamaan; aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik); mail-catcher lingkungan uji untuk kode OTP login (TC-AUTH-MFA-166); IP uji yang dikenal untuk asersi kolom IP Address; kemampuan klik ganda cepat pada button (TC-AUTH-MFA-172); reCAPTCHA mode uji di environment.
- Seeding state BE per user: login sukses sebelumnya dari browser uji A (device dikenali), lokasi dan waktu login terakhir, ID device browser uji B belum ada di daftar trusted device, dan Authenticator terdaftar dengan secret yang dikenal aplikasi authenticator uji; mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
- Keempat user berprofil NEWDEVE (bukan login pertama), jadi tiap login langsung menuju Choose Verification Method tanpa layar Confirm to Continue.

## Test Steps

### TC-AUTH-MFA-165: Pencatatan login final via MFA setelah Login with Password dicatat Success dengan Note Login with password

1. Buka jendela privat baru di browser pertama (tanpa sesi login)
2. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
3. Ketik `wirakusuma+{runId}-034@qwertysystem.net` pada field Email
4. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
5. Centang widget reCAPTCHA "I'm not a robot"
6. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
7. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
8. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
9. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `wirakusuma+{runId}-034@qwertysystem.net` pada kotak digit lalu klik [Login]
10. Pindah ke browser kedua (sesi Total Control Global Settings), buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Wira Kusuma` yang dibuat sesudah langkah 1 dimulai
11. Verifikasi Tampil tepat satu entri baru untuk `Wira Kusuma`: Activity `Login`, Status `Success`, Note `Login with password`, IP Address berisi IP uji
12. Buka `Global Settings > User > Detail > User Log` untuk `Wira Kusuma` dan cari entri yang dibuat sesudah langkah 1 dimulai
13. Verifikasi Tampil tepat satu entri baru: Activity `Login`, Status `Success`, Note `Login with password`, IP Address yang sama
14. Verifikasi Note mengikuti faktor pertama (bukan metode faktor-2)

### TC-AUTH-MFA-166: Pencatatan login final via MFA setelah Login with OTP dicatat Success dengan Note Login with OTP

15. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela privat baru (tanpa sesi login)
16. Buka halaman `Auth > Login with OTP > Request OTP` di browser → halaman Request OTP tampil
17. Ketik `yoshuasimanjuntak+{runId}-034@qwertysystem.net` pada field Email
18. Centang widget reCAPTCHA "I'm not a robot"
19. Klik button [Request OTP] → halaman Verify OTP tampil
20. Ketik 6 digit kode OTP login dari email `yoshuasimanjuntak+{runId}-034@qwertysystem.net` (dibaca lewat mail-catcher) pada kotak digit
21. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `yoshuasimanjuntak+{runId}-034@qwertysystem.net` pada kotak digit lalu klik [Login]
22. Pindah ke browser kedua, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Yoshua Simanjuntak` yang dibuat sesudah langkah 15 dimulai
23. Verifikasi Tampil tepat satu entri baru untuk `Yoshua Simanjuntak`: Activity `Login`, Status `Success`, Note `Login with OTP`
24. Buka `Global Settings > User > Detail > User Log` untuk `Yoshua Simanjuntak` dan cari entri yang dibuat sesudah langkah 15 dimulai
25. Verifikasi Tampil tepat satu entri baru: Activity `Login`, Status `Success`, Note `Login with OTP`
26. Verifikasi Tidak ada entri Success kedua dari faktor-1 (login-otp) untuk attempt ini pada kedua surface log

### TC-AUTH-MFA-172: Satu percobaan gagal menghasilkan tepat satu entri per surface termasuk saat klik ganda

27. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela privat baru (tanpa sesi login)
28. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
29. Ketik `sitisantoso+{runId}-034@qwertysystem.net` pada field Email
30. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
31. Centang widget reCAPTCHA "I'm not a robot"
32. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
33. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
34. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
35. Ketik 6 digit kode yang salah `000000` pada kotak digit
36. Klik button [Login] dua kali dengan cepat
37. Pindah ke browser kedua, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Siti Santoso` yang dibuat sesudah langkah 27 dimulai
38. Verifikasi Tampil tepat satu entri Failed `Incorrect OTP` baru untuk `Siti Santoso`
39. Buka `Global Settings > User > Detail > User Log` untuk `Siti Santoso` dan cari entri yang dibuat sesudah langkah 27 dimulai
40. Verifikasi Tampil tepat satu entri Failed `Incorrect OTP` baru
41. Verifikasi Tidak ada entri ganda dari klik ganda pada kedua surface log

### TC-AUTH-MFA-173: Kolom entri log login MFA pada surface log sesuai spesifikasi

42. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela privat baru (tanpa sesi login)
43. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
44. Ketik `andisantoso+{runId}-034@qwertysystem.net` pada field Email
45. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
46. Centang widget reCAPTCHA "I'm not a robot"
47. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
48. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
49. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
50. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `andisantoso+{runId}-034@qwertysystem.net` pada kotak digit lalu klik [Login]
51. Pindah ke browser kedua, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Andi Santoso` yang dibuat sesudah langkah 42 dimulai serta perhatikan header
52. Verifikasi `Global Settings > Activity Log > Session` menampilkan kolom: Date, User, Employee ID, Position, Division, Activity, Status, Note, IP Address
53. Verifikasi Entri baru untuk `Andi Santoso`: Activity `Login`, Status `Success`
54. Buka `Global Settings > User > Detail > User Log` untuk `Andi Santoso` dan cari entri yang dibuat sesudah langkah 42 dimulai serta perhatikan header
55. Verifikasi `Global Settings > User > Detail > User Log` menampilkan kolom: Date, Activity, Status, Note, IP Address
56. Verifikasi Entri baru: Activity `Login`, Status `Success`

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Kelas harness: pencatatan (Status/Note spesifik) dibaca lewat akun aktor di browser kedua; asersi absence ada di spec `TC-AUTH-MFA-E2E-035`. TC-AUTH-MFA-172 (Failed) ditaruh di spec ini sesuai pembagian rencana karena asersinya adalah jumlah entri ("tepat satu"), bukan absence. TC-AUTH-MFA-166 memakai Login with OTP sebagai faktor-1 dengan mail-catcher hanya untuk mengambil kode OTP login.
- TC-AUTH-MFA-22 dan 23 tidak ada di spec ini; seluruh Expected keduanya dicakup spec `TC-AUTH-MFA-E2E-019-evaluasi-single-step-tanpa-mfa`. Post Condition keduanya ("entri Success ditulis oleh faktor-1") tidak punya langkah observasi di TC dan tidak diasersi (lihat "Temuan untuk QA").
- Urutan mengikuti TC sumber. Tiap TC memakai user sendiri, jadi urutan antar TC tidak saling bergantung.
- Melewati ±35 langkah (56 langkah, ±41 netto setelah langkah prefix login faktor-1 tidak dihitung) karena empat TC pencatatan yang masing-masing membaca dua surface log; tiap TC independen (user dan jendela privat sendiri, entri log dibatasi penanda waktu TC itu), sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal dan spec tidak dipecah.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): buka jendela privat baru dan perpindahan antar browser pertama dan kedua di awal tiap TC. Entri "baru" dibedakan dari entri seeding lewat stempel waktu: hanya entri yang dibuat sesudah langkah pembuka jendela privat TC itu dimulai yang dihitung.
- Temuan untuk QA:
  - Seluruh TC di spec ini menulis "password valid `Nama User`" pada Langkah Uji; spec memakai `Spectra.env.MFA_PASSWORD` sebagai password valid user seeding.
  - TC-AUTH-MFA-166 Langkah Uji 5 dan 6 tidak menyebut tombol atau transisi setelah kode OTP login diketik, dan tidak menyebut halaman Authenticator Verification sebelum kode TOTP diketik; spec mengikuti Langkah Uji apa adanya (PRD `AUTHMFA-LOGIC-03` menetapkan faktor-1 OTP langsung menuju Authenticator Verification).
  - TC-AUTH-MFA-165 Expected butir c: "tidak ada Note di luar enum kanon" tidak dapat diasersi karena enum Note tidak dirinci di TC; spec hanya mengasersi Note `Login with password` dan bahwa Note mengikuti faktor pertama. Perlu daftar enum Note di TC.
  - TC-AUTH-MFA-22 dan TC-AUTH-MFA-23 Post Condition "entri Success Login with password / Login with OTP ditulis oleh faktor-1 (bukan MFA)" tidak punya Expected padanan maupun langkah observasi di Langkah Uji, dan pembeda penulis entri tidak terlihat di UI; tidak diasersi di spec mana pun. Perlu Expected atau langkah observasi di TC bila ingin diuji.
  - Mekanisme seeding state BE per user (login sebelumnya dari browser uji A, lokasi dan waktu login terakhir, Authenticator terdaftar dengan secret yang dikenal authenticator uji) belum ada di Pre-setup (#20/#21) TC.
  - TC-AUTH-MFA-172 Expected tidak menyebut apakah halaman Authenticator Verification menampilkan caption `Invalid code`; tidak diasersi.
