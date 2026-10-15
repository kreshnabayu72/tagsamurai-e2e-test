---
id: TC-AUTH-MFA-E2E-002-routing-metode-faktor-kedua
title: "Routing Pemilihan Metode Faktor Kedua"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-53
  - TC-AUTH-MFA-55
  - TC-AUTH-MFA-56
  - TC-AUTH-MFA-57
  - TC-AUTH-MFA-58
  - TC-AUTH-MFA-60
coverage:
  web: automated
---

# Routing Pemilihan Metode Faktor Kedua

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): enam user, password `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Semua user sudah pernah login sukses di web (tanpa layar Confirm to Continue); TC pertama berjalan di browser awal; browser awal dan tiap jendela privat tanpa ID device tersimpan, dikenali sebagai browser uji B; login dari browser uji B memicu MFA karena ID device belum ada di daftar trusted device.
  - Profil NEWDEV (Tabel Data Uji Pre-setup #4: Activated, Active ON, Authenticator belum terdaftar):
    - TC-AUTH-MFA-53: `Ika Purwanti` (`ikapurwanti+{runId}-002@qwertysystem.net`)
    - TC-AUTH-MFA-56: `Galih Saputro` (`galihsaputro+{runId}-002@qwertysystem.net`)
    - TC-AUTH-MFA-58: `Slamet Riyadi` (`slametriyadi+{runId}-002@qwertysystem.net`)
  - Profil NEWDEVE (Tabel Data Uji Pre-setup #5: seperti NEWDEV, Authenticator sudah terdaftar):
    - TC-AUTH-MFA-55: `Retno Wardani` (`retnowardani+{runId}-002@qwertysystem.net`)
    - TC-AUTH-MFA-57: `Mira Handoko` (`mirahandoko+{runId}-002@qwertysystem.net`)
    - TC-AUTH-MFA-60: `Arif Budiman` (`arifbudiman+{runId}-002@qwertysystem.net`)
- Hook `after`: hapus keenam user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah TC pertama dimulai di jendela privat baru.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Jendela privat; reCAPTCHA mode uji di environment.
  - Mail-catcher lingkungan uji untuk membaca kode OTP login (TC-AUTH-MFA-55) dan memastikan email OTP faktor-2 baru diterima (TC-AUTH-MFA-56), dengan baseline jumlah email untuk `galihsaputro+{runId}-002@qwertysystem.net` dicatat sebelum aksi yang diamati.
  - Seeding state BE per user: riwayat login web sukses dengan trusted device ber-ID device browser uji A untuk keenam user, dan enrollment Authenticator aktif untuk ketiga user profil NEWDEVE; mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - Jeda nyata ≤30 detik: menunggu toast hilang otomatis 4 detik (langkah 40).

## Test Steps

### TC-AUTH-MFA-53: Faktor-1 Password menampilkan halaman pilihan faktor kedua

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `ikapurwanti+{runId}-002@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
6. Verifikasi Halaman Choose Verification Method menampilkan opsi "OTP via email" dan "Authenticator app"
7. Verifikasi Tidak ada opsi lain

### TC-AUTH-MFA-60: Pilihan Choose Verification Method identik saat alasan MFA adalah login tak biasa

8. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
9. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
10. Ketik `arifbudiman+{runId}-002@qwertysystem.net` pada field Email
11. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
12. Centang widget reCAPTCHA "I'm not a robot"
13. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
14. Verifikasi Opsi "OTP via email" dan "Authenticator app" tampil sama dengan alasan MFA lain
15. Verifikasi Title "Choose verification method" sama dengan alasan MFA lain
16. Verifikasi Subtitle "Select how you'd like to verify your identity" sama dengan alasan MFA lain
17. Verifikasi Tidak ada teks atau opsi yang menyebut alasan MFA (device baru)

### TC-AUTH-MFA-55: Faktor-1 OTP melewati halaman pilihan dan langsung ke Authenticator Verification

18. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
19. Buka halaman `Auth > Login with OTP > Request OTP` di browser → halaman Request OTP tampil
20. Ketik `retnowardani+{runId}-002@qwertysystem.net` pada field Email
21. Centang widget reCAPTCHA "I'm not a robot"
22. Klik button [Request OTP] → halaman Verify OTP tampil
23. Ketik 6 digit kode OTP login dari email `retnowardani+{runId}-002@qwertysystem.net` pada kotak digit
24. Verifikasi Halaman Choose Verification Method tidak tampil
25. Verifikasi Halaman `Auth > MFA > Authenticator Verification` tampil langsung karena Authenticator sudah terdaftar

### TC-AUTH-MFA-56: Memilih OTP via email membuka OTP Verification dan mengirim kode ke email akun

26. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
27. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
28. Ketik `galihsaputro+{runId}-002@qwertysystem.net` pada field Email
29. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
30. Centang widget reCAPTCHA "I'm not a robot"
31. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
32. Pilih opsi "OTP via email" pada halaman Choose Verification Method
33. Catat jumlah email di mail-catcher untuk `galihsaputro+{runId}-002@qwertysystem.net` sebagai baseline
34. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `galihsaputro+{runId}-002@qwertysystem.net`
35. Verifikasi Halaman `Auth > MFA > OTP Verification` tampil
36. Verifikasi Email OTP faktor-2 diterima di `galihsaputro+{runId}-002@qwertysystem.net` (jumlah email bertambah satu dari baseline)
37. Verifikasi Subtitle halaman: "We sent a code to galihsaputro+{runId}-002@qwertysystem.net"
38. Verifikasi Toast sukses: "Success, the code has been sent." tampil
39. Verifikasi Toast tampil di kanan bawah
40. Verifikasi Toast hilang otomatis setelah 4 detik

### TC-AUTH-MFA-57: Memilih Authenticator app dengan enrollment aktif membuka Authenticator Verification

41. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
42. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
43. Ketik `mirahandoko+{runId}-002@qwertysystem.net` pada field Email
44. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
45. Centang widget reCAPTCHA "I'm not a robot"
46. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
47. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
48. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
49. Verifikasi Halaman `Auth > MFA > Authenticator Verification` tampil
50. Verifikasi Halaman Enrollment tidak tampil

### TC-AUTH-MFA-58: Memilih Authenticator app tanpa enrollment aktif membuka Enrollment Authenticator

51. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
52. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
53. Ketik `slametriyadi+{runId}-002@qwertysystem.net` pada field Email
54. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
55. Centang widget reCAPTCHA "I'm not a robot"
56. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
57. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
58. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
59. Verifikasi Halaman `Auth > MFA > Enrollment Authenticator` tampil
60. Verifikasi Halaman Authenticator Verification tidak tampil

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal tiap TC setelah TC pertama; langkah 33 mencatat baseline jumlah email TC-AUTH-MFA-56) bukan asersi tambahan (S-03, S-12).
- Penyimpangan urutan (S-05, S-10): TC-AUTH-MFA-60 ditaruh tepat setelah TC-AUTH-MFA-53 karena keduanya hanya screening halaman Choose Verification Method; TC-AUTH-MFA-55 sampai TC-AUTH-MFA-58 (routing yang menindaklanjuti pilihan) menyusul sesuai urutan TC sumber.
- Browser/jendela privat berbeda dipakai berurutan hanya untuk membentuk identitas device (browser uji B), tanpa asersi lintas jendela; bukan konteks kedua (tidak butuh butir P-2).
- Temuan untuk QA: (1) TC-AUTH-MFA-60 Expected "title dan subtitle sama" tidak menyebut teksnya; spec memakai Title dan Subtitle dari TC-AUTH-MFA-01 (S-02, S-15). (2) Post Condition tanpa langkah observasi dan tanpa Expected padanan tidak diasersi di spec (S-01, S-15): TC-AUTH-MFA-53, 55, 57, 58, 60 "Sesi pre-auth MFA aktif untuk <user>" (teramati sebagai halaman MFA tampil, sudah menjadi `Verifikasi` Expected); TC-AUTH-MFA-56 "Satu kode OTP aktif untuk `Galih Saputro`; hitungan resend 0"; TC-AUTH-MFA-57 "tidak ada email OTP faktor-2 terkirim"; TC-AUTH-MFA-58 "Secret Authenticator pending dibuat untuk sesi pre-auth ini; enrollment belum aktif". Perlu Expected atau langkah observasi di TC bila Post itu hendak diasersi. (3) TC-AUTH-MFA-55 Langkah Uji tidak menyebut kode OTP login dibaca dari mail-catcher; dilengkapi di Prerequisites. (4) Data Uji "browser uji B" pada TC-AUTH-MFA-53, 56, 57, 58, 60 diwujudkan sebagai jendela privat baru (ID device belum dikenali). (5) Mekanisme seed state BE (trusted device ber-ID device browser uji A, enrollment Authenticator aktif) belum ada di Pre-setup (#20/#21); spec tidak menyebut endpoint karangan (S-11, S-13).
