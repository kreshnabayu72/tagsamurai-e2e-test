---
id: TC-AUTH-MFA-E2E-010-validasi-kode-authenticator-dan-state-ui
title: "Validasi Kode Authenticator dan State UI Halaman Authenticator Verification"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-94
  - TC-AUTH-MFA-95
  - TC-AUTH-MFA-93
  - TC-AUTH-MFA-09
  - TC-AUTH-MFA-92
coverage:
  web: automated
---

# Validasi Kode Authenticator dan State UI Halaman Authenticator Verification

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): lima user profil NEWDEVE (Tabel Data Uji Pre-setup #5: Activated, Active ON, sudah pernah login sukses di web dari browser uji A (device dikenali), login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari, Authenticator sudah terdaftar dengan secret yang diketahui aplikasi authenticator uji), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-94: `Tito Wahyudi` (`titowahyudi+{runId}-010@qwertysystem.net`)
  - TC-AUTH-MFA-95: `Umar Faruq` (`umarfaruq+{runId}-010@qwertysystem.net`)
  - TC-AUTH-MFA-93: `Salsa Dewi` (`salsadewi+{runId}-010@qwertysystem.net`)
  - TC-AUTH-MFA-09: `Fajar Nugroho` (`fajarnugroho+{runId}-010@qwertysystem.net`)
  - TC-AUTH-MFA-92: `Rafi Mahendra` (`rafimahendra+{runId}-010@qwertysystem.net`)
- Hook `after`: hapus kelima user dan tutup semua jendela privat. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah TC pertama dimulai di jendela privat baru. TC pertama berjalan di browser awal; browser awal dan tiap jendela privat tanpa ID device tersimpan, dikenali sebagai browser uji B. Login dari IP uji Jakarta (ID) hanya memicu MFA karena device baru. Semua user berprofil NEWDEVE, jadi tiap login Password melewati Choose Verification Method tanpa layar Confirm to Continue.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture. Kode salah `000000` dan `123` adalah input uji yang submit-nya diblokir, ditulis literal.
- Kemampuan teknis: jendela privat; reCAPTCHA mode uji di environment; aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) yang memegang secret user seeding untuk menghasilkan kode valid (TC-AUTH-MFA-92); pemantau request jaringan untuk memastikan tidak ada request verifikasi (TC-AUTH-MFA-92).
- Kemampuan teknis, seeding state BE per user: status Activated dan Active ON, trusted device ber-ID device browser uji A (device dikenali), lokasi dan waktu login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari, consent sudah disetujui sehingga tanpa layar Confirm to Continue, dan Authenticator terdaftar dengan secret yang diketahui aplikasi authenticator uji. Mekanisme seeding (endpoint atau skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
- Jeda nyata: TC-AUTH-MFA-92 menunggu 5 detik tanpa mengklik apa pun (langkah 62), jeda pendek di bawah 30 detik sesuai konvensi bagian 6.

## Test Steps

### TC-AUTH-MFA-94: Klik [Login] pada Authenticator Verification tanpa mengisi kode

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `titowahyudi+{runId}-010@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
6. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
7. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
8. Klik button [Login] tanpa mengisi kotak digit
9. Verifikasi Tidak ada sesi yang dibuat
10. Verifikasi Halaman tetap Authenticator Verification
11. Verifikasi Caption error di bawah kotak digit: "Code must not be empty"

### TC-AUTH-MFA-95: Klik [Login] pada Authenticator Verification sebelum 6 digit terisi

12. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
13. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
14. Ketik `umarfaruq+{runId}-010@qwertysystem.net` pada field Email
15. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
16. Centang widget reCAPTCHA "I'm not a robot"
17. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
18. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
19. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
20. Ketik 3 digit kode `123` pada kotak digit
21. Klik button [Login]
22. Verifikasi Tidak ada sesi yang dibuat
23. Verifikasi Halaman tetap Authenticator Verification
24. Verifikasi Caption error di bawah kotak digit: "Code must not be empty" (kode parsial didefinisikan sama dengan kosong)

### TC-AUTH-MFA-93: Verifikasi Authenticator dengan kode salah

25. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
26. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
27. Ketik `salsadewi+{runId}-010@qwertysystem.net` pada field Email
28. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
29. Centang widget reCAPTCHA "I'm not a robot"
30. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
31. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
32. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
33. Ketik 6 digit kode salah `000000` pada kotak digit
34. Klik button [Login]
35. Verifikasi Caption error di bawah kotak digit: "Invalid code"
36. Verifikasi Keenam kotak dikosongkan (field di-clear)
37. Verifikasi Tidak ada sesi yang dibuat
38. Verifikasi Tidak ada tautan recovery code

### TC-AUTH-MFA-09: Slot SegmentedInput berstatus Invalid setelah kode Authenticator salah

39. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
40. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
41. Ketik `fajarnugroho+{runId}-010@qwertysystem.net` pada field Email
42. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
43. Centang widget reCAPTCHA "I'm not a robot"
44. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
45. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
46. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
47. Ketik 6 digit kode salah `000000` pada kotak digit
48. Klik button [Login]
49. Verifikasi Keenam kotak berwarna severity danger (Invalid State)
50. Verifikasi Alert pesan di bawah kotak digit: "Invalid code"
51. Verifikasi Halaman tetap Authenticator Verification
52. Verifikasi Tidak ada sesi yang dibuat

### TC-AUTH-MFA-92: Authenticator Verification tidak auto-submit saat digit ke-6 terisi

53. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
54. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
55. Ketik `rafimahendra+{runId}-010@qwertysystem.net` pada field Email
56. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
57. Centang widget reCAPTCHA "I'm not a robot"
58. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
59. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
60. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
61. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `rafimahendra+{runId}-010@qwertysystem.net` pada kotak digit
62. Tunggu 5 detik tanpa mengklik apa pun
63. Verifikasi Keenam kotak terisi
64. Verifikasi Tidak ada request verifikasi yang berjalan
65. Verifikasi Halaman tetap Authenticator Verification
66. Verifikasi Button [Login] enabled

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Urutan mengikuti rencana: seluruh TC di spec ini diblokir (tidak ada yang membuat sesi), sehingga tidak ada penyimpangan urutan. TC-AUTH-MFA-92 di akhir karena satu-satunya yang mengetik kode valid (tidak dikirim).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal tiap TC kecuali TC pertama) bukan asersi tambahan (S-03, S-09).
- Jumlah langkah melewati ±35 karena lima TC independen, masing-masing dengan user dan jendela privat sendiri; langkah prefix login faktor-1 yang identik tidak dihitung, sehingga spec tidak dipecah. TC-AUTH-MFA-12 ada di spec TC-AUTH-MFA-E2E-056.
- Pencatatan pada Post Condition TC-AUTH-MFA-94, 95, 93, 09 (Failed `Empty OTP` atau `Incorrect OTP`) tidak diasersikan di spec ini; asersi pencatatan berada di spec pencatatan.
- Temuan untuk QA: (1) TC-AUTH-MFA-09 butir a ("keenam kotak berwarna severity danger") dan TC-AUTH-MFA-93 butir b ("keenam kotak dikosongkan") menyatakan state kotak berbeda untuk skenario yang sama (kode `000000` salah pada Authenticator Verification); tidak jelas apakah kotak tetap terisi berwarna danger atau langsung dikosongkan. Spec mengikuti masing-masing TC apa adanya (S-15). (2) TC-AUTH-MFA-92 butir a ("tidak ada request verifikasi") tidak punya cara pengecekan di Langkah Uji; dicek lewat pemantau request jaringan (Prerequisites). (3) Post Condition "tidak ada entri log" pada TC-AUTH-MFA-92 tidak punya Expected padanan maupun langkah observasi di TC, dan TC itu tidak masuk spec absence; tidak diasersi di spec (S-01, S-05, S-15). QA perlu menambah Expected atau langkah observasi ke TC bila ketiadaan entri log itu harus diuji. (4) Pre-setup TC (#20/#21) belum memuat mekanisme seeding state BE per user (trusted device ber-ID device browser A, lokasi dan waktu login terakhir, secret authenticator yang dikenal authenticator uji, consent, logout web terakhir); mekanisme seed disediakan tim FE/BE.
